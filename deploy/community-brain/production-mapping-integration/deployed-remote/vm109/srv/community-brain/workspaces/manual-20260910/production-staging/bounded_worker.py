"""One-shot production rehearsal: exactly two synthetic processing stages."""

import asyncio
import hashlib
import json
import os
import ssl
from pathlib import Path
from uuid import UUID

import httpx
import nats
from community_brain.jobs.models import Job, ModelCall, Outbox, Source, Stage
from community_brain.jobs.runtime import make_store
from community_brain.jobs.worker import OpenRouter, Worker
from community_brain.processing.pipeline import OutcomeUnknown
from sqlalchemy import select
from sqlalchemy.orm import Session

STREAM = "COMMUNITY_BRAIN_PROD"
SUBJECT = "cbm.prod.jobs.stage.ready.v1"
MEETING = "production-synthetic-20260910"
CEILING = 12  # Per job, at most 24 requests for the two-job exercise.


def connection_options(env):
    if env["CB_NATS_URL"] != "tls://platform-events.patchoutech.lab:4223":
        raise ValueError("Unexpected production queue endpoint")
    return {
        "servers": env["CB_NATS_URL"],
        "user": env["CB_NATS_USER"],
        "password": env["CB_NATS_PASSWORD"],
        "tls": ssl.create_default_context(cafile="/run/certs/ca-bundle.pem"),
        "tls_handshake_first": True,
        "inbox_prefix": b"_INBOX.cbm_prod_worker",
        "allow_reconnect": False,
        "connect_timeout": 10,
    }


def validate_job(session, store, job, mode, fixture):
    if not job or job.scope != "community-brain" or job.mode != mode:
        raise ValueError("Unapproved job")
    if job.identity != {
        "meeting_id": MEETING,
        "started_at": "2026-09-10T00:00:00Z",
        "timezone": "Etc/UTC",
        "local_date": "2026-09-10",
        "provider": "manual",
    }:
        raise ValueError("Unexpected synthetic identity")
    kinds = {"transcript", "chat"} if mode == "weekly" else {"transcript"}
    if set(job.sources) != kinds | ({"aliases"} if store.aliases_supplier else set()):
        raise ValueError("Unexpected sources")
    for kind, source_id in job.sources.items():
        source = session.get(Source, UUID(source_id))
        expected = (
            store.aliases_supplier() if kind == "aliases" else fixture[kind]
        ).encode()
        if (
            not source
            or source.scope != job.scope
            or source.meeting_id != MEETING
            or source.kind != kind
            or source.sha256 != hashlib.sha256(expected).hexdigest()
            or store.storage.read(source.path, source.sha256) != expected
        ):
            raise ValueError("Nonfixture source rejected")
    stage = session.scalar(
        select(Stage).where(Stage.job_id == job.id, Stage.name == "processing")
    )
    if (
        not stage
        or stage.state != "queued"
        or stage.attempts != 0
        or stage.generation != 1
    ):
        raise ValueError("No replay or retry authorized")
    if session.scalar(select(ModelCall.id).where(ModelCall.job_id == job.id).limit(1)):
        raise ValueError("Previous model intent requires review")
    return stage


class BoundedProvider(OpenRouter):
    def __init__(self, key):
        super().__init__(key)
        self.calls = 0

    def __call__(self, request):
        if self.calls >= CEILING:
            raise OutcomeUnknown("bounded request ceiling reached")
        try:
            response = httpx.get(
                "https://openrouter.ai/api/v1/key",
                headers={"Authorization": "Bearer " + self.api_key},
                timeout=20,
            )
            response.raise_for_status()
            data = response.json()["data"]
            if not (
                data["limit"] == 2
                and data["limit_reset"] is None
                and data["limit_remaining"] > 0
                and data["is_management_key"] is False
                and data["include_byok_in_limit"] is True
            ):
                raise ValueError("Incorrect production allowance")
        except (httpx.HTTPError, ValueError, KeyError, TypeError) as exc:
            raise OutcomeUnknown("production allowance uncertain") from exc
        self.calls += 1
        return super().__call__(request)


async def run(store, manifest, fixture, connect, provider_factory):
    if set(manifest) != {"weekly", "transcript_backfill"}:
        raise ValueError("Exactly two explicit job IDs required")
    ids = {mode: UUID(value) for mode, value in manifest.items()}
    if len(set(ids.values())) != 2:
        raise ValueError("Distinct jobs required")
    # Validate both before connecting or creating a provider request.
    approved = {}
    with Session(store.engine) as session:
        for mode, job_id in ids.items():
            stage = validate_job(
                session, store, session.get(Job, job_id), mode, fixture
            )
            event = session.scalar(
                select(Outbox).where(
                    Outbox.stage_id == stage.id, Outbox.generation == 1
                )
            )
            if not event or event.sent_at is not None:
                raise ValueError(
                    "Previously dispatched or missing event requires review"
                )
            approved[mode] = (stage.id, event.id, event.created_at.isoformat())
    nc = await connect()
    try:
        js = nc.jetstream()
        sub = await js.pull_subscribe_bind("community-brain-worker", stream=STREAM)
        for mode, job_id in ids.items():
            stage_id, event_id, created = approved[mode]
            body = {
                "schema_version": 1,
                "event_id": str(event_id),
                "stage_id": str(stage_id),
                "generation": 1,
                "job_id": str(job_id),
                "occurred_at": created,
                "trace_id": str(event_id),
            }
            await js.publish(
                SUBJECT,
                json.dumps(body).encode(),
                headers={"Nats-Msg-Id": str(event_id)},
            )
            with Session(store.engine) as session, session.begin():
                session.get(Outbox, event_id).sent_at = store.now(session)
            message = (await sub.fetch(1, timeout=10))[0]
            if json.loads(message.data) != body:
                await message.nak(delay=60)
                raise ValueError("Unexpected queue work; no handling authorized")
            worker = Worker(
                store, provider_factory()
            )  # No indexing/publishing/acquisition handlers.
            await worker.handle(message)
            with Session(store.engine) as session:
                stage = session.get(Stage, stage_id)
                job = session.get(Job, job_id)
                if stage.state != "succeeded" or job.processing != "succeeded":
                    raise RuntimeError(
                        "Processing incomplete; explicit review required"
                    )
                print(
                    json.dumps(
                        {
                            "job_id": str(job_id),
                            "mode": mode,
                            "processing": job.processing,
                        }
                    ),
                    flush=True,
                )
    finally:
        await nc.close()


def main():
    if (
        os.environ.get("CB_ENABLE_MODEL_CALLS") != "true"
        or os.environ.get("CB_ENABLE_NETWORK_PUBLICATION") != "false"
    ):
        raise ValueError("Incorrect bounded enablement")
    if any(
        os.environ.get(k)
        for k in ("CB_FATHOM_API_KEY", "CB_GITHUB_TOKEN", "CB_GIT_REMOTE")
    ):
        raise ValueError("Unrelated credential rejected")
    root = Path("/checks")
    manifest = json.loads(Path("/approval/jobs.json").read_text())
    fixture = json.loads((root / "synthetic-fixture.json").read_text())
    options = connection_options(os.environ)
    asyncio.run(
        run(
            make_store(),
            manifest,
            fixture,
            lambda: nats.connect(**options),
            lambda: BoundedProvider(os.environ["CB_OPENROUTER_API_KEY"]),
        )
    )


if __name__ == "__main__":
    main()

"""Consume exactly one approved processing stage with the real durable worker."""

import asyncio
import json
import os
import sys
import time
from pathlib import Path
from uuid import UUID

import httpx
import nats
from community_brain.jobs.models import Attempt, Job, ModelCall, Stage
from community_brain.jobs.publication import PublicationHandlers
from community_brain.jobs.runtime import make_store
from community_brain.jobs.worker import OpenRouter, Worker, dispatch
from community_brain.llm import LLMOutcomeUnknown
from community_brain.processing.pipeline import OutcomeUnknown
from sqlalchemy import select
from sqlalchemy.orm import Session


class BoundedOpenRouter(OpenRouter):
    calls = 0
    ceiling = 12

    def __call__(self, request):
        if self.calls >= self.ceiling:
            raise OutcomeUnknown("development request count guard reached")
        try:
            response = httpx.get(
                "https://openrouter.ai/api/v1/key",
                headers={"Authorization": "Bearer " + self.api_key},
                timeout=20,
            )
            response.raise_for_status()
            data = response.json()["data"]
            assert data["limit"] == 5 and data["limit_reset"] is None
            assert data["limit_remaining"] > 0 and data["is_management_key"] is False
            assert data["include_byok_in_limit"] is True
        except Exception as error:
            raise OutcomeUnknown("development allowance uncertain") from error
        self.calls += 1
        return super().__call__(request)


def audit_ingestion(
    store, *, journal_path="/state/files/live-indexing-calls.jsonl", ceiling=16
):
    """Real HTTP requests with allowance checks and private intent/usage receipts."""
    from community_brain import llm

    original_post = llm.httpx.post
    journal = Path(journal_path)
    if journal.exists():
        raise RuntimeError("Previous indexing intents require review")
    count = 0

    def record(value):
        with journal.open("a") as stream:
            stream.write(json.dumps(value, sort_keys=True) + "\n")
            stream.flush()
            os.fsync(stream.fileno())

    def post(url, **kwargs):
        nonlocal count
        assert url == llm.OPENROUTER_URL
        if count >= ceiling:
            raise LLMOutcomeUnknown("development request ceiling reached")
        response = httpx.get(
            "https://openrouter.ai/api/v1/key",
            headers={"Authorization": "Bearer " + os.environ["CB_OPENROUTER_API_KEY"]},
            timeout=20,
        )
        try:
            response.raise_for_status()
            allowance = response.json()["data"]
            assert allowance["limit"] == 5 and allowance["limit_reset"] is None
            assert (
                allowance["limit_remaining"] > 0
                and allowance["is_management_key"] is False
            )
            assert allowance["include_byok_in_limit"] is True
        except Exception as error:
            raise LLMOutcomeUnknown("allowance uncertain") from error
        count += 1
        record(
            {
                "request": count,
                "state": "intent",
                "model": kwargs["json"]["model"],
                "time": time.time(),
            }
        )
        try:
            response = original_post(url, **kwargs)
            response.raise_for_status()
            body = response.json()
            path, sha, _ = store.storage.put(json.dumps(body).encode())
            record(
                {
                    "request": count,
                    "state": "response",
                    "response_path": path,
                    "sha256": sha,
                    "usage": body.get("usage"),
                }
            )
        except Exception as error:
            raise LLMOutcomeUnknown(
                "indexing response or receipt is uncertain"
            ) from error
        return response

    llm.httpx.post = post


def verify_approved_recording(job, *, weekly=False):
    assert job.scope == "community-brain-dev"
    assert job.identity["meeting_id"] == "181075701"
    assert job.identity["started_at"] == "2026-09-08T21:54:33Z"
    assert str(job.parent_id) == "33cc7538-e326-4f74-93ef-f2fcbb5c1624"
    assert job.mode == ("weekly" if weekly else "transcript_backfill")
    assert job.sources["transcript"] == "27969d75-10a9-4a46-8cf4-b63d1d7035d9"
    if weekly:
        assert job.sources.get("chat") == "23d9780b-513e-4782-96d2-97211e31e855"
    else:
        assert not job.sources.get("chat")


async def main():
    assert os.environ["CB_ENABLE_MODEL_CALLS"] == "true"
    assert os.environ["CB_ENABLE_NETWORK_PUBLICATION"] == "false"
    job_id = UUID(sys.argv[1])
    operation = sys.argv[2] if len(sys.argv) > 2 else "processing"
    weekly_index = operation == "approved-weekly-index"
    approved_weekly = operation in ("approved-weekly", "approved-weekly-index")
    approved_index = operation in ("approved-index", "approved-weekly-index")
    approved_backfill = operation in (
        "approved-backfill",
        "approved-index",
        "approved-weekly",
        "approved-weekly-index",
    )
    if approved_backfill:
        operation = "indexing" if approved_index else "processing"
    assert operation in ("processing", "indexing")
    store = make_store()
    with Session(store.engine) as session:
        job = session.get(Job, job_id)
        assert job.scope == "community-brain-dev"
        if approved_backfill:
            verify_approved_recording(job, weekly=approved_weekly)
        else:
            assert job.identity["meeting_id"] == "live-development-synthetic-20260909"
            assert job.mode == "weekly"
        stage = session.scalar(
            select(Stage).where(Stage.job_id == job_id, Stage.name == operation)
        )
        assert stage.state == "queued", (
            "No automatic retry/reconciliation of a previous exercise"
        )
        if approved_index:
            assert stage.attempts == 0 and stage.generation == 1
        if stage.attempts:
            assert (
                operation == "indexing"
                and stage.attempts == 1
                and stage.generation == 2
            )
            authorization = session.scalar(
                select(Attempt).where(
                    Attempt.stage_id == stage.id,
                    Attempt.state == "retry_authorized",
                    Attempt.fence == -stage.generation,
                )
            )
            assert authorization is not None, "Explicit API reconciliation is required"
            assert (
                authorization.reason
                == "Development initialization repaired; no indexing requests recorded; operator approves reconciliation"
            )
        if operation == "processing":
            assert (
                session.scalar(
                    select(ModelCall.id).where(ModelCall.job_id == job_id).limit(1)
                )
                is None
            )
        else:
            assert job.processing == "succeeded"
        stage_id = stage.id
    if weekly_index:
        assert str(job_id) == "7bce1799-dd0f-40fa-a444-a7797ff38b1b"
        assert os.environ.get("CB_WEEKLY_ISOLATED_INDEX") == "true"
        assert (
            Path(os.environ["CB_CORPUS_ROOT"]) / "approved-weekly-isolated"
        ).read_text().strip() == str(job_id)
    if operation == "indexing":
        from community_brain.ingestion.config_loader import (
            load_chunking_config,
            load_extraction_config,
        )

        config = Path(os.environ["CB_PIPELINE_CONFIG_DIR"])
        load_chunking_config(config / "chunking.yaml")
        extraction = load_extraction_config(config / "extraction-config.yaml")
        for name in (
            extraction.chunk_extraction_prompt_file,
            extraction.session_themes_prompt_file,
        ):
            assert (config / "extraction-prompts" / name).is_file()
        assert (config / "entity-registry.yaml").is_file()
    provider = BoundedOpenRouter(os.environ["CB_OPENROUTER_API_KEY"])
    if approved_weekly:
        provider.ceiling = 20
    worker = Worker(store, provider)
    if operation == "indexing":
        os.environ["OPENROUTER_API_KEY"] = os.environ["CB_OPENROUTER_API_KEY"]
        audit_ingestion(
            store,
            journal_path="/state/files/weekly-indexing-calls.jsonl"
            if weekly_index
            else "/state/files/recording-indexing-calls.jsonl"
            if approved_index
            else "/state/files/live-indexing-calls.jsonl",
            ceiling=31 if weekly_index else 30 if approved_index else 16,
        )
        handlers = PublicationHandlers(
            store,
            os.environ["CB_CORPUS_ROOT"],
            os.environ["CB_PIPELINE_CONFIG_DIR"],
            os.environ["OLLAMA_BASE_URL"],
        )
        worker.handlers = {"indexing": handlers.indexing}
    connection = await nats.connect(os.environ["CB_NATS_URL"])
    try:
        js = connection.jetstream()
        subscription = await js.pull_subscribe_bind(
            "community-brain-worker", stream="CB_DEV_JOBS"
        )
        await dispatch(store, js, "cb.dev.jobs")
        from acquisition_worker import terminal_duplicate
        from community_brain.jobs.models import Outbox

        for _ in range(10):
            message = (await subscription.fetch(1, timeout=10))[0]
            envelope = json.loads(message.data)
            if envelope["job_id"] == str(job_id) and envelope["stage_id"] == str(
                stage_id
            ):
                break
            with Session(store.engine) as session:
                terminal = terminal_duplicate(
                    session.get(Stage, UUID(envelope["stage_id"])),
                    session.get(Outbox, UUID(envelope["event_id"])),
                    envelope,
                )
            if not terminal:
                await message.nak(delay=60)
                raise RuntimeError("Unrelated active work; no processing started")
            await message.ack_sync()
        else:
            raise RuntimeError("Duplicate notification limit reached")
        await worker.handle(message)
        with Session(store.engine) as session:
            job = session.get(Job, job_id)
            calls = session.scalars(
                select(ModelCall).where(ModelCall.job_id == job_id)
            ).all()
            print(
                json.dumps(
                    {
                        "job_id": str(job_id),
                        "processing": job.processing,
                        "indexing": job.indexing,
                        "artifacts": job.artifacts,
                        "calls": [
                            {
                                "state": call.state,
                                "request": call.request_meta,
                                "usage": call.usage,
                            }
                            for call in calls
                        ],
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            if getattr(job, operation) not in ("succeeded", "complete"):
                raise RuntimeError(
                    "Stage did not complete; inspect state before any retry"
                )
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())

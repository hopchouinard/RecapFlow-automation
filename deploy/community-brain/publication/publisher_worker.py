"""Reviewed publication oneshot. No daemon, model credentials or corpus writes."""

import asyncio
from datetime import datetime, timezone, timedelta
import json
import os
from pathlib import Path
import sys
from uuid import UUID

import nats
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from community_brain.jobs.github_release import GitHubRelease
from community_brain.jobs.manual import run_selected
from community_brain.jobs.models import Artifact, Job, Stage
from community_brain.jobs.prepared_publication import (
    PreparedGit,
    PreparedPublication,
    record,
)
from community_brain.jobs.publication_selection import selection, six_files
from community_brain.jobs.storage import Storage
from community_brain.jobs.store import Store, fingerprint
from community_brain.jobs.worker import Worker


def controls(env, *, minimum_seconds=600):
    if (
        env.get("CB_ENABLE_NETWORK_PUBLICATION") != "true"
        or env.get("CB_ENABLE_MODEL_CALLS") != "false"
    ):
        raise ValueError("explicit publication-only enablement required")
    forbidden = (
        "CB_OPENROUTER_API_KEY",
        "OPENROUTER_API_KEY",
        "CB_FATHOM_API_KEY",
        "CB_PUBLISHER_GITHUB_PRIVATE_KEY_BASE64",
        "INFISICAL_CLIENT_SECRET",
    )
    if any(env.get(k) for k in forbidden):
        raise ValueError("provider or signing/bootstrap credentials forbidden")
    if (
        env.get("CB_PUBLISHER_GITHUB_APP_ID") != "4978270"
        or env.get("CB_PUBLISHER_GITHUB_INSTALLATION_ID") != "162488086"
    ):
        raise ValueError("publisher identity mismatch")
    ids = json.loads(env["CB_PUBLISHER_GITHUB_REPOSITORY_IDS"])
    if sorted(map(int, ids)) != [1176379254, 1249770482]:
        raise ValueError("publisher repositories mismatch")
    expiry = datetime.fromisoformat(
        env["CB_PUBLISHER_GITHUB_TOKEN_EXPIRES_AT"].replace("Z", "+00:00")
    )
    if expiry <= datetime.now(timezone.utc) + timedelta(seconds=minimum_seconds):
        raise ValueError("fresh publisher token required")
    if not env.get("CB_PUBLISHER_GITHUB_TOKEN"):
        raise ValueError("publisher token required")


def validate_job(store, plan, checkpoint):
    if (
        plan["job_id"] != "744d0f3f-8da7-4c12-bc15-5ec0a046518d"
        or plan["local_date"] != "2026-09-15"
    ):
        raise ValueError("unapproved job")
    if (
        checkpoint.get("verified") is not True
        or checkpoint.get("job_id") != plan["job_id"]
        or checkpoint.get("manifest_sha256") != plan["checkpoint_sha256"]
    ):
        raise ValueError("verified matching checkpoint required")
    with Session(store.engine) as s:
        job = s.get(Job, UUID(plan["job_id"]))
        if (
            not job
            or job.scope != plan["scope"]
            or job.parent_id
            or job.mode != "weekly"
            or job.identity["local_date"] != plan["local_date"]
            or fingerprint(job.identity) != plan["identity_sha256"]
        ):
            raise ValueError("job identity changed")
        if (
            job.processing != "succeeded"
            or job.artifacts != "ready"
            or job.indexing != "complete"
        ):
            raise ValueError("job not complete")
        artifacts = {}
        for a in s.scalars(select(Artifact).where(Artifact.job_id == job.id)):
            store.storage.read(a.path, a.sha256)
            artifacts[a.name] = a.sha256
        if artifacts != plan["artifacts"] or set(artifacts) != six_files(
            plan["local_date"]
        ):
            raise ValueError("artifact selection changed")
        stages = s.scalars(select(Stage).where(Stage.job_id == job.id)).all()
        if any(
            x.state in {"running", "partial", "outcome_unknown", "failed"}
            for x in stages
        ):
            raise ValueError("job requires reconciliation")


def main():
    os.umask(0o077)
    controls(os.environ)
    command, name = sys.argv[1:3]
    if command not in {"preflight", "enqueue", "execute"} or name not in {
        "git",
        "distribution",
    }:
        raise ValueError("explicit publication command/stage required")
    plan = json.loads(Path("/approval/plan.json").read_text())
    if fingerprint(plan) != os.environ["CB_PUBLICATION_PLAN_SHA256"]:
        raise ValueError("publication plan changed")
    checkpoint = json.loads(Path("/approval/checkpoint.json").read_text())
    store = Store(
        create_engine(os.environ["CB_DATABASE_URL"], pool_pre_ping=True),
        Storage("/files"),
    )
    validate_job(store, plan, checkpoint)
    token = os.environ["CB_PUBLISHER_GITHUB_TOKEN"]
    operator = PreparedGit(
        "/repos/operator.git",
        plan["operator"],
        token=token,
        askpass="/helpers/git-askpass.py",
    )
    consumer = PreparedGit(
        "/repos/consumer.git",
        plan["consumer"],
        token=token,
        askpass="/helpers/git-askpass.py",
    )
    publisher = GitHubRelease(
        plan["consumer"]["repository"],
        plan["consumer"]["commit"],
        token,
        tag_verifier=lambda version: consumer.head("refs/tags/" + version),
    )
    try:
        handler = PreparedPublication(
            plan,
            "/candidate",
            operator,
            consumer,
            publisher,
            "/journal/operations.jsonl",
        )
        handler.validate()
        chosen = Path("/journal") / (name + "-selection.json")
        if command == "preflight":
            expected_operator = (
                plan["operator"]["base"]
                if name == "git"
                else plan["operator"]["commit"]
            )
            if (
                operator.head("refs/heads/main") != expected_operator
                or consumer.head("refs/heads/main") != plan["consumer"]["base"]
                or consumer.head("refs/tags/" + plan["version"]) is not None
            ):
                raise ValueError("remote ref drift requires review")
            api = (
                "https://api.github.com/repos/"
                + plan["consumer"]["repository"]
                + "/releases"
            )
            response = publisher.client.get(api + "/tags/" + plan["version"])
            if response.status_code != 404:
                raise ValueError("release version requires review")
            for page in range(1, 101):
                response = publisher.client.get(
                    api, params={"per_page": 100, "page": page}
                )
                response.raise_for_status()
                items = response.json()
                if any(x.get("tag_name") == plan["version"] for x in items):
                    raise ValueError("existing draft requires review")
                if len(items) < 100:
                    break
            else:
                raise ValueError("release listing ceiling")
            print(
                json.dumps(
                    {"stage": name, "preflight": True, "plan_sha256": fingerprint(plan)}
                )
            )
            return
        if command == "enqueue":
            if chosen.exists():
                raise ValueError("existing selection requires review")
            if name == "distribution":
                with Session(store.engine) as s:
                    if s.get(Job, UUID(plan["job_id"])).git != "complete":
                        raise ValueError("recap publication incomplete")
            record(
                "/journal/operations.jsonl",
                {
                    "operation": "enqueue",
                    "stage": name,
                    "plan_sha256": fingerprint(plan),
                    "state": "intent",
                },
            )
            store.request_publication(
                plan["scope"],
                "approved-first-publication",
                UUID(plan["job_id"]),
                name,
                "first-publication-v1.2.0-" + name,
            )
            approved = selection(
                store,
                plan["job_id"],
                name,
                1,
                scope=plan["scope"],
                checkpoint=checkpoint,
            )
            with chosen.open("x") as stream:
                json.dump(approved, stream, sort_keys=True)
                stream.flush()
                os.fsync(stream.fileno())
            print(json.dumps({"stage": name, "selected": True}))
            return
        approved = json.loads(chosen.read_text())
        if (
            approved["job_id"] != plan["job_id"]
            or approved["stage"] != name
            or approved["artifacts"] != plan["artifacts"]
            or approved["checkpoint_sha256"] != plan["checkpoint_sha256"]
        ):
            raise ValueError("selection does not match approved plan")
        marker = Path("/journal") / (name + "-execution.started")
        with marker.open("x") as stream:
            stream.write(fingerprint(plan) + "\n")
            stream.flush()
            os.fsync(stream.fileno())

        def no_model(_):
            raise RuntimeError("model work forbidden")

        worker = Worker(
            store,
            no_model,
            handlers={"git": handler.git, "distribution": handler.distribution},
        )

        def guard():
            controls(os.environ, minimum_seconds=60)
            with Session(store.engine) as s:
                stage = s.get(Stage, UUID(approved["stage_id"]))
                store.owned(s, stage.id, stage.fence, worker.owner)

        operator.before_write = consumer.before_write = guard
        publisher.client.event_hooks["request"] = [
            lambda req: guard() if req.method in {"POST", "PATCH"} else None
        ]
        from bounded_worker import connection_options, STREAM, SUBJECT

        async def execute():
            return await run_selected(
                store,
                approved,
                worker,
                lambda: nats.connect(**connection_options(os.environ)),
                stream=STREAM,
                subject=SUBJECT,
                select_manifest=lambda *a, **kw: selection(
                    *a, checkpoint=checkpoint, **kw
                ),
            )

        result = asyncio.run(execute())
        record(
            "/journal/operations.jsonl",
            {
                "operation": "stage",
                "stage": name,
                "state": "verified",
                "result": result,
            },
        )
        print(
            json.dumps(
                {
                    "stage": name,
                    "state": result["state"],
                    "plan_sha256": fingerprint(plan),
                }
            )
        )
    finally:
        publisher.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # Durable stage/journal contains effect evidence. Never print token-bearing
        # subprocess arguments, HTTP objects, env or source/artifact content.
        print(
            json.dumps({"state": "requires_review", "error_class": type(exc).__name__})
        )
        raise SystemExit(1)

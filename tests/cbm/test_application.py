import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import UUID

from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import select
from sqlalchemy.orm import Session

from community_brain.jobs.api import create_app
from community_brain.jobs.auth import Principal
from community_brain.jobs.models import Artifact, Attempt, Job, ModelCall, Outbox, Stage
from community_brain.jobs.storage import Storage
from community_brain.jobs.store import Conflict, Store
from community_brain.jobs.worker import Worker
from community_brain.processing.pipeline import CANON, OutcomeUnknown

ROOT = Path(__file__).resolve().parents[2]
ALL = frozenset(
    [
        "jobs:submit",
        "jobs:read",
        "jobs:retry",
        "jobs:rerun",
        "artifacts:read",
        "sources:upload",
    ]
)
MEETING = {
    "meeting_id": "fixture-1",
    "started_at": "2026-09-08T22:00:00Z",
    "timezone": "America/Toronto",
    "local_date": "2026-09-08",
}


@pytest.fixture
def store(engine, tmp_path):
    config = Config(str(ROOT / "community-brain/alembic.ini"))
    with engine.begin() as conn:
        config.attributes["connection"] = conn
        command.upgrade(config, "head")
    yield Store(engine, Storage(tmp_path / "files"))
    with engine.begin() as conn:
        config.attributes["connection"] = conn
        command.downgrade(config, "base")


@pytest.fixture
def client(store):
    def authenticate(token):
        if token == "operator":
            return Principal("operator", "fixture", ALL)
        if token == "other":
            return Principal("other", "other", ALL)
        if token == "reader":
            return Principal(
                "reader", "fixture", frozenset(["jobs:read", "artifacts:read"])
            )
        raise ValueError()

    with TestClient(create_app(store, authenticate)) as client:
        client.headers["Authorization"] = "Bearer operator"
        yield client


def submit(client, mode="transcript_backfill", key="key"):
    uploaded = client.post(
        "/api/v1/sources",
        json={
            "meeting_id": "fixture-1",
            "kind": "transcript",
            "content": "A fixture transcript",
        },
    ).json()
    request = {
        "identity": MEETING,
        "mode": mode,
        "sources": {"transcript": uploaded["id"]},
    }
    response = client.post(
        "/api/v1/jobs", json=request, headers={"Idempotency-Key": key}
    )
    assert response.status_code == 202, response.text
    return UUID(response.json()["id"]), request


def fake_model(request):
    if request["expect"] == "prep.chunk":
        content = (
            "<!--SEGMENT\ntopic: sample\nspeakers: A\nkeywords: fixture\nsummary: fixture\n-->\n"
            + "A useful substantive sentence. " * 10
        )
    elif request["expect"].startswith("signal."):
        content = "\n\n".join("## " + s + "\nBody" for s in CANON)
    else:
        content = "Plain content"
    return {"choices": [{"message": {"content": content}, "finish_reason": "stop"}]}


def processing(store, job_id):
    with Session(store.engine) as s:
        return s.scalar(
            select(Stage.id).where(Stage.job_id == job_id, Stage.name == "processing")
        )


def test_durable_acceptance_idempotency_waiting_and_identity(client, store):
    job_id, request = submit(client, mode="weekly")
    assert (
        client.get(f"/api/v1/jobs/{job_id}").json()["processing"] == "waiting_for_input"
    )
    assert (
        client.post(
            "/api/v1/jobs", json=request, headers={"Idempotency-Key": "key"}
        ).status_code
        == 200
    )
    assert (
        client.post(
            "/api/v1/jobs", json=request, headers={"Idempotency-Key": "second"}
        ).status_code
        == 200
    )
    changed = {**request, "mode": "transcript_backfill"}
    assert (
        client.post(
            "/api/v1/jobs", json=changed, headers={"Idempotency-Key": "second"}
        ).status_code
        == 409
    )
    chat = client.post(
        "/api/v1/sources",
        json={"meeting_id": "fixture-1", "kind": "chat", "content": "chat"},
    ).json()["id"]
    assert (
        client.post(f"/api/v1/jobs/{job_id}/sources", json={"chat": chat}).status_code
        == 202
    )
    assert client.get(f"/api/v1/jobs/{job_id}").json()["processing"] == "queued"
    # Repeating the same binding is a no-op after a lost HTTP response.
    assert (
        client.post(f"/api/v1/jobs/{job_id}/sources", json={"chat": chat}).status_code
        == 202
    )
    replacement = client.post(
        "/api/v1/sources",
        json={"meeting_id": "fixture-1", "kind": "chat", "content": "changed chat"},
    ).json()["id"]
    assert client.post(f"/api/v1/jobs/{job_id}/sources", json={"chat": replacement}).status_code == 409


def test_scoped_authorization_and_validation(client, store):
    job_id, _ = submit(client)
    assert (
        client.get(
            f"/api/v1/jobs/{job_id}", headers={"Authorization": "Bearer other"}
        ).status_code
        == 404
    )
    assert (
        client.get(
            "/api/v1/jobs", headers={"Authorization": "Bearer invalid"}
        ).status_code
        == 401
    )
    assert (
        client.post(
            "/api/v1/sources", json={}, headers={"Authorization": "Bearer reader"}
        ).status_code
        == 403
    )
    bad = {"identity": {**MEETING, "local_date": "2026-09-09"}, "mode": "weekly"}
    result = client.post("/api/v1/jobs", json=bad, headers={"Idempotency-Key": "bad"})
    assert result.status_code == 422 and result.json()["code"] == "invalid_request"


def test_processing_artifacts_usage_and_duplicate_claim(client, store):
    job_id, _ = submit(client)
    stage_id = processing(store, job_id)
    worker = Worker(store, fake_model)
    fence = store.claim(stage_id, worker.owner)
    assert store.claim(stage_id, "other") is None
    worker.execute(stage_id, fence)
    view = client.get(f"/api/v1/jobs/{job_id}").json()
    assert (
        view["processing"] == "succeeded"
        and view["artifacts"] == "ready"
        and view["indexing"] == "pending"
    )
    artifacts = client.get(f"/api/v1/jobs/{job_id}/artifacts").json()["items"]
    assert len(artifacts) == 3
    assert all(client.get(a["url"]).status_code == 200 for a in artifacts)
    assert store.claim(stage_id, worker.owner) is None
    with Session(store.engine) as s:
        assert all(c.usage is None for c in s.scalars(select(ModelCall)))
        assert len(s.scalars(select(Attempt)).all()) == 1


def test_unknown_effect_held_after_restart(client, store):
    job_id, _ = submit(client)
    stage_id = processing(store, job_id)

    def unknown(request):
        raise OutcomeUnknown()

    worker = Worker(store, unknown)
    worker.execute(stage_id, store.claim(stage_id, worker.owner))
    store.recover()
    view = client.get(f"/api/v1/jobs/{job_id}").json()
    assert view["processing"] == "outcome_unknown"
    stage = next(s for s in view["stages"] if s["name"] == "processing")
    assert (
        client.post(
            f"/api/v1/jobs/{job_id}/stages/{stage_id}/retry",
            json={"generation": stage["generation"], "reason": "retry"},
            headers={"Idempotency-Key": "retry"},
        ).status_code
        == 409
    )


def test_expired_claim_fenced_and_bounded_recovery(client, store):
    job_id, _ = submit(client)
    stage_id = processing(store, job_id)
    fence = store.claim(stage_id, "old")
    with Session(store.engine) as s, s.begin():
        s.get(Stage, stage_id).lease_until = datetime.now(timezone.utc) - timedelta(
            seconds=1
        )
    with pytest.raises(Conflict, match="claim_lost"):
        store.heartbeat(stage_id, fence, "old")
    store.recover()
    with Session(store.engine) as s:
        assert s.get(Stage, stage_id).state == "retry_wait"
        assert s.scalar(select(Attempt)).state == "retry_wait"
    assert store.claim(stage_id, "new") is None


def test_corrupt_artifact_and_cross_scope_content_rejected(client, store):
    job_id, _ = submit(client)
    stage_id = processing(store, job_id)
    worker = Worker(store, fake_model)
    worker.execute(stage_id, store.claim(stage_id, worker.owner))
    artifact = client.get(f"/api/v1/jobs/{job_id}/artifacts").json()["items"][0]
    assert (
        client.get(
            artifact["url"], headers={"Authorization": "Bearer other"}
        ).status_code
        == 404
    )
    with Session(store.engine) as s:
        path = s.get(Artifact, UUID(artifact["id"])).path
    (store.storage.root / path).write_text("corrupt")
    assert client.get(artifact["url"]).status_code == 409
    assert client.get(f"/api/v1/jobs/{job_id}").json()["artifacts"] == "corrupt"


def test_storage_rejects_symlink_and_traversal(store, tmp_path):
    outside = tmp_path / "outside"
    outside.write_text("private")
    (store.storage.root / "link").symlink_to(outside)
    with pytest.raises(OSError):
        store.storage.read("link")
    with pytest.raises(ValueError):
        store.storage.read("../outside")


def test_rerun_versions_without_overwriting(client, store):
    job_id, request = submit(client)
    request = {**request, "reason": "new reviewed run"}
    response = client.post(
        f"/api/v1/jobs/{job_id}/reruns",
        json=request,
        headers={"Idempotency-Key": "key"},
    )
    assert response.status_code == 202 and response.json()["id"] != str(job_id)
    assert (
        client.post(
            f"/api/v1/jobs/{job_id}/reruns",
            json=request,
            headers={"Idempotency-Key": "key"},
        ).status_code
        == 200
    )


def test_worker_restart_reuses_completed_model_call(client, store, monkeypatch):
    job_id, _ = submit(client)
    stage_id = processing(store, job_id)
    calls = []

    def model(request):
        calls.append(request["stepName"])
        return fake_model(request)

    worker = Worker(store, model)
    fence = store.claim(stage_id, worker.owner)
    original = store.storage.put
    writes = []

    def crash(data):
        writes.append(1)
        if len(writes) == 2:
            raise RuntimeError("crash between response journal and artifact")
        return original(data)

    monkeypatch.setattr(store.storage, "put", crash)
    with pytest.raises(RuntimeError):
        worker.execute(stage_id, fence)
    monkeypatch.setattr(store.storage, "put", original)
    with Session(store.engine) as s, s.begin():
        s.get(Stage, stage_id).lease_until = datetime.now(timezone.utc) - timedelta(
            seconds=1
        )
    store.recover()
    with Session(store.engine) as s, s.begin():
        s.get(Stage, stage_id).due_at = datetime.now(timezone.utc) - timedelta(
            seconds=1
        )
    replacement = Worker(store, model)
    replacement.execute(stage_id, store.claim(stage_id, replacement.owner))
    assert calls.count("prep") == 1
    assert client.get(f"/api/v1/jobs/{job_id}").json()["processing"] == "succeeded"


def test_actual_jetstream_delivery_and_queue_loss_recovery(client, store, services):
    import nats
    from nats.js.api import ConsumerConfig, AckPolicy
    from uuid import uuid4
    from community_brain.jobs.worker import dispatch

    job_id, _ = submit(client)

    async def scenario():
        nc = await nats.connect(services[1])
        js = nc.jetstream()
        stream = "APP_" + uuid4().hex
        subject = "cbm.test." + uuid4().hex
        try:
            await js.add_stream(name=stream, subjects=[subject])
            sub = await js.pull_subscribe(
                subject,
                durable="test",
                stream=stream,
                config=ConsumerConfig(
                    ack_policy=AckPolicy.EXPLICIT, ack_wait=0.2, max_deliver=5
                ),
            )
            await dispatch(store, js, subject)
            msg = (await sub.fetch(1, timeout=3))[0]
            worker = Worker(store, fake_model)
            await worker.handle(msg)
            assert (
                client.get(f"/api/v1/jobs/{job_id}").json()["processing"] == "succeeded"
            )
            await js.publish(subject, msg.data)  # broker dedup intentionally bypassed
            await worker.handle((await sub.fetch(1, timeout=3))[0])
            with Session(store.engine) as s:
                assert len(s.scalars(select(Attempt)).all()) == 1
            # Simulate loss of all broker delivery state after publication ACK.
            await dispatch(store, js, subject)
            await js.delete_stream(stream)
            with Session(store.engine) as s, s.begin():
                for event in s.scalars(select(Outbox)):
                    event.sent_at = datetime.now(timezone.utc) - timedelta(minutes=6)
            store.recover()
            with Session(store.engine) as s:
                assert (
                    s.scalar(select(Outbox).where(Outbox.sent_at.is_(None))) is not None
                )
        finally:
            await nc.close()

    asyncio.run(scenario())


def test_partial_indexing_remains_independent_of_ready_files(client, store):
    job_id, _ = submit(client)
    stage_id = processing(store, job_id)
    worker = Worker(
        store,
        fake_model,
        handlers={
            "indexing": lambda _: {
                "state": "partial",
                "chunks_written": 29,
                "chunks_failed": 1,
            }
        },
    )
    worker.execute(stage_id, store.claim(stage_id, worker.owner))
    with Session(store.engine) as s:
        stage_id = s.scalar(
            select(Stage.id).where(Stage.job_id == job_id, Stage.name == "indexing")
        )
    worker.execute(stage_id, store.claim(stage_id, worker.owner))
    view = client.get(f"/api/v1/jobs/{job_id}").json()
    assert view["artifacts"] == "ready" and view["indexing"] == "partial"
    with pytest.raises(Conflict, match="prerequisites"):
        store.request_publication(
            "fixture", "operator", job_id, "distribution", "release"
        )


def test_api_pagination_does_not_drop_equal_timestamps(client, store):
    job_id, request = submit(client)
    for i in range(3):
        assert (
            client.post(
                f"/api/v1/jobs/{job_id}/reruns",
                json={**request, "reason": str(i)},
                headers={"Idempotency-Key": str(i)},
            ).status_code
            == 202
        )
    with Session(store.engine) as s, s.begin():
        for job in s.scalars(select(Job)):
            job.created_at = datetime(2026, 9, 9, tzinfo=timezone.utc)
    first = client.get("/api/v1/jobs?limit=2").json()
    second = client.get(
        "/api/v1/jobs", params={"limit": 2, "cursor": first["next_cursor"]}
    ).json()
    assert len({j["id"] for j in first["items"] + second["items"]}) == 4


def test_failed_post_retry_reuses_successful_calls(client, store):
    job_id, _ = submit(client)
    stage_id = processing(store, job_id)
    calls = []
    fail = [True]

    def model(request):
        calls.append(request["stepName"])
        if fail[0] and request["stepName"] == "post.section.general":
            return {
                "choices": [{"message": {"content": ""}, "finish_reason": "length"}]
            }
        return fake_model(request)

    worker = Worker(store, model)
    worker.execute(stage_id, store.claim(stage_id, worker.owner))
    with Session(store.engine) as s:
        generation = s.get(Stage, stage_id).generation
    before = len(calls)
    fail[0] = False
    store.retry(
        "fixture", stage_id, generation, "corrected provider issue", key="retry"
    )
    worker.execute(stage_id, store.claim(stage_id, worker.owner))
    assert len(calls) == before + 1
    assert client.get(f"/api/v1/jobs/{job_id}").json()["processing"] == "succeeded"


def test_completed_rendezvous_deduplicates_later_full_submission(client, store):
    job_id, request = submit(client, mode="weekly")
    chat = client.post(
        "/api/v1/sources",
        json={"meeting_id": "fixture-1", "kind": "chat", "content": "chat"},
    ).json()["id"]
    assert (
        client.post(f"/api/v1/jobs/{job_id}/sources", json={"chat": chat}).status_code
        == 202
    )
    request["sources"]["chat"] = chat
    response = client.post(
        "/api/v1/jobs", json=request, headers={"Idempotency-Key": "complete-inputs"}
    )
    assert response.status_code == 200 and response.json()["id"] == str(job_id)


def test_git_lost_push_receipt_reconciles_without_another_commit(
    client, store, tmp_path, monkeypatch
):
    import os
    import subprocess
    from community_brain.jobs.publication import PublicationHandlers

    job_id, _ = submit(client)
    stage_id = processing(store, job_id)
    worker = Worker(store, fake_model)
    worker.execute(stage_id, store.claim(stage_id, worker.owner))
    seed = tmp_path / "seed"
    seed.mkdir()
    remote = tmp_path / "remote.git"
    environment = {
        **os.environ,
        "GIT_AUTHOR_NAME": "Fixture",
        "GIT_AUTHOR_EMAIL": "fixture@localhost",
        "GIT_COMMITTER_NAME": "Fixture",
        "GIT_COMMITTER_EMAIL": "fixture@localhost",
    }
    for args in (
        ["init", "-b", "main"],
        ["-c", "commit.gpgsign=false", "commit", "--allow-empty", "-m", "fixture"],
    ):
        subprocess.run(
            ["git", *args], cwd=seed, env=environment, capture_output=True, check=True
        )
    subprocess.run(
        ["git", "clone", "--bare", str(seed), str(remote)],
        capture_output=True,
        check=True,
    )
    handlers = PublicationHandlers(
        store, tmp_path / "corpus", tmp_path / "config", None, str(remote)
    )
    real_run = subprocess.run
    failed = []

    def lost(*args, **kwargs):
        result = real_run(*args, **kwargs)
        if "push" in args[0] and not failed:
            failed.append(True)
            return subprocess.CompletedProcess(args[0], 1, "", "lost acknowledgment")
        return result

    monkeypatch.setattr(subprocess, "run", lost)
    with pytest.raises(OutcomeUnknown):
        handlers.git(job_id)
    before = real_run(
        ["git", "--git-dir", str(remote), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    assert handlers.git(job_id)["commit"] == before

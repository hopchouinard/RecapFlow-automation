"""Automatic submission boundaries against isolated PostgreSQL and JetStream."""

import asyncio
import fcntl
from datetime import timedelta
from types import SimpleNamespace
from uuid import UUID

import pytest
import test_application
from community_brain.jobs.api import create_app
from community_brain.jobs.auth import Principal
from community_brain.jobs.automatic import POLICY, next_stage, require_automatic
from community_brain.jobs.models import Attempt, Job, Outbox, Stage
from community_brain.jobs.store import Conflict
from community_brain.jobs.worker import Worker
from community_brain.processing.pipeline import OutcomeUnknown
from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session
from test_application import ALL, MEETING, fake_model
from test_manual import approve, exercise
from test_production_bounded import jobs


@pytest.fixture
def store(engine, tmp_path):
    yield from test_application.store.__wrapped__(engine, tmp_path)


def request(store, *, fathom=False, date="2026-09-11", meeting="new-fixture"):
    sources = {
        "chat": str(
            store.add_source("community-brain", meeting, "chat", "Fixture chat")
        )
    }
    if not fathom:
        sources["transcript"] = str(
            store.add_source(
                "community-brain", meeting, "transcript", "Fixture transcript"
            )
        )
    return {
        "identity": {
            **MEETING,
            "meeting_id": meeting,
            "local_date": date,
            "started_at": date + "T22:00:00Z",
            "provider": "fathom" if fathom else "manual",
        },
        "mode": "weekly",
        "sources": sources,
    }


def accept(store, body, key="new"):
    store.indexed_date = store.indexed_date or (lambda _: False)
    return store.accept("community-brain", "operator", key, body, automatic=True)[0]


@pytest.mark.parametrize("fathom", [False, True])
def test_full_loop_leaves_old_outbox_untouched_and_surfaces_files(
    store, services, fathom
):
    old, _ = jobs(store)
    body = request(store, fathom=fathom)
    job_id = accept(store, body)
    called = []

    class Fathom:
        def fetch(self, identity):
            called.append(identity)
            return "Selected fixture transcript"

    worker = Worker(
        store,
        fake_model,
        fathom=Fathom(),
        handlers={"indexing": lambda _: {"state": "complete", "chunks_failed": 0}},
    )
    names = []
    while item := next_stage(store, "community-brain"):
        assert item["job_id"] == str(job_id)
        names.append(item["stage"])
        asyncio.run(
            exercise(store, services, approve(store, job_id, item["stage"]), worker)
        )
    assert names == (["acquisition"] if fathom else []) + ["processing", "indexing"]
    assert called == ([body["identity"]] if fathom else [])
    with Session(store.engine) as session:
        job = session.get(Job, job_id)
        assert job.config["automation_policy"] == POLICY
        assert job.processing == "succeeded" and job.indexing == "complete"
        assert job.git == job.distribution == "not_requested"
        old_stages = session.scalars(
            select(Stage).where(Stage.job_id.in_([UUID(v) for v in old.values()]))
        ).all()
        assert all(s.attempts == 0 for s in old_stages)
        assert all(
            e.sent_at is None
            for e in session.scalars(
                select(Outbox).where(Outbox.stage_id.in_([s.id for s in old_stages]))
            )
        )
    archive = SimpleNamespace(
        scope="community-brain", meetings=[{"date": "2025-02-02", "artifacts": []}]
    )
    client = TestClient(
        create_app(
            store,
            lambda _: Principal("operator", "community-brain", ALL),
            archive=archive,
            automatic=True,
        )
    )
    client.headers["Authorization"] = "Bearer fixture"
    catalog = client.get("/api/v1/meetings").json()["items"]
    assert [m["date"] for m in catalog] == ["2026-09-11", "2025-02-02"]
    assert catalog[0]["source"] == "processed" and catalog[0]["indexing"] == "complete"
    assert len(catalog[0]["artifacts"]) == 6
    for artifact in catalog[0]["artifacts"]:
        assert client.get(artifact["url"]).status_code == 200
    assert accept(store, body, key="duplicate") == job_id
    assert next_stage(store, "community-brain") is None


def test_existing_jobs_never_opt_in_and_date_collisions_fail_closed(store):
    body = request(store)
    old, _ = store.accept("community-brain", "operator", "old", body)
    assert accept(store, body, key="new") == old
    with pytest.raises(ValueError, match="not opted"):
        require_automatic(store, old)
    assert next_stage(store, "community-brain") is None
    with pytest.raises(Conflict, match="date_already_submitted"):
        accept(store, request(store, meeting="other"), key="other")
    store.indexed_date = lambda _: True
    with pytest.raises(Conflict, match="already_indexed"):
        accept(
            store,
            request(store, date="2026-09-12", meeting="protected"),
            key="protected",
        )
    with Session(store.engine) as session:
        assert len(session.scalars(select(Job)).all()) == 1


def test_uncertain_calls_and_expired_leases_are_never_replayed(store, services):
    job_id = accept(store, request(store))

    def unknown(_):
        raise OutcomeUnknown("simulated lost provider response")

    with pytest.raises(RuntimeError, match="incomplete"):
        asyncio.run(
            exercise(store, services, approve(store, job_id), Worker(store, unknown))
        )
    assert next_stage(store, "community-brain") is None
    with Session(store.engine) as session:
        stage = session.scalar(
            select(Stage).where(Stage.job_id == job_id, Stage.name == "processing")
        )
        stage_id = stage.id
        assert stage.state == "outcome_unknown" and stage.attempts == 1
    store.retry(
        "community-brain", stage_id, 1, "explicit test reconciliation", reconcile=True
    )
    assert (
        next_stage(store, "community-brain") is None
    )  # generation 2 requires manual handling
    accept(store, request(store, date="2026-09-12", meeting="lease"), key="lease")
    item = next_stage(store, "community-brain")
    stage_id = UUID(item["stage_id"])
    fence = store.claim(stage_id, "orphan", expected_generation=1)
    with Session(store.engine) as session, session.begin():
        session.get(Stage, stage_id).lease_until = store.now(session) - timedelta(
            seconds=1
        )
    assert next_stage(store, "community-brain") is None
    with Session(store.engine) as session:
        stage = session.get(Stage, stage_id)
        assert stage.state == "outcome_unknown" and stage.fence > fence
        assert (
            session.scalar(select(Attempt).where(Attempt.stage_id == stage_id)).state
            == "outcome_unknown"
        )


def test_api_assigns_policy_and_checkpoint_barrier_blocks_writes_only(store):
    store.indexed_date = lambda _: False
    client = TestClient(
        create_app(
            store,
            lambda _: Principal("operator", "community-brain", ALL),
            automatic=True,
        )
    )
    client.headers["Authorization"] = "Bearer fixture"
    body = request(store)
    assert client.get("/api/v1/me").json()["automatic_processing"] is True
    with (store.storage.root / ".submission.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        assert (
            client.post(
                "/api/v1/jobs", json=body, headers={"Idempotency-Key": "blocked"}
            ).status_code
            == 503
        )
        assert client.get("/api/v1/jobs").json()["items"] == []
    assert (
        client.post(
            "/api/v1/jobs",
            json={**body, "automation_policy": POLICY},
            headers={"Idempotency-Key": "forged"},
        ).status_code
        == 422
    )
    response = client.post(
        "/api/v1/jobs", json=body, headers={"Idempotency-Key": "accepted"}
    )
    assert response.status_code == 202, response.text
    require_automatic(store, response.json()["id"])


def test_checkpoint_keeps_read_only_retrieval_available(store):
    app = create_app(
        store, lambda _: Principal("operator", "community-brain", ALL), automatic=True
    )

    @app.post("/retrieval/query")
    def read_only_query():
        return {"context": "fixture"}

    client = TestClient(app, headers={"Authorization": "Bearer fixture"})
    with (store.storage.root / ".submission.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        assert client.post("/retrieval/query", json={"query": "fixture"}).json() == {
            "context": "fixture"
        }
        assert (
            client.post(
                "/api/v1/sources",
                json={"meeting_id": "denied", "kind": "chat", "content": "fixture"},
            ).status_code
            == 503
        )

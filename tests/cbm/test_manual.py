"""Manual selection against real private PostgreSQL/JetStream; no external calls."""

import asyncio
from uuid import UUID

import nats
import pytest
import test_application
from community_brain.jobs.manual import run_selected, selection
from community_brain.jobs.models import Job, Outbox, Stage
from community_brain.jobs.worker import Worker
from community_brain.processing.pipeline import OutcomeUnknown
from nats.js.api import ConsumerConfig
from sqlalchemy import select
from sqlalchemy.orm import Session
from test_application import fake_model
from test_production_bounded import jobs


@pytest.fixture
def store(engine, tmp_path):
    yield from test_application.store.__wrapped__(engine, tmp_path)


def approve(store, job_id, name="processing", generation=1):
    return selection(store, job_id, name, generation, scope="community-brain")


async def exercise(store, services, approved, worker, before=None):
    nc = await nats.connect(services[1])
    js = nc.jetstream()
    await js.add_stream(name="MANUAL", subjects=["manual.ready"])
    await js.add_consumer(
        "MANUAL",
        ConsumerConfig(
            durable_name="community-brain-worker",
            filter_subject="manual.ready",
            ack_policy="explicit",
        ),
    )
    try:
        if before:
            await before(js)
        return await run_selected(
            store,
            approved,
            worker,
            lambda: nats.connect(services[1]),
            stream="MANUAL",
            subject="manual.ready",
        )
    finally:
        await js.delete_stream("MANUAL")
        await nc.close()


def test_only_selected_processing_no_index_or_unrelated_dispatch(store, services):
    ids, _ = jobs(store)
    approved = approve(store, ids["weekly"])
    asyncio.run(exercise(store, services, approved, Worker(store, fake_model)))
    with Session(store.engine) as session:
        stages = session.scalars(select(Stage)).all()
        assert sum(s.attempts for s in stages) == 1
        assert sum(e.sent_at is not None for e in session.scalars(select(Outbox))) == 1
        assert session.get(Job, UUID(ids["weekly"])).processing == "succeeded"
        assert all(s.attempts == 0 for s in stages if s.name != "processing")
    with pytest.raises(ValueError, match="reconciliation"):
        approve(store, ids["weekly"])
    with pytest.raises(ValueError, match="excluded"):
        selection(
            store,
            ids["weekly"],
            "indexing",
            1,
            scope="community-brain",
            excluded_jobs=ids.values(),
        )


def test_changed_selection_rejected_before_connection(store):
    ids, _ = jobs(store)
    approved = approve(store, ids["weekly"])
    approved["artifacts"] = {"forged": "hash"}

    async def no_connect():
        pytest.fail("must not connect")

    with pytest.raises(ValueError, match="selection changed"):
        asyncio.run(
            run_selected(
                store,
                approved,
                Worker(store, fake_model),
                no_connect,
                stream="MANUAL",
                subject="manual.ready",
            )
        )


def test_unrelated_queue_message_is_not_executed_or_discarded(store, services):
    ids, _ = jobs(store)
    approved = approve(store, ids["weekly"])

    async def before(js):
        await js.publish("manual.ready", b'{"unrelated":true}')

    with pytest.raises(ValueError, match="unexpected queued"):
        asyncio.run(
            exercise(store, services, approved, Worker(store, fake_model), before)
        )
    with Session(store.engine) as session:
        assert all(s.attempts == 0 for s in session.scalars(select(Stage)))


def test_unknown_outcome_cannot_restart_and_stale_generation_cannot_claim(
    store, services
):
    ids, _ = jobs(store)
    approved = approve(store, ids["weekly"])

    def unknown(request):
        raise OutcomeUnknown("lost response")

    with pytest.raises(RuntimeError, match="incomplete"):
        asyncio.run(exercise(store, services, approved, Worker(store, unknown)))
    with pytest.raises(ValueError, match="reconciliation"):
        approve(store, ids["weekly"])
    stage_id = UUID(approved["stage_id"])
    store.retry(
        "community-brain",
        stage_id,
        1,
        "Explicit simulated reconciliation",
        reconcile=True,
    )
    assert store.claim(stage_id, "stale", expected_generation=1) is None
    retried = approve(store, ids["weekly"], generation=2)
    asyncio.run(exercise(store, services, retried, Worker(store, fake_model)))
    with Session(store.engine) as session:
        assert session.get(Job, UUID(ids["weekly"])).processing == "succeeded"


def test_partial_index_requires_new_generation_and_preserves_artifacts(store, services):
    ids, _ = jobs(store)
    asyncio.run(
        exercise(
            store, services, approve(store, ids["weekly"]), Worker(store, fake_model)
        )
    )
    approved = approve(store, ids["weekly"], "indexing")
    worker = Worker(
        store,
        lambda request: pytest.fail("no processing replay"),
        handlers={"indexing": lambda job: {"state": "partial", "chunks_failed": 1}},
    )
    with pytest.raises(RuntimeError, match="incomplete"):
        asyncio.run(exercise(store, services, approved, worker))
    with pytest.raises(ValueError, match="reconciliation"):
        approve(store, ids["weekly"], "indexing")
    store.retry(
        "community-brain", UUID(approved["stage_id"]), 1, "Retry known failed chunk"
    )
    retried = approve(store, ids["weekly"], "indexing", 2)
    assert retried["artifacts"] == approved["artifacts"]
    worker.handlers["indexing"] = lambda job: {"state": "complete", "chunks_failed": 0}
    asyncio.run(exercise(store, services, retried, worker))
    with Session(store.engine) as session:
        job = session.get(Job, UUID(ids["weekly"]))
        assert job.indexing == "complete" and job.artifacts == "ready"
        assert job.git == job.distribution == "not_requested"


def test_existing_canonical_date_is_rejected_before_index_dispatch(
    store, services, tmp_path, monkeypatch
):
    import importlib
    from pathlib import Path

    import lancedb

    monkeypatch.syspath_prepend(
        str(
            Path(__file__).resolve().parents[2]
            / "deploy/community-brain/production-staging"
        )
    )
    adapter = importlib.import_module("manual_worker")
    ids, _ = jobs(store)
    asyncio.run(
        exercise(
            store, services, approve(store, ids["weekly"]), Worker(store, fake_model)
        )
    )
    root = tmp_path / "corpus"
    lancedb.connect(str(root / "lancedb/nomic-v1")).create_table(
        "chunks", [{"session_id": "2026-09-10"}]
    )
    monkeypatch.setenv("CB_CORPUS_ROOT", str(root))
    with pytest.raises(ValueError, match="replacement decision"):
        adapter.reviewed_selection(store, ids["weekly"], "indexing", 1)
    with Session(store.engine) as session:
        stage = session.scalar(
            select(Stage).where(
                Stage.job_id == UUID(ids["weekly"]), Stage.name == "indexing"
            )
        )
        assert stage.attempts == 0 and stage.state == "queued"


def test_selected_api_client_submits_only_waiting_acquisition(
    store, monkeypatch, capsys
):
    import importlib
    import io
    import json
    import sys
    import time
    from pathlib import Path

    from community_brain.jobs.api import create_app
    from community_brain.jobs.auth import Principal
    from fastapi.testclient import TestClient

    monkeypatch.syspath_prepend(
        str(
            Path(__file__).resolve().parents[2]
            / "deploy/community-brain/production-staging"
        )
    )
    module = importlib.import_module("selected_job_client")
    jobs(store)
    source = store.add_source(
        "community-brain", "181075701", "chat", "Synthetic API-only test"
    )
    application = create_app(
        store,
        lambda token: Principal(
            "operator",
            "community-brain",
            frozenset({"sources:upload", "jobs:submit", "jobs:read", "artifacts:read"}),
        ),
    )
    monkeypatch.setattr(
        module.httpx,
        "Client",
        lambda **kwargs: TestClient(application, headers=kwargs["headers"]),
    )
    monkeypatch.setattr(
        sys,
        "stdin",
        io.StringIO(
            json.dumps(
                {
                    "operation": "submit",
                    "token": "fixture",
                    "expires_at": int(time.time()) + 60,
                    "chat_source_id": source,
                }
            )
        ),
    )
    module.main()
    result = json.loads(capsys.readouterr().out)
    with Session(store.engine) as session:
        job = session.get(Job, UUID(result["job_id"]))
        assert job.identity == module.IDENTITY and job.processing == "waiting_for_input"
        stages = session.scalars(select(Stage).where(Stage.job_id == job.id)).all()
        assert all(s.attempts == 0 for s in stages)
        assert {s.name for s in stages if s.state == "queued"} == {"acquisition"}


def test_hidden_rehearsals_are_not_workspace_jobs_but_remain_durable(store):
    from community_brain.jobs.api import create_app
    from community_brain.jobs.auth import Principal
    from fastapi.testclient import TestClient

    ids, _ = jobs(store)
    hidden = ids["weekly"]
    app = create_app(
        store,
        lambda _: Principal("reader", "community-brain", frozenset(["jobs:read"])),
        hidden_jobs=[hidden],
    )
    c = TestClient(app)
    headers = {"Authorization": "Bearer reader"}
    listed = c.get("/api/v1/jobs?limit=1", headers=headers).json()
    assert [j["id"] for j in listed["items"]] == [ids["transcript_backfill"]]
    assert listed["next_cursor"] is None
    assert c.get("/api/v1/jobs/" + hidden, headers=headers).status_code == 404
    with Session(store.engine) as session:
        assert session.get(Job, UUID(hidden)) is not None
        assert len(session.scalars(select(Outbox)).all()) == 2

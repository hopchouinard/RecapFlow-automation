"""Bounded production adapter against disposable DB/queue and fake model only."""

import asyncio
import importlib.util
import json
from pathlib import Path

import nats
import pytest
import test_application
from community_brain.jobs.models import Job, Stage
from nats.js.api import ConsumerConfig
from sqlalchemy import select
from sqlalchemy.orm import Session
from test_application import fake_model

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "bounded_production",
    ROOT / "deploy/community-brain/production-staging/bounded_worker.py",
)
bounded = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bounded)


@pytest.fixture
def store(engine, tmp_path):
    yield from test_application.store.__wrapped__(engine, tmp_path)


def jobs(store):
    fixture = json.loads(
        (
            ROOT / "deploy/community-brain/production-staging/synthetic-fixture.json"
        ).read_text()
    )
    sources = {
        kind: store.add_source("community-brain", bounded.MEETING, kind, body)
        for kind, body in fixture.items()
    }
    identity = {
        "meeting_id": bounded.MEETING,
        "started_at": "2026-09-10T00:00:00Z",
        "timezone": "Etc/UTC",
        "local_date": "2026-09-10",
        "provider": "manual",
    }
    result = {}
    for mode in ("weekly", "transcript_backfill"):
        selected = (
            sources if mode == "weekly" else {"transcript": sources["transcript"]}
        )
        job_id, _ = store.accept(
            "community-brain",
            "bounded-test",
            mode,
            {"identity": identity, "mode": mode, "sources": selected},
        )
        result[mode] = str(job_id)
    return result, fixture


def test_two_jobs_only_and_no_indexing_or_replay(store, services):
    manifest, fixture = jobs(store)

    async def exercise():
        nc = await nats.connect(services[1])
        js = nc.jetstream()
        await js.add_stream(name=bounded.STREAM, subjects=[bounded.SUBJECT])
        await js.add_consumer(
            bounded.STREAM,
            ConsumerConfig(
                durable_name="community-brain-worker",
                filter_subject=bounded.SUBJECT,
                ack_policy="explicit",
            ),
        )
        try:
            await bounded.run(
                store,
                manifest,
                fixture,
                lambda: nats.connect(services[1]),
                lambda: fake_model,
            )
            with Session(store.engine) as session:
                assert all(
                    j.processing == "succeeded" for j in session.scalars(select(Job))
                )
                assert all(
                    s.attempts == 0
                    for s in session.scalars(
                        select(Stage).where(Stage.name != "processing")
                    )
                )
            with pytest.raises(ValueError, match="replay"):
                await bounded.run(
                    store,
                    manifest,
                    fixture,
                    lambda: nats.connect(services[1]),
                    lambda: fake_model,
                )
        finally:
            await js.delete_stream(bounded.STREAM)
            await nc.close()

    asyncio.run(exercise())


def test_changed_source_rejected_before_queue_connection(store):
    manifest, fixture = jobs(store)
    fixture["transcript"] = "unapproved content"

    async def no_connect():
        pytest.fail("must reject before connecting")

    with pytest.raises(ValueError, match="Nonfixture"):
        asyncio.run(
            bounded.run(store, manifest, fixture, no_connect, lambda: fake_model)
        )


def test_wrong_provider_cap_and_request_ceiling_never_call_model(monkeypatch):
    from types import SimpleNamespace

    monkeypatch.setattr(
        bounded.httpx,
        "get",
        lambda *a, **kw: SimpleNamespace(
            raise_for_status=lambda: None, json=lambda: {"data": {"limit": 5}}
        ),
    )
    monkeypatch.setattr(
        bounded.OpenRouter,
        "__call__",
        lambda *a: pytest.fail("model must not be called"),
    )
    provider = bounded.BoundedProvider("fixture")
    with pytest.raises(bounded.OutcomeUnknown, match="allowance"):
        provider({})
    provider.calls = 12
    with pytest.raises(bounded.OutcomeUnknown, match="ceiling"):
        provider({})


def test_tls_first_options_and_wrong_endpoint(monkeypatch):
    env = {
        "CB_NATS_URL": "tls://platform-events.patchoutech.lab:4223",
        "CB_NATS_USER": "fixture",
        "CB_NATS_PASSWORD": "fixture",
    }
    marker = object()
    monkeypatch.setattr(bounded.ssl, "create_default_context", lambda **kw: marker)
    options = bounded.connection_options(env)
    assert options["tls"] is marker and options["tls_handshake_first"] is True
    assert options["inbox_prefix"] == b"_INBOX.cbm_prod_worker"
    assert options["allow_reconnect"] is False
    env["CB_NATS_URL"] = "nats://localhost:4222"
    with pytest.raises(ValueError):
        bounded.connection_options(env)


def test_unknown_outcome_stops_before_second_job(store, services):
    manifest, fixture = jobs(store)

    def unknown(request):
        raise bounded.OutcomeUnknown("simulated lost response")

    async def exercise():
        nc = await nats.connect(services[1])
        js = nc.jetstream()
        await js.add_stream(name=bounded.STREAM, subjects=[bounded.SUBJECT])
        await js.add_consumer(
            bounded.STREAM,
            ConsumerConfig(
                durable_name="community-brain-worker",
                filter_subject=bounded.SUBJECT,
                ack_policy="explicit",
            ),
        )
        try:
            with pytest.raises(RuntimeError, match="incomplete"):
                await bounded.run(
                    store,
                    manifest,
                    fixture,
                    lambda: nats.connect(services[1]),
                    lambda: unknown,
                )
            with Session(store.engine) as session:
                values = {j.mode: j.processing for j in session.scalars(select(Job))}
                assert values["weekly"] == "outcome_unknown"
                stages = session.scalars(
                    select(Stage).join(Job).where(Job.mode == "transcript_backfill")
                ).all()
                assert all(s.attempts == 0 for s in stages)
        finally:
            await js.delete_stream(bounded.STREAM)
            await nc.close()

    asyncio.run(exercise())

"""Execute Request027 selected worker adapter on VM108 with synthetic providers.

Real PostgreSQL, JetStream, durable stages, artifacts and LanceDB. External
providers, allowance authority and queue connection binding are fixtures.
This does not certify production host launchers, paid budgets or transports.
"""

import asyncio
import hashlib
import json
import os
from pathlib import Path
from types import SimpleNamespace
from uuid import UUID
from unittest.mock import patch
from contextlib import nullcontext
import manual_worker

import lancedb
import nats
from nats.js.api import ConsumerConfig
from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session
from community_brain.jobs.models import Base, Stage, Job, Outbox
from community_brain.jobs.runtime import make_store, SPA
from community_brain.jobs.api import create_app
from community_brain.jobs.auth import Principal
from community_brain.jobs.automatic import next_stage
from community_brain.jobs.manual import run_selected
from community_brain.jobs.publication import PublicationHandlers
from community_brain.jobs.worker import Worker
from community_brain.ingestion.schema import pyarrow_table_schema
from manual_worker import reviewed_selection, complete_fts
from fixtures import (
    fake_model,
    _fake_extract_response,
    _mock_ollama_embed,
    _write_min_configs,
)

assert os.environ["CB_DATABASE_URL"].startswith(
    "postgresql+psycopg://fixture@cbm-auto-pg/"
)
assert not any(key.endswith(("API_KEY", "TOKEN")) for key in os.environ)
root = Path("/state")
_write_min_configs(root / "config")
store = make_store()
Base.metadata.create_all(store.engine)  # Disposable empty schema, never a shared DB.
lancedb.connect(str(root / "corpus/lancedb/nomic-v1")).create_table(
    "chunks", schema=pyarrow_table_schema()
)
app = create_app(
    store,
    lambda _: Principal(
        "fixture",
        "community-brain",
        frozenset({"jobs:read", "artifacts:read", "jobs:submit", "sources:upload"}),
    ),
    automatic=True,
    archive=SimpleNamespace(scope="community-brain", meetings=[]),
)
app.mount("/", SPA(directory="/app/web/dist", html=True), name="ui")
client = TestClient(app, headers={"Authorization": "Bearer fixture"})
assert client.get("/api/v1/me").json()["automatic_processing"] is True
assert client.get("/").status_code == 200
for path in Path("/app/web/dist").rglob("*"):
    if path.is_file():
        assert (
            hashlib.sha256(
                client.get("/" + str(path.relative_to("/app/web/dist"))).content
            ).digest()
            == hashlib.sha256(path.read_bytes()).digest()
        )
identity = {
    "meeting_id": "old",
    "local_date": "2026-09-08",
    "started_at": "2026-09-08T22:00:00Z",
    "timezone": "America/Toronto",
    "provider": "manual",
}
source = store.add_source(
    "community-brain", "old", "transcript", "Old synthetic source"
)
old, _ = store.accept(
    "community-brain",
    "fixture",
    "old",
    {
        "identity": identity,
        "mode": "transcript_backfill",
        "sources": {"transcript": str(source)},
    },
)


async def main():
    nc = await nats.connect("nats://cbm-auto-nats:4222")
    js = nc.jetstream()
    await js.add_stream(name="AUTOFIXTURE", subjects=["fixture.ready"])
    await js.add_consumer(
        "AUTOFIXTURE",
        ConsumerConfig(
            durable_name="community-brain-worker",
            filter_subject="fixture.ready",
            ack_policy="explicit",
        ),
    )
    stages = []
    first_rows = None
    for fathom, date in ((False, "2026-09-11"), (True, "2026-09-12")):
        meeting = "fixture-" + date
        sources = {}
        for kind in ["chat"] if fathom else ["transcript", "chat"]:
            sources[kind] = client.post(
                "/api/v1/sources",
                json={
                    "meeting_id": meeting,
                    "kind": kind,
                    "content": "Synthetic " + kind,
                },
            ).json()["id"]
        body = {
            "identity": {
                **identity,
                "meeting_id": meeting,
                "local_date": date,
                "started_at": date + "T22:00:00Z",
                "provider": "fathom" if fathom else "manual",
            },
            "mode": "weekly",
            "sources": sources,
        }
        response = client.post(
            "/api/v1/jobs", json=body, headers={"Idempotency-Key": meeting}
        )
        assert response.status_code == 202, response.text
        job_id = UUID(response.json()["id"])

        class Fathom:
            def __init__(self, *args): pass

            def close(self): pass

            def fetch(self, selected):
                assert selected["meeting_id"] == meeting
                return "Selected synthetic Fathom transcript"

        handler = PublicationHandlers(store, root / "corpus", root / "config", None)
        worker = Worker(
            store,
            fake_model,
            fathom=Fathom(),
            handlers={
                "indexing": lambda job: complete_fts(handler, root / "corpus", job)
            },
        )
        while selected := next_stage(store, "community-brain"):
            assert selected["job_id"] == str(job_id)
            approval = reviewed_selection(store, job_id, selected["stage"], 1)
            with (
                patch(
                    "community_brain.ingestion.embedding.ollama.Client.embed",
                    side_effect=_mock_ollama_embed,
                ),
                patch(
                    "community_brain.ingestion.embedding.ollama.embed",
                    side_effect=_mock_ollama_embed,
                ),
                patch(
                    "community_brain.ingestion.extractor._call_llm",
                    side_effect=_fake_extract_response,
                ),
                patch(
                    "community_brain.ingestion.session_extractor._call_llm",
                    side_effect=_fake_extract_response,
                ),
            ):
                environment = {
                    'CB_ENABLE_NETWORK_PUBLICATION': 'false',
                    'CB_ENABLE_MODEL_CALLS': 'true',
                    'OLLAMA_BASE_URL': 'http://synthetic-provider.invalid',
                }
                key_name = ('CB_FATHOM_API_KEY' if selected['stage'] == 'acquisition'
                            else 'CB_OPENROUTER_API_KEY')
                environment[key_name] = 'synthetic-no-provider-access'
                with (
                    patch.dict(os.environ, environment),
                    patch.object(manual_worker, 'ManualProvider', lambda key: fake_model),
                    patch.object(manual_worker, 'SelectedFathom', Fathom),
                    patch.object(manual_worker, 'audited_indexing', lambda *args: nullcontext()),
                    patch.object(manual_worker, 'connection_options',
                                 lambda env: {'servers': 'nats://cbm-auto-nats:4222'}),
                    patch.object(manual_worker, 'STREAM', 'AUTOFIXTURE'),
                    patch.object(manual_worker, 'SUBJECT', 'fixture.ready'),
                ):
                    await manual_worker.execute(store, approval)
            stages.append(selected["stage"])
        view = client.get("/api/v1/jobs/" + str(job_id)).json()
        assert view["indexing"] == "complete" and view["artifacts"] == "ready", view
        assert view["git"] == view["distribution"] == "not_requested"
        assert client.post(
            "/api/v1/jobs", json=body, headers={"Idempotency-Key": meeting + "-again"}
        ).json()["id"] == str(job_id)
        table = lancedb.connect(str(root / "corpus/lancedb/nomic-v1")).open_table(
            "chunks"
        )
        current = (
            table.search().where("session_id = '2026-09-11'").limit(10000).to_list()
        )
        if first_rows is None:
            first_rows = current
        else:
            assert first_rows == current
        assert table.index_stats("bm25_text_idx")["num_unindexed_rows"] == 0
    with Session(store.engine) as session:
        old_stages = session.scalars(select(Stage).where(Stage.job_id == old)).all()
        assert all(s.attempts == 0 for s in old_stages)
        assert all(
            e.sent_at is None
            for e in session.scalars(
                select(Outbox).where(Outbox.stage_id.in_([s.id for s in old_stages]))
            )
        )
    catalog = client.get("/api/v1/meetings").json()["items"]
    assert len(catalog) == 2
    for meeting in catalog:
        assert meeting["indexing"] == "complete"
        for artifact in meeting["artifacts"]:
            response = client.get(artifact["url"])
            assert (
                response.status_code == 200
                and hashlib.sha256(response.content).hexdigest() == artifact["sha256"]
            )
    await nc.close()
    print(
        json.dumps(
            {
                "passed": True,
                "selected_worker_execute": True,
                "production_host_and_budget_certified": False,
                "stages": stages,
                "meetings": len(catalog),
                "searchable_rows": table.count_rows(),
                "fts": {
                    key: table.index_stats("bm25_text_idx")[key]
                    for key in ("num_indexed_rows", "num_unindexed_rows")
                },
                "old_outbox_untouched": True,
                "first_meeting_unchanged": True,
                "external_calls": 0,
            }
        )
    )


asyncio.run(main())

"""VM108-only indexing of a copied production synthetic job. No live DB/queue."""

import asyncio
import hashlib
import json
import os
import sys
from pathlib import Path
from uuid import UUID

import lancedb
import nats
from community_brain.jobs.manual import run_selected, selection
from community_brain.jobs.models import Artifact, Job, ModelCall, Source, Stage
from community_brain.jobs.publication import PublicationHandlers, corpus_lock
from community_brain.jobs.runtime import make_store
from community_brain.jobs.worker import Worker
from indexing_budget import allowance, audited_indexing
from nats.js.api import ConsumerConfig
from sqlalchemy import select
from sqlalchemy.orm import Session

ROOT = Path("/state")
JOB = "f6e9abed-e862-4eb7-a231-e98467adcaba"
COPY = "cbm-manual-index-20260910-vm108"
DB = "postgresql+psycopg://cbmcopy@postgres:5432/cbm_copy"
STREAM, SUBJECT = "CBM_DISPOSABLE_INDEX", "cbm.copy.index.ready"


def row_hash(rows):
    return hashlib.sha256(
        json.dumps(
            sorted(rows, key=lambda r: r["chunk_id"]),
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()


def guard():
    if json.loads(Path("/copy.json").read_text())["identity"] != COPY:
        raise ValueError("not the approved disposable copy")
    if os.environ["CB_DATABASE_URL"] != DB:
        raise ValueError("non-disposable database forbidden")
    if os.environ.get("CB_ENABLE_NETWORK_PUBLICATION") != "false":
        raise ValueError("publication must remain disabled")
    if any(
        name in os.environ
        for name in ("CB_FATHOM_API_KEY", "CB_NATS_PASSWORD", "CB_GITHUB_TOKEN")
    ):
        raise ValueError("unrelated credential in copy")
    return make_store()


def table():
    return lancedb.connect(str(ROOT / "corpus/lancedb/nomic-v1")).open_table("chunks")


def preflight(store):
    manifest = json.loads(Path("/inputs/managed-state-manifest.json").read_text())
    for name, value in manifest["files"].items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != value["sha256"]:
            raise ValueError("copy checksum mismatch")
    with Session(store.engine) as session:
        jobs = session.scalars(select(Job)).all()
        assert len(jobs) == 2 and all(j.processing == "succeeded" for j in jobs)
        for model, path, sha in (
            (Source, "path", "sha256"),
            (Artifact, "path", "sha256"),
            (ModelCall, "response_path", "response_hash"),
        ):
            for record in session.scalars(select(model)):
                store.storage.read(getattr(record, path), getattr(record, sha))
        assert all(
            s.attempts == 0
            for s in session.scalars(select(Stage))
            if s.name != "processing"
        )
    rows = table().to_arrow().to_pylist()
    assert len(rows) == 1901 and len({r["session_id"] for r in rows}) == 87
    assert not any(r["session_id"] == "2026-09-10" for r in rows)
    approved = selection(store, JOB, "indexing", 1, scope="community-brain")
    result = {
        "copy": COPY,
        "production_unchanged_claimed": False,
        "baseline_rows": len(rows),
        "baseline_rows_sha256": row_hash(rows),
        "verified_files": len(manifest["files"]),
        "selection": approved,
        "request_ceiling": 32,
        "lifetime_cap_usd": 2,
    }
    with (ROOT / "files/copy-preflight.json").open("x") as output:
        json.dump(result, output, indent=2)
    print(json.dumps(result))


async def execute(store):
    approved = json.loads((ROOT / "files/copy-preflight.json").read_text())["selection"]
    key = os.environ["CB_OPENROUTER_API_KEY"]
    before = allowance(key)
    os.environ["OPENROUTER_API_KEY"] = key
    nc = await nats.connect("nats://nats:4222", allow_reconnect=False)
    try:
        js = nc.jetstream()
        await js.add_stream(name=STREAM, subjects=[SUBJECT], max_bytes=8 * 1024 * 1024)
        await js.add_consumer(
            STREAM,
            ConsumerConfig(
                durable_name="community-brain-worker",
                filter_subject=SUBJECT,
                ack_policy="explicit",
            ),
        )
    finally:
        await nc.close()
    handler = PublicationHandlers(
        store, ROOT / "corpus", ROOT / "config", os.environ["OLLAMA_BASE_URL"]
    )

    def no_processing(request):
        raise RuntimeError("processing not authorized in this copy")

    with audited_indexing(
        store, key, ROOT / "files/copy-indexing-requests.jsonl", ceiling=32
    ):
        result = await run_selected(
            store,
            approved,
            Worker(store, no_processing, handlers={"indexing": handler.indexing}),
            lambda: nats.connect("nats://nats:4222", allow_reconnect=False),
            stream=STREAM,
            subject=SUBJECT,
        )
    print(
        json.dumps(
            {
                "copy": COPY,
                "stage_state": result["state"],
                "allowance_before": before,
                "allowance_after": allowance(key),
            }
        )
    )


def verify(store):
    baseline = json.loads((ROOT / "files/copy-preflight.json").read_text())
    tbl = table()
    rows = tbl.to_arrow().to_pylist()
    original = [r for r in rows if r["session_id"] != "2026-09-10"]
    added = [r for r in rows if r["session_id"] == "2026-09-10"]
    assert (
        len(original) == 1901 and row_hash(original) == baseline["baseline_rows_sha256"]
    )
    assert added and all(
        r["extraction_status"] == "success" and len(r["embedding"]) == 768
        for r in added
    )
    with Session(store.engine) as session:
        stage = session.scalar(
            select(Stage).where(Stage.job_id == UUID(JOB), Stage.name == "indexing")
        )
        assert stage.state == "succeeded" and stage.attempts == 1
        assert all(
            s.attempts == 0
            for s in session.scalars(select(Stage))
            if s.name != "processing" and s.id != stage.id
        )
        assert all(
            j.git == j.distribution == "not_requested"
            for j in session.scalars(select(Job))
        )
    # Explicit copy-only maintenance: existing FTS presence is not coverage proof.
    before = tbl.index_stats("bm25_text_idx")
    with corpus_lock(ROOT / "corpus"):
        tbl.create_fts_index("bm25_text", replace=True)
    after = tbl.index_stats("bm25_text_idx")
    assert after["num_indexed_rows"] == len(rows) and after["num_unindexed_rows"] == 0
    hits = (
        tbl.search("synthetic", query_type="fts")
        .where("session_id = '2026-09-10'")
        .limit(10)
        .to_list()
    )
    assert hits
    journal = [
        json.loads(line)
        for line in (ROOT / "files/copy-indexing-requests.jsonl")
        .read_text()
        .splitlines()
    ]
    intents = [r for r in journal if r["state"] == "intent"]
    responses = [r for r in journal if r["state"] == "response"]
    assert len(intents) == len(responses) <= 32
    for record in responses:
        store.storage.read(record["path"], record["sha256"])
    result = {
        "copy": COPY,
        "original_rows_unchanged": True,
        "added_chunks": len(added),
        "total_rows": len(rows),
        "requests": len(intents),
        "responses": len(responses),
        "cost_usd": sum(r["usage"]["cost"] for r in responses),
        "fts_before_unindexed": before["num_unindexed_rows"],
        "fts_after_indexed": after["num_indexed_rows"],
        "fts_after_unindexed": 0,
        "synthetic_fts_hits": len(hits),
        "publication": False,
    }
    (ROOT / "files/copy-result.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result))


if __name__ == "__main__":
    store = guard()
    command = sys.argv[1]
    if command == "preflight":
        preflight(store)
    elif command == "execute":
        asyncio.run(execute(store))
    elif command == "verify":
        verify(store)
    else:
        raise ValueError("unknown command")

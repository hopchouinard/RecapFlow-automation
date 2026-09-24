"""Metadata-only receipt for the approved isolated recording index."""

import json
from pathlib import Path
from uuid import UUID

import lancedb
from community_brain.jobs.models import Job, Stage
from community_brain.jobs.runtime import make_store
from sqlalchemy import select
from sqlalchemy.orm import Session

store = make_store()
job_id = UUID("acd77c69-10d8-4079-9514-35ca5cc0c9fc")
with Session(store.engine) as session:
    stage = session.scalar(
        select(Stage).where(Stage.job_id == job_id, Stage.name == "indexing")
    )
    job = session.get(Job, job_id)
    assert stage.state == "succeeded" and stage.attempts == 1
    assert job.git == job.distribution == "not_requested"
    result = {
        k: stage.result[k]
        for k in (
            "state",
            "chunks_failed",
            "chunks_written",
            "chunks_by_type",
            "extraction_model",
            "schema_version",
        )
    }
    result.update(
        job_id=str(job_id),
        attempts=stage.attempts,
        unknown_speaker_count=len(stage.result["unknown_speakers_flagged"]),
        git=job.git,
        distribution=job.distribution,
    )
table = lancedb.connect("/state/corpus/lancedb/nomic-v1").open_table("chunks")
rows = table.search().where("session_id = '2026-09-08'").limit(100).to_list()
assert len(rows) == 29 and table.count_rows() == 38
assert all(len(r["embedding"]) == 768 for r in rows)
result.update(
    total_chunks=table.count_rows(),
    recording_chunks=len(rows),
    embedding_dimensions=768,
)
journal = [
    json.loads(x)
    for x in Path("/state/files/recording-indexing-calls.jsonl")
    .read_text()
    .splitlines()
]
assert sum(r["state"] == "intent" for r in journal) == 30
assert sum(r["state"] == "response" for r in journal) == 30
result.update(
    requests=30,
    responses=30,
    cost=sum((r.get("usage") or {}).get("cost", 0) for r in journal),
)
print(json.dumps(result, sort_keys=True))

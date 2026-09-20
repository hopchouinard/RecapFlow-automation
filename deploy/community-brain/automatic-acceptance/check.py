"""Read-only initial activation acceptance inside the production API container."""

import json
import os
from pathlib import Path

import lancedb
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from community_brain.jobs.automatic import POLICY
from community_brain.jobs.models import Job, Stage, Outbox, ModelCall, Source, Artifact
from community_brain.jobs.runtime import make_store

assert os.environ.get("CB_AUTOMATIC_PROCESSING") == "true"
assert os.environ["CB_CORPUS_ROOT"] == "/state/corpus"
assert not any(
    key in os.environ
    for key in (
        "CB_OPENROUTER_API_KEY",
        "OPENROUTER_API_KEY",
        "CB_FATHOM_API_KEY",
        "CB_NATS_PASSWORD",
    )
)
store = make_store()
with Session(store.engine) as session:
    counts = {
        model.__tablename__: session.scalar(select(func.count()).select_from(model))
        for model in (Job, Stage, Outbox, ModelCall, Source, Artifact)
    }
    eligible = session.scalar(
        select(func.count())
        .select_from(Job)
        .where(Job.config["automation_policy"].astext == POLICY)
    )
    unsent = session.scalar(
        select(func.count()).select_from(Outbox).where(Outbox.sent_at.is_(None))
    )
    assert counts == {
        "cb_jobs": 3,
        "cb_stages": 15,
        "cb_outbox": 7,
        "cb_model_calls": 29,
        "cb_sources": 6,
        "cb_artifacts": 15,
    }, counts
    assert eligible == 0 and unsent == 3
root = Path(os.environ["CB_CORPUS_ROOT"])
table = lancedb.connect(str(root / "lancedb/nomic-v1")).open_table("chunks")
rows = table.count_rows()
sessions = len(set(table.to_arrow().column("session_id").to_pylist()))
fts = table.index_stats("bm25_text_idx")
assert rows == 1901 and sessions == 87
assert fts["num_indexed_rows"] == rows and fts["num_unindexed_rows"] == 0
print(
    json.dumps(
        {
            "automatic_processing": True,
            "api_worker_keys_absent": True,
            "database": counts,
            "eligible_jobs": eligible,
            "old_unsent_events": unsent,
            "sessions": sessions,
            "rows": rows,
            "fts_indexed_rows": fts["num_indexed_rows"],
        }
    )
)

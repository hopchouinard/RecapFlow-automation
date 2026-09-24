"""Offline restored-state integrity checks; no worker or inference client runs."""

import json
from uuid import UUID

import lancedb
from community_brain.jobs.models import Artifact, Job, ModelCall, Source, Stage
from community_brain.jobs.runtime import make_store
from sqlalchemy import func, select
from sqlalchemy.orm import Session

store = make_store()
with Session(store.engine) as session:
    counts = {
        m.__name__: session.scalar(select(func.count()).select_from(m))
        for m in (Job, ModelCall, Source, Artifact)
    }
    assert counts["Job"] == 4 and counts["ModelCall"] == 32 and counts["Source"] == 6
    for model in (Source, Artifact):
        for item in session.scalars(select(model)):
            assert len(store.storage.read(item.path, item.sha256)) == item.size
    calls = session.scalars(select(ModelCall)).all()
    assert all(c.state == "succeeded" for c in calls)
    for call in calls:
        store.storage.read(call.response_path, call.response_hash)
    weekly = session.get(Job, UUID("7bce1799-dd0f-40fa-a444-a7797ff38b1b"))
    assert (
        weekly.processing == "succeeded"
        and weekly.git == weekly.distribution == "not_requested"
    )
    # The coordinated backup predates weekly indexing. Do not replay this pending stage.
    stage = session.scalar(
        select(Stage).where(Stage.job_id == weekly.id, Stage.name == "indexing")
    )
    assert stage.state == "queued"
    assert weekly.indexing == "pending"
    assert session.scalar(select(func.count()).select_from(ModelCall)) == 32
corpus = lancedb.connect("/state/corpus/lancedb/nomic-v1").open_table("chunks")
assert corpus.count_rows() == 38
rows = corpus.search().limit(100).to_list()
assert all(len(row["embedding"]) == 768 for row in rows)
print(
    json.dumps(
        {
            "counts": counts,
            "all_source_artifact_response_hashes_verified": True,
            "restored_corpus_chunks": 38,
            "embedding_dimensions": 768,
            "weekly_indexing_pending_at_snapshot": True,
            "worker_started": False,
            "provider_calls": 0,
            "queue_replay_performed": False,
        },
        sort_keys=True,
    )
)

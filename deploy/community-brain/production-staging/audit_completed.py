"""Reconcile durable bounded outcomes, usage and private file references."""

import hashlib
import json
import os
from collections import Counter
from pathlib import Path

from community_brain.jobs.models import Artifact, Job, ModelCall, Source, Stage
from community_brain.jobs.storage import Storage
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

engine = create_engine(os.environ["CB_DATABASE_URL"])
storage = Storage("/state/files")
with Session(engine) as session:
    jobs = session.scalars(select(Job)).all()
    assert len(jobs) == 2 and {j.mode for j in jobs} == {
        "weekly",
        "transcript_backfill",
    }
    assert all(j.processing == "succeeded" and j.artifacts == "ready" for j in jobs)
    stages = session.scalars(select(Stage)).all()
    assert all(s.attempts == 0 for s in stages if s.name != "processing")
    assert all(s.attempts == 1 for s in stages if s.name == "processing")
    sources = session.scalars(select(Source)).all()
    artifacts = session.scalars(select(Artifact)).all()
    calls = session.scalars(select(ModelCall)).all()
    assert all(c.state != "intent" for c in calls)
    per_job = Counter(str(c.job_id) for c in calls)
    assert max(per_job.values()) <= 12
    for s in sources:
        storage.read(s.path, s.sha256)
    for a in artifacts:
        storage.read(a.path, a.sha256)
    for c in calls:
        storage.read(c.response_path, c.response_hash)
    costs = [c.usage.get("cost") if c.usage else None for c in calls]
    assert all(v is not None for v in costs)
    result = {
        "jobs": 2,
        "sources": len(sources),
        "artifacts": len(artifacts),
        "model_calls": len(calls),
        "calls_per_job": dict(per_job),
        "model_states": dict(Counter(c.state for c in calls)),
        "saved_response_cost_usd": sum(costs),
        "all_referenced_hashes_verified": True,
        "processing_attempts_each": 1,
        "nonprocessing_attempts": 0,
    }
root = Path("/state/corpus")
manifest = globals()["CORPUS_MANIFEST"]
for name, sha in manifest["files"].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == sha
for row in globals()["SOURCE_MANIFEST"]["files"]:
    if row["path"].startswith("config/"):
        assert (
            hashlib.sha256((Path("/state") / row["path"]).read_bytes()).hexdigest()
            == row["sha256"]
        )
result["preserved_corpus_config_unchanged"] = True
print(json.dumps(result))

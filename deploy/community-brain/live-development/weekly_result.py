"""Metadata-only verification of approved processing; never print source/output text."""

import json
from uuid import UUID

from community_brain.jobs.models import Artifact, Job, ModelCall, Source, Stage
from community_brain.jobs.runtime import make_store
from sqlalchemy import select
from sqlalchemy.orm import Session

store = make_store()
job_id = UUID("7bce1799-dd0f-40fa-a444-a7797ff38b1b")
with Session(store.engine) as session:
    job = session.get(Job, job_id)
    source = session.get(Source, UUID(job.sources["transcript"]))
    assert (
        source.sha256
        == "79540c3f3f08a09dee48d5784026e0f980ec8a9fb85414091fdffba61fe18f75"
    )
    store.storage.read(source.path, source.sha256)
    chat = session.get(Source, UUID(job.sources["chat"]))
    assert (
        chat.sha256
        == "5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084"
    )
    store.storage.read(chat.path, chat.sha256)
    artifacts = session.scalars(select(Artifact).where(Artifact.job_id == job_id)).all()
    for artifact in artifacts:
        store.storage.read(artifact.path, artifact.sha256)
    calls = session.scalars(select(ModelCall).where(ModelCall.job_id == job_id)).all()
    stages = session.scalars(select(Stage).where(Stage.job_id == job_id)).all()
    print(
        json.dumps(
            {
                "job_id": str(job.id),
                "parent_id": str(job.parent_id),
                "processing": job.processing,
                "indexing": job.indexing,
                "git": job.git,
                "distribution": job.distribution,
                "source_hash_verified": True,
                "chat_hash_verified": True,
                "stages": [
                    {
                        "id": str(s.id),
                        "name": s.name,
                        "state": s.state,
                        "generation": s.generation,
                        "error": s.error,
                    }
                    for s in stages
                ],
                "artifacts": [
                    {
                        "name": a.name,
                        "bytes": a.size,
                        "sha256": a.sha256,
                        "private_path": "/state/files/" + a.path,
                    }
                    for a in artifacts
                ],
                "calls": [
                    {"state": c.state, "request": c.request_meta, "usage": c.usage}
                    for c in calls
                ],
            },
            sort_keys=True,
        )
    )

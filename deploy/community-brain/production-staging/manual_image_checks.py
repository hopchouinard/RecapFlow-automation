"""No-provider checks of the exact image/helpers in the VM108 disposable copy."""

import hashlib
import json
import os
import secrets
import time
from uuid import UUID

from community_brain.ingestion import extractor, session_extractor
from community_brain.jobs.models import Job, Source
from community_brain.jobs.publication import PublicationHandlers
from community_brain.jobs.runtime import app
from community_brain.query.query_local import _resolve_cue_rules
from disposable_index import COPY, JOB, ROOT, guard, row_hash, table
from fastapi.testclient import TestClient
from manual_worker import EXCLUDED, PROCESSING_CEILING, complete_fts, reviewed_selection
from sqlalchemy import select
from sqlalchemy.orm import Session

store = guard()
assert "CB_OPENROUTER_API_KEY" not in os.environ
for job_id in EXCLUDED:
    try:
        reviewed_selection(store, job_id, "indexing", 1)
    except ValueError as error:
        assert str(error) == "excluded job"
    else:
        raise AssertionError("production synthetic selection accepted")


def deny(*args, **kwargs):
    raise AssertionError("provider call forbidden during idempotency check")


extractor._call_llm = session_extractor._call_llm = deny
before = row_hash(table().to_arrow().to_pylist())
handler = PublicationHandlers(
    store, ROOT / "corpus", ROOT / "config", os.environ["OLLAMA_BASE_URL"]
)
result = complete_fts(handler, ROOT / "corpus", UUID(JOB))
assert result["chunks_skipped_idempotent"] == 8 and result["chunks_written"] == 0
assert row_hash(table().to_arrow().to_pylist()) == before

permissions = {
    "reader": ["jobs:read", "artifacts:read", "retrieval:read"],
    "collector": ["sources:upload:chat"],
    "operator": ["sources:upload", "jobs:submit", "jobs:read", "artifacts:read"],
}
tokens = {name: secrets.token_urlsafe(32) for name in permissions}
os.environ.update(
    COMMUNITY_BRAIN_CUE_RULES_PATH="/state/config/query-cues.yaml",
    COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH="/state/config/speaker-aliases.yaml",
    CB_ENABLE_RETRIEVAL="true",
    CB_CORPUS_SCOPE="community-brain",
    COMMUNITY_BRAIN_DISTRIBUTION_MODE="true",
    LANCEDB_PATH=str(ROOT / "corpus/lancedb/nomic-v1"),
    CB_OIDC_ISSUER="https://fixture.invalid/oidc",
    CB_OIDC_JWKS_URL="https://fixture.invalid/jwks",
    CB_OIDC_AUDIENCE="fixture",
    CB_OIDC_CLIENT_ID="fixture",
    CB_SERVICE_IDENTITIES=json.dumps(
        [
            {
                "subject": name,
                "scope": "community-brain",
                "permissions": perms,
                "sha256": hashlib.sha256(tokens[name].encode()).hexdigest(),
                "expires_at": int(time.time()) + 600,
            }
            for name, perms in permissions.items()
        ]
    ),
)
assert len(_resolve_cue_rules()) > 2


def headers(name):
    return {"Authorization": "Bearer " + tokens[name]}


with Session(store.engine) as session:
    source = session.scalar(select(Source).where(Source.kind == "chat"))
    body = {
        "meeting_id": source.meeting_id,
        "kind": "chat",
        "content": store.storage.read(source.path, source.sha256).decode(),
    }
    source_id = str(source.id)
    job_ids = [str(j.id) for j in session.scalars(select(Job))]
with TestClient(app()) as client:
    assert client.get("/health").status_code == 200
    assert client.get("/api/v1/jobs").status_code == 401
    assert client.post("/api/v1/sources", json=body).status_code == 401
    receipt = client.post("/api/v1/sources", json=body, headers=headers("collector"))
    assert receipt.status_code == 201 and receipt.json()["id"] == source_id
    repeated = client.post("/api/v1/sources", json=body, headers=headers("collector"))
    assert receipt.json() == repeated.json()
    for kind in ("transcript", "aliases"):
        assert (
            client.post(
                "/api/v1/sources",
                json={**body, "kind": kind},
                headers=headers("collector"),
            ).status_code
            == 403
        )
    assert client.get("/api/v1/jobs", headers=headers("collector")).status_code == 403
    assert (
        client.post("/api/v1/jobs", json={}, headers=headers("collector")).status_code
        == 403
    )
    assert client.get("/api/v1/jobs", headers=headers("operator")).status_code == 200
    assert client.get("/metrics", headers=headers("operator")).status_code == 403
    downloaded = 0
    for job_id in job_ids:
        artifacts = client.get(
            f"/api/v1/jobs/{job_id}/artifacts", headers=headers("reader")
        ).json()["items"]
        for artifact in artifacts:
            response = client.get(artifact["url"], headers=headers("reader"))
            assert (
                response.status_code == 200
                and hashlib.sha256(response.content).hexdigest() == artifact["sha256"]
            )
            downloaded += 1
    query = {
        "question": "synthetic fixture migration rehearsal",
        "top_k": 5,
        "filters": {"session_date_range": ["2026-09-10", "2026-09-10"]},
    }
    assert client.post("/retrieval/query", json=query).status_code == 401
    response = client.post("/retrieval/query", json=query, headers=headers("reader"))
    assert response.status_code == 200
    chunks = response.json()["chunks"]
    assert chunks and all(
        c["ground_truth"]["session_id"] == "2026-09-10" for c in chunks
    )
    assert all(c["provenance"]["extraction_status"] == "success" for c in chunks)
    assert any(c["score_breakdown"]["bm25_rank"] is not None for c in chunks)
    assert any(c["score_breakdown"]["vector_similarity"] > 0 for c in chunks)
    assert (
        client.post("/retrieval/ingest", json={}, headers=headers("reader")).status_code
        == 404
    )
print(
    json.dumps(
        {
            "copy": COPY,
            "synthetic_live_selection_denied": True,
            "idempotent_chunks_skipped": 8,
            "new_model_calls": 0,
            "rows_unchanged": True,
            "health": True,
            "unauthenticated_denied": True,
            "collector_nonchat_denied": True,
            "collector_jobs_denied": True,
            "upload_deduplicated": True,
            "artifacts_hash_verified": downloaded,
            "authenticated_hybrid_hits": len(chunks),
            "configured_cue_rules": len(_resolve_cue_rules()),
            "processing_request_ceiling": PROCESSING_CEILING,
            "remote_publication": False,
        }
    )
)

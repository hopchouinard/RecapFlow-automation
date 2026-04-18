"""FastAPI retrieval server for Community Brain.

Exposes a /query endpoint that searches LanceDB and returns ranked chunks.
No LLM inference — the caller handles answer generation.

Usage:
    python -m community_brain.query.retrieval_server
    RETRIEVAL_API_KEY=secret uvicorn community_brain.query.retrieval_server:app --port 8999
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

from community_brain.ingestion.pipeline import (
    CommitError,
    IngestRequest,
    ingest_session,
)
from community_brain.query.query_local import search_chunks

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
load_dotenv(CONFIG_DIR / ".env")

DEFAULT_DB_PATH = str(PROJECT_ROOT / "lancedb" / "nomic-v1")

CONFIG_DIR_OVERRIDE_ENV = "COMMUNITY_BRAIN_CONFIG_DIR"


def _config_dir() -> Path:
    """Resolve the config directory.

    Tests and alternate deployments can override via COMMUNITY_BRAIN_CONFIG_DIR.
    Defaults to the package's config/ directory.
    """
    override = os.environ.get(CONFIG_DIR_OVERRIDE_ENV)
    if override:
        return Path(override)
    return CONFIG_DIR

# API key auth: set RETRIEVAL_API_KEY env var to require authentication.
# When set, all /query requests must include X-API-Key header.
_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
RETRIEVAL_API_KEY = os.environ.get("RETRIEVAL_API_KEY")


def _verify_api_key(api_key: str | None = Security(_api_key_header)) -> str | None:
    """Verify API key if RETRIEVAL_API_KEY is configured.

    Reads from os.environ at call time so that test fixtures that set/unset
    the env var between requests are honoured without a module reload.
    """
    configured_key = os.environ.get("RETRIEVAL_API_KEY")
    if configured_key is None:
        # No key configured; allow (localhost-only deployment)
        return None
    if api_key != configured_key:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
    return api_key


app = FastAPI(
    title="Community Brain Retrieval API",
    description="Search coaching call transcripts by semantic similarity.",
    version="0.1.0",
)


class IngestHTTPRequest(BaseModel):
    session_id: str
    session_date: str
    session_title: str | None = None
    artifact_paths: dict[str, str]
    force_reextract: bool = False


class IngestHTTPResponse(BaseModel):
    session_id: str
    chunks_written: int
    chunks_by_type: dict[str, int]
    chunks_skipped_idempotent: int
    chunks_failed: int
    extraction_model: str
    extraction_prompt_version: str
    schema_version: str
    warnings: list[str]
    unknown_entities_flagged: list[str]
    unknown_speakers_flagged: list[str]


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5
    filter_date: str | None = None
    filter_speaker: str | None = None


class ChunkResult(BaseModel):
    chunk_id: str
    session_date: str
    topic: str
    summary: str
    text: str
    speakers: list[str]
    score: float


class QueryResponse(BaseModel):
    chunks: list[ChunkResult]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest, _key: str | None = Depends(_verify_api_key)):
    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    ollama_base_url = os.environ.get("OLLAMA_BASE_URL")

    results = search_chunks(
        question=request.question,
        db_path=db_path,
        top_k=request.top_k,
        filter_date=request.filter_date,
        filter_speaker=request.filter_speaker,
        ollama_base_url=ollama_base_url,
    )

    chunks = []
    for r in results:
        speakers_raw = r.get("speakers_in_chunk", "[]")
        if isinstance(speakers_raw, str):
            try:
                speakers = json.loads(speakers_raw)
            except json.JSONDecodeError:
                speakers = [speakers_raw]
        else:
            speakers = speakers_raw

        chunks.append(ChunkResult(
            chunk_id=r["chunk_id"],
            session_date=r["session_date"],
            topic=r.get("topic", ""),
            summary=r.get("summary", ""),
            text=r["text"],
            speakers=speakers,
            score=round(1 - r.get("_distance", 0), 4),
        ))

    return QueryResponse(chunks=chunks)


@app.post("/ingest", response_model=IngestHTTPResponse)
def ingest(req: IngestHTTPRequest, _key: str | None = Depends(_verify_api_key)):
    """Ingest a session's artifacts into LanceDB.

    Returns 400 for invalid input (empty artifact_paths, invalid session_id).
    Returns 500 for LanceDB commit failures (torn-state recoverable via reindex).
    Returns 200 with IngestResult JSON on success, even when some chunks failed
    extraction (check `chunks_failed` in the response).
    """
    if not req.artifact_paths:
        raise HTTPException(status_code=400, detail="no artifact_paths provided")

    ollama_base_url = os.environ.get("OLLAMA_BASE_URL")
    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)

    pipeline_req = IngestRequest(
        session_id=req.session_id,
        session_date=req.session_date,
        session_title=req.session_title,
        artifact_paths=req.artifact_paths,
        force_reextract=req.force_reextract,
    )

    try:
        result = ingest_session(
            request=pipeline_req,
            config_dir=_config_dir(),
            db_path=db_path,
            ollama_base_url=ollama_base_url,
        )
    except ValueError as exc:
        # session_id or chunk_id validation failure, or other contract violations
        raise HTTPException(status_code=400, detail=str(exc))
    except CommitError as exc:
        # LanceDB torn-state; operator can recover via /reindex or force_reextract
        raise HTTPException(status_code=500, detail=str(exc))

    if result.warnings and result.chunks_written == 0 and "no artifacts to ingest" in (result.warnings[0] if result.warnings else ""):
        raise HTTPException(status_code=400, detail=result.warnings[0])

    return IngestHTTPResponse(
        session_id=result.session_id,
        chunks_written=result.chunks_written,
        chunks_by_type=result.chunks_by_type,
        chunks_skipped_idempotent=result.chunks_skipped_idempotent,
        chunks_failed=result.chunks_failed,
        extraction_model=result.extraction_model,
        extraction_prompt_version=result.extraction_prompt_version,
        schema_version=result.schema_version,
        warnings=result.warnings,
        unknown_entities_flagged=result.unknown_entities_flagged,
        unknown_speakers_flagged=result.unknown_speakers_flagged,
    )


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("RETRIEVAL_PORT", "8999"))
    host = os.environ.get("RETRIEVAL_HOST", "127.0.0.1")
    uvicorn.run(app, host=host, port=port)

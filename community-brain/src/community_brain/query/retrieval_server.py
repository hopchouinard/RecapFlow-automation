"""FastAPI retrieval server for Community Brain.

Exposes a /query endpoint that searches LanceDB and returns ranked chunks.
No LLM inference — the caller handles answer generation.

Usage:
    python -m community_brain.query.retrieval_server
    RETRIEVAL_API_KEY=secret uvicorn community_brain.query.retrieval_server:app --port 8999
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, field_validator

from community_brain.ingestion.pipeline import (
    CommitError,
    IngestRequest,
    ingest_session,
)
from community_brain.query.query_local import sql_quote

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


VALID_ARTIFACT_KEYS = frozenset({"prepared_transcript", "extracted_signal", "community_post"})


class IngestHTTPRequest(BaseModel):
    session_id: str
    session_date: str
    session_title: str | None = None
    artifact_paths: dict[str, str]
    force_reextract: bool = False

    @field_validator("artifact_paths")
    @classmethod
    def _validate_artifact_keys(cls, v: dict[str, str]) -> dict[str, str]:
        unknown = set(v.keys()) - VALID_ARTIFACT_KEYS
        if unknown:
            raise ValueError(
                f"unknown artifact keys {sorted(unknown)}; allowed: {sorted(VALID_ARTIFACT_KEYS)}"
            )
        return v


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


class QueryFilters(BaseModel):
    session_date_range: list[str] | None = None
    content_type: list[str] | None = None

    speakers_spoke: list[str] | None = None
    speakers_spoke_match: str = "any"
    speakers_mentioned: list[str] | None = None
    speakers_mentioned_match: str = "any"

    entities: list[str] | None = None
    entities_match: str = "any"

    keywords: list[str] | None = None
    keywords_match: str = "any"

    schema_version_min: str | None = None

    require_chunk_markers: list[str] | None = None
    exclude_chunk_markers: list[str] | None = None
    require_corpus_markers: list[str] | None = None
    exclude_corpus_markers: list[str] | None = None

    has_question: bool | None = None
    has_answer: bool | None = None
    has_unresolved_question: bool | None = None
    has_insight: bool | None = None
    references_prior: bool | None = None


class QueryRequestV2(BaseModel):
    question: str
    top_k: int = 10
    filters: QueryFilters | None = None
    # v1 only supports "structured". "flat" is reserved for a future release
    # that returns flattened chunks without the ground_truth/derived_metadata
    # partitioning.
    response_shape: Literal["structured"] = "structured"


class QueryChunkResult(BaseModel):
    ground_truth: dict
    derived_metadata: dict
    provenance: dict
    similarity: float


class QueryResponseV2(BaseModel):
    query: str
    chunks: list[QueryChunkResult]
    total_matched: int
    filters_applied: dict


GROUND_TRUTH_FIELDS = (
    "chunk_id", "session_id", "session_date", "session_title",
    "source_file", "full_text",
)

PROVENANCE_FIELDS = (
    "schema_version", "extraction_model", "extraction_prompt_version",
    "extraction_status", "extraction_error", "extracted_at",
)

DERIVED_FIELDS = (
    "content_type", "chunk_index", "total_chunks_in_source",
    "speakers_spoke", "speakers_mentioned", "entities", "keywords",
    "topic_label", "session_themes",
    "speech_acts", "stance", "certainty",
    "chunk_local_markers", "corpus_derived_markers", "corpus_markers_computed_at",
    "has_question", "has_answer", "has_unresolved_question", "has_insight",
    "decisions", "action_items", "external_refs", "references_prior",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponseV2)
def query(req: QueryRequestV2, _key: str | None = Depends(_verify_api_key)):
    from community_brain.query.query_local import search_chunks_v2

    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    ollama_base_url = os.environ.get("OLLAMA_BASE_URL")

    # Use an empty QueryFilters to get spec-default values (e.g. *_match = "any")
    # even when the caller omits the filters field entirely.
    effective_filters = req.filters if req.filters is not None else QueryFilters()
    filters_dict = effective_filters.model_dump(exclude_none=False)

    raw = search_chunks_v2(
        question=req.question,
        db_path=db_path,
        top_k=req.top_k,
        filters=filters_dict,
        ollama_base_url=ollama_base_url,
    )

    chunks: list[QueryChunkResult] = []
    for row in raw:
        ground = {k: row.get(k) for k in GROUND_TRUTH_FIELDS}
        derived = {k: row.get(k) for k in DERIVED_FIELDS}
        provenance = {k: row.get(k) for k in PROVENANCE_FIELDS}
        similarity = round(1 - row.get("_distance", 0), 4)
        chunks.append(QueryChunkResult(
            ground_truth=ground,
            derived_metadata=derived,
            provenance=provenance,
            similarity=similarity,
        ))

    return QueryResponseV2(
        query=req.question,
        chunks=chunks,
        total_matched=len(chunks),
        filters_applied=filters_dict,
    )


@app.post("/ingest", response_model=IngestHTTPResponse)
def ingest(req: IngestHTTPRequest, _key: str | None = Depends(_verify_api_key)):
    """Ingest a session's artifacts into LanceDB.

    Returns 400 for invalid input (empty artifact_paths, invalid session_id).
    Returns 422 for Pydantic validation failures (unknown artifact keys).
    Returns 500 for LanceDB commit failures (torn-state recoverable via reindex).
    Returns 200 with IngestResult JSON on success, even when some chunks failed
    extraction (check `chunks_failed` in the response).
    """
    # TODO(Task 23): constrain artifact_paths to COMMUNITY_BRAIN_ARTIFACT_ROOT.
    # Currently any authenticated caller can ingest files the server process can
    # read. For VM deployment behind an API key this is acceptable; for Docker
    # with shared mounts, artifact paths should be validated against a known
    # root directory.
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
        raise HTTPException(
            status_code=500,
            detail={
                "error": "commit_torn_state",
                "message": str(exc),
                "recovery": (
                    f"Re-run POST /ingest with force_reextract=true for "
                    f"session_id '{req.session_id}' to recover."
                ),
            },
        )

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


# --- /sessions inventory endpoints ---

def _load_all_session_rows() -> list[dict]:
    """Load minimum session-level columns for aggregation.

    Returns empty list if the chunks table does not exist yet. Pulls only the
    columns needed by the sessions aggregation (not full_text or embeddings)
    so this stays cheap even on large corpuses.
    """
    import lancedb

    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    try:
        db = lancedb.connect(db_path)
    except Exception as exc:
        logger.warning("Failed to connect to LanceDB at %s: %s", db_path, exc)
        return []

    try:
        if "chunks" not in db.list_tables().tables:
            return []
        table = db.open_table("chunks")
    except Exception as exc:
        logger.warning("Failed to open chunks table: %s", exc)
        return []

    cols = [
        "session_id",
        "session_date",
        "session_title",
        "content_type",
        "has_unresolved_question",
        "session_themes",
    ]
    try:
        arr = table.search().select(cols).limit(100_000).to_arrow()
    except Exception as exc:
        logger.warning("Failed to read session rows from chunks table: %s", exc)
        return []

    return [
        {col: arr[col][i].as_py() for col in arr.column_names}
        for i in range(arr.num_rows)
    ]


def _aggregate_sessions(rows: list[dict]) -> dict[str, dict]:
    """Aggregate per-chunk rows into per-session dicts.

    Each session's chunk_counts is a breakdown by content_type.
    unresolved_question_count tallies rows where has_unresolved_question is true.
    session_themes is taken from the first-seen row (all chunks in a session
    share the same denormalized themes).
    """
    agg: dict[str, dict] = {}
    for row in rows:
        sid = row["session_id"]
        if sid not in agg:
            agg[sid] = {
                "session_id": sid,
                "session_date": row["session_date"],
                "session_title": row.get("session_title"),
                "chunk_counts": {},
                "unresolved_question_count": 0,
                "session_themes": list(row.get("session_themes") or []),
            }
        ctype = row["content_type"]
        agg[sid]["chunk_counts"][ctype] = agg[sid]["chunk_counts"].get(ctype, 0) + 1
        if row.get("has_unresolved_question"):
            agg[sid]["unresolved_question_count"] += 1
    return agg


@app.get("/sessions")
def list_sessions(_key: str | None = Depends(_verify_api_key)):
    """List all sessions in the corpus with aggregated metadata.

    Sorted by session_date descending (newest first).
    """
    rows = _load_all_session_rows()
    agg = _aggregate_sessions(rows)
    sessions = sorted(agg.values(), key=lambda s: s["session_date"], reverse=True)
    return {"total": len(sessions), "sessions": sessions}


@app.get("/sessions/{session_id}")
def get_session(session_id: str, _key: str | None = Depends(_verify_api_key)):
    """Get one session's aggregated metadata. 404 if the session is not in the corpus."""
    rows = _load_all_session_rows()
    agg = _aggregate_sessions(rows)
    if session_id not in agg:
        raise HTTPException(status_code=404, detail=f"session not found: {session_id}")
    return agg[session_id]


# --- /reindex endpoint (v1 minimal: dry-run + operation matching) ---

SUPPORTED_REINDEX_OPS = frozenset({"re-extract", "re-embed", "delete"})


class ReindexRequest(BaseModel):
    filter: dict = {}
    operation: str
    dry_run: bool = True
    priority_order: str = "newest_first"


class ReindexResponse(BaseModel):
    operation: str
    dry_run: bool
    matched_chunk_ids: list[str]
    note: str


def _reindex_select_chunk_ids(filter_clause: dict) -> list[str]:
    """Return chunk_ids matching the filter. Used by /reindex dry-run and future v2 mutations.

    Supported filter keys in v1:
      - extraction_prompt_version (exact match)
      - extraction_status (exact match)
      - session_date_range ([start, end])
    """
    import lancedb

    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    try:
        db = lancedb.connect(db_path)
    except Exception as exc:
        logger.warning("Failed to connect to LanceDB at %s: %s", db_path, exc)
        return []

    try:
        if "chunks" not in db.list_tables().tables:
            return []
        table = db.open_table("chunks")
    except Exception as exc:
        logger.warning("Failed to open chunks table for reindex: %s", exc)
        return []

    clauses: list[str] = []
    for key in ("extraction_prompt_version", "extraction_status"):
        val = filter_clause.get(key)
        if val:
            clauses.append(f"{key} = '{sql_quote(val)}'")
    dr = filter_clause.get("session_date_range")
    if dr and len(dr) == 2:
        clauses.append(
            f"session_date >= '{sql_quote(dr[0])}' AND session_date <= '{sql_quote(dr[1])}'"
        )

    query = table.search().select(["chunk_id"])
    if clauses:
        query = query.where(" AND ".join(clauses))
    try:
        arr = query.limit(100_000).to_arrow()
    except Exception as exc:
        logger.warning("Failed to read chunk_ids for reindex filter: %s", exc)
        return []
    return [arr["chunk_id"][i].as_py() for i in range(arr.num_rows)]


@app.post("/reindex", response_model=ReindexResponse)
def reindex(req: ReindexRequest, _key: str | None = Depends(_verify_api_key)):
    """Match chunks against a filter and (in v2) apply re-extract/re-embed/delete.

    V1 scope: validates the operation, runs the filter, returns matched chunk_ids.
    Mutations are NOT performed in v1 — callers use POST /ingest with
    force_reextract=true on a per-session basis to rebuild chunks under a new
    extraction prompt version. V2 will add in-place re-extract, re-embed after
    an embedding model swap, and retraction-style delete; SSE progress
    streaming is planned for long-running operations.
    """
    if req.operation not in SUPPORTED_REINDEX_OPS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"unsupported operation: {req.operation!r}. "
                f"Allowed: {sorted(SUPPORTED_REINDEX_OPS)}"
            ),
        )

    matched = _reindex_select_chunk_ids(req.filter)

    if req.dry_run:
        note = "dry run: no mutations applied"
    else:
        note = (
            f"{req.operation} against {len(matched)} chunks is not implemented in v1. "
            f"Use POST /ingest with force_reextract=true on a per-session basis "
            f"to re-extract under a new prompt version."
        )

    return ReindexResponse(
        operation=req.operation,
        dry_run=req.dry_run,
        matched_chunk_ids=matched,
        note=note,
    )


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("RETRIEVAL_PORT", "8999"))
    host = os.environ.get("RETRIEVAL_HOST", "127.0.0.1")
    uvicorn.run(app, host=host, port=port)

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

from community_brain.query.query_local import search_chunks

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
load_dotenv(CONFIG_DIR / ".env")

DEFAULT_DB_PATH = str(PROJECT_ROOT / "lancedb" / "nomic-v1")

# API key auth: set RETRIEVAL_API_KEY env var to require authentication.
# When set, all /query requests must include X-API-Key header.
_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
RETRIEVAL_API_KEY = os.environ.get("RETRIEVAL_API_KEY")


def _verify_api_key(api_key: str | None = Security(_api_key_header)) -> str | None:
    """Verify API key if RETRIEVAL_API_KEY is configured."""
    if RETRIEVAL_API_KEY is None:
        # No key configured; allow (localhost-only deployment)
        return None
    if api_key != RETRIEVAL_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
    return api_key


app = FastAPI(
    title="Community Brain Retrieval API",
    description="Search coaching call transcripts by semantic similarity.",
    version="0.1.0",
)


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


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("RETRIEVAL_PORT", "8999"))
    host = os.environ.get("RETRIEVAL_HOST", "127.0.0.1")
    uvicorn.run(app, host=host, port=port)

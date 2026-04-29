"""Tests for the recanonicalize CLI (standalone chunk-rewrite pass)."""
from __future__ import annotations

from pathlib import Path

import lancedb
import pyarrow as pa
import pytest

from community_brain.cli.recanonicalize import recanonicalize_chunks
from community_brain.ingestion.schema import Chunk, EMBEDDING_DIM, pyarrow_table_schema


def _make_chunk(
    *,
    chunk_id: str,
    session_id: str = "test-session",
    speakers_spoke: list[str] | None = None,
    speakers_mentioned: list[str] | None = None,
    entities: list[str] | None = None,
    keywords: list[str] | None = None,
    topic_label: str = "Test topic",
    full_text: str = "test full text",
    content_type: str = "prepared_transcript",
    embed_text: str | None = None,
    bm25_text: str | None = None,
) -> dict:
    """Build a minimal chunk row dict for the LanceDB-write helper."""
    import datetime as dt
    embedding = [0.01] * EMBEDDING_DIM
    if embed_text is None:
        embed_text = (
            f"topic: {topic_label}\n"
            f"speakers: {', '.join(speakers_spoke or [])}\n"
            f"mentions: {', '.join(speakers_mentioned or [])}\n"
            f"entities: {', '.join(entities or [])}\n"
            f"keywords: {', '.join(keywords or [])}\n"
            f"summary: a summary"
        )
    if bm25_text is None:
        bm25_text = (
            f"{topic_label}\n"
            f"{', '.join(entities or [])}\n"
            f"{', '.join(speakers_spoke or [])}\n"
            f"{', '.join(speakers_mentioned or [])}\n"
            f"{', '.join(keywords or [])}\n"
            f"{full_text}"
        )
    return {
        "schema_version": "1.1",
        "chunk_id": chunk_id,
        "session_id": session_id,
        "session_date": "2026-01-01",
        "session_title": None,
        "content_type": content_type,
        "source_file": "test.md",
        "chunk_index": 0,
        "total_chunks_in_source": 1,
        "speakers_spoke": speakers_spoke or [],
        "speakers_mentioned": speakers_mentioned or [],
        "entities": entities or [],
        "keywords": keywords or [],
        "topic_label": topic_label,
        "session_themes": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "corpus_derived_markers": [],
        "corpus_markers_computed_at": None,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "extraction_model": "test-model",
        "extraction_prompt_version": "chunk-extraction-v2",
        "extraction_status": "success",
        "extraction_error": None,
        "extracted_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "embed_text": embed_text,
        "full_text": full_text,
        "bm25_text": bm25_text,
        "embedding": embedding,
    }


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "test.lancedb"


def _create_table(db_path: Path, rows: list[dict]):
    db = lancedb.connect(str(db_path))
    schema = pyarrow_table_schema()
    table = db.create_table("chunks", schema=schema)
    if rows:
        table.add(rows)
    return table


def _stub_embed(text: str) -> list[float]:
    """Deterministic stub embedding (no Ollama call)."""
    return [0.5] * EMBEDDING_DIM


def test_recanonicalize_updates_changed_chunks(db_path: Path):
    """When the registry has 'Adam' -> 'Adam James' but a chunk's
    speakers_spoke contains the raw 'Adam', recanonicalize updates it."""
    rows = [
        _make_chunk(
            chunk_id="c1",
            speakers_spoke=["Adam"],
            entities=["Adam"],
        ),
    ]
    _create_table(db_path, rows)
    registry = {"aliases": {"Adam James": ["Adam"]}, "pending": []}
    stats = recanonicalize_chunks(db_path, registry, embed_fn=_stub_embed)
    assert stats["scanned"] == 1
    assert stats["updated"] == 1
    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    rows_after = table.to_arrow().to_pylist()
    assert rows_after[0]["speakers_spoke"] == ["Adam James"]
    assert rows_after[0]["entities"] == ["Adam James"]
    assert "Adam James" in rows_after[0]["bm25_text"]


def test_recanonicalize_noop_when_no_changes(db_path: Path):
    """When all chunks already have canonical names, recanonicalize is a fast scan."""
    rows = [
        _make_chunk(chunk_id="c1", speakers_spoke=["Adam James"], entities=["Adam James"]),
    ]
    _create_table(db_path, rows)
    registry = {"aliases": {"Adam James": ["Adam"]}, "pending": []}
    stats = recanonicalize_chunks(db_path, registry, embed_fn=_stub_embed)
    assert stats["scanned"] == 1
    assert stats["updated"] == 0


def test_recanonicalize_idempotent(db_path: Path):
    """Running recanonicalize twice produces the same result."""
    rows = [_make_chunk(chunk_id="c1", speakers_spoke=["Adam"], entities=[])]
    _create_table(db_path, rows)
    registry = {"aliases": {"Adam James": ["Adam"]}, "pending": []}
    stats1 = recanonicalize_chunks(db_path, registry, embed_fn=_stub_embed)
    stats2 = recanonicalize_chunks(db_path, registry, embed_fn=_stub_embed)
    assert stats1["updated"] == 1
    assert stats2["updated"] == 0


def test_recanonicalize_handles_signal_chunks(db_path: Path):
    """Signal/post chunks have embed_text == full_text; canonicalization
    of name lists doesn't change embed_text (since full_text is verbatim).
    bm25_text DOES change (it includes the structured fields)."""
    rows = [
        _make_chunk(
            chunk_id="s1",
            content_type="extracted_signal",
            speakers_spoke=[],
            entities=["Adam"],
            full_text="Some signal content.",
            embed_text="Some signal content.",
        ),
    ]
    _create_table(db_path, rows)
    registry = {"aliases": {"Adam James": ["Adam"]}, "pending": []}
    stats = recanonicalize_chunks(db_path, registry, embed_fn=_stub_embed)
    assert stats["updated"] == 1
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    assert rows_after[0]["entities"] == ["Adam James"]
    assert "Adam James" in rows_after[0]["bm25_text"]
    # Signal embed_text == full_text; full_text didn't change, so embed_text didn't either.
    assert rows_after[0]["embed_text"] == "Some signal content."


def test_recanonicalize_dry_run_does_not_write(db_path: Path):
    rows = [_make_chunk(chunk_id="c1", speakers_spoke=["Adam"], entities=["Adam"])]
    _create_table(db_path, rows)
    registry = {"aliases": {"Adam James": ["Adam"]}, "pending": []}
    stats = recanonicalize_chunks(db_path, registry, embed_fn=_stub_embed, dry_run=True)
    assert stats["scanned"] == 1
    assert stats["updated"] == 1  # would-update count
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    assert rows_after[0]["speakers_spoke"] == ["Adam"]  # unchanged

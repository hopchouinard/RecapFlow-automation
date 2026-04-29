"""Tests for the lint_corpus CLI."""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import lancedb
import pytest

from community_brain.cli.lint_corpus import lint_corpus_chunks
from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema


def _make_chunk_row(
    *,
    chunk_id: str,
    session_id: str,
    embedding: list[float] | None = None,
    full_text: str = "test content",
    content_type: str = "prepared_transcript",
    corpus_derived_markers: list[str] | None = None,
) -> dict:
    """Construct a minimal v1.1 chunk row for in-test LanceDB seeding."""
    if embedding is None:
        embedding = [0.0] * EMBEDDING_DIM
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
        "speakers_spoke": [],
        "speakers_mentioned": [],
        "entities": [],
        "keywords": [],
        "topic_label": "Test topic",
        "session_themes": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "corpus_derived_markers": corpus_derived_markers or [],
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
        "embed_text": "test embed_text",
        "full_text": full_text,
        "bm25_text": "test bm25_text",
        "embedding": embedding,
    }


def _create_table(db_path: Path, rows: list[dict]):
    db = lancedb.connect(str(db_path))
    table = db.create_table("chunks", schema=pyarrow_table_schema())
    if rows:
        table.add(rows)
    return table


def _direction_vector(seed: int) -> list[float]:
    """Build a normalized embedding pointing in a specific direction.
    Two chunks with the same seed have cosine similarity ~1.0; different
    seeds give similarity ~0.0.
    """
    vec = [0.0] * EMBEDDING_DIM
    vec[seed % EMBEDDING_DIM] = 1.0
    return vec


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "test.lancedb"


def test_recurrent_marker_applied_to_cross_session_neighbors(db_path: Path):
    """A chunk with K-nearest neighbors spanning 2+ sessions at high similarity
    receives the 'recurrent' marker."""
    # 3 sessions, 2 chunks each, all chunks share the same embedding direction.
    # Every chunk has 5 high-similarity neighbors across 2 different sessions.
    rows = []
    for sid in ("s1", "s2", "s3"):
        for i in range(2):
            rows.append(_make_chunk_row(
                chunk_id=f"{sid}:c{i}",
                session_id=sid,
                embedding=_direction_vector(0),  # all aligned
            ))
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    assert stats["scanned"] == 6
    # All chunks should be marked recurrent (each has >=2 cross-session high-sim neighbors).
    assert stats["recurrent"] == 6
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    for r in rows_after:
        assert "recurrent" in r["corpus_derived_markers"]


def test_unique_chunk_no_recurrent_marker(db_path: Path):
    """Chunks without high-similarity cross-session neighbors stay unmarked."""
    # Each chunk has a unique embedding direction; no neighbors above threshold.
    rows = [
        _make_chunk_row(
            chunk_id=f"s{i}:c0",
            session_id=f"s{i}",
            embedding=_direction_vector(i),
        )
        for i in range(3)
    ]
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    assert stats["scanned"] == 3
    assert stats["recurrent"] == 0
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    for r in rows_after:
        assert r["corpus_derived_markers"] == []


def test_lint_corpus_idempotent(db_path: Path):
    """Running lint_corpus twice produces the same markers (no duplication)."""
    rows = []
    for sid in ("s1", "s2", "s3"):
        rows.append(_make_chunk_row(
            chunk_id=f"{sid}:c0",
            session_id=sid,
            embedding=_direction_vector(0),
        ))
    _create_table(db_path, rows)
    stats1 = lint_corpus_chunks(db_path)
    stats2 = lint_corpus_chunks(db_path)
    assert stats1["recurrent"] == stats2["recurrent"]
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    for r in rows_after:
        # Marker should appear exactly once even after two passes.
        assert r["corpus_derived_markers"].count("recurrent") <= 1


def test_lint_corpus_writes_corpus_markers_computed_at(db_path: Path):
    """corpus_markers_computed_at is set to a non-null UTC timestamp on every row."""
    rows = [
        _make_chunk_row(chunk_id="s1:c0", session_id="s1"),
    ]
    _create_table(db_path, rows)
    lint_corpus_chunks(db_path)
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    assert rows_after[0]["corpus_markers_computed_at"] is not None


def test_lint_corpus_neighbors_in_same_session_dont_count(db_path: Path):
    """Three chunks in ONE session, all aligned. No cross-session neighbors,
    so no recurrent marker."""
    rows = [
        _make_chunk_row(
            chunk_id=f"s1:c{i}",
            session_id="s1",
            embedding=_direction_vector(0),
        )
        for i in range(3)
    ]
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    assert stats["recurrent"] == 0


def test_lint_corpus_below_threshold_neighbors_dont_count(db_path: Path):
    """Cross-session neighbors below similarity threshold don't trigger recurrent."""
    # Each chunk in a different direction -> low cross-similarity.
    rows = [
        _make_chunk_row(
            chunk_id=f"s{i}:c0",
            session_id=f"s{i}",
            embedding=_direction_vector(i),
        )
        for i in range(5)
    ]
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    assert stats["recurrent"] == 0


def test_recurrent_requires_neighbors_from_distinct_sessions(db_path: Path):
    """HIGH 2 regression: two highly-similar neighbors from a SINGLE other session
    must NOT mark the target as recurrent.

    cross_session_session_ids counts distinct sessions, not neighbor chunks.
    {s2} has len=1 which is below CROSS_SESSION_COUNT_MIN=2, so no recurrent mark.
    """
    rows = [
        # Target chunk in s1
        _make_chunk_row(
            chunk_id="s1:c0",
            session_id="s1",
            embedding=_direction_vector(0),
        ),
        # Two highly-similar neighbors in s2 (single other session)
        _make_chunk_row(
            chunk_id="s2:c0",
            session_id="s2",
            embedding=_direction_vector(0),
        ),
        _make_chunk_row(
            chunk_id="s2:c1",
            session_id="s2",
            embedding=_direction_vector(0),
        ),
    ]
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    # cross_session_session_ids = {"s2"} -> len=1 -> below CROSS_SESSION_COUNT_MIN=2
    assert stats["recurrent"] == 0, (
        "Two neighbors from ONE other session should not satisfy recurrent threshold"
    )


def test_lint_corpus_marker_update_non_destructive_on_failure(
    db_path: Path, monkeypatch
) -> None:
    """HIGH 1 regression: if the marker write fails, the row must be unchanged.

    Under the update()-based implementation, a failed update leaves the row
    intact (no delete has occurred). The lint function raises, which propagates
    out of the auto-trigger. Chunks are NOT destroyed.
    """
    import lancedb as _ldb
    from community_brain.cli import lint_corpus as _lint_mod

    rows = [
        _make_chunk_row(
            chunk_id="s1:c0",
            session_id="s1",
            embedding=_direction_vector(0),
            full_text="original content",
        ),
        _make_chunk_row(
            chunk_id="s2:c0",
            session_id="s2",
            embedding=_direction_vector(0),
        ),
    ]
    _create_table(db_path, rows)

    # Capture the real open_table so we can wrap it
    real_connect = _ldb.connect

    class _FaultyTable:
        """Proxy that raises on update() to simulate a write failure."""
        def __init__(self, real_table):
            self._real = real_table

        def __getattr__(self, name):
            return getattr(self._real, name)

        def update(self, *args, **kwargs):
            raise RuntimeError("simulated marker write failure")

    class _FaultyDB:
        def __init__(self, real_db):
            self._real = real_db

        def open_table(self, name):
            return _FaultyTable(self._real.open_table(name))

    original_connect = _ldb.connect

    def patched_connect(path, *args, **kwargs):
        return _FaultyDB(original_connect(path, *args, **kwargs))

    monkeypatch.setattr(_lint_mod, "lancedb", type("mod", (), {
        "connect": staticmethod(patched_connect),
    })())

    # lint_corpus raises because update() fails
    with pytest.raises(RuntimeError, match="simulated marker write failure"):
        _lint_mod.lint_corpus_chunks(db_path)

    # The row must still be present and its full_text must be unchanged
    db = _ldb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    assert len(rows_after) == 2, "Row count changed — data was destroyed"
    s1_row = next(r for r in rows_after if r["chunk_id"] == "s1:c0")
    assert s1_row["full_text"] == "original content", (
        "full_text was mutated — row was not left intact after update failure"
    )

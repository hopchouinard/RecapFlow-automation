"""Tests for the FTS index lifecycle (boot-time creation, post-ingest refresh)."""

from __future__ import annotations

import lancedb
import pyarrow as pa
import pytest

from community_brain.query.fts_lifecycle import (
    drop_full_text_index_if_present,
    ensure_fts_index,
    has_fts_index,
)


def _make_chunks_table(db_path):
    db = lancedb.connect(str(db_path))
    schema = pa.schema([
        ("chunk_id", pa.string()),
        ("full_text", pa.string()),
        ("embedding", pa.list_(pa.float32(), 4)),
    ])
    table = db.create_table("chunks", schema=schema)
    table.add([
        {"chunk_id": "a", "full_text": "hello world", "embedding": [1.0, 0, 0, 0]},
    ])
    return db, table


def test_has_fts_index_returns_false_when_absent(tmp_path):
    _db, table = _make_chunks_table(tmp_path)
    assert has_fts_index(table, "full_text") is False


def test_ensure_fts_index_creates_when_absent(tmp_path):
    _db, table = _make_chunks_table(tmp_path)
    assert has_fts_index(table, "full_text") is False
    ensure_fts_index(table, "full_text")
    assert has_fts_index(table, "full_text") is True


def test_ensure_fts_index_is_idempotent(tmp_path):
    _db, table = _make_chunks_table(tmp_path)
    ensure_fts_index(table, "full_text")
    # Calling again must not raise nor duplicate work
    ensure_fts_index(table, "full_text")
    assert has_fts_index(table, "full_text") is True


def test_ensure_fts_index_logs_creation_time(tmp_path, caplog):
    import logging
    _db, table = _make_chunks_table(tmp_path)
    with caplog.at_level(logging.INFO):
        ensure_fts_index(table, "full_text")
    assert any(
        "FTS index" in rec.message and "full_text" in rec.message
        for rec in caplog.records
    )


from community_brain.query.fts_lifecycle import optimize_fts_index


def test_optimize_fts_index_makes_new_rows_searchable(tmp_path):
    """End-to-end: add a row after the FTS index is built, call optimize,
    and verify the new row is visible to FTS query.

    Under LanceDB 0.30.x the auto-update path means new rows are searchable
    BEFORE optimize_fts_index runs; this test verifies the production hook
    does not undo that (it must remain a clean no-op)."""
    _db, table = _make_chunks_table(tmp_path)
    ensure_fts_index(table, "full_text")

    # Add a row that contains a unique token absent from the original data
    table.add([
        {"chunk_id": "b", "full_text": "supercalifragilistic Adam", "embedding": [0, 1.0, 0, 0]},
    ])
    optimize_fts_index(table, "full_text")

    # FTS query for the new token must surface chunk_id 'b'
    results = table.search("supercalifragilistic", query_type="fts").limit(5).to_list()
    ids = [r["chunk_id"] for r in results]
    assert "b" in ids, f"expected 'b' to be searchable after optimize; got {ids}"


def test_optimize_fts_index_does_not_raise_on_repeated_calls(tmp_path):
    _db, table = _make_chunks_table(tmp_path)
    ensure_fts_index(table, "full_text")
    optimize_fts_index(table, "full_text")
    optimize_fts_index(table, "full_text")  # second call must not raise
    optimize_fts_index(table, "full_text")  # third call must not raise


def test_optimize_fts_index_does_not_log_warning_after_t8_wireup(tmp_path, caplog):
    """The T7 stub logged a WARNING saying it was unwired. After T8 the
    auto-update no-op path is in place; calling optimize_fts_index should
    NOT log at WARNING or higher under happy-path conditions.

    Adapted from the plan's failure-tolerance test: under the no-op path
    there's no underlying lancedb call to monkeypatch, so we instead assert
    the function is silent (no warnings) on the happy path. T11/T12's wiring
    tasks ensure the no-op is harmless when called from real code paths."""
    import logging
    _db, table = _make_chunks_table(tmp_path)
    ensure_fts_index(table, "full_text")
    with caplog.at_level(logging.WARNING):
        optimize_fts_index(table, "full_text")
    # No WARNING-level records from the optimize call (debug logs are fine)
    warnings_or_higher = [r for r in caplog.records if r.levelno >= logging.WARNING]
    assert warnings_or_higher == [], (
        f"optimize_fts_index logged at WARNING+ unexpectedly: {warnings_or_higher}"
    )


# --- T18: bm25_text default + legacy cleanup ---


def _make_bm25_table(db_path):
    """Minimal table with a bm25_text column for T18 tests."""
    db = lancedb.connect(str(db_path))
    schema = pa.schema([
        ("chunk_id", pa.string()),
        ("bm25_text", pa.string()),
        ("full_text", pa.string()),
        ("embedding", pa.list_(pa.float32(), 4)),
    ])
    table = db.create_table("chunks", schema=schema)
    table.add([
        {
            "chunk_id": "a",
            "bm25_text": "hello world coaching call",
            "full_text": "hello world",
            "embedding": [1.0, 0, 0, 0],
        },
    ])
    return db, table


def test_ensure_fts_index_default_column_is_bm25_text(tmp_path):
    """Default column for ensure_fts_index is bm25_text (v3 migration)."""
    _db, table = _make_bm25_table(tmp_path)
    assert has_fts_index(table, "bm25_text") is False
    ensure_fts_index(table)  # default column = bm25_text
    assert has_fts_index(table, "bm25_text") is True


def test_ensure_fts_index_default_does_not_create_full_text_index(tmp_path):
    """When called with no column arg, ensure_fts_index should NOT create a
    full_text FTS index — it targets bm25_text only."""
    _db, table = _make_bm25_table(tmp_path)
    ensure_fts_index(table)  # default = bm25_text
    # full_text index should remain absent
    assert has_fts_index(table, "full_text") is False


def test_drop_full_text_index_if_present_no_op_when_absent(tmp_path):
    """When no full_text FTS index exists, drop helper returns False without raising."""
    _db, table = _make_bm25_table(tmp_path)
    result = drop_full_text_index_if_present(table)
    # Either False (no index found / API unavailable) or True (attempted drop).
    # The key guarantee is: no exception raised.
    assert result is False


def test_drop_full_text_index_if_present_returns_false_on_fresh_table(tmp_path):
    """On a table that has never had a full_text FTS index, the helper is a no-op."""
    _db, table = _make_bm25_table(tmp_path)
    # Build bm25_text index — simulates the v3 state after migration.
    ensure_fts_index(table, "bm25_text")
    result = drop_full_text_index_if_present(table)
    assert result is False
    # bm25_text index is still present after the drop attempt
    assert has_fts_index(table, "bm25_text") is True

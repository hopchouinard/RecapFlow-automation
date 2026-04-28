"""Tests for the FTS index lifecycle (boot-time creation, post-ingest refresh)."""

from __future__ import annotations

import lancedb
import pyarrow as pa
import pytest

from community_brain.query.fts_lifecycle import (
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

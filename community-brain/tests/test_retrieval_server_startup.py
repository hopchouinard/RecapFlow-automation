"""Tests for the retrieval server startup lifecycle (FTS index ensure-on-boot)."""

from __future__ import annotations

import lancedb
import pytest
from fastapi.testclient import TestClient

from community_brain.ingestion.schema import pyarrow_table_schema


@pytest.fixture
def populated_db(tmp_path, monkeypatch):
    db_path = tmp_path / "lancedb"
    db = lancedb.connect(str(db_path))
    schema = pyarrow_table_schema()
    db.create_table("chunks", schema=schema)
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    return db_path


def test_startup_ensures_fts_index_on_chunks_full_text(populated_db):
    """When the server boots and the chunks table exists without an FTS
    index, the lifespan startup hook must build it."""
    from community_brain.query import retrieval_server
    from community_brain.query.fts_lifecycle import has_fts_index

    db = lancedb.connect(str(populated_db))
    table = db.open_table("chunks")
    assert has_fts_index(table, "full_text") is False, "precondition: no FTS index yet"

    with TestClient(retrieval_server.app) as _client:
        # TestClient context triggers lifespan startup
        pass

    table = db.open_table("chunks")
    assert has_fts_index(table, "full_text") is True


def test_startup_no_chunks_table_does_not_raise(tmp_path, monkeypatch):
    """Fresh deployment: no chunks table yet. Startup must not crash —
    /ingest will create the table later."""
    monkeypatch.setenv("LANCEDB_PATH", str(tmp_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    from community_brain.query import retrieval_server

    with TestClient(retrieval_server.app) as client:
        resp = client.get("/health")
        assert resp.status_code == 200

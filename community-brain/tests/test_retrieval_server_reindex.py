"""Tests for POST /reindex (v1 minimal: dry-run matching only, mutations deferred)."""

from __future__ import annotations

from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod


def test_post_reindex_dry_run_returns_matching_chunk_ids(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._reindex_select_chunk_ids",
        return_value=["2024-01-01:transcript:001", "2024-01-01:transcript:002"],
    ):
        resp = client.post(
            "/reindex",
            json={
                "filter": {"extraction_prompt_version": "chunk-extraction-v1"},
                "operation": "re-extract",
                "dry_run": True,
            },
        )

    assert resp.status_code == 200
    data = resp.json()
    assert data["matched_chunk_ids"] == [
        "2024-01-01:transcript:001",
        "2024-01-01:transcript:002",
    ]
    assert data["dry_run"] is True
    assert data["operation"] == "re-extract"


def test_post_reindex_unsupported_operation_returns_400(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    resp = client.post(
        "/reindex",
        json={
            "filter": {},
            "operation": "something-else",
            "dry_run": True,
        },
    )
    assert resp.status_code == 400
    detail = resp.json().get("detail", "")
    assert "something-else" in detail or "operation" in detail.lower()


def test_post_reindex_non_dry_run_returns_v1_deferral_note(monkeypatch) -> None:
    """V1 doesn't perform mutations; non-dry-run returns a note pointing at /ingest."""
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._reindex_select_chunk_ids",
        return_value=["x:transcript:001"],
    ):
        resp = client.post(
            "/reindex",
            json={
                "filter": {"extraction_prompt_version": "v1"},
                "operation": "re-extract",
                "dry_run": False,
            },
        )

    assert resp.status_code == 200
    data = resp.json()
    assert data["dry_run"] is False
    assert data["matched_chunk_ids"] == ["x:transcript:001"]
    # The note should point operators at the v1 recovery path
    assert "force_reextract" in data["note"]


def test_post_reindex_accepts_all_three_supported_operations(monkeypatch) -> None:
    """re-extract, re-embed, and delete are all accepted (even if not yet implemented)."""
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    for op in ["re-extract", "re-embed", "delete"]:
        with patch(
            "community_brain.query.retrieval_server._reindex_select_chunk_ids",
            return_value=[],
        ):
            resp = client.post(
                "/reindex",
                json={"filter": {}, "operation": op, "dry_run": True},
            )
        assert resp.status_code == 200, f"failed for operation={op}"
        assert resp.json()["operation"] == op


def test_post_reindex_empty_match_returns_empty_list(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._reindex_select_chunk_ids",
        return_value=[],
    ):
        resp = client.post(
            "/reindex",
            json={
                "filter": {"extraction_prompt_version": "nonexistent"},
                "operation": "re-extract",
                "dry_run": True,
            },
        )

    assert resp.status_code == 200
    assert resp.json()["matched_chunk_ids"] == []

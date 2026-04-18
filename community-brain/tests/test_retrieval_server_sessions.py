"""Tests for GET /sessions and /sessions/{id} endpoints."""

from __future__ import annotations

from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod


def _fake_rows() -> list[dict]:
    return [
        {
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "Agent frameworks",
            "content_type": "prepared_transcript",
            "has_unresolved_question": False,
            "session_themes": ["agent frameworks", "production"],
        },
        {
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "Agent frameworks",
            "content_type": "community_post",
            "has_unresolved_question": True,
            "session_themes": ["agent frameworks", "production"],
        },
        {
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "Agent frameworks",
            "content_type": "extracted_signal",
            "has_unresolved_question": False,
            "session_themes": ["agent frameworks", "production"],
        },
        {
            "session_id": "2026-04-01",
            "session_date": "2026-04-01",
            "session_title": "Embeddings",
            "content_type": "prepared_transcript",
            "has_unresolved_question": False,
            "session_themes": ["embedding tradeoffs"],
        },
    ]


def test_get_sessions_returns_aggregated_sessions(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._load_all_session_rows",
        return_value=_fake_rows(),
    ):
        resp = client.get("/sessions")

    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 2
    session_ids = [s["session_id"] for s in data["sessions"]]
    assert "2026-03-10" in session_ids
    assert "2026-04-01" in session_ids


def test_get_sessions_aggregates_chunk_counts_by_type(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._load_all_session_rows",
        return_value=_fake_rows(),
    ):
        resp = client.get("/sessions")

    data = resp.json()
    s_march = next(s for s in data["sessions"] if s["session_id"] == "2026-03-10")
    assert s_march["chunk_counts"]["prepared_transcript"] == 1
    assert s_march["chunk_counts"]["community_post"] == 1
    assert s_march["chunk_counts"]["extracted_signal"] == 1
    assert s_march["unresolved_question_count"] == 1
    assert "agent frameworks" in s_march["session_themes"]


def test_get_sessions_sorted_newest_first(monkeypatch) -> None:
    """Default sort: most recent session first."""
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._load_all_session_rows",
        return_value=_fake_rows(),
    ):
        resp = client.get("/sessions")

    data = resp.json()
    assert data["sessions"][0]["session_id"] == "2026-04-01"
    assert data["sessions"][1]["session_id"] == "2026-03-10"


def test_get_sessions_empty_corpus(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._load_all_session_rows",
        return_value=[],
    ):
        resp = client.get("/sessions")

    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 0
    assert data["sessions"] == []


def test_get_sessions_detail(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._load_all_session_rows",
        return_value=_fake_rows(),
    ):
        resp = client.get("/sessions/2026-03-10")

    assert resp.status_code == 200
    data = resp.json()
    assert data["session_id"] == "2026-03-10"
    assert data["chunk_counts"]["prepared_transcript"] == 1
    assert data["unresolved_question_count"] == 1


def test_get_sessions_detail_not_found(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._load_all_session_rows",
        return_value=_fake_rows(),
    ):
        resp = client.get("/sessions/1999-01-01")

    assert resp.status_code == 404

"""Tests for the extended POST /query endpoint with structured response."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod


def _fake_search_results() -> list[dict]:
    """Shape matching what search_chunks returns from LanceDB."""
    return [
        {
            "chunk_id": "2026-03-10:transcript:001",
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "t",
            "content_type": "prepared_transcript",
            "source_file": "x.md",
            "full_text": "ground truth text",
            "embed_text": "topic: x",
            "topic_label": "x",
            "speakers_spoke": ["Alex Rojas"],
            "speakers_mentioned": ["Alex Rojas"],
            "entities": ["LangGraph"],
            "keywords": ["agents"],
            "session_themes": ["agent frameworks"],
            "speech_acts": ["comparison"],
            "stance": "positive",
            "certainty": "asserted",
            "chunk_local_markers": ["emphasized"],
            "corpus_derived_markers": [],
            "corpus_markers_computed_at": None,
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": True,
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            "chunk_index": 1,
            "total_chunks_in_source": 2,
            "schema_version": "1.0",
            "extraction_model": "m",
            "extraction_prompt_version": "chunk-extraction-v1",
            "extraction_status": "success",
            "extraction_error": None,
            "extracted_at": "2026-03-10T14:22:11+00:00",
            "_distance": 0.12,
        }
    ]


def test_post_query_returns_structured_shape(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.query_local.search_chunks",
        return_value=_fake_search_results(),
    ):
        resp = client.post("/query", json={"question": "what about agents?", "top_k": 5})

    assert resp.status_code == 200
    data = resp.json()
    assert "chunks" in data
    assert len(data["chunks"]) == 1
    chunk = data["chunks"][0]
    assert "ground_truth" in chunk
    assert "derived_metadata" in chunk
    assert "provenance" in chunk
    assert chunk["ground_truth"]["chunk_id"] == "2026-03-10:transcript:001"
    assert chunk["ground_truth"]["full_text"] == "ground truth text"
    assert chunk["derived_metadata"]["stance"] == "positive"
    assert chunk["derived_metadata"]["entities"] == ["LangGraph"]
    assert chunk["provenance"]["extraction_prompt_version"] == "chunk-extraction-v1"
    assert chunk["provenance"]["schema_version"] == "1.0"
    assert "similarity" in chunk


def test_post_query_passes_filters_to_search(monkeypatch) -> None:
    """Filter values from the HTTP body reach search_chunks correctly."""
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    captured: dict = {}

    def _spy(question, db_path, top_k, filters, ollama_base_url):
        captured["filters"] = filters
        captured["question"] = question
        captured["top_k"] = top_k
        return _fake_search_results()

    with patch(
        "community_brain.query.query_local.search_chunks",
        side_effect=_spy,
    ):
        resp = client.post(
            "/query",
            json={
                "question": "x",
                "top_k": 3,
                "filters": {
                    "entities": ["LangGraph"],
                    "entities_match": "any",
                    "require_chunk_markers": ["emphasized"],
                    "has_insight": True,
                },
            },
        )

    assert resp.status_code == 200
    assert captured["question"] == "x"
    assert captured["top_k"] == 3
    assert captured["filters"]["entities"] == ["LangGraph"]
    assert captured["filters"]["entities_match"] == "any"
    assert captured["filters"]["require_chunk_markers"] == ["emphasized"]
    assert captured["filters"]["has_insight"] is True


def test_post_query_default_filters_match_spec(monkeypatch) -> None:
    """Omitted filters default to None / 'any' per spec."""
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    captured: dict = {}

    def _spy(question, db_path, top_k, filters, ollama_base_url):
        captured["filters"] = filters
        return []

    with patch(
        "community_brain.query.query_local.search_chunks",
        side_effect=_spy,
    ):
        resp = client.post("/query", json={"question": "x"})

    assert resp.status_code == 200
    f = captured["filters"]
    assert f["entities_match"] == "any"
    assert f["speakers_spoke_match"] == "any"
    assert f["entities"] is None
    assert f["has_question"] is None


def test_post_query_filters_applied_echoed_in_response(monkeypatch) -> None:
    """The response's filters_applied echoes what was sent."""
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.query_local.search_chunks",
        return_value=_fake_search_results(),
    ):
        resp = client.post(
            "/query",
            json={
                "question": "x",
                "filters": {"entities": ["LangGraph"], "has_insight": True},
            },
        )

    assert resp.status_code == 200
    data = resp.json()
    applied = data["filters_applied"]
    assert applied["entities"] == ["LangGraph"]
    assert applied["has_insight"] is True


def test_post_query_total_matched_reflects_returned_chunks(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.query_local.search_chunks",
        return_value=_fake_search_results(),
    ):
        resp = client.post("/query", json={"question": "x"})

    assert resp.status_code == 200
    data = resp.json()
    assert data["total_matched"] == 1
    assert data["query"] == "x"


def test_post_query_returns_empty_on_fresh_deployment(tmp_path: Path, monkeypatch) -> None:
    """Fresh deployment with no ingested sessions should return empty chunks, not 500."""
    monkeypatch.setenv("LANCEDB_PATH", str(tmp_path / "empty-lancedb"))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    client = TestClient(server_mod.app)

    def _fake_embed(model, input):
        return {"embeddings": [[0.0] * 768 for _ in input]}

    with patch("community_brain.query.query_local.ollama.embed", side_effect=_fake_embed):
        resp = client.post("/query", json={"question": "x"})

    assert resp.status_code == 200
    data = resp.json()
    assert data["total_matched"] == 0
    assert data["chunks"] == []


def test_post_query_rejects_unknown_response_shape(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    resp = client.post("/query", json={"question": "x", "response_shape": "flat"})
    assert resp.status_code == 422

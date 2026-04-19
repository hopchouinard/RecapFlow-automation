"""End-to-end smoke test: ingest fixtures, then query them via the API.

Runs in-process using TestClient + a real LanceDB temp directory. LLM calls
are mocked (Stage B themes + Stage C extraction). Embeddings are fake 768-dim
vectors. This is the closest approximation to production behavior without
actually starting Docker or calling Ollama/OpenRouter.

Verifies:
  - POST /ingest writes chunks to LanceDB with the v1.0 schema
  - POST /query returns those chunks via vector search
  - GET /sessions reflects the ingested session
  - The three endpoints compose correctly end-to-end
"""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod

FIXTURES = Path(__file__).parent / "fixtures"


def _fake_extract_response(model, prompt):
    """Route Stage B vs Stage C by prompt content."""
    if "SESSION_INPUT:" in prompt:
        return json.dumps({"themes": ["agent frameworks", "embeddings"]})
    return json.dumps({
        "entities": ["LangGraph"],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": ["comparison"],
        "stance": "positive",
        "certainty": "asserted",
        "chunk_local_markers": ["emphasized"],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
    })


def _mock_embed(model, input):
    """Fake embeddings — same vector per input so query cosine-similarity works."""
    return {"embeddings": [[0.1] * 768 for _ in input]}


def _seed_config(tmp_path: Path) -> Path:
    """Write minimum valid configs for the pipeline to run."""
    cfg = tmp_path / "config"
    cfg.mkdir()
    (cfg / "chunking.yaml").write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )
    (cfg / "extraction-config.yaml").write_text(
        """
session_themes:
  prompt_file: session-themes-v1.md
  model: test-model
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: test-model
        """,
        encoding="utf-8",
    )
    (cfg / "speaker-aliases.yaml").write_text(
        'version: "x"\naliases: {}\npending: []\n', encoding="utf-8"
    )
    (cfg / "entity-registry.yaml").write_text(
        (
            'version: "x"\n'
            'entities:\n'
            '  LangGraph:\n'
            '    type: framework\n'
            '    aliases: [langgraph]\n'
            'pending: []\n'
        ),
        encoding="utf-8",
    )
    prompts = cfg / "extraction-prompts"
    prompts.mkdir()
    (prompts / "session-themes-v1.md").write_text("p", encoding="utf-8")
    (prompts / "chunk-extraction-v1.md").write_text("p", encoding="utf-8")
    return cfg


def test_end_to_end_ingest_then_query(tmp_path: Path, monkeypatch) -> None:
    """Full round-trip: ingest fixtures, then query them and validate shape."""
    cfg_dir = _seed_config(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    # Do NOT set COMMUNITY_BRAIN_ARTIFACT_ROOT for this test; artifacts live in
    # tests/fixtures/ which is outside any constrained root.
    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

    client = TestClient(server_mod.app)

    ingest_body = {
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "Agent frameworks comparison",
        "artifact_paths": {
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            "extracted_signal": str(FIXTURES / "extracted-signal-sample.md"),
            "community_post": str(FIXTURES / "community-post-sample.md"),
        },
        "force_reextract": False,
    }

    with patch(
        "community_brain.ingestion.embedding.ollama.embed", side_effect=_mock_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_fake_extract_response,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_fake_extract_response,
    ):
        ingest_resp = client.post("/ingest", json=ingest_body)

    assert ingest_resp.status_code == 200, ingest_resp.text
    ingest_data = ingest_resp.json()
    assert ingest_data["chunks_written"] >= 7
    assert ingest_data["schema_version"] == "1.0"
    assert ingest_data["chunks_failed"] == 0

    # Query with a mocked query-side embedding (same vector so cosine returns matches)
    with patch(
        "community_brain.query.query_local.ollama.embed",
        return_value={"embeddings": [[0.1] * 768]},
    ):
        query_resp = client.post("/query", json={"question": "agent frameworks", "top_k": 5})

    assert query_resp.status_code == 200
    query_data = query_resp.json()
    assert query_data["total_matched"] > 0
    chunk = query_data["chunks"][0]
    assert "ground_truth" in chunk
    assert "derived_metadata" in chunk
    assert "provenance" in chunk
    assert chunk["provenance"]["schema_version"] == "1.0"
    assert chunk["derived_metadata"]["entities"] == ["LangGraph"]
    # session_themes from Stage B should be denormalized onto this chunk
    assert chunk["derived_metadata"]["session_themes"] == ["agent frameworks", "embeddings"]


def test_end_to_end_sessions_endpoint_after_ingest(tmp_path: Path, monkeypatch) -> None:
    """After ingesting, /sessions reflects the session with chunk counts."""
    cfg_dir = _seed_config(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

    client = TestClient(server_mod.app)

    body = {
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "t",
        "artifact_paths": {
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        "force_reextract": False,
    }

    with patch(
        "community_brain.ingestion.embedding.ollama.embed", side_effect=_mock_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_fake_extract_response,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_fake_extract_response,
    ):
        client.post("/ingest", json=body)

    # /sessions should now list one session
    resp = client.get("/sessions")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 1
    session = data["sessions"][0]
    assert session["session_id"] == "2026-03-10"
    assert session["chunk_counts"]["prepared_transcript"] >= 1

    # /sessions/{id} detail
    detail = client.get("/sessions/2026-03-10")
    assert detail.status_code == 200
    assert detail.json()["session_id"] == "2026-03-10"


def test_end_to_end_reindex_dry_run_reflects_ingested_corpus(
    tmp_path: Path, monkeypatch
) -> None:
    """/reindex dry-run should see the chunks written by /ingest."""
    cfg_dir = _seed_config(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

    client = TestClient(server_mod.app)

    body = {
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "t",
        "artifact_paths": {
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        "force_reextract": False,
    }

    with patch(
        "community_brain.ingestion.embedding.ollama.embed", side_effect=_mock_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_fake_extract_response,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_fake_extract_response,
    ):
        client.post("/ingest", json=body)

    # Reindex dry-run should match the chunks we just wrote
    resp = client.post(
        "/reindex",
        json={
            "filter": {"extraction_prompt_version": "chunk-extraction-v1"},
            "operation": "re-extract",
            "dry_run": True,
        },
    )
    assert resp.status_code == 200
    assert len(resp.json()["matched_chunk_ids"]) > 0


def test_end_to_end_idempotent_ingest(tmp_path: Path, monkeypatch) -> None:
    """Re-POSTing /ingest with same session under same version is a no-op."""
    cfg_dir = _seed_config(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

    client = TestClient(server_mod.app)

    body = {
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "t",
        "artifact_paths": {
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        "force_reextract": False,
    }

    with patch(
        "community_brain.ingestion.embedding.ollama.embed", side_effect=_mock_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_fake_extract_response,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_fake_extract_response,
    ):
        first = client.post("/ingest", json=body)
        second = client.post("/ingest", json=body)

    assert first.status_code == 200
    assert second.status_code == 200
    first_data = first.json()
    second_data = second.json()
    assert first_data["chunks_written"] > 0
    # Second call: everything is skipped (idempotent)
    assert second_data["chunks_written"] == 0
    assert second_data["chunks_skipped_idempotent"] == first_data["chunks_written"]

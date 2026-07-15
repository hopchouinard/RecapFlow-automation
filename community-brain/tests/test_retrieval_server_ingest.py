"""Tests for POST /ingest endpoint."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.ingestion.schema import SCHEMA_VERSION
from community_brain.query import retrieval_server as server_mod

FIXTURES = Path(__file__).parent / "fixtures"


def _fake_extract_response(model, prompt, **_kwargs):
    if "SESSION_INPUT:" in prompt:
        return json.dumps({"themes": ["agent frameworks"]})
    return json.dumps({
        "topic_label": "Test topic",
        "entities": [],
        "speakers_mentioned": [],
        "keywords": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
    })


def _mock_ollama_embed(model, input):
    return {"embeddings": [[0.0] * 768 for _ in input]}


def _write_configs(tmp_path: Path) -> Path:
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
  prompt_file: chunk-extraction-v2.md
  model: test-model
        """,
        encoding="utf-8",
    )
    (cfg / "speaker-aliases.yaml").write_text(
        'version: "x"\naliases: {}\npending: []\n', encoding="utf-8"
    )
    (cfg / "entity-registry.yaml").write_text(
        'version: "x"\nentities: {}\npending: []\n', encoding="utf-8"
    )
    prompts = cfg / "extraction-prompts"
    prompts.mkdir()
    (prompts / "session-themes-v1.md").write_text("p", encoding="utf-8")
    (prompts / "chunk-extraction-v2.md").write_text("p", encoding="utf-8")
    return cfg


def test_post_ingest_success(tmp_path: Path, monkeypatch) -> None:
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"

    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.delenv("OLLAMA_BASE_URL", raising=False)

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
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=_mock_ollama_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_fake_extract_response,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_fake_extract_response,
    ):
        resp = client.post("/ingest", json=body)

    assert resp.status_code == 200
    data = resp.json()
    assert data["session_id"] == "2026-03-10"
    assert data["chunks_written"] > 0
    assert data["schema_version"] == SCHEMA_VERSION
    assert data["extraction_prompt_version"] == "chunk-extraction-v2"


def test_post_ingest_empty_artifact_paths_returns_400(tmp_path: Path, monkeypatch) -> None:
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    client = TestClient(server_mod.app)
    resp = client.post(
        "/ingest",
        json={
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "t",
            "artifact_paths": {},
            "force_reextract": False,
        },
    )
    # Endpoint-level check raises 400; Pydantic validator only rejects unknown
    # keys (422), not empty dicts. The explicit `if not req.artifact_paths`
    # guard in the handler returns 400 for empty.
    assert resp.status_code == 400


def test_post_ingest_invalid_session_id_returns_400(tmp_path: Path, monkeypatch) -> None:
    """SQL-injection attempt in session_id must be rejected with 400."""
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    client = TestClient(server_mod.app)
    resp = client.post(
        "/ingest",
        json={
            "session_id": "x' OR '1'='1",
            "session_date": "2026-03-10",
            "session_title": "t",
            "artifact_paths": {
                "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            },
            "force_reextract": False,
        },
    )
    assert resp.status_code == 400
    assert "session_id" in resp.json().get("detail", "").lower()


def test_post_ingest_requires_api_key_when_configured(tmp_path: Path, monkeypatch) -> None:
    """When RETRIEVAL_API_KEY is set, requests without matching header are rejected."""
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.setenv("RETRIEVAL_API_KEY", "secret-key-for-this-test")

    # Force the module to re-read the env var by reloading it.
    # Without this, the module-level RETRIEVAL_API_KEY variable cached at import time.
    import importlib
    import community_brain.query.retrieval_server as rs
    importlib.reload(rs)

    client = TestClient(rs.app)
    resp = client.post(
        "/ingest",
        json={
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "t",
            "artifact_paths": {"prepared_transcript": "x.md"},
            "force_reextract": False,
        },
    )
    assert resp.status_code == 403


def test_post_ingest_response_shape_contains_expected_fields(tmp_path: Path, monkeypatch) -> None:
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.delenv("OLLAMA_BASE_URL", raising=False)

    client = TestClient(server_mod.app)

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=_mock_ollama_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_fake_extract_response,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_fake_extract_response,
    ):
        resp = client.post(
            "/ingest",
            json={
                "session_id": "2026-03-10",
                "session_date": "2026-03-10",
                "session_title": "t",
                "artifact_paths": {
                    "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
                },
                "force_reextract": False,
            },
        )

    assert resp.status_code == 200
    data = resp.json()
    for field in [
        "session_id", "chunks_written", "chunks_by_type",
        "chunks_skipped_idempotent", "chunks_failed",
        "extraction_model", "extraction_prompt_version", "schema_version",
        "warnings", "unknown_entities_flagged", "unknown_speakers_flagged",
    ]:
        assert field in data, f"missing field {field} in response"


def test_post_ingest_unknown_artifact_key_returns_422(tmp_path: Path, monkeypatch) -> None:
    """Unknown artifact_paths keys must be rejected with 422 (Pydantic validation)."""
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    client = TestClient(server_mod.app)
    resp = client.post(
        "/ingest",
        json={
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "t",
            "artifact_paths": {"weird_key": "/tmp/x.md"},
            "force_reextract": False,
        },
    )
    assert resp.status_code == 422
    body = str(resp.json()).lower()
    assert "weird_key" in body or "unknown" in body


def test_post_ingest_commit_error_returns_structured_detail(tmp_path: Path, monkeypatch) -> None:
    """On CommitError, response body should contain structured recovery info."""
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    client = TestClient(server_mod.app)

    from community_brain.ingestion.pipeline import CommitError

    def _raise_commit_error(*a, **kw):
        raise CommitError("simulated torn state")

    with patch(
        "community_brain.query.retrieval_server.ingest_session",
        side_effect=_raise_commit_error,
    ):
        resp = client.post(
            "/ingest",
            json={
                "session_id": "2026-03-10",
                "session_date": "2026-03-10",
                "session_title": "t",
                "artifact_paths": {
                    "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
                },
                "force_reextract": False,
            },
        )

    assert resp.status_code == 500
    detail = resp.json()["detail"]
    assert isinstance(detail, dict)
    assert detail["error"] == "commit_torn_state"
    assert "force_reextract" in detail["recovery"]
    assert "2026-03-10" in detail["recovery"]


def test_empty_retrieval_api_key_env_disables_auth(tmp_path: Path, monkeypatch) -> None:
    """Blank RETRIEVAL_API_KEY (e.g. from `:-` shell default) must not block requests."""
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.setenv("RETRIEVAL_API_KEY", "")  # empty string, not unset

    client = TestClient(server_mod.app)

    # Just hitting /health is enough — if auth is wrongly enabled, it'd 403
    resp = client.get("/health")
    assert resp.status_code == 200

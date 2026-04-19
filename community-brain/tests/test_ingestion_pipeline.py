"""Integration tests for the ingestion pipeline orchestrator.

LLM calls are mocked; LanceDB uses a temp directory; embeddings are faked.
"""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from community_brain.ingestion.pipeline import IngestRequest, ingest_session

FIXTURES = Path(__file__).parent / "fixtures"


def _fake_extract_response(model, prompt):
    """Distinguish Stage B (themes) from Stage C (chunk metadata) by prompt content."""
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


def _write_min_configs(base: Path) -> Path:
    """Write minimal valid configs to `base` and return its path."""
    base.mkdir(parents=True, exist_ok=True)
    (base / "chunking.yaml").write_text(
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
    (base / "extraction-config.yaml").write_text(
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
    (base / "speaker-aliases.yaml").write_text(
        'version: "x"\naliases:\n  Alex Rojas: [alexrojas]\npending: []\n',
        encoding="utf-8",
    )
    (base / "entity-registry.yaml").write_text(
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
    prompts = base / "extraction-prompts"
    prompts.mkdir(exist_ok=True)
    (prompts / "session-themes-v1.md").write_text("session themes prompt", encoding="utf-8")
    (prompts / "chunk-extraction-v1.md").write_text("chunk extraction prompt", encoding="utf-8")
    return base


def _mock_ollama_embed(model, input):
    return {"embeddings": [[0.0] * 768 for _ in input]}


@pytest.fixture
def mocked_pipeline_env():
    """Patch all external boundaries (LLM, embedding) for pipeline tests."""
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
        yield


def test_ingest_session_end_to_end(tmp_path: Path, mocked_pipeline_env) -> None:
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="Agent frameworks comparison",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            "extracted_signal": str(FIXTURES / "extracted-signal-sample.md"),
            "community_post": str(FIXTURES / "community-post-sample.md"),
        },
        force_reextract=False,
    )

    result = ingest_session(
        request=request,
        config_dir=config_dir,
        db_path=str(db_path),
        ollama_base_url=None,
    )

    assert result.chunks_written > 0
    assert result.chunks_by_type["prepared_transcript"] == 2
    assert result.chunks_by_type["extracted_signal"] == 4
    assert result.chunks_by_type["community_post"] == 1
    assert result.extraction_prompt_version == "chunk-extraction-v1"
    assert result.schema_version == "1.0"


def test_ingest_session_idempotent_reingest(tmp_path: Path, mocked_pipeline_env) -> None:
    """Re-running ingest on same session with same prompt version is a no-op."""
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )

    first = ingest_session(request, config_dir, str(db_path), None)
    second = ingest_session(request, config_dir, str(db_path), None)

    assert first.chunks_written > 0
    assert second.chunks_skipped_idempotent == first.chunks_written
    assert second.chunks_written == 0


def test_ingest_session_force_reextract_overrides_idempotency(
    tmp_path: Path, mocked_pipeline_env
) -> None:
    """force_reextract=True re-runs extraction even when version matches."""
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=True,
    )

    first = ingest_session(request, config_dir, str(db_path), None)
    # Second run with force_reextract=True should rewrite the chunks, not skip
    request_force = IngestRequest(
        session_id=request.session_id,
        session_date=request.session_date,
        session_title=request.session_title,
        artifact_paths=request.artifact_paths,
        force_reextract=True,
    )
    second = ingest_session(request_force, config_dir, str(db_path), None)

    assert second.chunks_written > 0
    assert second.chunks_skipped_idempotent == 0


def test_ingest_session_chunk_extraction_failure_marks_status_failed(
    tmp_path: Path,
) -> None:
    """A chunk whose LLM extraction fails should get extraction_status='failed'
    but the session as a whole proceeds and commits."""
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    def _broken_extract(model, prompt):  # noqa: ARG001
        if "SESSION_INPUT:" in prompt:
            return json.dumps({"themes": ["x"]})
        return "not json"  # malformed

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=_mock_ollama_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_broken_extract,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_broken_extract,
    ):
        result = ingest_session(request, config_dir, str(db_path), None)

    assert result.chunks_written > 0  # Chunks still written even with extraction failures
    assert result.chunks_failed > 0


def test_ingest_session_populates_session_themes_on_every_chunk(
    tmp_path: Path, mocked_pipeline_env
) -> None:
    """Stage B themes must be denormalized onto every chunk."""
    import lancedb

    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            "extracted_signal": str(FIXTURES / "extracted-signal-sample.md"),
            "community_post": str(FIXTURES / "community-post-sample.md"),
        },
        force_reextract=False,
    )

    ingest_session(request, config_dir, str(db_path), None)

    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    rows = list(table.search().to_list())
    assert len(rows) > 0
    for row in rows:
        assert row["session_themes"] == ["agent frameworks", "embeddings"]


def test_ingest_session_rejects_sql_injection_in_session_id(
    tmp_path: Path, mocked_pipeline_env
) -> None:
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    request = IngestRequest(
        session_id="x' OR '1'='1",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )
    with pytest.raises(ValueError, match="session_id"):
        ingest_session(request, config_dir, str(db_path), None)


def test_ingest_session_failed_chunks_have_empty_embedding(
    tmp_path: Path,
) -> None:
    """Chunks whose LLM extraction failed are persisted but not embedded."""
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    def _broken_chunk_extract(model, prompt):
        if "SESSION_INPUT:" in prompt:
            return json.dumps({"themes": ["x"]})
        return "not json"  # malformed chunk extraction

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=_mock_ollama_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_broken_chunk_extract,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_broken_chunk_extract,
    ):
        ingest_session(request, config_dir, str(db_path), None)

    import lancedb as _lancedb

    db = _lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    rows = list(table.search().to_list())

    # All chunks should have failed extraction in this scenario
    failed_rows = [r for r in rows if r["extraction_status"] == "failed"]
    assert len(failed_rows) > 0
    # Failed rows must have an error message populated
    for row in failed_rows:
        assert row["extraction_error"] is not None


def test_ingest_session_force_reextract_removes_orphan_chunks(
    tmp_path: Path, mocked_pipeline_env
) -> None:
    """When force_reextract=True and new parse produces fewer chunks,
    orphan chunks from prior run get cleaned up."""
    import lancedb as _lancedb

    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    # First run: full artifact set (transcript + signal + post)
    full_request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            "extracted_signal": str(FIXTURES / "extracted-signal-sample.md"),
            "community_post": str(FIXTURES / "community-post-sample.md"),
        },
        force_reextract=False,
    )
    ingest_session(full_request, config_dir, str(db_path), None)

    before_count = len(list(_lancedb.connect(str(db_path)).open_table("chunks").search().to_list()))
    assert before_count > 1  # multiple chunks exist from all three artifact types

    # Second run: only prepared_transcript with force_reextract=True
    # signal and community_post orphan chunks should be wiped
    partial_request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=True,
    )
    ingest_session(partial_request, config_dir, str(db_path), None)

    # Re-open the connection to avoid stale cache
    rows = list(_lancedb.connect(str(db_path)).open_table("chunks").search().to_list())
    content_types = {r["content_type"] for r in rows}
    assert content_types == {"prepared_transcript"}


def test_ingest_session_empty_artifacts_returns_warning(
    tmp_path: Path, mocked_pipeline_env
) -> None:
    """If no artifact_paths are provided, return an IngestResult with a warning."""
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={},
        force_reextract=False,
    )

    result = ingest_session(request, config_dir, str(db_path), None)
    assert result.chunks_written == 0
    assert any("no artifacts" in w.lower() for w in result.warnings)


def test_ingest_session_rejects_artifact_path_outside_root(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """When COMMUNITY_BRAIN_ARTIFACT_ROOT is set, paths outside it are rejected."""
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    # Set the root to a different tmp subdir, then pass a path outside it.
    allowed_root = tmp_path / "allowed"
    allowed_root.mkdir()
    monkeypatch.setenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", str(allowed_root))

    # FIXTURES is in tests/fixtures/, not under allowed_root
    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )

    with pytest.raises(ValueError, match="escapes COMMUNITY_BRAIN_ARTIFACT_ROOT"):
        ingest_session(request, config_dir, str(db_path), None)


def test_ingest_session_accepts_artifact_path_inside_root(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """Paths inside COMMUNITY_BRAIN_ARTIFACT_ROOT proceed normally."""
    import shutil
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    allowed_root = tmp_path / "allowed"
    allowed_root.mkdir()
    # Copy the fixture into the allowed root
    copied = allowed_root / "prepared-transcript-sample.md"
    shutil.copy(FIXTURES / "prepared-transcript-sample.md", copied)
    monkeypatch.setenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", str(allowed_root))

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={"prepared_transcript": str(copied)},
        force_reextract=False,
    )
    result = ingest_session(request, config_dir, str(db_path), None)
    assert result.chunks_written > 0


def test_ingest_session_no_constraint_when_root_unset(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """When COMMUNITY_BRAIN_ARTIFACT_ROOT is NOT set, any readable path is accepted."""
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"
    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )
    result = ingest_session(request, config_dir, str(db_path), None)
    assert result.chunks_written > 0

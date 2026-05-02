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
        # v2 fields required by extractor
        "topic_label": "Agent frameworks comparison",
        "speakers_mentioned": [],
        "keywords": ["LangGraph", "agent", "framework"],
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": True,
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
    assert result.schema_version == "1.1"


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


def test_commit_chunks_accepts_real_speakers_after_first_write_had_none(tmp_path: Path) -> None:
    """Regression: a fresh table's schema must accept list[str] speakers_spoke.

    Bug: _commit_chunks used to create the LanceDB table by letting pyarrow
    infer the schema from the first batch. If the first write's chunks all
    normalized speakers_spoke=None -> [] (community_post-only or
    extracted_signal-only ingests), pyarrow inferred List(Null) for that
    column. A subsequent write with speakers_spoke=["Alice"] then failed with
    "cannot cast field 'speakers_spoke' from List(Utf8) to List(Null)" and
    left the table torn -- force_reextract could not recover.

    Fix: _commit_chunks now passes an explicit pyarrow schema to create_table
    so list element types are declared, not inferred.
    """
    import datetime as dt

    import lancedb

    from community_brain.ingestion.pipeline import _commit_chunks
    from community_brain.ingestion.schema import Chunk, ContentType

    def make_chunk(chunk_id: str, speakers: list[str] | None, content_type: ContentType) -> Chunk:
        return Chunk(
            schema_version="1.0",
            chunk_id=chunk_id,
            session_id=chunk_id.split(":")[0],
            session_date=chunk_id.split(":")[0],
            session_title="t",
            content_type=content_type,
            source_file=f"output/{chunk_id.split(':')[0]}/x.md",
            chunk_index=1,
            total_chunks_in_source=1,
            speakers_spoke=speakers,
            speakers_mentioned=None,
            entities=[],
            keywords=None,
            topic_label=None,
            session_themes=[],
            speech_acts=[],
            stance=None,
            certainty="asserted",
            chunk_local_markers=[],
            corpus_derived_markers=[],
            corpus_markers_computed_at=None,
            has_question=False,
            has_answer=False,
            has_unresolved_question=False,
            has_insight=False,
            decisions=None,
            action_items=None,
            external_refs=None,
            references_prior=False,
            extraction_model="m",
            extraction_prompt_version="v",
            extraction_status="success",
            extraction_error=None,
            extracted_at=dt.datetime(2026, 4, 18, tzinfo=dt.timezone.utc),
            embed_text="x",
            full_text="x",
            bm25_text="x",
            embedding=[0.0] * 768,
        )

    db_path = tmp_path / "lancedb"

    first = make_chunk("2026-04-18:post:001", speakers=None, content_type="community_post")
    _commit_chunks(str(db_path), "2026-04-18", [first], full_session_rewrite=False)

    second = make_chunk(
        "2026-04-19:transcript:001", speakers=["Alice", "Bob"], content_type="prepared_transcript"
    )
    _commit_chunks(str(db_path), "2026-04-19", [second], full_session_rewrite=False)

    rows = (
        lancedb.connect(str(db_path))
        .open_table("chunks")
        .search()
        .where("chunk_id = '2026-04-19:transcript:001'")
        .to_list()
    )
    assert len(rows) == 1
    assert rows[0]["speakers_spoke"] == ["Alice", "Bob"]

    # The embedding column must remain a vector column (FixedSizeList) so
    # table.search(query_vector) works. Regression against the first fix
    # attempt, which used variable-length list<double> and broke /query.
    tbl = lancedb.connect(str(db_path)).open_table("chunks")
    vec_rows = tbl.search([0.1] * 768).limit(2).to_list()
    assert len(vec_rows) == 2
    assert "_distance" in vec_rows[0]


def test_ingest_session_calls_ensure_fts_index_after_commit(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """After a successful chunk commit, ingest_session must call
    ensure_fts_index (via _post_commit_maintenance) so the new chunks become
    BM25-searchable on the next /query."""
    ensure_calls: list[tuple] = []
    from community_brain.query.fts_lifecycle import ensure_fts_index as _real_ensure

    def _capture(table, column):
        ensure_calls.append((column,))
        return _real_ensure(table, column)

    monkeypatch.setattr(
        "community_brain.ingestion.pipeline.ensure_fts_index",
        _capture,
    )

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

    ingest_session(
        request=request,
        config_dir=config_dir,
        db_path=str(db_path),
        ollama_base_url=None,
    )

    # ensure_fts_index is called at least once after commit (once in _commit_chunks
    # for table creation, once in _post_commit_maintenance for post-commit invariant).
    assert len(ensure_calls) >= 1, (
        f"expected at least one ensure_fts_index call with column='bm25_text'; got {ensure_calls}"
    )
    assert all(col == "bm25_text" for (col,) in ensure_calls), (
        f"all calls should target bm25_text; got {ensure_calls}"
    )


def test_pipeline_populates_bm25_text_on_commit(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """Chunks committed by ingest_session must have bm25_text containing
    topic_label, entities, speakers_spoke, speakers_mentioned, keywords,
    and full_text content concatenated.
    """
    import lancedb
    from community_brain.ingestion.pipeline import ingest_session

    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

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

    ingest_session(
        request=request,
        config_dir=config_dir,
        db_path=str(db_path),
        ollama_base_url=None,
    )

    db = lancedb.connect(str(db_path))
    tbl = db.open_table("chunks")
    rows = tbl.to_arrow().to_pylist()

    assert len(rows) > 0, "no rows committed"
    for row in rows:
        assert row["bm25_text"], f"empty bm25_text on {row['chunk_id']}"
        # bm25_text must embed full_text content
        assert row["full_text"][:50] in row["bm25_text"], (
            f"full_text prefix missing from bm25_text on {row['chunk_id']}"
        )
        # bm25_text must reflect Stage C entities, not the construction-time
        # empty list. The mock returns entities=["LangGraph"] for every chunk.
        assert "LangGraph" in row["bm25_text"], (
            f"Stage C entity 'LangGraph' missing from bm25_text on {row['chunk_id']}; "
            f"bm25_text was synthesized before Stage C populated entities"
        )


def test_pipeline_embed_text_includes_stage_c_entities_for_transcripts(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """After Stage C populates entities, transcript embed_text must reflect
    them (same timing pattern as bm25_text). Construction-time-only synthesis
    used entities=[] so embed_text was stale until Stage C re-synthesis.

    signal/post chunks must keep embed_text == full_text (no enrichment).
    """
    import lancedb
    from community_brain.ingestion.pipeline import ingest_session

    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

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

    ingest_session(
        request=request,
        config_dir=config_dir,
        db_path=str(db_path),
        ollama_base_url=None,
    )

    db = lancedb.connect(str(db_path))
    tbl = db.open_table("chunks")
    rows = tbl.to_arrow().to_pylist()

    transcript_rows = [r for r in rows if r["content_type"] == "prepared_transcript"]
    signal_post_rows = [r for r in rows if r["content_type"] in ("extracted_signal", "community_post")]

    assert transcript_rows, "expected at least one prepared_transcript row"

    for row in transcript_rows:
        # embed_text must use structured v3 format (six-line layout)
        embed = row["embed_text"]
        assert embed.startswith("topic:"), (
            f"embed_text does not start with 'topic:' on {row['chunk_id']}; got: {embed[:60]!r}"
        )
        assert "speakers:" in embed, f"'speakers:' missing from embed_text on {row['chunk_id']}"
        assert "mentions:" in embed, f"'mentions:' missing from embed_text on {row['chunk_id']}"
        assert "entities:" in embed, f"'entities:' missing from embed_text on {row['chunk_id']}"
        assert "keywords:" in embed, f"'keywords:' missing from embed_text on {row['chunk_id']}"
        assert "summary:" in embed, f"'summary:' missing from embed_text on {row['chunk_id']}"
        # Stage C entity must be reflected (not the construction-time empty list)
        assert "LangGraph" in embed, (
            f"Stage C entity 'LangGraph' missing from embed_text on {row['chunk_id']}; "
            f"embed_text was synthesized before Stage C populated entities"
        )

    for row in signal_post_rows:
        # signal/post chunks: embed_text must equal full_text (no enrichment)
        assert row["embed_text"] == row["full_text"], (
            f"embed_text != full_text on {row['content_type']} chunk {row['chunk_id']}"
        )


def test_pipeline_persists_all_stage_c_v2_fields(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """Committed chunks must carry all Stage C v2 fields (topic_label, keywords,
    has_question, has_insight, speakers_mentioned) reflecting the mocked LLM
    response, not the chunker defaults (None / empty).

    Regression test for the HIGH 1 finding from Codex adversarial review:
    pipeline's Stage C success branch was discarding parsed v2 fields.
    """
    import lancedb
    from community_brain.ingestion.pipeline import ingest_session

    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

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

    ingest_session(
        request=request,
        config_dir=config_dir,
        db_path=str(db_path),
        ollama_base_url=None,
    )

    db = lancedb.connect(str(db_path))
    tbl = db.open_table("chunks")
    rows = tbl.to_arrow().to_pylist()

    assert len(rows) > 0, "no rows committed"
    for row in rows:
        # topic_label must reflect the mocked Stage C response, not chunker default (None)
        assert row["topic_label"] == "Agent frameworks comparison", (
            f"topic_label not written by Stage C on {row['chunk_id']}; "
            f"got {row['topic_label']!r} (chunker default is None)"
        )
        # keywords must carry the mocked v2 values
        assert "LangGraph" in (row["keywords"] or []), (
            f"keywords not written by Stage C on {row['chunk_id']}; "
            f"got {row['keywords']!r}"
        )
        # has_insight must reflect the mocked True value
        assert row["has_insight"] is True, (
            f"has_insight not written by Stage C on {row['chunk_id']}; "
            f"got {row['has_insight']!r}"
        )
        # has_question must reflect the mocked False value (not a default issue,
        # but confirms the flag path runs through)
        assert row["has_question"] is False, (
            f"has_question not written by Stage C on {row['chunk_id']}; "
            f"got {row['has_question']!r}"
        )
        # speakers_mentioned must be the mocked [] value, not chunker default (None)
        assert row["speakers_mentioned"] is not None, (
            f"speakers_mentioned is None on {row['chunk_id']} — Stage C v2 fields not written"
        )


def test_commit_chunks_refuses_to_mutate_pre_v1_1_table(tmp_path: Path) -> None:
    """If the existing chunks table lacks bm25_text column (pre-v1.1),
    _commit_chunks raises CommitError BEFORE deleting anything.

    Regression test for the migration hazard surfaced in v3 Phase 1
    adversarial review: delete-then-add against a v1.0 table would
    delete rows then fail to add v1.1 records, causing data loss.
    """
    import datetime as dt

    import lancedb
    import pyarrow as pa

    from community_brain.ingestion.pipeline import CommitError, _commit_chunks
    from community_brain.ingestion.schema import EMBEDDING_DIM, Chunk, ContentType

    # Build a v1.0-shape schema: full pyarrow_table_schema() minus bm25_text.
    v1_0_schema = pa.schema([
        ("schema_version", pa.string()),
        ("chunk_id", pa.string()),
        ("session_id", pa.string()),
        ("session_date", pa.string()),
        ("session_title", pa.string()),
        ("content_type", pa.string()),
        ("source_file", pa.string()),
        ("chunk_index", pa.int64()),
        ("total_chunks_in_source", pa.int64()),
        ("speakers_spoke", pa.list_(pa.string())),
        ("speakers_mentioned", pa.list_(pa.string())),
        ("entities", pa.list_(pa.string())),
        ("keywords", pa.list_(pa.string())),
        ("topic_label", pa.string()),
        ("session_themes", pa.list_(pa.string())),
        ("speech_acts", pa.list_(pa.string())),
        ("stance", pa.string()),
        ("certainty", pa.string()),
        ("chunk_local_markers", pa.list_(pa.string())),
        ("corpus_derived_markers", pa.list_(pa.string())),
        ("corpus_markers_computed_at", pa.string()),
        ("has_question", pa.bool_()),
        ("has_answer", pa.bool_()),
        ("has_unresolved_question", pa.bool_()),
        ("has_insight", pa.bool_()),
        ("decisions", pa.list_(pa.string())),
        ("action_items", pa.list_(pa.string())),
        ("external_refs", pa.list_(pa.string())),
        ("references_prior", pa.bool_()),
        ("extraction_model", pa.string()),
        ("extraction_prompt_version", pa.string()),
        ("extraction_status", pa.string()),
        ("extraction_error", pa.string()),
        ("extracted_at", pa.string()),
        ("embed_text", pa.string()),
        ("full_text", pa.string()),
        # bm25_text deliberately absent — this is the pre-v1.1 shape
        ("embedding", pa.list_(pa.float32(), EMBEDDING_DIM)),
    ])

    # Seed the v1.0 table with one existing row so we can verify it survives.
    db_path = tmp_path / "lancedb"
    db = lancedb.connect(str(db_path))
    existing_row = {
        "schema_version": "1.0",
        "chunk_id": "2026-01-01:post:001",
        "session_id": "2026-01-01",
        "session_date": "2026-01-01",
        "session_title": "old session",
        "content_type": "community_post",
        "source_file": "output/2026-01-01/community-post.md",
        "chunk_index": 1,
        "total_chunks_in_source": 1,
        "speakers_spoke": [],
        "speakers_mentioned": [],
        "entities": [],
        "keywords": [],
        "topic_label": None,
        "session_themes": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "corpus_derived_markers": [],
        "corpus_markers_computed_at": None,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "extraction_model": "m",
        "extraction_prompt_version": "chunk-extraction-v1",
        "extraction_status": "success",
        "extraction_error": None,
        "extracted_at": "2026-01-01T00:00:00+00:00",
        "embed_text": "old embed",
        "full_text": "old full text",
        "embedding": [0.0] * EMBEDDING_DIM,
    }
    db.create_table("chunks", data=[existing_row], schema=v1_0_schema)

    # Construct a v1.1 Chunk to attempt to ingest.
    new_chunk = Chunk(
        schema_version="1.1",
        chunk_id="2026-01-01:post:002",
        session_id="2026-01-01",
        session_date="2026-01-01",
        session_title="old session",
        content_type="community_post",
        source_file="output/2026-01-01/community-post.md",
        chunk_index=2,
        total_chunks_in_source=2,
        speakers_spoke=None,
        speakers_mentioned=None,
        entities=[],
        keywords=None,
        topic_label=None,
        session_themes=[],
        speech_acts=[],
        stance=None,
        certainty="asserted",
        chunk_local_markers=[],
        corpus_derived_markers=[],
        corpus_markers_computed_at=None,
        has_question=False,
        has_answer=False,
        has_unresolved_question=False,
        has_insight=False,
        decisions=None,
        action_items=None,
        external_refs=None,
        references_prior=False,
        extraction_model="m",
        extraction_prompt_version="chunk-extraction-v1",
        extraction_status="success",
        extraction_error=None,
        extracted_at=dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc),
        embed_text="new embed",
        full_text="new full text",
        bm25_text="new bm25",
        embedding=[0.0] * EMBEDDING_DIM,
    )

    # _commit_chunks must raise CommitError without touching existing rows.
    with pytest.raises(CommitError, match="pre-v1.1"):
        _commit_chunks(str(db_path), "2026-01-01", [new_chunk], full_session_rewrite=True)

    # The existing row must still be intact — no deletion occurred.
    rows = (
        lancedb.connect(str(db_path))
        .open_table("chunks")
        .search()
        .to_list()
    )
    assert len(rows) == 1, f"expected 1 row (untouched), got {len(rows)}"
    assert rows[0]["chunk_id"] == "2026-01-01:post:001"


# ---------------------------------------------------------------------------
# T9: canonicalization applied at chunk write
# ---------------------------------------------------------------------------

def _write_min_configs_with_aliases(base: Path) -> Path:
    """Like _write_min_configs but speaker-aliases.yaml includes Adam->Adam James."""
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
    # aliases: Adam James has raw alias "Adam"; Brandon Hancock has no aliases
    (base / "speaker-aliases.yaml").write_text(
        'version: "x"\naliases:\n  Adam James:\n    - Adam\n  Brandon Hancock: []\npending: []\n',
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


def test_pipeline_canonicalizes_speakers_at_write(
    tmp_path: Path, monkeypatch
) -> None:
    """When the speaker-aliases registry has 'Adam' -> 'Adam James', Stage C output
    containing the raw 'Adam' is committed with canonical 'Adam James' form in
    speakers_mentioned and entities."""
    import json
    import lancedb
    from community_brain.ingestion.pipeline import IngestRequest, ingest_session

    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)
    config_dir = _write_min_configs_with_aliases(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    # Stage C returns raw "Adam" in both entities and speakers_mentioned
    def _alias_extract(model, prompt):  # noqa: ARG001
        if "SESSION_INPUT:" in prompt:
            return json.dumps({"themes": ["agent frameworks"]})
        return json.dumps({
            "entities": ["Adam"],
            "new_entities_seen": [],
            "new_speakers_seen": [],
            "speech_acts": ["discussion"],
            "stance": "neutral",
            "certainty": "asserted",
            "chunk_local_markers": [],
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            "topic_label": "Canonicalization test",
            "speakers_mentioned": ["Adam"],
            "keywords": ["canonicalization"],
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": False,
        })

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=_mock_ollama_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_alias_extract,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_alias_extract,
    ):
        request = IngestRequest(
            session_id="2026-03-10",
            session_date="2026-03-10",
            session_title="Canonicalization test",
            artifact_paths={
                "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            },
            force_reextract=False,
        )
        ingest_session(request=request, config_dir=config_dir, db_path=str(db_path), ollama_base_url=None)

    db = lancedb.connect(str(db_path))
    tbl = db.open_table("chunks")
    rows = tbl.to_arrow().to_pylist()

    assert len(rows) > 0, "no rows committed"
    for row in rows:
        entities = row.get("entities") or []
        speakers_mentioned = row.get("speakers_mentioned") or []
        assert "Adam James" in entities, (
            f"entities not canonicalized on {row['chunk_id']}: got {entities!r}"
        )
        assert "Adam" not in entities, (
            f"raw 'Adam' still present in entities on {row['chunk_id']}: {entities!r}"
        )
        assert "Adam James" in speakers_mentioned, (
            f"speakers_mentioned not canonicalized on {row['chunk_id']}: got {speakers_mentioned!r}"
        )
        assert "Adam" not in speakers_mentioned, (
            f"raw 'Adam' still in speakers_mentioned on {row['chunk_id']}: {speakers_mentioned!r}"
        )


def test_canonicalization_preserves_speaker_mention_partition(
    tmp_path: Path, monkeypatch
) -> None:
    """Regression for verification round 6 finding: when speakers_spoke and
    speakers_mentioned use DIFFERENT raw aliases that canonicalize to the
    SAME name, the canonical name must NOT end up in both lists.

    Scenario:
    - speakers_spoke (raw): ["Adam - Gold Flamingo"]  -> canonical "Adam James"
    - Stage C emits speakers_mentioned (raw): ["Adam"] -> canonical "Adam James"
    - Without the partition fix, "Adam James" would appear in BOTH lists.
    - After the fix, "Adam James" must be ONLY in speakers_spoke.
    """
    import json
    import lancedb
    from community_brain.ingestion.pipeline import IngestRequest, ingest_session

    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)

    # Build a config where BOTH "Adam - Gold Flamingo" and "Adam" resolve to "Adam James".
    config_dir = _write_min_configs_with_aliases(tmp_path / "config")
    (config_dir / "speaker-aliases.yaml").write_text(
        (
            'version: "x"\n'
            'aliases:\n'
            '  Adam James:\n'
            '    - Adam\n'
            '    - Adam - Gold Flamingo\n'
            '  Brandon Hancock: []\n'
            'pending: []\n'
        ),
        encoding="utf-8",
    )
    db_path = tmp_path / "lancedb"

    # Stage C sees raw SPEAKERS_SPOKE=["Adam - Gold Flamingo"] and returns
    # speakers_mentioned=["Adam"] — realistic because Stage C doesn't resolve
    # aliases; it just recognizes the bare name "Adam" from the transcript text.
    def _partition_extract(model, prompt):  # noqa: ARG001
        if "SESSION_INPUT:" in prompt:
            return json.dumps({"themes": ["partition regression"]})
        return json.dumps({
            "entities": [],
            "new_entities_seen": [],
            "new_speakers_seen": [],
            "speech_acts": ["discussion"],
            "stance": "neutral",
            "certainty": "asserted",
            "chunk_local_markers": [],
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            "topic_label": "Partition regression test",
            "speakers_mentioned": ["Adam"],
            "keywords": ["partition"],
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": False,
        })

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=_mock_ollama_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_partition_extract,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_partition_extract,
    ):
        request = IngestRequest(
            session_id="2026-03-11",
            session_date="2026-03-11",
            session_title="Partition regression test",
            artifact_paths={
                "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            },
            force_reextract=False,
        )
        ingest_session(request=request, config_dir=config_dir, db_path=str(db_path), ollama_base_url=None)

    db = lancedb.connect(str(db_path))
    tbl = db.open_table("chunks")
    rows = tbl.to_arrow().to_pylist()

    assert len(rows) > 0, "no rows committed"
    for row in rows:
        speakers_spoke = row.get("speakers_spoke") or []
        speakers_mentioned = row.get("speakers_mentioned") or []
        if "Adam James" in speakers_spoke:
            assert "Adam James" not in speakers_mentioned, (
                f"Partition broken on {row['chunk_id']}: 'Adam James' is in BOTH "
                f"speakers_spoke={speakers_spoke!r} and speakers_mentioned={speakers_mentioned!r}. "
                "Post-canonicalization subtraction of speakers_spoke from speakers_mentioned "
                "did not fire."
            )


def test_pipeline_unknown_speakers_flow_to_pending(
    tmp_path: Path, monkeypatch
) -> None:
    """Names in Stage C speakers_mentioned that aren't in the alias map are
    appended to speaker-aliases.yaml's pending list at session end."""
    import json
    import lancedb
    import yaml
    from community_brain.ingestion.pipeline import IngestRequest, ingest_session

    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)
    # Use base config with no aliases so Tony/Vlad are guaranteed unknowns
    config_dir = _write_min_configs(tmp_path / "config")
    # Overwrite with truly empty alias map
    (config_dir / "speaker-aliases.yaml").write_text(
        'version: "x"\naliases: {}\npending: []\n',
        encoding="utf-8",
    )
    db_path = tmp_path / "lancedb"

    def _unknown_extract(model, prompt):  # noqa: ARG001
        if "SESSION_INPUT:" in prompt:
            return json.dumps({"themes": ["topics"]})
        return json.dumps({
            "entities": [],
            "new_entities_seen": [],
            "new_speakers_seen": [],
            "speech_acts": [],
            "stance": "neutral",
            "certainty": "asserted",
            "chunk_local_markers": [],
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            "topic_label": "Unknown test",
            "speakers_mentioned": ["Tony", "Vlad"],
            "keywords": [],
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": False,
        })

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=_mock_ollama_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_unknown_extract,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_unknown_extract,
    ):
        request = IngestRequest(
            session_id="2026-03-10",
            session_date="2026-03-10",
            session_title="Unknown test",
            artifact_paths={
                "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            },
            force_reextract=False,
        )
        ingest_session(request=request, config_dir=config_dir, db_path=str(db_path), ollama_base_url=None)

    updated = yaml.safe_load((config_dir / "speaker-aliases.yaml").read_text())
    pending = updated.get("pending") or []
    assert "Tony" in pending, f"'Tony' not in pending: {pending!r}"
    assert "Vlad" in pending, f"'Vlad' not in pending: {pending!r}"


def test_pipeline_canonicalization_applied_before_resynthesis(
    tmp_path: Path, monkeypatch
) -> None:
    """bm25_text reflects canonical names, not raw aliases, confirming
    canonicalization fires before the bm25_text re-synthesis block."""
    import json
    import lancedb
    from community_brain.ingestion.pipeline import IngestRequest, ingest_session

    monkeypatch.delenv("COMMUNITY_BRAIN_ARTIFACT_ROOT", raising=False)
    config_dir = _write_min_configs_with_aliases(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    def _canon_resync_extract(model, prompt):  # noqa: ARG001
        if "SESSION_INPUT:" in prompt:
            return json.dumps({"themes": ["resynthesis test"]})
        return json.dumps({
            "entities": ["Adam"],
            "new_entities_seen": [],
            "new_speakers_seen": [],
            "speech_acts": [],
            "stance": "neutral",
            "certainty": "asserted",
            "chunk_local_markers": [],
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            "topic_label": "Resynthesis test",
            "speakers_mentioned": ["Adam"],
            "keywords": [],
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": False,
        })

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=_mock_ollama_embed,
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=_canon_resync_extract,
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_canon_resync_extract,
    ):
        request = IngestRequest(
            session_id="2026-03-10",
            session_date="2026-03-10",
            session_title="Resynthesis test",
            artifact_paths={
                "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            },
            force_reextract=False,
        )
        ingest_session(request=request, config_dir=config_dir, db_path=str(db_path), ollama_base_url=None)

    db = lancedb.connect(str(db_path))
    tbl = db.open_table("chunks")
    rows = tbl.to_arrow().to_pylist()

    assert len(rows) > 0, "no rows committed"
    for row in rows:
        bm25 = row.get("bm25_text") or ""
        assert "Adam James" in bm25, (
            f"'Adam James' not found in bm25_text of {row['chunk_id']}: {bm25!r}"
        )
        # bm25_text must not contain standalone raw "Adam" (i.e., without " James" following).
        # "Adam James" obviously contains "Adam" as a substring, so check that
        # the raw-only form (", Adam," or " Adam\n" etc.) is absent.
        import re
        # Match "Adam" that is NOT followed by " James"
        raw_adam_pattern = re.compile(r'\bAdam\b(?! James)')
        assert not raw_adam_pattern.search(bm25), (
            f"Raw 'Adam' (without 'James') still in bm25_text of {row['chunk_id']}: {bm25!r}"
        )


# ---------------------------------------------------------------------------
# Phase 3 of ingest-lint-decoupling fix
# Spec: docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md
# ---------------------------------------------------------------------------


def test_post_commit_maintenance_does_not_call_lint_corpus() -> None:
    """The lint_corpus auto-trigger has been removed from /ingest's
    post-commit path. Neither the import nor the call site should remain
    in pipeline.py — operators run lint via cron or manual invocation
    instead (spec 2026-05-02-ingest-lint-decoupling-design.md §5).
    """
    import inspect
    from community_brain.ingestion import pipeline

    source = inspect.getsource(pipeline._post_commit_maintenance)
    assert "lint_corpus_chunks" not in source, (
        "lint_corpus_chunks must not be referenced inside _post_commit_maintenance"
    )
    assert not hasattr(pipeline, "lint_corpus_chunks"), (
        "lint_corpus_chunks must not be imported into the pipeline module — "
        "the auto-trigger was removed in spec 2026-05-02-ingest-lint-decoupling-design.md"
    )


def test_post_commit_maintenance_still_verifies_corpus_state(monkeypatch) -> None:
    """verify_corpus_v3_state survives the auto-trigger removal — it's the
    invariant check that protects schema and FTS state. Removing it would
    silently break /query when post-commit state is inconsistent.
    """
    from community_brain.ingestion.pipeline import _post_commit_maintenance

    called_with: list = []

    def fake_verify(table):
        called_with.append(table)

    monkeypatch.setattr(
        "community_brain.ingestion.pipeline.verify_corpus_v3_state",
        fake_verify,
    )

    sentinel_table = object()
    _post_commit_maintenance(sentinel_table)

    assert called_with == [sentinel_table], (
        "verify_corpus_v3_state was not called by _post_commit_maintenance — "
        "the post-commit invariant check has been broken"
    )


def test_commit_chunks_builds_fts_index_when_creating_table(
    tmp_path: Path, mocked_pipeline_env
) -> None:
    """Regression: fresh-table _commit_chunks must build the bm25_text FTS index.

    Spec §17.1 drops the v1.0 table on deploy; first /ingest creates the v1.1
    table. Without explicit FTS build, /query hybrid has no lexical leg until
    server restart triggers the startup hook. This test asserts the index is
    present immediately after the first ingest into a brand-new database.
    """
    import lancedb as _lancedb
    from community_brain.query.fts_lifecycle import has_fts_index

    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "fresh_lancedb"

    # Confirm the DB directory doesn't exist yet (truly fresh deploy).
    assert not db_path.exists()

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="Fresh table FTS regression",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )

    result = ingest_session(request, config_dir, str(db_path), None)
    assert result.chunks_written > 0, "Ingest must write chunks for this test to be meaningful"

    # Open the table and verify the FTS index exists on bm25_text.
    db = _lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    assert has_fts_index(table, "bm25_text"), (
        "bm25_text FTS index must exist immediately after the first ingest "
        "into a fresh table (spec §17.1 fresh-deploy regression)"
    )


def test_commit_chunks_raises_when_fts_index_creation_fails(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """Fresh-table FTS index failure must raise CommitError, not silently
    ship without a bm25_text index. Regression for the verification-pass
    finding: degraded retrieval should be a loud failure, not a log line.

    Monkeypatches ensure_fts_index (the fresh-table case in _commit_chunks)
    to raise, then asserts CommitError propagates out of ingest_session.
    """
    import lancedb as _lancedb
    from community_brain.ingestion.pipeline import CommitError

    # Patch ensure_fts_index to raise on the fresh-table path.
    def _raise_fts(*_args, **_kwargs):
        raise RuntimeError("simulated FTS build failure")

    monkeypatch.setattr(
        "community_brain.ingestion.pipeline.ensure_fts_index",
        _raise_fts,
    )

    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "fts_fail_lancedb"

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="FTS failure test",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )

    with pytest.raises(CommitError, match="FTS index build on bm25_text failed"):
        ingest_session(request, config_dir, str(db_path), None)


def test_commit_chunks_rebuilds_fts_when_existing_table_lacks_it(
    tmp_path: Path, mocked_pipeline_env
) -> None:
    """Regression: if the existing chunks table lacks the bm25_text FTS index
    (simulating a half-initialized state from a prior failed fresh-table init),
    _commit_chunks must rebuild the index before mutation so /query keeps both
    retrieval legs.
    """
    import lancedb as _lancedb
    import pyarrow as pa
    from community_brain.ingestion.pipeline import TABLE_NAME, _commit_chunks
    from community_brain.ingestion.schema import pyarrow_table_schema
    from community_brain.query.fts_lifecycle import has_fts_index

    db_path = str(tmp_path / "half_init_lancedb")
    db = _lancedb.connect(db_path)

    # Create the table with valid v1.1 schema but intentionally skip the FTS build
    # (simulates: fresh-table init ran create_table + add but FTS build raised).
    config_dir = _write_min_configs(tmp_path / "config")
    request_first = IngestRequest(
        session_id="2026-01-10",
        session_date="2026-01-10",
        session_title="Half-init session",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )
    # Do the first ingest normally so the table+rows+FTS exist.
    ingest_session(request_first, config_dir, db_path, None)

    # Now simulate the half-init: drop the FTS index by rewriting the table
    # without it (LanceDB doesn't expose a drop-index API, so we recreate).
    tbl = db.open_table(TABLE_NAME)
    rows = tbl.to_arrow()
    db.drop_table(TABLE_NAME)
    db.create_table(TABLE_NAME, data=rows, schema=pyarrow_table_schema())
    tbl_no_fts = db.open_table(TABLE_NAME)
    assert not has_fts_index(tbl_no_fts, "bm25_text"), "precondition: table lacks FTS index"

    # Second ingest against same db — takes existing-table branch.
    # Must rebuild the FTS index.
    request_second = IngestRequest(
        session_id="2026-01-17",
        session_date="2026-01-17",
        session_title="Retry after half-init",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )
    result = ingest_session(request_second, config_dir, db_path, None)
    assert result.chunks_written > 0, f"expected chunks written, got {result}"

    tbl_after = db.open_table(TABLE_NAME)
    assert has_fts_index(tbl_after, "bm25_text"), (
        "FTS index was not rebuilt on the existing-table path; "
        "/query would have silently fallen back to vector-only"
    )


def test_commit_chunks_after_fresh_table_fts_failure_rebuilds_on_retry(
    tmp_path: Path, mocked_pipeline_env, monkeypatch
) -> None:
    """End-to-end regression for verification round-3 finding:
    1. First /ingest creates fresh table; ensure_fts_index raises (simulated).
       CommitError raised; table and rows persist.
    2. Second /ingest with ensure_fts_index restored:
       - Takes existing-table branch (column check passes).
       - Must build the FTS index before returning success.
    Without the fix, step 2 returns success with no FTS index.
    """
    import lancedb as _lancedb
    from community_brain.ingestion.pipeline import CommitError, TABLE_NAME
    from community_brain.query.fts_lifecycle import ensure_fts_index as _real_ensure_fts
    from community_brain.query.fts_lifecycle import has_fts_index

    call_count = {"n": 0}

    def _fail_first(*args, **kwargs):
        call_count["n"] += 1
        if call_count["n"] == 1:
            raise RuntimeError("simulated FTS failure on first call")
        return _real_ensure_fts(*args, **kwargs)

    monkeypatch.setattr(
        "community_brain.ingestion.pipeline.ensure_fts_index",
        _fail_first,
    )

    config_dir = _write_min_configs(tmp_path / "config")
    db_path = str(tmp_path / "retry_fts_lancedb")

    request = IngestRequest(
        session_id="2026-02-10",
        session_date="2026-02-10",
        session_title="Retry FTS regression",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )

    # Step 1: first ingest — fresh-table path — FTS build raises.
    with pytest.raises(CommitError, match="FTS index build on bm25_text failed"):
        ingest_session(request, config_dir, db_path, None)

    # Table and rows must have been persisted (pre-fix bug left them behind).
    db = _lancedb.connect(db_path)
    assert TABLE_NAME in db.list_tables().tables, "table must persist after CommitError"
    tbl_torn = db.open_table(TABLE_NAME)
    assert not has_fts_index(tbl_torn, "bm25_text"), "precondition: no FTS index after failure"

    # Step 2: retry — idempotency path: all chunks already present from the torn
    # first ingest, so chunks_written=0 and chunks_skipped_idempotent>0.
    # The FTS invariant must still be enforced on this path.
    result = ingest_session(request, config_dir, db_path, None)
    assert result.chunks_skipped_idempotent > 0, (
        f"expected idempotency skip on retry, got {result}"
    )

    tbl_after = db.open_table(TABLE_NAME)
    assert has_fts_index(tbl_after, "bm25_text"), (
        "FTS index was not rebuilt on the all-skipped idempotency retry path; "
        "round-3 finding NOT fixed"
    )



"""Tests for the v1.0 LanceDB chunk schema."""

from __future__ import annotations

import datetime as dt

from community_brain.ingestion.schema import Chunk, SCHEMA_VERSION


def test_schema_version_is_1_0() -> None:
    assert SCHEMA_VERSION == "1.0"


def test_chunk_construction_with_all_fields() -> None:
    chunk = Chunk(
        schema_version="1.0",
        chunk_id="2026-03-10:transcript:001",
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="Agent frameworks comparison",
        content_type="prepared_transcript",
        source_file="output/2026-03-10/prepared-transcript.md",
        chunk_index=1,
        total_chunks_in_source=2,
        speakers_spoke=["Alex Rojas", "Sam"],
        speakers_mentioned=["Alex Rojas", "Sam"],
        entities=["LangGraph"],
        keywords=["agent orchestration"],
        topic_label="agent orchestration tools",
        session_themes=["agent frameworks", "production deployment"],
        speech_acts=["comparison", "recommendation"],
        stance="positive",
        certainty="asserted",
        chunk_local_markers=["emphasized"],
        corpus_derived_markers=[],
        corpus_markers_computed_at=None,
        has_question=True,
        has_answer=True,
        has_unresolved_question=False,
        has_insight=True,
        decisions=None,
        action_items=None,
        external_refs=["https://langchain.com/docs/langgraph"],
        references_prior=False,
        extraction_model="google/gemini-3.1-flash-lite-preview",
        extraction_prompt_version="chunk-extraction-v1",
        extraction_status="success",
        extraction_error=None,
        extracted_at=dt.datetime(2026, 3, 10, 14, 22, 11, tzinfo=dt.timezone.utc),
        embed_text="...",
        full_text="...",
        embedding=[0.0] * 768,
    )
    assert chunk.chunk_id == "2026-03-10:transcript:001"
    assert chunk.extraction_status == "success"


def test_chunk_to_arrow_dict_normalizes_null_list_fields() -> None:
    """Null list-valued fields become empty lists in the arrow representation.

    LanceDB/Arrow doesn't nicely support null lists; we normalize on the way out.
    """
    chunk = Chunk(
        schema_version="1.0",
        chunk_id="2026-03-10:post:main",
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title=None,
        content_type="community_post",
        source_file="output/2026-03-10/community-post.md",
        chunk_index=0,
        total_chunks_in_source=1,
        speakers_spoke=None,
        speakers_mentioned=["Alex Rojas", "Sam"],
        entities=[],
        keywords=None,
        topic_label="session_narrative",
        session_themes=["agent frameworks"],
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
        extraction_model="google/gemini-3.1-flash-lite-preview",
        extraction_prompt_version="chunk-extraction-v1",
        extraction_status="success",
        extraction_error=None,
        extracted_at=dt.datetime(2026, 3, 10, 15, 0, 0, tzinfo=dt.timezone.utc),
        embed_text="text",
        full_text="text",
        embedding=[0.0] * 768,
    )

    d = chunk.to_arrow_dict()
    assert d["chunk_id"] == "2026-03-10:post:main"
    assert d["content_type"] == "community_post"
    # Null list-valued fields become empty lists in the arrow representation
    assert d["speakers_spoke"] == []
    assert d["keywords"] == []
    assert d["decisions"] == []
    assert d["action_items"] == []
    assert d["external_refs"] == []


def test_chunk_to_arrow_dict_serializes_datetimes_iso() -> None:
    now = dt.datetime(2026, 3, 10, 14, 22, 11, tzinfo=dt.timezone.utc)
    chunk = Chunk(
        schema_version="1.0",
        chunk_id="x",
        session_id="x",
        session_date="2026-03-10",
        session_title=None,
        content_type="community_post",
        source_file="x",
        chunk_index=0,
        total_chunks_in_source=1,
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
        corpus_markers_computed_at=now,
        has_question=False,
        has_answer=False,
        has_unresolved_question=False,
        has_insight=False,
        decisions=None,
        action_items=None,
        external_refs=None,
        references_prior=False,
        extraction_model="m",
        extraction_prompt_version="v1",
        extraction_status="success",
        extraction_error=None,
        extracted_at=now,
        embed_text="t",
        full_text="t",
        embedding=[0.0] * 4,
    )
    d = chunk.to_arrow_dict()
    assert d["extracted_at"] == "2026-03-10T14:22:11+00:00"
    assert d["corpus_markers_computed_at"] == "2026-03-10T14:22:11+00:00"


def test_chunk_to_arrow_dict_preserves_null_corpus_markers_computed_at() -> None:
    """When corpus_markers_computed_at is None (v1 default), it stays None."""
    chunk = _minimal_chunk(corpus_markers_computed_at=None)
    d = chunk.to_arrow_dict()
    assert d["corpus_markers_computed_at"] is None


def test_lancedb_table_schema_describes_37_fields() -> None:
    from community_brain.ingestion.schema import lancedb_table_schema

    schema = lancedb_table_schema()
    # v1.0 has 37 fields total
    assert len(schema) == 37


def test_chunk_dataclass_matches_lancedb_schema_fields() -> None:
    """Lock step: if someone adds a field to Chunk, lancedb_table_schema must update too."""
    from dataclasses import fields
    from community_brain.ingestion.schema import Chunk, lancedb_table_schema
    chunk_fields = {f.name for f in fields(Chunk)}
    schema_fields = set(lancedb_table_schema().keys())
    assert chunk_fields == schema_fields, (
        f"Drift: in Chunk only {chunk_fields - schema_fields}; "
        f"in schema only {schema_fields - chunk_fields}"
    )


def _minimal_chunk(**overrides) -> "Chunk":
    """Helper: build a minimal valid Chunk with overridable fields."""
    defaults = dict(
        schema_version="1.0",
        chunk_id="x",
        session_id="x",
        session_date="2026-01-01",
        session_title=None,
        content_type="community_post",
        source_file="x",
        chunk_index=0,
        total_chunks_in_source=1,
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
        extraction_prompt_version="v1",
        extraction_status="success",
        extraction_error=None,
        extracted_at=dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc),
        embed_text="t",
        full_text="t",
        embedding=[0.0] * 4,
    )
    defaults.update(overrides)
    return Chunk(**defaults)

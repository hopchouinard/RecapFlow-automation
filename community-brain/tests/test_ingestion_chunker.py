"""Tests for the chunker that composes Chunk records from parsed artifacts."""

from __future__ import annotations

from pathlib import Path

from community_brain.ingestion.parser import (
    parse_prepared_transcript,
    parse_extracted_signal,
    parse_community_post,
)
from community_brain.ingestion.chunker import (
    chunk_prepared_transcript,
    chunk_extracted_signal,
    chunk_community_post,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_chunk_prepared_transcript_creates_one_chunk_per_segment() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)

    chunks = chunk_prepared_transcript(
        segments,
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="Agent frameworks comparison",
        source_file="output/2026-03-10/prepared-transcript.md",
        segment_max_tokens=1500,
    )

    assert len(chunks) == 2
    assert chunks[0].chunk_id == "2026-03-10:transcript:001"
    assert chunks[1].chunk_id == "2026-03-10:transcript:002"
    assert chunks[0].content_type == "prepared_transcript"
    assert chunks[0].total_chunks_in_source == 2


def test_chunk_prepared_transcript_embed_text_uses_segment_header() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)
    chunks = chunk_prepared_transcript(
        segments, "2026-03-10", "2026-03-10",
        "Agent frameworks comparison",
        "output/2026-03-10/prepared-transcript.md",
        1500,
    )
    first = chunks[0]
    assert "agent orchestration tools" in first.embed_text  # topic
    assert "LangChain" in first.embed_text  # keywords present in embed input
    assert first.topic_label == "agent orchestration tools"


def test_chunk_prepared_transcript_speakers_spoke_from_body() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)
    chunks = chunk_prepared_transcript(
        segments, "2026-03-10", "2026-03-10", "t", "t", 1500,
    )
    speakers_spoke = chunks[0].speakers_spoke or []
    assert "Alex Rojas" in speakers_spoke
    assert "Sam" in speakers_spoke


def test_chunk_prepared_transcript_flags_qa_and_insight() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)
    chunks = chunk_prepared_transcript(
        segments, "2026-03-10", "2026-03-10", "t", "t", 1500,
    )
    # First segment has <Q>, <A>, and ▶
    assert chunks[0].has_question is True
    assert chunks[0].has_answer is True
    assert chunks[0].has_unresolved_question is False
    assert chunks[0].has_insight is True


def test_chunk_prepared_transcript_flags_unresolved_question() -> None:
    """If a segment has <Q> but no matching <A>, has_unresolved_question is True."""
    import re
    from community_brain.ingestion.parser import TranscriptSegment
    seg = TranscriptSegment(
        topic="t",
        speakers=["A"],
        keywords=["k"],
        summary="s",
        body="[00:00:00] A: text\n<Q>[00:01:00] A: open question</Q>\nmore text after without answer",
    )
    chunks = chunk_prepared_transcript([seg], "d", "d", "t", "t", 1500)
    assert chunks[0].has_question is True
    assert chunks[0].has_answer is False
    assert chunks[0].has_unresolved_question is True


def test_chunk_prepared_transcript_sub_chunks_large_segment() -> None:
    """A segment whose body exceeds segment_max_tokens gets sliding-window split."""
    from community_brain.ingestion.parser import TranscriptSegment
    # Build a long body — each paragraph roughly 30 tokens, 40 paragraphs
    big_body = "\n\n".join(
        f"[00:{i:02d}:00] Speaker: " + "word " * 25 for i in range(40)
    )
    seg = TranscriptSegment(
        topic="long topic",
        speakers=["Speaker"],
        keywords=["k1", "k2"],
        summary="a long segment",
        body=big_body,
    )
    chunks = chunk_prepared_transcript(
        [seg], "2026-03-10", "2026-03-10", "t", "t", segment_max_tokens=200,
    )
    # Should produce multiple sub-chunks
    assert len(chunks) > 1
    # All share the same segment header as embed_text
    embed_texts = {c.embed_text for c in chunks}
    assert len(embed_texts) == 1
    # Chunk IDs are sequential
    assert chunks[0].chunk_id == "2026-03-10:transcript:001"
    assert chunks[1].chunk_id == "2026-03-10:transcript:002"
    # total_chunks_in_source reflects the post-split count
    assert all(c.total_chunks_in_source == len(chunks) for c in chunks)


def test_chunk_extracted_signal_one_chunk_per_section() -> None:
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)
    chunks = chunk_extracted_signal(
        sections,
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        source_file="output/2026-03-10/extracted-signal.md",
    )

    # Fixture has tools, qa, insights, links
    assert len(chunks) == 4
    slugs = sorted(c.chunk_id.split(":")[-1] for c in chunks)
    assert slugs == ["insights", "links", "qa", "tools"]


def test_chunk_extracted_signal_topic_label_matches_slug() -> None:
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)
    chunks = chunk_extracted_signal(sections, "2026-03-10", "2026-03-10", "t", "t")

    for chunk in chunks:
        slug = chunk.chunk_id.split(":")[-1]
        assert chunk.topic_label == slug
        assert chunk.content_type == "extracted_signal"


def test_chunk_extracted_signal_embed_text_equals_full_text() -> None:
    """Per dual-field rule: signal chunks embed and return the same text."""
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)
    chunks = chunk_extracted_signal(sections, "2026-03-10", "2026-03-10", "t", "t")
    for chunk in chunks:
        assert chunk.embed_text == chunk.full_text


def test_chunk_extracted_signal_speakers_spoke_is_none() -> None:
    """Signal chunks don't have a speaker (they're LLM-synthesized summaries)."""
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)
    chunks = chunk_extracted_signal(sections, "2026-03-10", "2026-03-10", "t", "t")
    for chunk in chunks:
        assert chunk.speakers_spoke is None


def test_chunk_community_post_single_chunk_whole_doc() -> None:
    text = (FIXTURES / "community-post-sample.md").read_text(encoding="utf-8")
    post = parse_community_post(text)
    chunks = chunk_community_post(
        post,
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        source_file="output/2026-03-10/community-post.md",
        post_max_tokens=2500,
    )
    assert len(chunks) == 1
    assert chunks[0].chunk_id == "2026-03-10:post:main"
    assert chunks[0].topic_label == "session_narrative"
    assert chunks[0].embed_text == chunks[0].full_text
    assert chunks[0].full_text == text


def test_chunk_community_post_sliding_window_for_oversize() -> None:
    """A community post over post_max_tokens gets sliding-window split."""
    from community_brain.ingestion.parser import CommunityPost
    from community_brain.chunk_utils import count_tokens

    body = "\n\n".join(f"Paragraph {i}: " + "word " * 30 for i in range(60))
    post = CommunityPost(body=body, token_count=count_tokens(body))

    chunks = chunk_community_post(
        post,
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        source_file="x.md",
        post_max_tokens=500,
    )
    assert len(chunks) > 1
    assert chunks[0].chunk_id == "2026-03-10:post:001"
    assert all(c.topic_label == "session_narrative" for c in chunks)
    # Indexed, not :main
    assert ":main" not in chunks[0].chunk_id


def test_chunk_prepared_transcript_schema_version_and_defaults() -> None:
    """Every Chunk carries schema_version 1.0 and defaults for LLM-derived fields."""
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)
    chunks = chunk_prepared_transcript(
        segments, "2026-03-10", "2026-03-10", "t", "t", 1500,
    )
    c = chunks[0]
    assert c.schema_version == "1.0"
    # LLM-derived fields are defaulted — extractor fills later
    assert c.entities == []
    assert c.speech_acts == []
    assert c.stance is None
    assert c.certainty == "asserted"
    assert c.chunk_local_markers == []
    assert c.corpus_derived_markers == []
    assert c.corpus_markers_computed_at is None
    assert c.session_themes == []
    # Provenance fields are placeholders — pipeline fills later
    assert c.extraction_model == ""
    assert c.extraction_prompt_version == ""
    assert c.extraction_status == "success"
    # embedding is empty until the embedding stage
    assert c.embedding == []

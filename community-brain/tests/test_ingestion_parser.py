"""Tests for the three artifact parsers."""

from __future__ import annotations

from pathlib import Path

import pytest

from community_brain.ingestion.parser import (
    TranscriptSegment,
    CommunityPost,
    parse_prepared_transcript,
    parse_extracted_signal,
    parse_community_post,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_prepared_transcript_yields_segments() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)

    assert len(segments) == 2
    assert isinstance(segments[0], TranscriptSegment)


def test_prepared_transcript_first_segment_header() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)

    first = segments[0]
    assert first.topic == "agent orchestration tools"
    assert "Alex Rojas" in first.speakers
    assert "Sam" in first.speakers
    assert "LangChain" in first.keywords
    assert "LangGraph" in first.keywords
    assert first.summary.startswith("Alex and Sam compare")


def test_prepared_transcript_segment_body_preserves_tags() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)

    first_body = segments[0].body
    assert "[tool:LangGraph]" in first_body
    assert "<Q>" in first_body
    assert "<A>" in first_body
    assert "\u25b6" in first_body  # the ▶ insight marker


def test_prepared_transcript_empty_input() -> None:
    assert parse_prepared_transcript("") == []


def test_prepared_transcript_tolerates_unresolved_speakers_block() -> None:
    text = """=== SESSION ===
date: 2026-04-01
===

<!--SEGMENT
topic: test
speakers: Unknown Person
keywords: test
summary: test segment
-->

[00:00:00] Unknown Person: something

=== UNRESOLVED SPEAKERS ===
- Unknown Person (appears 1 times, example: "something")
===
"""
    segments = parse_prepared_transcript(text)
    assert len(segments) == 1
    # Body should not include the unresolved-speakers trailer
    assert "=== UNRESOLVED SPEAKERS ===" not in segments[0].body


def test_parse_extracted_signal_yields_canonical_sections() -> None:
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)

    slugs = [s.slug for s in sections]
    assert "tools" in slugs
    assert "qa" in slugs
    assert "insights" in slugs
    assert "links" in slugs
    # 'general' and 'decisions' not present in fixture — should not appear
    assert "general" not in slugs
    assert "decisions" not in slugs


def test_extracted_signal_section_contains_body() -> None:
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)

    tools_section = next(s for s in sections if s.slug == "tools")
    assert "LangGraph" in tools_section.body


def test_extracted_signal_rejects_non_canonical_slug() -> None:
    text = """## Tooling

- Something
"""
    with pytest.raises(ValueError, match="non-canonical"):
        parse_extracted_signal(text)


def test_extracted_signal_empty_input() -> None:
    assert parse_extracted_signal("") == []


def test_extracted_signal_all_canonical_slugs_accepted() -> None:
    text = """## tools

- X

## qa

**Q:** a
**A:** b

## insights

- Y

## links

- https://example.com

## decisions

- Z

## general

- W
"""
    sections = parse_extracted_signal(text)
    slugs = [s.slug for s in sections]
    assert slugs == ["tools", "qa", "insights", "links", "decisions", "general"]


def test_parse_community_post_returns_whole_document() -> None:
    text = (FIXTURES / "community-post-sample.md").read_text(encoding="utf-8")
    post = parse_community_post(text)

    assert isinstance(post, CommunityPost)
    assert post.body == text
    assert post.token_count > 0


def test_parse_community_post_empty() -> None:
    post = parse_community_post("")
    assert post.body == ""
    assert post.token_count == 0

"""Tests for bm25_text synthesis."""
from __future__ import annotations

from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text


def test_synthesize_includes_all_fields():
    result = synthesize_bm25_text(
        topic_label="Sales funnel discussion",
        entities=["Adam James", "Gold Flamingo"],
        speakers_spoke=["Brandon Hancock"],
        speakers_mentioned=["Andrej Karpathy"],
        keywords=["LinkedIn", "outreach"],
        full_text="01:23:45 - Brandon Hancock\nAdam, what's next for the funnel?",
    )
    assert "Sales funnel discussion" in result
    assert "Adam James" in result
    assert "Gold Flamingo" in result
    assert "Brandon Hancock" in result
    assert "Andrej Karpathy" in result
    assert "LinkedIn" in result
    assert "outreach" in result
    assert "Adam, what's next for the funnel?" in result


def test_synthesize_handles_empty_lists():
    result = synthesize_bm25_text(
        topic_label="Generic topic",
        entities=[],
        speakers_spoke=[],
        speakers_mentioned=[],
        keywords=[],
        full_text="some content",
    )
    # No crash; full_text and topic_label preserved.
    assert "Generic topic" in result
    assert "some content" in result


def test_synthesize_handles_none_lists_as_empty():
    result = synthesize_bm25_text(
        topic_label="Some topic",
        entities=None,
        speakers_spoke=None,
        speakers_mentioned=None,
        keywords=None,
        full_text="content",
    )
    assert "Some topic" in result
    assert "content" in result


def test_synthesize_handles_none_topic_label():
    result = synthesize_bm25_text(
        topic_label=None,
        entities=["X"],
        speakers_spoke=[],
        speakers_mentioned=[],
        keywords=[],
        full_text="text",
    )
    assert "X" in result
    assert "text" in result


def test_synthesize_separates_with_newlines():
    result = synthesize_bm25_text(
        topic_label="topic",
        entities=["e1", "e2"],
        speakers_spoke=["s1"],
        speakers_mentioned=[],
        keywords=["k1"],
        full_text="body",
    )
    # Each section on its own line; entities and keywords joined within their line by ", ".
    lines = result.split("\n")
    assert "topic" in lines
    assert "e1, e2" in lines
    assert "s1" in lines
    assert "k1" in lines
    assert "body" in lines

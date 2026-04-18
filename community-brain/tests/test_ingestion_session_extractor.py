"""Tests for Stage B session-level theme extraction and deterministic input selection."""

from __future__ import annotations

import json
from unittest.mock import patch

from community_brain.ingestion.parser import (
    TranscriptSegment,
    CommunityPost,
    SignalSection,
)
from community_brain.ingestion.session_extractor import (
    SessionThemesResult,
    select_session_input,
    extract_session_themes,
)


def test_select_session_input_prefers_community_post_when_small() -> None:
    post = CommunityPost(body="short post", token_count=100)
    segments = [
        TranscriptSegment(topic="x", speakers=[], keywords=[], summary="s", body="body")
    ]
    sections = [SignalSection(slug="tools", body="## tools\n- X")]

    source, text = select_session_input(
        community_post=post,
        transcript_segments=segments,
        signal_sections=sections,
        max_tokens=3000,
    )
    assert source == "community_post"
    assert text == "short post"


def test_select_session_input_falls_back_to_segment_headers_when_post_too_large() -> None:
    post = CommunityPost(body="huge post", token_count=5000)
    segments = [
        TranscriptSegment(topic="t1", speakers=["A"], keywords=["k1"], summary="s1", body="b"),
        TranscriptSegment(topic="t2", speakers=["B"], keywords=["k2"], summary="s2", body="b"),
    ]
    sections: list[SignalSection] = []

    source, text = select_session_input(
        community_post=post,
        transcript_segments=segments,
        signal_sections=sections,
        max_tokens=3000,
    )
    assert source == "transcript_headers"
    assert "t1" in text
    assert "t2" in text
    assert "s1" in text


def test_select_session_input_falls_back_to_signal_when_no_post_no_segments() -> None:
    sections = [SignalSection(slug="tools", body="## tools\n- X")]
    source, text = select_session_input(
        community_post=None,
        transcript_segments=[],
        signal_sections=sections,
        max_tokens=3000,
    )
    assert source == "signal"
    assert "tools" in text


def test_select_session_input_returns_none_when_no_input_available() -> None:
    source, text = select_session_input(
        community_post=None,
        transcript_segments=[],
        signal_sections=[],
        max_tokens=3000,
    )
    assert source is None
    assert text == ""


def test_select_session_input_excludes_segment_bodies() -> None:
    """Concatenation uses topic/summary/keywords only — never the body."""
    segments = [
        TranscriptSegment(
            topic="topic-one",
            speakers=["A"],
            keywords=["k"],
            summary="summary-one",
            body="SECRET BODY CONTENT THAT MUST NOT LEAK",
        ),
    ]
    source, text = select_session_input(
        community_post=None,
        transcript_segments=segments,
        signal_sections=[],
        max_tokens=3000,
    )
    assert source == "transcript_headers"
    assert "topic-one" in text
    assert "summary-one" in text
    assert "SECRET BODY CONTENT" not in text


def test_extract_session_themes_success() -> None:
    payload = {"themes": ["agent frameworks", "production deployment", "model selection"]}
    with patch(
        "community_brain.ingestion.session_extractor._call_llm",
        return_value=json.dumps(payload),
    ):
        result = extract_session_themes(
            input_text="...session summary...",
            model="m",
            prompt_template="p",
        )
    assert isinstance(result, SessionThemesResult)
    assert result.themes == ["agent frameworks", "production deployment", "model selection"]
    assert result.status == "success"
    assert result.error is None


def test_extract_session_themes_empty_input_returns_skipped() -> None:
    """Empty input bypasses the LLM and returns status='skipped'."""
    result = extract_session_themes(input_text="", model="m", prompt_template="p")
    assert result.status == "skipped"
    assert result.themes == []


def test_extract_session_themes_invalid_json_returns_failed() -> None:
    with patch(
        "community_brain.ingestion.session_extractor._call_llm",
        return_value="garbage",
    ):
        result = extract_session_themes(input_text="x", model="m", prompt_template="p")
    assert result.status == "failed"
    assert result.themes == []
    assert "json" in (result.error or "").lower()


def test_extract_session_themes_llm_exception_returns_failed() -> None:
    def _raise(*_a, **_k):
        raise RuntimeError("rate limited")

    with patch("community_brain.ingestion.session_extractor._call_llm", side_effect=_raise):
        result = extract_session_themes(input_text="x", model="m", prompt_template="p")
    assert result.status == "failed"
    assert result.themes == []
    assert "rate limited" in (result.error or "")


def test_extract_session_themes_strips_markdown_fence() -> None:
    fenced = '```json\n{"themes": ["a", "b", "c"]}\n```'
    with patch("community_brain.ingestion.session_extractor._call_llm", return_value=fenced):
        result = extract_session_themes(input_text="x", model="m", prompt_template="p")
    assert result.status == "success"
    assert result.themes == ["a", "b", "c"]


def test_extract_session_themes_missing_themes_field_returns_empty() -> None:
    """LLM returns JSON but with no 'themes' key — treat as empty success, not failure."""
    with patch(
        "community_brain.ingestion.session_extractor._call_llm",
        return_value='{"other_field": "x"}',
    ):
        result = extract_session_themes(input_text="x", model="m", prompt_template="p")
    assert result.status == "success"
    assert result.themes == []


def test_extract_session_themes_prompt_includes_input() -> None:
    """The prompt sent to the LLM includes the session_input."""
    captured: dict[str, str] = {}

    def _capture(model: str, prompt: str) -> str:
        captured["prompt"] = prompt
        return json.dumps({"themes": ["x"]})

    with patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=_capture,
    ):
        extract_session_themes(
            input_text="distinctive input marker",
            model="test-m",
            prompt_template="PROMPT TEMPLATE",
        )

    assert "PROMPT TEMPLATE" in captured["prompt"]
    assert "distinctive input marker" in captured["prompt"]

"""Tests for v4 filter rendering."""
from __future__ import annotations


def _make_chunk(
    *,
    chunk_id: str = "test:c0",
    session_date: str = "2026-02-25",
    session_title: str = "Test session",
    full_text: str = "[12:00:00] Speaker: hello",
    speakers_spoke: list[str] | None = None,
    speakers_mentioned: list[str] | None = None,
    topic_label: str = "test topic",
    has_question: bool = False,
    has_unresolved_question: bool = False,
    has_insight: bool = False,
    references_prior: bool = False,
) -> dict:
    return {
        "chunk_id": chunk_id,
        "ground_truth": {
            "chunk_id": chunk_id,
            "session_id": session_date,
            "session_date": session_date,
            "session_title": session_title,
            "full_text": full_text,
        },
        "derived_metadata": {
            "speakers_spoke": speakers_spoke or [],
            "speakers_mentioned": speakers_mentioned or [],
            "topic_label": topic_label,
            "has_question": has_question,
            "has_unresolved_question": has_unresolved_question,
            "has_insight": has_insight,
            "references_prior": references_prior,
        },
    }


def test_render_chunk_includes_source_n_header():
    from community_brain.openwebui.community_brain_filter import _render_chunk
    chunk = _make_chunk(
        chunk_id="2026-02-25:transcript:008",
        session_title="AI Developer Accelerator Coaching Call",
        full_text="[12:34:56] Patrick: hello world",
        speakers_spoke=["Patrick Chouinard", "Brandon Hancock"],
        speakers_mentioned=["Adam James"],
        topic_label="AI agent security",
        has_question=True,
        has_insight=True,
    )
    rendered = _render_chunk(chunk, source_index=3)
    assert "[SOURCE 3 — chunk_id: 2026-02-25:transcript:008]" in rendered
    assert "[session: 2026-02-25 — AI Developer Accelerator Coaching Call]" in rendered
    assert "[speakers spoke: Patrick Chouinard, Brandon Hancock]" in rendered
    assert "[speakers mentioned: Adam James]" in rendered
    assert "[topic: AI agent security]" in rendered
    # Existing flag rendering retained — exact phrasing depends on _flag_tags_for_chunk.
    # Just verify the marker is present:
    assert "flags:" in rendered
    assert "<transcript_data>" in rendered
    assert "</transcript_data>" in rendered


def test_render_chunk_empty_speakers_renders_none():
    from community_brain.openwebui.community_brain_filter import _render_chunk
    chunk = _make_chunk(speakers_spoke=[], speakers_mentioned=[])
    rendered = _render_chunk(chunk, source_index=1)
    assert "[speakers spoke: <none>]" in rendered
    assert "[speakers mentioned: <none>]" in rendered


def test_render_chunk_position_contract_metadata_outside_transcript():
    """All [tag: ...] lines must appear BEFORE <transcript_data> opens."""
    from community_brain.openwebui.community_brain_filter import _render_chunk
    chunk = _make_chunk(speakers_spoke=["X"], speakers_mentioned=[])
    rendered = _render_chunk(chunk, source_index=1)
    transcript_open_idx = rendered.index("<transcript_data>")
    for tag in ("[SOURCE 1", "[session:", "[speakers spoke:", "[speakers mentioned:", "[topic:"):
        assert rendered.index(tag) < transcript_open_idx, f"{tag} should be before <transcript_data>"

"""Stage B: session-level theme extraction.

Runs ONCE per session (not per chunk). Produces `session_themes`, a list of
3-5 high-level themes that get denormalized onto every chunk of the session.

Deterministic input priority (spec §5.3):

  1. community_post if present AND within max_tokens
  2. ELSE concatenation of transcript segment headers
     (topic + summary + keywords; segment bodies excluded)
  3. ELSE extracted_signal full text
  4. ELSE skip Stage B (returns status="skipped", themes=[])

Same failure contract as Stage C: LLM or JSON errors return
SessionThemesResult(status="failed", error=...) rather than raising.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Literal

from community_brain.ingestion._llm_parse import strip_code_fence
from community_brain.ingestion.parser import (
    CommunityPost,
    SignalSection,
    TranscriptSegment,
)
from community_brain.llm import call_llm

logger = logging.getLogger(__name__)

InputSource = Literal["community_post", "transcript_headers", "signal"]
_Status = Literal["success", "failed", "skipped"]


@dataclass
class SessionThemesResult:
    """Parsed output of Stage B session-level extraction."""
    themes: list[str]
    status: _Status
    error: str | None = None


def _call_llm(model: str, prompt: str) -> str:
    """Indirection for testing. Wraps the OpenRouter client."""
    return call_llm(prompt=prompt, model=model)


def select_session_input(
    community_post: CommunityPost | None,
    transcript_segments: list[TranscriptSegment],
    signal_sections: list[SignalSection],
    max_tokens: int,
) -> tuple[InputSource | None, str]:
    """Pick the Stage B input per deterministic priority.

    Returns (source_name, text). source_name is None when no input is available
    (the caller should skip Stage B and proceed with empty session_themes).
    """
    if community_post is not None and community_post.token_count <= max_tokens:
        return "community_post", community_post.body

    if transcript_segments:
        parts = [
            f"topic: {s.topic}\nsummary: {s.summary}\nkeywords: {', '.join(s.keywords)}"
            for s in transcript_segments
        ]
        return "transcript_headers", "\n\n".join(parts)

    if signal_sections:
        return "signal", "\n\n".join(s.body for s in signal_sections)

    return None, ""


def extract_session_themes(
    input_text: str,
    model: str,
    prompt_template: str,
) -> SessionThemesResult:
    """Run Stage B extraction for one session.

    Args:
        input_text: The concatenated input chosen by select_session_input.
            Empty string bypasses the LLM and returns status="skipped".
        model: OpenRouter model identifier.
        prompt_template: The session-themes prompt (loaded from
            session-themes-v1.md).

    Returns:
        SessionThemesResult. status="skipped" for empty input,
        "success" on a parseable LLM response (even if themes list is empty),
        "failed" on any exception or parse error.
    """
    if not input_text:
        return SessionThemesResult(themes=[], status="skipped", error="no input")

    prompt = f"{prompt_template}\n\nSESSION_INPUT:\n{input_text}"

    try:
        raw = _call_llm(model=model, prompt=prompt)
    except Exception as exc:
        logger.warning("Stage B LLM failed: %s", exc)
        return SessionThemesResult(
            themes=[], status="failed", error=f"{type(exc).__name__}: {exc}"
        )

    cleaned = strip_code_fence(raw)

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        logger.warning("Invalid JSON from Stage B: %s (raw preview: %r)", exc, raw[:200])
        return SessionThemesResult(
            themes=[], status="failed", error=f"invalid JSON: {exc}"
        )

    if not isinstance(data, dict):
        return SessionThemesResult(
            themes=[], status="failed",
            error=f"expected JSON object, got {type(data).__name__}",
        )

    raw_themes = data.get("themes")
    themes: list[str] = []
    if isinstance(raw_themes, list):
        themes = [str(t) for t in raw_themes if isinstance(t, (str, int, float))]

    return SessionThemesResult(themes=themes, status="success", error=None)



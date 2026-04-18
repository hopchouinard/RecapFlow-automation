"""Stage C: per-chunk LLM metadata extraction.

Takes a chunk's full_text plus the current entity registry and speaker aliases,
calls the extraction LLM, parses JSON, and returns structured metadata.

Failures (network, invalid JSON) are returned as status="failed" with an error
message so the pipeline orchestrator can record `extraction_status="failed"` on
the chunk and continue with the rest of the session rather than aborting.

Markdown code fences around JSON (which some LLMs emit despite explicit "output
only JSON" instructions) are stripped before parsing.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Literal

from community_brain.ingestion._llm_parse import strip_code_fence
from community_brain.llm import call_llm

logger = logging.getLogger(__name__)

_ExtractionStatus = Literal["success", "failed"]

_VALID_STANCES = {"positive", "negative", "neutral", "mixed"}
_VALID_CERTAINTIES = {"asserted", "hedged", "speculative"}


@dataclass
class ExtractionResult:
    """Parsed output of Stage C extraction for a single chunk."""
    status: _ExtractionStatus
    entities: list[str]
    new_entities_seen: list[str]
    new_speakers_seen: list[str]
    speech_acts: list[str]
    stance: str | None
    certainty: str
    chunk_local_markers: list[str]
    decisions: list[str]
    action_items: list[str]
    external_refs: list[str]
    references_prior: bool
    error: str | None = None


def _call_llm(model: str, prompt: str) -> str:
    """Indirection for testing. Wraps the OpenRouter client call."""
    return call_llm(prompt=prompt, model=model)


def extract_chunk_metadata(
    chunk_text: str,
    entity_registry_names: list[str],
    speaker_alias_names: list[str],
    model: str,
    prompt_template: str,
) -> ExtractionResult:
    """Run Stage C extraction on one chunk.

    Args:
        chunk_text: The chunk's full_text (what the LLM analyzes).
        entity_registry_names: Canonical entity names currently in the registry.
            The LLM is told to resolve mentions to these names or flag unknowns.
        speaker_alias_names: Canonical speaker names currently in the registry.
            Unknown speaker attributions get flagged for review.
        model: OpenRouter model identifier, e.g. "google/gemini-3.1-flash-lite-preview".
        prompt_template: The extraction prompt (loaded from chunk-extraction-v1.md).
            Rendered before the context blocks below.

    Returns:
        ExtractionResult with status="success" and populated fields on success,
        or status="failed" with a populated error message on any failure mode.
    """
    prompt = (
        f"{prompt_template}\n\n"
        f"ENTITY_REGISTRY:\n{json.dumps(entity_registry_names)}\n\n"
        f"SPEAKER_ALIASES:\n{json.dumps(speaker_alias_names)}\n\n"
        f"CHUNK_TEXT:\n{chunk_text}\n"
    )

    try:
        raw = _call_llm(model=model, prompt=prompt)
    except Exception as exc:
        logger.warning("LLM call failed: %s", exc)
        return _failure(f"{type(exc).__name__}: {exc}")

    cleaned = strip_code_fence(raw)

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        logger.warning("Invalid JSON from LLM: %s (raw preview: %r)", exc, raw[:200])
        return _failure(f"invalid JSON from LLM: {exc}")

    if not isinstance(data, dict):
        return _failure(f"expected JSON object, got {type(data).__name__}")

    return ExtractionResult(
        status="success",
        entities=_as_str_list(data.get("entities")),
        new_entities_seen=_as_str_list(data.get("new_entities_seen")),
        new_speakers_seen=_as_str_list(data.get("new_speakers_seen")),
        speech_acts=_as_str_list(data.get("speech_acts")),
        stance=_coerce_stance(data.get("stance")),
        certainty=_coerce_certainty(data.get("certainty")),
        chunk_local_markers=_as_str_list(data.get("chunk_local_markers")),
        decisions=_as_str_list(data.get("decisions")),
        action_items=_as_str_list(data.get("action_items")),
        external_refs=_as_str_list(data.get("external_refs")),
        references_prior=bool(data.get("references_prior", False)),
        error=None,
    )


def _coerce_stance(value) -> str | None:
    """Validate stance against known Literal values; fall back to None with a warning."""
    if value is None:
        return None
    if isinstance(value, str) and value in _VALID_STANCES:
        return value
    logger.warning(
        "LLM returned invalid stance %r; defaulting to None (allowed: %s)",
        value, sorted(_VALID_STANCES),
    )
    return None


def _coerce_certainty(value) -> str:
    """Validate certainty against known Literal values; fall back to 'asserted' with a warning."""
    if isinstance(value, str) and value in _VALID_CERTAINTIES:
        return value
    logger.warning(
        "LLM returned invalid certainty %r; defaulting to 'asserted' (allowed: %s)",
        value, sorted(_VALID_CERTAINTIES),
    )
    return "asserted"


def _as_str_list(value) -> list[str]:
    """Coerce an LLM field to list[str], discarding non-string items defensively."""
    if value is None:
        return []
    if not isinstance(value, list):
        return []
    return [str(item) for item in value if isinstance(item, (str, int, float))]


def _failure(msg: str) -> ExtractionResult:
    """Construct a failed-extraction result with safe-default fields."""
    return ExtractionResult(
        status="failed",
        entities=[],
        new_entities_seen=[],
        new_speakers_seen=[],
        speech_acts=[],
        stance=None,
        certainty="asserted",
        chunk_local_markers=[],
        decisions=[],
        action_items=[],
        external_refs=[],
        references_prior=False,
        error=msg,
    )

"""Cue rules for hybrid retrieval v2 metadata-aware boosting.

A CueRule fires when ANY phrase in `cue_phrases` is found
(case-insensitive substring) in the question, AND the chunk satisfies
`target_predicate`. When it fires, `delta` is added to the chunk's RRF score.

Rules are hardcoded here in v2; the schema's flag/array universe is small
enough that YAML config would be premature. See spec §5 for the full design.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class CueRule:
    name: str
    cue_phrases: tuple[str, ...]
    target_predicate: Callable[[dict], bool]
    delta: float


def _has_unresolved_question(chunk: dict) -> bool:
    return chunk.get("has_unresolved_question") is True


def _has_decisions(chunk: dict) -> bool:
    decisions = chunk.get("decisions")
    return isinstance(decisions, list) and len(decisions) > 0


def _has_action_items(chunk: dict) -> bool:
    items = chunk.get("action_items")
    return isinstance(items, list) and len(items) > 0


def _has_insight(chunk: dict) -> bool:
    return chunk.get("has_insight") is True


def _references_prior(chunk: dict) -> bool:
    return chunk.get("references_prior") is True


def _has_question(chunk: dict) -> bool:
    return chunk.get("has_question") is True


CUE_RULES: tuple[CueRule, ...] = (
    CueRule(
        name="unresolved_questions",
        cue_phrases=(
            "unresolved",
            "open question",
            "not answered",
            "outstanding",
            "didn't get answered",
            "didn't get fully answered",
        ),
        target_predicate=_has_unresolved_question,
        delta=0.010,
    ),
    CueRule(
        name="decisions",
        cue_phrases=("decision", "decided", "resolved", "concluded"),
        target_predicate=_has_decisions,
        delta=0.008,
    ),
    CueRule(
        name="action_items",
        cue_phrases=(
            "action item",
            "commit",
            "commitment",
            "next step",
            "to-do",
            "todo",
            "homework",
        ),
        target_predicate=_has_action_items,
        delta=0.008,
    ),
    CueRule(
        name="insights",
        cue_phrases=("insight", "realization", "aha moment", "key takeaway"),
        target_predicate=_has_insight,
        delta=0.006,
    ),
    CueRule(
        name="referenced_prior",
        cue_phrases=("referenced", "prior call", "last week", "previously", "discussed before"),
        target_predicate=_references_prior,
        delta=0.006,
    ),
    CueRule(
        name="questions_general",
        cue_phrases=("question", "asked"),
        target_predicate=_has_question,
        delta=0.003,
    ),
)

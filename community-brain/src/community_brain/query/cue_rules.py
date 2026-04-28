"""Cue rules for hybrid retrieval v2 metadata-aware boosting.

A CueRule fires when ANY phrase in `cue_phrases` is found
(case-insensitive substring) in the question, AND the chunk satisfies
`target_predicate`. When it fires, `delta` is added to the chunk's RRF score.

Rules are hardcoded here in v2; the schema's flag/array universe is small
enough that YAML config would be premature. See spec §5 for the full design.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Callable


logger = logging.getLogger(__name__)


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


def cue_phrase_matches(question: str, phrases: tuple[str, ...]) -> bool:
    """Case-insensitive substring match: returns True if any phrase appears
    anywhere in `question` ignoring case.
    """
    q = question.lower()
    return any(p in q for p in phrases)


def apply_cue_boosts(
    question: str,
    candidates: list[dict],
    rules: tuple[CueRule, ...] = CUE_RULES,
) -> list[dict]:
    """Apply cue-driven additive boosts to candidate RRF scores.

    For each rule whose cue phrases match the question, scan the candidates;
    for each candidate satisfying the rule's target_predicate, add the
    rule's delta to the candidate's `_rrf_score`. Returns a new list of new
    dicts, sorted by boosted score descending.

    Rule exceptions are caught and logged at WARNING; the offending rule is
    skipped, other rules continue.

    Spec §5.4 (composition): multiple rules can fire on the same candidate;
    deltas accumulate without cap.
    """
    boosted = [dict(c) for c in candidates]

    for rule in rules:
        if not cue_phrase_matches(question, rule.cue_phrases):
            continue
        for chunk in boosted:
            try:
                if rule.target_predicate(chunk):
                    chunk["_rrf_score"] = chunk.get("_rrf_score", 0.0) + rule.delta
            except Exception as exc:
                logger.warning(
                    "cue rule %r predicate raised on chunk %r: %s; skipping rule for remaining candidates",
                    rule.name,
                    chunk.get("chunk_id", "<no-id>"),
                    exc,
                )
                # Don't continue applying this rule to other chunks once it
                # has demonstrated it raises — the predicate is buggy.
                break

    boosted.sort(key=lambda c: c.get("_rrf_score", 0.0), reverse=True)
    return boosted

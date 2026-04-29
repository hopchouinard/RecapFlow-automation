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
from pathlib import Path
from typing import Any, Callable

import yaml


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


def _build_predicate(spec: dict[str, Any]):
    """Translate a YAML target_predicate dict to a callable predicate.

    Supported shapes:
      - {field: NAME, value: VAL}                  -> chunk[NAME] == VAL
      - {field: NAME, check: non_empty}            -> chunk[NAME] is non-empty list/string
      - {field: NAME, check: contains, value: STR} -> STR in chunk[NAME] (list or string)
    """
    field = spec.get("field")
    if not field:
        raise ValueError("target_predicate missing 'field'")
    if "value" in spec and "check" not in spec:
        expected = spec["value"]
        return lambda chunk, _f=field, _v=expected: chunk.get(_f) == _v
    check = spec.get("check")
    if check == "non_empty":
        def pred(chunk, _f=field):
            v = chunk.get(_f)
            return isinstance(v, (list, str)) and len(v) > 0
        return pred
    if check == "contains":
        needle = spec.get("value")
        if needle is None:
            raise ValueError("check: contains requires 'value'")
        def pred(chunk, _f=field, _n=needle):
            v = chunk.get(_f)
            if isinstance(v, list):
                return _n in v
            if isinstance(v, str):
                return _n in v
            return False
        return pred
    raise ValueError(f"unsupported target_predicate spec: {spec}")


def load_cue_rules_from_yaml(path: str | Path) -> tuple[CueRule, ...]:
    """Load cue rules from YAML.

    Returns empty tuple on missing file. Logs WARN.
    Skips individual malformed rules with ERROR; continues with the rest.
    """
    p = Path(path)
    if not p.exists():
        logger.warning("cue rules YAML not found: %s; using empty rule set", p)
        return ()
    try:
        data = yaml.safe_load(p.read_text())
    except Exception as exc:
        logger.error("failed to parse cue rules YAML at %s: %s", p, exc)
        return ()
    if not isinstance(data, dict) or "cue_rules" not in data:
        logger.error("cue rules YAML at %s missing top-level 'cue_rules' key", p)
        return ()
    rules: list[CueRule] = []
    for entry in data.get("cue_rules") or []:
        try:
            name = entry["name"]
            cue_phrases = tuple(entry["cue_phrases"])
            if len(cue_phrases) == 0:
                raise ValueError("cue_phrases is empty")
            predicate = _build_predicate(entry["target_predicate"])
            delta = float(entry["delta"])
            if delta < 0:
                raise ValueError("delta must be non-negative")
            rules.append(CueRule(
                name=name,
                cue_phrases=cue_phrases,
                target_predicate=predicate,
                delta=delta,
            ))
        except Exception as exc:
            logger.error(
                "skipping malformed cue rule %r: %s",
                entry.get("name", "<unnamed>") if isinstance(entry, dict) else "<not-a-dict>",
                exc,
            )
    return tuple(rules)

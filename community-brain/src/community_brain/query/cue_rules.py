"""Cue rules for hybrid retrieval v4 metadata-aware boosting.

Two rule shapes are supported:

1. **Legacy** (`cue_phrases` + `target_predicate`): rule fires when any
   phrase in `cue_phrases` is a case-insensitive substring of the question,
   AND the chunk satisfies `target_predicate`.

2. **v4** (`question_regex` + `match_strategy`): rule fires when
   `question_regex` matches the question, AND `apply_v4_strategy` returns
   True for the chunk under one of the strategies (`iso_date_equals`,
   `month_year_overlap`, `token_overlap`, `name_resolve_then_check`).

When a rule fires, `delta` is added to the chunk's RRF score. Rules load
from `config/query-cues.yaml` at call time and are merged with an
in-memory speaker auto-rule synthesized from `config/speaker-aliases.yaml`.
See spec docs/superpowers/specs/2026-05-03-retrieval-v4-quality-improvements-design.md §5.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import yaml


logger = logging.getLogger(__name__)

MONTH_NAMES: tuple[str, ...] = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)
_MONTH_TO_NUM = {name: f"{i+1:02d}" for i, name in enumerate(MONTH_NAMES)}


def apply_v4_strategy(
    *,
    question: str,
    chunk: dict,
    question_regex: str,
    match_field: str,
    match_strategy: str,
) -> bool:
    """Evaluate a v4 cue rule's match strategy.

    Returns True if the rule should fire for this (question, chunk) pair.
    Unknown strategies log a WARNING and return False (defensive — no raises).
    """
    try:
        m = re.search(question_regex, question, flags=re.IGNORECASE)
    except re.error as exc:
        logger.warning("cue rule regex %r failed to compile: %s", question_regex, exc)
        return False
    if not m:
        return False

    if match_strategy == "iso_date_equals":
        captured = m.group(1) if m.lastindex else m.group(0)
        return chunk.get(match_field) == captured

    if match_strategy == "month_year_overlap":
        # Capture groups: 1 = month name, 2 = year
        if not m.lastindex or m.lastindex < 2:
            return False
        month_name = m.group(1)
        year = m.group(2)
        # Normalize: "march" -> "March"
        month_name_norm = month_name.capitalize()
        if month_name_norm not in _MONTH_TO_NUM:
            return False
        target_prefix = f"{year}-{_MONTH_TO_NUM[month_name_norm]}"
        session_date = chunk.get(match_field, "")
        return isinstance(session_date, str) and session_date.startswith(target_prefix)

    if match_strategy == "token_overlap":
        # Captures get joined with "-" and checked against tokens in match_field.
        # E.g., "Q1 2026" -> "Q1-2026" expected as a token in bm25_text.
        # Comparison is case-insensitive: the question_regex runs with
        # IGNORECASE, so captures may be lowercase/mixed; bm25_text tokens are
        # stored at canonical casing ("Q1-2026", "early-March-2026"). casefold
        # both sides so "q1 2026" still boosts a chunk with "Q1-2026".
        if not m.lastindex:
            return False
        captures = [m.group(i) for i in range(1, m.lastindex + 1) if m.group(i)]
        if not captures:
            return False
        token = "-".join(captures).casefold()
        field_value = chunk.get(match_field, "")
        if not isinstance(field_value, str):
            return False
        tokens = field_value.split()
        return any(token in t.casefold() for t in tokens)

    if match_strategy == "name_resolve_then_check":
        # Capture the matched name from the question. Regex runs IGNORECASE so
        # `captured` may be in any casing; resolver keys are stored at registry
        # casing. Look up via casefolded view so "adam james" resolves to the
        # same canonical as "Adam James" / "ADAM JAMES".
        captured = m.group(1) if m.lastindex else m.group(0)
        canonical = _SPEAKER_CASEFOLD_LOOKUP.get(captured.casefold())
        if canonical is None:
            return False
        # Check ONLY the field named in match_field (caller-controlled).
        # The auto-rule generator creates two rules — one per field —
        # so each rule applies its own delta to its own field.
        # field_values come from extraction at registry casing, so the
        # set-intersection here uses the registry-cased lookup.
        field_values = chunk.get(match_field) or []
        if not isinstance(field_values, list):
            return False
        all_names_for_canonical = {
            n for n, c in _SPEAKER_NAME_TO_CANONICAL.items() if c == canonical
        }
        return bool(set(field_values) & all_names_for_canonical)

    logger.warning("unknown cue match strategy: %r", match_strategy)
    return False


# ---------------------------------------------------------------------------
# Speaker auto-rule generation
# ---------------------------------------------------------------------------

# Module-level cache: name -> canonical (registry casing)
# Populated by build_speaker_auto_rule; read by name_resolve_then_check
_SPEAKER_NAME_TO_CANONICAL: dict[str, str] = {}

# Parallel index keyed by name.casefold() -> canonical (registry casing).
# Used by name_resolve_then_check so user queries in any casing
# ("adam james", "ADAM JAMES") resolve to the same canonical as the
# registry-cased entry.
_SPEAKER_CASEFOLD_LOOKUP: dict[str, str] = {}


def _load_speaker_aliases_yaml(path: Path) -> dict[str, list[str]]:
    """Returns {canonical_name: [aliases]} from speaker-aliases.yaml.

    Reads the production schema:

        aliases:
          <Canonical Name>:
            - <alias>
            - <alias>

    Returns an empty dict on missing/malformed files.
    """
    if not path.exists():
        logger.warning("speaker-aliases.yaml not found: %s", path)
        return {}
    try:
        data = yaml.safe_load(path.read_text())
    except Exception as exc:
        logger.error("failed to parse speaker-aliases.yaml at %s: %s", path, exc)
        return {}
    raw = (data or {}).get("aliases") or {}
    out: dict[str, list[str]] = {}
    for canonical, aliases in raw.items():
        if isinstance(aliases, list):
            out[canonical] = list(aliases)
        else:
            out[canonical] = []
    return out


def _refresh_speaker_resolver(path: str | Path) -> dict[str, list[str]]:
    """Re-read speaker-aliases.yaml and refresh the name->canonical lookup.

    Called by retrieval_server on hot-reload of speaker-aliases.yaml.
    Returns the parsed aliases map so callers can reuse it without a second
    YAML parse.
    """
    global _SPEAKER_NAME_TO_CANONICAL, _SPEAKER_CASEFOLD_LOOKUP
    aliases_map = _load_speaker_aliases_yaml(Path(path))
    _SPEAKER_NAME_TO_CANONICAL = {}
    _SPEAKER_CASEFOLD_LOOKUP = {}
    for canonical, aliases in aliases_map.items():
        _SPEAKER_NAME_TO_CANONICAL[canonical] = canonical
        _SPEAKER_CASEFOLD_LOOKUP[canonical.casefold()] = canonical
        for alias in aliases:
            _SPEAKER_NAME_TO_CANONICAL[alias] = canonical
            _SPEAKER_CASEFOLD_LOOKUP[alias.casefold()] = canonical
    return aliases_map


def build_speaker_auto_rule(path: str | Path) -> tuple["CueRule", "CueRule"]:
    """Synthesize the speaker auto-rules from the alias registry.

    Builds a regex with all canonical names and aliases, longest-first so
    multi-word names match before single-word alternatives.

    Returns a tuple of TWO rules sharing the same regex:
      - 'speaker_auto_spoke' (match_field=speakers_spoke, delta=0.04)
      - 'speaker_auto_mentioned' (match_field=speakers_mentioned, delta=0.02)

    Both use match_strategy='name_resolve_then_check' which respects the
    match_field -- only checks that one field for the canonical's group.
    """
    aliases_map = _refresh_speaker_resolver(path)

    # Collect ALL names (canonicals + aliases)
    name_to_canonical: dict[str, str] = {}
    for canonical, aliases in aliases_map.items():
        name_to_canonical[canonical] = canonical
        for alias in aliases:
            name_to_canonical[alias] = canonical

    if not name_to_canonical:
        # Empty registry -- return two rules that never match.
        # Never-match sentinel for empty-registry case.
        never_match = r"(?!x)x"
        spoke = CueRule(
            name="speaker_auto_spoke", cue_phrases=(), target_predicate=None,
            delta=0.04, question_regex=never_match,
            match_field="speakers_spoke", match_strategy="name_resolve_then_check",
            recruit=True,
        )
        mentioned = CueRule(
            name="speaker_auto_mentioned", cue_phrases=(), target_predicate=None,
            delta=0.02, question_regex=never_match,
            match_field="speakers_mentioned", match_strategy="name_resolve_then_check",
            recruit=True,
        )
        return (spoke, mentioned)

    # Longest-first alternation; escape regex metacharacters.
    sorted_names = sorted(name_to_canonical.keys(), key=lambda n: -len(n))
    escaped = [re.escape(n) for n in sorted_names]
    pattern = r"\b(" + "|".join(escaped) + r")\b"

    spoke = CueRule(
        name="speaker_auto_spoke",
        cue_phrases=(),
        target_predicate=None,
        delta=0.04,
        question_regex=pattern,
        match_field="speakers_spoke",
        match_strategy="name_resolve_then_check",
        recruit=True,
    )
    mentioned = CueRule(
        name="speaker_auto_mentioned",
        cue_phrases=(),
        target_predicate=None,
        delta=0.02,
        question_regex=pattern,
        match_field="speakers_mentioned",
        match_strategy="name_resolve_then_check",
        recruit=True,
    )
    return (spoke, mentioned)


# Last-known-good cache keyed by resolved path string.
# On successful load, the result is stored here.
# On failure with a cached path, the cached result is returned (MEDIUM finding fix).
_LAST_GOOD_RULES: dict[str, tuple["CueRule", ...]] = {}


@dataclass(frozen=True)
class CueRule:
    name: str
    cue_phrases: tuple[str, ...]
    target_predicate: Callable[[dict], bool] | None
    delta: float
    # v4 additions (all optional for backward compat):
    question_regex: str | None = None
    match_field: str | None = None
    match_strategy: str | None = None
    # v5 additions (design D3): recruitment opt-in + the raw YAML
    # target_predicate mapping, preserved so candidate_injection can derive
    # a WHERE clause from the same definition the boost predicate uses.
    recruit: bool = False
    predicate_spec: dict | None = None


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

    Two rule shapes are supported:

    1. Legacy (cue_phrases + target_predicate): rule fires if any cue
       phrase is in the question; for each chunk passing
       target_predicate, add delta.

    2. v4 (question_regex + match_strategy): rule fires if regex matches
       question; for each chunk passing apply_v4_strategy with the
       rule's match_field, add delta.

    Rule exceptions are caught and logged at WARNING; the offending
    rule is skipped, other rules continue.
    """
    boosted = [dict(c) for c in candidates]

    for rule in rules:
        is_v4 = rule.question_regex is not None and rule.match_strategy is not None

        if is_v4:
            question_regex = rule.question_regex
            match_strategy = rule.match_strategy
            assert question_regex is not None and match_strategy is not None  # narrowed by is_v4
            try:
                if not re.search(question_regex, question, flags=re.IGNORECASE):
                    continue
            except re.error:
                logger.warning("v4 cue rule %r has invalid regex; skipping", rule.name)
                continue
            for chunk in boosted:
                try:
                    if apply_v4_strategy(
                        question=question,
                        chunk=chunk,
                        question_regex=question_regex,
                        match_field=rule.match_field or "",
                        match_strategy=match_strategy,
                    ):
                        chunk["_rrf_score"] = chunk.get("_rrf_score", 0.0) + rule.delta
                        chunk["_cue_delta"] = chunk.get("_cue_delta", 0.0) + rule.delta
                        chunk.setdefault("_cue_rules_fired", []).append(rule.name)
                except Exception as exc:
                    logger.warning(
                        "v4 cue rule %r raised on chunk %r: %s; skipping rule for remaining candidates",
                        rule.name, chunk.get("chunk_id", "<no-id>"), exc,
                    )
                    break
            continue

        # Legacy path
        if not cue_phrase_matches(question, rule.cue_phrases):
            continue
        for chunk in boosted:
            try:
                if rule.target_predicate is not None and rule.target_predicate(chunk):
                    chunk["_rrf_score"] = chunk.get("_rrf_score", 0.0) + rule.delta
                    chunk["_cue_delta"] = chunk.get("_cue_delta", 0.0) + rule.delta
                    chunk.setdefault("_cue_rules_fired", []).append(rule.name)
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
        def _pred_non_empty(chunk, _f=field):
            v = chunk.get(_f)
            return isinstance(v, (list, str)) and len(v) > 0
        return _pred_non_empty
    if check == "contains":
        needle = spec.get("value")
        if needle is None:
            raise ValueError("check: contains requires 'value'")
        def _pred_contains(chunk, _f=field, _n=needle):
            v = chunk.get(_f)
            if isinstance(v, list):
                return _n in v
            if isinstance(v, str):
                return _n in v
            return False
        return _pred_contains
    raise ValueError(f"unsupported target_predicate spec: {spec}")


def load_cue_rules_from_yaml(path: str | Path) -> tuple[CueRule, ...]:
    """Load cue rules from YAML.

    Returns empty tuple on first-time missing/malformed file (bootstrap path).
    For subsequent failures on a previously-cached path, returns the
    last-known-good rules and logs WARNING — protects /query from transient
    edit windows that produce malformed/partial YAML.

    Skips individual malformed rules with ERROR; continues with the rest.
    """
    p = Path(path)
    cache_key = str(p.resolve()) if p.exists() else str(p)

    def _fallback_or_empty(reason: str) -> tuple[CueRule, ...]:
        cached = _LAST_GOOD_RULES.get(cache_key)
        if cached is not None:
            logger.warning(
                "cue rules YAML load failed (%s); using last-known-good %d rules from cache",
                reason,
                len(cached),
            )
            return cached
        return ()

    if not p.exists():
        logger.warning("cue rules YAML not found: %s; using empty rule set", p)
        return _fallback_or_empty("file missing")
    try:
        data = yaml.safe_load(p.read_text())
    except Exception as exc:
        logger.error("failed to parse cue rules YAML at %s: %s", p, exc)
        return _fallback_or_empty(f"parse error: {exc}")
    if not isinstance(data, dict) or "cue_rules" not in data:
        logger.error("cue rules YAML at %s missing top-level 'cue_rules' key", p)
        return _fallback_or_empty("missing 'cue_rules' top-level key")
    rules: list[CueRule] = []
    for entry in data.get("cue_rules") or []:
        try:
            name = entry["name"]
            delta = float(entry["delta"])
            if delta < 0:
                raise ValueError("delta must be non-negative")

            # v4 path: question_regex + match_strategy (no cue_phrases / target_predicate)
            has_qr = "question_regex" in entry
            has_ms = "match_strategy" in entry
            if has_qr != has_ms:
                raise ValueError(
                    "v4 cue rule requires both 'question_regex' and 'match_strategy' "
                    "(got only one); see spec §5.2a"
                )
            if has_qr and has_ms:
                rules.append(CueRule(
                    name=name,
                    cue_phrases=(),
                    target_predicate=None,
                    delta=delta,
                    question_regex=entry["question_regex"],
                    match_field=entry.get("match_field"),
                    match_strategy=entry["match_strategy"],
                    recruit=bool(entry.get("recruit", False)),
                ))
                continue

            # Legacy path: cue_phrases + target_predicate
            raw_phrases = entry["cue_phrases"]
            if isinstance(raw_phrases, str):
                raise ValueError(
                    f"cue_phrases must be a list of strings, got bare string {raw_phrases!r} "
                    f"(common YAML mistake: write 'cue_phrases: [{raw_phrases}]' instead)"
                )
            if not isinstance(raw_phrases, (list, tuple)):
                raise ValueError(
                    f"cue_phrases must be a list, got {type(raw_phrases).__name__}"
                )
            if len(raw_phrases) == 0:
                raise ValueError("cue_phrases is empty")
            for phrase in raw_phrases:
                if not isinstance(phrase, str):
                    raise ValueError(
                        f"cue_phrases element must be a string, got "
                        f"{type(phrase).__name__}: {phrase!r}"
                    )
                if not phrase:
                    raise ValueError("cue_phrases element is empty string")
            cue_phrases = tuple(raw_phrases)
            predicate = _build_predicate(entry["target_predicate"])
            rules.append(CueRule(
                name=name,
                cue_phrases=cue_phrases,
                target_predicate=predicate,
                delta=delta,
                recruit=bool(entry.get("recruit", False)),
                predicate_spec=dict(entry["target_predicate"]),
            ))
        except Exception as exc:
            logger.error(
                "skipping malformed cue rule %r: %s",
                entry.get("name", "<unnamed>") if isinstance(entry, dict) else "<not-a-dict>",
                exc,
            )
    out = tuple(rules)
    if out:
        _LAST_GOOD_RULES[cache_key] = out
    return out

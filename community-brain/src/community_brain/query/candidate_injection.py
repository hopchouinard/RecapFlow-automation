"""Cue-driven candidate injection (v5).

Cue boosts re-rank the fixed candidate pool of top_k * OVERSAMPLE_FACTOR;
they cannot rescue chunks whose base hybrid relevance is too weak to enter
the pool (the v4 pool-limit finding). This module recruits candidates
directly: for each firing cue rule with recruit=True, it derives a targeted
LanceDB query from the rule's own match definition and merges the results
into the candidate pool BEFORE the boost pass prices them.

Design: Patchou-plan tasks/03 2026-07-01-community-brain-grounding-design.md
§D2-D7. Recruitment always ANDs the caller's WHERE (success guard + user
filters) so injection can never leak filtered-out or failed chunks.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

# Module import (not from-import): the speaker resolver dicts inside
# cue_rules are REBOUND by _refresh_speaker_resolver on every registry
# reload. A from-import would freeze a stale reference.
from community_brain.query import cue_rules as _cue_rules
from community_brain.query.cue_rules import CueRule, cue_phrase_matches

logger = logging.getLogger(__name__)

# Per-rule recruitment budget: how many chunks one firing rule may pull
# into the candidate pool.
INJECT_PER_RULE = 10

# Hard cap on total injected candidates per query, across all firing rules.
# Bounds worst-case pool growth and per-query latency.
MAX_INJECTED_TOTAL = 30


def _sql_quote(value: str) -> str:
    """SQL-standard single-quote doubling. Mirrors query_local.sql_quote;
    duplicated (one line) because query_local imports this module and the
    reverse import would be circular.
    """
    return value.replace("'", "''")


@dataclass(frozen=True)
class RecruitmentSpec:
    """A targeted recruitment query derived from one firing cue rule.

    where: LanceDB WHERE fragment selecting chunks the rule targets, or None.
    fts_text: override text for the FTS leg (token_overlap recruits by the
        date token itself — the question's other words are noise), or None
        to search with the original question.
    """
    rule_name: str
    where: str | None
    fts_text: str | None


def build_recruitment_query(rule: CueRule, question: str) -> RecruitmentSpec | None:
    """Derive a recruitment query for `rule` against `question`.

    Returns None when the rule is not recruit-enabled, does not fire on the
    question, or has no strategy with a derivable targeted predicate
    (legacy non_empty/contains checks stay boost-only — no portable
    LanceDB SQL for list-column membership).
    """
    if not rule.recruit:
        return None

    # v4 shape: question_regex + match_strategy
    if rule.question_regex is not None and rule.match_strategy is not None:
        try:
            m = re.search(rule.question_regex, question, flags=re.IGNORECASE)
        except re.error as exc:
            logger.warning(
                "recruitment: rule %r regex failed to compile: %s", rule.name, exc
            )
            return None
        if not m:
            return None

        if rule.match_strategy == "iso_date_equals":
            captured = m.group(1) if m.lastindex else m.group(0)
            return RecruitmentSpec(
                rule_name=rule.name,
                where=f"{rule.match_field} = '{_sql_quote(captured)}'",
                fts_text=None,
            )

        if rule.match_strategy == "month_year_overlap":
            if not m.lastindex or m.lastindex < 2:
                return None
            month_name = m.group(1).capitalize()
            year = m.group(2)
            month_num = _cue_rules._MONTH_TO_NUM.get(month_name)
            if month_num is None:
                return None
            prefix = f"{year}-{month_num}"
            return RecruitmentSpec(
                rule_name=rule.name,
                where=(
                    f"{rule.match_field} >= '{_sql_quote(prefix)}-01' "
                    f"AND {rule.match_field} <= '{_sql_quote(prefix)}-31'"
                ),
                fts_text=None,
            )

        if rule.match_strategy == "token_overlap":
            if not m.lastindex:
                return None
            captures = [m.group(i) for i in range(1, m.lastindex + 1) if m.group(i)]
            if not captures:
                return None
            token = "-".join(captures)
            # bm25_text token membership is exactly what the FTS index
            # answers; recruit by searching the token itself.
            return RecruitmentSpec(rule_name=rule.name, where=None, fts_text=token)

        if rule.match_strategy == "name_resolve_then_check":
            captured = m.group(1) if m.lastindex else m.group(0)
            canonical = _cue_rules._SPEAKER_CASEFOLD_LOOKUP.get(captured.casefold())
            if canonical is None:
                return None
            names = sorted(
                n
                for n, c in _cue_rules._SPEAKER_NAME_TO_CANONICAL.items()
                if c == canonical
            )
            if not names:
                return None
            clauses = " OR ".join(
                f"array_has({rule.match_field}, '{_sql_quote(n)}')" for n in names
            )
            return RecruitmentSpec(
                rule_name=rule.name, where=f"({clauses})", fts_text=None
            )

        logger.warning(
            "recruitment: unknown strategy %r on rule %r", rule.match_strategy, rule.name
        )
        return None

    # Legacy shape: cue_phrases + predicate_spec
    if not rule.cue_phrases or not cue_phrase_matches(question, rule.cue_phrases):
        return None
    spec = rule.predicate_spec
    if not spec or "field" not in spec:
        return None
    if "value" in spec and "check" not in spec:
        field_name = spec["field"]
        value = spec["value"]
        if isinstance(value, bool):
            return RecruitmentSpec(
                rule_name=rule.name,
                where=f"{field_name} = {'true' if value else 'false'}",
                fts_text=None,
            )
        if isinstance(value, str):
            return RecruitmentSpec(
                rule_name=rule.name,
                where=f"{field_name} = '{_sql_quote(value)}'",
                fts_text=None,
            )
    return None


def inject_candidates(
    *,
    question: str,
    table,
    rules: tuple[CueRule, ...],
    where_expr: str,
    existing_chunk_ids: set[str],
    query_vector: list[float],
) -> list[dict]:
    """Run recruitment for every firing recruit-enabled rule; return
    normalized rows not already in the pool.

    Every returned row carries:
      _rrf_score = 0.0            (no base hybrid signal; the downstream
                                   boost pass prices it via the rules)
      _distance / _vector_similarity  (cosine vs the query vector so the
                                   public `similarity` keeps spec §7.2
                                   semantics)
      _injected_by = [rule names that recruited it]

    Per-rule flow: FTS query (fts_text or the question) over bm25_text with
    (<rule where>) AND <where_expr>, limit INJECT_PER_RULE. If the FTS leg
    errors or finds nothing and the rule has a hard WHERE, fall back to a
    plain filtered scan — a quiet session may share zero lexical tokens
    with the question; that pathological case is this feature's reason to
    exist. Total injections are capped at MAX_INJECTED_TOTAL.
    """
    # Function-level import: query_local imports this module at module
    # level; importing back at module level would be circular.
    from community_brain.query.query_local import _cosine_distance

    injected: dict[str, dict] = {}
    for rule in rules:
        if len(injected) >= MAX_INJECTED_TOTAL:
            logger.warning(
                "recruitment: MAX_INJECTED_TOTAL=%d reached; remaining rules skipped",
                MAX_INJECTED_TOTAL,
            )
            break
        spec = build_recruitment_query(rule, question)
        if spec is None:
            continue
        combined_where = (
            f"({spec.where}) AND {where_expr}" if spec.where else where_expr
        )
        fts_query = spec.fts_text if spec.fts_text is not None else question
        rows: list[dict] = []
        try:
            rows = (
                table.search(fts_query, query_type="fts", fts_columns="bm25_text")
                .where(combined_where)
                .limit(INJECT_PER_RULE)
                .to_arrow()
                .to_pylist()
            )
        except Exception as exc:
            # Transient: recruitment is additive best-effort; the base
            # hybrid results are unaffected. Fall through to the scan path.
            logger.warning(
                "recruitment: FTS query for rule %r failed (%r); trying filtered scan",
                rule.name,
                exc,
            )
            rows = []
        if not rows and spec.where is not None:
            try:
                rows = (
                    table.search()
                    .where(combined_where)
                    .limit(INJECT_PER_RULE)
                    .to_arrow()
                    .to_pylist()
                )
            except Exception as exc:
                logger.warning(
                    "recruitment: filtered scan for rule %r failed (%r); skipping rule",
                    rule.name,
                    exc,
                )
                rows = []
        for row in rows:
            if len(injected) >= MAX_INJECTED_TOTAL:
                break
            chunk_id = row.get("chunk_id") or ""
            if not chunk_id or chunk_id in existing_chunk_ids:
                continue
            if chunk_id in injected:
                injected[chunk_id]["_injected_by"].append(rule.name)
                continue
            row["_rrf_score"] = 0.0
            embedding = row.get("embedding")
            if embedding:
                row["_distance"] = _cosine_distance(query_vector, list(embedding))
            else:
                row["_distance"] = 0.0
            row["_vector_similarity"] = 1.0 - float(row["_distance"])
            row["_injected_by"] = [rule.name]
            injected[chunk_id] = row
    return list(injected.values())

"""v5 cue-driven candidate injection: recruitment-query derivation (design D4)."""
from __future__ import annotations

from community_brain.query.candidate_injection import (
    RecruitmentSpec,
    build_recruitment_query,
)
from community_brain.query.cue_rules import CueRule, build_speaker_auto_rule

ISO_RULE = CueRule(
    name="date_iso_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
    match_field="session_date", match_strategy="iso_date_equals", recruit=True,
)

MONTH_RULE = CueRule(
    name="date_month_year_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
    match_field="session_date", match_strategy="month_year_overlap", recruit=True,
)

QUARTER_RULE = CueRule(
    name="date_quarter_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(Q[1-4])\s+(\d{4})\b",
    match_field="bm25_text", match_strategy="token_overlap", recruit=True,
)

LEGACY_BOOL_RULE = CueRule(
    name="unresolved_questions", cue_phrases=("unresolved",), target_predicate=None,
    delta=0.04, recruit=True,
    predicate_spec={"field": "has_unresolved_question", "value": True},
)

LEGACY_NON_EMPTY_RULE = CueRule(
    name="decisions", cue_phrases=("decision",), target_predicate=None,
    delta=0.008, recruit=True,
    predicate_spec={"field": "decisions", "check": "non_empty"},
)

ALIASES_YAML = """
aliases:
  Adam James:
    - Adam
"""


def test_non_recruit_rule_returns_none():
    rule = CueRule(
        name="x", cue_phrases=(), target_predicate=None, delta=0.04,
        question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
        match_field="session_date", match_strategy="iso_date_equals", recruit=False,
    )
    assert build_recruitment_query(rule, "what happened on 2025-12-30?") is None


def test_iso_date_rule_derives_equality_where():
    spec = build_recruitment_query(ISO_RULE, "What was discussed on 2025-12-30?")
    assert spec == RecruitmentSpec(
        rule_name="date_iso_match",
        where="session_date = '2025-12-30'",
        fts_text=None,
    )


def test_iso_date_rule_none_when_question_has_no_date():
    assert build_recruitment_query(ISO_RULE, "What did Adam say?") is None


def test_month_year_rule_derives_range_where():
    spec = build_recruitment_query(MONTH_RULE, "What happened in December 2025?")
    assert spec is not None
    assert spec.where == (
        "session_date >= '2025-12-01' AND session_date <= '2025-12-31'"
    )
    assert spec.fts_text is None


def test_token_overlap_rule_recruits_via_fts_token():
    spec = build_recruitment_query(QUARTER_RULE, "themes in Q1 2026 calls?")
    assert spec is not None
    assert spec.where is None
    assert spec.fts_text == "Q1-2026"


def test_speaker_rule_derives_array_has_where(tmp_path):
    p = tmp_path / "speaker-aliases.yaml"
    p.write_text(ALIASES_YAML)
    spoke, _mentioned = build_speaker_auto_rule(p)
    spec = build_recruitment_query(spoke, "What did Adam say about pricing?")
    assert spec is not None
    assert spec.where == (
        "(array_has(speakers_spoke, 'Adam') OR array_has(speakers_spoke, 'Adam James'))"
    )


def test_legacy_bool_predicate_derives_equality_where():
    spec = build_recruitment_query(LEGACY_BOOL_RULE, "what stayed unresolved?")
    assert spec is not None
    assert spec.where == "has_unresolved_question = true"
    assert spec.fts_text is None


def test_legacy_bool_rule_none_when_no_phrase_match():
    assert build_recruitment_query(LEGACY_BOOL_RULE, "what was decided?") is None


def test_legacy_non_empty_predicate_is_not_recruitable():
    assert build_recruitment_query(LEGACY_NON_EMPTY_RULE, "what decisions happened?") is None


def test_where_values_are_sql_quoted():
    rule = CueRule(
        name="q", cue_phrases=("about",), target_predicate=None, delta=0.01,
        recruit=True, predicate_spec={"field": "stance", "value": "o'brien"},
    )
    spec = build_recruitment_query(rule, "tell me about stances")
    assert spec is not None
    assert spec.where == "stance = 'o''brien'"

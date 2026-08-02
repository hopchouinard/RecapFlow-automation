"""Day-precision matching for phrased dates (2026-08-02).

`date_phrased_with_day` was a v4 hotpatch that reused `month_year_overlap`,
deliberately not capturing the day -- its own comment says the captures
"(month, year) can flow through month_year_overlap unchanged". So a rule with
"with_day" in its name had MONTH precision.

Measured live against the deployed server: asking

    "What did the community discuss in the coaching call from March 4th, 2026?"

injected 10 candidates from 2026-03-17, 2026-03-24 and 2026-03-31 and NEVER
2026-03-04, which is in the corpus. The ISO phrasing of the same date
recruited 2026-03-04 correctly. That is why the phrased-date-with-day eval
probe sat at target_recall 0.0 in every run of every block, and it was
misattributed to a corpus gap (FU-19) rather than to retrieval.
"""
from __future__ import annotations

import pytest

from community_brain.query.cue_rules import apply_v4_strategy

PHRASED_REGEX = (
    r"\b(January|February|March|April|May|June|July|August|September|"
    r"October|November|December)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b"
)

QUESTION = "What did the community discuss in the coaching call from March 4th, 2026?"


def _fires(question, session_date, regex=PHRASED_REGEX,
           strategy="phrased_date_equals"):
    return apply_v4_strategy(
        question=question,
        chunk={"session_date": session_date},
        question_regex=regex,
        match_field="session_date",
        match_strategy=strategy,
    )


class TestPhrasedDateEquals:
    def test_matches_the_named_day(self):
        assert _fires(QUESTION, "2026-03-04") is True

    @pytest.mark.parametrize("other", ["2026-03-10", "2026-03-17",
                                       "2026-03-24", "2026-03-31"])
    def test_does_not_match_other_days_in_the_same_month(self, other):
        """The exact failure observed live: same month, wrong day, recruited."""
        assert _fires(QUESTION, other) is False

    def test_does_not_match_the_same_day_in_another_month_or_year(self):
        assert _fires(QUESTION, "2026-04-04") is False
        assert _fires(QUESTION, "2025-03-04") is False

    @pytest.mark.parametrize("phrasing", [
        "What was covered on March 4th, 2026?",
        "What was covered on March 4, 2026?",
        "What was covered on march 4TH 2026?",
        "What was covered on March 04, 2026?",
    ])
    def test_accepts_ordinal_comma_case_and_zero_padding_variants(self, phrasing):
        assert _fires(phrasing, "2026-03-04") is True

    def test_single_digit_day_is_zero_padded_not_string_matched(self):
        """"March 4" must become 04, never a naive f-string "2026-03-4"."""
        assert _fires("Anything from March 4, 2026?", "2026-03-04") is True

    def test_no_date_in_question_does_not_fire(self):
        assert _fires("What did the community discuss?", "2026-03-04") is False

    def test_missing_capture_groups_return_false_not_raise(self):
        """Defensive: a rule wired to this strategy with a 2-group regex must
        fail closed rather than IndexError."""
        two_group = r"\b(January|February|March)\s+(\d{4})\b"
        assert _fires("March 2026?", "2026-03-04", regex=two_group) is False

    def test_non_string_session_date_returns_false(self):
        assert apply_v4_strategy(
            question=QUESTION,
            chunk={"session_date": None},
            question_regex=PHRASED_REGEX,
            match_field="session_date",
            match_strategy="phrased_date_equals",
        ) is False


class TestRecruitmentParity:
    """The boost path and the recruitment path must implement the SAME set of
    match strategies.

    cue_rules.apply_v4_strategy decides whether a rule FIRES (the score boost);
    candidate_injection.build_recruitment_query decides what it RECRUITS (the
    candidate pool). A strategy present in only one degrades silently: the
    phrased-date fix was written into cue_rules first, and end-to-end
    verification came back "recruitment: unknown strategy 'phrased_date_equals'"
    with zero candidates injected -- a fix that unit-tested green and did
    nothing in production.
    """

    def test_phrased_date_equals_recruits_the_exact_day(self):
        from community_brain.query.candidate_injection import build_recruitment_query
        from community_brain.query.cue_rules import CueRule

        rule = CueRule(
            name="date_phrased_with_day",
            cue_phrases=(),
            target_predicate=None,
            delta=0.04,
            question_regex=PHRASED_REGEX,
            match_field="session_date",
            match_strategy="phrased_date_equals",
            recruit=True,
        )
        spec = build_recruitment_query(rule, QUESTION)
        assert spec is not None, "recruitment returned nothing for a firing rule"
        assert spec.where == "session_date = '2026-03-04'"
        assert spec.rule_name == "date_phrased_with_day"

    def test_every_configured_strategy_is_recruitable(self):
        """Every match_strategy used by a recruit:true rule in the shipped
        config must be implemented by the recruitment path.

        Tested per STRATEGY with a controlled regex, not per rule: several
        rules share a strategy with different regexes (date_relative_phrasing
        and date_quarter_match are both token_overlap), so one sample question
        cannot match them all. The invariant under test is strategy coverage.
        """
        import yaml
        from pathlib import Path
        from community_brain.query.candidate_injection import build_recruitment_query
        from community_brain.query.cue_rules import CueRule

        cfg = Path(__file__).resolve().parents[1] / "config" / "query-cues.yaml"
        rules = yaml.safe_load(cfg.read_text(encoding="utf-8"))["cue_rules"]

        # strategy -> (regex that exercises it, question that matches)
        probes = {
            "iso_date_equals": (r"\b(\d{4}-\d{2}-\d{2})\b",
                                "What happened on 2026-03-04?"),
            "phrased_date_equals": (PHRASED_REGEX,
                                    "What happened on March 4th, 2026?"),
            "month_year_overlap": (r"\b(January|February|March)\s+(\d{4})\b",
                                   "What happened in March 2026?"),
            "token_overlap": (r"\b(Q[1-4])\s+(\d{4})\b",
                              "What happened in Q1 2026?"),
        }

        used = {r.get("match_strategy") for r in rules
                if r.get("recruit") and r.get("question_regex")}
        used.discard(None)

        unknown = sorted(s for s in used if s not in probes)
        assert unknown == [], (
            f"recruit:true rules use strategies with no coverage probe here: "
            f"{unknown} — add one rather than deleting the assertion"
        )

        broken = []
        for strat in sorted(used):
            regex, question = probes[strat]
            rule = CueRule(
                name=f"probe_{strat}", cue_phrases=(), target_predicate=None,
                delta=0.04, question_regex=regex, match_field="session_date",
                match_strategy=strat, recruit=True,
            )
            if build_recruitment_query(rule, question) is None:
                broken.append(strat)
        assert broken == [], (
            f"strategies the recruitment path cannot handle: {broken}"
        )

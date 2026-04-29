"""Tests for cue rule definitions and the CueRule dataclass."""

from __future__ import annotations

from community_brain.query.cue_rules import CueRule, CUE_RULES


def test_cue_rule_is_immutable_dataclass():
    rule = CueRule(
        name="test",
        cue_phrases=("foo",),
        target_predicate=lambda chunk: True,
        delta=0.005,
    )
    assert rule.name == "test"
    assert rule.cue_phrases == ("foo",)
    assert rule.delta == 0.005
    # frozen=True must prevent mutation
    try:
        rule.name = "other"  # type: ignore[misc]
        raised = False
    except Exception:
        raised = True
    assert raised, "CueRule must be frozen"


def test_cue_rules_initial_set_has_six_rules():
    """Initial set per spec §5.2: six rules."""
    names = {r.name for r in CUE_RULES}
    assert names == {
        "unresolved_questions",
        "decisions",
        "action_items",
        "insights",
        "referenced_prior",
        "questions_general",
    }


def test_cue_rules_deltas_match_spec():
    """Spec §5.2 delta calibration."""
    by_name = {r.name: r for r in CUE_RULES}
    assert by_name["unresolved_questions"].delta == 0.010
    assert by_name["decisions"].delta == 0.008
    assert by_name["action_items"].delta == 0.008
    assert by_name["insights"].delta == 0.006
    assert by_name["referenced_prior"].delta == 0.006
    assert by_name["questions_general"].delta == 0.003


def test_unresolved_questions_predicate():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["unresolved_questions"]
    assert rule.target_predicate({"has_unresolved_question": True})
    assert not rule.target_predicate({"has_unresolved_question": False})
    assert not rule.target_predicate({"has_unresolved_question": None})
    assert not rule.target_predicate({})


def test_decisions_predicate_requires_non_empty_list():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["decisions"]
    assert rule.target_predicate({"decisions": ["decided to X"]})
    assert not rule.target_predicate({"decisions": []})
    assert not rule.target_predicate({"decisions": None})
    assert not rule.target_predicate({})


def test_action_items_predicate_requires_non_empty_list():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["action_items"]
    assert rule.target_predicate({"action_items": ["follow up with Adam"]})
    assert not rule.target_predicate({"action_items": []})
    assert not rule.target_predicate({"action_items": None})


def test_insights_predicate():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["insights"]
    assert rule.target_predicate({"has_insight": True})
    assert not rule.target_predicate({"has_insight": False})


def test_referenced_prior_predicate():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["referenced_prior"]
    assert rule.target_predicate({"references_prior": True})
    assert not rule.target_predicate({"references_prior": False})


def test_questions_general_predicate():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["questions_general"]
    assert rule.target_predicate({"has_question": True})
    assert not rule.target_predicate({"has_question": False})


def test_cue_phrases_are_lowercase():
    """Phrases must be lowercase so case-insensitive matching is one .lower() away."""
    for rule in CUE_RULES:
        for phrase in rule.cue_phrases:
            assert phrase == phrase.lower(), f"{rule.name!r} has non-lowercase phrase {phrase!r}"


import logging

from community_brain.query.cue_rules import (
    CueRule,
    CUE_RULES,
    apply_cue_boosts,
    cue_phrase_matches,
)


def test_cue_phrase_matches_case_insensitive():
    assert cue_phrase_matches("What UNRESOLVED questions remain?", ("unresolved",))
    assert cue_phrase_matches("decided to ship", ("decided",))
    assert not cue_phrase_matches("everything is great", ("unresolved",))


def test_cue_phrase_matches_substring_not_word_boundary():
    """Spec §5.1: case-insensitive substring (not word-boundary)."""
    # 'decision' substring matches 'decisions' too, by design
    assert cue_phrase_matches("we made decisions today", ("decision",))


def test_apply_cue_boosts_no_cue_match_no_change():
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.020, "has_unresolved_question": True},
        {"chunk_id": "b", "_rrf_score": 0.015, "has_unresolved_question": False},
    ]
    result = apply_cue_boosts("what was the weather like?", candidates)
    assert result[0]["_rrf_score"] == 0.020
    assert result[1]["_rrf_score"] == 0.015


def test_apply_cue_boosts_unresolved_question_cue_promotes_flagged_chunk():
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.018, "has_unresolved_question": False},
        {"chunk_id": "b", "_rrf_score": 0.015, "has_unresolved_question": True},
    ]
    result = apply_cue_boosts("what unresolved questions remain?", candidates)
    by_id = {c["chunk_id"]: c for c in result}
    assert by_id["a"]["_rrf_score"] == 0.018
    assert by_id["b"]["_rrf_score"] == 0.015 + 0.010


def test_apply_cue_boosts_returns_resorted_list():
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.018, "has_unresolved_question": False},
        {"chunk_id": "b", "_rrf_score": 0.015, "has_unresolved_question": True},
    ]
    result = apply_cue_boosts("what unresolved questions remain?", candidates)
    # b boosted to 0.025; should now rank first
    assert result[0]["chunk_id"] == "b"
    assert result[1]["chunk_id"] == "a"


def test_apply_cue_boosts_multiple_rules_compose_additively():
    """A chunk satisfying multiple flag predicates whose cues are all in the
    question accumulates all the deltas."""
    candidates = [
        {
            "chunk_id": "a",
            "_rrf_score": 0.010,
            "has_unresolved_question": True,
            "references_prior": True,
        },
    ]
    result = apply_cue_boosts(
        "what unresolved questions referenced prior calls?", candidates
    )
    # 0.010 + 0.010 (unresolved) + 0.006 (referenced_prior) = 0.026
    assert abs(result[0]["_rrf_score"] - 0.026) < 1e-9


def test_apply_cue_boosts_predicate_exception_logs_and_skips_rule(caplog):
    """A rule whose target_predicate raises must not crash the whole boost
    pass — it logs and is skipped, other rules continue."""
    bad_rule = CueRule(
        name="bad_rule",
        cue_phrases=("trigger",),
        target_predicate=lambda chunk: chunk["nonexistent_field"]["nested"],
        delta=0.005,
    )
    rules = (*CUE_RULES, bad_rule)
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.010, "has_unresolved_question": True},
    ]
    with caplog.at_level(logging.WARNING):
        result = apply_cue_boosts(
            "trigger unresolved", candidates, rules=rules
        )
    # unresolved cue still fires
    assert abs(result[0]["_rrf_score"] - 0.020) < 1e-9
    assert any("bad_rule" in rec.message for rec in caplog.records)


def test_apply_cue_boosts_does_not_mutate_input():
    """Defensive: apply_cue_boosts returns a new list of new dicts."""
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.010, "has_unresolved_question": True},
    ]
    original_score = candidates[0]["_rrf_score"]
    apply_cue_boosts("what unresolved questions remain?", candidates)
    assert candidates[0]["_rrf_score"] == original_score

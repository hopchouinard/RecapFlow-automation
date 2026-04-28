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

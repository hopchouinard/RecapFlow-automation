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


# ---------------------------------------------------------------------------
# YAML loader tests (T13)
# ---------------------------------------------------------------------------

import pytest  # noqa: E402 (below other imports is fine for test files)


def test_load_cue_rules_from_yaml(tmp_path):
    """The YAML loader produces CueRule instances with predicates that match
    the same shape as the legacy hardcoded set."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml

    yaml_text = """
cue_rules:
  - name: test_unresolved
    cue_phrases: [unresolved]
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010
  - name: test_decisions
    cue_phrases: [decision]
    target_predicate:
      field: decisions
      check: non_empty
    delta: 0.008
"""
    path = tmp_path / "cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert len(rules) == 2

    # boolean rule
    bool_rule = rules[0]
    assert bool_rule.name == "test_unresolved"
    assert bool_rule.target_predicate({"has_unresolved_question": True}) is True
    assert bool_rule.target_predicate({"has_unresolved_question": False}) is False

    # non_empty rule
    list_rule = rules[1]
    assert list_rule.target_predicate({"decisions": ["X"]}) is True
    assert list_rule.target_predicate({"decisions": []}) is False
    assert list_rule.target_predicate({"decisions": None}) is False


def test_load_cue_rules_missing_file_returns_empty(tmp_path):
    """Missing YAML file: loader returns empty tuple, logs WARN."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    rules = load_cue_rules_from_yaml(tmp_path / "missing.yaml")
    assert rules == ()


def test_load_cue_rules_malformed_yaml_returns_empty(tmp_path):
    """Unparseable YAML: loader returns empty tuple, logs ERROR."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "broken.yaml"
    path.write_text("[: invalid: yaml: -")
    rules = load_cue_rules_from_yaml(path)
    assert rules == ()


def test_load_cue_rules_missing_top_level_key_returns_empty(tmp_path):
    """YAML without 'cue_rules' top-level key: loader returns empty, logs ERROR."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "wrong.yaml"
    path.write_text("not_cue_rules: []")
    rules = load_cue_rules_from_yaml(path)
    assert rules == ()


def test_load_cue_rules_skips_malformed_rule_keeps_others(tmp_path):
    """A rule missing required keys is skipped; well-formed rules still load."""
    yaml_text = """
cue_rules:
  - name: bad
    cue_phrases: []
    target_predicate:
      field: missing_value_or_check
    delta: 0.01
  - name: good
    cue_phrases: [x]
    target_predicate:
      field: has_question
      value: true
    delta: 0.003
"""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert len(rules) == 1
    assert rules[0].name == "good"


def test_load_cue_rules_negative_delta_skipped(tmp_path):
    """A rule with negative delta is rejected; other rules load."""
    yaml_text = """
cue_rules:
  - name: bad_negative
    cue_phrases: [foo]
    target_predicate:
      field: has_question
      value: true
    delta: -0.01
  - name: good
    cue_phrases: [x]
    target_predicate:
      field: has_question
      value: true
    delta: 0.003
"""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert len(rules) == 1
    assert rules[0].name == "good"


def test_load_cue_rules_contains_predicate(tmp_path):
    """Predicate type 'contains' supported for list-or-string fields."""
    yaml_text = """
cue_rules:
  - name: entity_match
    cue_phrases: [foo]
    target_predicate:
      field: entities
      check: contains
      value: Adam
    delta: 0.005
"""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert len(rules) == 1
    rule = rules[0]
    assert rule.target_predicate({"entities": ["Adam", "Bob"]}) is True
    assert rule.target_predicate({"entities": ["Bob"]}) is False
    assert rule.target_predicate({"entities": "Adam Smith"}) is True  # string also supported


# ---------------------------------------------------------------------------
# Regression tests for Codex Phase 4 findings (HIGH + MEDIUM)
# ---------------------------------------------------------------------------

import pytest  # noqa: F811 (already imported above; harmless re-import in test files)


@pytest.fixture(autouse=False)
def clear_cue_rules_cache():
    """Clear the module-level last-known-good cache before and after each test
    that manipulates it, so tests don't bleed into each other."""
    from community_brain.query import cue_rules as _mod
    _mod._LAST_GOOD_RULES.clear()
    yield
    _mod._LAST_GOOD_RULES.clear()


def test_load_cue_rules_rejects_bare_string_cue_phrases(tmp_path, clear_cue_rules_cache):
    """Catastrophic-failure-mode regression: bare string for cue_phrases
    must NOT be accepted as a character-by-character cue list."""
    yaml_text = '''
cue_rules:
  - name: bad_bare_string
    cue_phrases: unresolved
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010
  - name: good
    cue_phrases: [unresolved]
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010
'''
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "bare_string_cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert len(rules) == 1
    assert rules[0].name == "good"


def test_load_cue_rules_rejects_non_string_cue_phrase_element(tmp_path, clear_cue_rules_cache):
    """Non-string elements in cue_phrases would cause TypeError in cue_phrase_matches."""
    yaml_text = '''
cue_rules:
  - name: bad_int
    cue_phrases: [123]
    target_predicate:
      field: has_question
      value: true
    delta: 0.010
'''
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "int_cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert rules == ()


def test_load_cue_rules_rejects_empty_string_cue_phrase(tmp_path, clear_cue_rules_cache):
    """Empty string is a substring of every question — would fire on every query."""
    yaml_text = '''
cue_rules:
  - name: bad_empty
    cue_phrases: [""]
    target_predicate:
      field: has_question
      value: true
    delta: 0.010
'''
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "empty_cue.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert rules == ()


def test_load_cue_rules_uses_last_known_good_on_subsequent_failure(tmp_path, clear_cue_rules_cache):
    """Successful load is cached; a subsequent failure on the same path
    returns the cached rules instead of empty (MEDIUM finding)."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml

    path = tmp_path / "transient_cues.yaml"
    path.write_text('''
cue_rules:
  - name: good
    cue_phrases: [unresolved]
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010
''')
    rules1 = load_cue_rules_from_yaml(path)
    assert len(rules1) == 1

    # Simulate partial write during in-place editor save
    path.write_text("[: invalid yaml")
    rules2 = load_cue_rules_from_yaml(path)
    # Cache rescues us
    assert len(rules2) == 1
    assert rules2[0].name == "good"


def test_load_cue_rules_empty_on_first_failure(tmp_path, clear_cue_rules_cache):
    """No cache yet → first-ever failure returns empty (bootstrap behavior)."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "never_existed_bootstrap.yaml"  # never written
    rules = load_cue_rules_from_yaml(path)
    assert rules == ()


def test_apply_cue_boosts_tracks_fired_rules_and_delta():
    """apply_cue_boosts now populates _cue_delta and _cue_rules_fired
    on each chunk it boosts."""
    rule_a = CueRule(
        name="ra",
        cue_phrases=("foo",),
        target_predicate=lambda c: c.get("flag_a") is True,
        delta=0.01,
    )
    rule_b = CueRule(
        name="rb",
        cue_phrases=("foo",),
        target_predicate=lambda c: c.get("flag_b") is True,
        delta=0.005,
    )
    candidates = [
        {"chunk_id": "c1", "_rrf_score": 0.05, "flag_a": True, "flag_b": True},
        {"chunk_id": "c2", "_rrf_score": 0.05, "flag_a": True, "flag_b": False},
        {"chunk_id": "c3", "_rrf_score": 0.05, "flag_a": False, "flag_b": False},
    ]
    boosted = apply_cue_boosts("foo bar", candidates, rules=(rule_a, rule_b))
    by_id = {c["chunk_id"]: c for c in boosted}
    # c1 fires both rules
    assert by_id["c1"]["_cue_delta"] == pytest.approx(0.015)
    assert sorted(by_id["c1"]["_cue_rules_fired"]) == ["ra", "rb"]
    # c2 fires only ra
    assert by_id["c2"]["_cue_delta"] == pytest.approx(0.01)
    assert by_id["c2"]["_cue_rules_fired"] == ["ra"]
    # c3 fires nothing
    assert by_id["c3"].get("_cue_delta", 0.0) == 0.0
    assert by_id["c3"].get("_cue_rules_fired", []) == []


def test_cue_rule_supports_match_field_and_strategy():
    """v4: CueRule accepts match_field and match_strategy as optional kwargs."""
    from community_brain.query.cue_rules import CueRule

    # Legacy rule (target_predicate) still works
    legacy = CueRule(
        name="legacy",
        cue_phrases=("foo",),
        target_predicate=lambda c: True,
        delta=0.01,
    )
    assert legacy.match_field is None
    assert legacy.match_strategy is None

    # New v4 rule shape
    v4 = CueRule(
        name="date_iso",
        cue_phrases=(),  # v4 rules use question_regex instead
        target_predicate=None,
        delta=0.04,
        question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
        match_field="session_date",
        match_strategy="iso_date_equals",
    )
    assert v4.match_field == "session_date"
    assert v4.match_strategy == "iso_date_equals"
    assert v4.question_regex == r"\b(\d{4}-\d{2}-\d{2})\b"


def test_yaml_loader_supports_v4_fields(tmp_path):
    """v4 cue rules in YAML use question_regex + match_field + match_strategy."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml

    p = tmp_path / "cues.yaml"
    p.write_text("""
cue_rules:
  - name: date_iso
    question_regex: '\\b(\\d{4}-\\d{2}-\\d{2})\\b'
    match_field: session_date
    match_strategy: iso_date_equals
    delta: 0.04
""")
    rules = load_cue_rules_from_yaml(p)
    assert len(rules) == 1
    assert rules[0].name == "date_iso"
    assert rules[0].match_strategy == "iso_date_equals"
    assert rules[0].match_field == "session_date"
    assert rules[0].delta == 0.04


def test_existing_apply_cue_boosts_works_with_yaml_loaded_rules(tmp_path):
    """Smoke test: the existing apply_cue_boosts function works with YAML-loaded rules."""
    from community_brain.query.cue_rules import (
        apply_cue_boosts, load_cue_rules_from_yaml,
    )
    yaml_text = """
cue_rules:
  - name: r
    cue_phrases: [unresolved]
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010
"""
    path = tmp_path / "cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.01, "has_unresolved_question": True},
        {"chunk_id": "b", "_rrf_score": 0.02, "has_unresolved_question": False},
    ]
    boosted = apply_cue_boosts("unresolved questions", candidates, rules=rules)
    by_id = {c["chunk_id"]: c["_rrf_score"] for c in boosted}
    assert by_id["a"] == pytest.approx(0.020)
    assert by_id["b"] == pytest.approx(0.020)


def test_apply_cue_boosts_handles_v4_rules():
    """v4 rules with question_regex + match_strategy fire correctly."""
    import pytest
    from community_brain.query.cue_rules import CueRule, apply_cue_boosts

    rule = CueRule(
        name="date_iso",
        cue_phrases=(),
        target_predicate=None,
        delta=0.04,
        question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
        match_field="session_date",
        match_strategy="iso_date_equals",
    )
    candidates = [
        {"chunk_id": "a", "session_date": "2026-03-04", "_rrf_score": 0.020},
        {"chunk_id": "b", "session_date": "2026-02-25", "_rrf_score": 0.020},
    ]
    boosted = apply_cue_boosts(
        question="What did they discuss on 2026-03-04?",
        candidates=candidates,
        rules=(rule,),
    )
    by_id = {c["chunk_id"]: c for c in boosted}
    assert by_id["a"]["_rrf_score"] == pytest.approx(0.060)
    assert by_id["b"]["_rrf_score"] == pytest.approx(0.020)
    assert by_id["a"]["_cue_delta"] == pytest.approx(0.040)
    assert by_id["a"]["_cue_rules_fired"] == ["date_iso"]


def test_apply_cue_boosts_speaker_two_rule_pattern(tmp_path):
    """build_speaker_auto_rule returns 2 rules; apply_cue_boosts dispatches
    each independently. The 'spoke' rule fires on speakers_spoke matches with
    delta 0.04; the 'mentioned' rule fires on speakers_mentioned-only matches
    with delta 0.02."""
    import pytest
    from community_brain.query.cue_rules import (
        apply_cue_boosts, build_speaker_auto_rule,
    )

    yaml_path = tmp_path / "speaker-aliases.yaml"
    yaml_path.write_text("""
aliases:
  Adam James:
    - Adam
""")
    spoke_rule, mentioned_rule = build_speaker_auto_rule(yaml_path)

    candidates = [
        {
            "chunk_id": "a",
            "speakers_spoke": ["Adam James"],
            "speakers_mentioned": [],
            "_rrf_score": 0.020,
        },
        {
            "chunk_id": "b",
            "speakers_spoke": ["Brandon Hancock"],
            "speakers_mentioned": ["Adam James"],
            "_rrf_score": 0.020,
        },
        {
            "chunk_id": "c",
            "speakers_spoke": [],
            "speakers_mentioned": [],
            "_rrf_score": 0.020,
        },
    ]
    boosted = apply_cue_boosts(
        question="What has Adam James talked about?",
        candidates=candidates,
        rules=(spoke_rule, mentioned_rule),
    )
    by_id = {c["chunk_id"]: c for c in boosted}
    assert by_id["a"]["_rrf_score"] == pytest.approx(0.060)
    assert by_id["b"]["_rrf_score"] == pytest.approx(0.040)
    assert by_id["c"]["_rrf_score"] == pytest.approx(0.020)


def test_yaml_loader_rejects_half_v4_entry(tmp_path, caplog):
    """An entry with only one of question_regex/match_strategy is rejected
    at load time with a clear error (not a silent KeyError on cue_phrases)."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml

    p = tmp_path / "cues.yaml"
    # Entry has question_regex but no match_strategy → should be rejected,
    # NOT silently fall through to legacy.
    p.write_text("""
cue_rules:
  - name: half_v4_broken
    question_regex: '\\b\\w+\\b'
    delta: 0.04
""")
    with caplog.at_level(logging.ERROR):
        rules = load_cue_rules_from_yaml(p)
    # Rule was rejected; loader returned an empty rule set (no last-known-good cache yet).
    assert len(rules) == 0
    assert any("question_regex" in r.message and "match_strategy" in r.message
               for r in caplog.records)

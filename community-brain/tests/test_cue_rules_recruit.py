"""v5: recruit flag + predicate_spec preservation on cue rules (design D3)."""
from __future__ import annotations

from community_brain.query.cue_rules import (
    build_speaker_auto_rule,
    load_cue_rules_from_yaml,
)

V4_RULE_YAML = """
cue_rules:
  - name: date_iso_match
    question_regex: '\\b(\\d{4}-\\d{2}-\\d{2})\\b'
    match_field: session_date
    match_strategy: iso_date_equals
    delta: 0.04
    recruit: true
"""

V4_RULE_NO_RECRUIT_YAML = """
cue_rules:
  - name: date_iso_match
    question_regex: '\\b(\\d{4}-\\d{2}-\\d{2})\\b'
    match_field: session_date
    match_strategy: iso_date_equals
    delta: 0.04
"""

LEGACY_RULE_YAML = """
cue_rules:
  - name: unresolved_questions
    cue_phrases:
      - unresolved
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.04
    recruit: true
"""

ALIASES_YAML = """
aliases:
  Adam James:
    - Adam
"""


def test_loader_parses_recruit_flag_on_v4_rule(tmp_path):
    p = tmp_path / "cues.yaml"
    p.write_text(V4_RULE_YAML)
    rules = load_cue_rules_from_yaml(p)
    assert len(rules) == 1
    assert rules[0].recruit is True


def test_loader_recruit_defaults_to_false(tmp_path):
    p = tmp_path / "cues.yaml"
    p.write_text(V4_RULE_NO_RECRUIT_YAML)
    rules = load_cue_rules_from_yaml(p)
    assert rules[0].recruit is False


def test_loader_preserves_predicate_spec_on_legacy_rule(tmp_path):
    p = tmp_path / "cues.yaml"
    p.write_text(LEGACY_RULE_YAML)
    rules = load_cue_rules_from_yaml(p)
    assert rules[0].recruit is True
    assert rules[0].predicate_spec == {"field": "has_unresolved_question", "value": True}
    # legacy predicate callable still built
    assert rules[0].target_predicate is not None
    assert rules[0].target_predicate({"has_unresolved_question": True}) is True


def test_v4_rule_has_no_predicate_spec(tmp_path):
    p = tmp_path / "cues.yaml"
    p.write_text(V4_RULE_YAML)
    rules = load_cue_rules_from_yaml(p)
    assert rules[0].predicate_spec is None


def test_speaker_auto_rules_recruit_by_default(tmp_path):
    p = tmp_path / "speaker-aliases.yaml"
    p.write_text(ALIASES_YAML)
    spoke, mentioned = build_speaker_auto_rule(p)
    assert spoke.recruit is True
    assert mentioned.recruit is True

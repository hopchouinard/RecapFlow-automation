"""Tests for speaker auto-rule generation from speaker-aliases.yaml."""
from __future__ import annotations

import re
from pathlib import Path

from community_brain.query.cue_rules import (
    build_speaker_auto_rule,
    apply_v4_strategy,
)


def _write_speaker_yaml(tmp_path: Path, content: str) -> Path:
    p = tmp_path / "speaker-aliases.yaml"
    p.write_text(content)
    return p


def test_build_speaker_auto_rule_returns_two_rules(tmp_path: Path):
    """v4 returns a tuple: one rule for speakers_spoke (full delta) and
    one for speakers_mentioned (half delta). Same regex on both."""
    yaml_content = """
aliases:
  Adam James:
    - Adam
    - "Adam (Gold Flamingo)"
  Brandon Hancock:
    - Brandon
    - Brendan
  Patrick Chouinard:
    - Patrick
"""
    yaml_path = _write_speaker_yaml(tmp_path, yaml_content)
    rules = build_speaker_auto_rule(yaml_path)

    assert isinstance(rules, tuple)
    assert len(rules) == 2

    spoke_rule, mentioned_rule = rules
    assert spoke_rule.name == "speaker_auto_spoke"
    assert spoke_rule.match_field == "speakers_spoke"
    assert spoke_rule.match_strategy == "name_resolve_then_check"
    assert spoke_rule.delta == 0.04

    assert mentioned_rule.name == "speaker_auto_mentioned"
    assert mentioned_rule.match_field == "speakers_mentioned"
    assert mentioned_rule.match_strategy == "name_resolve_then_check"
    assert mentioned_rule.delta == 0.02

    # Both rules share the same regex
    assert spoke_rule.question_regex == mentioned_rule.question_regex
    # Behavior: the regex matches and captures the expected names
    m_adam = re.search(spoke_rule.question_regex, "What has Adam James talked about?", re.IGNORECASE)
    assert m_adam is not None, "regex should match 'Adam James' in question"
    assert m_adam.group(1) == "Adam James"
    m_brandon = re.search(spoke_rule.question_regex, "What has Brandon Hancock talked about?", re.IGNORECASE)
    assert m_brandon is not None, "regex should match 'Brandon Hancock' in question"
    assert m_brandon.group(1) == "Brandon Hancock"


def test_speaker_auto_rule_longest_first(tmp_path: Path):
    """Longer names must come BEFORE shorter aliases in the regex alternation."""
    yaml_content = """
aliases:
  Adam James:
    - Adam
"""
    yaml_path = _write_speaker_yaml(tmp_path, yaml_content)
    rules = build_speaker_auto_rule(yaml_path)
    regex = rules[0].question_regex
    # Behavior: "Adam James" must be captured in full, not just "Adam",
    # proving longest-first ordering wins the alternation.
    m = re.search(regex, "Adam James", re.IGNORECASE)
    assert m is not None, f"regex should match 'Adam James'; got: {regex}"
    assert m.group(1) == "Adam James", (
        f"captured group should be 'Adam James' (longest-first), got {m.group(1)!r}; regex: {regex}"
    )


def test_name_resolve_strategy_matches_speakers_spoke_only(tmp_path: Path):
    """name_resolve_then_check respects match_field — only checks the named field."""
    yaml_content = """
aliases:
  Adam James:
    - Adam
"""
    yaml_path = _write_speaker_yaml(tmp_path, yaml_content)
    rules = build_speaker_auto_rule(yaml_path)
    spoke_rule = rules[0]

    chunk_with_spoke = {
        "speakers_spoke": ["Adam James"],
        "speakers_mentioned": [],
    }
    chunk_with_mentioned_only = {
        "speakers_spoke": [],
        "speakers_mentioned": ["Adam James"],
    }

    # spoke rule fires for chunk_with_spoke but NOT for chunk_with_mentioned_only
    assert apply_v4_strategy(
        question="What has Adam James talked about?",
        chunk=chunk_with_spoke,
        question_regex=spoke_rule.question_regex,
        match_field="speakers_spoke",
        match_strategy="name_resolve_then_check",
    ) is True
    assert apply_v4_strategy(
        question="What has Adam James talked about?",
        chunk=chunk_with_mentioned_only,
        question_regex=spoke_rule.question_regex,
        match_field="speakers_spoke",
        match_strategy="name_resolve_then_check",
    ) is False


def test_name_resolve_strategy_alias_resolves_to_canonical(tmp_path: Path):
    """Question uses 'Adam' alone; chunk has 'Adam James' canonical."""
    yaml_content = """
aliases:
  Adam James:
    - Adam
"""
    yaml_path = _write_speaker_yaml(tmp_path, yaml_content)
    rules = build_speaker_auto_rule(yaml_path)
    spoke_rule = rules[0]

    chunk = {
        "speakers_spoke": ["Adam James"],
        "speakers_mentioned": [],
    }
    matched = apply_v4_strategy(
        question="What has Adam talked about?",
        chunk=chunk,
        question_regex=spoke_rule.question_regex,
        match_field="speakers_spoke",
        match_strategy="name_resolve_then_check",
    )
    assert matched is True


def test_name_resolve_strategy_no_match_when_speaker_absent(tmp_path: Path):
    yaml_content = """
aliases:
  Adam James:
    - Adam
  Brandon Hancock:
    - Brandon
"""
    yaml_path = _write_speaker_yaml(tmp_path, yaml_content)
    rules = build_speaker_auto_rule(yaml_path)
    spoke_rule = rules[0]

    chunk = {
        "speakers_spoke": ["Brandon Hancock"],
        "speakers_mentioned": [],
    }
    matched = apply_v4_strategy(
        question="What has Adam James talked about?",
        chunk=chunk,
        question_regex=spoke_rule.question_regex,
        match_field="speakers_spoke",
        match_strategy="name_resolve_then_check",
    )
    assert matched is False

"""Last-known-good cache for speaker auto-rules (v5 D12).

The cue-rules YAML loader already survives transient edit windows via
_LAST_GOOD_RULES; build_speaker_auto_rule did not — a partial write to
speaker-aliases.yaml silently degraded speaker boosts to never-match for
that request. The cache must restore the resolver dicts too, since
name_resolve_then_check resolves through module-level state.
"""
from __future__ import annotations

from community_brain.query import cue_rules

ALIASES_YAML = """
aliases:
  Adam James:
    - Adam
  Garron Selliken:
    - Garron
"""


def test_lkg_returns_cached_rules_after_corrupt_rewrite(tmp_path):
    p = tmp_path / "speaker-aliases.yaml"
    p.write_text(ALIASES_YAML)
    first = cue_rules.build_speaker_auto_rule(p)
    assert "Adam" in (first[0].question_regex or "")

    # Simulate a partial-write window: the file is momentarily unparseable.
    p.write_text("aliases: [unclosed")
    second = cue_rules.build_speaker_auto_rule(p)

    assert second == first
    # The resolver dicts survived too — not just the rule objects.
    assert cue_rules._SPEAKER_CASEFOLD_LOOKUP.get("adam") == "Adam James"
    assert cue_rules._SPEAKER_NAME_TO_CANONICAL.get("Garron") == "Garron Selliken"


def test_first_time_empty_registry_still_returns_never_match(tmp_path):
    p = tmp_path / "empty-aliases.yaml"
    p.write_text("aliases: {}\n")
    spoke, mentioned = cue_rules.build_speaker_auto_rule(p)
    assert spoke.question_regex == r"(?!x)x"
    assert mentioned.question_regex == r"(?!x)x"


def test_lkg_is_per_path(tmp_path):
    good = tmp_path / "good.yaml"
    good.write_text(ALIASES_YAML)
    cue_rules.build_speaker_auto_rule(good)

    other = tmp_path / "other.yaml"
    other.write_text("aliases: [unclosed")
    spoke, _ = cue_rules.build_speaker_auto_rule(other)
    # No prior good load for THIS path -> never-match, not the good cache.
    assert spoke.question_regex == r"(?!x)x"

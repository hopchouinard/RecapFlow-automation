"""Tests for apply_canonicalizations CLI."""
from __future__ import annotations

import pytest

from community_brain.cli.apply_canonicalizations import (
    apply_proposals_to_registry,
    ProposalConflictError,
)


def test_apply_merges_accepted_proposals_into_aliases():
    """An accepted proposal becomes a new aliases entry; pending entries removed."""
    registry = {
        "version": "2026-04-29",
        "aliases": {"Existing Person": ["existing"]},
        "pending": ["Adam", "Adam - Gold Flamingo", "Tony"],
    }
    proposals = {
        "proposals": [
            {
                "canonical": "Adam James",
                "candidate_aliases": ["Adam", "Adam - Gold Flamingo"],
                "confidence": "medium",
                "reason": "token containment",
            },
        ],
        "ambiguous": [{"name": "Tony", "reason": "ambiguous first name"}],
    }
    updated = apply_proposals_to_registry(registry, proposals)
    assert "Adam James" in updated["aliases"]
    assert "Adam" in updated["aliases"]["Adam James"]
    assert "Adam - Gold Flamingo" in updated["aliases"]["Adam James"]
    assert "Existing Person" in updated["aliases"]
    assert "Adam" not in updated["pending"]
    assert "Adam - Gold Flamingo" not in updated["pending"]
    # Tony stays in pending — operator decides later.
    assert "Tony" in updated["pending"]


def test_apply_preserves_existing_aliases_for_canonical():
    """If 'Adam James' already exists with prior aliases, append new ones (no replacement)."""
    registry = {
        "aliases": {"Adam James": ["AdamJ"]},
        "pending": ["Adam"],
    }
    proposals = {
        "proposals": [
            {
                "canonical": "Adam James",
                "candidate_aliases": ["Adam"],
                "confidence": "high",
                "reason": "test",
            },
        ],
        "ambiguous": [],
    }
    updated = apply_proposals_to_registry(registry, proposals)
    assert "AdamJ" in updated["aliases"]["Adam James"]
    assert "Adam" in updated["aliases"]["Adam James"]


def test_apply_idempotent():
    """Applying the same proposals twice produces the same registry."""
    registry = {"aliases": {"Adam James": []}, "pending": ["Adam"]}
    proposals = {
        "proposals": [
            {"canonical": "Adam James", "candidate_aliases": ["Adam"],
             "confidence": "high", "reason": "test"},
        ],
        "ambiguous": [],
    }
    once = apply_proposals_to_registry(registry, proposals)
    twice = apply_proposals_to_registry(once, proposals)
    assert once == twice


def test_apply_handles_empty_proposals():
    registry = {"aliases": {"Existing": ["e1"]}, "pending": ["Tony"]}
    updated = apply_proposals_to_registry(registry, {"proposals": [], "ambiguous": []})
    assert updated == registry


def test_apply_does_not_modify_input_registry():
    """apply_proposals_to_registry should be pure — input registry unchanged."""
    registry = {"aliases": {"Adam James": []}, "pending": ["Adam"]}
    proposals = {
        "proposals": [
            {"canonical": "Adam James", "candidate_aliases": ["Adam"],
             "confidence": "high", "reason": "test"},
        ],
        "ambiguous": [],
    }
    _ = apply_proposals_to_registry(registry, proposals)
    # Original unchanged
    assert "Adam" in registry["pending"]
    assert registry["aliases"]["Adam James"] == []


def test_apply_canonicals_sorted():
    """Aliases list is sorted for deterministic output."""
    registry = {"aliases": {"X": ["zeta", "alpha"]}, "pending": ["beta"]}
    proposals = {
        "proposals": [
            {"canonical": "X", "candidate_aliases": ["beta"],
             "confidence": "high", "reason": "test"},
        ],
        "ambiguous": [],
    }
    updated = apply_proposals_to_registry(registry, proposals)
    assert updated["aliases"]["X"] == sorted(["zeta", "alpha", "beta"])


def test_apply_raises_when_candidate_is_already_a_different_canonical_alias():
    """Stale proposals: 'Adam' was already promoted to 'Adam James',
    but a proposal tries to add 'Adam' as alias of 'Adam Smith'."""
    registry = {
        "aliases": {"Adam James": ["Adam"], "Adam Smith": []},
        "pending": [],
    }
    proposals = {
        "proposals": [
            {"canonical": "Adam Smith", "candidate_aliases": ["Adam"],
             "confidence": "high", "reason": "test"},
        ],
        "ambiguous": [],
    }
    with pytest.raises(ProposalConflictError, match="already an alias"):
        apply_proposals_to_registry(registry, proposals)


def test_apply_raises_when_candidate_is_a_canonical():
    """A proposal can't make a canonical name into an alias of another canonical."""
    registry = {
        "aliases": {"Adam James": [], "Adam Smith": []},
        "pending": [],
    }
    proposals = {
        "proposals": [
            {"canonical": "Adam James", "candidate_aliases": ["Adam Smith"],
             "confidence": "high", "reason": "test"},
        ],
        "ambiguous": [],
    }
    with pytest.raises(ProposalConflictError, match="already a canonical"):
        apply_proposals_to_registry(registry, proposals)

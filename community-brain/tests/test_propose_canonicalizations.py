"""Tests for the propose_canonicalizations CLI."""
from __future__ import annotations

from community_brain.cli.propose_canonicalizations import (
    generate_proposals,
)


def test_high_confidence_case_insensitive_exact_match():
    """'asako' (pending) -> 'Asako Hayase' (canonical) when first-name match exists."""
    registry = {
        "aliases": {"Asako Hayase": []},
        "pending": ["asako"],
    }
    proposals = generate_proposals(registry)
    assert any(
        p["canonical"] == "Asako Hayase"
        and "asako" in p["candidate_aliases"]
        and p["confidence"] == "high"
        for p in proposals["proposals"]
    )


def test_medium_confidence_token_containment():
    """'Adam' (pending) + 'Adam - Gold Flamingo' (pending) -> 'Adam James' canonical."""
    registry = {
        "aliases": {"Adam James": []},
        "pending": ["Adam", "Adam - Gold Flamingo"],
    }
    proposals = generate_proposals(registry)
    matching = [p for p in proposals["proposals"] if p["canonical"] == "Adam James"]
    assert len(matching) == 1
    aliases = set(matching[0]["candidate_aliases"])
    assert "Adam" in aliases
    assert "Adam - Gold Flamingo" in aliases
    # Confidence is medium because at least one entry came in via medium-tier heuristic.
    assert matching[0]["confidence"] == "medium"


def test_ambiguous_first_name_no_proposal():
    """'Tony' with no canonical 'Tony X' candidate -> goes to ambiguous."""
    registry = {
        "aliases": {"Tom Welsh": [], "Brandon Hancock": []},
        "pending": ["Tony"],
    }
    proposals = generate_proposals(registry)
    assert any(a["name"] == "Tony" for a in proposals["ambiguous"])
    assert not any(
        "Tony" in p["candidate_aliases"] for p in proposals["proposals"]
    )


def test_ambiguous_zoom_display_name():
    """'David's iPhone' has no plausible canonical -> ambiguous."""
    registry = {
        "aliases": {"David Sanders": []},
        "pending": ["David's iPhone"],
    }
    proposals = generate_proposals(registry)
    assert any(a["name"] == "David's iPhone" for a in proposals["ambiguous"])


def test_idempotent_generates_same_proposals():
    """Running generate_proposals twice on the same input produces the same output (modulo timestamp)."""
    registry = {
        "aliases": {"Adam James": []},
        "pending": ["Adam"],
    }
    p1 = generate_proposals(registry)
    p2 = generate_proposals(registry)
    assert p1["proposals"] == p2["proposals"]
    assert p1["ambiguous"] == p2["ambiguous"]


def test_first_name_with_multiple_canonicals_is_ambiguous():
    """If 'Mike' could be Mike Simko or Mike Anderson, surface as ambiguous."""
    registry = {
        "aliases": {"Mike Simko": [], "Mike Anderson": []},
        "pending": ["Mike"],
    }
    proposals = generate_proposals(registry)
    assert any(a["name"] == "Mike" for a in proposals["ambiguous"])


def test_already_canonical_pending_entry():
    """Edge case: 'Adam James' appears in both aliases AND pending — surface
    as ambiguous OR as a self-match proposal. Operator decides."""
    registry = {
        "aliases": {"Adam James": []},
        "pending": ["Adam James"],
    }
    proposals = generate_proposals(registry)
    surfaces_in_ambiguous = any(a["name"] == "Adam James" for a in proposals["ambiguous"])
    surfaces_in_proposals = any(
        p["canonical"] == "Adam James"
        and "Adam James" in p["candidate_aliases"]
        for p in proposals["proposals"]
    )
    assert surfaces_in_ambiguous or surfaces_in_proposals


def test_empty_pending_returns_empty_proposals():
    registry = {"aliases": {"Adam James": []}, "pending": []}
    proposals = generate_proposals(registry)
    assert proposals["proposals"] == []
    assert proposals["ambiguous"] == []


def test_proposals_have_expected_top_level_keys():
    """Output shape: generated_at + proposals + ambiguous."""
    registry = {"aliases": {"Adam James": []}, "pending": ["Adam"]}
    proposals = generate_proposals(registry)
    assert set(proposals.keys()) == {"generated_at", "proposals", "ambiguous"}
    assert isinstance(proposals["generated_at"], str)

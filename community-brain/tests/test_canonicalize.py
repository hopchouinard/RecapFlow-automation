"""Tests for the canonicalization pass."""
from __future__ import annotations

import pytest

from community_brain.ingestion.canonicalize import (
    build_alias_map,
    canonicalize_names,
)


def test_build_alias_map_inverts_registry():
    """build_alias_map produces alias -> canonical lookup from speaker-aliases.yaml shape."""
    registry = {
        "aliases": {
            "Adam James": ["Adam", "Adam - Gold Flamingo"],
            "Delvis Nunez": ["delvis"],
        },
        "pending": [],
    }
    m = build_alias_map(registry)
    assert m["Adam"] == "Adam James"
    assert m["Adam - Gold Flamingo"] == "Adam James"
    assert m["delvis"] == "Delvis Nunez"


def test_build_alias_map_includes_canonical_self_reference():
    """Canonicals also map to themselves so canonicalize_names is idempotent."""
    registry = {"aliases": {"Adam James": ["Adam"]}, "pending": []}
    m = build_alias_map(registry)
    assert m["Adam James"] == "Adam James"


def test_build_alias_map_handles_empty_registry():
    m = build_alias_map({"aliases": {}, "pending": []})
    assert m == {}


def test_build_alias_map_handles_none_alias_lists():
    """Some entries may have empty/None alias lists in the YAML."""
    registry = {"aliases": {"Adam James": None, "Brandon Hancock": []}}
    m = build_alias_map(registry)
    assert m["Adam James"] == "Adam James"
    assert m["Brandon Hancock"] == "Brandon Hancock"


def test_canonicalize_names_replaces_aliases():
    alias_map = {"Adam": "Adam James", "delvis": "Delvis Nunez"}
    raw = ["Adam", "Brandon Hancock", "delvis"]
    canonical, unknown = canonicalize_names(raw, alias_map)
    assert canonical == ["Adam James", "Brandon Hancock", "Delvis Nunez"]
    assert unknown == ["Brandon Hancock"]


def test_canonicalize_names_preserves_unknown():
    alias_map = {"Adam": "Adam James"}
    raw = ["Tony", "Adam"]
    canonical, unknown = canonicalize_names(raw, alias_map)
    assert "Tony" in canonical
    assert "Adam James" in canonical
    assert "Tony" in unknown


def test_canonicalize_names_deduplicates():
    """Two raw forms that map to the same canonical produce one entry."""
    alias_map = {"Adam": "Adam James", "Adam - Gold Flamingo": "Adam James"}
    raw = ["Adam", "Adam - Gold Flamingo"]
    canonical, _ = canonicalize_names(raw, alias_map)
    assert canonical == ["Adam James"]


def test_canonicalize_names_preserves_first_occurrence_order():
    alias_map = {"a": "A", "b": "B", "c": "C"}
    raw = ["c", "a", "b", "a"]
    canonical, _ = canonicalize_names(raw, alias_map)
    assert canonical == ["C", "A", "B"]


def test_canonicalize_names_handles_none_input():
    canonical, unknown = canonicalize_names(None, {"X": "Y"})
    assert canonical == []
    assert unknown == []


def test_canonicalize_names_handles_empty_input():
    canonical, unknown = canonicalize_names([], {"X": "Y"})
    assert canonical == []
    assert unknown == []


def test_canonicalize_names_handles_empty_alias_map():
    canonical, unknown = canonicalize_names(["Tony", "Adam"], {})
    assert canonical == ["Tony", "Adam"]
    assert set(unknown) == {"Tony", "Adam"}

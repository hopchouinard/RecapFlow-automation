"""Canonicalization pass for v3 person-bearing fields.

Applies the speaker-aliases.yaml alias map to extracted name lists at
chunk write time and during the recanonicalize pass. Returns the
canonical-form list plus any unknown names that should be appended to
the registry's pending: queue.

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §7
"""
from __future__ import annotations


def build_alias_map(registry: dict) -> dict[str, str]:
    """Invert a speaker-aliases.yaml-shape registry into alias->canonical lookup.

    Each canonical name is also mapped to itself so callers don't need
    to special-case "is this already canonical?".
    """
    aliases = registry.get("aliases") or {}
    out: dict[str, str] = {}
    for canonical, alias_list in aliases.items():
        out[canonical] = canonical
        for alias in alias_list or []:
            out[alias] = canonical
    return out


def canonicalize_names(
    raw_names: list[str] | None,
    alias_map: dict[str, str],
) -> tuple[list[str], list[str]]:
    """Apply alias_map to raw_names; return (canonical_list, unknown_list).

    canonical_list: input names with each replaced by its canonical form
        when alias_map has it; raw form retained otherwise. De-duplicated
        while preserving first-occurrence order.
    unknown_list: names not present in alias_map (returned in raw form,
        for the caller to append to the registry's pending queue).
    """
    if not raw_names:
        return [], []
    seen: set[str] = set()
    canonical: list[str] = []
    unknown: list[str] = []
    for name in raw_names:
        resolved = alias_map.get(name, name)
        if resolved not in seen:
            seen.add(resolved)
            canonical.append(resolved)
        if name not in alias_map:
            unknown.append(name)
    return canonical, unknown


def canonicalize_chunk_fields(
    *,
    speakers_spoke: list[str] | None,
    speakers_mentioned: list[str] | None,
    entities: list[str] | None,
    alias_map: dict[str, str],
) -> tuple[list[str], list[str], list[str], list[str], list[str]]:
    """Canonicalize all three person-bearing fields and enforce the
    speakers_spoke / speakers_mentioned partition.

    Returns:
        (canon_speakers_spoke, canon_speakers_mentioned, canon_entities,
         unknown_speakers_spoke, unknown_speakers_mentioned)

    Partition enforcement: speakers_mentioned excludes any name in
    speakers_spoke, applied AFTER canonicalization (so different raw
    aliases that collapse to the same canonical can't put the same
    person in both lists).

    Used by both ingest pipeline (pipeline.py) and recanonicalize CLI
    (recanonicalize.py) so the partition fix can't drift across call sites.
    """
    canon_spk, unk_spk = canonicalize_names(speakers_spoke, alias_map)
    canon_men, unk_men = canonicalize_names(speakers_mentioned, alias_map)
    canon_ent, _ = canonicalize_names(entities, alias_map)
    # Partition: speakers_mentioned excludes anyone in speakers_spoke
    spoke_set = set(canon_spk)
    canon_men = [n for n in canon_men if n not in spoke_set]
    return canon_spk, canon_men, canon_ent, unk_spk, unk_men

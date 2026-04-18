"""Speaker and entity registries with atomic YAML writes.

v1 constraint: single-writer. The pipeline orchestrator holds one registry
instance per session and flushes once at the end. Atomic rename guarantees
no partial writes survive a crash.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TypedDict

import yaml

from community_brain.ingestion._io import merge_and_atomic_write_yaml


class EntityRecord(TypedDict, total=False):
    """Shape of a single entity entry in entity-registry.yaml."""
    type: str            # tool | framework | company | person | concept | product
    category: str
    aliases: list[str]


@dataclass
class SpeakerRegistry:
    """In-memory view of speaker-aliases.yaml with pending queue.

    NOTE: The ``aliases`` field is owned by this registry. Do not mutate it
    directly from outside — use ``add_alias`` so the lookup table stays
    consistent.
    """
    version: str
    aliases: dict[str, list[str]]  # canonical -> list of raw aliases
    pending: list[str]
    _lookup: dict[str, str] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        self._rebuild_lookup()

    def _rebuild_lookup(self) -> None:
        self._lookup = {}
        for canonical, raws in self.aliases.items():
            self._lookup[canonical] = canonical
            for raw in raws:
                self._lookup[raw] = canonical

    def canonicalize(self, raw: str) -> str | None:
        """Return the canonical name for a raw speaker mention, or None if unknown.

        Speaker lookups are CASE-SENSITIVE because speakers are proper nouns:
        "alex" and "Alex" could be two different people in the same session.
        Raw mentions are stored and compared exactly as-is.
        """
        return self._lookup.get(raw)

    def as_flat_map(self) -> dict[str, str]:
        """Return a flat ``{raw: canonical, canonical: canonical}`` mapping.

        Suitable as a drop-in replacement for the legacy ``speaker-aliases.json``
        shape consumed by ``normalize_speaker(speaker, aliases)``.
        """
        return dict(self._lookup)

    def append_pending(self, raw_names: list[str]) -> None:
        """Buffer unknown raw names into the pending queue (deduped in memory)."""
        existing = set(self.pending)
        for name in raw_names:
            if name and name not in existing:
                self.pending.append(name)
                existing.add(name)

    def add_alias(self, canonical: str, raw: str) -> None:
        """Add a single raw->canonical alias mapping at runtime.

        Use this instead of mutating self.aliases directly so the lookup table
        stays consistent.
        """
        self.aliases.setdefault(canonical, [])
        if raw not in self.aliases[canonical]:
            self.aliases[canonical].append(raw)
        self._rebuild_lookup()

    def flush(self, path: Path) -> None:
        """Atomically write the registry to disk.

        Merges in-memory pending with any pending entries currently on disk
        before writing, so concurrent flushes from different processes or
        sessions cannot lose updates (TOCTOU-safe). The per-path lock in
        merge_and_atomic_write_yaml serializes the read-merge-write cycle.
        """
        payload = {
            "version": self.version,
            "aliases": self.aliases,
            "pending": self.pending,
        }
        merge_and_atomic_write_yaml(path, payload, merge_list_keys=("pending",))


@dataclass
class EntityRegistry:
    """In-memory view of entity-registry.yaml with pending queue.

    NOTE: The ``entities`` field is owned by this registry. Do not mutate it
    directly from outside — use ``add_entity`` so the lookup table stays
    consistent.
    """
    version: str
    entities: dict[str, EntityRecord]  # canonical -> {type, category, aliases}
    pending: list[str]
    _lookup: dict[str, str] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        self._rebuild_lookup()

    def _rebuild_lookup(self) -> None:
        self._lookup = {}
        for canonical, meta in self.entities.items():
            self._lookup[canonical.lower()] = canonical
            self._lookup[canonical] = canonical
            for alias in meta.get("aliases", []) or []:
                self._lookup[alias.lower()] = canonical
                self._lookup[alias] = canonical

    def canonicalize(self, raw: str) -> str | None:
        """Return the canonical entity name for a raw mention, or None.

        CASE-INSENSITIVE via str.lower() (ASCII-oriented). Does NOT apply Unicode
        casefold() or NFKC normalization — adequate for ASCII tool/product names
        (Codex, LangChain) but may miss non-ASCII variants. If multilingual entity
        names become relevant in v2, upgrade to casefold + NFKC.

        The lookup first tries the exact string, then its lowercased form.
        """
        if raw in self._lookup:
            return self._lookup[raw]
        return self._lookup.get(raw.lower())

    def append_pending(self, raw_names: list[str]) -> None:
        """Buffer unknown raw mentions into the pending queue (deduped)."""
        existing = set(self.pending)
        for name in raw_names:
            if name and name not in existing:
                self.pending.append(name)
                existing.add(name)

    def add_entity(self, canonical: str, record: EntityRecord) -> None:
        """Add a single entity at runtime. Rebuilds the canonicalize lookup.

        Preserves all fields from the TypedDict (including any future additions)
        via dict unpacking, with a defensive list copy for the aliases field so
        external mutation can't leak in.
        """
        copied: dict = dict(record)
        if "aliases" in copied and copied["aliases"] is not None:
            copied["aliases"] = list(copied["aliases"])
        self.entities[canonical] = copied  # type: ignore[assignment]
        self._rebuild_lookup()

    def flush(self, path: Path) -> None:
        """Atomically write the registry to disk.

        Merges in-memory pending with any pending entries currently on disk
        before writing, so concurrent flushes from different processes or
        sessions cannot lose updates (TOCTOU-safe). The per-path lock in
        merge_and_atomic_write_yaml serializes the read-merge-write cycle.
        """
        payload = {
            "version": self.version,
            "entities": self.entities,
            "pending": self.pending,
        }
        merge_and_atomic_write_yaml(path, payload, merge_list_keys=("pending",))


def load_speaker_registry(path: Path) -> SpeakerRegistry:
    """Load speaker-aliases.yaml into a SpeakerRegistry.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the YAML is structurally malformed (wrong top-level
            type, aliases value is not a list, etc.).
    """
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    if data is None:
        raise ValueError(
            f"{path.name}: file is empty; expected YAML mapping"
        )
    if not isinstance(data, dict):
        raise ValueError(
            f"speaker-aliases.yaml must be a YAML mapping at top level, "
            f"got {type(data).__name__}"
        )

    raw_aliases = data.get("aliases", {})
    if "aliases" in data and raw_aliases is None:
        raise ValueError(
            f"{path.name}: 'aliases' is null; use an empty mapping {{}} for no aliases"
        )
    if not isinstance(raw_aliases, dict):
        raise ValueError(
            f"speaker-aliases.yaml: 'aliases' must be a mapping, "
            f"got {type(raw_aliases).__name__}"
        )
    for canonical, alias_list in raw_aliases.items():
        if not isinstance(alias_list, list):
            raise ValueError(
                f"aliases['{canonical}'] must be a list of strings, "
                f"got {type(alias_list).__name__}"
            )
        for item in alias_list:
            if not isinstance(item, str):
                raise ValueError(
                    f"aliases['{canonical}'] must be a list of strings, "
                    f"got element of type {type(item).__name__}"
                )

    raw_pending = data.get("pending") or []
    if not isinstance(raw_pending, list):
        raise ValueError(
            f"speaker-aliases.yaml: 'pending' must be a list, "
            f"got {type(raw_pending).__name__}"
        )

    return SpeakerRegistry(
        version=data.get("version", ""),
        aliases=raw_aliases,
        pending=list(raw_pending),
    )


def load_entity_registry(path: Path) -> EntityRegistry:
    """Load entity-registry.yaml into an EntityRegistry.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the YAML is structurally malformed (wrong top-level
            type, entity value is not a mapping, aliases is not a list, etc.).
    """
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    if data is None:
        raise ValueError(
            f"{path.name}: file is empty; expected YAML mapping"
        )
    if not isinstance(data, dict):
        raise ValueError(
            f"entity-registry.yaml must be a YAML mapping at top level, "
            f"got {type(data).__name__}"
        )

    raw_entities = data.get("entities", {})
    if "entities" in data and raw_entities is None:
        raise ValueError(
            f"{path.name}: 'entities' is null; use an empty mapping {{}} for no entities"
        )
    if not isinstance(raw_entities, dict):
        raise ValueError(
            f"entity-registry.yaml: 'entities' must be a mapping, "
            f"got {type(raw_entities).__name__}"
        )
    for canonical, meta in raw_entities.items():
        if not isinstance(meta, dict):
            raise ValueError(
                f"entities['{canonical}'] must be a mapping, "
                f"got {type(meta).__name__}"
            )
        alias_list = meta.get("aliases")
        if alias_list is not None:
            if not isinstance(alias_list, list):
                raise ValueError(
                    f"entities['{canonical}'].aliases must be a list of strings, "
                    f"got {type(alias_list).__name__}"
                )
            for item in alias_list:
                if not isinstance(item, str):
                    raise ValueError(
                        f"entities['{canonical}'].aliases must be a list of strings, "
                        f"got element of type {type(item).__name__}"
                    )

    raw_pending = data.get("pending") or []
    if not isinstance(raw_pending, list):
        raise ValueError(
            f"entity-registry.yaml: 'pending' must be a list, "
            f"got {type(raw_pending).__name__}"
        )

    return EntityRegistry(
        version=data.get("version", ""),
        entities=raw_entities,
        pending=list(raw_pending),
    )

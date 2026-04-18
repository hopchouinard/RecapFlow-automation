"""Speaker and entity registries with atomic YAML writes.

v1 constraint: single-writer. The pipeline orchestrator holds one registry
instance per session and flushes once at the end. Atomic rename guarantees
no partial writes survive a crash.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class SpeakerRegistry:
    """In-memory view of speaker-aliases.yaml with pending queue."""
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
        """Return the canonical name for a raw speaker mention, or None if unknown."""
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

    def flush(self, path: Path) -> None:
        """Atomically write the registry to disk.

        Writes to a temp file in the same directory, fsyncs, then renames.
        """
        tmp = path.with_suffix(path.suffix + ".tmp")
        payload = {
            "version": self.version,
            "aliases": self.aliases,
            "pending": self.pending,
        }
        tmp.write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        fd = os.open(str(tmp), os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        os.replace(tmp, path)


@dataclass
class EntityRegistry:
    """In-memory view of entity-registry.yaml with pending queue."""
    version: str
    entities: dict[str, dict]  # canonical -> {type, category, aliases}
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
        """Return the canonical entity name for a raw mention, or None."""
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

    def flush(self, path: Path) -> None:
        tmp = path.with_suffix(path.suffix + ".tmp")
        payload = {
            "version": self.version,
            "entities": self.entities,
            "pending": self.pending,
        }
        tmp.write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        fd = os.open(str(tmp), os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        os.replace(tmp, path)


def load_speaker_registry(path: Path) -> SpeakerRegistry:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    return SpeakerRegistry(
        version=data.get("version", ""),
        aliases=data.get("aliases") or {},
        pending=list(data.get("pending") or []),
    )


def load_entity_registry(path: Path) -> EntityRegistry:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    return EntityRegistry(
        version=data.get("version", ""),
        entities=data.get("entities") or {},
        pending=list(data.get("pending") or []),
    )

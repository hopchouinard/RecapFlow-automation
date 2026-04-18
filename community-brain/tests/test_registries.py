"""Tests for speaker/entity registry load and atomic append."""

from __future__ import annotations

from pathlib import Path

import yaml

from community_brain.ingestion.registries import (
    SpeakerRegistry,
    EntityRegistry,
    load_speaker_registry,
    load_entity_registry,
)


def _write_speaker_yaml(path: Path, aliases: dict[str, list[str]], pending: list[str]) -> None:
    path.write_text(
        yaml.safe_dump({"version": "2026-04-18", "aliases": aliases, "pending": pending}),
        encoding="utf-8",
    )


def _write_entity_yaml(path: Path, entities: dict, pending: list[str]) -> None:
    path.write_text(
        yaml.safe_dump({"version": "2026-04-18", "entities": entities, "pending": pending}),
        encoding="utf-8",
    )


def test_load_speaker_registry_resolves_aliases(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Alex Rojas": ["alexrojas", "Alex R"]}, [])

    reg = load_speaker_registry(path)

    assert reg.canonicalize("alexrojas") == "Alex Rojas"
    assert reg.canonicalize("Alex R") == "Alex Rojas"
    assert reg.canonicalize("Alex Rojas") == "Alex Rojas"


def test_load_speaker_registry_unknown_returns_none(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Alex Rojas": ["alexrojas"]}, [])
    reg = load_speaker_registry(path)
    assert reg.canonicalize("SomeoneElse") is None


def test_speaker_registry_append_pending_is_atomic(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])

    reg = load_speaker_registry(path)
    reg.append_pending(["NewPerson", "AnotherOne"])
    reg.flush(path)

    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert data["pending"] == ["NewPerson", "AnotherOne"]
    assert data["aliases"]["Sam"] == ["sam"]


def test_speaker_registry_append_pending_dedupes(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {}, ["ExistingPending"])

    reg = load_speaker_registry(path)
    reg.append_pending(["ExistingPending", "NewOne", "NewOne"])
    reg.flush(path)

    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert sorted(data["pending"]) == ["ExistingPending", "NewOne"]


def test_entity_registry_canonicalize(tmp_path: Path) -> None:
    path = tmp_path / "entity-registry.yaml"
    _write_entity_yaml(
        path,
        {
            "LangChain": {
                "type": "framework",
                "category": "agent_framework",
                "aliases": ["Langchain", "langchain"],
            }
        },
        [],
    )

    reg = load_entity_registry(path)

    assert reg.canonicalize("langchain") == "LangChain"
    assert reg.canonicalize("LangChain") == "LangChain"
    assert reg.canonicalize("SomethingElse") is None


def test_entity_registry_flush_preserves_yaml_shape(tmp_path: Path) -> None:
    path = tmp_path / "entity-registry.yaml"
    _write_entity_yaml(
        path,
        {
            "Codex": {
                "type": "tool",
                "category": "coding_assistant",
                "aliases": ["codex"],
            }
        },
        [],
    )

    reg = load_entity_registry(path)
    reg.append_pending(["MystTool"])
    reg.flush(path)

    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert data["entities"]["Codex"]["type"] == "tool"
    assert data["pending"] == ["MystTool"]


def test_registry_flush_uses_atomic_rename(tmp_path: Path) -> None:
    """Writing should not leave a partial file if interrupted."""
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])

    reg = load_speaker_registry(path)
    reg.append_pending(["X"])
    reg.flush(path)

    tmp_files = list(tmp_path.glob("*.tmp"))
    assert tmp_files == []

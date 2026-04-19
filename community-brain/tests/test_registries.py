"""Tests for speaker/entity registry load and atomic append."""

from __future__ import annotations

import threading
from pathlib import Path

import pytest
import yaml

from community_brain.ingestion.registries import (
    load_entity_registry,
    load_speaker_registry,
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


def test_registry_flush_preserves_original_on_replace_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """If os.replace fails (e.g. crash), the original YAML must be intact."""
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])
    original_bytes = path.read_bytes()

    reg = load_speaker_registry(path)
    reg.append_pending(["WouldBeAdded"])

    def boom(*_a, **_kw):
        raise OSError("simulated power loss")

    monkeypatch.setattr("community_brain.ingestion._io.os.replace", boom)

    with pytest.raises(OSError, match="simulated power loss"):
        reg.flush(path)

    # Original file content unchanged
    assert path.read_bytes() == original_bytes
    # Temp file cleaned up
    tmp_files = list(tmp_path.glob("*.tmp.*"))
    assert tmp_files == []


def test_load_speaker_registry_rejects_non_list_aliases(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    path.write_text(
        'version: "x"\naliases:\n  Sam: sam\npending: []\n',  # scalar instead of list
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Sam"):
        load_speaker_registry(path)


def test_load_speaker_registry_rejects_non_dict_top_level(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    path.write_text("- just\n- a\n- list\n", encoding="utf-8")
    with pytest.raises(ValueError, match="mapping"):
        load_speaker_registry(path)


def test_load_entity_registry_rejects_non_dict_entity_meta(tmp_path: Path) -> None:
    path = tmp_path / "entity-registry.yaml"
    path.write_text(
        'version: "x"\nentities:\n  LangChain: "nope"\npending: []\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="LangChain"):
        load_entity_registry(path)


def test_speaker_registry_add_alias_keeps_lookup_consistent(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])
    reg = load_speaker_registry(path)

    reg.add_alias("Sam", "samC")

    assert reg.canonicalize("samC") == "Sam"


def test_entity_registry_add_entity_keeps_lookup_consistent(tmp_path: Path) -> None:
    path = tmp_path / "entity-registry.yaml"
    _write_entity_yaml(path, {}, [])
    reg = load_entity_registry(path)

    reg.add_entity("Codex", {"type": "tool", "aliases": ["codex"]})

    assert reg.canonicalize("codex") == "Codex"


def test_concurrent_flushes_to_same_path_serialize(tmp_path: Path) -> None:
    """Two threads flushing the same registry path should not produce a corrupted file."""
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])

    errors: list[Exception] = []

    def worker(name: str) -> None:
        try:
            reg = load_speaker_registry(path)
            reg.append_pending([name])
            reg.flush(path)
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker, args=(f"Person{i}",)) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == [], errors

    # File must still parse as valid YAML and have the original Sam entry
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert data is not None
    assert data["aliases"]["Sam"] == ["sam"]
    # No leftover temp files
    assert list(tmp_path.glob("*.tmp.*")) == []


def test_concurrent_flushes_preserve_all_pending(tmp_path: Path) -> None:
    """10 threads each append a unique pending name; all 10 must survive."""
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])

    errors: list[Exception] = []
    barrier = threading.Barrier(10)

    def worker(name: str) -> None:
        try:
            barrier.wait()
            reg = load_speaker_registry(path)
            reg.append_pending([name])
            reg.flush(path)
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker, args=(f"Person{i}",)) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == [], errors

    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    pending = data["pending"]
    expected_names = {f"Person{i}" for i in range(10)}
    assert set(pending) == expected_names, f"lost updates; expected {expected_names}, got {pending}"


def test_flush_merges_with_on_disk_pending(tmp_path: Path) -> None:
    """A registry loaded with empty pending should merge any entries written
    to disk between load and flush, not overwrite them."""
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])

    reg = load_speaker_registry(path)
    reg.append_pending(["AddedInMemory"])

    # Simulate another process writing to the file between our load and flush
    _write_speaker_yaml(path, {"Sam": ["sam"]}, ["WrittenOnDisk"])

    reg.flush(path)

    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert set(data["pending"]) == {"WrittenOnDisk", "AddedInMemory"}


def test_load_speaker_registry_rejects_empty_file(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    path.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="empty"):
        load_speaker_registry(path)


def test_load_speaker_registry_rejects_null_aliases(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    path.write_text('version: "x"\naliases: null\npending: []\n', encoding="utf-8")
    with pytest.raises(ValueError, match="null"):
        load_speaker_registry(path)


def test_load_entity_registry_rejects_empty_file(tmp_path: Path) -> None:
    path = tmp_path / "entity-registry.yaml"
    path.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="empty"):
        load_entity_registry(path)


def test_render_alias_block_empty_registry(tmp_path: Path) -> None:
    from community_brain.ingestion.registries import render_alias_block

    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {}, [])
    reg = load_speaker_registry(path)

    block = render_alias_block(reg)

    # Header is always emitted so the prompt's "if not in this list" clause
    # remains syntactically anchored even with zero canonical entries.
    assert block.startswith("## SPEAKER_ALIASES")
    assert "pass the raw name through unchanged" in block
    # No canonical entries -> no bullet lines
    assert "\n- " not in block


def test_render_alias_block_populated_registry(tmp_path: Path) -> None:
    from community_brain.ingestion.registries import render_alias_block

    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(
        path,
        {
            "Alex Rojas": ["alexrojas", "Alex R"],
            "Sam": ["sam", "Samantha"],
        },
        pending=["SomeNewPerson"],
    )
    reg = load_speaker_registry(path)

    block = render_alias_block(reg)

    # Canonical entries appear sorted alphabetically for determinism
    assert block.index("- Alex Rojas") < block.index("- Sam")
    # Each canonical name lists its aliases in yaml order
    assert "- Alex Rojas — aliases: alexrojas, Alex R" in block
    assert "- Sam — aliases: sam, Samantha" in block
    # Pending entries MUST NOT leak into the rendered block
    assert "SomeNewPerson" not in block


def test_render_alias_block_canonical_with_no_aliases(tmp_path: Path) -> None:
    """A canonical name with an empty alias list renders without the em-dash tail."""
    from community_brain.ingestion.registries import render_alias_block

    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Solo Speaker": []}, [])
    reg = load_speaker_registry(path)

    block = render_alias_block(reg)
    assert "- Solo Speaker" in block
    assert "— aliases:" not in block

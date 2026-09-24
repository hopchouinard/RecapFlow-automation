"""Reject altered or unsafe preserved data before restoring it."""

import importlib.util
import json
from pathlib import Path

import pytest

path = (
    Path(__file__).resolve().parents[2]
    / "deploy/community-brain/preserved-rehearsal/verify_delivery.py"
)
spec = importlib.util.spec_from_file_location("verify_delivery", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def fixture(root):
    names = [
        "config/speaker-aliases.yaml",
        "config/entity-registry.yaml",
        "config/query-cues.yaml",
        "corpus/lancedb/nomic-v1/chunks.lance/data/fixture.lance",
        "output/2026-09-08/community-post.md",
    ]
    entries = []
    for name in names:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"fixture")
        entries.append({"path": name, "bytes": 7, "sha256": module.sha256(path)})
    manifest = {
        "preservation_id": "2026-09-09-community-brain",
        "source_archive_manifest_sha256": "1d873beab28d5d9309dcc6ed74dda31431b6e354b9b436edf097cbc32c9876ba",
        "files": entries,
    }
    (root / "manifest.json").write_text(json.dumps(manifest))
    return manifest


def test_complete_delivery(tmp_path):
    fixture(tmp_path)
    assert module.verify(tmp_path)["files_verified"] == 5


@pytest.mark.parametrize(
    "damage", ["hash", "missing", "extra", "symlink", "duplicate", "wrong_origin"]
)
def test_refuses_damaged_delivery(tmp_path, damage):
    manifest = fixture(tmp_path)
    target = tmp_path / manifest["files"][0]["path"]
    if damage == "hash":
        target.write_bytes(b"changed")
    elif damage == "missing":
        target.unlink()
    elif damage == "extra":
        (tmp_path / ".env").write_text("fixture-only")
    elif damage == "symlink":
        target.unlink()
        target.symlink_to(tmp_path / "config/entity-registry.yaml")
    elif damage == "duplicate":
        manifest["files"].append(manifest["files"][0])
    else:
        manifest["source_archive_manifest_sha256"] = "0" * 64
    (tmp_path / "manifest.json").write_text(json.dumps(manifest))
    with pytest.raises(AssertionError):
        module.verify(tmp_path)


@pytest.mark.parametrize(
    "name",
    [
        "../output/x.txt",
        "/output/x.txt",
        "output/../x.txt",
        "output//x.txt",
        "config/.env",
        "config/key.pem",
        "corpus/lancedb/nomic-v1/.git/config",
        "output/run.sh",
        "data/config",
    ],
)
def test_refuses_unapproved_paths(name):
    assert not module.allowed(name)

"""Verify a data-only preservation delivery without printing private contents."""

import hashlib
import json
from pathlib import Path, PurePosixPath

CONFIG_FILES = {
    "canonicalization-proposals.yaml",
    "speaker-aliases.yaml",
    "entity-registry.yaml",
    "query-cues.yaml",
    "chunking.yaml",
    "extraction-config.yaml",
}


def allowed(name):
    path = PurePosixPath(name)
    if (
        not name
        or path.is_absolute()
        or str(path) != name
        or any(p in (".", "..") for p in path.parts)
    ):
        return False
    if any(
        p in (".git", ".env", "node_modules", ".venv", "__pycache__")
        or p.startswith(".env.")
        for p in path.parts
    ):
        return False
    if len(path.parts) < 2:
        return False
    if path.parts[0] == "corpus":
        return (
            path.parts[:3] == ("corpus", "lancedb", "nomic-v1")
            and len(path.parts) > 3
            and path.suffix.lower()
            not in (".pem", ".key", ".env", ".sqlite", ".db", ".py", ".sh")
        )
    if path.parts[0] == "config":
        return (len(path.parts) == 2 and path.name in CONFIG_FILES) or (
            len(path.parts) == 3
            and path.parts[1] == "extraction-prompts"
            and path.suffix == ".md"
        )
    return path.parts[0] in ("output", "historical") and (
        path.suffix.lower() in (".md", ".txt")
        or path.name in ("meta.json", "extracted-signal.md.legacy")
    )


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def verify(root):
    root = Path(root)
    assert not root.is_symlink() and root.is_dir(), "Invalid delivery root"
    manifest_path = root / "manifest.json"
    assert not manifest_path.is_symlink()
    manifest = json.loads(manifest_path.read_text())
    assert manifest["preservation_id"] == "2026-09-09-community-brain"
    assert (
        manifest["source_archive_manifest_sha256"]
        == "1d873beab28d5d9309dcc6ed74dda31431b6e354b9b436edf097cbc32c9876ba"
    )
    entries = manifest["files"]
    assert entries, "Empty preservation delivery"
    seen = set()
    for entry in entries:
        name = entry["path"]
        assert allowed(name) and name not in seen, (
            "Unsafe, unexpected or duplicate path"
        )
        seen.add(name)
        path = root
        for part in PurePosixPath(name).parts:
            path /= part
            assert not path.is_symlink(), "Symlink delivery entry"
        assert path.is_file() and path.stat().st_size == entry["bytes"], (
            "Missing or changed file"
        )
        assert sha256(path) == entry["sha256"], "Delivery hash mismatch"
    actual = set()
    for path in root.rglob("*"):
        assert not path.is_symlink(), "Symlink in delivery"
        if path.is_file() and path != manifest_path:
            actual.add(path.relative_to(root).as_posix())
    assert actual == seen, "Manifest does not cover every delivered file"
    assert {
        "config/speaker-aliases.yaml",
        "config/entity-registry.yaml",
        "config/query-cues.yaml",
    } <= seen
    assert any(p.startswith("corpus/lancedb/nomic-v1/chunks.lance/") for p in seen)
    return {
        "manifest_sha256": sha256(manifest_path),
        "files_verified": len(seen),
        "bytes_verified": sum(e["bytes"] for e in entries),
        "preservation_id": manifest["preservation_id"],
        "metadata": manifest.get("metadata", {}),
    }


if __name__ == "__main__":
    import sys

    try:
        result = verify(sys.argv[1])
        # Metadata supplied by management is not printed until its fields are validated.
        result.pop("metadata", None)
        print(json.dumps(result, sort_keys=True))
    except Exception:  # noqa: BLE001 - do not print private paths/content
        raise SystemExit(
            "Preserved delivery verification failed; inspect privately before restore"
        ) from None

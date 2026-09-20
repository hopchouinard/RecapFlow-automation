"""Pin, validate and normalize the management archive into a fresh private copy."""

import json
import os
import tarfile
from pathlib import Path, PurePosixPath

from verify_delivery import allowed, sha256, verify

ROOT = Path("/srv/dev-data/artifacts/cbm-preserved-corpus-rehearsal")
TARGET = Path("/srv/dev-data/workspaces/cbm-preserved-20260910/delivery")
MANIFEST_SHA = "4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7"
ARCHIVE_SHA = "ecb100f2e4af7c3ae4350392158f936a2756ea1852fc1d6728812237502275a3"


def normalized(name):
    path = PurePosixPath(name)
    assert not path.is_absolute() and str(path) == name and ".." not in path.parts
    for old, new in (
        ("n8n/community-brain/lancedb/", "corpus/lancedb/"),
        ("n8n/community-brain/config/", "config/"),
        ("n8n/community-brain/raw-transcripts/", "historical/raw-transcripts/"),
        ("n8n/output/", "output/"),
        ("n8n/historical/", "historical/"),
    ):
        if name.startswith(old):
            result = new + name[len(old) :]
            assert allowed(result), "Unapproved payload path"
            return result
    raise ValueError("Unapproved archive root")


def main():
    os.umask(0o077)
    assert sha256(ROOT / "manifest.json") == MANIFEST_SHA
    assert sha256(ROOT / "data-only.tar.gz") == ARCHIVE_SHA
    source = json.loads((ROOT / "manifest.json").read_text())
    assert source["preservation"]["head"] == "b6f1aa46996d4ab7ccbbaed567864cc2d71f433a"
    assert source["file_count"] == 2627 and source["total_bytes"] == 108764895
    entries = {x["path"]: x for x in source["files"]}
    assert len(entries) == 2627
    mapped = {name: normalized(name) for name in entries}
    assert len(set(mapped.values())) == 2627
    assert not TARGET.exists(), "Existing restore requires review"
    TARGET.mkdir(parents=True, mode=0o700)
    seen = set()
    result = []
    with tarfile.open(ROOT / "data-only.tar.gz", "r:gz") as archive:
        for member in archive:
            assert (
                member.isfile() and member.name in entries and member.name not in seen
            )
            entry = entries[member.name]
            assert member.size == entry["bytes"]
            path = TARGET / mapped[member.name]
            path.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as src, path.open("xb") as dst:
                import shutil

                shutil.copyfileobj(src, dst)
            assert sha256(path) == entry["sha256"]
            seen.add(member.name)
            result.append(
                {
                    "path": mapped[member.name],
                    "bytes": entry["bytes"],
                    "sha256": entry["sha256"],
                }
            )
    assert seen == set(entries)
    manifest = {
        "preservation_id": "2026-09-09-community-brain",
        "source_archive_manifest_sha256": "1d873beab28d5d9309dcc6ed74dda31431b6e354b9b436edf097cbc32c9876ba",
        "management_manifest_sha256": MANIFEST_SHA,
        "management_archive_sha256": ARCHIVE_SHA,
        "metadata": source["corpus"],
        "files": result,
    }
    (TARGET / "manifest.json").write_text(json.dumps(manifest, sort_keys=True) + "\n")
    receipt = verify(TARGET)
    receipt.pop("metadata", None)
    for path in [TARGET, *TARGET.rglob("*")]:
        os.chown(path, 10001, 10001)
    (ROOT / "restore-delivery-receipt.json").write_text(
        json.dumps(receipt, sort_keys=True) + "\n"
    )
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

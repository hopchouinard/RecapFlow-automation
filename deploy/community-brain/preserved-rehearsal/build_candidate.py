"""Approved divider-only exclusions in a fresh, privately retained consumer candidate."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import lancedb
from community_brain.jobs.publication import build_bundle, validate_bundle
from community_brain.query.fts_lifecycle import ensure_fts_index
from verify_delivery import sha256, verify


def validate_exclusions(rows, approved):
    failed = [r for r in rows if r["extraction_status"] != "success"]
    expected = {r["chunk_id"]: r for r in approved}
    assert len(expected) == len(approved) == len(failed) == 13
    assert {r["chunk_id"] for r in failed} == set(expected)
    for row in failed:
        assert row["extraction_status"] == "failed"
        assert row["content_type"] == "prepared_transcript"
        assert row["full_text"] == "---"
        assert (
            hashlib.sha256(row["full_text"].encode()).hexdigest()
            == expected[row["chunk_id"]]["full_text_sha256"]
        )
        assert row["session_id"] == expected[row["chunk_id"]]["session_id"]
    return failed


def ordered(table):
    return table.combine_chunks().sort_by([("chunk_id", "ascending")])


def main():
    root = Path("/delivery")
    before = verify(root)
    source = lancedb.connect(str(root / "corpus/lancedb/nomic-v1")).open_table("chunks")
    original = source.search().limit(None).to_arrow()
    rows = original.to_pylist()
    approved = json.loads(
        Path("/results/failed-chunk-repair-candidates.json").read_text()
    )
    failed = validate_exclusions(rows, approved)
    assert len(rows) == 1914 and len({r["session_id"] for r in rows}) == 87
    kept = source.search().where("extraction_status = 'success'").limit(None).to_arrow()
    assert kept.num_rows == 1901
    work = Path("/results/consumer-candidate-v1")
    work.mkdir(mode=0o700, exist_ok=False)
    corpus = work / "corpus/lancedb/nomic-v1"
    candidate = lancedb.connect(str(corpus)).create_table("chunks", data=kept)
    ensure_fts_index(candidate, column="bm25_text")
    retained = candidate.search().limit(None).to_arrow()
    assert ordered(retained).equals(ordered(kept), check_metadata=True)
    assert set(retained.column("session_id").to_pylist()) == set(
        original.column("session_id").to_pylist()
    )
    output = work / "package"
    manifest = build_bundle(
        corpus,
        output,
        "preserved-20260909-success-only-v1",
        datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    )
    # A fresh consumer installation is retained for independent query checks.
    import tarfile

    installed = work / "installed"
    installed.mkdir()
    with tarfile.open(
        output / f"corpus-{manifest['corpus_version']}.tar.gz"
    ) as archive:
        for member in archive:
            assert member.isfile() and member.name in manifest["files"]
            path = installed / member.name
            assert path.resolve().is_relative_to(installed.resolve())
            path.parent.mkdir(parents=True, exist_ok=True)
            data = archive.extractfile(member).read()
            assert hashlib.sha256(data).hexdigest() == manifest["files"][member.name]
            path.write_bytes(data)
    reopened = lancedb.connect(str(installed / "lancedb/nomic-v1")).open_table("chunks")
    assert ordered(reopened.search().limit(None).to_arrow()).equals(
        ordered(kept), check_metadata=True
    )
    exclusions = [
        {
            "chunk_id": r["chunk_id"],
            "session_id": r["session_id"],
            "reason": "failed_markdown_divider_only",
            "full_text_sha256": hashlib.sha256(r["full_text"].encode()).hexdigest(),
        }
        for r in sorted(failed, key=lambda x: x["chunk_id"])
    ]
    provenance = {
        "policy": "approved-divider-only-exclusions-v1",
        "source_management_manifest_sha256": "4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7",
        "normalized_source_manifest_sha256": before["manifest_sha256"],
        "source_rows": 1914,
        "retained_rows": 1901,
        "sessions": 87,
        "exclusions": exclusions,
    }
    prov = output / "candidate-provenance.json"
    prov.write_text(json.dumps(provenance, sort_keys=True) + "\n")
    manifest["derivation"] = {
        "policy": provenance["policy"],
        "provenance_file": prov.name,
        "provenance_sha256": sha256(prov),
    }
    (output / "corpus-manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n"
    )
    validate_bundle(output)
    assert verify(root) == before
    result = {
        "retained_rows": 1901,
        "excluded_divider_rows": 13,
        "sessions": 87,
        "all_retained_values_and_schema_equal": True,
        "fresh_consumer_reopened": True,
        "source_delivery_unchanged": True,
        "archive_sha256": manifest["archive_sha256"],
        "provenance_sha256": sha256(prov),
        "package_manifest_sha256": sha256(output / "corpus-manifest.json"),
        "generation_calls": 0,
        "embedding_calls": 0,
        "remote_publication": False,
    }
    (work / "result.json").write_text(json.dumps(result, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

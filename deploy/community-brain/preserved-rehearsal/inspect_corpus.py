"""Read-only inspection and optional local consumer-package verification."""

import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import lancedb
from community_brain.jobs.publication import build_bundle
from community_brain.query.corpus_verify import verify_corpus_v3_state_readonly
from verify_delivery import verify


def inspect(delivery, output):
    root, output = Path(delivery), Path(output)
    assert not output.resolve().is_relative_to(root.resolve())
    before = verify(root)
    corpus = root / "corpus/lancedb/nomic-v1"
    table = lancedb.connect(str(corpus)).open_table("chunks")
    verify_corpus_v3_state_readonly(table)
    rows = (
        table.search()
        .select(
            [
                "session_id",
                "chunk_id",
                "schema_version",
                "extraction_status",
                "content_type",
            ]
        )
        .limit(None)
        .to_arrow()
        .to_pylist()
    )
    assert rows and len({r["chunk_id"] for r in rows}) == len(rows), (
        "Empty corpus or duplicate chunk IDs"
    )
    assert {r["schema_version"] for r in rows} == {"1.1"}
    assert table.schema.field("embedding").type.list_size == 768
    statuses = Counter(r["extraction_status"] for r in rows)
    result = {k: v for k, v in before.items() if k != "metadata"}
    result.update(
        session_count=len({r["session_id"] for r in rows}),
        chunk_count=len(rows),
        extraction_status_counts=dict(statuses),
        schema_version="1.1",
        embedding_dimensions=768,
        fts_verified=True,
    )
    output.mkdir(parents=True, exist_ok=False)
    if set(statuses) == {"success"}:
        bundle = build_bundle(
            corpus,
            output / "consumer",
            "preserved-20260909-dev",
            datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        )
        result.update(
            consumer_package_verified=True,
            consumer_archive_sha256=bundle["archive_sha256"],
        )
    else:
        result.update(
            consumer_package_verified=False,
            consumer_blocker="preserved_non_success_chunks_require_review",
        )
    assert verify(root) == before, "Source delivery changed during inspection"
    result.update(delivery_unchanged=True, provider_calls=0, remote_publication=False)
    (output / "inspection.json").write_text(json.dumps(result, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    try:
        inspect(sys.argv[1], sys.argv[2])
    except Exception:  # noqa: BLE001 - keep private source diagnostics off shared stdout
        raise SystemExit(
            "Preserved corpus inspection failed; no repair or publication attempted"
        ) from None

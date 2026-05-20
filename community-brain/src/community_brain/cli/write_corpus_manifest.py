"""write_corpus_manifest — emit corpus-manifest.json for a staged LanceDB.

Used by scripts/release-corpus.sh after compaction. The manifest ships
alongside the corpus tarball; verify-install.sh reads it to cross-check
the running server's /health response on recipient machines.

Usage:
    python -m community_brain.cli.write_corpus_manifest \\
        --staging /tmp/corpus-staging-v1.0.0 \\
        --out corpus-manifest.json \\
        --version v1.0.0

The --staging path should point to the staging root that contains
lancedb/nomic-v1/chunks.lance/ inside.

Exit codes:
    0 — manifest written successfully
    2 — input/infrastructure error (path missing, LanceDB cannot open, etc.)
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import lancedb

from community_brain.ingestion.embedding import _active_embed_model
from community_brain.ingestion.schema import SCHEMA_VERSION


def _utc_iso_z() -> str:
    """ISO 8601 timestamp with 'Z' suffix (Zulu time)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _count_sessions_and_chunks(table) -> tuple[int, int]:
    """Return (distinct session_id count, total row count).

    Uses table.count_rows() for chunk_count (native, no full-table scan)
    and a column-projected query for sessions (avoids loading 768-dim
    embedding vectors just to count distinct session_id values).
    """
    chunk_count = table.count_rows()
    arrow_tbl = table.search().select(["session_id"]).limit(None).to_arrow()
    distinct_sessions = len(set(arrow_tbl.column("session_id").to_pylist()))
    return (distinct_sessions, chunk_count)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Write corpus-manifest.json for a staged LanceDB."
    )
    parser.add_argument("--staging", type=Path, required=True,
                        help="Staging root containing lancedb/nomic-v1/chunks.lance/")
    parser.add_argument("--out", type=Path, required=True,
                        help="Path to write corpus-manifest.json")
    parser.add_argument("--version", required=True,
                        help="Corpus version string (e.g. 'v1.0.0')")
    args = parser.parse_args(argv)

    db_path = args.staging / "lancedb" / "nomic-v1"
    if not db_path.exists():
        print(f"ERROR: lancedb path not found: {db_path}", file=sys.stderr)
        return 2

    try:
        db = lancedb.connect(str(db_path))
    except Exception as exc:
        print(f"ERROR: cannot open LanceDB at {db_path}: {exc}", file=sys.stderr)
        return 2

    try:
        table_names = db.list_tables().tables
    except Exception as exc:
        print(f"ERROR: cannot list tables in {db_path}: {exc}", file=sys.stderr)
        return 2

    if "chunks" not in table_names:
        print(f"ERROR: no 'chunks' table in {db_path}", file=sys.stderr)
        return 2

    try:
        table = db.open_table("chunks")
        session_count, chunk_count = _count_sessions_and_chunks(table)
    except Exception as exc:
        print(f"ERROR: cannot read chunks table: {exc}", file=sys.stderr)
        return 2

    manifest = {
        "corpus_version": args.version,
        "schema_version": SCHEMA_VERSION,
        "embedding_model": _active_embed_model(),
        "session_count": session_count,
        "chunk_count": chunk_count,
        "generation_timestamp_utc": _utc_iso_z(),
    }

    try:
        args.out.write_text(json.dumps(manifest, indent=2) + "\n")
    except Exception as exc:
        print(f"ERROR: cannot write manifest to {args.out}: {exc}", file=sys.stderr)
        return 2

    print(f"OK: wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

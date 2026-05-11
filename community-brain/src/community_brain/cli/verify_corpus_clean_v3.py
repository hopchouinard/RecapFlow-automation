"""verify_corpus_clean_v3 — release-time gate for Tier B corpus tarballs.

Asserts a staged (post-compaction) LanceDB at the given path is in
clean v3 state:
  1. bm25_text column present
  2. FTS index on bm25_text exists
  3. NO legacy FTS index on full_text (left over from pre-v3)

Used by scripts/release-corpus.sh between compaction and tarballing.
A non-zero exit aborts the release before the bad blob can ship.

Usage:
    python -m community_brain.cli.verify_corpus_clean_v3 <lancedb_path>

The path should point to the directory containing the `chunks.lance`
table (i.e. one level above chunks.lance, e.g. `/tmp/staging/lancedb/nomic-v1`).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import lancedb

from community_brain.query.corpus_verify import (
    CorpusInvalidError,
    verify_corpus_v3_state_readonly,
)


def _has_legacy_full_text_fts(table) -> bool:
    """True if any FTS-style index is registered on the full_text column.

    Uses the same case-insensitive detection logic as fts_lifecycle.has_fts_index
    so behaviour matches across LanceDB version variance.

    Raises:
        RuntimeError: if list_indices() itself fails. The release gate must
            distinguish "corpus has no legacy index" (safe) from "we cannot
            tell whether the corpus has a legacy index" (infrastructure
            failure, do not ship). The latter must surface, not silently
            pass.
    """
    try:
        indices = table.list_indices()
    except Exception as exc:
        raise RuntimeError(
            f"list_indices() failed: {exc}. Cannot determine legacy-FTS state."
        ) from exc
    for idx in indices:
        idx_type = getattr(idx, "index_type", None)
        columns = getattr(idx, "columns", []) or []
        type_str = str(idx_type).upper()
        if ("FTS" in type_str or "INVERTED" in type_str) and "full_text" in columns:
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify a staged LanceDB is in clean v3 state for distribution."
    )
    parser.add_argument(
        "db_path",
        type=Path,
        help="Path to LanceDB directory (e.g. /tmp/staging/lancedb/nomic-v1)",
    )
    args = parser.parse_args(argv)

    if not args.db_path.exists():
        print(f"ERROR: path does not exist: {args.db_path}", file=sys.stderr)
        return 2

    try:
        db = lancedb.connect(str(args.db_path))
    except Exception as exc:
        print(f"ERROR: cannot open LanceDB at {args.db_path}: {exc}", file=sys.stderr)
        return 2

    try:
        table_names = db.list_tables().tables
    except Exception as exc:
        print(f"ERROR: cannot list tables in {args.db_path}: {exc}", file=sys.stderr)
        return 2
    if "chunks" not in table_names:
        print(f"ERROR: no 'chunks' table in {args.db_path}", file=sys.stderr)
        return 2

    table = db.open_table("chunks")

    # Structural + FTS-presence check (raises CorpusInvalidError on failure).
    try:
        verify_corpus_v3_state_readonly(table)
    except CorpusInvalidError as exc:
        print(f"ERROR: corpus failed v3 readonly check: {exc}", file=sys.stderr)
        return 1

    # Legacy v2 index check (clean v3 corpora must NOT carry full_text FTS).
    try:
        has_legacy = _has_legacy_full_text_fts(table)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if has_legacy:
        print(
            "ERROR: legacy FTS index detected on full_text column. "
            "Compaction did not strip the v2 index. Drop it before "
            "tarballing — recipients on RO mounts cannot do this themselves.",
            file=sys.stderr,
        )
        return 1

    print(f"OK: corpus at {args.db_path} is clean v3 state.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

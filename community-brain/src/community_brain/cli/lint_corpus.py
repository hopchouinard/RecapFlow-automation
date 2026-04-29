"""lint_corpus CLI -- populate corpus_derived_markers on chunks.

For each chunk, find K-nearest neighbors in embedding space; flag as
'recurrent' if the neighbors include >= 2 from different sessions.

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §9.
T24 will auto-trigger this from /ingest at end of session commit.

Usage:
    python -m community_brain.cli.lint_corpus [--db /data/lancedb/nomic-v1]
"""
from __future__ import annotations

import argparse
import datetime as dt
import logging
from pathlib import Path

import lancedb


logger = logging.getLogger(__name__)

K_NEAREST = 8
SIMILARITY_THRESHOLD = 0.65
CROSS_SESSION_COUNT_MIN = 2


def _now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def lint_corpus_chunks(db_path: str | Path) -> dict[str, int]:
    """Apply 'recurrent' markers across the corpus; set computed_at on every row.

    Returns {"scanned": int, "recurrent": int}.
    """
    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    rows = table.to_arrow().to_pylist()
    now_iso = _now_iso()

    recurrent_count = 0
    for row in rows:
        chunk_id = row["chunk_id"]
        session_id = row["session_id"]
        embedding = row["embedding"]
        try:
            results = (
                table.search(embedding)
                .limit(K_NEAREST + 1)  # +1 to skip self
                .to_arrow()
                .to_pylist()
            )
        except Exception as exc:
            logger.error("lint_corpus k-nearest query failed for %s: %s", chunk_id, exc)
            continue

        cross_session = 0
        for nbr in results:
            if nbr["chunk_id"] == chunk_id:
                continue
            distance = nbr.get("_distance", 1.0)
            similarity = 1.0 - distance
            if similarity < SIMILARITY_THRESHOLD:
                continue
            if nbr["session_id"] != session_id:
                cross_session += 1

        existing_markers = list(row.get("corpus_derived_markers") or [])
        if cross_session >= CROSS_SESSION_COUNT_MIN:
            if "recurrent" not in existing_markers:
                existing_markers.append("recurrent")
            recurrent_count += 1

        # Update row via delete+add (project pattern; LanceDB 0.30.x lacks robust update API
        # for list-typed columns -- see recanonicalize.py for the established convention).
        safe_id = chunk_id.replace("'", "''")
        original_row_snapshot = dict(row)
        new_row = {
            **original_row_snapshot,
            "corpus_derived_markers": existing_markers,
            "corpus_markers_computed_at": now_iso,
        }
        try:
            table.delete(f"chunk_id = '{safe_id}'")
            table.add([new_row])
        except Exception as exc:
            logger.error("lint_corpus row rewrite failed for %s: %s", chunk_id, exc)
            try:
                table.add([original_row_snapshot])
                logger.info(
                    "lint_corpus: restored original row for %s after rewrite failure",
                    chunk_id,
                )
            except Exception as restore_exc:
                logger.critical(
                    "lint_corpus CRITICAL: row %s LOST after rewrite failure (%s) AND "
                    "restore failure (%s). Source artifact at /data/output/<session>/ "
                    "is the recovery path.",
                    chunk_id, exc, restore_exc,
                )
            raise exc

    return {"scanned": len(rows), "recurrent": recurrent_count}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Populate corpus_derived_markers (recurrent) on chunks."
    )
    parser.add_argument("--db", default="/data/lancedb/nomic-v1")
    args = parser.parse_args()
    stats = lint_corpus_chunks(args.db)
    print(f"[ok] lint_corpus: scanned {stats['scanned']}, recurrent {stats['recurrent']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

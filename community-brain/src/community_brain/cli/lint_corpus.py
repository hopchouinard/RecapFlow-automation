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

    # MEDIUM mitigation: soft warning at large corpus sizes. KNN is O(N) per
    # chunk; at 10k+ chunks the auto-trigger adds non-trivial latency per /ingest.
    # Don't fail — just signal that the operator should consider moving lint to
    # a manual/cron schedule at that scale.
    if len(rows) > 10_000:
        logger.warning(
            "lint_corpus: scanning %d chunks; consider running this manually "
            "rather than as an /ingest auto-trigger at this scale",
            len(rows),
        )

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

        # HIGH 2 fix: track distinct session IDs, not neighbor-chunk count.
        # Two similar chunks from a single other session must not satisfy the
        # CROSS_SESSION_COUNT_MIN >= 2 threshold.
        cross_session_session_ids: set[str] = set()
        for nbr in results:
            if nbr["chunk_id"] == chunk_id:
                continue
            distance = nbr.get("_distance", 1.0)
            similarity = 1.0 - distance
            if similarity < SIMILARITY_THRESHOLD:
                continue
            if nbr["session_id"] != session_id:
                cross_session_session_ids.add(nbr["session_id"])

        existing_markers = list(row.get("corpus_derived_markers") or [])
        # Strip markers owned by lint_corpus before re-evaluating so that
        # stale markers are removed when the chunk no longer qualifies.
        # Currently lint owns 'recurrent'; add any future lint-owned markers here.
        LINT_OWNED_MARKERS = {"recurrent"}
        had_lint_markers = any(m in LINT_OWNED_MARKERS for m in existing_markers)
        existing_markers = [m for m in existing_markers if m not in LINT_OWNED_MARKERS]
        if len(cross_session_session_ids) >= CROSS_SESSION_COUNT_MIN:
            existing_markers.append("recurrent")
            recurrent_count += 1

        # Decide how to write back.
        #
        # LanceDB 0.30.x update() raises "concat requires input of at least one
        # array" when the new value for a list[str] column is an empty list [].
        # Two cases for the marker column:
        #
        #   A) existing_markers is non-empty: safe to call update() directly.
        #   B) existing_markers is empty AND the row previously had lint-owned
        #      markers: must CLEAR them. update() would choke on []; use
        #      row-rewrite (delete + add) as the fallback — same data-loss risk
        #      accepted in T11/recanonicalize, but bounded: only fires when
        #      clearing the LAST lint-owned marker.
        #   C) existing_markers is empty AND the row had no lint-owned markers:
        #      nothing to write for the marker column; update timestamp only.
        safe_id = chunk_id.replace("'", "''")
        needs_marker_clear = (not existing_markers) and had_lint_markers
        try:
            if needs_marker_clear:
                # Row-rewrite path: delete then add with cleared markers.
                snapshot = dict(row)
                snapshot["corpus_derived_markers"] = []
                snapshot["corpus_markers_computed_at"] = now_iso
                try:
                    table.delete(f"chunk_id = '{safe_id}'")
                    table.add([snapshot])
                except Exception as rewrite_exc:
                    # Attempt restore; if this also fails the row is lost — log loudly.
                    try:
                        table.add([dict(row)])
                        logger.error(
                            "lint_corpus marker clear failed for %s: %s — "
                            "row restored from snapshot",
                            chunk_id,
                            rewrite_exc,
                        )
                    except Exception as restore_exc:
                        logger.error(
                            "lint_corpus CRITICAL: marker clear AND restore failed "
                            "for %s: clear=%s restore=%s — row may be lost",
                            chunk_id,
                            rewrite_exc,
                            restore_exc,
                        )
                    raise rewrite_exc
            else:
                table.update(
                    where=f"chunk_id = '{safe_id}'",
                    values={"corpus_markers_computed_at": now_iso},
                )
                if existing_markers:
                    table.update(
                        where=f"chunk_id = '{safe_id}'",
                        values={"corpus_derived_markers": existing_markers},
                    )
        except Exception as exc:
            logger.error(
                "lint_corpus marker update failed for %s: %s — row unchanged",
                chunk_id,
                exc,
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

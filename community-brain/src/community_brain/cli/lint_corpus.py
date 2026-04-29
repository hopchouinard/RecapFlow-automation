"""lint_corpus CLI -- populate corpus_derived_markers on chunks.

For each chunk, find K-nearest neighbors in embedding space; flag as
'recurrent' if the neighbors include >= 2 from different sessions.

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §9.
T24 will auto-trigger this from /ingest at end of session commit.

Usage:
    python -m community_brain.cli.lint_corpus [--db /data/lancedb/nomic-v1]
    python -m community_brain.cli.lint_corpus [--db /path] --rebuild
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


def lint_corpus_chunks(db_path: str | Path, *, rebuild: bool = False) -> dict[str, int]:
    """Apply 'recurrent' markers across the corpus; set computed_at on every row.

    rebuild=False (default): additive-only. Adds 'recurrent' when a chunk
        qualifies. Skips stale-marker removal — uses table.update() exclusively
        so writes are atomic. Auto-triggered after /ingest. Logs a WARN when
        stale markers are found that would have been removed under rebuild=True.

    rebuild=True (manual): full recompute. Removes 'recurrent' from chunks
        that no longer qualify. Uses row-rewrite (delete+add with snapshot
        restore) for the empty-list case because LanceDB 0.30.x rejects
        empty list[str] values in update(). Run this manually after big
        corpus changes (re-extracts, threshold tweaks, session deletions).

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

    LINT_OWNED_MARKERS: set[str] = {"recurrent"}

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

        # Track distinct session IDs, not neighbor-chunk count.
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
        should_be_recurrent = len(cross_session_session_ids) >= CROSS_SESSION_COUNT_MIN
        currently_recurrent = "recurrent" in existing_markers

        safe_id = chunk_id.replace("'", "''")

        try:
            if should_be_recurrent and not currently_recurrent:
                # ADD path — safe atomic update; non-empty list so update() is fine.
                new_markers = existing_markers + ["recurrent"]
                table.update(
                    where=f"chunk_id = '{safe_id}'",
                    values={
                        "corpus_derived_markers": new_markers,
                        "corpus_markers_computed_at": now_iso,
                    },
                )
                recurrent_count += 1

            elif not should_be_recurrent and currently_recurrent:
                if rebuild:
                    # REMOVE path — destructive row-rewrite (rebuild=True, explicit operator action).
                    new_markers = [m for m in existing_markers if m not in LINT_OWNED_MARKERS]
                    if new_markers:
                        # Non-empty result: safe to update() directly.
                        table.update(
                            where=f"chunk_id = '{safe_id}'",
                            values={
                                "corpus_derived_markers": new_markers,
                                "corpus_markers_computed_at": now_iso,
                            },
                        )
                    else:
                        # Empty result — LanceDB 0.30.x rejects empty list[str] in update().
                        # Fall back to row-rewrite (delete + add) with snapshot restore.
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
                    # Auto-trigger (rebuild=False): skip removal, log WARN.
                    # Operator must run lint_corpus_chunks(rebuild=True) to clean up.
                    logger.warning(
                        "lint_corpus: chunk %s has stale 'recurrent' marker (no longer "
                        "qualifies); rebuild=False so leaving stale. Run "
                        "lint_corpus_chunks(rebuild=True) to clean up.",
                        chunk_id,
                    )

            elif should_be_recurrent:
                # Already recurrent and still qualifies — no-op for markers; bump timestamp.
                # Non-empty markers list so update() is safe.
                recurrent_count += 1
                table.update(
                    where=f"chunk_id = '{safe_id}'",
                    values={"corpus_markers_computed_at": now_iso},
                )

            else:
                # Doesn't qualify and isn't currently marked — bump timestamp only.
                # The timestamp column is string, not list[str], so update() is always
                # safe here even when corpus_derived_markers is [].
                table.update(
                    where=f"chunk_id = '{safe_id}'",
                    values={"corpus_markers_computed_at": now_iso},
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
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help=(
            "Recompute markers from scratch (destructive; uses row-rewrite "
            "for stale-marker cleanup). Default off — use after big corpus "
            "changes; auto-trigger from /ingest is always rebuild=False."
        ),
    )
    args = parser.parse_args()
    stats = lint_corpus_chunks(args.db, rebuild=args.rebuild)
    print(f"[ok] lint_corpus: scanned {stats['scanned']}, recurrent {stats['recurrent']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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
import os
from pathlib import Path
from typing import Any

import lancedb


logger = logging.getLogger(__name__)

K_NEAREST = 8
SIMILARITY_THRESHOLD = 0.65
CROSS_SESSION_COUNT_MIN = 2

# v5 D13: corpus-wide alarm threshold for has_unresolved_question=True.
# chunk-extraction-v3 deliberately defaults the flag toward true; healthy
# corpus rate observed ~27%. Above 50% the flag has stopped discriminating
# and the prompt has likely drifted over-permissive.
UNRESOLVED_RATE_ALARM_THRESHOLD = 0.50


def _now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def lint_corpus_chunks(db_path: str | Path, *, rebuild: bool = False) -> dict[str, Any]:
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

    Returns {"scanned": int, "recurrent": int, "unresolved_rate": float, "unresolved_alarm": bool}.
    """
    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    rows = table.to_arrow().to_pylist()
    now_iso = _now_iso()

    unresolved_count = sum(
        1 for r in rows if r.get("has_unresolved_question") is True
    )
    unresolved_rate = (unresolved_count / len(rows)) if rows else 0.0
    unresolved_alarm = unresolved_rate > UNRESOLVED_RATE_ALARM_THRESHOLD
    if unresolved_alarm:
        logger.warning(
            "lint_corpus: has_unresolved_question rate %.1f%% exceeds %.0f%% "
            "alarm threshold — the chunk-extraction prompt may be "
            "over-triggering; review before the next re-extract",
            unresolved_rate * 100,
            UNRESOLVED_RATE_ALARM_THRESHOLD * 100,
        )

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
                # Already correctly marked — count it but don't write.
                # corpus_markers_computed_at semantics tightened to "last meaningful
                # marker change" (spec 2026-05-02-ingest-lint-decoupling-design.md §7).
                recurrent_count += 1

            else:
                # Doesn't qualify and isn't currently marked — no-op, no write.
                pass

        except Exception as exc:
            logger.error(
                "lint_corpus marker update failed for %s: %s — row unchanged",
                chunk_id,
                exc,
            )
            raise exc

    return {
        "scanned": len(rows),
        "recurrent": recurrent_count,
        "unresolved_rate": unresolved_rate,
        "unresolved_alarm": unresolved_alarm,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Populate corpus_derived_markers (recurrent) on chunks."
    )
    # CLI convenience: read env var as fallback default so operators don't need
    # to pass --db explicitly when COMMUNITY_BRAIN_DB_PATH is set in the shell.
    # This is the only place the env var is consulted; lint_corpus_chunks() itself
    # treats its db_path parameter as authoritative and never reads the env var.
    _default_db = os.environ.get("COMMUNITY_BRAIN_DB_PATH") or "/data/lancedb/nomic-v1"
    parser.add_argument("--db", default=_default_db)
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
    print(
        f"[ok] lint_corpus: scanned {stats['scanned']}, "
        f"recurrent {stats['recurrent']}, "
        f"unresolved_rate {stats['unresolved_rate']:.1%}"
    )
    if stats["unresolved_alarm"]:
        print(
            "[ALARM] has_unresolved_question rate exceeds "
            f"{UNRESOLVED_RATE_ALARM_THRESHOLD:.0%} — extraction prompt may be "
            "over-triggering"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

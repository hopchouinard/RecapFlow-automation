"""FTS index lifecycle helpers for hybrid retrieval v3.

Three operations:
  - ensure_fts_index(table, column): idempotent. Creates an FTS index on the
    column if absent. Called at server boot so the first query never hits a
    missing index. Defaults to column="bm25_text" (v3).
  - optimize_fts_index(table, column): called after each /ingest commit.
    Production behavior depends on the spike outcome (Task 1):
      * auto-update: no-op
      * optimize required: table.optimize()
      * recreate required: table.create_fts_index(column, replace=True)
    Defaults to column="bm25_text" (v3).
  - drop_full_text_index_if_present(table): best-effort cleanup of the legacy
    v2 FTS index on the full_text column. Called at server boot on the v3
    migration path. Returns True if a drop was attempted, False otherwise.

All operations log their work at INFO/WARNING and never raise into callers
on routine path. Caller-side fallback (graceful degradation) lives in
search_chunks.
"""

from __future__ import annotations

import logging
import time

logger = logging.getLogger(__name__)


def has_fts_index(table, column: str) -> bool:
    """Return True if `table` has an FTS index on `column`.

    LanceDB exposes `list_indices()` which returns index metadata. The FTS
    indices have `index_type` containing "FTS" or "Inverted" depending on
    LanceDB version; we check both for forward compatibility.
    """
    try:
        indices = table.list_indices()
    except Exception as exc:
        logger.warning("table.list_indices() raised %r; assuming no FTS index", exc)
        return False
    for idx in indices:
        index_type = getattr(idx, "index_type", "") or ""
        columns = getattr(idx, "columns", []) or []
        if column in columns and ("FTS" in str(index_type).upper() or "INVERTED" in str(index_type).upper()):
            return True
    return False


def ensure_fts_index(table, column: str = "bm25_text") -> None:
    """Idempotent: create the FTS index on `column` if absent. Logs duration.

    "Idempotent" has to survive `has_fts_index` being wrong, because it is
    best-effort by construction: it swallows any `list_indices()` failure and
    returns False ("assuming no FTS index"). Every route that makes detection
    fail therefore arrives here and calls `create_fts_index` on a table that
    already has the index.

    That is not hypothetical. Measured on the n8n VM, 2026-08-02: lancedb
    client 0.30.2 enumerated ZERO indices on a table where client 0.34.0
    enumerated `bm25_text_idx`. The older client then tried to create it and
    LanceDB answered "Index name 'bm25_text_idx' already exists". The raise
    propagated through `verify_corpus_v3_state` and turned every /query into
    a 503 — a detection miss escalated into a hard outage of the endpoint.

    So an "already exists" error is treated as success: it *is* the
    postcondition this function promises. Deliberately NOT `replace=True` —
    that rebuilds a healthy index on every detection miss, which is expensive
    on a real corpus and destructive for no reason. Any other exception still
    propagates; an unbuildable table must still fail closed.
    """
    if has_fts_index(table, column):
        logger.debug("FTS index on column %r already present; skipping creation", column)
        return
    logger.info("FTS index on column %r absent; building...", column)
    t0 = time.monotonic()
    try:
        table.create_fts_index(column)
    except Exception as exc:
        if "already exists" in str(exc).lower():
            logger.warning(
                "FTS index on column %r was reported absent by has_fts_index but "
                "already exists on create; treating as present. This usually means "
                "the index was written by a different LanceDB client version than "
                "the one reading it.",
                column,
            )
            return
        raise
    logger.info("FTS index on column %r built in %.2fs", column, time.monotonic() - t0)


def optimize_fts_index(table, column: str = "bm25_text") -> None:
    """LanceDB FTS auto-includes rows added after index creation (verified
    by the spike, spec §11.1 Resolution: lancedb 0.30.x auto-update path).
    No-op.

    Kept as a callable function rather than removed because:
      - call sites (pipeline.py post-commit, future operator hooks) treat
        it as the canonical refresh API; the indirection lets us swap to
        table.optimize() or create_fts_index(..., replace=True) in one
        place if a future LanceDB version drops auto-update;
      - explicit "we considered this and chose no-op" reads better than
        the absence of any refresh hook would.
    """
    logger.debug("optimize_fts_index(%r): auto-update path; no-op", column)


def drop_full_text_index_if_present(table) -> bool:
    """Best-effort drop of any FTS index on the legacy full_text column.

    Returns True if a drop was attempted (regardless of success), False if
    the LanceDB version doesn't expose drop_index API or no such index
    exists. Logs at DEBUG; does not raise.

    Rationale: v3 migrates the FTS index to bm25_text. Old full_text
    indexes may linger from v2 deploys. Idempotent cleanup at boot.

    Per-deploy context (spec §17.1 step 3): the deploy procedure drops the
    chunks table entirely before v3 goes live, so this helper mostly handles
    already-absent indexes gracefully. It fires usefully only if someone
    deploys v3 against a non-fresh table (which the spec explicitly tells
    operators not to do).

    LanceDB 0.30.2 API note: table.drop_index() was not confirmed available
    in 0.30.2. If it's absent, this function returns False and logs DEBUG.
    The functional impact of leaving the legacy index in place is disk space
    only; it's not a correctness issue.
    """
    try:
        if not hasattr(table, "drop_index"):
            logger.debug(
                "LanceDB table.drop_index not available; skipping full_text cleanup"
            )
            return False
        # LanceDB names FTS indexes with a derived suffix; try both common forms.
        # The exact name depends on lancedb internals.
        for candidate in ("full_text_idx", "full_text_fts_idx"):
            try:
                table.drop_index(candidate)
                logger.info("dropped legacy FTS index %r on full_text", candidate)
                return True
            except Exception:
                continue  # try next candidate name
        logger.debug("no legacy full_text FTS index found to drop")
        return False
    except Exception as exc:
        logger.debug("drop_full_text_index_if_present failed: %s", exc)
        return False

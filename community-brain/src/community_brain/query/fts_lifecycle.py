"""FTS index lifecycle helpers for hybrid retrieval v2.

Two operations:
  - ensure_fts_index(table, column): idempotent. Creates an FTS index on the
    column if absent. Called at server boot so the first query never hits a
    missing index.
  - optimize_fts_index(table, column): called after each /ingest commit.
    Production behavior depends on the spike outcome (Task 1):
      * auto-update: no-op
      * optimize required: table.optimize()
      * recreate required: table.create_fts_index(column, replace=True)

Both operations log their work at INFO/WARNING and never raise into callers
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


def ensure_fts_index(table, column: str) -> None:
    """Idempotent: create the FTS index on `column` if absent. Logs duration."""
    if has_fts_index(table, column):
        logger.debug("FTS index on column %r already present; skipping creation", column)
        return
    logger.info("FTS index on column %r absent; building...", column)
    t0 = time.monotonic()
    table.create_fts_index(column)
    logger.info("FTS index on column %r built in %.2fs", column, time.monotonic() - t0)


def optimize_fts_index(table, column: str) -> None:
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

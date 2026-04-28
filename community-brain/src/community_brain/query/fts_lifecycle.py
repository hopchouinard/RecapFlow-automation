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
    """Refresh the FTS index after new rows are added.

    The exact mechanic was decided by the spike (Task 1, spec §11.1). Update
    the body of this function according to the recorded resolution:
      - auto-update: leave as no-op + debug log
      - optimize required: call table.optimize()
      - recreate required: call table.create_fts_index(column, replace=True)

    Failures are caught and logged at WARNING; chunks are already committed
    so a refresh failure is not fatal.
    """
    # IMPLEMENTATION NOTE for the engineer running this task:
    # Replace the body below with the path the spike (Task 1) verified.
    # Default is a no-op + warning so missing this step shows up loudly.
    logger.warning(
        "optimize_fts_index is a no-op until Task 8 wires the spike outcome. "
        "Spike resolution (spec §11.1): LanceDB 0.30.x auto-updates FTS on add; "
        "T8 will replace this body with a clean no-op + rationale."
    )

"""Holistic corpus-validity check for v3.

A v3 server must satisfy these invariants for correct retrieval:
1. chunks table either does not exist (fresh deploy) OR has v1.1 schema
2. if exists: schema includes bm25_text column
3. if exists: FTS index on bm25_text is present

Called from:
- retrieval_server lifespan startup hook (fail closed)
- _post_commit_maintenance (after ingest)
- /query path (pre-search check)

Distinguishes 'corpus invalid for v3' (refuse service, return 503) from
'transient runtime failure' (graceful degradation acceptable).

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §17.1
"""
from __future__ import annotations

from community_brain.query.fts_lifecycle import ensure_fts_index


class CorpusInvalidError(Exception):
    """Corpus is not in a valid v3 state. Refuse service."""


def verify_corpus_v3_state(table) -> None:
    """Raise CorpusInvalidError if the chunks table is not in a valid v3 state.

    No-op if the table is fresh (will be created on first ingest).
    Caller MUST handle the case where the table doesn't exist yet.

    Checks:
    1. bm25_text column is present (v1.1+ schema). If absent, the corpus
       predates v3 and must be dropped + re-ingested per spec §17.1.
    2. FTS index on bm25_text exists (via ensure_fts_index, which is
       idempotent — it will attempt to create it if absent). If it cannot
       be created, the table state is unbuildable; operator action required.
    """
    schema_names = set(table.schema.names)
    if "bm25_text" not in schema_names:
        raise CorpusInvalidError(
            "chunks table is pre-v1.1 (no bm25_text column). v3 server "
            "cannot serve this corpus. Drop the table per spec §17.1 and "
            "re-ingest, or roll back to v2 server."
        )
    # FTS index check — use ensure_fts_index since it's idempotent.
    # If it raises, the index is unbuildable on this table state.
    try:
        ensure_fts_index(table, column="bm25_text")
    except Exception as exc:
        raise CorpusInvalidError(
            f"chunks table has bm25_text column but FTS index cannot be "
            f"ensured: {exc}. Operator action required."
        ) from exc

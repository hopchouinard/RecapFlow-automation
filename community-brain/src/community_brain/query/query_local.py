"""Query helpers for Community Brain (v1 chunks-table search path).

Exposes the v2-suffixed search/filter helpers used by the retrieval server.
Both `_v2` symbols here are pending rename to canonical names in a follow-up
task; the suffix is intentionally retained for now to keep the rename diff
isolated.
"""

from __future__ import annotations

import logging

import lancedb
import ollama

from community_brain.ingestion.embedding import _active_embed_model

logger = logging.getLogger(__name__)

__all__ = [
    "search_chunks_v2",
    "build_filter_expression_v2",
    "sql_quote",
]


def sql_quote(value: str) -> str:
    """Escape a string for SQL single-quoted literal context.

    Doubles embedded single quotes per SQL-standard escaping.
    LanceDB's DataFusion parser accepts this.

    Note: this is ONLY safe for simple string values. For complex filter
    scenarios (e.g., structured JSON values), parameterized queries would
    be needed. All v1 filter values are simple string scalars, so this is
    sufficient.
    """
    return value.replace("'", "''")


def build_filter_expression_v2(filters: dict | None) -> str | None:
    """Build a LanceDB WHERE clause from the v2 filter dict.

    Semantics (per spec §7.1):
      - None or empty list → filter ignored
      - list-valued filters (entities, speakers_spoke, speakers_mentioned,
        keywords) use `_match` companion: "any" → OR, "all" → AND
      - require_chunk_markers / require_corpus_markers → AND of array_has
      - exclude_chunk_markers / exclude_corpus_markers → AND of NOT array_has
      - has_* and references_prior → bool equality when not None
      - schema_version_min → >= lexicographic comparison

    Returns None if no filter clauses apply.

    All string values are escaped via sql_quote to handle apostrophes and other
    special characters safely (SQL-standard double-quote escaping).
    """
    if not filters:
        return None

    clauses: list[str] = []

    dr = filters.get("session_date_range")
    if dr and len(dr) == 2:
        clauses.append(
            f"session_date >= '{sql_quote(dr[0])}' AND session_date <= '{sql_quote(dr[1])}'"
        )

    content_types = filters.get("content_type")
    if content_types:
        quoted = ", ".join(f"'{sql_quote(v)}'" for v in content_types)
        clauses.append(f"content_type IN ({quoted})")

    for field_name in ("speakers_spoke", "speakers_mentioned", "entities", "keywords"):
        vals = filters.get(field_name)
        if not vals:
            continue
        match = filters.get(f"{field_name}_match", "any")
        parts = [f"array_has({field_name}, '{sql_quote(v)}')" for v in vals]
        joiner = " AND " if match == "all" else " OR "
        clauses.append("(" + joiner.join(parts) + ")")

    for marker_field, key in (
        ("chunk_local_markers", "require_chunk_markers"),
        ("corpus_derived_markers", "require_corpus_markers"),
    ):
        vals = filters.get(key)
        if vals:
            parts = [f"array_has({marker_field}, '{sql_quote(v)}')" for v in vals]
            clauses.append("(" + " AND ".join(parts) + ")")

    for marker_field, key in (
        ("chunk_local_markers", "exclude_chunk_markers"),
        ("corpus_derived_markers", "exclude_corpus_markers"),
    ):
        vals = filters.get(key)
        if vals:
            parts = [f"NOT array_has({marker_field}, '{sql_quote(v)}')" for v in vals]
            clauses.append("(" + " AND ".join(parts) + ")")

    for bool_field in (
        "has_question", "has_answer", "has_unresolved_question",
        "has_insight", "references_prior",
    ):
        v = filters.get(bool_field)
        if v is not None:
            clauses.append(f"{bool_field} = {'true' if v else 'false'}")

    ver_min = filters.get("schema_version_min")
    if ver_min:
        clauses.append(f"schema_version >= '{sql_quote(ver_min)}'")

    if not clauses:
        return None
    return " AND ".join(clauses)


def search_chunks_v2(
    question: str,
    db_path: str,
    top_k: int,
    filters: dict | None,
    ollama_base_url: str | None = None,
    table_name: str = "chunks",
) -> list[dict]:
    """Filter-then-rank v2 search against the new chunks table.

    Applies `build_filter_expression_v2(filters)` as a LanceDB WHERE clause
    first, then ranks the filtered rows by vector similarity to the embedded
    question. Per spec §7.1: filtering precedes ranking; ranking uses vector
    similarity alone in v1.

    Returns empty list if the table doesn't exist yet (fresh deployment).

    Returns raw LanceDB row dicts (including `_distance`). The retrieval server
    translates these into the structured ground_truth/derived_metadata/provenance
    response shape.
    """
    db = lancedb.connect(db_path)
    if table_name not in db.list_tables().tables:
        return []

    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=_active_embed_model(), input=[question])
    else:
        response = ollama.embed(model=_active_embed_model(), input=[question])
    query_vector = response["embeddings"][0]

    table = db.open_table(table_name)
    query = table.search(query_vector).limit(top_k)

    # Failed-extraction chunks carry a zero-vector embedding and must be
    # excluded from vector search. AND the user filter with the status guard.
    user_expr = build_filter_expression_v2(filters)
    status_guard = "extraction_status = 'success'"
    expr = f"({user_expr}) AND {status_guard}" if user_expr else status_guard
    query = query.where(expr)

    results = query.to_arrow()
    return [
        {col: results[col][i].as_py() for col in results.column_names}
        for i in range(results.num_rows)
    ]

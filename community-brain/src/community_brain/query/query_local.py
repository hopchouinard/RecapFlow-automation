"""Query helpers for Community Brain (v1 chunks-table search path).

Exposes the search/filter helpers used by the retrieval server.
"""

from __future__ import annotations

import logging
import os

import lancedb
import ollama

from community_brain.ingestion.embedding import _active_embed_model
from community_brain.query.corpus_verify import CorpusInvalidError
from community_brain.query.cue_rules import (
    CueRule,
    apply_cue_boosts,
    build_speaker_auto_rule,
    load_cue_rules_from_yaml,
)

logger = logging.getLogger(__name__)

# Hybrid retrieval oversampling factor (spec §3.1): the LanceDB hybrid query
# returns top_k * OVERSAMPLE_FACTOR raw candidates so the downstream cue-boost
# step (T10) has headroom to re-rank before truncating to top_k.
OVERSAMPLE_FACTOR = 3

# Default path for the cue-rules YAML inside the container (spec §12.4).
# Overridable via COMMUNITY_BRAIN_CUE_RULES_PATH env var at call time.
CUE_RULES_PATH_DEFAULT = "/app/config/query-cues.yaml"

# Default path for the speaker-aliases YAML inside the container.
# Overridable via COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH at call time.
SPEAKER_ALIASES_PATH_DEFAULT = "/app/config/speaker-aliases.yaml"


def _resolve_cue_rules() -> tuple[CueRule, ...]:
    """Load cue rules from YAML at call time and merge with the
    in-memory speaker auto-rule synthesized from speaker-aliases.yaml.
    Both paths are overridable via env vars at call time. Falls back to
    empty tuples if files are missing/malformed.
    """
    cue_path = os.environ.get("COMMUNITY_BRAIN_CUE_RULES_PATH") or CUE_RULES_PATH_DEFAULT
    yaml_rules = load_cue_rules_from_yaml(cue_path)

    aliases_path = (
        os.environ.get("COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH")
        or SPEAKER_ALIASES_PATH_DEFAULT
    )
    speaker_rules = build_speaker_auto_rule(aliases_path)  # tuple of 2

    return tuple(yaml_rules) + speaker_rules

__all__ = [
    "search_chunks",
    "build_filter_expression",
    "sql_quote",
]


def _cosine_distance(a: list[float], b: list[float]) -> float:
    """Cosine distance between two equal-length vectors. Range [0, 2].

    Used to populate `_distance` on hybrid-query results — LanceDB's hybrid
    mode returns `_relevance_score` (the RRF score) but no `_distance`.
    Spec §7.2 requires the public `similarity` field (computed downstream
    as `1 - _distance` in retrieval_server) to reflect vector cosine
    similarity, not the internal RRF/cue-boost score.
    """
    import math
    dot = 0.0
    norm_a = 0.0
    norm_b = 0.0
    for x, y in zip(a, b):
        dot += x * y
        norm_a += x * x
        norm_b += y * y
    if norm_a == 0.0 or norm_b == 0.0:
        return 1.0
    return 1.0 - dot / (math.sqrt(norm_a) * math.sqrt(norm_b))


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


def build_filter_expression(filters: dict | None) -> str | None:
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


def _compute_metadata_summary(top_k_chunks: list[dict]) -> dict:
    """Authoritative aggregate counts of boolean derived flags across the
    retrieved chunks. Used by the answering LLM (Finding 8 fix path c).
    """
    flag_fields = (
        "has_question",
        "has_answer",
        "has_unresolved_question",
        "has_insight",
        "references_prior",
    )
    summary: dict[str, int] = {"of_top_k": len(top_k_chunks)}
    for f in flag_fields:
        count = sum(1 for c in top_k_chunks if c.get(f) is True)
        summary[f"{f}_count"] = count
    return summary


def search_chunks(
    question: str,
    db_path: str,
    top_k: int,
    filters: dict | None,
    ollama_base_url: str | None = None,
    table_name: str = "chunks",
    _use_hybrid: bool = True,
) -> dict:
    """Hybrid (vector + BM25) search against the chunks table with optional
    structured filters and the success-guard.

    Pipeline (spec §3.1):
      1. Embed `question` via Ollama (nomic-embed-text).
      2. LanceDB hybrid query: RRF(vector, BM25 on bm25_text), oversampled
         by OVERSAMPLE_FACTOR.
      3. WHERE clause: extraction_status = 'success' AND caller's filters.
      4. Return top (top_k * OVERSAMPLE_FACTOR) raw rows; cue boost runs
         downstream in the caller (T10 wires that in).

    `_use_hybrid=False` is a test-only knob that drops the BM25 leg —
    used by the lift-validation tests in the golden query suite to prove
    the hybrid pathway is what surfaces the missing chunks.
    """
    db = lancedb.connect(db_path)
    if table_name not in db.list_tables().tables:
        return {"chunks": [], "metadata_summary": _compute_metadata_summary([])}
    table = db.open_table(table_name)

    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=_active_embed_model(), input=[question])
    else:
        response = ollama.embed(model=_active_embed_model(), input=[question])
    query_vector = response["embeddings"][0]

    user_expr = build_filter_expression(filters)
    status_guard = "extraction_status = 'success'"
    where_expr = f"({user_expr}) AND {status_guard}" if user_expr else status_guard

    candidate_count = top_k * OVERSAMPLE_FACTOR

    if _use_hybrid:
        try:
            # LanceDB 0.30.x hybrid API: explicit builder form. Passing the
            # vector positionally to .search() while also calling .text(...)
            # raises ValueError. See spec §11.1 Resolution side note.
            # fts_columns pins the lexical leg to bm25_text; without this,
            # LanceDB may fall back to a legacy full_text FTS index that
            # drop_full_text_index_if_present can't always clean up.
            query = (
                table.search(query_type="hybrid", fts_columns="bm25_text")
                .vector(query_vector)
                .text(question)
                .where(where_expr)
                .limit(candidate_count)
            )
            results = query.to_arrow()
        except Exception as exc:
            # Runtime hybrid-search failure after verify_corpus_v3_state passed
            # at /query entry means the corpus is in an unexpected bad state
            # (corrupt index, fts_columns incompatibility, persistent FTS
            # execution error). Don't silently degrade to vector-only — fail
            # loud per the convergent refactor's principle. Operator must
            # investigate. If a narrowly-scoped transient failure mode is
            # observed in production later, add it back with a typed exception
            # check; do NOT revert to a catch-all.
            raise CorpusInvalidError(
                f"hybrid search failed at runtime despite passing corpus "
                f"verification: {exc}. Corpus may have a corrupt FTS index or "
                f"other state issue."
            ) from exc
    else:
        query = (
            table.search(query_vector)
            .where(where_expr)
            .limit(candidate_count)
        )
        results = query.to_arrow()

    candidates: list[dict] = []
    for i in range(results.num_rows):
        row = {col: results[col][i].as_py() for col in results.column_names}
        # LanceDB hybrid mode emits _relevance_score (RRF) but no _distance.
        # Vector-only fallback emits _distance (cosine) but no _relevance_score.
        # Normalize:
        #   - _rrf_score: the internal ranking signal the cue-boost layer reads.
        #   - _distance:  vector cosine distance, preserved per spec §7.2 so
        #                 retrieval_server's `similarity = 1 - _distance` keeps
        #                 the v1 numeric scale (~0.3–0.8 cosine similarity).
        if "_relevance_score" in row:
            row["_rrf_score"] = float(row["_relevance_score"])
            embedding = row.get("embedding")
            if embedding:
                row["_distance"] = _cosine_distance(query_vector, list(embedding))
            else:
                # No embedding column projected; let downstream similarity
                # default to 1.0 (1 - 0). Better than fabricating a value.
                row["_distance"] = 0.0
        else:
            # Vector-only fallback path: _distance is already present from LanceDB.
            row["_rrf_score"] = 1.0 - float(row.get("_distance", 0.0))
        # Derive vector_similarity from the cosine distance computed above.
        # Range: [0.0, 1.0]; higher = more similar.
        row["_vector_similarity"] = 1.0 - float(row.get("_distance", 0.0))
        candidates.append(row)

    # BM25-only query to capture per-candidate rank in the lexical leg.
    # This is a separate lightweight query — just FTS, no vector component —
    # so we can assign a 1-indexed rank to each candidate. ~10-20ms overhead
    # at current corpus size (acceptable per spec §15). Candidates that don't
    # appear in the BM25 result got here purely via the vector leg; their
    # bm25_rank will be None.
    # fts_columns pins the lexical leg to bm25_text (same rationale as the
    # hybrid search above). Limit is max(top_k * 10, 1000): generous enough
    # that bm25_rank=None reliably means "vector-only" or "outside top-1000
    # BM25 results" (rare at current corpus size). See ScoreBreakdown docstring.
    try:
        bm25_limit = max(top_k * 10, 1000)
        bm25_results = (
            table.search(question, query_type="fts", fts_columns="bm25_text")
            .where(where_expr)
            .limit(bm25_limit)
            .to_arrow()
            .to_pylist()
        )
        bm25_rank_by_id: dict[str, int] = {
            row["chunk_id"]: idx + 1
            for idx, row in enumerate(bm25_results)
        }
    except Exception as exc:
        # Transient: the BM25 rank query is a secondary scoring annotation, not
        # the primary result set. Its failure means score_breakdown.bm25_rank will
        # be None for all chunks, but ranking and retrieval remain correct via the
        # hybrid query's RRF output. Not an invariant violation.
        logger.warning("BM25 rank query failed (%r); bm25_rank will be None for all chunks", exc)
        bm25_rank_by_id = {}

    for chunk in candidates:
        chunk["_bm25_rank"] = bm25_rank_by_id.get(chunk.get("chunk_id", ""))

    # Snapshot RRF score before cue boost so score_breakdown can report
    # the pre-boost value separately from the final ranking signal.
    for chunk in candidates:
        chunk["_rrf_score_pre_boost"] = chunk.get("_rrf_score", 0.0)

    rules = _resolve_cue_rules()
    boosted = apply_cue_boosts(question, candidates, rules=rules)

    top_k_chunks = boosted[:top_k]

    # Build per-chunk score_breakdown dict from the tracked accumulators.
    # The underscored fields (_vector_similarity etc.) are kept on the chunk
    # for debugging; score_breakdown is the public surface.
    for chunk in top_k_chunks:
        chunk["score_breakdown"] = {
            "vector_similarity": chunk.get("_vector_similarity", 0.0),
            "bm25_rank": chunk.get("_bm25_rank"),
            "rrf_score": chunk.get("_rrf_score_pre_boost", 0.0),
            "cue_delta": chunk.get("_cue_delta", 0.0),
            "cue_rules_fired": chunk.get("_cue_rules_fired", []),
        }

    # IMPORTANT: do NOT re-sync _distance from _rrf_score here.
    # _distance reflects vector cosine similarity (spec §7.2); cue boost
    # only changes ranking via _rrf_score, not the surface similarity field.
    metadata_summary = _compute_metadata_summary(top_k_chunks)
    return {
        "chunks": top_k_chunks,
        "metadata_summary": metadata_summary,
    }

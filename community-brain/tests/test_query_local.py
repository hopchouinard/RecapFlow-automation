"""Tests for build_filter_expression — pure logic, no LanceDB."""

from __future__ import annotations

from community_brain.query.query_local import build_filter_expression, sql_quote


def test_build_filter_expression_empty_returns_none() -> None:
    assert build_filter_expression(None) is None
    assert build_filter_expression({}) is None


def test_build_filter_expression_date_range() -> None:
    expr = build_filter_expression({
        "session_date_range": ["2025-01-01", "2026-04-18"],
    })
    assert expr is not None
    assert "session_date >= '2025-01-01'" in expr
    assert "session_date <= '2026-04-18'" in expr


def test_build_filter_expression_content_type_list() -> None:
    expr = build_filter_expression({"content_type": ["prepared_transcript"]})
    assert expr is not None
    assert "content_type IN ('prepared_transcript')" in expr


def test_build_filter_expression_entities_any_match() -> None:
    expr = build_filter_expression({
        "entities": ["LangGraph", "Codex"],
        "entities_match": "any",
    })
    assert expr is not None
    # "any" uses OR between array_has checks
    assert "OR" in expr
    assert "array_has(entities, 'LangGraph')" in expr
    assert "array_has(entities, 'Codex')" in expr


def test_build_filter_expression_entities_all_match() -> None:
    expr = build_filter_expression({
        "entities": ["LangGraph", "Codex"],
        "entities_match": "all",
    })
    assert expr is not None
    assert "AND" in expr
    assert "array_has(entities, 'LangGraph')" in expr
    assert "array_has(entities, 'Codex')" in expr


def test_build_filter_expression_empty_list_is_ignored() -> None:
    """Empty list filter should be a no-op (like None)."""
    expr = build_filter_expression({"entities": []})
    assert expr is None


def test_build_filter_expression_require_chunk_markers() -> None:
    expr = build_filter_expression({
        "require_chunk_markers": ["emphasized", "sustained"],
    })
    assert expr is not None
    # require = all markers must be present (AND semantics)
    assert "array_has(chunk_local_markers, 'emphasized')" in expr
    assert "array_has(chunk_local_markers, 'sustained')" in expr
    assert "AND" in expr


def test_build_filter_expression_exclude_chunk_markers() -> None:
    expr = build_filter_expression({
        "exclude_chunk_markers": ["emphasized"],
    })
    assert expr is not None
    assert "NOT array_has(chunk_local_markers, 'emphasized')" in expr


def test_build_filter_expression_bool_fields() -> None:
    expr = build_filter_expression({
        "has_question": True,
        "has_unresolved_question": False,
    })
    assert expr is not None
    assert "has_question = true" in expr
    assert "has_unresolved_question = false" in expr


def test_build_filter_expression_bool_none_is_ignored() -> None:
    expr = build_filter_expression({
        "has_question": None,
    })
    assert expr is None


def test_build_filter_expression_schema_version_min() -> None:
    expr = build_filter_expression({"schema_version_min": "1.0"})
    assert expr is not None
    assert "schema_version >= '1.0'" in expr


def test_build_filter_expression_combines_with_and() -> None:
    """Multiple filter kinds are combined with AND."""
    expr = build_filter_expression({
        "content_type": ["prepared_transcript"],
        "has_insight": True,
    })
    assert expr is not None
    assert " AND " in expr


def test_sql_quote_doubles_single_quotes() -> None:
    """sql_quote must escape embedded single quotes by doubling them."""
    assert sql_quote("O'Brien") == "O''Brien"
    assert sql_quote("no apostrophe") == "no apostrophe"
    assert sql_quote("it's it's") == "it''s it''s"
    assert sql_quote("") == ""


def test_build_filter_expression_escapes_apostrophes_in_entity_names() -> None:
    """Speakers/entities with apostrophes must not break the generated WHERE clause."""
    expr = build_filter_expression({"speakers_spoke": ["O'Brien"]})
    assert expr is not None
    assert "O''Brien" in expr


def test_build_filter_expression_escapes_apostrophes_in_content_type() -> None:
    expr = build_filter_expression({"content_type": ["it's_weird"]})
    assert expr is not None
    assert "it''s_weird" in expr


def test_query_local_uses_shared_active_embed_model() -> None:
    """query_local must delegate to ingestion.embedding._active_embed_model
    so a single env var controls both ingest and query sides."""
    import community_brain.query.query_local as ql
    from community_brain.ingestion import embedding as emb

    # The function object is the same — not redefined locally
    assert ql._active_embed_model is emb._active_embed_model

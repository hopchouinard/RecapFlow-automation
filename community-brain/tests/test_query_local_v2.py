"""Tests for build_filter_expression_v2 — pure logic, no LanceDB."""

from __future__ import annotations

from community_brain.query.query_local import build_filter_expression_v2


def test_build_filter_expression_v2_empty_returns_none() -> None:
    assert build_filter_expression_v2(None) is None
    assert build_filter_expression_v2({}) is None


def test_build_filter_expression_v2_date_range() -> None:
    expr = build_filter_expression_v2({
        "session_date_range": ["2025-01-01", "2026-04-18"],
    })
    assert expr is not None
    assert "session_date >= '2025-01-01'" in expr
    assert "session_date <= '2026-04-18'" in expr


def test_build_filter_expression_v2_content_type_list() -> None:
    expr = build_filter_expression_v2({"content_type": ["prepared_transcript"]})
    assert expr is not None
    assert "content_type IN ('prepared_transcript')" in expr


def test_build_filter_expression_v2_entities_any_match() -> None:
    expr = build_filter_expression_v2({
        "entities": ["LangGraph", "Codex"],
        "entities_match": "any",
    })
    assert expr is not None
    # "any" uses OR between array_has checks
    assert "OR" in expr
    assert "array_has(entities, 'LangGraph')" in expr
    assert "array_has(entities, 'Codex')" in expr


def test_build_filter_expression_v2_entities_all_match() -> None:
    expr = build_filter_expression_v2({
        "entities": ["LangGraph", "Codex"],
        "entities_match": "all",
    })
    assert expr is not None
    assert "AND" in expr
    assert "array_has(entities, 'LangGraph')" in expr
    assert "array_has(entities, 'Codex')" in expr


def test_build_filter_expression_v2_empty_list_is_ignored() -> None:
    """Empty list filter should be a no-op (like None)."""
    expr = build_filter_expression_v2({"entities": []})
    assert expr is None


def test_build_filter_expression_v2_require_chunk_markers() -> None:
    expr = build_filter_expression_v2({
        "require_chunk_markers": ["emphasized", "sustained"],
    })
    assert expr is not None
    # require = all markers must be present (AND semantics)
    assert "array_has(chunk_local_markers, 'emphasized')" in expr
    assert "array_has(chunk_local_markers, 'sustained')" in expr
    assert "AND" in expr


def test_build_filter_expression_v2_exclude_chunk_markers() -> None:
    expr = build_filter_expression_v2({
        "exclude_chunk_markers": ["emphasized"],
    })
    assert expr is not None
    assert "NOT array_has(chunk_local_markers, 'emphasized')" in expr


def test_build_filter_expression_v2_bool_fields() -> None:
    expr = build_filter_expression_v2({
        "has_question": True,
        "has_unresolved_question": False,
    })
    assert expr is not None
    assert "has_question = true" in expr
    assert "has_unresolved_question = false" in expr


def test_build_filter_expression_v2_bool_none_is_ignored() -> None:
    expr = build_filter_expression_v2({
        "has_question": None,
    })
    assert expr is None


def test_build_filter_expression_v2_schema_version_min() -> None:
    expr = build_filter_expression_v2({"schema_version_min": "1.0"})
    assert expr is not None
    assert "schema_version >= '1.0'" in expr


def test_build_filter_expression_v2_combines_with_and() -> None:
    """Multiple filter kinds are combined with AND."""
    expr = build_filter_expression_v2({
        "content_type": ["prepared_transcript"],
        "has_insight": True,
    })
    assert expr is not None
    assert " AND " in expr

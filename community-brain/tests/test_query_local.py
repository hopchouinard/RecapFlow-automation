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


def test_search_chunks_uses_yaml_cue_rules(monkeypatch, tmp_path):
    """search_chunks should load cue rules from a YAML at the configured path on each call.

    COMMUNITY_BRAIN_CUE_RULES_PATH env var overrides the default path.
    The merged result also includes 2 speaker auto-rules synthesized from
    speaker-aliases.yaml; when that file is missing, both sentinel rules
    use a never-match regex so they're inert at /query time.
    """
    yaml_path = tmp_path / "query-cues.yaml"
    yaml_path.write_text("""
cue_rules:
  - name: r
    cue_phrases: [unresolved]
    target_predicate: {field: has_unresolved_question, value: true}
    delta: 0.010
""")
    monkeypatch.setenv("COMMUNITY_BRAIN_CUE_RULES_PATH", str(yaml_path))
    monkeypatch.setenv(
        "COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH", str(tmp_path / "missing-aliases.yaml")
    )

    import community_brain.query.query_local as query_local

    rules = query_local._resolve_cue_rules()
    # YAML rule + 2 speaker auto-rules (sentinel never-match regex when registry empty)
    assert len(rules) == 3
    yaml_rule_names = [r.name for r in rules if r.match_strategy is None]
    assert yaml_rule_names == ["r"]
    speaker_rule_names = sorted(r.name for r in rules if r.match_strategy is not None)
    assert speaker_rule_names == ["speaker_auto_mentioned", "speaker_auto_spoke"]


def test_yaml_cue_rules_path_default_when_env_unset(monkeypatch, tmp_path):
    """Without COMMUNITY_BRAIN_CUE_RULES_PATH, the default path is used.
    With a missing default file, the YAML rule set is empty (loader's
    graceful-degradation contract from T13). The merged result still
    contains the 2 speaker auto-rule sentinels.
    """
    monkeypatch.delenv("COMMUNITY_BRAIN_CUE_RULES_PATH", raising=False)
    monkeypatch.setenv(
        "COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH", str(tmp_path / "missing-aliases.yaml")
    )

    import community_brain.query.query_local as query_local

    monkeypatch.setattr(
        query_local,
        "CUE_RULES_PATH_DEFAULT",
        str(tmp_path / "missing.yaml"),
        raising=False,
    )
    rules = query_local._resolve_cue_rules()
    # No YAML rules, but the two never-match speaker sentinels are always returned.
    yaml_rules = tuple(r for r in rules if r.match_strategy is None)
    assert yaml_rules == ()
    speaker_rule_names = sorted(r.name for r in rules if r.match_strategy is not None)
    assert speaker_rule_names == ["speaker_auto_mentioned", "speaker_auto_spoke"]

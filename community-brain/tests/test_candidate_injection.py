"""v5 cue-driven candidate injection: recruitment-query derivation (design D4)."""
from __future__ import annotations

from community_brain.query.candidate_injection import (
    RecruitmentSpec,
    build_recruitment_query,
)
from community_brain.query.cue_rules import CueRule, build_speaker_auto_rule

ISO_RULE = CueRule(
    name="date_iso_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
    match_field="session_date", match_strategy="iso_date_equals", recruit=True,
)

MONTH_RULE = CueRule(
    name="date_month_year_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
    match_field="session_date", match_strategy="month_year_overlap", recruit=True,
)

QUARTER_RULE = CueRule(
    name="date_quarter_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(Q[1-4])\s+(\d{4})\b",
    match_field="bm25_text", match_strategy="token_overlap", recruit=True,
)

LEGACY_BOOL_RULE = CueRule(
    name="unresolved_questions", cue_phrases=("unresolved",), target_predicate=None,
    delta=0.04, recruit=True,
    predicate_spec={"field": "has_unresolved_question", "value": True},
)

LEGACY_NON_EMPTY_RULE = CueRule(
    name="decisions", cue_phrases=("decision",), target_predicate=None,
    delta=0.008, recruit=True,
    predicate_spec={"field": "decisions", "check": "non_empty"},
)

ALIASES_YAML = """
aliases:
  Adam James:
    - Adam
"""


def test_non_recruit_rule_returns_none():
    rule = CueRule(
        name="x", cue_phrases=(), target_predicate=None, delta=0.04,
        question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
        match_field="session_date", match_strategy="iso_date_equals", recruit=False,
    )
    assert build_recruitment_query(rule, "what happened on 2025-12-30?") is None


def test_iso_date_rule_derives_equality_where():
    spec = build_recruitment_query(ISO_RULE, "What was discussed on 2025-12-30?")
    assert spec == RecruitmentSpec(
        rule_name="date_iso_match",
        where="session_date = '2025-12-30'",
        fts_text=None,
    )


def test_iso_date_rule_none_when_question_has_no_date():
    assert build_recruitment_query(ISO_RULE, "What did Adam say?") is None


def test_month_year_rule_derives_range_where():
    spec = build_recruitment_query(MONTH_RULE, "What happened in December 2025?")
    assert spec is not None
    assert spec.where == (
        "session_date >= '2025-12-01' AND session_date <= '2025-12-31'"
    )
    assert spec.fts_text is None


def test_token_overlap_rule_recruits_via_fts_token():
    spec = build_recruitment_query(QUARTER_RULE, "themes in Q1 2026 calls?")
    assert spec is not None
    assert spec.where is None
    assert spec.fts_text == "Q1-2026"


def test_speaker_rule_derives_array_has_where(tmp_path):
    p = tmp_path / "speaker-aliases.yaml"
    p.write_text(ALIASES_YAML)
    spoke, _mentioned = build_speaker_auto_rule(p)
    spec = build_recruitment_query(spoke, "What did Adam say about pricing?")
    assert spec is not None
    assert spec.where == (
        "(array_has(speakers_spoke, 'Adam') OR array_has(speakers_spoke, 'Adam James'))"
    )


def test_legacy_bool_predicate_derives_equality_where():
    spec = build_recruitment_query(LEGACY_BOOL_RULE, "what stayed unresolved?")
    assert spec is not None
    assert spec.where == "has_unresolved_question = true"
    assert spec.fts_text is None


def test_legacy_bool_rule_none_when_no_phrase_match():
    assert build_recruitment_query(LEGACY_BOOL_RULE, "what was decided?") is None


def test_legacy_non_empty_predicate_is_not_recruitable():
    assert build_recruitment_query(LEGACY_NON_EMPTY_RULE, "what decisions happened?") is None


def test_where_values_are_sql_quoted():
    rule = CueRule(
        name="q", cue_phrases=("about",), target_predicate=None, delta=0.01,
        recruit=True, predicate_spec={"field": "stance", "value": "o'brien"},
    )
    spec = build_recruitment_query(rule, "tell me about stances")
    assert spec is not None
    assert spec.where == "stance = 'o''brien'"


# ---------------------------------------------------------------------------
# inject_candidates (real LanceDB, tmp_path storage — never mocked)
# ---------------------------------------------------------------------------
import datetime as dt

import lancedb

from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema
from community_brain.query.candidate_injection import (
    INJECT_PER_RULE,
    MAX_INJECTED_TOTAL,
    inject_candidates,
)
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index


def _chunk_row(
    *,
    chunk_id: str,
    session_date: str,
    full_text: str = "generic content",
    bm25_text: str = "generic content",
    extraction_status: str = "success",
    has_unresolved_question: bool = False,
    speakers_spoke: list[str] | None = None,
    embedding: list[float] | None = None,
) -> dict:
    return {
        "schema_version": "1.1",
        "chunk_id": chunk_id,
        "session_id": session_date,
        "session_date": session_date,
        "session_title": None,
        "content_type": "prepared_transcript",
        "source_file": "test.md",
        "chunk_index": 0,
        "total_chunks_in_source": 1,
        "speakers_spoke": speakers_spoke or [],
        "speakers_mentioned": [],
        "entities": [],
        "keywords": [],
        "topic_label": "t",
        "session_themes": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "corpus_derived_markers": [],
        "corpus_markers_computed_at": None,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": has_unresolved_question,
        "has_insight": False,
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "extraction_model": "test-model",
        "extraction_prompt_version": "chunk-extraction-v3",
        "extraction_status": extraction_status,
        "extraction_error": None,
        "extracted_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "embed_text": "x",
        "full_text": full_text,
        "bm25_text": bm25_text,
        "embedding": embedding if embedding is not None else [0.1] * EMBEDDING_DIM,
    }


def _make_table(tmp_path, rows):
    db = lancedb.connect(str(tmp_path / "db"))
    table = db.create_table("chunks", schema=pyarrow_table_schema())
    table.add(rows)
    ensure_fts_index(table, "bm25_text")
    optimize_fts_index(table, "bm25_text")
    return table


SUCCESS_GUARD = "extraction_status = 'success'"
QUERY_VEC = [0.5] * EMBEDDING_DIM


def test_inject_recruits_quiet_session_by_iso_date(tmp_path):
    rows = [
        _chunk_row(chunk_id="q1", session_date="2025-12-30",
                   full_text="holiday call check-ins",
                   bm25_text="holiday call check-ins"),
        _chunk_row(chunk_id="q2", session_date="2025-12-30",
                   full_text="year wrap-up thread",
                   bm25_text="year wrap-up thread"),
        _chunk_row(chunk_id="other", session_date="2026-01-07"),
    ]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30?",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    ids = sorted(r["chunk_id"] for r in injected)
    assert ids == ["q1", "q2"]
    for r in injected:
        assert r["_rrf_score"] == 0.0
        assert r["_injected_by"] == ["date_iso_match"]
        assert "_distance" in r
        assert "_vector_similarity" in r


def test_inject_excludes_failed_extractions(tmp_path):
    rows = [
        _chunk_row(chunk_id="ok", session_date="2025-12-30"),
        _chunk_row(chunk_id="bad", session_date="2025-12-30",
                   extraction_status="failed"),
    ]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30?",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    assert [r["chunk_id"] for r in injected] == ["ok"]


def test_inject_dedups_against_existing_pool(tmp_path):
    rows = [
        _chunk_row(chunk_id="q1", session_date="2025-12-30"),
        _chunk_row(chunk_id="q2", session_date="2025-12-30"),
    ]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30?",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids={"q1"},
        query_vector=QUERY_VEC,
    )
    assert [r["chunk_id"] for r in injected] == ["q2"]


def test_inject_accumulates_rule_names_on_shared_recruit(tmp_path):
    month_and_iso = (ISO_RULE, MONTH_RULE)
    rows = [_chunk_row(chunk_id="q1", session_date="2025-12-30")]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30, in December 2025?",
        table=table,
        rules=month_and_iso,
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    assert len(injected) == 1
    assert injected[0]["_injected_by"] == ["date_iso_match", "date_month_year_match"]


def test_inject_respects_per_rule_budget(tmp_path):
    rows = [
        _chunk_row(chunk_id=f"c{i:02d}", session_date="2025-12-30")
        for i in range(MAX_INJECTED_TOTAL + 10)
    ]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30?",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    assert 0 < len(injected) <= INJECT_PER_RULE


def test_inject_returns_empty_when_no_rule_fires(tmp_path):
    rows = [_chunk_row(chunk_id="q1", session_date="2025-12-30")]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="Tell me about onboarding.",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    assert injected == []

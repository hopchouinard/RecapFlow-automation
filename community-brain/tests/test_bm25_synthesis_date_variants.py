"""Tests for v4 date variants in bm25_text."""
from __future__ import annotations

import pytest


def test_bm25_text_includes_iso_date():
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label="t",
        entities=None,
        speakers_spoke=None,
        speakers_mentioned=None,
        keywords=None,
        full_text="hello",
        session_date="2026-03-04",
    )
    assert "2026-03-04" in out


def test_bm25_text_includes_year_month():
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label=None, entities=None, speakers_spoke=None,
        speakers_mentioned=None, keywords=None, full_text="x",
        session_date="2026-03-04",
    )
    assert "2026-03" in out
    assert "March-2026" in out


def test_bm25_text_includes_phrased_date():
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label=None, entities=None, speakers_spoke=None,
        speakers_mentioned=None, keywords=None, full_text="x",
        session_date="2026-03-04",
    )
    assert "March 4 2026" in out
    assert "March 4th 2026" in out


def test_bm25_text_includes_quarter_and_half():
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label=None, entities=None, speakers_spoke=None,
        speakers_mentioned=None, keywords=None, full_text="x",
        session_date="2026-03-04",
    )
    assert "Q1-2026" in out
    assert "H1-2026" in out


def test_bm25_text_relative_day_prefix_early():
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label=None, entities=None, speakers_spoke=None,
        speakers_mentioned=None, keywords=None, full_text="x",
        session_date="2026-03-04",  # day 4 -> early
    )
    assert "early-March-2026" in out
    assert "mid-March-2026" not in out
    assert "late-March-2026" not in out


def test_bm25_text_relative_day_prefix_mid():
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label=None, entities=None, speakers_spoke=None,
        speakers_mentioned=None, keywords=None, full_text="x",
        session_date="2026-03-15",  # day 15 -> mid
    )
    assert "mid-March-2026" in out
    assert "early-March-2026" not in out


def test_bm25_text_relative_day_prefix_late():
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label=None, entities=None, speakers_spoke=None,
        speakers_mentioned=None, keywords=None, full_text="x",
        session_date="2026-03-25",  # day 25 -> late
    )
    assert "late-March-2026" in out


@pytest.mark.parametrize("month_num,quarter", [
    ("01", "Q1"), ("03", "Q1"),
    ("04", "Q2"), ("06", "Q2"),
    ("07", "Q3"), ("09", "Q3"),
    ("10", "Q4"), ("12", "Q4"),
])
def test_bm25_text_quarter_mapping(month_num, quarter):
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label=None, entities=None, speakers_spoke=None,
        speakers_mentioned=None, keywords=None, full_text="x",
        session_date=f"2026-{month_num}-15",
    )
    assert f"{quarter}-2026" in out


def test_bm25_text_existing_fields_still_present():
    """Ensure date variants don't break existing field rendering."""
    from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
    out = synthesize_bm25_text(
        topic_label="my topic",
        entities=["X", "Y"],
        speakers_spoke=["Adam"],
        speakers_mentioned=["Brandon"],
        keywords=["k1", "k2"],
        full_text="full content",
        session_date="2026-03-04",
    )
    assert "my topic" in out
    assert "X, Y" in out
    assert "Adam" in out
    assert "Brandon" in out
    assert "k1, k2" in out
    assert "full content" in out

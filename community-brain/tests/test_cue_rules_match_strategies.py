"""Tests for v4 CueRule match strategies."""
from __future__ import annotations

from community_brain.query.cue_rules import (
    apply_v4_strategy,
    MONTH_NAMES,
)


def test_iso_date_equals_matches():
    chunk = {"session_date": "2026-03-04"}
    assert apply_v4_strategy(
        question="What did the community discuss on 2026-03-04?",
        chunk=chunk,
        question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
        match_field="session_date",
        match_strategy="iso_date_equals",
    ) is True


def test_iso_date_equals_no_match():
    chunk = {"session_date": "2026-02-25"}
    assert apply_v4_strategy(
        question="What did the community discuss on 2026-03-04?",
        chunk=chunk,
        question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
        match_field="session_date",
        match_strategy="iso_date_equals",
    ) is False


def test_iso_date_no_capture_no_match():
    chunk = {"session_date": "2026-03-04"}
    assert apply_v4_strategy(
        question="What did the community discuss recently?",
        chunk=chunk,
        question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
        match_field="session_date",
        match_strategy="iso_date_equals",
    ) is False


def test_month_year_overlap_matches():
    chunk = {"session_date": "2026-03-04"}
    assert apply_v4_strategy(
        question="What did they discuss in March 2026?",
        chunk=chunk,
        question_regex=r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
        match_field="session_date",
        match_strategy="month_year_overlap",
    ) is True


def test_month_year_overlap_wrong_month():
    chunk = {"session_date": "2026-03-04"}
    assert apply_v4_strategy(
        question="What did they discuss in February 2026?",
        chunk=chunk,
        question_regex=r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
        match_field="session_date",
        match_strategy="month_year_overlap",
    ) is False


def test_token_overlap_matches():
    chunk = {"bm25_text": "topic\n\nspeakers\n\nQ1-2026 H1-2026 March-2026\n\nfull text here"}
    assert apply_v4_strategy(
        question="What about Q1 2026?",
        chunk=chunk,
        question_regex=r"\b(Q[1-4])\s+(\d{4})\b",
        match_field="bm25_text",
        match_strategy="token_overlap",
    ) is True


def test_token_overlap_no_match():
    chunk = {"bm25_text": "topic\n\nspeakers\n\nQ2-2026 H1-2026 April-2026\n\nfull text here"}
    assert apply_v4_strategy(
        question="What about Q1 2026?",
        chunk=chunk,
        question_regex=r"\b(Q[1-4])\s+(\d{4})\b",
        match_field="bm25_text",
        match_strategy="token_overlap",
    ) is False


def test_unknown_strategy_returns_false():
    """Unknown strategy is logged but doesn't raise — defensive."""
    chunk = {"session_date": "2026-03-04"}
    assert apply_v4_strategy(
        question="anything",
        chunk=chunk,
        question_regex=r".*",
        match_field="session_date",
        match_strategy="not_a_real_strategy",
    ) is False


def test_month_names_constant_has_all_twelve():
    assert len(MONTH_NAMES) == 12
    assert MONTH_NAMES[0] == "January"
    assert MONTH_NAMES[11] == "December"

import json
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from community_brain.query import build_filter_expression
from community_brain.query.query_local import (
    search_chunks,
    format_results,
    build_answer_prompt,
)


MOCK_RESULTS = [
    {
        "chunk_id": "2025-09-02-chunk-001",
        "session_date": "2025-09-02",
        "topic": "AI Tools and New Tech Adoption",
        "summary": "Group discusses Codex in Cursor.",
        "text": "[00:02:29] Patrick: Did anybody try the new codex?",
        "speakers_in_chunk": '["Patrick Chouinard", "Shakur"]',
        "_distance": 0.15,
    },
    {
        "chunk_id": "2025-09-02-chunk-010",
        "session_date": "2025-09-02",
        "topic": "Database Schema for RAG",
        "summary": "Discussion about pgvector and Postgres.",
        "text": "[00:15:00] Brandon: We should use pgvector...",
        "speakers_in_chunk": '["Brandon Hancock"]',
        "_distance": 0.35,
    },
]


class TestBuildFilterExpression:
    def test_no_filters(self):
        assert build_filter_expression() is None

    def test_date_only(self):
        expr = build_filter_expression(filter_date="2025-09-02")
        assert expr == "session_date = '2025-09-02'"

    def test_speaker_only(self):
        expr = build_filter_expression(filter_speaker="Patrick")
        assert expr == "speakers_in_chunk LIKE '%Patrick%'"

    def test_both_filters(self):
        expr = build_filter_expression(filter_date="2025-09-02", filter_speaker="Patrick")
        assert "session_date = '2025-09-02'" in expr
        assert "speakers_in_chunk LIKE '%Patrick%'" in expr
        assert " AND " in expr

    def test_speaker_with_apostrophe_escaped(self):
        """O'Connor should not break the filter expression."""
        expr = build_filter_expression(filter_speaker="O'Connor")
        assert "O''Connor" in expr
        # Should not contain unescaped single quote that breaks the expression
        assert "O'Connor" not in expr.replace("O''Connor", "")

    def test_invalid_date_format_rejected(self):
        with pytest.raises(ValueError, match="Invalid date format"):
            build_filter_expression(filter_date="not-a-date")

    def test_injection_attempt_in_date_rejected(self):
        with pytest.raises(ValueError, match="Invalid date format"):
            build_filter_expression(filter_date="2025-01-01' OR '1'='1")

    def test_speaker_injection_escaped(self):
        """Crafted speaker input should be escaped, not produce a valid injection."""
        expr = build_filter_expression(filter_speaker="'; DROP TABLE --")
        # The single quotes should be doubled, not left raw
        assert "''" in expr


class TestFormatResults:
    def test_format_results_verbose(self):
        output = format_results(MOCK_RESULTS, verbose=True)
        assert "AI Tools and New Tech Adoption" in output
        assert "Codex" in output
        assert "[1]" in output
        assert "2025-09-02" in output

    def test_format_results_brief(self):
        output = format_results(MOCK_RESULTS, verbose=False)
        assert "[1]" in output
        assert "2025-09-02" in output
        assert "AI Tools and New Tech Adoption" in output
        # Brief mode should NOT include full text
        assert "Did anybody try" not in output

    def test_empty_results(self):
        output = format_results([], verbose=True)
        assert "No results found" in output


class TestBuildPrompt:
    def test_includes_context_and_question(self):
        prompt = build_answer_prompt("What about Codex?", MOCK_RESULTS)
        assert "What about Codex?" in prompt
        assert "Codex in Cursor" in prompt
        assert "[00:02:29]" in prompt

    def test_source_numbering(self):
        prompt = build_answer_prompt("test", MOCK_RESULTS)
        assert "[Source 1]" in prompt
        assert "[Source 2]" in prompt

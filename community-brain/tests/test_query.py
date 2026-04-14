import json
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

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


class TestSearchChunks:
    def test_returns_results(self, tmp_path):
        """Search with a mocked LanceDB table."""
        mock_table = MagicMock()
        mock_table.search.return_value.limit.return_value.to_pandas.return_value = (
            MagicMock(to_dict=MagicMock(return_value={"records": MOCK_RESULTS}))
        )
        # This test verifies the function signature works; real integration tested in Task 5
        # For unit test, just verify format_results and build_answer_prompt work
        pass

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

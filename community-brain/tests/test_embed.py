import json
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from community_brain.embed.embed_nomic import (
    load_chunks_from_jsonl,
    build_lancedb_records,
    embed_and_store,
    NOMIC_DIMS,
)


SAMPLE_CHUNK = {
    "chunk_id": "2025-09-02-chunk-001",
    "session_date": "2025-09-02",
    "session_title": "Weekly Coaching Call",
    "speakers_in_chunk": ["Patrick Chouinard", "Shakur"],
    "chunk_position": 1,
    "total_chunks_in_session": 107,
    "content_tier": "historical",
    "content_type": "transcript",
    "source": "fathom_transcript",
    "topic": "AI Tools and New Tech Adoption",
    "summary": "Group discusses Codex in Cursor and Google image gen tools.",
    "text": "[00:02:29] Patrick Chouinard: Did anybody try the new codex?",
}


class TestLoadChunks:
    def test_loads_from_jsonl(self, tmp_path):
        jsonl_path = tmp_path / "chunks.jsonl"
        jsonl_path.write_text(
            json.dumps(SAMPLE_CHUNK) + "\n"
            + json.dumps({**SAMPLE_CHUNK, "chunk_id": "2025-09-02-chunk-002"}) + "\n"
        )
        chunks = load_chunks_from_jsonl(jsonl_path)
        assert len(chunks) == 2
        assert chunks[0]["chunk_id"] == "2025-09-02-chunk-001"

    def test_empty_file(self, tmp_path):
        jsonl_path = tmp_path / "empty.jsonl"
        jsonl_path.write_text("")
        chunks = load_chunks_from_jsonl(jsonl_path)
        assert len(chunks) == 0


class TestBuildRecords:
    def test_record_fields(self):
        records = build_lancedb_records([SAMPLE_CHUNK])
        assert len(records) == 1
        r = records[0]
        assert r["chunk_id"] == "2025-09-02-chunk-001"
        assert r["summary"] == SAMPLE_CHUNK["summary"]
        assert r["text"] == SAMPLE_CHUNK["text"]
        assert r["topic"] == "AI Tools and New Tech Adoption"
        assert r["session_date"] == "2025-09-02"
        # speakers stored as JSON string for LanceDB compatibility
        assert "Patrick Chouinard" in r["speakers_in_chunk"]

    def test_summary_is_the_embedding_source(self):
        """The summary field should be what gets embedded, not the text field."""
        records = build_lancedb_records([SAMPLE_CHUNK])
        # The record should have summary as a string (embedding happens at insert time)
        assert isinstance(records[0]["summary"], str)
        assert len(records[0]["summary"]) < len(records[0]["text"])


class TestEmbedAndStore:
    def test_creates_table_and_inserts(self, tmp_path):
        mock_embedding = [0.1] * NOMIC_DIMS

        def mock_ollama_embed(model, input):
            """Mock ollama.embed() returning embeddings for each input."""
            if isinstance(input, list):
                return {"embeddings": [mock_embedding for _ in input]}
            return {"embeddings": [mock_embedding]}

        with patch("community_brain.embed.embed_nomic.ollama.embed", side_effect=mock_ollama_embed):
            db_path = tmp_path / "test_lance"
            embed_and_store(
                chunks=[SAMPLE_CHUNK],
                db_path=str(db_path),
                table_name="transcripts",
            )

        # Verify the table was created with data
        import lancedb
        db = lancedb.connect(str(db_path))
        table = db.open_table("transcripts")
        assert table.count_rows() == 1
        results = table.to_arrow()
        assert results["chunk_id"][0].as_py() == "2025-09-02-chunk-001"
        assert results["topic"][0].as_py() == "AI Tools and New Tech Adoption"

    def test_falls_back_to_text_when_summary_empty(self, tmp_path):
        """Chunks from --no-llm have empty summaries; should embed the text field instead."""
        no_summary_chunk = {**SAMPLE_CHUNK, "chunk_id": "2025-09-02-chunk-nosummary", "summary": ""}
        embedded_inputs = []

        def mock_ollama_embed(model, input):
            embedded_inputs.extend(input if isinstance(input, list) else [input])
            mock_embedding = [0.1] * NOMIC_DIMS
            if isinstance(input, list):
                return {"embeddings": [mock_embedding for _ in input]}
            return {"embeddings": [mock_embedding]}

        with patch("community_brain.embed.embed_nomic.ollama.embed", side_effect=mock_ollama_embed):
            db_path = tmp_path / "test_lance"
            embed_and_store(
                chunks=[no_summary_chunk],
                db_path=str(db_path),
                table_name="transcripts",
            )

        # Should have embedded the text field, not an empty string
        assert len(embedded_inputs) == 1
        assert embedded_inputs[0] == no_summary_chunk["text"]

    def test_skips_existing_chunks(self, tmp_path):
        mock_embedding = [0.1] * NOMIC_DIMS

        def mock_ollama_embed(model, input):
            if isinstance(input, list):
                return {"embeddings": [mock_embedding for _ in input]}
            return {"embeddings": [mock_embedding]}

        with patch("community_brain.embed.embed_nomic.ollama.embed", side_effect=mock_ollama_embed):
            db_path = tmp_path / "test_lance"
            # First insert
            embed_and_store(
                chunks=[SAMPLE_CHUNK],
                db_path=str(db_path),
                table_name="transcripts",
            )
            # Second insert with same chunk — should skip
            embed_and_store(
                chunks=[SAMPLE_CHUNK],
                db_path=str(db_path),
                table_name="transcripts",
            )

        import lancedb
        db = lancedb.connect(str(db_path))
        table = db.open_table("transcripts")
        assert table.count_rows() == 1  # not duplicated

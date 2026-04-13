import json
from pathlib import Path
from unittest.mock import patch
from community_brain.backfill.chunk_historical import (
    chunk_single_session,
    generate_manifest,
    TIER_1_CUTOFF,
)

FIXTURES = Path(__file__).parent / "fixtures"


class TestChunkHistorical:
    def test_tier1_cutoff(self):
        assert TIER_1_CUTOFF == "2026-03-10"

    def test_chunk_single_session_no_llm(self, tmp_path):
        """Test v1 fallback mode (no LLM calls)."""
        chunks_dir = tmp_path / "chunks" / "historical"
        chunks_dir.mkdir(parents=True)
        raw_chunks_dir = tmp_path / "raw-chunks"
        raw_chunks_dir.mkdir()

        transcript_text = (FIXTURES / "sample-transcript.txt").read_text()
        transcript_file = tmp_path / "raw-transcripts" / "2025-01-15-test-session.txt"
        transcript_file.parent.mkdir(parents=True)
        transcript_file.write_text(transcript_text)

        result = chunk_single_session(
            transcript_path=transcript_file,
            chunks_dir=chunks_dir,
            raw_chunks_path=raw_chunks_dir / "all-chunks.jsonl",
            use_llm=False,
        )

        assert result is not None
        assert result["date"] == "2025-01-15"
        assert result["chunk_count"] > 0
        assert len(result["speakers"]) > 0

        # Check individual chunk files
        session_dir = chunks_dir / "2025-01-15"
        assert session_dir.exists()
        md_files = list(session_dir.glob("*.md"))
        assert len(md_files) == result["chunk_count"]
        content = md_files[0].read_text()
        assert "---" in content
        assert "session_date:" in content

        jsonl_file = raw_chunks_dir / "all-chunks.jsonl"
        assert jsonl_file.exists()
        lines = [l for l in jsonl_file.read_text().strip().split("\n") if l]
        assert len(lines) == result["chunk_count"]
        obj = json.loads(lines[0])
        assert obj["session_date"] == "2025-01-15"
        assert obj["content_tier"] == "historical"

    def test_chunk_single_session_with_llm(self, tmp_path):
        """Test v2 LLM pipeline with mocked LLM calls."""
        chunks_dir = tmp_path / "chunks" / "historical"
        chunks_dir.mkdir(parents=True)
        raw_chunks_dir = tmp_path / "raw-chunks"
        raw_chunks_dir.mkdir()

        transcript_text = (FIXTURES / "sample-transcript.txt").read_text()
        transcript_file = tmp_path / "raw-transcripts" / "2025-01-15-test-session.txt"
        transcript_file.parent.mkdir(parents=True)
        transcript_file.write_text(transcript_text)

        mock_topics = [
            {
                "topic_title": "Vector Store Comparison",
                "start_timestamp": "00:00:04",
                "end_timestamp": "00:03:25",
                "summary": "Group compares Pinecone, FAISS, and LanceDB for vector storage.",
            },
            {
                "topic_title": "Embedding Model Selection",
                "start_timestamp": "00:03:55",
                "end_timestamp": "00:05:15",
                "summary": "Carol compares nomic-embed-text vs OpenAI embeddings for transcripts.",
            },
            {
                "topic_title": "Chunking Strategies for Transcripts",
                "start_timestamp": "00:05:15",
                "end_timestamp": "00:08:20",
                "summary": "Patrick proposes speaker-aware chunking with 500-token targets.",
            },
        ]

        with patch("community_brain.topic_chunker.call_llm_json", return_value=mock_topics):
            result = chunk_single_session(
                transcript_path=transcript_file,
                chunks_dir=chunks_dir,
                raw_chunks_path=raw_chunks_dir / "all-chunks.jsonl",
                use_llm=True,
            )

        assert result is not None
        assert result["date"] == "2025-01-15"
        assert result["chunk_count"] >= 3

        # Check individual chunk files
        session_dir = chunks_dir / "2025-01-15"
        assert session_dir.exists()
        md_files = list(session_dir.glob("*.md"))
        assert len(md_files) >= 3
        # Find a file with "vector-store" in the name
        vector_files = [f for f in md_files if "vector-store" in f.name]
        assert len(vector_files) > 0, f"No vector-store chunk found in {[f.name for f in md_files]}"
        content = vector_files[0].read_text()
        assert "Vector Store Comparison" in content
        assert "**Summary:**" in content

        jsonl_file = raw_chunks_dir / "all-chunks.jsonl"
        lines = [l for l in jsonl_file.read_text().strip().split("\n") if l]
        obj = json.loads(lines[0])
        assert obj["topic"] != ""
        assert obj["summary"] != ""

    def test_skip_existing(self, tmp_path):
        chunks_dir = tmp_path / "chunks" / "historical"
        chunks_dir.mkdir(parents=True)
        raw_chunks_dir = tmp_path / "raw-chunks"
        raw_chunks_dir.mkdir()

        # Create existing session directory
        (chunks_dir / "2025-01-15").mkdir(parents=True)

        transcript_file = tmp_path / "raw-transcripts" / "2025-01-15-test.txt"
        transcript_file.parent.mkdir(parents=True)
        transcript_file.write_text("[00:01:00] Alice: Hello.")

        result = chunk_single_session(
            transcript_path=transcript_file,
            chunks_dir=chunks_dir,
            raw_chunks_path=raw_chunks_dir / "all-chunks.jsonl",
            force=False,
        )
        assert result is None


class TestManifest:
    def test_generate_manifest(self, tmp_path):
        sessions = [
            {
                "date": "2024-10-15",
                "title": "Weekly Coaching Call",
                "content_tier": "historical",
                "chunk_count": 85,
                "speakers": ["Patrick Chouinard", "Alice Chen"],
                "duration_minutes": None,
            },
            {
                "date": "2025-01-15",
                "title": "Weekly Coaching Call",
                "content_tier": "historical",
                "chunk_count": 42,
                "speakers": ["Patrick Chouinard", "Bob Martinez"],
                "duration_minutes": None,
            },
        ]
        manifest_path = tmp_path / "manifest.json"
        generate_manifest(sessions, manifest_path)

        assert manifest_path.exists()
        data = json.loads(manifest_path.read_text())
        assert data["version"] == "1.0.0"
        assert data["total_sessions"] == 2
        assert data["total_chunks"] == 127
        assert data["tier_1_cutoff"] == "2026-03-10"
        assert len(data["sessions"]) == 2
        assert data["sessions"][0]["date"] == "2024-10-15"
        assert data["sessions"][1]["date"] == "2025-01-15"

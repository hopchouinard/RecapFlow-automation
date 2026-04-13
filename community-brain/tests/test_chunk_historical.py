import json
from pathlib import Path
from community_brain.backfill.chunk_historical import (
    chunk_single_session,
    generate_manifest,
    TIER_1_CUTOFF,
)

FIXTURES = Path(__file__).parent / "fixtures"


class TestChunkHistorical:
    def test_tier1_cutoff(self):
        assert TIER_1_CUTOFF == "2026-03-10"

    def test_chunk_single_session(self, tmp_path):
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
        )

        assert result is not None
        assert result["date"] == "2025-01-15"
        assert result["chunk_count"] > 0
        assert len(result["speakers"]) > 0

        md_file = chunks_dir / "session-2025-01-15.md"
        assert md_file.exists()
        content = md_file.read_text()
        assert "---" in content
        assert "session_date:" in content

        jsonl_file = raw_chunks_dir / "all-chunks.jsonl"
        assert jsonl_file.exists()
        lines = [l for l in jsonl_file.read_text().strip().split("\n") if l]
        assert len(lines) == result["chunk_count"]
        obj = json.loads(lines[0])
        assert obj["session_date"] == "2025-01-15"
        assert obj["content_tier"] == "historical"

    def test_skip_existing(self, tmp_path):
        chunks_dir = tmp_path / "chunks" / "historical"
        chunks_dir.mkdir(parents=True)
        raw_chunks_dir = tmp_path / "raw-chunks"
        raw_chunks_dir.mkdir()

        (chunks_dir / "session-2025-01-15.md").write_text("already exists")

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

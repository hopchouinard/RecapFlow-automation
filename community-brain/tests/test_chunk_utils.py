import json
from pathlib import Path
from community_brain.chunk_utils import (
    SpeakerTurn,
    parse_transcript,
    normalize_speaker,
    count_tokens,
    Chunk,
    chunk_transcript,
)


class TestParseTranscript:
    def test_basic(self):
        text = (
            "[00:05:07] Patrick Chouinard: Hey, Ty.\n"
            "[00:05:09] Ty Wells: How's it going?\n"
            "[00:06:00] Patrick Chouinard: Did you try Claude Speak?"
        )
        turns = parse_transcript(text)
        assert len(turns) == 3
        assert turns[0] == SpeakerTurn(
            timestamp="00:05:07",
            speaker="Patrick Chouinard",
            text="Hey, Ty.",
        )
        assert turns[1].speaker == "Ty Wells"
        assert turns[1].text == "How's it going?"
        assert turns[2].timestamp == "00:06:00"

    def test_blank_lines_skipped(self):
        text = (
            "[00:01:00] Alice: Hello.\n"
            "\n"
            "\n"
            "[00:02:00] Bob: Hi there."
        )
        turns = parse_transcript(text)
        assert len(turns) == 2

    def test_unparseable_lines_skipped(self, caplog):
        text = (
            "[00:01:00] Alice: Hello.\n"
            "This is not a valid transcript line\n"
            "[00:02:00] Bob: Hi there."
        )
        turns = parse_transcript(text)
        assert len(turns) == 2
        assert "Skipping unparseable line" in caplog.text

    def test_speaker_with_colon_in_text(self):
        text = "[00:01:00] Alice: The URL is https://example.com: check it out."
        turns = parse_transcript(text)
        assert len(turns) == 1
        assert turns[0].text == "The URL is https://example.com: check it out."


class TestNormalizeSpeaker:
    def test_with_alias(self):
        aliases = {"Patchou": "Patrick Chouinard", "Pat C.": "Patrick Chouinard"}
        assert normalize_speaker("Patchou", aliases) == "Patrick Chouinard"
        assert normalize_speaker("Pat C.", aliases) == "Patrick Chouinard"

    def test_without_alias(self):
        assert normalize_speaker("Alice Chen", None) == "Alice Chen"
        assert normalize_speaker("Alice Chen", {}) == "Alice Chen"

    def test_no_match_returns_original(self):
        aliases = {"Patchou": "Patrick Chouinard"}
        assert normalize_speaker("Alice Chen", aliases) == "Alice Chen"


class TestCountTokens:
    def test_nonempty(self):
        count = count_tokens("Hello, world!")
        assert count > 0

    def test_empty(self):
        assert count_tokens("") == 0

    def test_reasonable_range(self):
        # "The quick brown fox jumps over the lazy dog" is ~9-10 tokens
        text = "The quick brown fox jumps over the lazy dog"
        count = count_tokens(text)
        assert 8 <= count <= 12

    def test_longer_text(self):
        # ~500 token text should count in that range
        text = "This is a test sentence. " * 50  # ~350-400 tokens
        count = count_tokens(text)
        assert 200 <= count <= 500


FIXTURES = Path(__file__).parent / "fixtures"


class TestChunkTranscript:
    def _make_turns(self, count: int, words_per_turn: int = 50) -> list[SpeakerTurn]:
        """Helper: generate speaker turns with predictable token counts."""
        speakers = ["Alice", "Bob", "Carol"]
        turns = []
        for i in range(count):
            speaker = speakers[i % len(speakers)]
            text = f"Word{i} " + "test content here please " * (words_per_turn // 3)
            turns.append(SpeakerTurn(
                timestamp=f"00:{i:02d}:00",
                speaker=speaker,
                text=text.strip(),
            ))
        return turns

    def test_basic_chunking(self):
        turns = self._make_turns(10)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        assert len(chunks) >= 2

    def test_speaker_boundary(self):
        import re as re_mod
        turns = self._make_turns(10)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        for chunk in chunks:
            lines = [
                l for l in chunk.text.split("\n")
                if l.strip() and not l.startswith("##")
            ]
            for line in lines:
                assert re_mod.match(r"\[\d{2}:\d{2}:\d{2}\]", line), (
                    f"Non-turn line found in chunk: {line[:60]}"
                )

    def test_overlap(self):
        turns = self._make_turns(15)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        if len(chunks) < 2:
            return
        for i in range(len(chunks) - 1):
            current_lines = set(chunks[i].text.strip().split("\n"))
            next_lines = set(chunks[i + 1].text.strip().split("\n"))
            overlap = current_lines & next_lines
            overlap_content = {l for l in overlap if not l.startswith("##") and l.strip()}
            assert len(overlap_content) > 0, f"No overlap between chunks {i} and {i+1}"

    def test_long_turn_becomes_own_chunk(self):
        turns = [
            SpeakerTurn("00:00:00", "Alice", "short turn"),
            SpeakerTurn("00:01:00", "Bob", "word " * 600),
            SpeakerTurn("00:02:00", "Alice", "another short turn"),
        ]
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session", target_tokens=500)
        long_turn_found = False
        for chunk in chunks:
            if "word word word word" in chunk.text and count_tokens(chunk.text) > 400:
                long_turn_found = True
        assert long_turn_found, "Long turn should become its own chunk"

    def test_metadata(self):
        turns = self._make_turns(5)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        for chunk in chunks:
            assert chunk.session_date == "2024-03-15"
            assert chunk.session_title == "Test Session"
            assert chunk.content_tier == "historical"
            assert chunk.content_type == "transcript"
            assert chunk.source == "fathom_transcript"
            assert len(chunk.speakers_in_chunk) > 0
            assert chunk.chunk_position >= 1

    def test_total_chunks_set(self):
        turns = self._make_turns(15)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        for chunk in chunks:
            assert chunk.total_chunks_in_session == len(chunks)

    def test_chunk_id_format(self):
        turns = self._make_turns(5)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        for i, chunk in enumerate(chunks):
            expected_id = f"2024-03-15-chunk-{i + 1:03d}"
            assert chunk.chunk_id == expected_id

    def test_with_fixture_file(self):
        text = (FIXTURES / "sample-transcript.txt").read_text()
        turns = parse_transcript(text)
        assert len(turns) >= 15
        chunks = chunk_transcript(turns, "2025-01-15", "Vector DB Discussion")
        assert len(chunks) >= 2
        all_speakers = set()
        for chunk in chunks:
            all_speakers.update(chunk.speakers_in_chunk)
        assert "Patrick Chouinard" in all_speakers
        assert "Alice Chen" in all_speakers

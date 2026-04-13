import json
from community_brain.chunk_utils import (
    SpeakerTurn,
    parse_transcript,
    normalize_speaker,
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


from community_brain.chunk_utils import count_tokens


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

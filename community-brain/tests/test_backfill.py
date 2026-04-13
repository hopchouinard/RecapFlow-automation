import json
from pathlib import Path
from community_brain.backfill.fetch_fathom import (
    is_coaching_call,
    slugify_title,
    format_transcript_entries,
)

FIXTURES = Path(__file__).parent / "fixtures"


class TestIsCoachingCall:
    def test_weekly_coaching_call(self):
        assert is_coaching_call("Weekly Coaching Call") is True

    def test_ai_developer_accelerator(self):
        assert is_coaching_call("AI Developer Accelerator — Coaching Call") is True

    def test_case_insensitive(self):
        assert is_coaching_call("weekly coaching call") is True
        assert is_coaching_call("WEEKLY COACHING CALL") is True
        assert is_coaching_call("ai developer accelerator — coaching call") is True

    def test_non_coaching_call(self):
        assert is_coaching_call("Team Standup") is False
        assert is_coaching_call("1:1 with Bob") is False

    def test_empty(self):
        assert is_coaching_call("") is False
        assert is_coaching_call(None) is False


class TestSlugifyTitle:
    def test_basic(self):
        assert slugify_title("Weekly Coaching Call") == "weekly-coaching-call"

    def test_special_chars(self):
        assert slugify_title("AI Developer Accelerator — Coaching Call") == "ai-developer-accelerator-coaching-call"

    def test_extra_spaces(self):
        assert slugify_title("  Some  Title  ") == "some-title"


class TestFormatTranscriptEntries:
    def test_basic(self):
        entries = [
            {"speaker": {"display_name": "Patrick"}, "timestamp": "00:05:07", "text": "Hello."},
            {"speaker": {"display_name": "Alice"}, "timestamp": "00:05:15", "text": "Hi!"},
        ]
        result = format_transcript_entries(entries)
        assert result == "[00:05:07] Patrick: Hello.\n[00:05:15] Alice: Hi!"

    def test_missing_speaker(self):
        entries = [
            {"speaker": None, "timestamp": "00:01:00", "text": "Something."},
            {"speaker": {}, "timestamp": "00:02:00", "text": "Else."},
        ]
        result = format_transcript_entries(entries)
        assert "[00:01:00] Unknown: Something." in result
        assert "[00:02:00] Unknown: Else." in result

    def test_empty(self):
        assert format_transcript_entries([]) == ""

import json
from pathlib import Path
from unittest.mock import patch
from community_brain.chunk_utils import SpeakerTurn, parse_transcript, count_tokens, _format_turn
from community_brain.topic_chunker import (
    Topic,
    extract_turns_for_topic,
    build_segmentation_prompt,
    parse_segmentation_response,
    chunk_by_topics,
)

FIXTURES = Path(__file__).parent / "fixtures"


class TestTopic:
    def test_dataclass_fields(self):
        t = Topic(
            topic_title="Test Topic",
            start_timestamp="00:01:00",
            end_timestamp="00:05:00",
            summary="A test topic.",
        )
        assert t.topic_title == "Test Topic"
        assert t.start_timestamp == "00:01:00"
        assert t.end_timestamp == "00:05:00"
        assert t.summary == "A test topic."


class TestExtractTurnsForTopic:
    def test_basic_extraction(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Before topic."),
            SpeakerTurn("00:02:00", "Bob", "Inside topic."),
            SpeakerTurn("00:03:00", "Alice", "Also inside."),
            SpeakerTurn("00:05:00", "Bob", "After topic."),
        ]
        topic = Topic("Test", "00:02:00", "00:04:00", "A test.")
        result = extract_turns_for_topic(turns, topic)
        assert len(result) == 2
        assert result[0].text == "Inside topic."
        assert result[1].text == "Also inside."

    def test_inclusive_boundaries(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Start."),
            SpeakerTurn("00:05:00", "Bob", "End."),
            SpeakerTurn("00:06:00", "Alice", "After."),
        ]
        topic = Topic("Test", "00:01:00", "00:05:00", "A test.")
        result = extract_turns_for_topic(turns, topic)
        assert len(result) == 2

    def test_empty_range(self):
        turns = [
            SpeakerTurn("00:10:00", "Alice", "Way later."),
        ]
        topic = Topic("Test", "00:01:00", "00:05:00", "A test.")
        result = extract_turns_for_topic(turns, topic)
        assert len(result) == 0


class TestBuildSegmentationPrompt:
    def test_contains_transcript(self):
        prompt = build_segmentation_prompt("some transcript text here")
        assert "some transcript text here" in prompt
        assert "topic_title" in prompt
        assert "JSON" in prompt or "json" in prompt


class TestParseSegmentationResponse:
    def test_valid_json_array(self):
        response = [
            {
                "topic_title": "Intro and Greetings",
                "start_timestamp": "00:00:00",
                "end_timestamp": "00:02:00",
                "summary": "Group greets each other.",
            },
            {
                "topic_title": "GPU Discussion",
                "start_timestamp": "00:02:00",
                "end_timestamp": "00:10:00",
                "summary": "Discussion about GPU benchmarks.",
            },
        ]
        topics = parse_segmentation_response(response)
        assert len(topics) == 2
        assert topics[0].topic_title == "Intro and Greetings"
        assert topics[1].summary == "Discussion about GPU benchmarks."

    def test_handles_missing_fields(self):
        response = [
            {"topic_title": "Test", "start_timestamp": "00:01:00"},
        ]
        topics = parse_segmentation_response(response)
        assert len(topics) == 1
        assert topics[0].end_timestamp == ""
        assert topics[0].summary == ""


class TestChunkByTopics:
    def test_small_topic_single_chunk(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Hello, this is a short topic."),
            SpeakerTurn("00:01:30", "Bob", "Yes, very short."),
        ]
        topics = [Topic("Short Topic", "00:01:00", "00:02:00", "A brief exchange.")]

        chunks = chunk_by_topics(
            turns=turns,
            topics=topics,
            session_date="2025-09-02",
            session_title="Test Session",
        )

        assert len(chunks) == 1
        assert chunks[0].topic == "Short Topic"
        assert chunks[0].summary == "A brief exchange."
        assert "Alice" in chunks[0].speakers_in_chunk
        assert "Bob" in chunks[0].speakers_in_chunk

    def test_large_topic_gets_split(self):
        turns = [
            SpeakerTurn(f"00:{i:02d}:00", ["Alice", "Bob"][i % 2], f"Turn {i}. " + "word " * 80)
            for i in range(1, 16)
        ]
        topics = [Topic("Big Topic", "00:01:00", "00:15:00", "A long discussion.")]

        with patch("community_brain.topic_chunker.call_llm", return_value="Sub-summary of this section."):
            chunks = chunk_by_topics(
                turns=turns,
                topics=topics,
                session_date="2025-09-02",
                session_title="Test Session",
                max_topic_tokens=800,
            )

        assert len(chunks) >= 2
        for chunk in chunks:
            assert chunk.topic == "Big Topic"
            assert chunk.summary != ""

    def test_multiple_topics(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Topic one content."),
            SpeakerTurn("00:02:00", "Bob", "More topic one."),
            SpeakerTurn("00:05:00", "Alice", "Topic two content."),
            SpeakerTurn("00:06:00", "Bob", "More topic two."),
        ]
        topics = [
            Topic("First Topic", "00:01:00", "00:03:00", "First discussion."),
            Topic("Second Topic", "00:05:00", "00:07:00", "Second discussion."),
        ]

        chunks = chunk_by_topics(
            turns=turns,
            topics=topics,
            session_date="2025-09-02",
            session_title="Test Session",
        )

        assert len(chunks) == 2
        assert chunks[0].topic == "First Topic"
        assert chunks[1].topic == "Second Topic"
        assert chunks[0].chunk_position == 1
        assert chunks[1].chunk_position == 2
        assert chunks[0].total_chunks_in_session == 2

    def test_chunk_ids_sequential(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Hello."),
            SpeakerTurn("00:05:00", "Bob", "World."),
        ]
        topics = [
            Topic("T1", "00:01:00", "00:03:00", "First."),
            Topic("T2", "00:05:00", "00:06:00", "Second."),
        ]

        chunks = chunk_by_topics(
            turns=turns,
            topics=topics,
            session_date="2025-09-02",
            session_title="Test Session",
        )

        assert chunks[0].chunk_id == "2025-09-02-chunk-001"
        assert chunks[1].chunk_id == "2025-09-02-chunk-002"

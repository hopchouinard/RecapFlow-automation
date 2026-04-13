# Community Brain SP1: Two-Pass LLM-Enhanced Chunking (v2) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the chunking pipeline from fixed-size sliding windows to LLM-enhanced topic-aware chunking with summaries, dramatically improving retrieval quality.

**Architecture:** Two-pass pipeline. Pass 1: send full transcript to Gemini 3.1 Flash Lite via OpenRouter for topic segmentation. Pass 2: chunk by topic boundaries, generate summaries. Existing `chunk_transcript()` retained as sub-splitter for oversized topics. New files: `llm.py`, `topic_chunker.py`. Modified files: `chunk_utils.py`, `chunk_historical.py`, and their tests.

**Tech Stack:** Python 3.12, httpx (OpenRouter API), tiktoken, existing community_brain package

**Spec:** `docs/superpowers/specs/2026-04-13-community-brain-sp1-chunking-v2.md`

---

## File Map

| Action | Path | Responsibility |
|--------|------|---------------|
| Create | `community-brain/src/community_brain/llm.py` | OpenRouter API client |
| Create | `community-brain/src/community_brain/topic_chunker.py` | Topic segmentation + chunk-by-topic logic |
| Modify | `community-brain/src/community_brain/chunk_utils.py:72-84` | Add `topic` and `summary` fields to `Chunk` dataclass |
| Modify | `community-brain/src/community_brain/chunk_utils.py:92-188` | Update `chunk_transcript()` to accept and pass through `topic`/`summary` |
| Modify | `community-brain/src/community_brain/chunk_utils.py:200-241` | Update `chunks_to_markdown()` to include topic headers and summaries |
| Modify | `community-brain/src/community_brain/backfill/chunk_historical.py:57-121` | Update `chunk_single_session()` to use two-pass pipeline |
| Create | `community-brain/tests/test_llm.py` | Tests for LLM client |
| Create | `community-brain/tests/test_topic_chunker.py` | Tests for topic segmentation and chunk-by-topic |
| Modify | `community-brain/tests/test_chunk_utils.py` | Update existing tests for new Chunk fields |
| Modify | `community-brain/tests/test_chunk_historical.py` | Update for two-pass pipeline |

---

### Task 1: Update Chunk Dataclass with topic + summary Fields

**Files:**
- Modify: `community-brain/src/community_brain/chunk_utils.py:72-84`
- Modify: `community-brain/tests/test_chunk_utils.py`

- [ ] **Step 1: Update the Chunk dataclass**

In `community-brain/src/community_brain/chunk_utils.py`, replace the `Chunk` dataclass (lines 72-84) with:

```python
@dataclass
class Chunk:
    """A single chunk of transcript content with metadata."""
    chunk_id: str
    session_date: str
    session_title: str
    speakers_in_chunk: list[str]
    chunk_position: int
    total_chunks_in_session: int
    content_tier: str
    content_type: str
    source: str
    topic: str
    summary: str
    text: str
```

- [ ] **Step 2: Update chunk_transcript() to set default topic and summary**

In `chunk_utils.py`, update the `_finalize_chunk` inner function (around line 120-134) to include the new fields:

```python
    def _finalize_chunk(chunk_turns: list[SpeakerTurn]) -> None:
        text = header + "\n".join(_format_turn(t) for t in chunk_turns)
        speakers = sorted(set(t.speaker for t in chunk_turns))
        chunks.append(Chunk(
            chunk_id="",
            session_date=session_date,
            session_title=session_title,
            speakers_in_chunk=speakers,
            chunk_position=0,
            total_chunks_in_session=0,
            content_tier=content_tier,
            content_type=content_type,
            source=source,
            topic="",
            summary="",
            text=text,
        ))
```

- [ ] **Step 3: Update chunks_to_markdown() to include topic and summary**

Replace the `chunks_to_markdown` function (lines 200-241) with:

```python
def chunks_to_markdown(
    chunks: list[Chunk],
    session_date: str,
    session_title: str,
) -> str:
    """Produce a markdown file with YAML frontmatter and chunks separated by ---."""
    if not chunks:
        return ""

    all_speakers = sorted(set(
        speaker
        for chunk in chunks
        for speaker in chunk.speakers_in_chunk
    ))
    content_tier = chunks[0].content_tier

    speakers_yaml = json.dumps(all_speakers)
    frontmatter = (
        f"---\n"
        f'session_date: "{session_date}"\n'
        f'session_title: "{session_title}"\n'
        f'content_tier: "{content_tier}"\n'
        f"speakers: {speakers_yaml}\n"
        f"chunk_count: {len(chunks)}\n"
        f"---\n"
    )

    sections = []
    total = len(chunks)
    for chunk in chunks:
        # Strip the session header from chunk text
        text_without_header = chunk.text
        header_prefix = f"## Session: {session_title} | Date: {session_date}\n\n"
        if text_without_header.startswith(header_prefix):
            text_without_header = text_without_header[len(header_prefix):]

        # Build section header with topic and summary if present
        if chunk.topic:
            section_header = f"### Topic: {chunk.topic}"
            # Add sub-chunk indicator if this topic was split
            sub_chunks_for_topic = [c for c in chunks if c.topic == chunk.topic]
            if len(sub_chunks_for_topic) > 1:
                idx = sub_chunks_for_topic.index(chunk) + 1
                section_header += f" ({idx} of {len(sub_chunks_for_topic)})"
        else:
            section_header = f"### Chunk {chunk.chunk_position} of {total}"

        summary_line = f"\n\n**Summary:** {chunk.summary}" if chunk.summary else ""

        section = f"{section_header}{summary_line}\n\n{text_without_header}"
        sections.append(section)

    body = f"\n## Session: {session_title} | Date: {session_date}\n\n"
    body += "\n\n---\n\n".join(sections)

    return frontmatter + body + "\n"
```

- [ ] **Step 4: Run existing tests — expect some failures due to new fields**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_chunk_utils.py -v
```

Expected: Tests that check chunk metadata or markdown output may need updating. The `test_metadata` test should still pass since it doesn't check `topic`/`summary`. The markdown tests may fail since the output format changed.

- [ ] **Step 5: Update failing tests**

In `tests/test_chunk_utils.py`, update `TestChunksToMarkdown::test_chunk_separators` — the format changed from `### Chunk N of M` to `### Topic:` when topic is set, but `chunk_transcript()` sets `topic=""`, so the old format should still be used for chunks without topics. Verify and fix any assertions that break.

Also update `TestChunksToJsonl::test_valid_jsonl` to check for the new fields:

```python
    def test_valid_jsonl(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Hello everyone."),
            SpeakerTurn("00:02:00", "Bob", "Hi Alice, great to be here."),
        ]
        chunks = chunk_transcript(turns, "2024-03-15", "Test", target_tokens=5000)
        jsonl = chunks_to_jsonl(chunks)
        lines = [l for l in jsonl.strip().split("\n") if l.strip()]
        assert len(lines) == len(chunks)
        for line in lines:
            obj = json.loads(line)
            assert "chunk_id" in obj
            assert "session_date" in obj
            assert "text" in obj
            assert "speakers_in_chunk" in obj
            assert "topic" in obj
            assert "summary" in obj
```

- [ ] **Step 6: Run all tests — verify they pass**

```bash
pytest tests/ -v
```

Expected: All 39 tests PASS.

- [ ] **Step 7: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/chunk_utils.py community-brain/tests/test_chunk_utils.py
git commit -m "feat(sp1-v2): add topic and summary fields to Chunk dataclass

Update Chunk with topic/summary fields. Update chunks_to_markdown to
render topic headers and summaries. Backward compatible — chunk_transcript
sets empty defaults. All 39 tests passing."
```

---

### Task 2: LLM Client (TDD)

**Files:**
- Create: `community-brain/tests/test_llm.py`
- Create: `community-brain/src/community_brain/llm.py`

- [ ] **Step 1: Write failing tests**

Create `community-brain/tests/test_llm.py`:

```python
import json
import httpx
import pytest
from unittest.mock import patch, MagicMock
from community_brain.llm import call_llm, call_llm_json, LLMError


class TestCallLlm:
    def test_returns_content_string(self):
        mock_response = httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": "Hello from LLM"}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 5},
            },
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        with patch("community_brain.llm.httpx.post", return_value=mock_response):
            result = call_llm("Say hello")
        assert result == "Hello from LLM"

    def test_raises_on_missing_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with patch("community_brain.llm._get_api_key", return_value=None):
                with pytest.raises(LLMError, match="OPENROUTER_API_KEY"):
                    call_llm("test")

    def test_retries_on_error(self):
        fail_response = httpx.Response(
            500,
            text="Internal Server Error",
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        ok_response = httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": "success"}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 5},
            },
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        with patch("community_brain.llm.httpx.post", side_effect=[fail_response, ok_response]):
            with patch("community_brain.llm.time.sleep"):  # don't actually sleep
                result = call_llm("test")
        assert result == "success"


class TestCallLlmJson:
    def test_parses_json_response(self):
        json_content = json.dumps([
            {"topic_title": "Test Topic", "start_timestamp": "00:01:00",
             "end_timestamp": "00:05:00", "summary": "A test topic."}
        ])
        mock_response = httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": json_content}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 20},
            },
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        with patch("community_brain.llm.httpx.post", return_value=mock_response):
            result = call_llm_json("segment this")
        assert isinstance(result, list)
        assert result[0]["topic_title"] == "Test Topic"

    def test_strips_markdown_code_fences(self):
        json_content = '```json\n[{"topic_title": "Test"}]\n```'
        mock_response = httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": json_content}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 10},
            },
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        with patch("community_brain.llm.httpx.post", return_value=mock_response):
            result = call_llm_json("test")
        assert result[0]["topic_title"] == "Test"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_llm.py -v
```

Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Implement llm.py**

Create `community-brain/src/community_brain/llm.py`:

```python
"""Thin OpenRouter API client for LLM calls.

Uses the OpenRouter chat completions endpoint with configurable model.
Default model: google/gemini-3.1-flash-lite-preview
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-3.1-flash-lite-preview"
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent / "config"


class LLMError(Exception):
    """Raised when an LLM call fails."""


def _get_api_key() -> str | None:
    """Get OpenRouter API key from environment."""
    load_dotenv(CONFIG_DIR / ".env")
    return os.environ.get("OPENROUTER_API_KEY")


def _get_model() -> str:
    """Get LLM model from environment or use default."""
    return os.environ.get("COMMUNITY_BRAIN_LLM_MODEL", DEFAULT_MODEL)


def call_llm(
    prompt: str,
    model: str | None = None,
    retries: int = 3,
) -> str:
    """Call OpenRouter chat completions API and return the response text.

    Args:
        prompt: The user message to send.
        model: Override the default model.
        retries: Number of retry attempts on failure.

    Returns:
        The assistant's response text.

    Raises:
        LLMError: If the API key is missing or all retries fail.
    """
    api_key = _get_api_key()
    if not api_key:
        raise LLMError("OPENROUTER_API_KEY not set in config/.env")

    if model is None:
        model = _get_model()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }

    for attempt in range(retries):
        try:
            response = httpx.post(
                OPENROUTER_URL,
                headers=headers,
                json=payload,
                timeout=120.0,
            )
            if response.status_code >= 500:
                if attempt < retries - 1:
                    backoff = 2 ** attempt
                    logger.warning(
                        "LLM API error %d, retrying in %ds",
                        response.status_code, backoff,
                    )
                    time.sleep(backoff)
                    continue
                raise LLMError(f"LLM API error after {retries} retries: {response.status_code}")

            response.raise_for_status()
            data = response.json()

            # Log token usage
            usage = data.get("usage", {})
            if usage:
                logger.info(
                    "LLM tokens — input: %d, output: %d",
                    usage.get("prompt_tokens", 0),
                    usage.get("completion_tokens", 0),
                )

            return data["choices"][0]["message"]["content"]

        except httpx.HTTPError as e:
            if attempt < retries - 1:
                backoff = 2 ** attempt
                logger.warning("LLM request failed (%s), retrying in %ds", e, backoff)
                time.sleep(backoff)
            else:
                raise LLMError(f"LLM request failed after {retries} retries: {e}") from e

    raise LLMError("Exhausted retries")


def call_llm_json(
    prompt: str,
    model: str | None = None,
    retries: int = 3,
) -> list | dict:
    """Call LLM and parse the response as JSON.

    Handles markdown code fences (```json ... ```) that models sometimes wrap responses in.

    Raises:
        LLMError: If JSON parsing fails after retries.
    """
    text = call_llm(prompt, model=model, retries=retries)

    # Strip markdown code fences if present
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*\n?", "", cleaned)
    cleaned = re.sub(r"\n?```\s*$", "", cleaned)
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise LLMError(f"Failed to parse LLM response as JSON: {e}\nResponse: {text[:200]}") from e
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_llm.py -v
```

Expected: All 5 tests PASS.

- [ ] **Step 5: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/llm.py community-brain/tests/test_llm.py
git commit -m "feat(sp1-v2): add OpenRouter LLM client

call_llm() and call_llm_json() with retry logic, rate-limit handling,
markdown fence stripping, and token usage logging.
5 tests passing."
```

---

### Task 3: Topic Segmentation + Chunk-by-Topics (TDD)

**Files:**
- Create: `community-brain/tests/test_topic_chunker.py`
- Create: `community-brain/src/community_brain/topic_chunker.py`

- [ ] **Step 1: Write failing tests**

Create `community-brain/tests/test_topic_chunker.py`:

```python
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
        # Create a topic with ~1200 tokens of content (exceeds 800 threshold)
        turns = [
            SpeakerTurn(f"00:{i:02d}:00", ["Alice", "Bob"][i % 2], f"Turn {i}. " + "word " * 80)
            for i in range(1, 16)
        ]
        topics = [Topic("Big Topic", "00:01:00", "00:15:00", "A long discussion.")]

        # Mock the LLM call for sub-summaries
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_topic_chunker.py -v
```

Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Implement topic_chunker.py**

Create `community-brain/src/community_brain/topic_chunker.py`:

```python
"""Topic-aware chunking for Community Brain transcripts.

Two-pass pipeline:
  Pass 1: LLM segments transcript into discussion topics
  Pass 2: Chunks by topic boundaries, generates summaries
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from community_brain.chunk_utils import (
    Chunk,
    SpeakerTurn,
    _format_turn,
    chunk_transcript,
    count_tokens,
)
from community_brain.llm import call_llm, call_llm_json

logger = logging.getLogger(__name__)

SEGMENTATION_PROMPT = """You are segmenting a coaching call transcript into discussion topics.

For each distinct topic discussed, provide:
- topic_title: A short descriptive title (5-10 words)
- start_timestamp: The [HH:MM:SS] where this topic begins
- end_timestamp: The [HH:MM:SS] where this topic ends
- summary: 1-2 sentence summary of what was discussed

Rules:
- A topic is a coherent discussion thread (e.g., "Trying Codex in Cursor", "GPU benchmarks for local models")
- Greetings, small talk, and transitions between topics are NOT separate topics — attach them to the adjacent topic
- If a topic is briefly interrupted and resumed, treat it as one topic
- Aim for 5-20 topics per hour of conversation
- Output as a JSON array only, no other text

Transcript:
{transcript_text}"""

SUB_SUMMARY_PROMPT = """Summarize this section of a coaching call transcript in 1-2 sentences.
Focus on the specific points discussed, tools mentioned, and conclusions reached.

Topic: {topic_title}
Transcript section:
{chunk_text}"""


@dataclass
class Topic:
    """A discussion topic identified by LLM segmentation."""
    topic_title: str
    start_timestamp: str
    end_timestamp: str
    summary: str


def build_segmentation_prompt(transcript_text: str) -> str:
    """Build the prompt for topic segmentation."""
    return SEGMENTATION_PROMPT.format(transcript_text=transcript_text)


def parse_segmentation_response(response: list[dict]) -> list[Topic]:
    """Parse the LLM's JSON response into Topic objects."""
    topics = []
    for item in response:
        topics.append(Topic(
            topic_title=item.get("topic_title", "Untitled"),
            start_timestamp=item.get("start_timestamp", ""),
            end_timestamp=item.get("end_timestamp", ""),
            summary=item.get("summary", ""),
        ))
    return topics


def segment_transcript(transcript_text: str) -> list[Topic]:
    """Pass 1: Send full transcript to LLM for topic segmentation.

    Returns a list of Topic objects with timestamp boundaries and summaries.
    """
    prompt = build_segmentation_prompt(transcript_text)
    response = call_llm_json(prompt)
    if not isinstance(response, list):
        response = [response]
    topics = parse_segmentation_response(response)
    logger.info("Segmented transcript into %d topics", len(topics))
    return topics


def extract_turns_for_topic(
    turns: list[SpeakerTurn],
    topic: Topic,
) -> list[SpeakerTurn]:
    """Extract speaker turns that fall within a topic's timestamp range."""
    result = []
    for turn in turns:
        if topic.start_timestamp <= turn.timestamp <= topic.end_timestamp:
            result.append(turn)
    return result


def _generate_sub_summary(topic_title: str, chunk_text: str) -> str:
    """Generate a summary for a sub-chunk of an oversized topic."""
    prompt = SUB_SUMMARY_PROMPT.format(
        topic_title=topic_title,
        chunk_text=chunk_text,
    )
    return call_llm(prompt)


def chunk_by_topics(
    turns: list[SpeakerTurn],
    topics: list[Topic],
    session_date: str,
    session_title: str,
    content_tier: str = "historical",
    source: str = "fathom_transcript",
    max_topic_tokens: int = 800,
) -> list[Chunk]:
    """Pass 2: Chunk transcript by topic boundaries with summaries.

    For each topic:
    - If total tokens ≤ max_topic_tokens: one chunk, use topic summary
    - If > max_topic_tokens: sub-split using chunk_transcript(), generate sub-summaries via LLM

    Returns a flat list of Chunk objects with sequential IDs.
    """
    all_chunks: list[Chunk] = []
    header = f"## Session: {session_title} | Date: {session_date}\n\n"

    for topic in topics:
        topic_turns = extract_turns_for_topic(turns, topic)
        if not topic_turns:
            logger.warning("No turns found for topic %r (%s-%s)",
                           topic.topic_title, topic.start_timestamp, topic.end_timestamp)
            continue

        # Calculate total tokens for this topic's content
        topic_text = "\n".join(_format_turn(t) for t in topic_turns)
        topic_tokens = count_tokens(topic_text)

        if topic_tokens <= max_topic_tokens:
            # Small topic — one chunk with the topic's summary
            text = header + topic_text
            speakers = sorted(set(t.speaker for t in topic_turns))
            all_chunks.append(Chunk(
                chunk_id="",
                session_date=session_date,
                session_title=session_title,
                speakers_in_chunk=speakers,
                chunk_position=0,
                total_chunks_in_session=0,
                content_tier=content_tier,
                content_type="transcript",
                source=source,
                topic=topic.topic_title,
                summary=topic.summary,
                text=text,
            ))
        else:
            # Large topic — sub-split using existing chunker, then generate sub-summaries
            logger.info(
                "Topic %r is %d tokens, sub-splitting (threshold: %d)",
                topic.topic_title, topic_tokens, max_topic_tokens,
            )
            sub_chunks = chunk_transcript(
                topic_turns,
                session_date=session_date,
                session_title=session_title,
                target_tokens=500,
                overlap_tokens=50,
                content_tier=content_tier,
                source=source,
            )
            for sub_chunk in sub_chunks:
                # Generate sub-summary via LLM
                # Strip header from text for the summary prompt
                text_for_summary = sub_chunk.text
                if text_for_summary.startswith(header):
                    text_for_summary = text_for_summary[len(header):]
                summary = _generate_sub_summary(topic.topic_title, text_for_summary)
                sub_chunk.topic = topic.topic_title
                sub_chunk.summary = summary
                all_chunks.append(sub_chunk)

    # Post-process: assign sequential IDs and totals
    total = len(all_chunks)
    for i, chunk in enumerate(all_chunks):
        chunk.chunk_position = i + 1
        chunk.total_chunks_in_session = total
        chunk.chunk_id = f"{session_date}-chunk-{i + 1:03d}"

    return all_chunks
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_topic_chunker.py -v
```

Expected: All 10 tests PASS.

- [ ] **Step 5: Run the full test suite**

```bash
pytest tests/ -v
```

Expected: All tests PASS (39 existing + 5 llm + 10 topic_chunker = 54).

- [ ] **Step 6: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/topic_chunker.py community-brain/tests/test_topic_chunker.py
git commit -m "feat(sp1-v2): add topic segmentation and chunk-by-topics

topic_chunker.py implements two-pass pipeline:
- segment_transcript(): LLM-based topic boundary detection
- chunk_by_topics(): topic-aware chunking with summaries
- Sub-splits oversized topics using existing chunk_transcript()
10 tests passing."
```

---

### Task 4: Update chunk_historical.py for Two-Pass Pipeline

**Files:**
- Modify: `community-brain/src/community_brain/backfill/chunk_historical.py`
- Modify: `community-brain/tests/test_chunk_historical.py`

- [ ] **Step 1: Update chunk_single_session to use two-pass pipeline**

In `community-brain/src/community_brain/backfill/chunk_historical.py`, replace the `chunk_single_session` function (lines 57-121) with:

```python
def chunk_single_session(
    transcript_path: Path,
    chunks_dir: Path,
    raw_chunks_path: Path,
    aliases: dict[str, str] | None = None,
    force: bool = False,
    use_llm: bool = True,
) -> dict | None:
    """Chunk a single transcript file using two-pass LLM pipeline.

    Pass 1: LLM segments transcript into discussion topics
    Pass 2: Chunks by topic boundaries with summaries

    If use_llm=False, falls back to the v1 sliding-window chunker.
    Returns session metadata or None if skipped.
    """
    session_date = _extract_date(transcript_path.name)
    if not session_date:
        logger.warning("Cannot extract date from %s, skipping", transcript_path.name)
        return None

    session_title = _extract_title(transcript_path.name)

    output_file = chunks_dir / f"session-{session_date}.md"
    if output_file.exists() and not force:
        logger.info("Skipped %s — already exists", session_date)
        return None

    text = transcript_path.read_text(encoding="utf-8")
    turns = parse_transcript(text)
    if not turns:
        logger.warning("No parseable turns in %s, skipping", transcript_path.name)
        return None

    if aliases:
        for turn in turns:
            turn.speaker = normalize_speaker(turn.speaker, aliases)

    if use_llm:
        from community_brain.topic_chunker import (
            chunk_by_topics,
            segment_transcript,
            _format_turn,
        )

        # Pass 1: Topic segmentation
        full_transcript = "\n".join(_format_turn(t) for t in turns)
        logger.info("Segmenting %s (%d turns)...", session_date, len(turns))
        topics = segment_transcript(full_transcript)
        logger.info("Found %d topics for %s", len(topics), session_date)

        # Pass 2: Chunk by topics
        chunks = chunk_by_topics(
            turns=turns,
            topics=topics,
            session_date=session_date,
            session_title=session_title,
            content_tier="historical",
            source="fathom_transcript",
        )
    else:
        chunks = chunk_transcript(
            turns,
            session_date=session_date,
            session_title=session_title,
            content_tier="historical",
            source="fathom_transcript",
        )

    if not chunks:
        logger.warning("No chunks produced for %s", session_date)
        return None

    chunks_dir.mkdir(parents=True, exist_ok=True)
    md_content = chunks_to_markdown(chunks, session_date, session_title)
    output_file.write_text(md_content, encoding="utf-8")

    raw_chunks_path.parent.mkdir(parents=True, exist_ok=True)
    jsonl_content = chunks_to_jsonl(chunks)
    with open(raw_chunks_path, "a", encoding="utf-8") as f:
        f.write(jsonl_content)

    all_speakers = sorted(set(
        speaker
        for chunk in chunks
        for speaker in chunk.speakers_in_chunk
    ))

    return {
        "date": session_date,
        "title": session_title,
        "content_tier": "historical",
        "chunk_count": len(chunks),
        "speakers": all_speakers,
        "duration_minutes": None,
    }
```

Also update the imports at the top of the file to include `_format_turn`:

```python
from community_brain.chunk_utils import (
    _format_turn,
    chunk_transcript,
    chunks_to_jsonl,
    chunks_to_markdown,
    normalize_speaker,
    parse_transcript,
)
```

- [ ] **Step 2: Update the CLI to add --no-llm flag**

In the `main()` function, add a new option and pass it through:

```python
@click.command()
@click.option("--date", "target_date", default=None, help="Chunk a specific session (YYYY-MM-DD)")
@click.option("--dry-run", is_flag=True, help="Show chunk counts without writing files")
@click.option("--force", is_flag=True, help="Re-chunk even if output already exists")
@click.option("--no-llm", is_flag=True, help="Use v1 sliding-window chunker instead of LLM pipeline")
def main(target_date: str | None, dry_run: bool, force: bool, no_llm: bool) -> None:
```

And in the loop where `chunk_single_session` is called:

```python
        result = chunk_single_session(
            transcript_path=f,
            chunks_dir=chunks_dir,
            raw_chunks_path=raw_chunks_path,
            aliases=aliases,
            force=force,
            use_llm=not no_llm,
        )
```

- [ ] **Step 3: Update test_chunk_historical.py**

Replace the content of `community-brain/tests/test_chunk_historical.py` with:

```python
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
        assert result["chunk_count"] >= 3  # at least one chunk per topic

        md_file = chunks_dir / "session-2025-01-15.md"
        assert md_file.exists()
        content = md_file.read_text()
        assert "### Topic: Vector Store Comparison" in content
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
```

- [ ] **Step 4: Run all tests**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/ -v
```

Expected: All tests PASS (~55 total).

- [ ] **Step 5: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/backfill/chunk_historical.py community-brain/tests/test_chunk_historical.py
git commit -m "feat(sp1-v2): update chunk_historical to use two-pass LLM pipeline

chunk_single_session() now uses topic segmentation + chunk-by-topics
by default. --no-llm flag falls back to v1 sliding window.
All tests passing."
```

---

### Task 5: Sample Validation — Re-chunk 3 Sessions with LLM Pipeline

This task requires real API calls to OpenRouter. Uses the 3 transcripts already in `raw-transcripts/`.

- [ ] **Step 1: Re-chunk the 3 sample sessions with v2 pipeline**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
python -m community_brain.backfill.chunk_historical --force 2>&1
```

Watch the output for:
- Topic count per session (expect 10-25)
- Any LLM errors or malformed JSON
- Total chunk count (expect fewer, more focused chunks than v1's 303)

- [ ] **Step 2: Inspect topic quality**

```bash
python3 -c "
import json
for line in open('raw-chunks/all-chunks.jsonl'):
    obj = json.loads(line)
    if obj['session_date'] == '2025-09-02':
        print(f'{obj[\"chunk_id\"]}: [{obj[\"topic\"]}] {obj[\"summary\"][:80]}...')
"
```

Check:
- Are topic titles descriptive and distinct?
- Do summaries accurately reflect the chunk content?
- Are there ~10-25 topics per session?

- [ ] **Step 3: Check token sizes**

```bash
source .venv/bin/activate
python3 -c "
import json
from community_brain.chunk_utils import count_tokens
sizes = []
for line in open('raw-chunks/all-chunks.jsonl'):
    obj = json.loads(line)
    tokens = count_tokens(obj['text'])
    sizes.append(tokens)
print(f'Total chunks: {len(sizes)}')
print(f'Min: {min(sizes)}, Max: {max(sizes)}, Avg: {sum(sizes)//len(sizes)}')
"
```

- [ ] **Step 4: Inspect markdown output**

```bash
head -60 chunks/historical/session-2025-09-02.md
```

Verify:
- Topic headers present (`### Topic: ...`)
- Summaries present (`**Summary:** ...`)
- Transcript text follows each summary
- Chunks separated by `---`

- [ ] **Step 5: Test in Open WebUI**

1. Commit and push the updated chunks
2. Pull on Mac Mini
3. Delete old "Test Historical" knowledge collection if it exists
4. Import `session-2025-09-02.md` into a new collection
5. Query: "What was discussed about Codex?"
6. Query: "What tools were mentioned for vector storage?"
7. Query: "Who participated in this call?"
8. Compare answer quality to v1 results

- [ ] **Step 6: Commit results**

```bash
cd /home/pchouinard/n8n
git add community-brain/chunks/ community-brain/raw-chunks/
git commit -m "data(sp1-v2): re-chunk 3 sample sessions with LLM topic pipeline

Topic-aware chunking with summaries. Quality validation pending."
```

- [ ] **Step 7: Push**

```bash
git push
```

---

## Verification Summary

SP1 v2 chunking is ready for bulk processing when:

| Check | Status |
|-------|--------|
| All unit tests pass (~55) | |
| Topic segmentation produces 10-25 topics per session | |
| Summaries accurately describe chunk content | |
| Markdown format correct (topic headers + summaries) | |
| JSONL includes topic and summary fields | |
| Open WebUI import works | |
| RAG queries return better results than v1 | |
| Cost per session ~$0.02 | |

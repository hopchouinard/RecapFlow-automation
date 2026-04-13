# Community Brain SP1: Backfill Pipeline — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the Python pipeline that fetches historical Fathom transcripts, chunks them with speaker-aware logic, and produces distribution-ready markdown + JSONL files.

**Architecture:** Python-first. Four modules: `chunk_utils.py` (shared chunking core), `fetch_fathom.py` (API fetcher), `chunk_historical.py` (orchestrator), and manifest generation. All code under `community-brain/src/community_brain/`. TDD — tests first, then implementation.

**Tech Stack:** Python 3.12, tiktoken, httpx, click, tqdm, python-dotenv, pytest

**Spec:** `docs/superpowers/specs/2026-04-13-community-brain-sp1-backfill-pipeline.md`

---

## File Map

| Action | Path | Responsibility |
|--------|------|---------------|
| Create | `community-brain/pyproject.toml` | Project config, dependencies |
| Create | `community-brain/.gitignore` | Ignore secrets, caches, raw-transcripts |
| Create | `community-brain/config/.env.example` | Env var template |
| Create | `community-brain/config/speaker-aliases.json` | Speaker name normalization (empty) |
| Create | `community-brain/src/community_brain/__init__.py` | Package init |
| Create | `community-brain/src/community_brain/chunk_utils.py` | Shared chunking logic |
| Create | `community-brain/src/community_brain/backfill/__init__.py` | Backfill package init |
| Create | `community-brain/src/community_brain/backfill/fetch_fathom.py` | Fathom API fetcher |
| Create | `community-brain/src/community_brain/backfill/chunk_historical.py` | Historical transcript chunker |
| Create | `community-brain/tests/test_chunk_utils.py` | Tests for chunking logic |
| Create | `community-brain/tests/test_backfill.py` | Tests for fetch + historical chunker |
| Create | `community-brain/tests/fixtures/sample-transcript.txt` | Test fixture: raw transcript |
| Exists | `community-brain/tests/fixtures/sample-session.md` | Already created in SP0 |

---

### Task 1: Python Project Setup

**Files:**
- Create: `community-brain/pyproject.toml`
- Create: `community-brain/.gitignore`
- Create: `community-brain/config/.env.example`
- Create: `community-brain/config/speaker-aliases.json`
- Create: `community-brain/src/community_brain/__init__.py`
- Create: `community-brain/src/community_brain/backfill/__init__.py`

- [ ] **Step 1: Install python3-pip and python3-venv**

The VM has Python 3.12 but no pip or venv. Install them:

```bash
sudo apt update && sudo apt install -y python3-pip python3-venv
```

If sudo requires a password, the user must run this manually via `! sudo apt install -y python3-pip python3-venv`.

- [ ] **Step 2: Create pyproject.toml**

Create `community-brain/pyproject.toml`:

```toml
[project]
name = "community-brain"
version = "0.1.0"
description = "Vectorized knowledge base from AI community coaching calls"
requires-python = ">=3.11"
license = {text = "MIT"}

dependencies = [
    "tiktoken>=0.7",
    "httpx>=0.27",
    "python-dotenv>=1.0",
    "click>=8.1",
    "tqdm>=4.66",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=5.0",
]

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.backends._legacy:_Backend"
```

- [ ] **Step 3: Create .gitignore**

Create `community-brain/.gitignore`:

```
config/.env
__pycache__/
*.pyc
.pytest_cache/
*.egg-info/
dist/
build/
.venv/
raw-transcripts/
```

- [ ] **Step 4: Create config files**

Create `community-brain/config/.env.example`:

```bash
# Fathom API (required for backfill)
FATHOM_API_KEY=

# Ollama endpoint (for future use in SP3)
OLLAMA_BASE_URL=http://10.1.50.219:11434

# OpenAI API key (optional, for SP3)
OPENAI_API_KEY=

# Open WebUI (for SP4 bulk import)
OPEN_WEBUI_URL=http://10.1.50.219:3000
```

Create `community-brain/config/speaker-aliases.json`:

```json
{}
```

- [ ] **Step 5: Create package init files**

Create `community-brain/src/community_brain/__init__.py`:

```python
"""Community Brain — vectorized knowledge base from AI community coaching calls."""
```

Create `community-brain/src/community_brain/backfill/__init__.py`:

```python
"""Backfill pipeline for historical Fathom transcripts."""
```

- [ ] **Step 6: Create virtual environment and install dependencies**

```bash
cd /home/pchouinard/n8n/community-brain
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Verify:

```bash
python -c "import tiktoken; print(tiktoken.__version__)"
python -c "import httpx; print(httpx.__version__)"
pytest --version
```

Expected: All imports succeed, versions printed.

- [ ] **Step 7: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/pyproject.toml community-brain/.gitignore community-brain/config/.env.example community-brain/config/speaker-aliases.json community-brain/src/community_brain/__init__.py community-brain/src/community_brain/backfill/__init__.py
git commit -m "feat(sp1): add Python project setup with dependencies

pyproject.toml, .gitignore, config templates, and package init files.
Dependencies: tiktoken, httpx, click, tqdm, python-dotenv, pytest."
```

---

### Task 2: Test Fixture — Sample Transcript

**Files:**
- Create: `community-brain/tests/fixtures/sample-transcript.txt`

- [ ] **Step 1: Create the sample transcript file**

Create `community-brain/tests/fixtures/sample-transcript.txt`:

```
[00:00:04] Patrick Chouinard: Hey everyone, welcome to this week's call. We've got a packed agenda today. We're going to talk about vector databases and then get into some hands-on RAG pipeline work.

[00:00:28] Alice Chen: Hi Patrick! Looking forward to it. I've been experimenting with Pinecone this week and have some interesting findings to share.

[00:00:45] Bob Martinez: Hey all. Quick question before we start — has anyone tried the new Weaviate release? They added some hybrid search features that look promising.

[00:01:15] Patrick Chouinard: I haven't tried it yet, Bob, but it's on my list. Let's make sure we cover that today. Alice, why don't you kick things off with your Pinecone findings?

[00:01:38] Alice Chen: Sure. So I set up a test with about fifty thousand document chunks. The indexing was fast, maybe ten minutes total. Query latency averaged around forty milliseconds. The real surprise was the metadata filtering. You can filter by date range, speaker, content type, all at query time without re-indexing.

[00:02:30] Bob Martinez: That's impressive. How does the cost compare to running something locally like FAISS or LanceDB?

[00:02:50] Alice Chen: That's the trade-off. Pinecone's free tier gives you one index with up to a hundred thousand vectors. Beyond that, it's about seventy dollars a month for the standard plan. For a community project where you want zero cost for end users, a local solution like LanceDB makes more sense.

[00:03:25] Patrick Chouinard: Exactly. And that aligns with our philosophy here. We want the community to be able to run everything locally without any API costs. LanceDB plus Ollama gives us that completely free stack.

[00:03:55] Carol Singh: I want to add something about the embedding model choice. I ran a comparison between nomic-embed-text and OpenAI's text-embedding-3-large on our transcript data. For conversational content like ours, the difference in retrieval quality is minimal. Maybe a two to three percent difference in recall at ten.

[00:04:30] Patrick Chouinard: That's really useful data, Carol. So the local model is basically as good as the paid one for our use case.

[00:04:45] Carol Singh: Exactly. The structure of conversational text is different from technical documentation. The vocabulary is more natural, the sentences are simpler, and the semantic relationships are more straightforward. Local embedding models handle that just fine.

[00:05:15] Bob Martinez: Makes sense. What about chunking strategy? I've been reading about different approaches and I'm not sure what works best for transcripts.

[00:05:40] Patrick Chouinard: Great question. For transcripts, I think speaker-aware chunking is the way to go. You never want to split in the middle of someone's statement. The natural boundaries are speaker transitions. You accumulate turns until you hit roughly five hundred tokens, then break at the nearest speaker change.

[00:06:15] Alice Chen: What about overlap? Do you include any content from the previous chunk in the next one?

[00:06:30] Patrick Chouinard: Yes, about fifty tokens of overlap. That way if someone asks a question at the end of one chunk and the answer starts at the beginning of the next, the retrieval system can still find the full context. The overlap turns are whole speaker turns though, not arbitrary token cuts.

[00:07:00] Bob Martinez: That makes a lot of sense. So the atomic unit is always a complete speaker turn.

[00:07:15] Patrick Chouinard: Right. A speaker turn is the smallest unit we work with. Never split mid-turn. If a single turn happens to be very long, say over a thousand tokens, it just becomes its own chunk. That's rare in conversational content though.

[00:07:45] Carol Singh: One more thing about metadata. Each chunk should carry its session date, speakers present, and position within the session. That way you can do filtered queries like show me everything Alice said about embeddings or find discussions from March twenty twenty six.

[00:08:20] Patrick Chouinard: Absolutely. The metadata is as important as the content for retrieval quality. Alright, let's shift to hands-on. Everyone open up your notebooks and let's build a chunker together.
```

This is ~750 words with 18 speaker turns across 4 speakers. It produces 2-3 chunks at ~500 tokens each and tests speaker boundaries, overlap, and metadata extraction.

- [ ] **Step 2: Verify the fixture**

```bash
wc -l community-brain/tests/fixtures/sample-transcript.txt
```

Expected: ~20 lines (18 speaker turns + blank lines between some).

```bash
wc -w community-brain/tests/fixtures/sample-transcript.txt
```

Expected: ~700-800 words.

- [ ] **Step 3: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/tests/fixtures/sample-transcript.txt
git commit -m "test(sp1): add sample transcript fixture for chunking tests

18 speaker turns across 4 speakers, ~750 words. Tests speaker-aware
chunking boundaries, overlap, and metadata extraction."
```

---

### Task 3: Transcript Parser + Speaker Normalizer (TDD)

**Files:**
- Create: `community-brain/tests/test_chunk_utils.py`
- Create: `community-brain/src/community_brain/chunk_utils.py`

- [ ] **Step 1: Write failing tests for parse_transcript and normalize_speaker**

Create `community-brain/tests/test_chunk_utils.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_chunk_utils.py -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'community_brain.chunk_utils'` or `ImportError`.

- [ ] **Step 3: Implement parse_transcript and normalize_speaker**

Create `community-brain/src/community_brain/chunk_utils.py`:

```python
"""Shared chunking utilities for Community Brain.

Provides transcript parsing, speaker normalization, token counting,
speaker-aware chunking, and output formatting (JSONL + markdown).
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

TRANSCRIPT_LINE_RE = re.compile(
    r"\[(\d{2}:\d{2}:\d{2})\]\s+(.+?):\s+(.*)"
)


@dataclass
class SpeakerTurn:
    """A single speaker turn from a transcript."""
    timestamp: str
    speaker: str
    text: str


def parse_transcript(text: str) -> list[SpeakerTurn]:
    """Parse raw transcript text into structured speaker turns.

    Each line is expected to match: [HH:MM:SS] Speaker Name: text
    Blank lines and unparseable lines are skipped with a warning.
    """
    turns: list[SpeakerTurn] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = TRANSCRIPT_LINE_RE.match(line)
        if not match:
            logger.warning("Skipping unparseable line: %s", line[:80])
            continue
        turns.append(SpeakerTurn(
            timestamp=match.group(1),
            speaker=match.group(2),
            text=match.group(3),
        ))
    return turns


def normalize_speaker(
    name: str,
    aliases: dict[str, str] | None = None,
) -> str:
    """Normalize a speaker name using an optional alias map."""
    if aliases and name in aliases:
        return aliases[name]
    return name
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_chunk_utils.py::TestParseTranscript -v
pytest tests/test_chunk_utils.py::TestNormalizeSpeaker -v
```

Expected: All 7 tests PASS.

- [ ] **Step 5: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/chunk_utils.py community-brain/tests/test_chunk_utils.py
git commit -m "feat(sp1): add transcript parser and speaker normalizer

parse_transcript() parses [HH:MM:SS] Speaker: text format.
normalize_speaker() applies optional alias mapping.
7 tests passing."
```

---

### Task 4: Token Counter (TDD)

**Files:**
- Modify: `community-brain/tests/test_chunk_utils.py`
- Modify: `community-brain/src/community_brain/chunk_utils.py`

- [ ] **Step 1: Write failing test for count_tokens**

Append to `community-brain/tests/test_chunk_utils.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_chunk_utils.py::TestCountTokens -v
```

Expected: FAIL — `ImportError: cannot import name 'count_tokens'`.

- [ ] **Step 3: Implement count_tokens**

Add to `community-brain/src/community_brain/chunk_utils.py`, after the `normalize_speaker` function:

```python
import tiktoken

_ENCODING = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    """Count tokens using cl100k_base encoding (standard for modern embedding models)."""
    return len(_ENCODING.encode(text))
```

Also add `tiktoken` to the imports at the top of the file (after `from dataclasses import ...`):

```python
import tiktoken
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_chunk_utils.py::TestCountTokens -v
```

Expected: All 4 tests PASS.

- [ ] **Step 5: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/chunk_utils.py community-brain/tests/test_chunk_utils.py
git commit -m "feat(sp1): add token counter using tiktoken cl100k_base

count_tokens() wraps tiktoken for consistent token counting.
4 tests passing."
```

---

### Task 5: Speaker-Aware Chunker (TDD)

**Files:**
- Modify: `community-brain/tests/test_chunk_utils.py`
- Modify: `community-brain/src/community_brain/chunk_utils.py`

- [ ] **Step 1: Write failing tests for chunk_transcript**

Append to `community-brain/tests/test_chunk_utils.py`:

```python
from pathlib import Path
from community_brain.chunk_utils import Chunk, chunk_transcript

FIXTURES = Path(__file__).parent / "fixtures"


class TestChunkTranscript:
    def _make_turns(self, count: int, words_per_turn: int = 50) -> list[SpeakerTurn]:
        """Helper: generate speaker turns with predictable token counts."""
        speakers = ["Alice", "Bob", "Carol"]
        turns = []
        for i in range(count):
            speaker = speakers[i % len(speakers)]
            # Each word is ~1-1.3 tokens; 50 words ≈ 55-65 tokens
            text = f"Word{i} " + "test content here please " * (words_per_turn // 3)
            turns.append(SpeakerTurn(
                timestamp=f"00:{i:02d}:00",
                speaker=speaker,
                text=text.strip(),
            ))
        return turns

    def test_basic_chunking(self):
        # 10 turns × ~60 tokens each ≈ 600 tokens → should produce 2+ chunks at 500-token target
        turns = self._make_turns(10)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        assert len(chunks) >= 2

    def test_speaker_boundary(self):
        # Every chunk's text should contain only complete [HH:MM:SS] Speaker: lines
        turns = self._make_turns(10)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        for chunk in chunks:
            # Remove the header line, check remaining lines
            lines = [
                l for l in chunk.text.split("\n")
                if l.strip() and not l.startswith("##")
            ]
            for line in lines:
                assert re.match(r"\[\d{2}:\d{2}:\d{2}\]", line), (
                    f"Non-turn line found in chunk: {line[:60]}"
                )

    def test_overlap(self):
        turns = self._make_turns(15)
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session")
        if len(chunks) < 2:
            return  # Can't test overlap with a single chunk
        # Last turn(s) of chunk N should appear at start of chunk N+1
        for i in range(len(chunks) - 1):
            current_lines = set(chunks[i].text.strip().split("\n"))
            next_lines = set(chunks[i + 1].text.strip().split("\n"))
            overlap = current_lines & next_lines
            # At least one non-header line should overlap
            overlap_content = {l for l in overlap if not l.startswith("##") and l.strip()}
            assert len(overlap_content) > 0, f"No overlap between chunks {i} and {i+1}"

    def test_long_turn_becomes_own_chunk(self):
        turns = [
            SpeakerTurn("00:00:00", "Alice", "short turn"),
            SpeakerTurn("00:01:00", "Bob", "word " * 600),  # ~600 tokens, exceeds target
            SpeakerTurn("00:02:00", "Alice", "another short turn"),
        ]
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session", target_tokens=500)
        # The long turn should be isolated in its own chunk
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
        """End-to-end test using the sample transcript fixture."""
        text = (FIXTURES / "sample-transcript.txt").read_text()
        turns = parse_transcript(text)
        assert len(turns) >= 15  # sanity check
        chunks = chunk_transcript(turns, "2025-01-15", "Vector DB Discussion")
        assert len(chunks) >= 2
        # All 4 speakers should appear across chunks
        all_speakers = set()
        for chunk in chunks:
            all_speakers.update(chunk.speakers_in_chunk)
        assert "Patrick Chouinard" in all_speakers
        assert "Alice Chen" in all_speakers
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_chunk_utils.py::TestChunkTranscript -v
```

Expected: FAIL — `ImportError: cannot import name 'Chunk'` or `cannot import name 'chunk_transcript'`.

- [ ] **Step 3: Implement Chunk dataclass and chunk_transcript**

Add to `community-brain/src/community_brain/chunk_utils.py`, after `count_tokens`:

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
    text: str


def _format_turn(turn: SpeakerTurn) -> str:
    """Format a speaker turn back to transcript line format."""
    return f"[{turn.timestamp}] {turn.speaker}: {turn.text}"


def chunk_transcript(
    turns: list[SpeakerTurn],
    session_date: str,
    session_title: str,
    target_tokens: int = 500,
    overlap_tokens: int = 50,
    content_tier: str = "historical",
    content_type: str = "transcript",
    source: str = "fathom_transcript",
) -> list[Chunk]:
    """Chunk speaker turns into overlapping, speaker-boundary-aware chunks.

    Algorithm:
    1. Accumulate turns until approaching target_tokens.
    2. At boundary, finalize chunk and start new one with overlap.
    3. Never split mid-turn. A single long turn becomes its own chunk.
    4. Overlap is whole turns from the end of the previous chunk.
    """
    if not turns:
        return []

    header = f"## Session: {session_title} | Date: {session_date}\n\n"
    header_tokens = count_tokens(header)

    chunks: list[Chunk] = []
    current_turns: list[SpeakerTurn] = []
    current_tokens = header_tokens

    def _finalize_chunk(chunk_turns: list[SpeakerTurn]) -> None:
        text = header + "\n".join(_format_turn(t) for t in chunk_turns)
        speakers = sorted(set(t.speaker for t in chunk_turns))
        chunks.append(Chunk(
            chunk_id="",  # set in post-processing
            session_date=session_date,
            session_title=session_title,
            speakers_in_chunk=speakers,
            chunk_position=0,  # set in post-processing
            total_chunks_in_session=0,  # set in post-processing
            content_tier=content_tier,
            content_type=content_type,
            source=source,
            text=text,
        ))

    def _get_overlap_turns(turns_list: list[SpeakerTurn]) -> list[SpeakerTurn]:
        """Get trailing turns that fit within overlap_tokens."""
        overlap: list[SpeakerTurn] = []
        tokens = 0
        for turn in reversed(turns_list):
            turn_tokens = count_tokens(_format_turn(turn))
            if tokens + turn_tokens > overlap_tokens:
                break
            overlap.insert(0, turn)
            tokens += turn_tokens
        return overlap

    for turn in turns:
        turn_text = _format_turn(turn)
        turn_tokens = count_tokens(turn_text)

        if turn_tokens > target_tokens:
            # Long turn: finalize current chunk if non-empty, then make long turn its own chunk
            if current_turns:
                _finalize_chunk(current_turns)
            logger.warning(
                "Turn at %s by %s is %d tokens (target: %d), making it its own chunk",
                turn.timestamp, turn.speaker, turn_tokens, target_tokens,
            )
            _finalize_chunk([turn])
            current_turns = []
            current_tokens = header_tokens
            continue

        if current_tokens + turn_tokens > target_tokens and current_turns:
            # Would exceed target — finalize and start new chunk with overlap
            _finalize_chunk(current_turns)
            overlap_turns = _get_overlap_turns(current_turns)
            current_turns = list(overlap_turns)
            current_tokens = header_tokens + sum(
                count_tokens(_format_turn(t)) for t in current_turns
            )

        current_turns.append(turn)
        current_tokens += turn_tokens

    # Finalize remaining turns
    if current_turns:
        _finalize_chunk(current_turns)

    # Post-process: set IDs, positions, and totals
    total = len(chunks)
    for i, chunk in enumerate(chunks):
        chunk.chunk_position = i + 1
        chunk.total_chunks_in_session = total
        chunk.chunk_id = f"{session_date}-chunk-{i + 1:03d}"

    return chunks
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_chunk_utils.py::TestChunkTranscript -v
```

Expected: All 8 tests PASS.

- [ ] **Step 5: Run the full test suite**

```bash
pytest tests/test_chunk_utils.py -v
```

Expected: All 19 tests PASS (7 parser + 4 token + 8 chunker).

- [ ] **Step 6: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/chunk_utils.py community-brain/tests/test_chunk_utils.py
git commit -m "feat(sp1): add speaker-aware transcript chunker

chunk_transcript() implements sliding window with speaker-boundary
awareness, configurable target/overlap tokens, and metadata population.
19 tests passing."
```

---

### Task 6: Output Formatters — JSONL + Markdown (TDD)

**Files:**
- Modify: `community-brain/tests/test_chunk_utils.py`
- Modify: `community-brain/src/community_brain/chunk_utils.py`

- [ ] **Step 1: Write failing tests for chunks_to_jsonl and chunks_to_markdown**

Append to `community-brain/tests/test_chunk_utils.py`:

```python
from community_brain.chunk_utils import chunks_to_jsonl, chunks_to_markdown


class TestChunksToJsonl:
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

    def test_roundtrip_metadata(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Hello."),
            SpeakerTurn("00:02:00", "Bob", "Hi."),
        ]
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session", target_tokens=5000)
        jsonl = chunks_to_jsonl(chunks)
        obj = json.loads(jsonl.strip().split("\n")[0])
        assert obj["session_date"] == "2024-03-15"
        assert obj["session_title"] == "Test Session"
        assert obj["content_tier"] == "historical"
        assert obj["chunk_position"] == 1


class TestChunksToMarkdown:
    def test_has_frontmatter(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Hello."),
            SpeakerTurn("00:02:00", "Bob", "Hi."),
        ]
        chunks = chunk_transcript(turns, "2024-03-15", "Test Session", target_tokens=5000)
        md = chunks_to_markdown(chunks, "2024-03-15", "Test Session")
        assert md.startswith("---\n")
        assert 'session_date: "2024-03-15"' in md
        assert 'session_title: "Test Session"' in md
        assert "content_tier: " in md
        assert "chunk_count: " in md

    def test_chunk_separators(self):
        turns = [SpeakerTurn(f"00:{i:02d}:00", "Alice", "word " * 60) for i in range(10)]
        chunks = chunk_transcript(turns, "2024-03-15", "Test", target_tokens=500)
        md = chunks_to_markdown(chunks, "2024-03-15", "Test")
        # Should have chunk headers
        assert "### Chunk 1 of " in md
        if len(chunks) > 1:
            assert "### Chunk 2 of " in md
        # Chunks separated by ---
        assert "\n---\n" in md

    def test_speakers_in_frontmatter(self):
        turns = [
            SpeakerTurn("00:01:00", "Alice", "Hello."),
            SpeakerTurn("00:02:00", "Bob", "Hi."),
            SpeakerTurn("00:03:00", "Alice", "Bye."),
        ]
        chunks = chunk_transcript(turns, "2024-03-15", "Test", target_tokens=5000)
        md = chunks_to_markdown(chunks, "2024-03-15", "Test")
        assert "Alice" in md.split("---")[1]  # frontmatter section
        assert "Bob" in md.split("---")[1]
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_chunk_utils.py::TestChunksToJsonl -v
pytest tests/test_chunk_utils.py::TestChunksToMarkdown -v
```

Expected: FAIL — `ImportError`.

- [ ] **Step 3: Implement chunks_to_jsonl and chunks_to_markdown**

Add to `community-brain/src/community_brain/chunk_utils.py`, after the `chunk_transcript` function. Also add `import json` and `from dataclasses import dataclass, asdict` at the top:

```python
def chunks_to_jsonl(chunks: list[Chunk]) -> str:
    """Serialize chunks to JSONL format (one JSON object per line)."""
    lines = []
    for chunk in chunks:
        obj = asdict(chunk)
        lines.append(json.dumps(obj, ensure_ascii=False))
    return "\n".join(lines) + "\n"


def chunks_to_markdown(
    chunks: list[Chunk],
    session_date: str,
    session_title: str,
) -> str:
    """Produce a markdown file with YAML frontmatter and chunks separated by ---."""
    if not chunks:
        return ""

    # Collect all speakers across all chunks
    all_speakers = sorted(set(
        speaker
        for chunk in chunks
        for speaker in chunk.speakers_in_chunk
    ))
    content_tier = chunks[0].content_tier

    # YAML frontmatter
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

    # Chunk sections
    sections = []
    total = len(chunks)
    for chunk in chunks:
        # Strip the header from chunk text (it's in each chunk's text field)
        # and replace with a chunk-specific subheader
        text_without_header = chunk.text
        header_prefix = f"## Session: {session_title} | Date: {session_date}\n\n"
        if text_without_header.startswith(header_prefix):
            text_without_header = text_without_header[len(header_prefix):]

        section = f"### Chunk {chunk.chunk_position} of {total}\n\n{text_without_header}"
        sections.append(section)

    body = f"\n## Session: {session_title} | Date: {session_date}\n\n"
    body += "\n\n---\n\n".join(sections)

    return frontmatter + body + "\n"
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_chunk_utils.py::TestChunksToJsonl -v
pytest tests/test_chunk_utils.py::TestChunksToMarkdown -v
```

Expected: All 5 tests PASS.

- [ ] **Step 5: Run the full test suite**

```bash
pytest tests/test_chunk_utils.py -v
```

Expected: All 24 tests PASS.

- [ ] **Step 6: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/chunk_utils.py community-brain/tests/test_chunk_utils.py
git commit -m "feat(sp1): add JSONL and markdown output formatters

chunks_to_jsonl() and chunks_to_markdown() produce distribution-ready
output formats. Markdown includes YAML frontmatter with session metadata.
24 tests passing."
```

---

### Task 7: Fathom API Fetcher (TDD)

**Files:**
- Create: `community-brain/tests/test_backfill.py`
- Create: `community-brain/src/community_brain/backfill/fetch_fathom.py`

- [ ] **Step 1: Write failing tests for fetch logic**

Create `community-brain/tests/test_backfill.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_backfill.py -v
```

Expected: FAIL — `ImportError`.

- [ ] **Step 3: Implement fetch_fathom.py**

Create `community-brain/src/community_brain/backfill/fetch_fathom.py`:

```python
"""Fetch coaching call transcripts from the Fathom API.

Usage:
    python -m community_brain.backfill.fetch_fathom
    python -m community_brain.backfill.fetch_fathom --after 2024-01-01 --before 2024-06-30
    python -m community_brain.backfill.fetch_fathom --dry-run
"""

from __future__ import annotations

import logging
import re
import time
from pathlib import Path

import click
import httpx
from dotenv import load_dotenv
from tqdm import tqdm

logger = logging.getLogger(__name__)

COACHING_TITLES = [
    "weekly coaching call",
    "ai developer accelerator — coaching call",
    "ai developer accelerator - coaching call",
]

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
RAW_TRANSCRIPTS_DIR = PROJECT_ROOT / "raw-transcripts"
CONFIG_DIR = PROJECT_ROOT / "config"


def is_coaching_call(title: str | None) -> bool:
    """Check if a meeting title matches known coaching call patterns."""
    if not title:
        return False
    return title.strip().lower() in COACHING_TITLES


def slugify_title(title: str) -> str:
    """Convert a title to a URL-safe slug."""
    slug = title.lower().strip()
    slug = re.sub(r"[—–]", "-", slug)  # em/en dash to hyphen
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def format_transcript_entries(entries: list[dict]) -> str:
    """Format Fathom API transcript entries into [HH:MM:SS] Speaker: text lines."""
    lines = []
    for entry in entries:
        speaker_obj = entry.get("speaker")
        if speaker_obj and isinstance(speaker_obj, dict):
            speaker = speaker_obj.get("display_name", "Unknown")
        else:
            speaker = "Unknown"
        timestamp = entry.get("timestamp", "00:00:00")
        text = entry.get("text", "")
        lines.append(f"[{timestamp}] {speaker}: {text}")
    return "\n".join(lines)


def _existing_dates(raw_dir: Path) -> set[str]:
    """Get set of dates that already have transcript files."""
    dates = set()
    if raw_dir.exists():
        for f in raw_dir.glob("*.txt"):
            match = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
            if match:
                dates.add(match.group(1))
    return dates


def _wait_for_rate_limit(response: httpx.Response) -> None:
    """Sleep if rate limit is close to being hit."""
    remaining = response.headers.get("RateLimit-Remaining")
    reset = response.headers.get("RateLimit-Reset")
    if remaining is not None and int(remaining) < 5 and reset is not None:
        wait_seconds = int(reset) + 1
        logger.info("Rate limit low (%s remaining), waiting %ds", remaining, wait_seconds)
        time.sleep(wait_seconds)


def _api_get(
    client: httpx.Client,
    url: str,
    params: dict | None = None,
    retries: int = 3,
) -> httpx.Response:
    """GET with retry and rate-limit handling."""
    for attempt in range(retries):
        try:
            response = client.get(url, params=params)
            if response.status_code == 429:
                reset = response.headers.get("RateLimit-Reset", "5")
                wait = int(reset) + 1
                logger.warning("Rate limited (429), waiting %ds", wait)
                time.sleep(wait)
                continue
            response.raise_for_status()
            _wait_for_rate_limit(response)
            return response
        except httpx.HTTPError as e:
            if attempt < retries - 1:
                backoff = 2 ** attempt
                logger.warning("Request failed (%s), retrying in %ds", e, backoff)
                time.sleep(backoff)
            else:
                raise
    raise RuntimeError("Exhausted retries")  # unreachable but satisfies type checker


def fetch_all_meetings(
    client: httpx.Client,
    base_url: str,
    after: str | None = None,
    before: str | None = None,
) -> list[dict]:
    """Page through all meetings from the Fathom API."""
    meetings = []
    params: dict = {}
    if after:
        params["created_after"] = after
    if before:
        params["created_before"] = before

    url = f"{base_url}/meetings"
    while True:
        response = _api_get(client, url, params=params)
        data = response.json()
        items = data.get("items", data) if isinstance(data, dict) else data
        if isinstance(items, list):
            meetings.extend(items)
        else:
            meetings.extend(items)

        # Handle pagination
        next_cursor = data.get("next_cursor") if isinstance(data, dict) else None
        if not next_cursor:
            break
        params["cursor"] = next_cursor

    return meetings


def fetch_transcript(
    client: httpx.Client,
    base_url: str,
    recording_id: str,
) -> list[dict]:
    """Fetch transcript entries for a specific recording."""
    response = _api_get(client, f"{base_url}/recordings/{recording_id}/transcript")
    return response.json()


@click.command()
@click.option("--after", default=None, help="Fetch meetings created after this date (YYYY-MM-DD)")
@click.option("--before", default=None, help="Fetch meetings created before this date (YYYY-MM-DD)")
@click.option("--dry-run", is_flag=True, help="List what would be fetched without downloading")
def main(after: str | None, before: str | None, dry_run: bool) -> None:
    """Fetch coaching call transcripts from the Fathom API."""
    import os

    load_dotenv(CONFIG_DIR / ".env")
    api_key = os.environ.get("FATHOM_API_KEY")
    if not api_key:
        raise click.ClickException("FATHOM_API_KEY not set. Copy config/.env.example to config/.env and fill it in.")

    base_url = "https://api.fathom.ai/external/v1"
    RAW_TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    existing = _existing_dates(RAW_TRANSCRIPTS_DIR)

    client = httpx.Client(
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30.0,
    )

    try:
        logger.info("Fetching meeting list from Fathom API...")
        meetings = fetch_all_meetings(client, base_url, after=after, before=before)
        logger.info("Found %d meetings total", len(meetings))

        coaching_calls = []
        for m in meetings:
            title = m.get("title", "")
            if is_coaching_call(title):
                coaching_calls.append(m)
            else:
                logger.info("Ignored: %s — %r (not a coaching call)", m.get("date", "?"), title)

        logger.info("Found %d coaching calls", len(coaching_calls))

        if dry_run:
            for m in coaching_calls:
                date = m.get("date", m.get("recording_start_time", "unknown"))[:10]
                title = m.get("title", "Untitled")
                status = "SKIP (exists)" if date in existing else "FETCH"
                click.echo(f"  [{status}] {date} — {title}")
            return

        fetched = 0
        skipped = 0
        total = len(coaching_calls)

        for m in tqdm(coaching_calls, desc="Fetching transcripts"):
            date = m.get("date", m.get("recording_start_time", "unknown"))[:10]
            title = m.get("title", "Untitled")
            recording_id = str(m.get("recording_id", m.get("id", "")))

            if date in existing:
                logger.info("Skipped %s — already exists", date)
                skipped += 1
                continue

            if not recording_id:
                logger.warning("No recording_id for %s — %s, skipping", date, title)
                continue

            try:
                entries = fetch_transcript(client, base_url, recording_id)
                formatted = format_transcript_entries(entries)
                slug = slugify_title(title)
                filename = f"{date}-{slug}.txt"
                (RAW_TRANSCRIPTS_DIR / filename).write_text(formatted, encoding="utf-8")
                fetched += 1
                existing.add(date)
                logger.info(
                    "Fetched %d/%d: %s — %s (%d entries)",
                    fetched, total - skipped, date, title, len(entries),
                )
            except Exception:
                logger.exception("Failed to fetch transcript for %s — %s", date, title)

        click.echo(f"\nDone. Fetched: {fetched}, Skipped: {skipped}, Errors: {total - fetched - skipped}")

    finally:
        client.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_backfill.py -v
```

Expected: All 11 tests PASS.

- [ ] **Step 5: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/backfill/fetch_fathom.py community-brain/tests/test_backfill.py
git commit -m "feat(sp1): add Fathom API transcript fetcher

fetch_fathom.py with CLI interface (--after, --before, --dry-run).
Handles pagination, rate limiting, resumability, and coaching call
title filtering. 11 tests passing."
```

---

### Task 8: Historical Chunker + Manifest (TDD)

**Files:**
- Modify: `community-brain/tests/test_backfill.py`
- Create: `community-brain/src/community_brain/backfill/chunk_historical.py`

- [ ] **Step 1: Write failing tests for chunk_historical and manifest**

Append to `community-brain/tests/test_backfill.py`:

```python
import os
import tempfile
from community_brain.backfill.chunk_historical import (
    chunk_single_session,
    generate_manifest,
    TIER_1_CUTOFF,
)


class TestChunkHistorical:
    def test_tier1_cutoff(self):
        assert TIER_1_CUTOFF == "2026-03-10"

    def test_chunk_single_session(self, tmp_path):
        # Set up directories
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

        # Markdown file created
        md_file = chunks_dir / "session-2025-01-15.md"
        assert md_file.exists()
        content = md_file.read_text()
        assert "---" in content
        assert "session_date:" in content

        # JSONL appended
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

        # Create existing output file
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
        assert result is None  # skipped


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
        # Sessions sorted by date
        assert data["sessions"][0]["date"] == "2024-10-15"
        assert data["sessions"][1]["date"] == "2025-01-15"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_backfill.py::TestChunkHistorical -v
pytest tests/test_backfill.py::TestManifest -v
```

Expected: FAIL — `ImportError`.

- [ ] **Step 3: Implement chunk_historical.py**

Create `community-brain/src/community_brain/backfill/chunk_historical.py`:

```python
"""Chunk historical Fathom transcripts into distribution-ready formats.

Usage:
    python -m community_brain.backfill.chunk_historical
    python -m community_brain.backfill.chunk_historical --date 2024-03-15
    python -m community_brain.backfill.chunk_historical --dry-run
"""

from __future__ import annotations

import json
import logging
import re
from datetime import date
from pathlib import Path

import click
from tqdm import tqdm

from community_brain.chunk_utils import (
    chunk_transcript,
    chunks_to_jsonl,
    chunks_to_markdown,
    normalize_speaker,
    parse_transcript,
)

logger = logging.getLogger(__name__)

TIER_1_CUTOFF = "2026-03-10"
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent


def _load_aliases(config_dir: Path) -> dict[str, str]:
    """Load speaker aliases from config."""
    aliases_path = config_dir / "speaker-aliases.json"
    if aliases_path.exists():
        return json.loads(aliases_path.read_text())
    return {}


def _extract_date(filename: str) -> str | None:
    """Extract YYYY-MM-DD from a filename."""
    match = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
    return match.group(1) if match else None


def _extract_title(filename: str) -> str:
    """Extract title from filename like 2024-03-15-weekly-coaching-call.txt."""
    name = Path(filename).stem  # remove .txt
    # Remove date prefix
    title_slug = re.sub(r"^\d{4}-\d{2}-\d{2}-?", "", name)
    if not title_slug:
        return "Coaching Call"
    # Convert slug back to title case
    return title_slug.replace("-", " ").title()


def chunk_single_session(
    transcript_path: Path,
    chunks_dir: Path,
    raw_chunks_path: Path,
    aliases: dict[str, str] | None = None,
    force: bool = False,
) -> dict | None:
    """Chunk a single transcript file. Returns session metadata or None if skipped."""
    session_date = _extract_date(transcript_path.name)
    if not session_date:
        logger.warning("Cannot extract date from %s, skipping", transcript_path.name)
        return None

    session_title = _extract_title(transcript_path.name)

    # Check if already processed
    output_file = chunks_dir / f"session-{session_date}.md"
    if output_file.exists() and not force:
        logger.info("Skipped %s — already exists", session_date)
        return None

    # Parse and chunk
    text = transcript_path.read_text(encoding="utf-8")
    turns = parse_transcript(text)
    if not turns:
        logger.warning("No parseable turns in %s, skipping", transcript_path.name)
        return None

    # Normalize speakers
    if aliases:
        for turn in turns:
            turn.speaker = normalize_speaker(turn.speaker, aliases)

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

    # Write markdown
    chunks_dir.mkdir(parents=True, exist_ok=True)
    md_content = chunks_to_markdown(chunks, session_date, session_title)
    output_file.write_text(md_content, encoding="utf-8")

    # Append JSONL
    raw_chunks_path.parent.mkdir(parents=True, exist_ok=True)
    jsonl_content = chunks_to_jsonl(chunks)
    with open(raw_chunks_path, "a", encoding="utf-8") as f:
        f.write(jsonl_content)

    # Collect speakers across all chunks
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


def generate_manifest(sessions: list[dict], manifest_path: Path) -> None:
    """Generate manifest.json from a list of session metadata dicts."""
    sessions_sorted = sorted(sessions, key=lambda s: s["date"])
    total_chunks = sum(s["chunk_count"] for s in sessions_sorted)

    manifest = {
        "version": "1.0.0",
        "last_updated": date.today().isoformat(),
        "total_sessions": len(sessions_sorted),
        "total_chunks": total_chunks,
        "tier_1_cutoff": TIER_1_CUTOFF,
        "sessions": sessions_sorted,
    }

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


@click.command()
@click.option("--date", "target_date", default=None, help="Chunk a specific session (YYYY-MM-DD)")
@click.option("--dry-run", is_flag=True, help="Show chunk counts without writing files")
@click.option("--force", is_flag=True, help="Re-chunk even if output already exists")
def main(target_date: str | None, dry_run: bool, force: bool) -> None:
    """Chunk historical transcripts into markdown and JSONL."""
    raw_dir = PROJECT_ROOT / "raw-transcripts"
    chunks_dir = PROJECT_ROOT / "chunks" / "historical"
    raw_chunks_path = PROJECT_ROOT / "raw-chunks" / "all-chunks.jsonl"
    manifest_path = PROJECT_ROOT / "chunks" / "manifest.json"
    config_dir = PROJECT_ROOT / "config"

    if not raw_dir.exists():
        raise click.ClickException(f"No raw-transcripts directory found at {raw_dir}")

    aliases = _load_aliases(config_dir)

    # Find transcript files
    transcript_files = sorted(raw_dir.glob("*.txt"))
    if target_date:
        transcript_files = [f for f in transcript_files if f.name.startswith(target_date)]

    # Filter to Tier 1 (before cutoff)
    tier1_files = []
    for f in transcript_files:
        file_date = _extract_date(f.name)
        if file_date and file_date < TIER_1_CUTOFF:
            tier1_files.append(f)

    if not tier1_files:
        click.echo("No Tier 1 transcripts found.")
        return

    if dry_run:
        click.echo(f"Found {len(tier1_files)} Tier 1 transcripts:")
        for f in tier1_files:
            text = f.read_text(encoding="utf-8")
            turns = parse_transcript(text)
            click.echo(f"  {f.name}: {len(turns)} turns")
        return

    # Clear JSONL if forcing re-chunk
    if force and raw_chunks_path.exists():
        raw_chunks_path.unlink()

    sessions = []
    for f in tqdm(tier1_files, desc="Chunking transcripts"):
        result = chunk_single_session(
            transcript_path=f,
            chunks_dir=chunks_dir,
            raw_chunks_path=raw_chunks_path,
            aliases=aliases,
            force=force,
        )
        if result:
            sessions.append(result)

    # Generate manifest (include any existing sessions from previous runs)
    # Re-scan chunks directory for all session files
    all_sessions = list(sessions)  # start with what we just processed
    for md_file in sorted(chunks_dir.glob("session-*.md")):
        file_date = _extract_date(md_file.name.replace("session-", ""))
        if file_date and not any(s["date"] == file_date for s in all_sessions):
            # Existing session not in current run — read metadata from file
            content = md_file.read_text(encoding="utf-8")
            # Count chunks by counting "### Chunk " headers
            chunk_count = content.count("### Chunk ")
            all_sessions.append({
                "date": file_date,
                "title": "Coaching Call",
                "content_tier": "historical",
                "chunk_count": chunk_count,
                "speakers": [],
                "duration_minutes": None,
            })

    generate_manifest(all_sessions, manifest_path)

    click.echo(
        f"\nDone. Chunked {len(sessions)} sessions → "
        f"{sum(s['chunk_count'] for s in sessions)} chunks. "
        f"Manifest updated with {len(all_sessions)} total sessions."
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pytest tests/test_backfill.py -v
```

Expected: All 15 tests PASS (11 fetch + 3 chunk_historical + 1 manifest).

- [ ] **Step 5: Run the full test suite**

```bash
pytest tests/ -v
```

Expected: All 39 tests PASS (24 chunk_utils + 15 backfill).

- [ ] **Step 6: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/backfill/chunk_historical.py community-brain/tests/test_backfill.py
git commit -m "feat(sp1): add historical chunker and manifest generator

chunk_historical.py processes raw transcripts into markdown + JSONL.
generate_manifest() creates chunks/manifest.json.
CLI with --date, --dry-run, --force flags.
39 tests passing across all modules."
```

---

### Task 9: Sample Validation — Fetch + Chunk 3-5 Real Sessions

This task requires the `FATHOM_API_KEY` to be set. It's a manual verification step.

**Files:**
- Create: `community-brain/config/.env` (from .env.example, with real API key)
- Generated: `community-brain/raw-transcripts/*.txt`
- Generated: `community-brain/chunks/historical/session-*.md`
- Generated: `community-brain/raw-chunks/all-chunks.jsonl`
- Generated: `community-brain/chunks/manifest.json`

- [ ] **Step 1: Set up config/.env**

```bash
cd /home/pchouinard/n8n/community-brain
cp config/.env.example config/.env
# Edit config/.env and add FATHOM_API_KEY
```

- [ ] **Step 2: Fetch a small sample**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
python -m community_brain.backfill.fetch_fathom --dry-run
```

Review the dry-run output. Then fetch 3-5 sessions:

```bash
python -m community_brain.backfill.fetch_fathom --after 2025-06-01 --before 2025-09-01
```

Verify files appeared:

```bash
ls -la raw-transcripts/
head -20 raw-transcripts/*.txt
```

- [ ] **Step 3: Chunk the sample**

```bash
python -m community_brain.backfill.chunk_historical
```

Verify output:

```bash
ls -la chunks/historical/
cat chunks/manifest.json
wc -l raw-chunks/all-chunks.jsonl
```

- [ ] **Step 4: Inspect chunk quality**

For each output file, check:
- Chunk sizes: `python3 -c "import json; [print(f'{json.loads(l)[\"chunk_id\"]}: {len(json.loads(l)[\"text\"].split())} words') for l in open('raw-chunks/all-chunks.jsonl')]"`
- Speaker boundaries: open a markdown file, confirm no mid-turn splits
- Metadata: spot-check chunk_id format, speakers, positions

- [ ] **Step 5: Test in Open WebUI**

1. Copy a markdown file to the Mac Mini
2. Import into Open WebUI Knowledge
3. Query with specific questions about the session content
4. Verify correct answers grounded in the document

- [ ] **Step 6: Review speaker names**

```bash
python3 -c "
import json
speakers = set()
for line in open('raw-chunks/all-chunks.jsonl'):
    obj = json.loads(line)
    speakers.update(obj['speakers_in_chunk'])
print('\n'.join(sorted(speakers)))
"
```

Check for inconsistencies. If found, update `config/speaker-aliases.json`.

- [ ] **Step 7: Sign off on chunk quality**

User reviews and confirms:
- Chunk sizes acceptable (~400-600 tokens)
- Speaker boundaries correct
- Metadata complete
- RAG queries return relevant results

After sign-off, proceed to bulk processing (Task 10).

---

### Task 10: Bulk Processing — All Historical Sessions

This task runs after the user signs off on sample quality in Task 9.

- [ ] **Step 1: Fetch all remaining sessions**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
python -m community_brain.backfill.fetch_fathom
```

Review output. Note any sessions that need to come from Brandon's manual track.

- [ ] **Step 2: Place any manually downloaded transcripts**

For sessions from Brandon's Fathom account, download from the website and save to `raw-transcripts/YYYY-MM-DD-slugified-title.txt`.

- [ ] **Step 3: Chunk all transcripts**

```bash
python -m community_brain.backfill.chunk_historical --force
```

- [ ] **Step 4: Verify totals**

```bash
cat chunks/manifest.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Sessions: {d[\"total_sessions\"]}, Chunks: {d[\"total_chunks\"]}')"
ls chunks/historical/ | wc -l
wc -l raw-chunks/all-chunks.jsonl
```

Expected: ~78 sessions, ~8,000-12,000 chunks.

- [ ] **Step 5: Run full test suite**

```bash
pytest tests/ -v
```

Expected: All tests PASS.

- [ ] **Step 6: Commit chunked output**

```bash
cd /home/pchouinard/n8n
git add community-brain/chunks/ community-brain/raw-chunks/
git commit -m "data(sp1): add all historical session chunks

$(cat community-brain/chunks/manifest.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'{d[\"total_sessions\"]} sessions, {d[\"total_chunks\"]} chunks')")
Tier 1 content: transcript-only, pre-March 10 2026."
```

- [ ] **Step 7: Push to GitHub**

```bash
git push
```

---

## Verification Summary

SP1 is complete when:

| Check | Status |
|-------|--------|
| All unit tests pass (39+) | |
| Sample reviewed and approved by project owner | |
| All ~78 historical sessions fetched | |
| All sessions chunked to markdown + JSONL | |
| manifest.json accurate | |
| Sample imported into Open WebUI with correct RAG results | |
| Speaker aliases populated if needed | |
| All committed and pushed | |

# Community Brain — Sub-project 1: Backfill Pipeline

**Date:** 2026-04-13
**Status:** Draft
**Parent:** [Master Architecture](2026-04-12-community-brain-architecture.md)
**Depends on:** Sub-project 0 (Open WebUI verified and running)

---

## 1. Goal

Fetch all ~78 historical coaching call transcripts from the Fathom API, chunk them using speaker-aware sliding window logic, and produce distribution-ready markdown files and JSONL for the Community Brain knowledge base. Validate chunk quality against Open WebUI before bulk processing.

---

## 2. Scope

This sub-project delivers four components:

1. **`fetch_fathom.py`** — Fetches raw transcripts from Fathom API
2. **`chunk_utils.py`** — Shared chunking logic (reused by SP2)
3. **`chunk_historical.py`** — Orchestrates chunking of historical transcripts
4. **`manifest.json`** — Index of all chunked sessions

### Out of Scope

- Enriched (Tier 2) chunking — that's SP2
- Embedding into LanceDB — that's SP3
- Open WebUI bulk import script — that's SP4
- Brandon's sessions from his Fathom account — those are manually downloaded and placed into `raw-transcripts/` (manual track, documented in this spec)

---

## 3. Input Data

### 3.1 Fathom API

**Endpoint:** `https://api.fathom.ai/external/v1/`

**Authentication:** Bearer token via `FATHOM_API_KEY` environment variable.

**Rate limit:** 60 calls per 60-second window. Headers: `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset`.

**Relevant endpoints:**
- `GET /meetings` — List meetings. Supports `created_after` and `created_before` query params (ISO 8601). Paginated (default 10 items per page).
- `GET /recordings/{recording_id}/transcript` — Fetch transcript for a specific recording. Returns JSON array of `{speaker: {display_name}, timestamp, text}` objects.

**Coaching call identification:** Filter by title matching either:
- `"Weekly Coaching Call"`
- `"AI Developer Accelerator — Coaching Call"`

Case-insensitive match. Log any recordings with non-matching titles for manual review.

### 3.2 Manual Track (Brandon's Sessions)

Some historical sessions are on Brandon's Fathom account and cannot be fetched via API. These are manually downloaded from the Fathom website and placed into `community-brain/raw-transcripts/` with the naming convention:

```
YYYY-MM-DD-session-title.txt
```

The session title portion is slugified (lowercase, hyphens for spaces, no special characters). Example: `2024-06-15-weekly-coaching-call.txt`

### 3.3 Transcript Format

Each line follows:
```
[HH:MM:SS] Speaker Name: Transcript text
```

Example:
```
[00:05:07] Patrick Chouinard: Hey, Ty.
[00:05:09] Ty Wells: How's it going?
[00:06:00] Patrick Chouinard: Did you have the chance to try Claude Speak?
```

- One entry per line, plain UTF-8 text
- Timestamp: always `[HH:MM:SS]` (8 chars in brackets)
- Speaker: variable length, followed by `: `
- Text: remainder of line, can contain punctuation and special characters

---

## 4. Components

### 4.1 Fathom Fetch (`src/community_brain/backfill/fetch_fathom.py`)

**CLI interface:**
```bash
# Fetch all coaching calls
python -m community_brain.backfill.fetch_fathom

# Fetch specific date range
python -m community_brain.backfill.fetch_fathom --after 2024-01-01 --before 2024-06-30

# Dry run — list what would be fetched without downloading
python -m community_brain.backfill.fetch_fathom --dry-run
```

**Behavior:**
1. Read `FATHOM_API_KEY` from environment (via `python-dotenv` loading `config/.env`)
2. Page through `GET /meetings` with `created_after`/`created_before` filters
3. For each meeting:
   - Check title matches coaching call pattern (case-insensitive)
   - Skip if `raw-transcripts/YYYY-MM-DD-*.txt` already exists for that date
   - Fetch transcript via `GET /recordings/{recording_id}/transcript`
   - Format as `[HH:MM:SS] Speaker: text` (one line per entry)
   - Save to `raw-transcripts/YYYY-MM-DD-{slugified-title}.txt`
4. Log progress: `Fetched 15/78: 2024-03-15 — Weekly Coaching Call (92 entries)`
5. Log skipped: `Skipped 2024-03-15 — already exists`
6. Log non-matching: `Ignored: 2024-05-20 — "Team Standup" (not a coaching call)`

**Rate limiting:**
- Read `RateLimit-Remaining` header after each call
- If remaining < 5, sleep until `RateLimit-Reset`
- On 429 response, wait per `RateLimit-Reset` header + 1 second buffer
- Estimated total calls: ~156 (pagination calls + one transcript fetch per session)
- Estimated time: ~3 minutes with pacing

**Error handling:**
- Network errors: retry up to 3 times with exponential backoff (1s, 2s, 4s)
- Missing transcript: log warning, skip session, continue
- Partial run: resumable by default (skips existing files)

**Output:** Raw transcript files in `community-brain/raw-transcripts/`

### 4.2 Chunking Utilities (`src/community_brain/chunk_utils.py`)

This is the shared core used by both SP1 (historical) and SP2 (enriched).

#### 4.2.1 Transcript Parser

**Function:** `parse_transcript(text: str) -> list[SpeakerTurn]`

Parses raw transcript text into structured speaker turns.

```python
@dataclass
class SpeakerTurn:
    timestamp: str       # "HH:MM:SS"
    speaker: str         # "Patrick Chouinard"
    text: str            # The spoken text
```

**Behavior:**
- Split input by lines
- Parse each line with regex: `\[(\d{2}:\d{2}:\d{2})\]\s+(.+?):\s+(.*)`
- Skip blank lines
- Log warning for unparseable lines (don't fail)

#### 4.2.2 Speaker Normalizer

**Function:** `normalize_speaker(name: str, aliases: dict[str, str] | None = None) -> str`

Applies alias mapping from `config/speaker-aliases.json` if provided.

```python
normalize_speaker("Patchou", {"Patchou": "Patrick Chouinard"})
# → "Patrick Chouinard"

normalize_speaker("Alice Chen", None)
# → "Alice Chen" (no change)
```

#### 4.2.3 Token Counter

**Function:** `count_tokens(text: str) -> int`

Counts tokens using `tiktoken` with the `cl100k_base` encoding (standard for modern embedding models).

#### 4.2.4 Speaker-Aware Chunker

**Function:** `chunk_transcript(turns: list[SpeakerTurn], session_date: str, session_title: str, target_tokens: int = 500, overlap_tokens: int = 50) -> list[Chunk]`

```python
@dataclass
class Chunk:
    chunk_id: str                # "2024-03-15-chunk-042"
    session_date: str            # "2024-03-15"
    session_title: str           # "Weekly Coaching Call"
    speakers_in_chunk: list[str] # ["Patrick Chouinard", "Alice Chen"]
    chunk_position: int          # 42
    total_chunks_in_session: int # 87 (set after all chunks created)
    content_tier: str            # "historical"
    content_type: str            # "transcript"
    source: str                  # "fathom_transcript"
    text: str                    # The chunk text with header
```

**Algorithm:**
1. Start with empty accumulator
2. For each speaker turn:
   - Count tokens in the turn
   - If adding this turn would exceed `target_tokens`:
     - Finalize current chunk
     - Start new chunk with overlap: include the last ~`overlap_tokens` worth of turns from the previous chunk
   - Add turn to accumulator
3. Finalize last chunk
4. Post-process: set `total_chunks_in_session` on all chunks
5. Each chunk's `text` field includes a header line: `## Session: {title} | Date: {date}\n\n`

**Boundary rules:**
- Never split mid-turn (a speaker turn is the atomic unit)
- If a single turn exceeds `target_tokens`, it becomes its own chunk (log warning for turns over 1000 tokens)
- Overlap is measured in tokens, but the unit is whole turns — include as many trailing turns from the previous chunk as fit within `overlap_tokens`

#### 4.2.5 Output Formatters

**Function:** `chunks_to_jsonl(chunks: list[Chunk]) -> str`

Serializes chunks to JSONL format (one JSON object per line).

**Function:** `chunks_to_markdown(chunks: list[Chunk], session_date: str, session_title: str) -> str`

Produces a markdown file with YAML frontmatter and chunks separated by `---`:

```markdown
---
session_date: "2024-03-15"
session_title: "Weekly Coaching Call"
content_tier: "historical"
speakers: ["Patrick Chouinard", "Alice Chen", "Bob Martinez"]
chunk_count: 87
---

## Session: Weekly Coaching Call | Date: 2024-03-15

### Chunk 1 of 87

[00:05:07] Patrick Chouinard: Hey everyone...
[00:05:09] Alice Chen: Hi Patrick...

---

### Chunk 2 of 87

[00:10:30] Bob Martinez: I wanted to share...
```

### 4.3 Historical Chunker (`src/community_brain/backfill/chunk_historical.py`)

**CLI interface:**
```bash
# Chunk all transcripts in raw-transcripts/
python -m community_brain.backfill.chunk_historical

# Chunk a specific session
python -m community_brain.backfill.chunk_historical --date 2024-03-15

# Dry run — show chunk counts without writing files
python -m community_brain.backfill.chunk_historical --dry-run
```

**Behavior:**
1. Scan `raw-transcripts/` for all `.txt` files
2. Filter to dates before March 10, 2026 (Tier 1 boundary)
3. For each transcript:
   - Parse with `parse_transcript()`
   - Normalize speakers with `normalize_speaker()`
   - Chunk with `chunk_transcript()`
   - Write markdown to `chunks/historical/session-YYYY-MM-DD.md`
   - Append JSONL to `raw-chunks/all-chunks.jsonl`
4. Generate/update `chunks/manifest.json`
5. Log summary: `Chunked 78 sessions → 9,847 chunks (avg 126 per session)`

**Resumability:** Skip sessions that already have a file in `chunks/historical/`. Use `--force` to re-chunk everything.

### 4.4 Manifest Generator

Integrated into `chunk_historical.py` (and later `chunk_enriched.py` in SP2).

**Output:** `chunks/manifest.json`

```json
{
  "version": "1.0.0",
  "last_updated": "2026-04-13",
  "total_sessions": 78,
  "total_chunks": 9847,
  "tier_1_cutoff": "2026-03-10",
  "sessions": [
    {
      "date": "2024-10-15",
      "title": "Weekly Coaching Call",
      "content_tier": "historical",
      "chunk_count": 85,
      "speakers": ["Patrick Chouinard", "Alice Chen", "Bob Martinez"],
      "duration_minutes": null
    }
  ]
}
```

- `duration_minutes`: populated from Fathom API metadata if available, otherwise `null`
- Sessions sorted by date ascending
- Regenerated in full each time (not incrementally patched)

---

## 5. Project Setup

### 5.1 Python Project Configuration

**`community-brain/pyproject.toml`:**

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

Only SP1 dependencies are included. SP3 will add `lancedb`, `openai`, `ollama`, `fastapi`, `uvicorn`.

### 5.2 Environment Configuration

**`community-brain/config/.env.example`:**

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

**`community-brain/config/.env`** — actual secrets, gitignored.

**`community-brain/.gitignore`:**

```
config/.env
__pycache__/
*.pyc
.pytest_cache/
*.egg-info/
raw-transcripts/
```

Note: `raw-transcripts/` is gitignored because raw Fathom transcripts are large and are an intermediate artifact. The chunked output in `chunks/` is what gets committed and distributed.

### 5.3 Speaker Aliases

**`community-brain/config/speaker-aliases.json`:**

```json
{}
```

Starts empty. After the sample review (verification gate), populate with any inconsistencies found.

---

## 6. Testing Strategy

### 6.1 Unit Tests

**`tests/test_chunk_utils.py`:**

Tests for the shared chunking logic:

- `test_parse_transcript_basic` — Parse 3-line transcript, verify speaker/timestamp/text extraction
- `test_parse_transcript_blank_lines` — Blank lines are skipped
- `test_parse_transcript_unparseable` — Malformed lines logged as warnings, not failures
- `test_normalize_speaker_with_alias` — Alias mapping works
- `test_normalize_speaker_without_alias` — No-op when no aliases configured
- `test_count_tokens` — Token count returns reasonable values (not zero, not wildly off)
- `test_chunk_transcript_basic` — 10 short turns → 1-2 chunks of ~500 tokens
- `test_chunk_transcript_speaker_boundary` — Chunks never split mid-turn
- `test_chunk_transcript_overlap` — Consecutive chunks share ~50 tokens of content
- `test_chunk_transcript_long_turn` — Single turn exceeding target gets its own chunk
- `test_chunk_transcript_metadata` — chunk_id, session_date, speakers_in_chunk populated correctly
- `test_chunk_transcript_total_set` — total_chunks_in_session set on all chunks after processing
- `test_chunks_to_jsonl` — JSONL output parses back to valid JSON objects
- `test_chunks_to_markdown` — Markdown output has YAML frontmatter and `---` separators

**`tests/test_backfill.py`:**

Tests for the fetch and historical chunking:

- `test_fetch_title_filter` — Only coaching call titles pass the filter
- `test_fetch_skip_existing` — Already-fetched dates are skipped
- `test_chunk_historical_end_to_end` — Sample transcript file → markdown + JSONL output
- `test_manifest_generation` — Manifest contains correct session count, chunk counts, dates

### 6.2 Test Fixtures

**`tests/fixtures/sample-transcript.txt`:**

A ~50 line transcript (subset of a real session, or fabricated) in the exact Fathom format. Used by unit tests.

**`tests/fixtures/sample-session.md`:**

Already exists from SP0. Represents expected output format.

### 6.3 Integration Test

After unit tests pass, run `chunk_historical.py` against 3-5 real transcripts fetched from Fathom. Manually inspect:

- Chunk sizes (~500 tokens each)
- Speaker boundaries (no mid-turn splits)
- Metadata completeness
- Markdown renders correctly
- Import into Open WebUI → query → correct results

---

## 7. Verification Gate

Sub-project 1 is complete when:

### 7.1 Sample Validation (before bulk processing)

- [ ] `fetch_fathom.py` successfully fetches 3-5 transcripts from Fathom API
- [ ] `chunk_historical.py` produces markdown and JSONL for those sessions
- [ ] Chunk sizes are in the ~400-600 token range
- [ ] No chunks split mid-speaker-turn
- [ ] Metadata (chunk_id, session_date, speakers, positions) is correct
- [ ] Markdown files import into Open WebUI successfully
- [ ] RAG queries against imported chunks return relevant results
- [ ] Speaker aliases populated if inconsistencies found
- [ ] Project owner signs off on chunk quality

### 7.2 Bulk Processing (after sign-off)

- [ ] All ~78 historical sessions fetched (API + manual track)
- [ ] All sessions chunked — markdown in `chunks/historical/`, JSONL in `raw-chunks/`
- [ ] `manifest.json` reflects all sessions with accurate counts
- [ ] All unit tests pass
- [ ] Files committed to repo

---

## 8. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Fathom API pagination quirks | Test with small date ranges first; log raw API responses in debug mode |
| Some sessions missing from API | Manual track: download from Fathom website, place in `raw-transcripts/` |
| Speaker name inconsistencies | Review after sample run; populate `speaker-aliases.json` |
| Very long speaker turns (>1000 tokens) | Log warning; turn becomes its own chunk |
| Fathom transcript format changes | Format is simple and stable; parser logs warnings for unparseable lines |
| `raw-transcripts/` grows large | Gitignored; intermediate artifact not committed |

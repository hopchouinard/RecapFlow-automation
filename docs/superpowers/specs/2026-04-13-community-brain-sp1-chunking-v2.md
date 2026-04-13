# Community Brain — SP1 Addendum: Two-Pass LLM-Enhanced Chunking (v2)

**Date:** 2026-04-13
**Status:** Draft
**Parent:** [SP1 Backfill Pipeline](2026-04-13-community-brain-sp1-backfill-pipeline.md)

---

## 1. Motivation

Testing the v1 sliding-window chunker against Open WebUI showed mediocre retrieval quality. A query about "Codex" returned no results because the brief Codex discussion was diluted across a 500-token chunk dominated by other topics. The embedding vector averaged across multiple topics, making it a weak match for any single-topic query.

**Root cause:** Fixed-size sliding windows don't respect topic boundaries. Each chunk covers 2-3 minutes of unrelated conversation, producing unfocused embeddings.

**Solution:** Two-pass LLM-enhanced chunking that segments by topic and generates summaries for search.

---

## 2. Architecture: Two-Pass Pipeline

### Pass 1: Topic Segmentation

Send the full transcript to an LLM. Ask it to identify discrete discussion topics with timestamp boundaries.

**Input:** Full transcript text (~1,500 turns, ~30K-50K tokens)

**LLM:** Gemini 3.1 Flash Lite Preview via OpenRouter (`google/gemini-3.1-flash-lite-preview`)
- 1,048,576 token context window (handles any transcript)
- $0.25/M input, $1.50/M output
- Fast, lightweight — ideal for pattern recognition tasks

**Prompt:**
```
You are segmenting a coaching call transcript into discussion topics.

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
- Output as JSON array

Transcript:
{transcript_text}
```

**Output:** JSON array of topics:
```json
[
  {
    "topic_title": "Trying Codex Inside Cursor",
    "start_timestamp": "00:02:29",
    "end_timestamp": "00:05:10",
    "summary": "Patrick asks if anyone has tried the new Codex inside Cursor. Shakur hasn't yet. Brief discussion about falling behind on new tool releases."
  },
  {
    "topic_title": "GPU Benchmarks for Running Local Models",
    "start_timestamp": "00:05:10",
    "end_timestamp": "00:12:45",
    "summary": "Group compares GPU requirements for running Mistral, LLaMA, and GPT-OSS locally. Brandon shares benchmarks from his RTX 4090 setup."
  }
]
```

### Pass 2: Chunk by Topic + Summarize

For each topic from Pass 1:

1. **Extract turns** between `start_timestamp` and `end_timestamp`
2. **If topic ≤ 800 tokens:** One chunk for the whole topic. The summary from Pass 1 is used directly.
3. **If topic > 800 tokens:** Sub-split at speaker boundaries using the existing sliding-window chunker (~500 tokens, ~50 token overlap). Generate a sub-summary for each sub-chunk via a second LLM call.

**Sub-summary prompt (for oversized topics only):**
```
Summarize this section of a coaching call transcript in 1-2 sentences.
Focus on the specific points discussed, tools mentioned, and conclusions reached.

Topic: {topic_title}
Transcript section:
{chunk_text}
```

---

## 3. Updated Chunk Schema

Two new fields: `topic` and `summary`.

```python
@dataclass
class Chunk:
    chunk_id: str
    session_date: str
    session_title: str
    speakers_in_chunk: list[str]
    chunk_position: int
    total_chunks_in_session: int
    content_tier: str
    content_type: str
    source: str
    topic: str              # NEW: topic title from segmentation
    summary: str            # NEW: LLM-generated summary
    text: str               # Full transcript text for this chunk
```

---

## 4. Updated Markdown Output Format

The markdown files now include topic and summary prominently, so Open WebUI embeds them as part of the chunk:

```markdown
---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
speakers: ["Patrick Chouinard", "Shakur", "Ty Wells", ...]
chunk_count: 15
---

## Session: Weekly Coaching Call | Date: 2025-09-02

### Topic: Trying Codex Inside Cursor

**Summary:** Patrick asks if anyone has tried the new Codex inside Cursor. Shakur hasn't yet. Brief discussion about falling behind on new tool releases.

[00:02:29] Patrick Chouinard: Did anybody get the chance to try the new codex?
[00:02:36] Shakur: No, not yet.
[00:02:38] Shakur: Did you get to?
[00:02:42] Patrick Chouinard: Very, very quickly. A couple of prompts, but nothing more.
[00:02:47] Patrick Chouinard: That's why I was wondering if anybody tried it inside of Cursor.

---

### Topic: GPU Benchmarks for Running Local Models (1 of 3)

**Summary:** Brandon shares RTX 4090 benchmarks showing Mistral 7B runs at 45 tokens/sec locally. Group discusses minimum VRAM requirements for different model sizes.

[00:05:10] Brandon Hancock: So I ran some benchmarks this week...
...
```

This format means:
- Open WebUI sees "Topic: Trying Codex Inside Cursor" + the summary + the transcript text
- The embedding naturally captures the topic focus
- Queries like "Codex" will strongly match this chunk

---

## 5. Updated JSONL Output Format

For LanceDB (Path B), the JSONL includes both fields:

```json
{
  "chunk_id": "2025-09-02-chunk-001",
  "session_date": "2025-09-02",
  "session_title": "Weekly Coaching Call",
  "speakers_in_chunk": ["Patrick Chouinard", "Shakur"],
  "chunk_position": 1,
  "total_chunks_in_session": 15,
  "content_tier": "historical",
  "content_type": "transcript",
  "source": "fathom_transcript",
  "topic": "Trying Codex Inside Cursor",
  "summary": "Patrick asks if anyone has tried the new Codex inside Cursor. Shakur hasn't yet. Brief discussion about falling behind on new tool releases.",
  "text": "## Session: Weekly Coaching Call | Date: 2025-09-02\n\n[00:02:29] Patrick Chouinard: Did anybody get the chance to try the new codex?..."
}
```

For Path B embedding, the `summary` field is what gets embedded (not `text`). This produces focused vectors that match single-topic queries precisely.

---

## 6. New Component: LLM Client (`src/community_brain/llm.py`)

Thin OpenRouter API client for LLM calls.

```python
def call_llm(prompt: str, model: str = "google/gemini-3.1-flash-lite-preview") -> str
```

**Configuration:**
- `OPENROUTER_API_KEY` in `config/.env`
- OpenRouter endpoint: `https://openrouter.ai/api/v1/chat/completions`
- Model configurable via env var `COMMUNITY_BRAIN_LLM_MODEL` (default: Gemini 3.1 Flash Lite)

**Error handling:**
- Retry up to 3 times with exponential backoff
- Parse JSON response; if LLM returns malformed JSON, retry with a nudge prompt
- Log token usage for cost tracking

---

## 7. Updated Pipeline Flow

### Backfill (chunk_historical.py)

```
For each transcript file in raw-transcripts/:
  1. Parse transcript → list[SpeakerTurn]
  2. Normalize speakers
  3. Format full transcript text
  4. Pass 1: Call LLM for topic segmentation → list[Topic]
  5. For each topic:
     a. Extract turns between start/end timestamps
     b. If ≤ 800 tokens: one chunk, use topic summary
     c. If > 800 tokens: sub-split at speaker boundaries,
        call LLM for sub-summary per sub-chunk
  6. Assign chunk IDs, positions, totals
  7. Write markdown + JSONL
  8. Update manifest
```

### Enriched (chunk_enriched.py — SP2, future)

Same two-pass approach applied to the Merged Call Summarizer's transcript output.

---

## 8. What Changes vs. Current Code

| Component | Change |
|---|---|
| `Chunk` dataclass | Add `topic: str` and `summary: str` fields |
| `chunk_transcript()` | Kept as fallback for sub-splitting oversized topics |
| `chunks_to_markdown()` | Updated to include topic headers and summaries |
| `chunks_to_jsonl()` | No change (uses `asdict`, auto-includes new fields) |
| New: `llm.py` | OpenRouter API client |
| New: `topic_segmenter.py` | Pass 1 logic: full transcript → topic list |
| New: `chunk_by_topics()` | Pass 2 logic: topics → chunks with summaries |
| `chunk_historical.py` | Updated to use two-pass pipeline |
| `pyproject.toml` | No new dependencies (httpx already included) |
| `config/.env.example` | Add `OPENROUTER_API_KEY` |

---

## 9. Cost Estimate

| Pass | Calls | Input Tokens | Output Tokens | Cost |
|---|---|---|---|---|
| Topic segmentation | ~78 | ~3.1M | ~234K | $1.13 |
| Sub-chunk summaries | ~2,000 (est.) | ~1M | ~100K | $0.40 |
| **Total backfill** | | | | **~$1.53** |
| **Per new session** | 1-2 | ~50K | ~5K | **~$0.02** |

(Earlier estimate of $3.13 was conservative — many topics will be under 800 tokens and won't need sub-summaries.)

---

## 10. Expected Quality Improvement

| Query Type | v1 (sliding window) | v2 (topic-aware + summaries) |
|---|---|---|
| Specific tool mention ("Codex") | Poor — diluted across mixed-topic chunk | Good — dedicated topic chunk with focused embedding |
| Speaker-specific ("What did Patrick say about X") | Moderate — speaker present but topic unfocused | Good — topic + speaker metadata |
| Broad topic ("GPU benchmarks") | Moderate — matches largest topic chunks | Good — topic title directly matches |
| Temporal ("What happened at the start of the call") | Poor — position metadata not leveraged | Moderate — topic order preserved |

---

## 11. Verification Gate

Before bulk processing:

- [ ] Topic segmentation produces sensible topic boundaries on 3 sample sessions
- [ ] Topic count per session is in the 10-25 range (not too granular, not too coarse)
- [ ] Summaries accurately reflect chunk content
- [ ] Updated markdown imports into Open WebUI successfully
- [ ] RAG queries ("What was discussed about Codex?") return the correct topic chunk
- [ ] Cost per session matches estimate (~$0.02)
- [ ] All tests pass

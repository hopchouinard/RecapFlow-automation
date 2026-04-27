# Community Brain Ingestion Pipeline — Design Specification

**Date:** 2026-04-18
**Status:** Approved for implementation
**Scope:** v1 of the Community Brain ingestion pipeline, covering ongoing weekly ingestion and historical backfill

---

## 1. Purpose and Context

This specification defines the ingestion pipeline that transforms weekly coaching-call artifacts into a queryable vector knowledge base stored in LanceDB. The pipeline serves the Community Brain project: a downloadable, queryable corpus of ~130 historical sessions plus ongoing weekly additions.

The design is informed by:
- An earlier pivot from Open WebUI native RAG to LanceDB with a dual-field embedding architecture (embed a focused summary, store and return the full text)
- The `docs/ref/llm-wiki.md` pattern of building a compiled knowledge layer rather than re-deriving from raw text at every query
- A non-negotiable constraint: structured fields extracted by LLMs are probabilistic and must be treated as retrieval hints, never as facts

The pipeline is designed for production use on a single host (the n8n VM), with the AVX2 CPU extension now exposed to the VM (previously blocked by Proxmox CPU type masking). LanceDB, n8n, and the retrieval server all run in Docker containers on the same host, sharing a filesystem volume for artifact exchange.

## 2. Goals and Non-Goals

### Goals

1. **Ingest weekly sessions automatically** into LanceDB with rich, queryable metadata
2. **Batch-process the historical backlog** (~130 sessions, ~2.5 years) through the same ingestion path
3. **Support five query classes** at the application layer: evolution over time, relationships between ideas, contradictions or disagreements, outcomes or impacts, missing or unresolved questions
4. **Preserve full source text** as ground truth, with LLM-derived metadata as a navigable overlay
5. **Tolerate schema and prompt evolution** without forcing full re-processing of existing corpus
6. **Operate on commodity infrastructure** — single host, Docker Compose, no external services beyond OpenRouter and (optionally) OpenAI

### Non-Goals

- Real-time ingestion (weekly cadence is sufficient)
- Multi-tenant isolation (single-corpus system)
- LLM inference in the retrieval path (retrieval server returns chunks; downstream clients generate answers)
- Cross-host deployment (single-machine architecture is assumed; see §3.2)
- Automatic corpus-wide analysis (v1 populates chunk-local metadata only; corpus-derived markers are infrastructure-only in v1, populated by a v2 corpus lint pass)
- Per-user access control beyond the existing API key

## 3. System Architecture

### 3.1 Single-Host Topology

All components run on the n8n VM (`n8n-automation.patchoutech.lab`):

```
┌──────────────────────────────────────────────────────────┐
│                   VM Host (Docker Compose)                │
│                                                            │
│  ┌──────────┐   ┌──────────┐   ┌───────────────────────┐ │
│  │   n8n    │   │ Postgres │   │  Retrieval Server     │ │
│  │          │   │  (n8n_db)│   │  (FastAPI + LanceDB)  │ │
│  └────┬─────┘   └──────────┘   └───────────┬───────────┘ │
│       │                                     │             │
│       └──────── shared volume ──────────────┘             │
│                  ./output/                                 │
│                                                            │
│  Additional volumes:                                       │
│    ./lancedb/         (persistent vector store)            │
│    ./config/          (registries, prompts, thresholds)    │
│    ./watch/           (n8n input drop zone)                │
│    ./historical-raw/  (batch input for historical)         │
└──────────────────────────────────────────────────────────┘
```

### 3.2 Deployment Constraint — Shared Filesystem

This architecture assumes a shared filesystem between n8n and the retrieval server, implemented via Docker volume mounts. The `/ingest` endpoint receives file paths (not content). Cross-host deployment would require switching from path-based ingestion to content-based ingestion (raw content in the request body) and is explicitly out of scope for v1.

### 3.3 Three n8n Workflows

**Workflow 1 — Merged Call Summarizer (existing, extended)**
- Rendezvous trigger: both `YYYY-MM-DD-zoom-chat.txt` and `YYYY-MM-DD-transcript.txt` present in `./watch/`
- Produces all existing artifacts plus `prepared-transcript.md` (new)
- Ends with HTTP POST to retrieval server `/ingest`

**Workflow 2 — Transcript-Only Summarizer (new, batch tool)**
- Manual trigger or batch loop with per-date parameter
- Input: a raw Fathom transcript file, no chat log required
- Reuses the prep, extract-signal, and community-post prompts
- Skips compressed-post and weekly-invite (not needed for historical)
- Ends with HTTP POST to retrieval server `/ingest`

**Workflow 3 — LanceDB Ingestion (implemented inside the retrieval server, exposed as `/ingest`)**
- Called by Workflows 1 and 2
- Parses artifacts, runs extraction, embeds, writes to LanceDB
- Idempotent on re-run

### 3.4 Retrieval Server Endpoint Surface

```
GET  /health                       existing
POST /query                        existing, extended (see §7.1)
POST /ingest                       NEW
POST /reindex                      NEW
GET  /sessions                     NEW
GET  /sessions/{session_id}        NEW
```

## 4. Data Flow

### 4.1 Ongoing Weekly Flow

```
Mac Mini (Zoom chat) ──rsync──→ watch/YYYY-MM-DD-zoom-chat.txt
Fathom poller ────────────────→ watch/YYYY-MM-DD-transcript.txt
                                         │
                                 (rendezvous: both present)
                                         │
                                         ▼
                          [Workflow 1: Merged Call Summarizer]
                              ├─ Validate + merge chat+transcript
                              ├─ Create output/YYYY-MM-DD/
                              ├─ Save transcript.txt
                              ├─ LLM: prep prompt on transcript
                              │       → prepared-transcript.md
                              ├─ LLM: extract-signal on merged
                              │       → extracted-signal.md
                              ├─ LLM: community-post on merged
                              │       → community-post.md
                              ├─ LLM: compress-post → community-post-compressed.md
                              ├─ LLM: weekly-invite → <date>-weekly-invite.md
                              └─ HTTP POST → retrieval-server /ingest
                                                 │
                                                 ▼
                                    [Retrieval Server /ingest]
                                    (see §5 extraction pipeline)
```

### 4.2 Historical Backfill Flow

```
Owner-provided transcripts → historical-raw/ (staging folder)
                                         │
                              (batch loop: per date)
                                         │
                                         ▼
                          [Workflow 2: Transcript-Only Summarizer]
                              ├─ Read historical-raw/YYYY-MM-DD-transcript.txt
                              ├─ Create output/YYYY-MM-DD/
                              ├─ Save transcript.txt
                              ├─ LLM: prep prompt → prepared-transcript.md
                              ├─ LLM: extract-signal → extracted-signal.md (thinner)
                              ├─ LLM: community-post → community-post.md   (thinner)
                              └─ HTTP POST → retrieval-server /ingest
```

### 4.3 Query Flow

```
User query in Open WebUI
   │
   ▼
community_brain_filter
   ├─ Prepends Inference Guidelines prompt fragment
   └─ Calls retrieval-server /query
            │
            ▼
   Retrieval server
   ├─ Embeds question (nomic-embed-text)
   ├─ Vector search in LanceDB with optional filters
   └─ Returns { ground_truth: [...], derived_metadata: [...], provenance: [...] }
            │
            ▼
   Downstream LLM receives structurally-separated response
   and reasons under the Inference Guidelines contract
```

### 4.4 Folder Conventions

```
watch/                                 ephemeral input (ongoing flow)
historical-raw/                        batch input (historical backfill only)
output/YYYY-MM-DD/                     artifacts per session
  ├─ transcript.txt
  ├─ prepared-transcript.md            (ingested)
  ├─ extracted-signal.md               (ingested)
  ├─ community-post.md                 (ingested)
  ├─ community-post-compressed.md      (not ingested; ongoing flow only)
  └─ YYYY-MM-DD-weekly-invite.md       (not ingested; ongoing flow only)

lancedb/nomic-v1/                      primary vector store

config/
  ├─ speaker-aliases.yaml              canonical speaker registry
  ├─ entity-registry.yaml              canonical entity registry
  ├─ chunking.yaml                     token thresholds and tunables
  ├─ extraction-config.yaml            points at current prompt versions
  └─ extraction-prompts/
      ├─ prep-prompt-v1.md
      ├─ chunk-extraction-v1.md
      ├─ session-themes-v1.md
      ├─ extract-signal-v1.md          (canonical vocabulary enforced)
      └─ CHANGELOG.md

docs/
  ├─ inference-guidelines.md           downstream contract
  └─ migrations/CHANGELOG.md           schema and extraction migration log
```

## 5. Extraction Pipeline

### 5.1 Three Stages

**Stage A — Parse and chunk (deterministic, no LLM)**
- Parse each artifact per §5.2 boundary rules
- Produce N chunk records with `full_text`, `chunk_id`, positional metadata, and parsed-from-text fields (`speakers_spoke`, `has_question`, `has_answer`, `has_insight`, `keywords`, `topic_label`)

**Stage B — Session-level LLM pass (1 call per session)**
- Produces `session_themes` (list of 3-5 high-level themes) denormalized onto every chunk of the session
- Deterministic input selection (see §5.3)

**Stage C — Chunk-level LLM pass (N calls, one per chunk)**
- Input: chunk `full_text` + entity registry + speaker aliases
- Produces: `entities` (normalized), `speech_acts`, `stance`, `certainty`, `chunk_local_markers`, `decisions`, `action_items`, `external_refs`, `references_prior`, plus `new_entities_seen` (unknowns flagged for review)
- Populates `extraction_model`, `extraction_prompt_version`, `extraction_status`, `extraction_error`, `extracted_at`

### 5.2 Chunking Rules Per Content Type

**prepared-transcript.md**
- Boundary: split at `<!--SEGMENT` markers produced by the prep prompt
- `embed_text`: concatenated segment header fields (topic, summary, keywords)
- `full_text`: complete segment body including inline annotations (`[HH:MM:SS] Speaker:`, `[tool:X]`, `<Q>`, `<A>`, `▶`)
- Overlong segments (body exceeds `chunking.transcript_segment_max_tokens`): sub-chunk via sliding window within the segment; each sub-chunk retains the segment header as its `embed_text`
- `topic_label`: parsed from segment header
- Chunk ID format: `{session_id}:transcript:{zero-padded-index}` (e.g., `2024-03-15:transcript:042`)

**extracted-signal.md**
- Boundary: split at top-level markdown heading (`## `) — one chunk per section
- `embed_text`: same as `full_text` (dual-field rule for already-summarized content)
- `full_text`: complete section including heading and body
- `topic_label`: the heading slug (canonical vocabulary — see §5.2.1)
- Chunk ID format: `{session_id}:signal:{canonical-slug}` (e.g., `2024-03-15:signal:tools`)

**community-post.md**
- Boundary: whole document as one chunk if `token_count <= chunking.post_max_tokens`; otherwise sliding window (rare)
- `embed_text`: same as `full_text`
- `full_text`: complete post
- `topic_label`: fixed value `"session_narrative"`
- Chunk ID format: `{session_id}:post:main` (or `{session_id}:post:{index}` if split)

#### 5.2.1 Extracted-Signal Canonical Vocabulary

The extract-signal prompt MUST produce sections only from this fixed vocabulary:

```
## tools       — tools, services, products, libraries discussed
## qa          — question and answer pairs
## insights    — key takeaways, recommendations, lessons
## links       — URLs and resources shared
## decisions   — decisions made or conclusions reached
## general     — catch-all for content not fitting the above
```

Sections are omitted entirely when empty (do not output empty sections). The extract-signal prompt file at `config/extraction-prompts/extract-signal-v1.md` enforces this via explicit instructions and a few-shot example.

A post-ingestion audit script scans chunk IDs for non-canonical signal slugs. Any mismatch indicates prompt drift and is logged for prompt correction.

### 5.3 Stage B Input Selection (Deterministic)

Priority, evaluated in order:

```
1. community_post.md if present AND token_count <= chunking.session_themes_input_max_tokens
2. ELSE concatenation of all prepared-transcript segment headers
   (topic + summary + keywords fields only; segment bodies excluded)
3. ELSE extracted_signal.md
4. ELSE skip Stage B: log a warning, set session_themes = [] on all chunks,
        continue ingestion. Session is still ingested successfully.
```

The chosen input (or the skip decision) is logged with the extraction for auditability. Same session under same config produces the same `session_themes` output on re-extraction.

**Rationale for soft-fail:** a missing-input case should not block ingestion of a session whose raw content is otherwise valid. `session_themes` is an enrichment; absence degrades retrieval quality for that session but doesn't corrupt it. Consistent with the "tolerate missing fields" principle applied elsewhere.

### 5.4 LLM Model Selection

| Stage | Model | Rationale |
|---|---|---|
| Prep prompt (Workflows 1 & 2) | Claude Sonnet 4.6 via OpenRouter | Existing credential; high-quality structured output |
| Extract-signal (Workflows 1 & 2) | Claude Sonnet 4.6 via OpenRouter | Existing |
| Community-post (Workflows 1 & 2) | Claude Sonnet 4.6 via OpenRouter | Existing |
| Session themes (Stage B) | Gemini 3.1 Flash Lite | Cheap, fast, good at summarization |
| Chunk extraction (Stage C) | Gemini 3.1 Flash Lite | Structured JSON output, cost-appropriate |
| Embeddings | nomic-embed-text via Ollama | Local, free, already running |

### 5.5 Cost Profile

Primary cost driver is **chunk count post-segmentation**, not session count. Monitor chunks-per-session during backfill to detect prompt drift (unusually fine segmentation indicates over-splitting).

**Historical backfill (one-time):**

| Step | Calls | Model | Estimate |
|---|---|---|---|
| Workflow 2: 3 Sonnet calls × 130 | 390 | Sonnet 4.6 | $15-25 |
| Stage B: 1 × 130 | 130 | Flash Lite | <$1 |
| Stage C: 1 × ~1,950 chunks | ~1,950 | Flash Lite | $3-5 |
| Embeddings | ~1,950 | nomic (local) | $0 |
| **Total** | | | **~$20-30** |

**Ongoing weekly:**

| Step | Calls/week | Estimate/week |
|---|---|---|
| Workflow 1: 5 Sonnet calls | 5 | ~$0.20 |
| Stage B | 1 | negligible |
| Stage C | ~15 | ~$0.03 |
| Embeddings | ~15 | $0 |
| **Total/week** | | **~$0.25** |

Actual costs should be instrumented via the `extracted_at` field + token counts for each LLM call.

### 5.6 Extraction Idempotency

Chunks with matching `extraction_prompt_version` AND `extraction_status = "success"` are skipped during ingestion unless `force_reextract: true` is passed. Chunks with `extraction_status = "failed"` are retried on every ingestion call regardless of the flag — error recovery is first-class, not opt-in.

Re-running `/ingest` on the same session is a no-op when all chunks are current and successful.

### 5.7 Rate Limiting and Batch Resumability

**Workflow 2 (historical backfill):**
- Configurable inter-session delay (default 30s; tune empirically per OpenRouter tier)
- Retry policy: per `config/chunking.yaml` retry settings (default 3 attempts, exponential backoff)
- Progress state at `config/backfill-state.json`:

```json
{
  "started_at": "2026-04-18T10:00:00Z",
  "total_sessions": 130,
  "completed": ["2024-03-15", "2024-03-22"],
  "failed": [{"date": "2024-04-05", "error": "...", "retry_count": 1}],
  "in_progress": null
}
```

- On start: skip dates in `completed`; retry dates in `failed` up to configured attempts; resume `in_progress` if interrupted
- On per-session failure: log, continue to next session; final failures reported at batch end

### 5.8 Unknown Entity and Speaker Handling

When Stage C extraction encounters mentions that don't match the registry:
- The extraction response includes `new_entities_seen` and/or `new_speakers_seen`
- The chunk is stored with whatever registered entries matched, plus the raw mention preserved verbatim in `full_text`
- Unknowns are appended to `pending:` in the appropriate registry YAML
- A `/pending-review` report (cron-scheduled, weekly) surfaces accumulated pending entries for operator review
- Promotion from `pending` to canonical is manual; once promoted, a targeted `/reindex` on affected chunks can be triggered

**Concurrency constraint:** registry updates are single-writer in v1. The retrieval server serializes all pending-entry appends through an in-process async lock. Multiple concurrent `/ingest` requests can run chunk-writing in parallel; only the registry append section is serialized. Multi-writer registry updates are out of scope for v1.

**Write atomicity:** registry updates are buffered in memory during a session's ingestion and flushed atomically to disk at the end of the session's commit. The write-to-disk pattern is: (1) serialize the updated YAML to a temporary file in the same directory, (2) `fsync`, (3) atomic `rename` over the target file. A crash mid-ingestion leaves either the pre-ingestion YAML or the post-ingestion YAML — never a partially-written file.

### 5.9 Prompt Versioning

Extraction prompts live in `config/extraction-prompts/` as versioned files. The active version is declared in `config/extraction-config.yaml`:

```yaml
session_themes:
  prompt_file: session-themes-v1.md
  model: gemini-3.1-flash-lite

chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: gemini-3.1-flash-lite

extract_signal:
  prompt_file: extract-signal-v1.md
  # ... (also produced in n8n, referenced here for versioning coordination)
```

When a prompt is updated:
1. Create new versioned file (`chunk-extraction-v2.md`)
2. Update `extraction-config.yaml` to point at it
3. Add an entry to `config/extraction-prompts/CHANGELOG.md`
4. Next ingestion run uses the new version for new chunks
5. Old chunks retain their `extraction_prompt_version = "chunk-extraction-v1"` metadata
6. When ready, trigger targeted re-extraction: `POST /reindex` with filter on the old version

## 6. LanceDB Schema

### 6.1 Full Schema (v1.0, 37 fields)

```
-- Identity & positional
schema_version:              string    "1.0"
chunk_id:                    string    unique
session_id:                  string
session_date:                date
session_title:               string | null
content_type:                enum      "prepared_transcript" | "extracted_signal" | "community_post"
source_file:                 string
chunk_index:                 int
total_chunks_in_source:      int

-- Attribution
speakers_spoke:              list[string] | null
speakers_mentioned:          list[string] | null

-- Semantic tags (chunk-level)
entities:                    list[string]               -- normalized via entity-registry.yaml
keywords:                    list[string] | null
topic_label:                 string | null

-- Session-level context (denormalized)
session_themes:              list[string]

-- Interpretation (LLM-derived, chunk-local)
speech_acts:                 list[enum]                 -- "question" | "answer" | "opinion" |
                                                          "recommendation" | "warning" | "anecdote" |
                                                          "decision" | "action_item" | "prediction" |
                                                          "comparison" | "definition"
stance:                      enum | null                -- "positive" | "negative" | "neutral" | "mixed"
certainty:                   enum                       -- "asserted" | "hedged" | "speculative"

chunk_local_markers:         list[enum]                 -- "emphasized" | "sustained" |
                                                          "breakthrough" | "resolved"
corpus_derived_markers:      list[enum]                 -- "recurrent" | ... (v1: always empty)
corpus_markers_computed_at:  datetime | null            -- v1: always null; populated by v2 corpus lint

-- Deterministic tags (from text scanning)
has_question:                bool
has_answer:                  bool
has_unresolved_question:     bool
has_insight:                 bool

-- Structured extracts
decisions:                   list[string] | null
action_items:                list[string] | null
external_refs:               list[string] | null
references_prior:            bool

-- Provenance
extraction_model:            string
extraction_prompt_version:   string
extraction_status:           enum                       -- "success" | "failed"
extraction_error:            string | null
extracted_at:                datetime

-- Content & embedding
embed_text:                  string
full_text:                   string
embedding:                   vector
```

### 6.2 Separation of Concerns

The schema distinguishes three categories of fields:

1. **Ground truth** — `chunk_id`, `session_id`, `session_date`, `source_file`, `full_text`. These are authoritative. Quotes and citations must resolve to these.

2. **Derived metadata** — `entities`, `speech_acts`, `stance`, `certainty`, `chunk_local_markers`, `decisions`, `action_items`, `external_refs`, `references_prior`, `session_themes`, `topic_label`. LLM-interpreted. Probabilistic. Re-derivable.

3. **Provenance** — `extraction_model`, `extraction_prompt_version`, `extraction_status`, `extraction_error`, `extracted_at`, `schema_version`. Tracks WHAT generated the data and WHETHER it succeeded. Operational state (`extraction_status`) is distinct from what-ran (`extraction_prompt_version`).

### 6.3 Chunk ID Conventions

Format: `{session_id}:{content_type_short}:{suffix}`

- `session_id`: default format `YYYY-MM-DD`. If multiple sessions occur on the same date, the second and subsequent sessions receive an incremental suffix: `YYYY-MM-DD-2`, `YYYY-MM-DD-3`, etc. The first session of a date keeps the bare date form (no suffix) for backward compatibility. Collision detection happens at ingestion time: before writing, the server checks for existing sessions matching the prospective `session_id` and increments until unique.
- `content_type_short`: one of `transcript`, `signal`, `post`
- `suffix`:
  - For `transcript`: zero-padded numeric index (e.g., `042`)
  - For `signal`: canonical slug from the fixed vocabulary (e.g., `tools`, `qa`)
  - For `post`: `main` (or `{index}` if split)

IDs are stable across re-ingestion: same input produces same ID, so re-ingestion updates rows rather than duplicating.

## 7. API Contract

### 7.1 POST /query

**Request:**

```json
{
  "question": "What tools have we discussed for agent orchestration?",
  "top_k": 10,

  "filters": {
    "session_date_range": ["2025-01-01", "2026-04-18"],
    "content_type": ["prepared_transcript", "extracted_signal"],

    "speakers_spoke": ["Alex Rojas"],
    "speakers_spoke_match": "any",
    "speakers_mentioned": [],
    "speakers_mentioned_match": "any",

    "entities": ["LangChain"],
    "entities_match": "any",

    "keywords": [],
    "keywords_match": "any",

    "schema_version_min": null,

    "require_chunk_markers": ["resolved"],
    "exclude_chunk_markers": [],
    "require_corpus_markers": [],
    "exclude_corpus_markers": [],

    "has_question": null,
    "has_answer": null,
    "has_unresolved_question": null,
    "has_insight": null,
    "references_prior": null
  },

  "response_shape": "structured"
}
```

All filters are optional. Defaults:
- `schema_version_min: null` — all generations included (per §8 migration policy)
- All `*_match` fields default to `"any"`
- Boolean filters default to `null` (no filtering on that field)

**Filter semantics:**
- A filter field set to `null` or omitted is ignored; it does not constrain results.
- A filter field set to an empty list (`[]`) is also ignored (treated same as null).
- List-valued filters (`entities`, `speakers_spoke`, `speakers_mentioned`, `keywords`) match chunks according to their `_match` companion field. `"any"` requires at least one overlap; `"all"` requires every filter value to be present in the chunk's list.
- **Absent-value rule for list fields:** if a chunk's field is null or empty, it does NOT match any list-valued filter constraint. Absence is treated as non-matching, not as a wildcard. This applies to `keywords`, `entities`, `speakers_spoke`, `speakers_mentioned` equally.

**Execution order:**
Filtering is applied first against the chunk metadata; ranking is then performed on the filtered set using vector similarity alone (v1). If filters eliminate all chunks, the response returns an empty `chunks` array with a populated `filters_applied` block so the caller can see what was filtered.

**Response (structured shape, default):**

```json
{
  "query": "What tools have we discussed for agent orchestration?",
  "chunks": [
    {
      "ground_truth": {
        "chunk_id": "2026-03-10:transcript:027",
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "Agent frameworks comparison",
        "source_file": "output/2026-03-10/prepared-transcript.md",
        "full_text": "...complete segment text verbatim..."
      },
      "derived_metadata": {
        "content_type": "prepared_transcript",
        "topic_label": "agent orchestration tools",
        "speakers_spoke": ["Alex Rojas", "Sam"],
        "speakers_mentioned": ["Alex Rojas", "Sam", "Shakur"],
        "entities": ["LangChain", "LangGraph", "CrewAI"],
        "keywords": ["agent orchestration", "tool calling", "state machines"],
        "session_themes": ["agent frameworks", "production deployment patterns"],
        "speech_acts": ["comparison", "recommendation"],
        "stance": "positive",
        "certainty": "asserted",
        "chunk_local_markers": ["emphasized", "sustained"],
        "corpus_derived_markers": [],
        "has_question": false,
        "has_answer": false,
        "has_unresolved_question": false,
        "has_insight": true,
        "decisions": null,
        "action_items": null,
        "external_refs": ["https://langchain.com/docs/langgraph"],
        "references_prior": false
      },
      "provenance": {
        "schema_version": "1.0",
        "extraction_model": "gemini-3.1-flash-lite",
        "extraction_prompt_version": "chunk-extraction-v1",
        "extraction_status": "success",
        "extraction_error": null,
        "extracted_at": "2026-03-10T14:22:11Z"
      },
      "similarity": 0.847
    }
  ],
  "total_matched": 10,
  "filters_applied": { "...echo of applied filters..." }
}
```

**Response (flat shape):** `response_shape: "flat"` returns a flattened structure; documented but not default. The nested `structured` shape is preferred because it encodes the trust model structurally.

### 7.2 POST /ingest

**Request:**

```json
{
  "session_id": "2026-04-14",
  "session_date": "2026-04-14",
  "session_title": "Open WebUI deployment patterns",
  "artifact_paths": {
    "prepared_transcript": "/data/output/2026-04-14/prepared-transcript.md",
    "extracted_signal":    "/data/output/2026-04-14/extracted-signal.md",
    "community_post":      "/data/output/2026-04-14/community-post.md"
  },
  "force_reextract": false
}
```

- Paths are container-local, resolved through the shared volume mount
- Missing artifacts are tolerated (historical sessions may have fewer); ingestion proceeds with available artifacts and logs a warning
- `force_reextract: true` overrides version-check idempotency for all chunks in this session

**Response:**

```json
{
  "session_id": "2026-04-14",
  "chunks_written": 17,
  "chunks_by_type": {
    "prepared_transcript": 12,
    "extracted_signal": 4,
    "community_post": 1
  },
  "extraction_model": "gemini-3.1-flash-lite",
  "extraction_prompt_version": "chunk-extraction-v1",
  "schema_version": "1.0",
  "chunks_skipped_idempotent": 0,
  "chunks_failed": 0,
  "warnings": [],
  "unknown_entities_flagged": ["new-tool-mentioned"],
  "unknown_speakers_flagged": []
}
```

**Transactional boundary:** ingestion is atomic per session. Either all chunks for the session are written to LanceDB successfully, or none are. The retrieval server stages chunks in memory (or a temporary table) during Stage C extraction and commits in a single LanceDB transaction at the end. Per-chunk extraction failures do not abort the session — they produce chunks with `extraction_status: "failed"` that still get written as part of the atomic commit.

**Error semantics:**
- Per-chunk extraction failure: chunk staged with `extraction_status: "failed"`, `extraction_error` populated, `extraction_prompt_version` still reflects WHICH prompt was attempted. Session commit proceeds.
- All required artifacts missing: HTTP 400, nothing written.
- LanceDB commit failure: HTTP 500, transaction rolled back, no partial session state in the corpus.

### 7.3 POST /reindex

Applies operational changes to a filtered subset without full re-ingestion.

**Request:**

```json
{
  "filter": {
    "extraction_prompt_version": "chunk-extraction-v1",
    "extraction_status": "failed",
    "session_date_range": ["2024-01-01", "2024-12-31"]
  },
  "operation": "re-extract",
  "dry_run": false,
  "priority_order": "newest_first"
}
```

**Operations:**
- `re-extract` — re-runs Stage C on matching chunks; updates derived fields + provenance; keeps `full_text` and `embedding` unchanged
- `re-embed` — re-runs embedding on matching chunks (after embedding model swap); keeps everything else unchanged
- `delete` — removes matching chunks (retractions or corrections; last-resort)

**Response:** Server-Sent Events stream

```
event: progress
data: {"completed": 120, "total": 1950, "eta_seconds": 800}

event: complete
data: {"chunks_updated": 1950, "duration_seconds": 1280, "failures": []}
```

### 7.4 GET /sessions and /sessions/{session_id}

Corpus inventory queries that don't invoke vector search.

```
GET /sessions?content_type=community_post&has_unresolved=true
```

Returns session-level aggregates: chunk counts by type, unresolved question counts, session themes, date range coverage. Useful for dashboards, coverage gap detection, corpus-wide reporting.

### 7.5 Authentication

Existing `RETRIEVAL_API_KEY` via `X-API-Key` header covers all endpoints. All mutating endpoints (`/ingest`, `/reindex`) use the same key in v1. Splitting into read/write key scopes is noted for v2.

## 8. Trust Model and Migration Policy

### 8.1 Trust Model Principles

1. **`full_text` is ground truth.** Authoritative, verbatim source content. All quotes and citations in downstream output must resolve to a specific `chunk_id`.

2. **Fields in `derived_metadata` are LLM interpretations.** Probabilistic, versioned, re-derivable. Used to orient retrieval and frame responses, not to substitute for reading source.

3. **When `derived_metadata` contradicts `full_text`, `full_text` wins.** No exceptions.

4. **Absence of a field ≠ absence of the property.** Missing `decisions` on an older chunk means that chunk predates that extraction, not that no decisions were discussed.

5. **Provenance is queryable.** Every chunk carries `extraction_model`, `extraction_prompt_version`, `extraction_status`, `extracted_at`, `schema_version`. Consumers can filter or weight by provenance when needed.

### 8.2 Enforcement Mechanisms

**(a) API response shape** — §7.1 nests fields under `ground_truth`, `derived_metadata`, `provenance`. Consumers see the distinction structurally.

**(b) Inference Guidelines prompt fragment** at `docs/inference-guidelines.md`. Loaded verbatim into downstream system prompts.

**(c) `community_brain_filter` Open WebUI function** prepends the Inference Guidelines fragment to every query sent to a downstream LLM.

### 8.3 Enforcement Boundary

The Inference Guidelines define a contract between the retrieval server and compliant consumers. The `community_brain_filter` is the reference compliant consumer. Consumers that bypass the Inference Guidelines — direct LanceDB access, custom API clients that ignore the `derived_metadata` vs `ground_truth` distinction, LLM prompts that don't prepend the guidelines fragment — are considered **unsupported**. The system's correctness guarantees apply only within the enforcement boundary. Misuse outside this boundary is not a system bug.

### 8.4 Migration Policy

**Core stance:** design for mixed generations. Avoid full re-ingestion. At 280+ hours of source content, full re-processing must be a rare, deliberate event, not a reflex response to schema tweaks.

**Change classification:**

| Change type | Example | Migration required |
|---|---|---|
| Additive-compatible | Add new nullable field | None. New ingestions populate; old chunks keep field as null. |
| Extraction improvement | Better chunk-extraction prompt (v1 → v2) | Optional `/reindex` re-extract when ready. Old chunks coexist under v1. |
| Embedding model change | `nomic-embed-text` → `nomic-v2` | Required re-embedding (embeddings incompatible across models). `/reindex re-embed`. |
| Field semantic change | `stance` enum adds new value | Treat as new field semantically. Deprecate old, add new. Never silently redefine. |
| Field removal | Drop unused field | Mark deprecated for one major version before removing. |
| Schema-breaking | Rename `content_type` enum values | Full migration plan. `schema_version` bumps major. Last resort. |

**Version numbering:**
- `schema_version` is semver-ish: `"1.0"`, `"1.1"`, `"2.0"`
- Minor bump: additive changes only, fully backward compatible
- Major bump: breaking changes; requires explicit migration entry in `docs/migrations/CHANGELOG.md`

### 8.5 Query-Time Default (Mixed Generations)

By default, queries include all schema versions. Retrieval ranking does not version-filter unless the client explicitly passes `schema_version_min`.

Prompts must tolerate missing fields gracefully. Absence of a field means the chunk predates that extraction, not that the property is absent from the content.

**Ranking bias (v1):** None. All chunks compete on vector similarity alone.
**Ranking bias (v2+, if needed):** May incorporate a small bonus for richer metadata coverage, evaluated only if retrieval quality shows measurable degradation from mixed-generation responses.

### 8.6 Migration Log

Every schema and extraction change adds an entry to `docs/migrations/CHANGELOG.md`:

```markdown
## YYYY-MM-DD — vX.Y {description}
- Change: {what changed}
- Rationale: {why}
- Migration: {automatic | reindex required | full re-ingest}
- Affected chunks: {scope}
- Rollback: {plan if this goes wrong}
```

Future contributors can reconstruct the corpus's evolution from this single file.

### 8.7 Never-Never Rules

- Never silently change a field's meaning while keeping the same name and version
- Never delete data without a retention decision (`/reindex delete` is the tool, not a cleanup pattern)
- Never bump `schema_version` without adding a migration log entry

## 9. Configuration Files

### 9.1 config/speaker-aliases.yaml

```yaml
version: 2026-04-18

aliases:
  Alex Rojas:
    - alexrojas
    - "Alex R"
    - arojas
  Alex Wilson:
    - AlexH
    - "Alex H"
  Sam:
    - sam
    - "Sam C"
  Shakur:
    - shakur

pending: []
```

### 9.2 config/entity-registry.yaml

```yaml
version: 2026-04-18

entities:
  Codex:
    type: tool
    category: coding_assistant
    aliases:
      - "OpenAI Codex"
      - "Codex CLI"
      - "codex"
  LangChain:
    type: framework
    category: agent_framework
    aliases:
      - "Langchain"
      - "langchain"
      - "LC"

pending: []
```

### 9.3 config/chunking.yaml

```yaml
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000

extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30

schema_version: "1.0"
```

### 9.4 config/extraction-config.yaml

```yaml
session_themes:
  prompt_file: session-themes-v1.md
  model: gemini-3.1-flash-lite

chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: gemini-3.1-flash-lite

extract_signal:
  prompt_file: extract-signal-v1.md

prep_prompt:
  prompt_file: prep-prompt-v1.md
```

## 10. Rollout Plan

### Phase 0 — Foundation (complete)
- AVX2 enabled on n8n VM (verified 2026-04-17)

### Phase 1 — Config and contracts
Ship artifacts before code depends on them:
- All four config files seeded
- All extraction prompts written and versioned
- `docs/inference-guidelines.md`
- `docs/migrations/CHANGELOG.md` initial entry

**Exit criteria:** files exist, reviewed, committed.

### Phase 2 — Retrieval server extension
- Add `/ingest`, `/reindex`, `/sessions` endpoints
- Implement chunking, extraction, embedding
- Implement v1.0 schema
- Extend `/query` with structured response shape + new filter fields
- Dockerize and add to `docker-compose.yml`

**Testing:**
- Unit tests for chunking rules per content type
- Unit tests for extraction parsing + registry lookups
- Integration test: round-trip ingest + query for one known session
- Idempotency test: re-ingest same session, verify no-op behavior

**Exit criteria:** server deploys; single test session ingested and queryable.

### Phase 3 — Workflow 1 extension
- Add prep-prompt step to existing summarizer
- Add final HTTP POST to `/ingest`
- Verify existing artifacts still produce correctly

**Testing:**
- Run on next live weekly session
- Confirm all artifacts present plus `prepared-transcript.md`
- Confirm ingestion succeeds
- Query the session, verify results

**Exit criteria:** one live weekly session ingested end-to-end.

### Phase 4 — Workflow 2 (historical batch)
- Build Transcript-Only Summarizer
- Accepts transcript file path; skips chat-log-dependent steps
- Uses `config/backfill-state.json` for resume

**Testing:**
- Single historical transcript end-to-end
- 5 historical transcripts with simulated interruption
- Rate limiting holds under sustained batch

**Exit criteria:** 5 historical sessions ingested; state file tracks correctly.

### Phase 5 — Full historical backfill
Run Workflow 2 across all ~130 sessions.
- Monitor pending entity/speaker accumulation
- Review and promote pending entries before Phase 6

**Exit criteria:** all sessions ingested; state file complete; registries cleaned up.

### Phase 6 — Open WebUI integration and validation

Update `community_brain_filter` to prepend Inference Guidelines and use the new response shape. Validate the five query types against the full corpus with explicit success criteria:

| Query type | Success criterion |
|---|---|
| Evolution over time | Result spans ≥2 distinct temporal phases (≥6 months apart); inference layer articulates change |
| Relationships between ideas | Result surfaces ≥2 distinct entities linked via topic overlap or explicit references |
| Contradictions / disagreements | Result contains ≥2 chunks with differing `stance` on same `topic_label` or entity |
| Outcomes or impacts | Result contains ≥1 chunk with non-null `decisions` or `action_items`, followed by ≥1 chunk with `references_prior: true` or matching `topic_label` |
| Missing / unresolved questions | Result contains ≥1 chunk with `has_unresolved_question: true` |

Failure on any criterion → iterate on the extraction prompt, Inference Guidelines, or retrieval ranking before Phase 6 sign-off.

**Exit criteria:** all five criteria met with representative queries.

#### Validation findings (2026-04-27 — partial validation against 8-session subset)

Initial validation pass against an 8-session corpus (six consecutive Feb 2025 sessions + two April 2026 sessions) surfaced the following lessons. Captured here so future operators don't re-discover them.

##### Chain integrity bugs (all fixed)

The end-to-end retrieval chain (Open WebUI → filter → retrieval server → LanceDB → Ollama embed → response → LLM generation) had several silent failure modes that produced confidently-wrong answers for days before being diagnosed:

1. **Filter timeout too tight.** The `community_brain_filter`'s default `timeout_seconds=3.0` was insufficient — `/query` includes a remote Ollama embed call that can spike past 3s under concurrent load or cold start. Silent `httpx.TimeoutException` → `("error", [])` → "unavailable" system prompt → models then ignored the unavailable instruction and answered from training priors. Bumped default to **30s**.

2. **"Unavailable" instruction too soft.** Original wording said *"Do not answer questions about coaching call content"* — multiple models (Gemma 4 4B, Gemma 4 26B, GPT-oss 20B in its visible thinking) interpreted "coaching call content" narrowly and decided abstract/strategic questions weren't strictly "about" coaching call content, then confabulated answers. Replaced with explicit `"RETRIEVAL SYSTEM ERROR ... You MUST NOT answer using general/training knowledge — even if the question seems answerable"` plus a quoted exact-response template.

3. **Filter URL valve resets to default on re-upload.** Open WebUI does not persist filter valve overrides across function file replacements. Operators MUST re-set `retrieval_url` after every filter upload. The default `http://host.docker.internal:8999/query` resolves to the Open WebUI host (typically the operator's Mac), not the VM where the retrieval server actually runs.

4. **Port binding was localhost-only.** Original `docker-compose.yml` bound the retrieval server to `127.0.0.1:8999` — LAN-unreachable. Cross-host Open WebUI deployments require `8999:8999` (all interfaces). Documented and changed in repo.

5. **`nomic-embed-text` can be silently evicted from Ollama.** Operators who pull large LLMs (Gemma 26B, Qwen 30B, GPT-oss 20B, etc.) into the same Ollama instance can lose the small embedding model to disk pressure or manual cleanup. `/health`, `/sessions`, `/speaker-aliases-block` continue to work normally — only `/query` fails (with HTTP 500). Operators should **pin `nomic-embed-text`** and treat its presence as a deploy-time precondition.

##### Retrieval limitations identified

6. **Vector search under-weights rare entity tokens.** Pure-vector retrieval via `nomic-embed-text` favors thematic similarity ("commit", "outcomes", "decisions") over proper-noun matches ("Adam", "Gold Flamingo"). Entity-grounded queries (*"What did Adam from Gold Flamingo commit to?"*) failed to surface the entity's actual chunks even when those chunks ranked at 0.42+ similarity for keyword-rephrased versions of the same question. **v2 backlog item:** add hybrid search (BM25 reranking on top-K vector candidates) to the retrieval server, or expose a `keyword_filter` parameter to the `/query` body.

##### Generation-layer findings (model comparison)

Same chain, same retrieved chunks, four different answering models:

| Model | RAG-discipline grade | Failure mode |
|---|---|---|
| Gemma 4 4B (`gemma4:e4b`) | F on abstract questions | Read chunks correctly in thinking step, then ignored them and answered from training-data marketing-school templates with zero `chunk_id` citations |
| Gemma 4 26B | F (worse than 4B) | Confidently hallucinated fake dates (`2024-05-22`, `2/24/24`) that don't exist in the corpus, with structured-looking output that masked the fabrication |
| Qwen3-coder 30B | B+ | Real chunk_id citations; faithful structural framing; numerical paraphrase drift on specific quantitative claims (e.g. "40,000 subscribers" → "$40K monthly") |
| GPT-oss 20B | A | Real citations, verbatim quotes, honest acknowledgment when relevant chunks weren't retrieved (refused to fabricate Adam-follow-up content rather than confabulating) |

**Key insight:** RAG-discipline is NOT primarily a parameter-count issue — Qwen3-coder 30B and GPT-oss 20B both outperformed Gemma 4 26B. It's a training/instruction-following profile concern. Gemma's prior on marketing/strategic topics overrides retrieved context. Recommended local-model defaults: GPT-oss 20B or Qwen3-coder 30B; avoid Gemma family for trust-partitioned retrieval workflows.

##### Corpus-coverage limits per query type (revised)

The five spec criteria above assume a corpus rich enough to satisfy them. Against the 8-session validation corpus:

- **Evolution over time** — works with adequate temporal spread (Feb 2025 + April 2026 = ~14 months satisfies the ≥6-month criterion).
- **Relationships between ideas** — works when the same entities recur across sessions; consecutive weekly sessions are stronger material than scattered samples for relationship surfacing.
- **Contradictions / disagreements** — **structurally weak** for this kind of corpus. Coaching-call disagreements are mostly intra-session (one mentor advising on a topic, one mentee with initial assumptions); they're not opposing positions held across sessions. The spec criterion ("≥2 chunks with differing `stance` on same `topic_label`") is too strict for typical mentor-mentee content.
- **Outcomes / impacts** — works when retrieval surfaces the entity's chunks. Vector search on entity-grounded queries (see finding 6) is the bottleneck — operator may need to rephrase questions with concrete content keywords until hybrid search lands in v2.
- **Missing / unresolved questions** — corpus has rich material (e.g. 11 unresolved-tagged chunks in 2025-02-05, 7 in 2025-02-19); pending validation.

##### Operational recipe (working configuration as of 2026-04-27)

For a Phase 6 sign-off run, this configuration is known good:

- Filter: post-Plan-A version with embedded `_INFERENCE_GUIDELINES` constant; `timeout_seconds=30`; URL pointing at the retrieval server's LAN-reachable address; tightened "unavailable" message.
- Retrieval server: bound to `0.0.0.0:8999` for cross-host access; `nomic-embed-text` pinned in Ollama.
- Answering model: GPT-oss 20B (validated) or Qwen3-coder 30B (validated with caveat on numerical drift). Avoid Gemma family.
- Operator awareness: vector-search-on-names limitation means entity queries may need keyword rephrasing until hybrid search ships.

### Rollout dependencies

```
Phase 0 → Phase 1 → Phase 2 ┬→ Phase 3 →──────────┐
                            └→ Phase 4 → Phase 5 →┴→ Phase 6
```

Phases 3 and 4 run in parallel after Phase 2 validates.

### Effort estimate

- Phase 1: 0.5 day
- Phase 2: 3-5 days
- Phase 3: 0.5 day
- Phase 4: 1 day
- Phase 5: 1-2 days wall clock (automated + review)
- Phase 6: 2-4 days (depending on prompt iteration cycles and query validation)

Total: ~9-15 working days for clean execution. Phase 6 is the most variable — prompt and retrieval tuning against the five success criteria typically requires several iteration cycles before all criteria are met.

## 11. Open Questions (Deferred to Implementation Time)

1. **Entity registry seeding.** Manual curation vs first-pass extraction with empty registry. Leaning toward the latter — less upfront, pending queue is designed for it. Decided in Phase 1.

2. **Backfill rate limit.** 30s between sessions is conservative. Tune empirically during Phase 4; target ~20% below observed limit.

3. **Session title source.** Fathom API may provide; otherwise fall back to community-post first line. Decided in Phase 3; defaults to null until resolved.

4. **Community-post chunking for unusually long posts.** Sliding-window fallback specified; revisit frequency during Phase 6.

5. **Retention / deletion flow.** `/reindex delete` is the tool; documented process deferred until first real retraction case arises.

6. **Corpus lint pass (v2).** Infrastructure in schema (`corpus_derived_markers`, `corpus_markers_computed_at`) but no implementation. Future project.

7. **Query-time latency profiling.** Measure once corpus is loaded; optimize only if needed.

8. **Open WebUI filter changes.** Scope is small but specific; Phase 6 item.

## 12. Explicit Out-of-Scope Items

- Corpus lint pass implementation (v2)
- Cross-host deployment (requires switching to content-based `/ingest`)
- Multi-tenant access control
- Real-time ingestion
- Automated migration testing harness
- Corpus snapshot / rollback (relies on daily `lancedb/` volume backup + replay)
- Read/write API key separation
- LanceDB-resident inference (retrieval server is retrieval-only)
- Multi-version ranking bias (v1 treats all generations equally in ranking; deferred pending empirical evidence of need)

## 13. Glossary

- **Artifact** — one of the markdown files produced by a summarizer workflow (prepared-transcript, extracted-signal, community-post)
- **Chunk** — a single row in LanceDB derived from an artifact by the chunking rules
- **Dual-field architecture** — `embed_text` (short, topical; used for vector similarity) + `full_text` (authoritative content; returned to consumers)
- **Enforcement boundary** — the set of consumers that apply the Inference Guidelines; outside this, correctness guarantees don't apply
- **Ground truth** — `full_text` plus identity fields; authoritative source content
- **Derived metadata** — LLM-extracted fields; probabilistic, re-derivable
- **Provenance** — metadata about what ran (model, prompt version) and whether it succeeded (status, error)
- **Session** — one coaching call, identified by `session_id` (typically `YYYY-MM-DD`)
- **Stage A/B/C** — the three phases of the extraction pipeline (deterministic parse, session-level LLM, chunk-level LLM)

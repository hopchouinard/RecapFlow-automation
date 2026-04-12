# Community Brain — Implementation Design Spec

**Date:** 2026-04-12
**Status:** Approved
**Approach:** Python-First (Approach A)
**License:** MIT

---

## 1. Project Overview

Community Brain is a vectorized, queryable knowledge base built from ~78 weeks of AI community coaching call transcripts. It is developed as a subproject within the existing n8n automation repo (`community-brain/` subdirectory) and published separately to a public GitHub repo for community distribution.

### Development vs Distribution

- **Development repo:** This n8n repo. All pipeline code, n8n workflows, and build tooling live here under `community-brain/`.
- **Public repo:** A separate `community-brain` repository (name placeholder, final name TBD with Brandon). Contains only distribution-facing files: chunks, query tools, docs, LanceDB databases. No secrets, no n8n workflows, no Fathom API scripts.

### Architecture Decision: Python-First

All chunking, embedding, and query logic lives in Python. n8n's role is orchestration only — one thin workflow that shells out to Python after the Merged Call Summarizer finishes. Rationale:

1. The published product is a Python project. One language, one test suite.
2. Chunking logic is testable from CLI without n8n.
3. Backfill is a one-shot CLI operation that doesn't belong in n8n.
4. The n8n integration is a single Execute Workflow with a Code node.

---

## 2. Content Tiers

| Tier | Date Range | Source | Content |
|------|-----------|--------|---------|
| **Tier 1 — Historical** | Before March 10, 2026 | Fathom API + manual download | Transcript only, no chat logs |
| **Tier 2 — Enriched** | March 10, 2026 onward | Merged Call Summarizer output | Transcript + chat log + extracted signal + recap |

Tier boundary: **March 10, 2026** — the first date the Merged Call Summarizer pipeline was used.

---

## 3. Repository Structure

All project files live under `community-brain/` in the n8n repo:

```
community-brain/
├── README.md                              # Project vision, quick start, setup options
├── CONTRIBUTING.md                        # How to help maintain
├── HOW-WE-BUILT-THIS.md                  # Pipeline documentation (educational)
├── LICENSE                                # MIT
├── pyproject.toml                         # Python project config, dependencies
│
├── chunks/                                # Primary distribution — import into Open WebUI
│   ├── historical/                        # Tier 1: pre-March 10, 2026
│   │   └── session-YYYY-MM-DD.md          # One markdown file per session
│   ├── enriched/                          # Tier 2: March 10, 2026+
│   │   └── session-YYYY-MM-DD.md          # One markdown file per session
│   └── manifest.json                      # Index of all sessions with metadata
│
├── raw-transcripts/                       # Raw Fathom transcripts (backfill input)
│   └── YYYY-MM-DD-session-title.txt       # [HH:MM:SS] Speaker: text format
│
├── raw-chunks/                            # Embedding-agnostic JSONL (all chunks, no embeddings)
│   └── all-chunks.jsonl
│
├── lancedb/                               # Path B: pre-embedded databases
│   ├── nomic-v1/
│   │   └── transcripts.lance/
│   └── openai-v1/
│       └── transcripts.lance/
│
├── src/                                   # All Python source code
│   └── community_brain/
│       ├── __init__.py
│       ├── chunk_utils.py                 # Core chunking logic (shared)
│       ├── backfill/
│       │   ├── __init__.py
│       │   ├── fetch_fathom.py            # Fathom API → raw transcript files
│       │   └── chunk_historical.py        # Raw transcripts → chunks
│       ├── enriched/
│       │   ├── __init__.py
│       │   └── chunk_enriched.py          # Summarizer output → chunks
│       ├── embed/
│       │   ├── __init__.py
│       │   ├── embed_nomic.py             # Chunks → LanceDB (nomic via Ollama)
│       │   └── embed_openai.py            # Chunks → LanceDB (OpenAI)
│       └── query/
│           ├── __init__.py
│           ├── query_local.py             # CLI: Ollama + LanceDB
│           ├── query_openai.py            # CLI: OpenAI + LanceDB
│           └── retrieval_server.py        # FastAPI wrapper
│
├── open-webui/                            # Open WebUI setup & integration
│   ├── docker-compose.yml                 # Open WebUI container config
│   ├── SETUP.md                           # Step-by-step setup guide
│   └── import-guide.md                    # How to import chunks
│
├── tests/                                 # Test suite
│   ├── test_chunk_utils.py
│   ├── test_backfill.py
│   ├── test_enriched.py
│   └── fixtures/                          # Sample data for testing
│       ├── sample-transcript.txt
│       └── sample-output/
│
└── config/                                # Configuration
    ├── .env.example                       # Template for env vars
    └── speaker-aliases.json               # Optional speaker name normalization
```

The n8n workflow for the enriched pipeline goes in `workflows/` at repo root, alongside existing workflows.

---

## 4. Sub-project 0: Open WebUI + Ollama Setup

### Scope

Docker Compose config on Mac Mini (10.1.50.219) for Open WebUI, connecting to the existing Ollama instance already running natively on the same machine.

### Components

- **Open WebUI container** — latest image, exposed on port 3000
- **Ollama connection** — points to existing instance at `http://10.1.50.219:11434` (or `host.docker.internal:11434`)
- **Persistent volume** — Open WebUI data (knowledge bases, chat history, user config)

### Pre-existing (no action needed)

- Ollama running on Mac Mini
- `gemma4:e4b` pulled and working
- `nomic-embed-text` pulled and working

### Deliverable

`open-webui/docker-compose.yml` with the container config.

### Verification Gate

1. Open WebUI loads in browser at `http://10.1.50.219:3000`
2. Gemma 4 E4B and nomic-embed-text appear as available models
3. Create a test Knowledge collection, import a sample markdown file
4. Ask Gemma 4 a question about the file's content, get a correct answer

---

## 5. Sub-project 1: Backfill Pipeline

### 5.1 Fathom Fetch (`fetch_fathom.py`)

**Two-track input:**

1. **API track** — Script pages through Fathom `GET /meetings` with `created_after`/`created_before` filters. For each meeting, fetches transcript via `GET /recordings/{id}/transcript`. Saves to `raw-transcripts/YYYY-MM-DD-session-title.txt`.
2. **Manual track** — Brandon's sessions downloaded from the Fathom website and placed directly into `raw-transcripts/` with the same naming convention.

**Rate limiting:**
- 60 calls/minute max (from Fathom docs)
- Read `RateLimit-Remaining` and `RateLimit-Reset` headers
- Backoff on 429 responses
- ~156 API calls total for ~78 sessions (list + fetch per session) = ~3 minutes

**Resumability:** Skips dates that already have a file in `raw-transcripts/`.

**Output format:** `[HH:MM:SS] Speaker Name: statement text` — same format the existing Fathom Poller already produces.

### 5.2 Core Chunking Logic (`chunk_utils.py`)

Shared by backfill and enriched pipelines.

**Sliding window, speaker-aware algorithm:**

1. Parse transcript into speaker turns: `(speaker, timestamp, text)`
2. Accumulate turns until approaching 500 tokens (counted via `tiktoken`)
3. At threshold, find nearest speaker boundary
4. Create chunk with ~50-token overlap (~10%) from end of previous chunk
5. Attach metadata to each chunk

**Rules:**
- Never split mid-sentence or mid-speaker-turn
- Prefer breaking at speaker transitions
- Each chunk includes a header: `## Session: {title} | Date: {date}`

**Metadata schema per chunk:**

```json
{
  "chunk_id": "2024-03-15-chunk-042",
  "session_date": "2024-03-15",
  "session_title": "RAG Architectures Deep Dive",
  "speakers_in_chunk": ["Patrick Chouinard", "Alice", "Bob"],
  "chunk_position": 42,
  "total_chunks_in_session": 87,
  "content_tier": "historical",
  "content_type": "transcript",
  "source": "fathom_transcript",
  "text": "... chunk text ..."
}
```

**Speaker normalization:** Uses `config/speaker-aliases.json` if present. Starts empty; populated after sample review if inconsistencies found.

### 5.3 Historical Chunking (`chunk_historical.py`)

**Input:** All files in `raw-transcripts/` for dates before March 10, 2026.

**Output (two formats):**

1. **Markdown** → `chunks/historical/session-YYYY-MM-DD.md`
   - YAML frontmatter with session metadata
   - All chunks for that session separated by `---`
   - This is what Open WebUI imports (Path A)

2. **JSONL** → appended to `raw-chunks/all-chunks.jsonl`
   - One JSON object per chunk with full metadata
   - This is what embedding scripts consume (Path B)

### 5.4 Manifest Generation

`chunks/manifest.json`:

```json
{
  "version": "1.0.0",
  "last_updated": "2026-04-12",
  "total_sessions": 78,
  "total_chunks": 9500,
  "tier_1_cutoff": "2026-03-10",
  "sessions": [
    {
      "date": "2024-10-15",
      "title": "Introduction to AI Coding Assistants",
      "content_tier": "historical",
      "chunk_count": 85,
      "speakers": ["Patrick Chouinard", "Alice", "Bob"],
      "duration_minutes": 105
    }
  ]
}
```

Regenerated whenever new sessions are added.

### 5.5 Verification Gate

1. Run fetch + chunk against 3-5 historical sessions
2. Review: chunk sizes, speaker boundary breaks, metadata completeness
3. Test import into Open WebUI (Sub-project 0)
4. Query imported chunks, verify relevant results
5. Sign-off, then bulk-process remaining ~73 sessions

---

## 6. Sub-project 2: Enriched Pipeline Extension

### 6.1 n8n Workflow: "Community Brain Chunker"

**Trigger:** Execute Workflow node appended to the end of the Merged Call Summarizer chain (after Save Weekly Invite).

**Receives:** Session date (`YYYY-MM-DD`) from the Summarizer.

**Action:** Single Code node that shells out to Python. Since n8n runs inside a Docker container and the `community-brain/` directory is on the host VM, the Code node uses `child_process.execSync` to run `docker exec` or calls a small HTTP endpoint on the host. The simplest approach: mount `community-brain/` into the n8n container as a volume (added to the existing `docker-compose.yml`) and install Python + dependencies inside the container. Alternatively, the Code node can make an HTTP request to a lightweight script running on the host.

The exact integration method will be determined during Sub-project 2 implementation based on what's cleanest with the existing Docker setup. Both approaches are viable.

```bash
# Option 1: Python inside n8n container (volume mount)
python3 /home/node/community-brain/src/community_brain/enriched/chunk_enriched.py --date YYYY-MM-DD

# Option 2: HTTP call to host-side script
curl -X POST http://host.docker.internal:8999/chunk --data '{"date": "YYYY-MM-DD"}'
```

The workflow JSON is stored in `workflows/` at repo root, documented in the same style as existing workflows in CLAUDE.md.

### 6.2 Enriched Chunking (`chunk_enriched.py`)

**Input:** Reads from `output/YYYY-MM-DD/` (Merged Call Summarizer output directory).

**Three sources chunked:**

| Source File | Strategy | Content Type |
|---|---|---|
| `transcript.txt` | Sliding window, speaker-aware, ~500 tokens | `transcript` |
| `extracted-signal.md` | One chunk per category | `categorized_links`, `categorized_tools`, `categorized_qa`, `categorized_insights`, `categorized_followups` |
| `community-post.md` | Sliding window, ~500 tokens | `recap_full` |

**Not chunked:** `community-post-compressed.md` and weekly invite — derivative content that would add noise.

**Category chunking (extracted-signal.md):**
- Parse by section headers (Shared Resources, Key Q&A, Key Insights, Tools & Concepts, Follow-Ups)
- One chunk per category per session
- If a category exceeds ~500 tokens, split at natural boundaries (e.g., between Q&A pairs)

### 6.3 Enriched Metadata

Same base schema as historical, plus enriched fields:

```json
{
  "chunk_id": "2026-04-07-enriched-tools-001",
  "session_date": "2026-04-07",
  "session_title": "Claude Code & Agentic Workflows",
  "speakers_in_chunk": ["Patrick Chouinard", "Carol"],
  "chunk_position": 1,
  "total_chunks_in_session": 65,
  "content_tier": "enriched",
  "content_type": "categorized_tools",
  "source": "n8n_enrichment_pipeline",
  "has_links": true,
  "has_chat_log_content": true,
  "text": "... chunk text ..."
}
```

### 6.4 Output

Same two formats:
- **Markdown** → `chunks/enriched/session-YYYY-MM-DD.md`
- **JSONL** → appended to `raw-chunks/all-chunks.jsonl`
- **Manifest** → `chunks/manifest.json` updated

### 6.5 Verification Gate

1. Run against 2-3 existing sessions in `output/` (2026-03-10, 2026-03-17, 2026-03-24)
2. Compare enriched chunks against historical chunks — schema consistency
3. Verify category chunks capture correct content boundaries
4. Test import into Open WebUI, query, verify results

---

## 7. Sub-project 3: Embedding + Query Tools

### 7.1 Embedding Scripts

**`embed_nomic.py`:**
- Input: `raw-chunks/all-chunks.jsonl`
- Calls Ollama at `OLLAMA_BASE_URL` (default: `http://10.1.50.219:11434`) with `nomic-embed-text`
- Output: `lancedb/nomic-v1/transcripts.lance/`
- Batch size: ~50 chunks
- Resumable: skips already-embedded chunk IDs
- Progress bar via `tqdm`

**`embed_openai.py`:**
- Same input, calls OpenAI API with `text-embedding-3-large`
- Requires `OPENAI_API_KEY`
- Output: `lancedb/openai-v1/transcripts.lance/`
- Batch size: ~100 chunks
- Same resumability

Both scripts are idempotent — re-running appends new chunks without duplicating.

### 7.2 CLI Query Tools

**`query_local.py`:**
```bash
python query_local.py "What tools were discussed for building RAG pipelines?"
```
- Embeds question via Ollama (`nomic-embed-text`)
- Searches `lancedb/nomic-v1/` for top-k chunks (default k=5)
- Sends chunks + question to Ollama (`gemma4:e4b`) for answer
- Prints answer with source citations (session date, chunk position)
- Flags: `--top-k`, `--model`, `--verbose`

**`query_openai.py`:**
- Same flow, uses OpenAI for embedding and inference
- Default model: `gpt-5.4-mini`
- Same flags

### 7.3 FastAPI Retrieval Server

**`retrieval_server.py`:**
- `POST /query` — `{"question": "...", "top_k": 5, "embedding_backend": "ollama|openai"}`
- Returns ranked chunks with metadata and similarity scores
- Retrieval only — no LLM inference. Caller handles generation.
- Configurable: `OLLAMA_BASE_URL`, `OPENAI_API_KEY`, `LANCEDB_PATH`

### 7.4 Verification Gate

1. Embed 3-5 sessions into both LanceDB variants
2. Run test queries against known content
3. Verify relevant chunks returned with correct metadata
4. Test both CLI tools end-to-end
5. Test FastAPI server with curl

---

## 8. Sub-project 4: Open WebUI Integration + Docs + Release

### 8.1 Bulk Import Script (`import_openwebui.py`)

- Uses Open WebUI REST API:
  1. `POST /api/v1/files/` — upload file
  2. `GET /api/v1/files/{id}/process/status` — poll until processed
  3. `POST /api/v1/knowledge/{id}/file/add` — add to Knowledge collection
- Creates a "Community Brain" Knowledge collection
- Iterates all markdown files in `chunks/historical/` and `chunks/enriched/`
- Progress bar, resumable (skips already-imported files)
- Configurable: `OPEN_WEBUI_URL` env var

### 8.2 Documentation

**`README.md`:**
- Community framing: "You built this knowledge base together — here's your copy"
- Quick start: clone → import → query in under 10 minutes
- Three setup options: Open WebUI (recommended), LanceDB CLI, FastAPI
- Model recommendations: Gemma 4 E4B default, model-agnostic note
- Content notice, versioning, exclusion policy

**`HOW-WE-BUILT-THIS.md`:**
- Chunking strategy and rationale
- Embedding model tradeoffs
- n8n enrichment pipeline overview (high level, no secrets)
- How to replicate for other communities
- Lessons learned

**`open-webui/SETUP.md`:**
- Install Ollama, pull gemma4:e4b and nomic-embed-text
- Docker Compose for Open WebUI
- Verify connection to Ollama
- Import chunks (manual or scripted)

**`open-webui/import-guide.md`:**
- UI and API import methods
- Expected re-embedding time (~10-15 min for ~10K chunks)
- Verification steps
- Troubleshooting

**`CONTRIBUTING.md`:**
- Adding new sessions
- Improving chunk quality
- Adding embedding variants

### 8.3 Release Prep

- MIT LICENSE file
- Set up public `community-brain` repo (name finalized with Brandon)
- Sync script or documented process to push distribution files from dev to public repo
- Cut `v1.0.0` release with all historical + enriched data
- Draft Skool community notice

### 8.4 Verification Gate

Full end-to-end: fresh Open WebUI instance, run import script, query with Gemma 4. Confirm "clone to querying in under 10 minutes" goal.

---

## 9. Configuration

### Environment Variables (`config/.env.example`)

```bash
# Fathom API (backfill only, not needed by end users)
FATHOM_API_KEY=

# Ollama (Mac Mini)
OLLAMA_BASE_URL=http://10.1.50.219:11434

# OpenAI (optional, for Path B OpenAI variant)
OPENAI_API_KEY=

# Open WebUI (for bulk import script)
OPEN_WEBUI_URL=http://10.1.50.219:3000

# LanceDB path (for query tools + retrieval server)
LANCEDB_PATH=./lancedb/nomic-v1
```

### Speaker Aliases (`config/speaker-aliases.json`)

```json
{}
```

Starts empty. Populated only if inconsistencies found during Sub-project 1 sample review.

### Python Dependencies (`pyproject.toml`)

- `tiktoken` — token counting
- `httpx` — HTTP client (Fathom API, Open WebUI API)
- `lancedb` — vector store
- `fastapi` + `uvicorn` — retrieval server
- `openai` — OpenAI embedding/inference
- `ollama` — Ollama Python client
- `click` — CLI interfaces
- `python-dotenv` — env var loading
- `tqdm` — progress bars
- `pytest` — testing

---

## 10. Fathom API Details

- **Rate limit:** 60 calls per 60-second window
- **Headers:** `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset`
- **Estimated calls:** ~156 (list pages + transcript fetches for ~78 sessions)
- **Estimated time:** ~3 minutes with pacing
- **Backoff:** Respect 429 status, wait per `RateLimit-Reset` header

---

## 11. What Gets Published vs What Stays Private

### Published (public repo)

```
community-brain/
├── README.md
├── CONTRIBUTING.md
├── HOW-WE-BUILT-THIS.md
├── LICENSE
├── pyproject.toml
├── chunks/                    # All session markdown files + manifest
├── raw-chunks/                # JSONL for re-embedding
├── lancedb/                   # Pre-embedded databases
├── src/community_brain/
│   ├── chunk_utils.py         # Shared chunking logic
│   ├── embed/                 # Embedding scripts
│   └── query/                 # Query tools + retrieval server
├── open-webui/                # Setup guides + docker-compose
├── tests/                     # Test suite
└── config/
    ├── .env.example
    └── speaker-aliases.json
```

### Private (stays in n8n repo)

- `src/community_brain/backfill/` — Fathom API fetch scripts (uses private API key)
- `src/community_brain/enriched/` — Depends on n8n pipeline output structure
- `raw-transcripts/` — Raw Fathom transcripts (not distributed)
- `config/.env` — Actual secrets
- n8n workflow JSON (`workflows/community-brain-chunker.json`)

---

## 12. Open Questions Resolved

| PRD Question | Resolution |
|---|---|
| Fathom API access | API for own sessions; manual download for Brandon's sessions |
| Session titles | Use from Fathom metadata; infer from content if unavailable |
| Speaker normalization | As-is with optional alias map after sample review |
| Enriched pipeline cutoff | March 10, 2026 |
| Open WebUI import format | Markdown files (one per session), with bulk import script using REST API |
| Repository naming | Placeholder `community-brain`, finalized with Brandon later |
| License | MIT |
| Exclusion requests | Manual redaction; process documented in CONTRIBUTING.md |
| n8n integration method | Execute Workflow node → Code node → shell exec to Python |
| Chunk format validation | 3-5 session sample review before bulk processing |

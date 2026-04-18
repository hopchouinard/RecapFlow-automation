# Community Brain — Implementation Specification

## Document Purpose

This document is a comprehensive implementation specification for a project codenamed **Community Brain**. It captures every architectural decision, design rationale, pipeline requirement, and long-term plan discussed during the design session. It is intended to be handed directly to Claude Code for implementation.

**Do not deviate from the decisions documented here without explicit instruction from the project owner.**

---

## 1. Project Vision

### 1.1 What This Is

Community Brain is an open-source, downloadable vector database containing the complete vectorized corpus of every AI community coaching call transcript accumulated over approximately 18 months (~78 weeks) of weekly sessions. Each session runs 1.5–2 hours.

The database is designed to be queried locally by community members using their own AI models and inference costs. The project owner builds and maintains the database; community members bring their own AI (BYO-AI).

### 1.2 Core Philosophy

- The content was created collectively by the community. The community deserves access to it in a queryable form.
- The project owner absorbs the cost of curation, chunking, embedding, and pipeline maintenance.
- The project owner does NOT absorb the cost of inference. Each user pays for their own query costs (which are zero if using local models).
- The recommended query path is fully local and free: Ollama + Open WebUI + Gemma 4.

### 1.3 Framing

The README should open with something to the effect of: *"You built this knowledge base together — here's your copy of it."*

### 1.4 Branding and Distribution

- This is a **standalone open-source project**. It is NOT branded under PatchouTech.
- The content belongs to the community. The architecture and pipeline are credited to the project owner as maintainer.
- Distribution is via a **public GitHub repository** with versioned releases.
- A suitable GitHub org or repo name should reflect the community identity (e.g., `ai-coaching-collective` or similar — to be decided by the project owner).

---

## 2. Corpus Description

### 2.1 Content Sources

There are two distinct tiers of content quality, and the pipeline must handle both:

#### Tier 1 — Historical Transcripts (Backfill)

- **Source:** Fathom API
- **Format:** Raw transcripts with speaker attribution and datetime timestamps per statement
- **Enrichment:** None. No chat logs available for historical sessions.
- **Volume:** ~78 weeks of sessions
- **Estimated size:** ~1.2–1.4 million words (~4,000–5,000 pages of text)
- **Estimated chunks:** ~8,000–12,000 chunks (at ~500-token chunks with overlap)

#### Tier 2 — Enriched Weekly Output (Ongoing Pipeline)

- **Source:** Existing n8n pipeline that merges the Fathom verbal transcript with the Zoom chat log
- **Enrichment:** The n8n pipeline produces multiple outputs:
  1. **Categorized facts list** — Raw information categorized by type: links, tools, questions, Q&A pairs, etc. Contains some names but not the original speaker-timestamp format.
  2. **Full detailed recap** — Comprehensive session recap
  3. **Compressed recap** — Shortened version for readability
  4. **Next week's invite** — Generated prompt/invite for the following coaching call
- **Key advantage:** Contains chat log content including all shared links, tool mentions, and inline discussion — significantly richer than transcript alone.

### 2.2 Content Awareness and Consent

- All sessions have been recorded using Fathom since inception. Participants are aware.
- Both video and written transcripts are published weekly on the public Skool community site.
- Vectorizing already-public content does not change the scope of access — it changes the convenience of access.
- **Recommended action:** Post a courtesy notice to the community before release, along the lines of: *"I'm packaging all our call transcripts into a downloadable vector database so anyone can query the full history with their own AI tools. This uses the same transcripts already posted here. If you want specific contributions excluded, let me know."*
- For members who have left the community: they participated while the recording/publishing policy was in effect and the content is already public. No retroactive action required.

---

## 3. Architecture Decisions

### 3.1 Distribution Model — Open WebUI Native RAG (Path A)

After evaluating two approaches, the selected distribution model is **Path A: Open WebUI's native RAG functionality**.

#### What this means:

- The project distributes pre-chunked content as structured files (JSONL and/or markdown files).
- Users import these files into their own Open WebUI instance.
- Open WebUI handles embedding locally using whatever embedding model the user has configured in Ollama.
- Re-embedding ~10,000 chunks locally with `nomic-embed-text` via Ollama takes approximately 10–15 minutes on decent hardware. This is a one-time cost.

#### Why Path A over Path B:

- **Path B** (custom LanceDB + FastAPI retrieval backend) was considered. It preserves pre-computed embeddings and skips re-embedding, but adds significant complexity: users must run a separate service, manage LanceDB files, and deal with embedding model compatibility.
- **Path A** wins on friction. The goal is "downloaded the repo → asking questions in under 5 minutes." Open WebUI's native document import achieves this.
- **Path B is documented as an advanced option** for users who want it, but is not the primary path.

#### Path B — Advanced Option (LanceDB + FastAPI):

For users who want to skip re-embedding or use pre-computed embeddings:

- Distribute pre-embedded LanceDB directories (one per embedding model variant)
- Provide a thin FastAPI wrapper service that Open WebUI can call as a tool/function
- Embedding model variants:
  - `nomic-embed-text` (for fully local/free usage via Ollama)
  - `text-embedding-3-large` (for users with an OpenAI API key)
- Users download whichever LanceDB variant matches their preferred embedding model

### 3.2 Recommended Query Model

**Primary recommendation: Gemma 4 E4B** via Ollama.

#### Rationale:

- Gemma 4 was released April 2, 2026 under Apache 2.0 (fully permissive, no commercial restrictions)
- The E4B variant is the sweet spot for most laptops — runs locally at conversational speed
- For users with a GPU (16GB+ VRAM), the **26B MoE** variant is recommended — it activates only 3.8B parameters during inference while delivering near-flagship quality
- Context windows up to 256K tokens on larger models — more than sufficient for RAG chunk windows
- The task (comprehension and summarization of conversational transcripts) is well within the capabilities of even the smaller variants
- Already available in Ollama: `ollama pull gemma4:e4b`
- Requires Ollama 0.20 or newer

#### Important — Model Agnosticism:

The architecture must NOT be locked to Gemma 4. The README should frame it as: *"We recommend Gemma 4 E4B for the best balance of quality and accessibility. By the time you're reading this, there may be something better — use whatever works for you."*

Any model that works with Open WebUI + Ollama (or any OpenAI-compatible API) should work.

### 3.3 Embedding Model Strategy

For the primary distribution path (Path A / Open WebUI native RAG), the embedding model is whatever the user has configured in their Open WebUI instance. The project recommends `nomic-embed-text` via Ollama as the default.

For the advanced path (Path B / LanceDB), two pre-embedded variants are provided:

| Variant | Embedding Model | Use Case | Cost |
|---------|----------------|----------|------|
| Local | `nomic-embed-text` | Fully local via Ollama | Free |
| Cloud | `text-embedding-3-large` | OpenAI API users | Requires API key |

Users download whichever variant matches their setup.

### 3.4 Package Structure

```
community-brain/
├── README.md                          # Vision, setup guide, BYO-AI instructions
├── CONTRIBUTING.md                    # How to help maintain the project
├── HOW-WE-BUILT-THIS.md              # Detailed pipeline documentation (educational)
├── LICENSE                            # To be determined — likely MIT or Apache 2.0
│
├── chunks/                            # Primary distribution — import into Open WebUI
│   ├── historical/                    # Tier 1: raw transcript chunks
│   │   ├── session-YYYY-MM-DD.md      # One file per session (or JSONL)
│   │   └── ...
│   ├── enriched/                      # Tier 2: enriched pipeline output chunks
│   │   ├── session-YYYY-MM-DD.md
│   │   └── ...
│   └── manifest.json                  # Index of all sessions with metadata
│
├── raw-chunks/                        # Embedding-agnostic JSONL for re-embedding
│   └── all-chunks.jsonl               # Every chunk with metadata, no embeddings
│
├── lancedb/                           # Path B: pre-embedded databases
│   ├── nomic-v1/
│   │   └── transcripts.lance/
│   └── openai-v1/
│       └── transcripts.lance/
│
├── advanced/                          # Path B: FastAPI retrieval wrapper
│   ├── retrieval-server.py            # Thin FastAPI service wrapping LanceDB
│   └── requirements.txt
│
├── scripts/                           # Pipeline tooling
│   ├── backfill/
│   │   ├── fetch-fathom-transcripts.py   # Fathom API → raw transcript files
│   │   └── chunk-historical.py           # Raw transcripts → chunked output
│   ├── embed/
│   │   ├── embed-nomic.py                # Chunk JSONL → LanceDB (nomic)
│   │   └── embed-openai.py               # Chunk JSONL → LanceDB (OpenAI)
│   └── utils/
│       └── chunk-utils.py                # Shared chunking logic
│
├── query/                             # Convenience query tools
│   ├── query_local.py                 # Example: Ollama + LanceDB CLI query
│   ├── query_openai.py                # Example: OpenAI API + LanceDB CLI query
│   └── requirements.txt
│
└── open-webui/                        # Open WebUI integration guide
    ├── SETUP.md                       # Step-by-step Open WebUI + Ollama setup
    └── import-guide.md                # How to import chunks into Open WebUI
```

---

## 4. Pipeline Specifications

### 4.1 Historical Backfill Pipeline

#### Step 1: Fetch Transcripts from Fathom API

- **Script:** `scripts/backfill/fetch-fathom-transcripts.py`
- **Input:** Fathom API credentials, date range covering all historical sessions
- **Output:** One raw transcript file per session, stored with naming convention `YYYY-MM-DD-session-title.txt`
- **Format:** Each line should preserve: speaker name, timestamp, statement text
- **Error handling:** Log any sessions that fail to fetch; allow re-running for specific date ranges

#### Step 2: Chunk Historical Transcripts

- **Script:** `scripts/backfill/chunk-historical.py`
- **Input:** Raw transcript files from Step 1
- **Output:** Chunked JSONL + individual session markdown files

#### Chunking Strategy for Historical Content (Tier 1):

- **Method:** Sliding window, speaker-aware boundaries
- **Chunk size:** ~500 tokens
- **Overlap:** ~50 tokens (approximately 10% overlap)
- **Speaker awareness:** Never split a chunk mid-sentence or mid-speaker-turn. Prefer breaking at speaker transitions.
- **Context preservation:** Each chunk should include a brief header with session date and session title (if available)

#### Metadata per chunk:

```json
{
  "chunk_id": "2024-03-15-chunk-042",
  "session_date": "2024-03-15",
  "session_title": "RAG Architectures Deep Dive",
  "speakers_in_chunk": ["Patrick", "Alice", "Bob"],
  "chunk_position": 42,
  "total_chunks_in_session": 87,
  "content_tier": "historical",
  "source": "fathom_transcript",
  "text": "... the actual chunk text ..."
}
```

### 4.2 Ongoing Enriched Pipeline Extension

This integrates into the existing n8n pipeline that already processes each weekly session.

#### New Step in Existing Pipeline:

After the n8n pipeline produces its outputs (categorized facts, full recap, compressed recap, next week invite), add a vectorization step that:

1. Takes the **categorized facts list** and chunks it **by category** (all links together, all tools together, all Q&A pairs together, etc.)
2. Takes the **full detailed recap** and chunks it using the same sliding-window strategy as historical content
3. Takes the **raw transcript** (with speaker attribution) and chunks it with speaker-aware boundaries
4. Outputs all chunks to the same JSONL format with enriched metadata

#### Chunking Strategy for Enriched Content (Tier 2):

- **Category chunks** (from categorized facts): One chunk per category per session. If a category is very large, split at natural boundaries.
- **Recap chunks** (from full recap): Sliding window, ~500 tokens, ~50 token overlap
- **Transcript chunks** (from raw transcript): Same as historical — sliding window, speaker-aware, ~500 tokens

#### Enriched Metadata per chunk:

```json
{
  "chunk_id": "2026-04-01-enriched-tools-001",
  "session_date": "2026-04-01",
  "session_title": "Gemma 4 Launch Discussion",
  "speakers_in_chunk": ["Patrick", "Carol"],
  "chunk_position": 1,
  "total_chunks_in_session": 65,
  "content_tier": "enriched",
  "content_type": "categorized_tools",
  "source": "n8n_enrichment_pipeline",
  "has_links": true,
  "has_chat_log_content": true,
  "text": "... the actual chunk text ..."
}
```

#### Content Types for `content_type` Field:

- `transcript` — Raw speaker-attributed transcript chunk
- `recap_full` — Chunk from the full detailed recap
- `recap_compressed` — Chunk from the compressed recap
- `categorized_links` — Extracted links from the session
- `categorized_tools` — Tool mentions and discussions
- `categorized_qa` — Question and answer pairs
- `categorized_general` — General categorized information

### 4.3 Embedding Pipeline (Path B Only)

- **Scripts:** `scripts/embed/embed-nomic.py` and `scripts/embed/embed-openai.py`
- **Input:** `raw-chunks/all-chunks.jsonl`
- **Output:** LanceDB directories under `lancedb/nomic-v1/` and `lancedb/openai-v1/`
- **Nomic embedding:** Uses `nomic-embed-text` via Ollama's local API (`http://localhost:11434/api/embeddings`)
- **OpenAI embedding:** Uses `text-embedding-3-large` via OpenAI API (requires `OPENAI_API_KEY` environment variable)
- **Both scripts must be idempotent:** Running them again should update/append, not duplicate

### 4.4 Manifest File

`chunks/manifest.json` serves as the index of all sessions:

```json
{
  "version": "1.0.0",
  "last_updated": "2026-04-08",
  "total_sessions": 78,
  "total_chunks": 9500,
  "sessions": [
    {
      "date": "2024-10-15",
      "title": "Introduction to AI Coding Assistants",
      "content_tier": "historical",
      "chunk_count": 85,
      "speakers": ["Patrick", "Alice", "Bob", "Carol"],
      "duration_minutes": 105
    }
  ]
}
```

---

## 5. Release and Update Strategy

### 5.1 Versioning

- Use **GitHub Releases** with semantic versioning
- `v1.0.0` = Initial release covering all historical backfill (~78 weeks)
- `v1.1.0` = Adds one quarter of new enriched sessions
- Subsequent releases add new sessions incrementally
- Breaking changes to chunk format or metadata schema bump the major version

### 5.2 Update Cadence

- New sessions are added as they occur through the enriched pipeline
- GitHub releases are cut periodically (suggested: quarterly) so users can pull a fresh snapshot
- Between releases, users can manually download individual new session files if published incrementally

### 5.3 Historical Note

Sessions before a certain date (to be determined based on when the enriched pipeline went live) contain transcript-only content without chat logs. The README and manifest should clearly note this:

> *"Sessions before [date] contain transcript content only. Sessions from [date] onward include enriched content with chat logs, shared links, and categorized information."*

---

## 6. User-Facing Documentation

### 6.1 README.md

Must include:

1. **Project vision** — What this is, why it exists, the "third brain" concept
2. **Quick start** — Fastest path from download to querying (Open WebUI + Ollama + Gemma 4)
3. **What's inside** — Description of the corpus, content tiers, what metadata is available
4. **Setup options:**
   - **Option A (Recommended):** Open WebUI native RAG — import chunks, use any model
   - **Option B (Advanced):** LanceDB + FastAPI — pre-embedded, skip re-embedding
   - **Option C (Minimal):** CLI query scripts for quick one-off questions
5. **Model recommendations** — Gemma 4 E4B as default, 26B MoE for GPU users, with explicit note about model agnosticism
6. **Content notice** — Attribution to the community, consent policy, how to request exclusion
7. **Versioning and updates** — How to get new sessions

### 6.2 HOW-WE-BUILT-THIS.md

This is the educational companion document. It must explain:

1. The chunking strategy and why those decisions were made
2. The embedding model choices and tradeoffs
3. The n8n enrichment pipeline architecture (high level)
4. How to replicate this pattern for other communities or corpora
5. Lessons learned

This document is as important as the database itself. It turns a download into a replicable pattern.

### 6.3 open-webui/SETUP.md

Step-by-step guide:

1. Install Ollama
2. Pull Gemma 4 E4B: `ollama pull gemma4:e4b`
3. Pull an embedding model: `ollama pull nomic-embed-text`
4. Install and run Open WebUI (Docker command provided)
5. Import the chunk files from the `chunks/` directory
6. Start querying

### 6.4 open-webui/import-guide.md

Specific instructions for importing the session files into Open WebUI's document/knowledge system, including:

- How to organize them (by date, by tier, all at once)
- Expected re-embedding time
- How to verify the import worked
- Troubleshooting common issues

---

## 7. Query Application

### 7.1 Scope

The project owner is willing to build a complete query application — not just distribute a raw database. The application should be "plug your API key or Ollama endpoint and go."

### 7.2 Primary Interface — Open WebUI

The primary recommended interface is Open WebUI with Ollama. This is not a custom-built UI — it's leveraging an existing, mature, open-source project that already handles:

- Chat interface
- RAG document management
- Model selection
- Conversation history
- Multi-user support (if needed)

### 7.3 CLI Query Tools (Fallback)

For users who don't want to run Open WebUI, provide simple CLI scripts:

#### `query/query_local.py`

- Uses Ollama for both embedding and inference
- Points at LanceDB directory (Path B)
- Simple: `python query_local.py "What tools were discussed for building RAG pipelines?"`
- Auto-detects whether Ollama is running locally

#### `query/query_openai.py`

- Uses OpenAI API for both embedding and inference
- Points at LanceDB directory (Path B)
- Requires `OPENAI_API_KEY` environment variable
- Simple: `python query_openai.py "What were the key takeaways about prompt engineering?"`

### 7.4 Advanced — FastAPI Retrieval Server (Path B)

`advanced/retrieval-server.py`:

- Thin FastAPI service wrapping LanceDB
- Exposes a `/query` endpoint that accepts a question, embeds it, retrieves top-k chunks, and returns them
- Can be called by Open WebUI as a function/tool
- Configurable embedding backend (Ollama or OpenAI)
- This is for users who want maximum control or want to build their own frontend

---

## 8. Technical Requirements

### 8.1 Language and Dependencies

- **Primary language:** Python 3.11+
- **Embedding/vector store:** LanceDB (for Path B)
- **HTTP framework:** FastAPI + uvicorn (for Path B retrieval server)
- **Fathom integration:** httpx or requests for Fathom API calls
- **Ollama integration:** ollama Python package or raw HTTP to `localhost:11434`
- **OpenAI integration:** openai Python package
- **Chunking:** tiktoken for token counting, custom chunking logic
- **Data format:** JSONL for chunk interchange, markdown for Open WebUI import files

### 8.2 Environment Variables

```bash
# Required for backfill
FATHOM_API_KEY=...

# Required for OpenAI embedding (Path B only)
OPENAI_API_KEY=...

# Optional — Ollama endpoint override
OLLAMA_BASE_URL=http://localhost:11434
```

### 8.3 Minimum User Requirements (for querying)

| Setup | RAM | Storage | GPU | Software |
|-------|-----|---------|-----|----------|
| Gemma 4 E4B (recommended) | 8GB+ | ~10GB | Optional | Ollama 0.20+, Open WebUI |
| Gemma 4 26B MoE | 16GB+ | ~20GB | 16GB+ VRAM | Ollama 0.20+, Open WebUI |
| OpenAI API | Any | ~500MB | None | Python 3.11+, API key |

---

## 9. Implementation Phases

### Phase 1 — Backfill Pipeline

1. Build `fetch-fathom-transcripts.py` — pull all historical transcripts via Fathom API
2. Build `chunk-utils.py` — shared chunking logic (sliding window, speaker-aware)
3. Build `chunk-historical.py` — process raw transcripts into chunked JSONL + markdown
4. Generate `manifest.json`
5. Test: verify chunk quality, metadata completeness, no data loss

### Phase 2 — Enriched Pipeline Extension

1. Design the n8n workflow node that takes enriched pipeline outputs and produces chunks
2. Build category-aware chunking for the categorized facts output
3. Integrate transcript + recap + category chunks into the same JSONL schema
4. Test: run against 2–3 recent sessions to validate

### Phase 3 — Embedding Pipeline (Path B)

1. Build `embed-nomic.py` — batch embed all chunks via Ollama
2. Build `embed-openai.py` — batch embed all chunks via OpenAI API
3. Generate LanceDB directories
4. Test: verify similarity search returns relevant results

### Phase 4 — Query Tools

1. Build `query_local.py` and `query_openai.py` CLI tools
2. Build `retrieval-server.py` FastAPI wrapper
3. Test: end-to-end query flow for both paths

### Phase 5 — Open WebUI Integration

1. Write `SETUP.md` — complete setup guide
2. Write `import-guide.md` — chunk import instructions
3. Determine optimal file format for Open WebUI import (markdown vs. JSONL vs. PDF)
4. Test: full flow from fresh Open WebUI install to successful query

### Phase 6 — Documentation and Release

1. Write `README.md`
2. Write `HOW-WE-BUILT-THIS.md`
3. Write `CONTRIBUTING.md`
4. Create GitHub repo
5. Cut `v1.0.0` release with all historical data
6. Post community notice on Skool

---

## 10. Open Questions for Project Owner

These items were not fully resolved during the design session and require decisions before or during implementation:

1. **Fathom API access:** Confirm API credentials and any rate limits. Are all ~78 sessions accessible via the API, or do some require manual download?

2. **Session titles:** Do historical Fathom transcripts have reliable session titles, or will titles need to be inferred/generated from content?

3. **Speaker name normalization:** Are speaker names consistent across sessions in Fathom transcripts, or do they vary (e.g., "Patrick C." vs "Patrick Chouinard" vs "Patchou")?

4. **Enriched pipeline cutoff date:** What is the exact date when the n8n enrichment pipeline went live? This determines the Tier 1 / Tier 2 boundary.

5. **Open WebUI import format:** The optimal format for Open WebUI document import needs testing. Markdown files (one per session) are the likely best option, but this should be validated against Open WebUI's current document handling.

6. **Repository naming and org:** Final decision on GitHub org/repo name.

7. **License:** MIT, Apache 2.0, or another open-source license for the project code. Note: the license covers the tooling and structure, not the content itself (which belongs to the community).

8. **Exclusion requests:** Process for handling any community member exclusion requests — manual redaction script, or more automated?

9. **n8n integration method:** How the new chunking step plugs into the existing n8n workflow — as a new node, a webhook call to a Python script, or an n8n code node?

10. **Chunk format validation:** Before bulk processing, run 2–3 sessions through the pipeline and have the project owner review chunk quality, boundary decisions, and metadata completeness.

---

## 11. Success Criteria

The project is considered complete when:

- [ ] All ~78 historical sessions are chunked and available in the `chunks/` directory
- [ ] The enriched pipeline extension is integrated and processing new sessions
- [ ] At least one pre-embedded LanceDB variant exists (nomic) for Path B users
- [ ] A user can go from `git clone` to querying the database in under 10 minutes using Open WebUI + Ollama + Gemma 4
- [ ] The CLI query tools work for both Ollama and OpenAI backends
- [ ] All documentation (README, HOW-WE-BUILT-THIS, SETUP, import guide) is complete
- [ ] The manifest.json accurately reflects all available content
- [ ] The project owner has reviewed chunk quality on a sample of sessions
- [ ] A community notice has been posted on Skool

---

*Document generated: April 8, 2026*
*Design session participants: Patrick (Patchou) Chouinard, Claude (Anthropic)*
*Implementation target: Claude Code*

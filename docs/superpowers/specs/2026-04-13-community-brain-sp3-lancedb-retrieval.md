# Community Brain — Sub-project 3: LanceDB Embedding + Retrieval

**Date:** 2026-04-13
**Status:** Draft
**Parent:** [Master Architecture](2026-04-12-community-brain-architecture.md)
**Depends on:** SP1 v2 chunking pipeline (topic-aware chunks with summaries available in `raw-chunks/all-chunks.jsonl`)

---

## 1. Goal

Build the embedding pipeline, CLI query tools, and FastAPI retrieval server using LanceDB. Validate that summary-based embedding produces high-quality retrieval for the 3 sample sessions before proceeding to bulk processing.

**This is now the primary retrieval path.** Open WebUI's native RAG failed to produce acceptable retrieval quality (see SP1 v2 validation). Open WebUI remains the chat interface, but retrieval is handled by our LanceDB + FastAPI backend.

---

## 2. Scope

1. **`embed_nomic.py`** — Embed chunk summaries into LanceDB using nomic-embed-text via Ollama
2. **`embed_openai.py`** — Embed chunk summaries into LanceDB using text-embedding-3-large via OpenAI
3. **`query_local.py`** — CLI query tool using Ollama for embedding + inference
4. **`query_openai.py`** — CLI query tool using OpenAI for embedding + inference
5. **`retrieval_server.py`** — FastAPI server for Open WebUI integration

### Out of Scope

- Bulk processing of all 78 sessions (deferred until retrieval quality validated)
- Open WebUI function/tool integration (documented for SP4, not built here)
- Enriched (Tier 2) pipeline (SP2)

---

## 3. Core Design: Dual-Field Embedding

The key architectural decision: **embed the summary, store the full text.**

```
LanceDB Table: "transcripts"
┌─────────────┬────────────────────┬──────────────────┬────────────┬───────────┐
│ chunk_id     │ summary (embedded) │ text (stored)    │ topic      │ metadata  │
├─────────────┼────────────────────┼──────────────────┼────────────┼───────────┤
│ 2025-09-02- │ "Group discusses   │ "[00:02:29]      │ "AI Tools  │ {date,    │
│ chunk-001   │  Codex in Cursor   │  Patrick: Did    │  and New   │  speakers,│
│             │  and Google image  │  anybody try...  │  Tech      │  tier,    │
│             │  gen tools"        │  ..."            │  Adoption" │  ...}     │
└─────────────┴────────────────────┴──────────────────┴────────────┴───────────┘
```

- **Search** runs against the `summary` vector — short, focused, matches queries well
- **Results** return the `text` column — full transcript for LLM answer generation
- **Metadata filtering** available on `session_date`, `speakers_in_chunk`, `topic`, `content_tier`

---

## 4. LanceDB Table Schema

```python
import lancedb
from lancedb.pydantic import LanceModel, Vector

class TranscriptChunk(LanceModel):
    chunk_id: str
    session_date: str
    session_title: str
    topic: str
    summary: str                    # This field gets embedded
    text: str                       # Full transcript content (stored, not embedded)
    speakers_in_chunk: str          # JSON-encoded list (LanceDB doesn't support list[str])
    chunk_position: int
    total_chunks_in_session: int
    content_tier: str
    content_type: str
    source: str
    vector: Vector(768)             # nomic-embed-text produces 768-dim vectors
```

For the OpenAI variant, `vector: Vector(3072)` (text-embedding-3-large dimensions).

---

## 5. Components

### 5.1 Embedding Script — Nomic (`src/community_brain/embed/embed_nomic.py`)

**CLI interface:**
```bash
# Embed all chunks
python -m community_brain.embed.embed_nomic

# Embed specific session
python -m community_brain.embed.embed_nomic --date 2025-09-02

# Dry run
python -m community_brain.embed.embed_nomic --dry-run
```

**Behavior:**
1. Read all chunks from `raw-chunks/all-chunks.jsonl`
2. For each chunk, call Ollama API to embed the `summary` field:
   - `POST http://{OLLAMA_BASE_URL}/api/embeddings` with `model: nomic-embed-text`
3. Create/append to LanceDB table at `lancedb/nomic-v1/transcripts.lance/`
4. Batch size: 50 chunks per batch (Ollama handles one at a time, but we batch DB writes)
5. Resumable: skip chunk_ids already in the table
6. Progress bar via tqdm
7. Log total token count and estimated time

**Estimated time:** ~10,000 chunks × ~50ms/embedding = ~8 minutes for full corpus

### 5.2 Embedding Script — OpenAI (`src/community_brain/embed/embed_openai.py`)

Same as nomic but uses OpenAI API:
- `POST https://api.openai.com/v1/embeddings` with `model: text-embedding-3-large`
- Batch size: 100 (OpenAI handles batches natively)
- Output: `lancedb/openai-v1/transcripts.lance/`
- Requires `OPENAI_API_KEY`

### 5.3 CLI Query Tool — Local (`src/community_brain/query/query_local.py`)

**CLI interface:**
```bash
python -m community_brain.query.query_local "What was discussed about Codex?"
python -m community_brain.query.query_local "What tools for RAG?" --top-k 10
python -m community_brain.query.query_local "GPU benchmarks" --verbose --model gemma4:e4b
```

**Behavior:**
1. Embed the query using nomic-embed-text via Ollama
2. Search `lancedb/nomic-v1/` for top-k similar chunks (default k=5)
3. Build a prompt: system context + retrieved chunks + user question
4. Send to Ollama (default model: `gemma4:e4b`) for answer generation
5. Print the answer with source citations:
   ```
   Answer: Patrick asked if anyone had tried Codex in Cursor. Shakur said he
   hadn't yet. The group noted that keeping up with new AI tool releases
   feels like a full-time job.

   Sources:
     [1] 2025-09-02 — AI Tools and New Tech Adoption (chunk-001)
     [2] 2025-09-02 — Coaching Call Logistics (chunk-002)
   ```

**Flags:**
- `--top-k N` — Number of chunks to retrieve (default: 5)
- `--model NAME` — Ollama model for answer generation (default: gemma4:e4b)
- `--verbose` — Show retrieved chunks before the answer
- `--filter-date YYYY-MM-DD` — Only search chunks from a specific date
- `--filter-speaker NAME` — Only search chunks containing a specific speaker

### 5.4 CLI Query Tool — OpenAI (`src/community_brain/query/query_openai.py`)

Same interface as local but uses OpenAI for both embedding and inference:
- Embedding: text-embedding-3-large
- Inference: gpt-5.4-mini (default, configurable)
- LanceDB path: `lancedb/openai-v1/`

### 5.5 FastAPI Retrieval Server (`src/community_brain/query/retrieval_server.py`)

**Endpoint:**
```
POST /query
{
  "question": "What was discussed about Codex?",
  "top_k": 5,
  "filter_date": null,
  "filter_speaker": null
}

Response:
{
  "chunks": [
    {
      "chunk_id": "2025-09-02-chunk-001",
      "session_date": "2025-09-02",
      "topic": "AI Tools and New Tech Adoption",
      "summary": "Group discusses Codex in Cursor and Google image gen...",
      "text": "[00:02:29] Patrick Chouinard: Did anybody get the chance...",
      "speakers": ["Patrick Chouinard", "Shakur", "Alex Rojas"],
      "score": 0.87
    }
  ]
}
```

**Retrieval only — no LLM inference.** The caller (Open WebUI, custom frontend) handles answer generation.

**Configuration:**
- `OLLAMA_BASE_URL` — Ollama endpoint for embedding queries
- `LANCEDB_PATH` — Path to LanceDB directory (default: `./lancedb/nomic-v1`)
- Port: 8999 (default, configurable via `--port`)

**Usage:**
```bash
python -m community_brain.query.retrieval_server
# or
uvicorn community_brain.query.retrieval_server:app --host 0.0.0.0 --port 8999
```

---

## 6. Dependencies

Add to `pyproject.toml`:
```toml
dependencies = [
    # existing...
    "lancedb>=0.15",
    "ollama>=0.4",
    "openai>=1.50",
    "fastapi>=0.115",
    "uvicorn>=0.32",
]
```

---

## 7. Testing Strategy

### Unit Tests

**`tests/test_embed.py`:**
- `test_build_lancedb_record` — Chunk → LanceDB record with correct fields
- `test_skip_existing` — Already-embedded chunks are skipped
- `test_summary_is_embedded_field` — The `summary` field is what gets vectorized

**`tests/test_query.py`:**
- `test_query_returns_results` — Mock LanceDB search returns ranked chunks
- `test_filter_by_date` — Date filter narrows results
- `test_filter_by_speaker` — Speaker filter works
- `test_verbose_output` — Verbose mode includes chunk text

**`tests/test_retrieval_server.py`:**
- `test_query_endpoint` — POST /query returns JSON with chunks
- `test_health_endpoint` — GET /health returns ok

### Integration Test

After embedding the 3 sample sessions:
1. Query: "What was discussed about Codex?" → should return chunk-001 from 2025-09-02
2. Query: "What tools for vector storage?" → should return RAG/database chunks
3. Query with date filter: "GPU benchmarks" filtered to 2025-09-02
4. Query with speaker filter: "What did Brandon say?" filtered to speaker "Brandon Hancock"

---

## 8. Verification Gate

SP3 is complete when:

- [ ] nomic embedding script processes all 3 sample sessions into LanceDB
- [ ] CLI query "What was discussed about Codex?" returns the correct topic chunk as top result
- [ ] CLI query with `--verbose` shows chunk summaries and text
- [ ] Metadata filtering by date and speaker works
- [ ] FastAPI server starts and responds to `/query` endpoint
- [ ] Query latency < 500ms for single queries
- [ ] All tests pass
- [ ] OpenAI embedding variant works (if key available)

**After validation:** Proceed to SP1 Task 10 (bulk processing), then embed all sessions.

---

## 9. Architecture for Open WebUI Integration (SP4 Preview)

Once the FastAPI retrieval server is working, Open WebUI can call it as a **function/tool**:

1. User asks a question in Open WebUI chat
2. Open WebUI calls our FastAPI `/query` endpoint
3. Server returns top-k chunks with summaries and text
4. Open WebUI feeds the chunks to Gemma 4 for answer generation

This gives us the best of both worlds: Open WebUI's chat interface + our controlled retrieval pipeline.

The actual Open WebUI function/tool setup is SP4 scope — but the FastAPI server built here is the foundation.

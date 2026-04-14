# Community Brain SP4: Open WebUI Integration

**Date:** 2026-04-13
**Status:** Draft
**Depends on:** SP3 (LanceDB embedding + retrieval server)

---

## 1. Goal

Wire the Community Brain retrieval pipeline into Open WebUI so users can query coaching call transcripts through a chat interface. Open WebUI handles the conversation UI; our FastAPI server handles retrieval; Ollama (gemma4:e4b) generates answers with retrieved context.

---

## 2. What's In Scope

1. **Open WebUI Filter Function** that intercepts user messages, calls the SP3 retrieval server, and injects retrieved chunks as system context before the LLM sees the prompt
2. **Retrieval server startup** as a background service (so it's always available when Open WebUI needs it)
3. **Model configuration** in Open WebUI with the filter attached
4. **System prompt** tuned for RAG answer generation with source citations
5. **End-to-end validation** through the Open WebUI chat interface

## 3. What's Out of Scope

- Bulk processing of remaining ~75 sessions (separate effort after pipeline is validated)
- OpenAI embedding path (nomic-embed-text via Ollama is the primary path)
- Open WebUI's native RAG (already tried, already failed; see architectural decisions)
- Multi-user access control / tenant isolation

---

## 4. Architecture

```
User → Open WebUI (Docker, localhost:3000)
         │
         ├─ Filter Function (inlet)
         │    ├─ Extract user's question from last message
         │    ├─ POST http://host.docker.internal:8999/query
         │    │    with X-API-Key header, 3s timeout
         │    ├─ If retrieval succeeds + chunks found:
         │    │    ├─ Remove any prior [COMMUNITY_BRAIN_CONTEXT] block
         │    │    ├─ Build tagged system message with retrieved sources
         │    │    └─ Insert at position 0 in body["messages"]
         │    ├─ If no relevant chunks (all below min_score):
         │    │    └─ Inject "no relevant sources found" system message
         │    └─ If retrieval fails (timeout, auth, server down):
         │         └─ Inject "retrieval unavailable" system message
         │
         ├─ Ollama gemma4:e4b generates answer with context
         │
         └─ Response displayed in chat UI

Retrieval server (host, 0.0.0.0:8999, API key required)
    ├─ Embeds question via Ollama nomic-embed-text
    ├─ Searches LanceDB
    └─ Returns ranked chunks
```

The Filter function is the only new code. Everything else (retrieval server, LanceDB, Ollama) already exists from SP3.

### 4.1 Network Topology

Open WebUI runs in Docker Desktop. The retrieval server runs natively on the Mac Mini host. This means:

- The retrieval server **must** bind to `0.0.0.0` (not `127.0.0.1`) so Docker can reach it
- The filter **must** use `http://host.docker.internal:8999/query` (not `localhost`)
- **API key auth is mandatory**, not optional. Binding to `0.0.0.0` exposes the port to the local network. `RETRIEVAL_API_KEY` must be set and the filter must send it via `X-API-Key` header on every request.

This is a single-user, single-machine deployment, but the network exposure demands authentication regardless.

---

## 5. Filter Function Design

### 5.1 Approach: Filter (not Pipe)

A **Filter** with an `inlet` method is the right choice because:
- We want to keep using Open WebUI's normal model routing (Ollama gemma4:e4b)
- We only need to modify the input (add context), not replace the entire pipeline
- A Pipe would require us to handle streaming, model selection, and chat completion ourselves
- Filters can be enabled globally or per-model with zero model config changes

### 5.2 Filter Behavior

**inlet (pre-processing):**
1. Strip any existing `[COMMUNITY_BRAIN_CONTEXT]` system message from `body["messages"]` (idempotent replacement; prevents stale context from prior turns, retries, or regenerates)
2. Extract the user's latest message content
3. Call `POST {retrieval_url}` with `{question, top_k}`, `X-API-Key` header, and a **3-second timeout**
4. Handle the response:
   - **Chunks returned above `min_score`:** Build a tagged system message (`[COMMUNITY_BRAIN_CONTEXT]`) containing RAG instructions and each chunk formatted with source number, date, topic, summary, and full transcript text. Insert at position 0.
   - **No relevant chunks** (empty results or all below `min_score`): Insert a system message stating "No relevant coaching call sources were found for this question. Answer based on your general knowledge and clearly state that you are not drawing from transcript sources."
   - **Retrieval failure** (timeout, connection error, 4xx/5xx): Insert a system message stating "Community Brain retrieval is currently unavailable. Do not answer questions about coaching call content. Instead, inform the user that transcript search is temporarily unavailable and suggest they try again shortly."
5. Return modified body

**Design rationale:** The filter **fails closed**, not open. When retrieval is broken, the LLM must not hallucinate answers that look grounded. Users should always know whether they're getting sourced answers or not.

**Idempotency:** The `[COMMUNITY_BRAIN_CONTEXT]` tag in the system message content acts as a marker. On every inlet call, the filter first removes any message containing this tag, then inserts a fresh one. This prevents context accumulation across multi-turn chats, retries, and regenerate actions.

### 5.3 Valves (Configuration)

| Valve | Type | Default | Purpose |
|-------|------|---------|---------|
| `retrieval_url` | str | `http://host.docker.internal:8999/query` | Retrieval server endpoint (must use `host.docker.internal` for Docker→host) |
| `top_k` | int | 5 | Number of chunks to retrieve |
| `api_key` | str | `""` | **Required.** API key matching the server's `RETRIEVAL_API_KEY` |
| `timeout_seconds` | float | 3.0 | HTTP timeout for retrieval calls |
| `enabled` | bool | True | Toggle retrieval on/off (when off, no context injected) |
| `min_score` | float | 0.2 | Minimum similarity score to include a chunk |

### 5.4 System Prompt Template

```
You are Community Brain, an AI assistant with access to coaching call transcripts
from the AI Developer Accelerator community. Answer questions using ONLY the
retrieved sources below. Cite sources as [1], [2], etc.

If the sources don't contain relevant information, say so honestly rather than
making up an answer.

## Retrieved Sources

[Source 1] Date: {date} | Topic: {topic}
Speakers: {speakers}
Summary: {summary}
Transcript:
{text}

---

[Source 2] ...
```

---

## 6. Retrieval Server as Background Service

The SP3 FastAPI server needs to be running whenever Open WebUI might need it. Options:

**Option A: launchd service (recommended for Mac Mini)**
- Create a `~/Library/LaunchAgents/com.communitybrain.retrieval.plist`
- Auto-starts on login, restarts on crash
- Logs to a known location

**Option B: Docker sidecar**
- Add a retrieval server container to the Docker Compose alongside Open WebUI
- More complex (needs Python + deps in a container), but keeps everything containerized

**Recommendation:** Option A for now. The retrieval server is lightweight Python that runs natively on the Mac Mini. Dockerizing it adds complexity without benefit since LanceDB and Ollama are already local.

---

## 7. File Map

| Action | Path | Responsibility |
|--------|------|---------------|
| Create | `community-brain/src/community_brain/openwebui/community_brain_filter.py` | The Open WebUI Filter function (self-contained, copy-pasteable into Open WebUI) |
| Create | `community-brain/scripts/com.communitybrain.retrieval.plist` | launchd service definition for retrieval server |
| Create | `community-brain/scripts/start-retrieval-server.sh` | Shell script launched by launchd |
| Create | `community-brain/tests/test_filter.py` | Unit tests for filter logic |

Note: The filter function file is developed in our repo for version control + testing, but gets **copy-pasted into Open WebUI's Functions UI** for deployment. Open WebUI functions are stored in its own database, not read from disk.

---

## 8. Implementation Tasks

### Task 1: Community Brain Filter Function
- Create the filter Python file with `inlet` method
- Valves for all configuration (retrieval_url, api_key, top_k, timeout_seconds, min_score, enabled)
- HTTP call to retrieval server with timeout and X-API-Key header
- Idempotent context injection: strip prior `[COMMUNITY_BRAIN_CONTEXT]` block, insert fresh one
- Three-state handling: chunks found → inject sources; no chunks → inject disclaimer; failure → inject unavailable notice
- Unit tests covering: success path, no results, timeout, auth failure, idempotent replacement, min_score filtering

### Task 2: Retrieval Server Background Service
- Create launchd plist and start script
- Configure with `RETRIEVAL_HOST=0.0.0.0`, `RETRIEVAL_API_KEY`, `RETRIEVAL_PORT=8999`
- Test start/stop/auto-restart behavior
- Verify server is reachable from Open WebUI's Docker container via `host.docker.internal:8999`
- Verify unauthenticated requests are rejected (403)

### Task 3: Open WebUI Configuration
- Install the filter function via Open WebUI Functions UI
- Configure Valves (retrieval_url with `host.docker.internal`, api_key, top_k, etc.)
- Attach filter to gemma4:e4b model (or enable globally)
- Set up a "Community Brain" model preset with appropriate base system prompt

### Task 4: End-to-End Validation
- Query "Codex and image generation tools" through Open WebUI chat → verify citations
- Query "What tools for vector storage?" → verify pgvector discussion
- Multi-turn conversation → verify context refreshes per turn (no stale chunks)
- Click "Regenerate" → verify context replaced, not duplicated
- Stop retrieval server → verify "retrieval unavailable" message appears
- Set wrong API key in Valve → verify "retrieval unavailable" message
- Query with no relevant chunks → verify "no sources found" disclaimer
- Disable filter toggle → verify no retrieval context injected
- Measure query latency (target: < 2s including LLM generation)

---

## 9. Deployment Configuration

The retrieval server runs on the Mac Mini host; Open WebUI runs in Docker Desktop on the same machine.

**Retrieval server environment (set in launchd plist or shell):**
```
RETRIEVAL_HOST=0.0.0.0
RETRIEVAL_API_KEY=<generate-a-strong-random-key>
RETRIEVAL_PORT=8999
```

**Filter Valves (configured in Open WebUI Functions UI):**
```
retrieval_url = http://host.docker.internal:8999/query
api_key = <same-key-as-above>
top_k = 5
timeout_seconds = 3.0
min_score = 0.2
```

`host.docker.internal` is Docker Desktop for Mac's built-in DNS that resolves to the host machine. This is the only supported topology for this deployment.

---

## 10. Verification Checklist

| Check | Status |
|-------|--------|
| Filter function passes unit tests | |
| Retrieval server starts automatically via launchd | |
| API key auth enforced (request without key → 403) | |
| Filter installed and enabled in Open WebUI | |
| "Codex and image gen tools" returns relevant chunks with citations | |
| "What tools for vector storage?" returns pgvector discussion | |
| Multi-turn chat: context refreshes per turn (no stale chunks) | |
| Regenerate: context replaced, not duplicated | |
| Retrieval server down → user sees "retrieval unavailable" message | |
| Wrong API key → user sees "retrieval unavailable" message | |
| No relevant chunks → user sees "no sources found" disclaimer | |
| Query latency < 2s end-to-end | |
| Filter toggle works (disable → no retrieval context) | |

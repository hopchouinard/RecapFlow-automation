# Community Brain — Sub-project 0: Open WebUI + Ollama Setup

**Date:** 2026-04-12
**Status:** Approved
**Parent:** [Master Architecture](2026-04-12-community-brain-architecture.md)

---

## 1. Goal

Stand up an Open WebUI instance on the Mac Mini (10.1.50.219) connected to the existing Ollama installation. Verify that the RAG knowledge import pipeline works end-to-end before building the chunking infrastructure.

This is the foundation that all subsequent sub-projects validate against.

---

## 2. Pre-existing Infrastructure (No Action Needed)

| Component | Status | Location |
|---|---|---|
| Ollama | Running natively | Mac Mini 10.1.50.219:11434 |
| `gemma4:e4b` | Pulled and working | Ollama |
| `nomic-embed-text` | Pulled and working | Ollama |
| Docker Desktop | Installed | Mac Mini |

---

## 3. Deliverables

### 3.1 Docker Compose File

**Path:** `community-brain/open-webui/docker-compose.yml`

**Contents:**
- Open WebUI container (`ghcr.io/open-webui/open-webui:main`)
- Exposed on port 3000
- Connected to host Ollama via `OLLAMA_BASE_URL=http://host.docker.internal:11434`
- Persistent named volume for Open WebUI data (`open-webui-data`)
- No Ollama container — uses the existing native installation

**Environment variables:**
- `OLLAMA_BASE_URL` — Points to host Ollama
- `WEBUI_AUTH` — Set to `false` for initial setup (single-user, local network). Can be enabled later.

### 3.2 Setup Documentation

**Path:** `community-brain/open-webui/SETUP.md`

Step-by-step guide covering:
1. Prerequisites (Docker Desktop, Ollama with models pulled)
2. Starting the Open WebUI container (`docker compose up -d`)
3. Accessing the UI at `http://10.1.50.219:3000`
4. Verifying Ollama connection (models visible in UI)
5. Creating a Knowledge collection
6. Importing a test document
7. Querying the test document with Gemma 4

### 3.3 Test Fixture

**Path:** `community-brain/tests/fixtures/sample-session.md`

A small markdown file (~500 words) simulating a chunked session. Contains specific, verifiable facts that can be queried (e.g., "On January 15, 2025, the group discussed using LangChain for building RAG pipelines. Alice recommended starting with FAISS for prototyping."). This lets us confirm that Open WebUI's RAG retrieval returns correct content.

---

## 4. Docker Compose Specification

```yaml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
      - WEBUI_AUTH=false
    volumes:
      - open-webui-data:/app/backend/data
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped

volumes:
  open-webui-data:
```

**Notes:**
- `extra_hosts` mapping ensures `host.docker.internal` resolves correctly on Linux Docker (it's automatic on macOS Docker Desktop, but explicit is safer).
- Port mapping: Open WebUI listens on 8080 internally, exposed as 3000 on the host.
- `WEBUI_AUTH=false` disables login for single-user local use. The Mac Mini is on a private network (10.1.50.x).

---

## 5. Verification Gate

All of these must pass before Sub-project 0 is considered complete:

### 5.1 Container Health
- [ ] `docker compose up -d` succeeds without errors
- [ ] Open WebUI accessible at `http://10.1.50.219:3000`
- [ ] Container stays running (no crash loops)

### 5.2 Ollama Connection
- [ ] Open WebUI Settings > Models shows `gemma4:e4b` as available
- [ ] Open WebUI Settings > Models shows `nomic-embed-text` as available
- [ ] A simple chat message to Gemma 4 returns a coherent response (no connection errors)

### 5.3 RAG Knowledge Import
- [ ] Create a Knowledge collection named "Test"
- [ ] Upload `tests/fixtures/sample-session.md` to the collection
- [ ] Processing completes without error (file status shows as processed)
- [ ] Embedding model used is `nomic-embed-text`

### 5.4 RAG Query
- [ ] Start a new chat with Gemma 4 E4B
- [ ] Attach the "Test" Knowledge collection to the chat (or use `#Test` reference)
- [ ] Ask a question about a specific fact in the test document
- [ ] Response correctly references content from the uploaded document
- [ ] Delete the "Test" collection after verification

---

## 6. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| `host.docker.internal` doesn't resolve on Mac Docker Desktop | Fallback: use `http://10.1.50.219:11434` directly as `OLLAMA_BASE_URL` |
| Ollama not listening on external interface | Ensure Ollama is bound to `0.0.0.0` (not just `127.0.0.1`). Check with `OLLAMA_HOST=0.0.0.0 ollama serve` or Ollama app settings. |
| Open WebUI doesn't detect embedding model | Manually configure embedding model in Open WebUI Admin > Settings > Documents > Embedding Model |
| Port 3000 already in use on Mac Mini | Change port mapping in docker-compose.yml (e.g., `3001:8080`) |

---

## 7. Out of Scope

- User authentication (single-user setup for now)
- TLS/HTTPS (local network only)
- Ollama installation or model pulling (already done)
- Actual Community Brain content import (that's Sub-project 1+)

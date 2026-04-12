# Community Brain SP0: Open WebUI + Ollama Setup — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up Open WebUI on the Mac Mini (10.1.50.219) connected to the existing Ollama instance, and verify end-to-end RAG knowledge import works.

**Architecture:** Single Docker container (Open WebUI) connecting to the native Ollama already running on the Mac Mini. No custom code — just infrastructure config, a test fixture, and documentation.

**Tech Stack:** Docker Compose, Open WebUI (`ghcr.io/open-webui/open-webui:main`), Ollama (existing), Gemma 4 E4B, nomic-embed-text

**Spec:** `docs/superpowers/specs/2026-04-12-community-brain-sp0-openwebui-setup.md`

---

## File Map

| Action | Path | Responsibility |
|--------|------|---------------|
| Create | `community-brain/open-webui/docker-compose.yml` | Open WebUI container config |
| Create | `community-brain/open-webui/SETUP.md` | Step-by-step setup guide |
| Create | `community-brain/tests/fixtures/sample-session.md` | Test document for RAG verification |

---

### Task 1: Create Directory Structure

**Files:**
- Create: `community-brain/open-webui/` (directory)
- Create: `community-brain/tests/fixtures/` (directory)

- [ ] **Step 1: Create the community-brain directory tree**

```bash
cd /home/pchouinard/n8n
mkdir -p community-brain/open-webui
mkdir -p community-brain/tests/fixtures
```

- [ ] **Step 2: Verify directories exist**

```bash
ls -la community-brain/
ls -la community-brain/open-webui/
ls -la community-brain/tests/fixtures/
```

Expected: Both directories exist and are empty.

- [ ] **Step 3: Commit scaffold**

```bash
git add community-brain/
git commit -m "scaffold: create community-brain directory structure for SP0"
```

Note: Git doesn't track empty directories. If the commit has nothing to add, skip this step — the directories will be committed alongside their first files in subsequent tasks.

---

### Task 2: Create Docker Compose File

**Files:**
- Create: `community-brain/open-webui/docker-compose.yml`

- [ ] **Step 1: Write the Docker Compose file**

Create `community-brain/open-webui/docker-compose.yml` with this exact content:

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

Key details:
- Open WebUI listens on port 8080 internally, mapped to 3000 on the host.
- `OLLAMA_BASE_URL` points to the host's Ollama via Docker's `host.docker.internal` alias.
- `extra_hosts` ensures `host.docker.internal` resolves on macOS Docker Desktop (it's usually automatic, but explicit is safer).
- `WEBUI_AUTH=false` disables login — this is a single-user setup on a private network (10.1.50.x).
- Named volume `open-webui-data` persists knowledge bases, chat history, and config across container restarts.

- [ ] **Step 2: Validate the YAML syntax**

```bash
cd /home/pchouinard/n8n/community-brain/open-webui
docker compose config
```

Expected: Parsed YAML output showing the resolved service config. No errors.

If `docker compose` is not available on the VM (Docker is on the Mac Mini), validate with:

```bash
python3 -c "import yaml; yaml.safe_load(open('community-brain/open-webui/docker-compose.yml'))" && echo "YAML valid"
```

- [ ] **Step 3: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/open-webui/docker-compose.yml
git commit -m "feat(sp0): add Open WebUI Docker Compose config

Connects to existing Ollama on Mac Mini via host.docker.internal.
Auth disabled for single-user local network setup."
```

---

### Task 3: Create Test Fixture

**Files:**
- Create: `community-brain/tests/fixtures/sample-session.md`

- [ ] **Step 1: Write the test fixture file**

Create `community-brain/tests/fixtures/sample-session.md` with this exact content:

```markdown
---
session_date: "2025-01-15"
session_title: "RAG Architectures Deep Dive"
content_tier: "historical"
speakers: ["Patrick Chouinard", "Alice Chen", "Bob Martinez", "Carol Singh"]
chunk_count: 3
---

## Session: RAG Architectures Deep Dive | Date: 2025-01-15

### Chunk 1 of 3

[00:05:12] Patrick Chouinard: Today we're diving into RAG architectures. I've been experimenting with three different approaches over the past month and want to share what I found. The first approach uses LangChain with FAISS as the vector store. It's the fastest to prototype but has some limitations at scale.

[00:06:45] Alice Chen: I've been using the same LangChain plus FAISS combo. One thing I noticed is that for collections under 100,000 documents, FAISS performs really well. The main bottleneck isn't retrieval speed — it's the chunking strategy. I switched from fixed-size chunks to semantic chunking and saw a 40% improvement in retrieval relevance.

[00:08:30] Bob Martinez: What embedding model are you using with that, Alice? I tried OpenAI's text-embedding-3-large and nomic-embed-text. The nomic model is surprisingly good for a local model, and it's free.

[00:09:15] Alice Chen: I'm using nomic-embed-text through Ollama. The quality is close enough to OpenAI's offering that the cost savings make it a no-brainer for development. I only switch to text-embedding-3-large for production deployments where clients need the absolute best retrieval quality.

---

### Chunk 2 of 3

[00:15:22] Carol Singh: I want to share something different. I've been building a RAG system for legal documents, and the standard chunking approaches don't work well. Legal text has very specific structural requirements — you can't split a clause across chunks or you lose the legal meaning.

[00:17:01] Patrick Chouinard: That's a great point about domain-specific chunking. What did you end up doing?

[00:17:45] Carol Singh: I built a custom chunker that respects section boundaries in the legal documents. It uses the heading hierarchy — chapters, sections, subsections — as natural chunk boundaries. Each chunk also includes a breadcrumb trail showing where it sits in the document structure. The retrieval quality improved dramatically, about 65% better relevance scores.

[00:19:30] Bob Martinez: That breadcrumb idea is clever. I wonder if we could apply something similar to our call transcripts — using speaker transitions as natural boundaries instead of arbitrary token counts.

[00:20:15] Patrick Chouinard: That's exactly what I've been thinking about. Speaker-aware chunking for conversational content. Never split mid-speaker-turn, prefer breaking at topic transitions. We should prototype this.

---

### Chunk 3 of 3

[00:35:00] Patrick Chouinard: Let me summarize the key tools and recommendations from today. For vector stores: FAISS for prototyping, Pinecone or Weaviate for production scale. For embedding models: nomic-embed-text via Ollama for local development, text-embedding-3-large for production. For frameworks: LangChain is the most mature, but LlamaIndex has better document parsing.

[00:36:45] Alice Chen: One more tool to mention — I've been using Ragas for evaluating RAG pipeline quality. It gives you metrics like faithfulness, relevance, and context precision. Really helpful for comparing different chunking strategies objectively.

[00:37:30] Carol Singh: And for anyone working with legal or structured documents, I recommend looking at Unstructured.io. Their document parser handles PDFs, DOCX, and HTML with layout awareness. It's open source and works well as a pre-processing step before chunking.

[00:38:15] Bob Martinez: Great session everyone. My action item is to test speaker-aware chunking on a few of our past transcripts. I'll share results next week.

[00:38:45] Patrick Chouinard: Perfect. Next week we'll review Bob's chunking experiments and also look at hybrid search — combining BM25 keyword search with vector similarity. See everyone Tuesday.
```

This fixture contains specific, verifiable facts for RAG testing:
- Alice recommended FAISS for prototyping (Chunk 1)
- nomic-embed-text was discussed as a local embedding model (Chunk 1)
- Carol built a custom chunker for legal documents with 65% relevance improvement (Chunk 2)
- Ragas was recommended for evaluating RAG pipelines (Chunk 3)
- Unstructured.io was recommended for document parsing (Chunk 3)
- Bob's action item was to test speaker-aware chunking (Chunk 3)

These facts will be used as verification queries in Task 5.

- [ ] **Step 2: Verify file content**

```bash
wc -w community-brain/tests/fixtures/sample-session.md
```

Expected: ~550-650 words (approximately the size of a real chunked session file).

- [ ] **Step 3: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/tests/fixtures/sample-session.md
git commit -m "feat(sp0): add sample session fixture for RAG verification

Contains 3 chunks with specific queryable facts about RAG architectures,
embedding models, and chunking strategies. Used to verify Open WebUI
knowledge import and retrieval."
```

---

### Task 4: Create Setup Documentation

**Files:**
- Create: `community-brain/open-webui/SETUP.md`

- [ ] **Step 1: Write the setup guide**

Create `community-brain/open-webui/SETUP.md` with this exact content:

```markdown
# Open WebUI + Ollama Setup Guide

This guide sets up Open WebUI on a Mac Mini to query the Community Brain knowledge base.

## Prerequisites

- **Docker Desktop** installed and running on the Mac Mini
- **Ollama** installed and running natively on the Mac Mini
- Models pulled in Ollama:
  - `ollama pull gemma4:e4b` (query model)
  - `ollama pull nomic-embed-text` (embedding model)

Verify Ollama is running and accessible:

    curl http://localhost:11434/api/tags

You should see `gemma4:e4b` and `nomic-embed-text` in the response.

## 1. Start Open WebUI

From the `community-brain/open-webui/` directory:

    docker compose up -d

This pulls the Open WebUI image (first run only, ~1-2 GB) and starts the container.

Verify the container is running:

    docker compose ps

Expected: `open-webui` container with status `Up` and port `0.0.0.0:3000->8080/tcp`.

## 2. Access the UI

Open a browser and go to:

    http://<mac-mini-ip>:3000

On first launch, Open WebUI will ask you to create an admin account. Create one with any email/password (this is local only — auth is disabled for API access but the UI still requires an initial account).

## 3. Verify Ollama Connection

1. Go to **Settings** (gear icon, bottom left)
2. Navigate to **Admin Settings > Connections**
3. Confirm the Ollama URL is `http://host.docker.internal:11434`
4. Click the refresh icon — you should see available models listed

If models don't appear:
- Check that Ollama is running: `curl http://localhost:11434/api/tags`
- Try the direct IP instead: change Ollama URL to `http://10.1.50.219:11434`
- Ensure Ollama is bound to all interfaces (not just localhost)

## 4. Configure Embedding Model

1. Go to **Admin Settings > Documents**
2. Under **Embedding Model**, select `nomic-embed-text`
3. Set **Embedding Model Engine** to `Ollama`
4. Save

## 5. Test: Import a Document

1. Go to **Workspace** (left sidebar) > **Knowledge**
2. Click **+ New Knowledge**
3. Name it `Test` with description `RAG verification test`
4. Click into the new collection, then click **Add File**
5. Upload `tests/fixtures/sample-session.md`
6. Wait for processing to complete (status changes from processing to ready)

## 6. Test: Query the Document

1. Start a **New Chat**
2. Select **gemma4:e4b** as the model
3. Click the **+** button next to the message input and attach the `Test` knowledge collection (or type `#Test` in the message)
4. Ask: `What embedding model did Alice recommend for local development?`
5. Expected answer: Should reference `nomic-embed-text` from the uploaded document

Additional test queries:
- `What tool did Carol build for legal documents?` (expected: custom chunker with section boundaries)
- `What is Ragas used for?` (expected: evaluating RAG pipeline quality)
- `What was Bob's action item?` (expected: test speaker-aware chunking)

## 7. Cleanup

After verification, delete the `Test` knowledge collection:
1. Go to **Workspace > Knowledge**
2. Click the `Test` collection
3. Delete it

The Open WebUI setup is now complete and ready for Community Brain content import.

## Troubleshooting

**Open WebUI won't start:**
- Check Docker Desktop is running
- Check port 3000 is not already in use: `lsof -i :3000`
- View container logs: `docker compose logs open-webui`

**Can't connect to Ollama:**
- Verify Ollama is running: `curl http://localhost:11434/api/tags`
- Try direct IP: change OLLAMA_BASE_URL to `http://10.1.50.219:11434` in docker-compose.yml and restart
- Check Ollama is listening on all interfaces, not just localhost

**Document import fails:**
- Check container logs for errors: `docker compose logs open-webui`
- Verify the embedding model is configured in Admin Settings > Documents
- Try a smaller test file first (plain text, a few sentences)

**Query returns unrelated or no results:**
- Confirm the Knowledge collection is attached to the chat
- Check that the document status shows as fully processed (not still processing)
- Try a more specific query that uses exact phrases from the document
```

- [ ] **Step 2: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/open-webui/SETUP.md
git commit -m "docs(sp0): add Open WebUI setup guide

Step-by-step guide covering container startup, Ollama connection
verification, embedding model config, and RAG import testing."
```

---

### Task 5: Deploy and Verify on Mac Mini

This task is performed manually on the Mac Mini. It cannot be run from the VM.

**Files:**
- No file changes — this is infrastructure deployment and manual verification.

- [ ] **Step 1: Copy files to Mac Mini**

From the VM, sync the community-brain directory to the Mac Mini:

```bash
rsync -avz /home/pchouinard/n8n/community-brain/ pchouinard@10.1.50.219:~/community-brain/
```

Or if the n8n repo is cloned on the Mac Mini, pull the latest changes there.

- [ ] **Step 2: Start Open WebUI on Mac Mini**

On the Mac Mini:

```bash
cd ~/community-brain/open-webui
docker compose up -d
```

Wait for the image to pull (first run, ~1-2 GB). Then verify:

```bash
docker compose ps
```

Expected: `open-webui` container status `Up`, port `0.0.0.0:3000->8080/tcp`.

- [ ] **Step 3: Verify container health**

```bash
curl -s http://localhost:3000/health | head -c 200
```

Expected: A response (HTML or JSON) indicating the service is running. If no response, check logs:

```bash
docker compose logs open-webui --tail 50
```

- [ ] **Step 4: Complete initial setup in browser**

Open `http://10.1.50.219:3000` in a browser.

1. Create the initial admin account (any email/password — local only)
2. Go to **Admin Settings > Connections** — verify Ollama URL shows `http://host.docker.internal:11434`
3. Click refresh — confirm `gemma4:e4b` and `nomic-embed-text` appear as available models

If models don't appear, update the Ollama URL to `http://10.1.50.219:11434` and retry.

- [ ] **Step 5: Configure embedding model**

1. Go to **Admin Settings > Documents**
2. Set Embedding Model to `nomic-embed-text`
3. Set Embedding Model Engine to `Ollama`
4. Save

- [ ] **Step 6: Test chat (no RAG)**

1. Start a new chat, select `gemma4:e4b`
2. Send: `What is 2 + 2?`
3. Expected: A coherent response (confirms Ollama connection works for inference)

- [ ] **Step 7: Test RAG import**

1. Go to **Workspace > Knowledge > + New Knowledge**
2. Name: `Test`, Description: `RAG verification test`
3. Upload `~/community-brain/tests/fixtures/sample-session.md`
4. Wait for processing to complete

- [ ] **Step 8: Test RAG query**

1. Start a new chat with `gemma4:e4b`
2. Attach the `Test` knowledge collection
3. Ask: `What embedding model did Alice recommend for local development?`
4. Expected: Response mentions `nomic-embed-text` with context from the document
5. Ask: `What tool did Carol use for legal documents and what improvement did she see?`
6. Expected: Response mentions custom chunker with section boundaries, 65% relevance improvement
7. Ask: `What was Bob's action item from this session?`
8. Expected: Response mentions testing speaker-aware chunking on past transcripts

- [ ] **Step 9: Cleanup test collection**

1. Go to **Workspace > Knowledge**
2. Delete the `Test` collection

- [ ] **Step 10: Record results**

Note any deviations from expected behavior:
- Did `host.docker.internal` work or did you need the direct IP?
- Did the embedding model auto-detect or require manual configuration?
- Were RAG query results accurate?
- Any other issues?

If the Ollama URL needed changing, update `community-brain/open-webui/docker-compose.yml` to match what actually worked.

- [ ] **Step 11: Commit any adjustments**

If the docker-compose.yml or SETUP.md needed changes based on actual deployment:

```bash
cd /home/pchouinard/n8n
git add community-brain/open-webui/
git commit -m "fix(sp0): adjust Open WebUI config based on deployment testing

[describe what changed and why]"
```

---

## Verification Summary

Sub-project 0 is complete when all of these are confirmed:

| Check | Status |
|-------|--------|
| Open WebUI container running on Mac Mini port 3000 | |
| Ollama connection verified (models visible) | |
| Embedding model set to nomic-embed-text | |
| Basic chat works with Gemma 4 E4B | |
| Sample session imported to Knowledge without errors | |
| RAG queries return correct, document-grounded answers | |
| Test collection cleaned up | |
| Any config adjustments committed | |

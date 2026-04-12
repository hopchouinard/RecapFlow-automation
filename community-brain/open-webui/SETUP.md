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

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A self-hosted **n8n** deployment using Docker Compose. This is NOT the n8n source code monorepo — it runs the official `n8nio/n8n:latest` Docker image with PostgreSQL as the database backend.

n8n is a workflow automation tool (similar to Zapier/Make) with a visual editor accessible at port 5678.

## Repository Structure

- `docker-compose.yml` — Orchestrates n8n + PostgreSQL containers
- `docker/Dockerfile` — Extends official n8n image (rarely needs changes)
- `.env` — Environment variables (DB credentials, auth, encryption key) — **contains secrets**
- `data/` — Persistent volume mounted at `/home/node/.n8n` inside the container
- `watch/` — Incoming files for workflow processing (mounted at `/home/node/watch` in container)
- `output/` — Workflow output files organized by date (mounted at `/home/node/output` in container)
- `workflows/` — Workflow JSON definitions for import into n8n
- `scripts/` — Mac-side sync scripts and launchd/Automator configs
- `docs/plans/` — Design and implementation plan documents

## Common Commands

```bash
# Start services (use v2 syntax — legacy docker-compose v1 is incompatible)
docker compose up -d

# View logs
docker compose logs -f n8n

# Stop services
docker compose down

# Upgrade n8n (pulls latest image, n8n auto-migrates the DB)
docker compose pull && docker compose up -d

# Import a workflow
docker cp workflows/my-workflow.json n8n:/tmp/workflow.json
docker exec n8n n8n import:workflow --input=/tmp/workflow.json

# Export all workflows
docker exec n8n n8n export:workflow --all
```

## Architecture

```
Mac Mini (~/Documents/Zoom/)
    → Automator Folder Action
    → rsync to VM

[VM: n8n-automation.patchoutech.lab]
    ./watch/ ──→ [n8n container :5678] ──→ [PostgreSQL container (n8n_db)]
                       |
                 ./data volume
                 ./output volume (workflow results)
```

- **n8n container**: runs the n8n server in production mode
- **PostgreSQL container** (`n8n_db`): stores workflows, credentials, and execution data; data persisted in Docker volume `db_data`; pinned to **postgres:17** to match existing data
- **`./data`**: mounted volume for n8n file storage (binary data, git integration, SSH keys)
- **`./watch`**: incoming files for workflow triggers (mapped to `/home/node/watch`)
- **`./output`**: workflow output files (mapped to `/home/node/output`)

## Environment Configuration

All config lives in `.env` and `docker-compose.yml`. Key variables:

| Variable | Purpose |
|----------|---------|
| `N8N_PORT` | Port n8n listens on (5678) |
| `N8N_ENCRYPTION_KEY` | Encrypts stored credentials — **NEVER change after setup** |
| `DB_TYPE`, `DB_POSTGRESDB_*` | PostgreSQL connection settings |
| `N8N_SECURE_COOKIE=false` | Required for HTTP access (no TLS) |
| `NODES_EXCLUDE=[]` | Re-enables hidden nodes (e.g., Local File Trigger, disabled since n8n 2.0) |
| `NODE_FUNCTION_ALLOW_BUILTIN=fs,path` | Allows Code nodes to use `require('fs')` and `require('path')` |

## Workflows

### Merged Call Summarizer (`workflows/merged-call-summarizer.json`) — Active

Watches `./watch/` for Zoom chat logs and Fathom transcripts. Uses a **rendezvous pattern**: whichever file arrives second detects the partner file and triggers the pipeline. Runs a 4-step LLM prompt chain via OpenRouter (Claude Sonnet 4.6), saves outputs to `./output/<date>/`:

```
Local File Trigger → Validate & Check Partner → Merge Content → Create Output Folder
    → Save transcript.txt
    → LLM: Extract Signal → Save extracted-signal.md
    → LLM: Community Post → Save community-post.md
    → LLM: Compress Post → Save community-post-compressed.md
    → Calculate Next Tuesday → LLM: Weekly Invite → Save YYYY-MM-DD-weekly-invite.md
```

**Input files** (both required, matched by `YYYY-MM-DD` prefix):
- `YYYY-MM-DD-zoom-chat.txt` — from Mac-side rsync
- `YYYY-MM-DD-transcript.txt` — from Fathom poller or manual fetch

**Output files** (`./output/YYYY-MM-DD/`):
- `transcript.txt` — formatted raw transcript
- `extracted-signal.md` — signal extracted from merged content
- `community-post.md` — polished community post
- `community-post-compressed.md` — compressed version for Skool
- `YYYY-MM-DD-weekly-invite.md` — next week's call invite (dated for next Tuesday)

Each LLM step uses a **Basic LLM Chain** node connected to an **OpenRouter Chat Model** sub-node. Credentials (OpenRouter API key, Fathom API key) are configured in the n8n UI.

### Fathom Transcript Poller (`workflows/fathom-transcript-poller.json`)

Polls the Fathom API every 15 minutes for new meeting recordings. Fetches transcripts, formats them as plain text, saves to `./watch/`. If a matching chat log already exists, triggers the Merged Call Summarizer via Execute Workflow node.

Stores last poll timestamp in `/home/node/.n8n/fathom-last-poll.txt`.

### Fathom Manual Lookup (two workflows, for testing)

- **Fathom: List Recordings** (`workflows/fathom-list-recordings.json`) — Manual trigger with a configurable date. Lists all Fathom recordings for that date with recording_id, title, duration.
- **Fathom: Fetch Transcript** (`workflows/fathom-fetch-transcript.json`) — Manual trigger with a configurable recording_id and date. Fetches the transcript and saves to `./watch/`.

Usage: Run List Recordings to find the recording_id, then run Fetch Transcript with that ID.

### Zoom Chat Summarizer (`workflows/zoom-chat-summarizer.json`) — Inactive (replaced)

Original chat-only summarizer. Kept for reference but replaced by the Merged Call Summarizer.

### Mac-Side File Sync

Files flow from Mac Mini to the VM automatically:

1. Zoom saves chat to `~/Documents/Zoom/<date> <time> <meeting>/`
2. **Automator Folder Action** on `~/Documents/Zoom/` triggers `scripts/sync-zoom-chats.sh`
3. Script extracts date from folder name, renames to `YYYY-MM-DD-zoom-chat.txt`, rsyncs to VM's `./watch/`
4. n8n Local File Trigger picks up the new file

Key files on Mac:
- `~/scripts/sync-zoom-chats.sh` — the sync script
- `~/Library/Workflows/Applications/Folder Actions/Sync Zoom Chats.workflow` — Automator action
- `~/.zoom-chat-synced` — tracks processed files (clear to reprocess)
- `~/.zoom-chat-sync.log` — sync log for debugging

## Important Notes

- **Use `docker compose` (v2)** — not `docker-compose` (v1). The legacy v1.29.2 is incompatible with newer Docker images.
- **Postgres is pinned to v17** — `postgres:latest` upgraded to v18 which changed the data directory layout and breaks existing volumes.
- **Local File Trigger** is disabled by default in n8n 2.0+ — `NODES_EXCLUDE=[]` re-enables it.
- **Code nodes** cannot use `require()` by default — `NODE_FUNCTION_ALLOW_BUILTIN` whitelist is required.
- **SSH key auth** must be set up between Mac and VM for rsync. Key passphrase stored in macOS Keychain via `ssh-add --apple-use-keychain`.

## Critical Warnings

- **NEVER** delete or modify `data/config` — contains the encryption key for all stored credentials
- **NEVER** change `N8N_ENCRYPTION_KEY` after credentials have been saved in n8n
- The `data/` directory must be preserved and backed up — it contains runtime state
- `.env` contains plaintext secrets — do not commit to public repositories

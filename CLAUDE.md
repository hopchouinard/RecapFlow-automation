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

**Plan B (2026-04-19) extension:** the workflow now has a sequential branch appended after the Weekly Invite step that fetches the speaker-aliases block from the retrieval server, runs a prep-prompt LLM call to produce `prepared-transcript.md`, and POSTs all three artifact paths (`prepared_transcript`, `extracted_signal`, `community_post`) to the retrieval server's `/ingest` endpoint. On `/ingest` failure the workflow logs to `./output/<date>/ingest-error.log` and still reports success — markdown artifacts always hit disk regardless of ingestion outcome.

### Transcript-Only Summarizer (`workflows/transcript-only-summarizer.json`) — Backfill

Manual trigger. Iterates `./historical/<folder>/` session directories, reads `transcript.md` + `meta.json` per session, runs 3 LLM calls (prep-prompt, Extract Signal with canonical headings, transcript-only Community Post), writes 3 artifacts to `./output/<session_id>/`, then POSTs to `/ingest` on the retrieval server. State tracked in `./n8n-state/backfill-state.json`: `completed` entries are skipped on re-trigger, `failed` entries retry on next run.

Used for the one-time historical backfill (~3 min per session under Sonnet+Sonnet+Kimi prompt mix; 30s inter-session delay). Resume-safe — kill the run anytime, restart, picks up where it left off.

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

---

## Project modules — more than just n8n

This repo is a multi-module project. Everything above describes the n8n orchestration layer. There is also a separate Python service under `community-brain/` — a standalone vector-search retrieval server that consumes n8n's output:

| Module | What | Where its docs live |
|---|---|---|
| n8n orchestration | Workflow engine running in Docker (covered above) | This file (root `CLAUDE.md`) |
| `community-brain/` | Python retrieval server: ingests coaching-call artifacts, embeds to LanceDB, serves `/query` + `/ingest` + `/sessions` over FastAPI (port 8999) | `community-brain/CLAUDE.md` — load this when working inside that subfolder |

**When someone says "deploy the retrieval server" or "deploy community-brain":** follow `community-brain/docs/DEPLOYMENT.md` end-to-end. It's a full SSH-driven runbook with a permission model (🟢 auto / 🟡 confirm / 🔴 gated) that Claude must respect when acting as operator. The sub-CLAUDE.md at `community-brain/CLAUDE.md` explains the architecture, trust model, testing conventions, and known v2 backlog.

The two modules interact at the filesystem boundary: n8n writes artifacts to `./output/<YYYY-MM-DD>/`, and the retrieval-server container mounts that directory read-only as `/data/output/`. Plan B will wire n8n workflows to POST to the retrieval server's `/ingest` endpoint after producing artifacts.

## Current status (as of 2026-04-28)

**Plan A — COMPLETE and DEPLOYED.** Retrieval server live on the n8n VM at `http://10.1.30.10:8999` (LAN-reachable). 37-field LanceDB v1.0 schema, trust-partitioned `/query`.

**Plan B — COMPLETE.** Both n8n workflows wired to the retrieval server:
- Workflow 1 (Merged Call Summarizer, n8n id 5): live weekly with prep-prompt + `/ingest` POST appended
- Workflow 2 (Transcript-Only Summarizer, n8n id 6): backfill workflow with state file + resume
- 8 sessions in LanceDB (~167 chunks): 6 consecutive Feb 2025 + `2026-04-14` + `2026-04-21`

**Phase 6 — PARTIAL VALIDATION COMPLETE.** 5 query types from spec §10 tested against the 8-session subset. 3 pass cleanly, 2 had retrieval-layer caveats (Findings 6 and 7) — both addressed in Hybrid Retrieval v2 below.

**Hybrid Retrieval v2 — COMPLETE and DEPLOYED.** `/query` ranking is now hybrid (vector + BM25 RRF, k=60) with cue-driven metadata-aware boosting, oversampled 3×, vector-only graceful fallback. Legacy v0 helpers + `_v2` suffix archaeology removed. Server bumped to `0.2.0`. 302 tests passing on main. Live-VM validation on 2026-04-28 confirmed Findings 6 and 7 empirically resolved (entity-grounded queries went from 0/10 → 6/10 Adam-containing chunks; metadata-tagged queries went from 1/10 → 6/10 `has_unresolved_question=True` chunks). Validation surfaced **Finding 8** — answering LLM under-utilizes Stage C metadata flags because the trust contract correctly tells it to re-derive — queued as a v3 candidate. See Plan A spec §10 for the full validation addendum.

**Hybrid Retrieval v3 + Stage C v2 — IN PROGRESS (feature branch).** Closes every Bucket-1 audit gap before Plan C: `entities` populated, `speakers_mentioned` populated, `keywords` uniform across content types, `speakers_spoke` canonicalized via three CLIs (propose / apply / recanonicalize). Synthesized `bm25_text` FTS column, score_breakdown + metadata_summary in /query, YAML cue rules with hot-reload, `recurrent` corpus marker via lint_corpus. F8 narrow fix via filter-side `[flags:]` and `[corpus summary:]` tags structurally separated from transcript content. 425 tests pass on `feat/retrieval-v3-stage-c-v2`. Awaiting deploy + 9-session re-extract + 8-criteria validation gate before Plan C kickoff. See `docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md` and `docs/superpowers/plans/2026-04-29-retrieval-v3-and-stage-c-v2-plan.md`.

**What's still open — one operational track:**
- **Track B:** Plan C — full backfill across remaining ~57 of 65 historical sessions (~12 hr overnight run, ~$3 cost). Operator decision: hold until v3 retrieval design lands so the corpus isn't reprocessed twice.

**👉 START HERE in any new session:** [`docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`](docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md).

**Canonical references:**
- **Handoff doc (read first):** `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`
- Plan A spec: `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md` (§10 Phase 6 has the validation findings catalog; Findings 6 and 7 cross-reference v2)
- Plan A plan: `docs/superpowers/plans/2026-04-18-community-brain-ingestion-plan-a.md`
- Plan B spec: `docs/superpowers/specs/2026-04-19-plan-b-n8n-ingestion-integration-design.md`
- Plan B plan: `docs/superpowers/plans/2026-04-19-plan-b-n8n-ingestion-integration-plan.md`
- v2 spec: `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`
- v2 plan: `docs/superpowers/plans/2026-04-27-hybrid-retrieval-v2-plan.md`
- Trust contract: `docs/inference-guidelines.md`
- Schema evolution rules: `docs/migrations/CHANGELOG.md`

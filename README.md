# n8n Automation Stack

This repository runs a self-hosted n8n instance with PostgreSQL using Docker Compose. It is focused on automating post-call content generation from Zoom chat logs and Fathom transcripts.

The primary workflow watches for two files that share the same `YYYY-MM-DD` prefix:

- `YYYY-MM-DD-zoom-chat.txt`
- `YYYY-MM-DD-transcript.txt`

When both files are present, n8n merges them and generates a transcript artifact, extracted signal notes, a community post, a compressed community post, and a dated weekly invite.

## What This Repository Contains

- Docker Compose deployment for n8n and PostgreSQL
- Persistent n8n state under `data/`
- File-based workflow inputs under `watch/`
- Generated outputs under `output/`
- Importable workflow JSON definitions under `workflows/`
- Mac-side Zoom chat sync script under `scripts/`
- Design and reference documentation under `docs/`

This is not the n8n source code monorepo. It runs the official `n8nio/n8n:latest` container image.

## Project Structure

```text
n8n/
├── .env
├── docker-compose.yml
├── docker/
│   └── Dockerfile
├── data/
├── docs/
│   ├── plans/
│   └── reference-architecture/
├── output/
├── scripts/
│   ├── com.patchoutech.sync-zoom-chats.plist
│   └── sync-zoom-chats.sh
├── watch/
└── workflows/
    ├── fathom-fetch-transcript.json
    ├── fathom-list-recordings.json
    ├── fathom-transcript-poller.json
    ├── merged-call-summarizer.json
    └── zoom-chat-summarizer.json
```

## Services

`docker-compose.yml` starts two containers:

- `n8n` using `n8nio/n8n:latest`
- `n8n_db` using `postgres:17`

The n8n container exposes port `5678` and mounts these folders:

- `./data` -> `/home/node/.n8n`
- `./watch` -> `/home/node/watch`
- `./output` -> `/home/node/output`

## Prerequisites

- Docker with Compose v2 available as `docker compose`
- Network access for n8n to reach any external APIs used by your workflows
- Valid credentials configured in n8n for any active integrations such as OpenRouter or Fathom

## Start And Stop

Start the stack:

```bash
docker compose up -d
```

View logs:

```bash
docker compose logs -f n8n
docker compose logs -f db
```

Stop the stack:

```bash
docker compose down
```

Open n8n in a browser:

```text
http://localhost:5678
```

## Current Runtime Configuration

The active compose file currently configures:

- PostgreSQL as the n8n database backend
- Basic auth enabled for the n8n UI
- `N8N_SECURE_COOKIE=false` for HTTP access without TLS
- `NODES_EXCLUDE=[]` so file-based nodes remain available
- `NODE_FUNCTION_ALLOW_BUILTIN=fs,path` for Code nodes that need those built-ins

Review `docker-compose.yml` and `.env` before exposing this instance outside a trusted network.

## Workflow Overview

### Merged Call Summarizer

`workflows/merged-call-summarizer.json` is the main workflow.

It waits for matching chat and transcript files in `watch/`, merges them, and writes results to `output/<date>/`.

Typical outputs:

- `transcript.txt`
- `extracted-signal.md`
- `community-post.md`
- `community-post-compressed.md`
- `YYYY-MM-DD-weekly-invite.md`

### Fathom Transcript Poller

`workflows/fathom-transcript-poller.json` polls Fathom for new recordings and saves transcript files into `watch/`. If the matching Zoom chat file already exists, it can trigger the summarizer flow.

### Fathom Manual Lookup

These workflows are useful for testing and backfills:

- `workflows/fathom-list-recordings.json`
- `workflows/fathom-fetch-transcript.json`

### Legacy Workflow

`workflows/zoom-chat-summarizer.json` is the earlier chat-only summarizer and is kept for reference.

## Import And Export Workflows

Import a workflow file into the running container:

```bash
docker cp workflows/merged-call-summarizer.json n8n:/tmp/workflow.json
docker exec n8n n8n import:workflow --input=/tmp/workflow.json
```

Export all workflows:

```bash
docker exec n8n n8n export:workflow --all
```

## Input And Output Conventions

Expected input files in `watch/`:

- `YYYY-MM-DD-zoom-chat.txt`
- `YYYY-MM-DD-transcript.txt`

Generated files are written to `output/YYYY-MM-DD/`.

Matching is date-based, so file names must keep the expected prefix format.

## Zoom Chat Sync Script

`scripts/sync-zoom-chats.sh` is intended to run on a Mac via an Automator Folder Action. It:

- watches for newly created Zoom meeting folders
- extracts the date from the folder name
- renames the chat file to `YYYY-MM-DD-zoom-chat.txt`
- rsyncs the file to the VM's `watch/` directory

The script tracks synced files in `~/.zoom-chat-synced` and logs activity to `~/.zoom-chat-sync.log`.

## Notes On The Dockerfile

`docker/Dockerfile` extends the official n8n image, but the current `docker-compose.yml` uses the upstream image directly rather than building from this Dockerfile. If you need custom packages or image-level changes, update compose to build from `docker/`.

## Documentation

Repository docs are organized in two sections:

- `docs/plans/` for implementation plans and change records
- `docs/reference-architecture/` for the end-to-end system design and operations reference

Start with `docs/reference-architecture/index.md` for the full architecture narrative.

## Operational Warnings

- Do not switch from `docker compose` to legacy `docker-compose` commands unless you have verified your environment supports it
- Keep PostgreSQL pinned to `postgres:17` unless you have a migration plan for the existing volume
- Do not delete or replace the contents of `data/` without a backup
- Treat `.env` and anything under `data/` as sensitive runtime material

## Useful Commands

Restart the stack after changes:

```bash
docker compose down
docker compose up -d
```

Pull a newer n8n image and restart:

```bash
docker compose pull
docker compose up -d
```

Inspect container status:

```bash
docker compose ps
```

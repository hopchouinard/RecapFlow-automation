# CLAUDE.md

## Legacy VM is recovery-only; OpenWebUI must migrate (2026-09-20)

Patrick explicitly confirmed that OpenWebUI is included in migration off
`n8n-automation`. That VM is retained only as a temporary functionality/recovery
backup pending retirement; it must not remain a required production consumer,
credential-renewal target, scheduler dependency or serving component. Preserve
its recovery state. Validate the replacement OpenWebUI and its integrations on
VM108, then migrate through the controlled production rollout and remove legacy
production dependencies. Do not restart or update the dormant stack merely to
make production renewal pass. Historical instructions to retain live OpenWebUI
there temporarily are superseded. Retirement itself still requires its evidence.

## Mandatory development-first validation (2026-09-20)

Patrick accepted the [current assessment and continuation plan](docs/migrations/cbm-current-state-and-continuation.md)
with this standing requirement for all subsequent work:

- Develop in the canonical Forge checkout and validate every application or
  operational change on **community-brain-dev, PVE1 VM108**, before production.
  Local tests supplement this VM validation; they do not replace it.
- This includes preprocessing, processing, pipeline mechanics, evaluations,
  external-data acquisition/import used in tests, configuration, recovery,
  scheduling, identity-renewal mechanics and deployment changes.
- Reproduce production problems and test their fixes in development first.
  Use isolated development state and scoped identities; keep external test data
  private and preserve its provenance. Existing spending limits still apply.
- Promote only the tested source/image/configuration version to
  **community-brain-prod, PVE1 VM109**, with recorded development results and a
  rollback path. Any subsequent change must pass development validation again.
- Read-only production diagnosis and post-deployment verification are permitted;
  production is not a test environment. Historical development receipts do not
  validate a new change. This rule does not reopen unrelated stopped work.

## Development VM authorization (2026-09-09)

For development VM access, container deployment or rehearsal, read
[the ready VM handoff](docs/migrations/cbm-development-vm-handoff.md).
Patrick explicitly authorized Forge administration and disposable development
workloads on PVE1 VM 108. This supersedes older preparation-only restrictions
for that VM. Production deployment and cutover remain prohibited.


For read-only Proxmox or network inspection, including an empty SSH agent or
missing connector, read [Forge infrastructure access](docs/migrations/forge-infrastructure-access.md).
Use the installed `forge-infra-read` command; it requires no developer credentials.


## Forge development handoff (2026-09-09)

For development location, migration implementation, preservation evidence, or
production-change scope, read [the migration handoff](docs/migrations/forge-development-handoff.md)
before acting. It supersedes older VM-only development instructions below.
The canonical migration checkout is `/home/t3code/projects/RecapFlow-automation`
on Forge. This phase authorizes preservation, repository reconciliation, and
preparation only. Production deploy, cutover, secret rotation, and service
retirement require a separately authorized phase. Use `scripts/verify-forge.sh`
for the current credential-free development baseline.


This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A self-hosted **n8n** deployment using Docker Compose. This is NOT the n8n source code monorepo — it runs the official `n8nio/n8n:latest` Docker image with PostgreSQL as the database backend.

n8n is a workflow automation tool (similar to Zapier/Make) with a visual editor accessible at port 5678.

## Development model

Migration development now happens on Forge at
`/home/t3code/projects/RecapFlow-automation`, branch
`migration/community-brain-forge-handoff`. The existing n8n VM checkout remains
an unchanged production source reference. Its old instruction that all edits
and commits originate on that VM is superseded by the dated handoff above.

The Mac Mini still has an operational role as the Zoom host: after a call, chat logs are **manually** copied to the VM's `watch/` directory (see "Mac-Side File Copy" below). The previous Automator + rsync automation was retired as too fragile. `scripts/` contains the legacy sync script kept for reference; it isn't wired up.

## Repository Structure

- `docker-compose.yml` — Orchestrates n8n + PostgreSQL containers
- `docker/Dockerfile` — Extends official n8n image (rarely needs changes)
- `.env` — Environment variables (DB credentials, auth, encryption key) — **contains secrets**
- `data/` — Persistent volume mounted at `/home/node/.n8n` inside the container
- `watch/` — Incoming files for workflow processing (mounted at `/home/node/watch` in container)
- `output/` — Workflow output files organized by date (mounted at `/home/node/output` in container)
- `workflows/` — Workflow JSON definitions for import into n8n
- `scripts/` — legacy Mac-side sync scripts (no longer wired up; kept for reference)
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
    → manual copy to VM (scp / drag-and-drop)

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
- `YYYY-MM-DD-zoom-chat.txt` — manually copied from the Mac after the call
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

### Mac-Side File Copy (manual)

Zoom saves chat logs on the Mac Mini at `~/Documents/Zoom/<date> <time> <meeting>/`. The chat file is copied to the VM's `watch/` directory **manually** (drag-and-drop / scp / Finder) after the call, renamed to `YYYY-MM-DD-zoom-chat.txt`. n8n's Local File Trigger then picks it up.

The previous automated path (Automator Folder Action + rsync via `scripts/sync-zoom-chats.sh`) was retired — it was too fragile to justify versus a one-step manual copy once per weekly call. The script is still in `scripts/` for reference, but it isn't wired up.

## Important Notes

- **Use `docker compose` (v2)** — not `docker-compose` (v1). The legacy v1.29.2 is incompatible with newer Docker images.
- **Postgres is pinned to v17** — `postgres:latest` upgraded to v18 which changed the data directory layout and breaks existing volumes.
- **Local File Trigger** is disabled by default in n8n 2.0+ — `NODES_EXCLUDE=[]` re-enables it.
- **Code nodes** cannot use `require()` by default — `NODE_FUNCTION_ALLOW_BUILTIN` whitelist is required.

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

## Current status (as of 2026-04-30)

**Plan A — COMPLETE and DEPLOYED.** Retrieval server live on the n8n VM at `http://10.1.30.10:8999` (LAN-reachable). 37-field LanceDB v1.0 schema, trust-partitioned `/query`.

**Plan B — COMPLETE.** Both n8n workflows wired to the retrieval server:
- Workflow 1 (Merged Call Summarizer, n8n id 5): live weekly with prep-prompt + `/ingest` POST appended
- Workflow 2 (Transcript-Only Summarizer, n8n id 6): backfill workflow with state file + resume
- 8 sessions in LanceDB (~167 chunks): 6 consecutive Feb 2025 + `2026-04-14` + `2026-04-21`

**Phase 6 — PARTIAL VALIDATION COMPLETE.** 5 query types from spec §10 tested against the 8-session subset. 3 pass cleanly, 2 had retrieval-layer caveats (Findings 6 and 7) — both addressed in Hybrid Retrieval v2 below.

**Hybrid Retrieval v2 — COMPLETE and DEPLOYED.** `/query` ranking is now hybrid (vector + BM25 RRF, k=60) with cue-driven metadata-aware boosting, oversampled 3×, vector-only graceful fallback. Legacy v0 helpers + `_v2` suffix archaeology removed. Server bumped to `0.2.0`. 302 tests passing on main. Live-VM validation on 2026-04-28 confirmed Findings 6 and 7 empirically resolved (entity-grounded queries went from 0/10 → 6/10 Adam-containing chunks; metadata-tagged queries went from 1/10 → 6/10 `has_unresolved_question=True` chunks). Validation surfaced **Finding 8** — answering LLM under-utilizes Stage C metadata flags because the trust contract correctly tells it to re-derive — queued as a v3 candidate. See Plan A spec §10 for the full validation addendum.

**Hybrid Retrieval v3 + Stage C v2 — DEPLOYED (2026-04-30).** All 9 ingested sessions re-extracted under v1.1 schema with chunk-extraction-v2 prompt. Validation gate: 5/9 criteria passed cleanly, 2 manual checks pending (Open WebUI F8 cross-check + filter `[flags:]` rendering), 2 soft-misses on entity-in-top-10 and has_unresolved_question-in-top-10 (each off by 1 chunk; documented as v4 candidates). Track B (Plan C — backfill remaining ~57 sessions) now unblocked. See `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md` §10 v3 addendum for the full validation report.

**Tier B (retrieval-only distribution) — SHIPPED v1.0.0 (2026-05-26).** Public distribution repo at https://github.com/hopchouinard/community-brain-distribution. First corpus release tagged `v1.0.0` (71 sessions, 1499 chunks, 26 MB tar.gz). Retrieval-server image published to `ghcr.io/hopchouinard/community-brain-retrieval:1.0.0` (multi-arch amd64+arm64). Distribution repo tagged `tier-b-v1.0.0`. CI (`verify-on-pr.yml`) exercises a fixture-corpus smoke install on every PR and is green. Plan C backfill is also done as part of getting to v1.0.0 (corpus reflects 71 of 65+ historical sessions; the operator added a few more during ingestion). **v1.1.0 shipped 2026-09-01: corpus 85 sessions / 1833 chunks, image `1.1.0` (manifest list `sha256:ceb3b08d`), retrieval v5 (cue-driven candidate injection + citation guard); distribution repo tagged `tier-b-v1.1.0`.** That release also filled the Open WebUI image pin, which had shipped as the literal `PLACEHOLDER_OWUI_SHA` since v1.0.0 and made `docker compose up -d` fail for every self-host user — `verify-on-pr.yml` never caught it because it rewrites that line to `:main` before running compose.

**Chunked LLM pipeline — DEPLOYED (2026-09-03).** Both summarizer workflows now route every LLM step through a shared **`OpenRouter Call`** sub-workflow (n8n id `openrouterCall`) that calls the OpenRouter HTTP API directly, instead of Basic LLM Chain nodes. This exists because `chainLlm` emits only `{text}` — it discards `finish_reason` and treats an empty response as success, which is how the 2026-09-01 run wrote a 0-byte `community-post-compressed.md` and skipped `prepared-transcript.md` entirely while reporting success.

- **Chunked steps:** Prep-Prompt (map by transcript line), Extract Signal (map-reduce; the Zoom chat log goes only to the reduce), Community Post (map by semantic section, so section order is enforced by code rather than prompt discipline). Compress and Weekly Invite are not chunked — the reduce step's size budget bounds their input.
- **Two-level retry:** W3 makes up to 3 attempts per item, escalating `reasoning_effort` down and `maxTokens` up; the caller then re-splits into smaller chunks up to 2 halvings before throwing. Reasoning-token burn is non-deterministic (1 of 3 identical requests measured returning empty), so retrying works.
- **Models are configured per step in each workflow's `Code: Pipeline Config` node** — one visible place, no model slug anywhere else. `moonshotai/kimi-k2.5` is retired.
- **Tests:** 91 Code-node unit tests, run with `./scripts/test-workflows.sh` (no host Node.js needed — it shells into a throwaway `n8nio/n8n` container and reads node `jsCode` straight out of the committed workflow JSON, so the JSON stays the single source of truth and UI edits are never overwritten).

**⚠️ DEPLOYMENT REQUIREMENT — `OpenRouter Call` must stay ACTIVE.** n8n 2.36.8 refuses to execute a workflow whose Execute Workflow node targets an inactive sub-workflow (`getPublishedWorkflowData` throws "Workflow is not active and cannot be executed"), so deactivating it breaks BOTH summarizers at their first LLM step. It has no autonomous trigger, so being active costs nothing. **Re-importing `openrouter-call.json` silently deactivates it** — every redeploy must be followed by re-activation and an n8n restart.

**What's still open:**
- **Tier A (community-full)** — operator-only ingestion stack as a separable distribution. Separate spec needed.
- **Recipient-facing announcement** — Skool post linking to the v1.0.0 release. Not done in v1.0.0 ship; operator-driven.
- **DISTRIBUTION_REPO_TOKEN PAT** — intentionally NOT configured (Option B path). Each new image release requires a manual `docker-compose.yml` SHA bump + PR. Acceptable for low-frequency Tier B releases; revisit if cadence increases.

**👉 START HERE in any new session:** [`docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`](docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md).

**Canonical references:**
- **Handoff doc (read first):** `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`
- Plan A spec: `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md` (§10 Phase 6 has the validation findings catalog; Findings 6 and 7 cross-reference v2)
- Plan A plan: `docs/superpowers/plans/2026-04-18-community-brain-ingestion-plan-a.md`
- Plan B spec: `docs/superpowers/specs/2026-04-19-plan-b-n8n-ingestion-integration-design.md`
- Plan B plan: `docs/superpowers/plans/2026-04-19-plan-b-n8n-ingestion-integration-plan.md`
- v2 spec: `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`
- v2 plan: `docs/superpowers/plans/2026-04-27-hybrid-retrieval-v2-plan.md`
- v3 spec: `docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md`
- v3 plan: `docs/superpowers/plans/2026-04-29-retrieval-v3-and-stage-c-v2-plan.md`
- Trust contract: `docs/inference-guidelines.md`
- Schema evolution rules: `docs/migrations/CHANGELOG.md`

<!-- BEGIN patchou-bootstrap: managed block, edits are overwritten by `patchou-bootstrap sync` -->

## Technology standard

This project follows the Patchou personal technology standard.

- **Before introducing any** framework, library, database, host, auth provider,
  message bus, scheduler, test tool, or dependency — load the `tech-stack` skill
  (`.agents/skills/tech-stack/SKILL.md`).
- **Record in [`STACK-DECISIONS.md`](STACK-DECISIONS.md)**: this project's profile,
  every Deferred family it resolves, and every exception it takes. Nothing is
  decided silently.
- The standard is *preferred*, not absolute. An exception needs a concrete,
  expressible, describable reason. "Simpler for now" and expected future growth
  are not reasons.

<!-- END patchou-bootstrap -->

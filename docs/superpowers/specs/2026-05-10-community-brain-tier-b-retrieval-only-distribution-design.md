# Community Brain — Tier B (Retrieval-Only) Distribution Design

**Date:** 2026-05-10
**Author:** pchouinard (with Claude Opus 4.7)
**Status:** Design — pending implementation plan
**Supersedes:** N/A
**Related:**
- Brainstorming brief: `docs/superpowers/community-tiers-brainstorming-brief.md`
- Operator-tier spec: `docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md`
- community-brain package architecture: `community-brain/CLAUDE.md`
- Trust contract: `docs/inference-guidelines.md`
- Schema versioning: `docs/migrations/CHANGELOG.md`

---

## 1. Context and goals

### 1.1 What this is

A self-contained package that lets a community participant run the Community Brain retrieval experience on their own machine, over the operator's curated coaching-call corpus, with zero operator-side hosting.

This is **Tier B** in the two-tier distribution split called out by the operator-tier spec. Tier A (Community-Full — distribute the full ingestion pipeline so recipients can build their own corpus) is deferred to a separate spec.

### 1.2 Why this tier exists

The operator-tier work produced a two-node stack (VM + workstation) that delivers a chat experience over a curated corpus. The corpus is valuable to the community participants who were ON those calls — they get a searchable, queryable memory of conversations they attended. Shipping the retrieval layer to those participants converts the operator's daily-driver tool into a community gift, without dragging the full ingestion pipeline along.

The "retrieval-only" tier maintains the personal-vs-shareable boundary established in the operator-tier work: ingestion/cost-tracking/personal API keys stay operator-personal; the curated LanceDB + retrieval API + chat UX ship.

### 1.3 Audience and trust model

**Primary audience:** members of the operator's public community who participated in the coaching calls. Specific characteristics that drive design:

- They were on the calls — corpus content is not new information to them; the value is searchability, not discovery.
- They build AI-assisted applications — assume they have at least one of `{Claude Code, Codex, Cursor, Gemini CLI, Aider}` installed and functional.
- Mixed technical sophistication, but uniformly comfortable enough with AI coding tools to delegate setup work to an agent if given good instructions.
- Hardware: mixed (Mac with Apple Silicon, Windows with WSL2, Linux). Cannot assume 24 GB unified memory for local-LLM mode.

**Distribution access model: genuinely public.** Both the `community-brain-distribution` repo and the corpus blob are published as public GitHub artifacts. Anyone on the internet who follows the install runbook can download and run the stack. This is deliberate, not accidental:

- The community itself is open and public; content was generated in that context.
- Recipients of primary interest are community participants, but no technical gating prevents outside access.
- The operator accepts that copies will circulate beyond the original community.
- "Consent-by-attendance" describes the *moral* basis (participants knew the calls were being recorded for community use); the *distribution mechanism* makes no attempt to enforce a participant-only audience.

Implications:
- No invite system, no signed-URL gating on the corpus blob, no email-based access lists.
- The repo and blob URL appear in public documentation; anyone can fetch them.
- If the operator ever wants to walk this back (e.g., a participant withdraws consent retroactively), the design needs a v2 access-control story — but the v1 commitment is public-by-default.

### 1.4 Locked-in decisions (from brainstorming + spec review, 2026-05-10)

| Decision | Choice | Rationale |
|---|---|---|
| Corpus content | Full curated corpus, ships as-is | Public-community provenance; participants are primary audience |
| Distribution access | Public (no gating) | See §1.3 trust model; explicit choice |
| Hosting model | 100% recipient self-host | Preserves personal-state philosophy; bounds operator cost; no multi-tenant infra |
| UX shape | Open WebUI + filter + custom model; pluggable inference backend | Matches operator's daily UX; same package supports cloud-LLM and local-LLM modes |
| Platforms | macOS, Linux native; **Windows via WSL2 only** | Bash-shaped tooling; WSL2 is the supported Windows path |
| Install path | Single rigorous Markdown runbook (agent-agnostic) + human extras + verification harness | Audience-aware: AI assistants drive install for recipients who delegate; humans follow same doc by hand |
| Distribution channel | Public GitHub repo, sibling `community-brain-distribution` | Cooked-product repo separate from operator source |
| Build/release model | Pre-built Docker images on ghcr.io + corpus blob as GitHub Release asset | SHA-pinning discipline; free hosting; `git pull` updates |
| Authoritative version axis | **Distribution-repo tag is the single version recipients see** | Repo tag pins server image SHA + corpus SHA via committed files; image and corpus sub-tags are operator-internal release machinery |
| API surface (distribution mode) | `/health`, `/query`, `/sessions`, `/sessions/{id}`, `/speaker-aliases-block` | All read-only; `/ingest` and `/reindex` physically removed |
| Distribution-mode mechanism | **Runtime env var** (`COMMUNITY_BRAIN_DISTRIBUTION_MODE=true`) controls route registration | Simpler for v1; build-time variant deferred to v2 if threat materializes |
| Network binding | 127.0.0.1 only for all services | Localhost is the auth gate; no token theater |

---

## 2. Architecture overview

### 2.1 Two-repo split

```
┌──────────────────────────────────────────────────────────────┐
│  operator-repo (this repo, public)                           │
│  ─────────────────────────────────                           │
│  community-brain/                  ← Python source           │
│  docker-compose.yml                ← operator stack          │
│  workflows/, prompts/, docs/       ← operator artifacts      │
│  .github/workflows/                                          │
│    build-retrieval-image.yml       ← NEW (Flow A)            │
│    release-corpus.yml              ← NEW (Flow B helper)     │
│    sync-curated-files.yml          ← NEW (auto-PR cross-repo)│
└────────────────────────────┬─────────────────────────────────┘
                             │ on `tier-b-retrieval-vX.Y.Z` tag
                             │ or `corpus-vX.Y.Z` release event
                             ▼
┌──────────────────────────────────────────────────────────────┐
│  community-brain-distribution (NEW public repo)              │
│  ────────────────────────────                                │
│  README.md                    ← 30-second orientation        │
│  INSTALL.md                   ← Rigorous runbook             │
│  verify-install.sh            ← Verification harness         │
│  docker-compose.yml           ← SHA-pinned                   │
│  .env.example                 ← All overrides commented out  │
│  community_brain_filter.py    ← Auto-synced from operator    │
│  inference-guidelines.md      ← Auto-synced; for OWUI paste  │
│  download-corpus.sh           ← Fetches LanceDB from Release │
│  docs/                                                       │
│    screenshots/               ← OWUI walkthrough images      │
│    tour.md                    ← Loom link + intro            │
│    troubleshooting.md         ← Common errors + fixes        │
│  .github/workflows/                                          │
│    verify-on-pr.yml           ← Smoke install on PR          │
└────────────────────────────┬─────────────────────────────────┘
                             │ recipient: git clone, git pull
                             ▼
┌──────────────────────────────────────────────────────────────┐
│  Recipient machine                                           │
│  ─────────────────                                           │
│  Docker (Desktop or CE)                                      │
│  Ollama                                                      │
│    nomic-embed-text:v1.5  ← mandatory                        │
│    gpt-oss:20b            ← optional (local-LLM mode)        │
│  Compose stack:                                              │
│    retrieval-server  127.0.0.1:8999  (read-only)             │
│    open-webui        127.0.0.1:3000                          │
│  Corpus volume:                                              │
│    corpus/lancedb/  ← extracted from tarball, mounted RO     │
└──────────────────────────────────────────────────────────────┘
```

The operator repo remains the source of truth for code. The distribution repo is the cooked product, curated for recipients. Recipients never need to interact with the operator repo, but it's public — curious or auditing users can read it.

### 2.2 Trust model implications

| Surface | Gate | Operator-collected data |
|---|---|---|
| `/query`, `/sessions` | 127.0.0.1 binding | None |
| `/ingest`, `/reindex` | Routes physically removed in distribution-mode build | N/A (not present) |
| Open WebUI auth | First-user-becomes-admin; OWUI native | None |
| Corpus blob URL | Documented in public install runbook | N/A |
| Recipient inference keys | Stored in recipient's `.env`; never round-trip to operator | None |
| Recipient query logs | Stored in OWUI's local `webui.db`; never round-trip | None |

**Zero phone-home.** Operator never sees recipient queries, recipient inference keys, recipient install events, or recipient version information. Any future "check for updates" feature must remain pull-based (recipient hits GitHub's public API, not operator's server).

### 2.3 Distribution-mode build of retrieval-server

The retrieval-server image published to ghcr.io for Tier B has a single behavioral difference from the operator image: when `COMMUNITY_BRAIN_DISTRIBUTION_MODE=true` is set, the FastAPI app does NOT register the `/ingest` and `/reindex` routes at startup. This is enforced at the route-registration layer (not at request-time), so even an attacker who reverse-proxies the container to the public internet hits a 404 on write endpoints rather than a 401.

The operator image (used in operator-tier deployment) keeps the env var unset and registers all routes normally. Same source code, different runtime config.

**Routes present in distribution mode:**

| Route | Method | Purpose |
|---|---|---|
| `/health` | GET | Liveness + version metadata (extended in v1; see §4.2) |
| `/query` | POST | Hybrid retrieval over corpus (the main read endpoint) |
| `/sessions` | GET | List all sessions in the corpus (manifest verification) |
| `/sessions/{session_id}` | GET | Per-session detail |
| `/speaker-aliases-block` | GET | Read-only registry block (safe; harmless; useful for diagnostic tooling) |

**Routes removed in distribution mode:**

| Route | Method | Reason |
|---|---|---|
| `/ingest` | POST | Write endpoint; distribution is read-only |
| `/reindex` | POST | Write endpoint; distribution is read-only |

**Required implementation contract:** an automated test must assert that `app.routes` does not contain `/ingest` or `/reindex` when `COMMUNITY_BRAIN_DISTRIBUTION_MODE=true` is set, and that all five listed routes ARE present. The test runs in both operator-repo CI (against the operator image, with the env var set) and distribution-repo CI (against the published image).

---

## 3. Distribution repo contents

### 3.1 Files and purposes

| File | Source | Maintained by | Purpose |
|---|---|---|---|
| `README.md` | Hand-written | Operator (rare updates) | 30-second orientation; "what is this, where to start" |
| `INSTALL.md` | Hand-written | Operator (updated per release) | Rigorous step-by-step install runbook |
| `verify-install.sh` | Hand-written | Operator | Bash verification harness; idempotent per-step checks |
| `docker-compose.yml` | Hand-written, SHA-bumped by CI | Mixed (Flow A bumps SHAs; humans edit structure) | Stack definition with pinned image digests |
| `.env.example` | Hand-written | Operator (per release when keys change) | Configurable knobs, all overrides commented |
| `community_brain_filter.py` | Auto-synced from operator repo | CI (`sync-curated-files.yml`) | Open WebUI filter; uploaded to OWUI as single file |
| `inference-guidelines.md` | Auto-synced from operator repo | CI | System prompt to paste into OWUI custom model |
| `download-corpus.sh` | Hand-written | Operator (rare updates); CORPUS_VERSION bumped by Flow B | Fetches + verifies LanceDB tarball |
| `docs/screenshots/*` | Hand-captured | Operator (when UI changes) | OWUI walkthrough imagery |
| `docs/tour.md` | Hand-written | Operator (rare updates) | Loom video link, "what this is, how to use it" |
| `docs/troubleshooting.md` | Hand-written | Operator (grows over time) | Common errors + remediation |
| `.github/workflows/verify-on-pr.yml` | Hand-written | Operator (rare updates) | CI smoke-installs the repo's own files on a runner |

### 3.2 What's deliberately NOT in this repo

- Python source code (community-brain package). Recipients pull images by SHA; they don't build.
- n8n workflows, prompts, ingestion configs.
- Operator credentials or `.env` files with real values.
- Corpus blob as a checked-in file. Hosted as a Release asset; fetched on demand.
- Operator's `output/`, `historical/`, `data/` directories.
- Any operator-personal documentation, runbooks, or specs.

### 3.3 docker-compose.yml shape (sketch)

```yaml
services:
  retrieval-server:
    image: ghcr.io/<operator>/community-brain-retrieval@sha256:abc123...
    environment:
      OLLAMA_BASE_URL: ${OLLAMA_BASE_URL}
      COMMUNITY_BRAIN_EMBED_MODEL: ${COMMUNITY_BRAIN_EMBED_MODEL:-nomic-embed-text}
      COMMUNITY_BRAIN_DISTRIBUTION_MODE: "true"
      LANCEDB_PATH: /data/lancedb/nomic-v1
    volumes:
      # Corpus directory layout: ./corpus/lancedb/nomic-v1/chunks.lance/...
      # Mounts to /data so LANCEDB_PATH resolves to /data/lancedb/nomic-v1.
      # Read-only: server expects clean v3 corpus state; no startup writes needed.
      - ./corpus:/data:ro
    ports:
      - "127.0.0.1:8999:8999"
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped

  open-webui:
    image: ghcr.io/open-webui/open-webui@sha256:def456...   # vanilla OWUI, SHA-pinned
    environment:
      OLLAMA_BASE_URL: ${OLLAMA_BASE_URL}
      OPENAI_API_BASE_URL: ${OPENAI_API_BASE_URL:-}
      OPENAI_API_KEY: ${OPENAI_API_KEY:-}
      WEBUI_SECRET_KEY: ${WEBUI_SECRET_KEY}
    volumes:
      - open-webui-data:/app/backend/data
    ports:
      - "127.0.0.1:3000:8080"
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped

volumes:
  open-webui-data:
    external: false
```

Three design choices to note:

1. **`./corpus:/data:ro` is the only data mount.** The image already bundles its `config/` directory at `/app/config` via `Dockerfile:13` (cue rules, speaker aliases, chunking config). Mounting a host `./config` would mask the bundled curated config; we deliberately do not mount it. Release pipeline ensures the published image contains the operator's curated registries.
2. **`LANCEDB_PATH=/data/lancedb/nomic-v1`** matches the Dockerfile default and the on-disk layout inside the corpus tarball.
3. **`extra_hosts: host.docker.internal:host-gateway`** is required so containers reach the host's Ollama on all three platforms. We learned this the hard way during operator-tier work; documented in INSTALL.md troubleshooting.

---

## 4. Build and release pipeline

### 4.1 Three independent flows

Releases are not monolithic. Each of the following can be cut independently:

**Flow A: retrieval-server image** (operator-repo CI, triggered by tag)

1. Operator tags `tier-b-retrieval-vX.Y.Z` in operator repo.
2. `.github/workflows/build-retrieval-image.yml` builds the `community-brain` package into a Docker image with `COMMUNITY_BRAIN_DISTRIBUTION_MODE` defaulted on, pushes to `ghcr.io/<operator>/community-brain-retrieval:X.Y.Z` and as `@sha256:...`.
3. Same workflow opens a PR in `community-brain-distribution` updating the `retrieval-server` image SHA in `docker-compose.yml`. Operator reviews + merges.

**Flow B: corpus snapshot** (operator runs locally; CI helper)

1. Operator runs `scripts/release-corpus.sh` (a script in the operator repo) which performs the safe-snapshot sequence detailed in §5.4. The script never opens the live LanceDB with mutating methods; it filesystem-snapshots first, then compacts the copy.
2. Outputs of the script: `corpus-vX.Y.Z.tar.gz`, `sha256sum.txt`, `corpus-manifest.json`.
3. Operator runs `gh release create corpus-vX.Y.Z` in `community-brain-distribution`, attaching all three files.
4. Operator opens a PR in `community-brain-distribution` updating `download-corpus.sh`'s `CORPUS_VERSION` constant and `EXPECTED_SHA256`. Operator reviews + merges.

**Internal vs recipient-facing version axes:** the `tier-b-retrieval-vX.Y.Z` tag (operator repo) and `corpus-vX.Y.Z` Release (distribution repo) are operator-internal release machinery — recipients never look at them. The authoritative version recipients see is the `community-brain-distribution` repo tag (`tier-b-vMAJOR.MINOR.PATCH`), which pins both via committed files (`docker-compose.yml` image SHA pin + `download-corpus.sh` CORPUS_VERSION/SHA constants). One version axis surfaces to recipients; the rest is bookkeeping.

**Flow C: Open WebUI SHA bump** (operator, ad hoc)

1. When operator decides to bump OWUI (after testing the new version against the filter + alembic migrations), operator manually opens a PR in `community-brain-distribution` with the new SHA.
2. `verify-on-pr.yml` runs in the distribution repo CI: spins up the stack on `ubuntu-latest`, runs `verify-install.sh --post-install`. Catches alembic regressions before merge.

### 4.2 Schema-bump discipline and the extended `/health` endpoint

If a `retrieval-server` release ships a LanceDB schema change (i.e., the new image expects a schema version newer than the latest published corpus), the matching `corpus-vX.Y.Z` Release MUST be published first or simultaneously.

**Extended `/health` (new in v1):** rather than inventing a separate `/version` endpoint, v1 extends the existing `/health` route to return server and schema metadata:

```json
{
  "status": "ok",
  "server_version": "0.3.0",
  "schema_version": "v1.1",
  "embedding_model": "nomic-embed-text",
  "distribution_mode": true
}
```

Enforcement mechanisms:
- The corpus tarball's `corpus-manifest.json` declares the schema version + embedding model that produced it.
- `/health` exposes the server's expected schema version + active embedding model at runtime.
- `verify-install.sh` cross-checks `/health` against the manifest before letting the recipient declare the install green; mismatch surfaces a clear "your corpus is schema vN.X, your server expects vN.Y — fetch a newer corpus" message.

Operator-side: never tag a new retrieval-server release for distribution without confirming the corpus is consistent. The release-rehearsal step (§11) catches this if missed.

### 4.3 Cross-repo authentication

The operator-repo CI needs write access to `community-brain-distribution` to open PRs. Implementation:

- A fine-grained GitHub PAT scoped only to `community-brain-distribution` with `contents: write` and `pull-requests: write`.
- Stored as a secret in the operator repo's Actions settings (`DISTRIBUTION_REPO_TOKEN`).
- Workflows use `gh` CLI or `peter-evans/create-pull-request` action with the token.

GitHub App is cleaner long-term but heavier to set up; PAT is fine for v1.

---

## 5. Corpus distribution mechanics

### 5.1 Sizing reality

Measured on the VM as of 2026-05-10:

| Subdir | Size | What it is |
|---|---:|---|
| `chunks.lance/data/` | 905 MB | Current rows |
| `chunks.lance/_versions/` | 4.0 GB | MVCC history (every transaction since table creation) |
| `chunks.lance/_transactions/` | 127 MB | Transaction metadata |
| `chunks.lance/_deletions/` | 12 MB | Soft-delete tombstones |
| `chunks.lance/_indices/` | 100 KB | Vector index |
| **Total** | **5.0 GB** | 69 sessions, fully ingested (post-Plan-C) |

After `optimize_files()` + `cleanup_old_versions()`, expected output is ~1 GB. After `tar.gz`, expected ~600–900 MB.

### 5.2 Growth projection

- ~13 MB per session in `data/` (905 MB / 69 sessions)
- ~1 new session per week (weekly coaching call cadence)
- ~70 MB/year growth, compacted
- Crosses 2 GB compacted in ~14 years

GitHub Releases' 2 GB-per-file cap is comfortable for the foreseeable future.

### 5.3 Hosting decision: GitHub Releases on `community-brain-distribution`

Rationale:
- Today's corpus fits with significant headroom.
- Linear growth keeps it under the cap for >10 years.
- Free, integrated with version tagging, no third-party setup.
- Migration path to Cloudflare R2 (or B2, S3) is a one-line URL change in `download-corpus.sh` if ever needed.

### 5.4 Safe-snapshot compaction recipe

**Why compaction matters:**
1. **Privacy:** `_versions/` contains operator-personal ingestion history (timestamps, intermediate-state snapshots from schema migrations, force-reextract operations). Shipping it leaks operator operational history.
2. **Size hygiene:** 4 GB of history is dead weight for recipients who have no way to time-travel into it.
3. **Read-only mount safety (§5.6):** the published corpus must be in clean v3 state so server startup doesn't need to mutate anything. Compaction is what produces that clean state.

**Safe sequence — filesystem snapshot BEFORE any LanceDB call.** Earlier draft of this spec described a sequence that called `optimize_files()` and `cleanup_old_versions()` on the live database and claimed "prod is never modified." That was wrong — those methods mutate the table they're called on. Corrected recipe:

```bash
# scripts/release-corpus.sh — runs on the VM (or via SSH from operator workstation)

# Step 1: filesystem snapshot the live LanceDB to a fresh path.
#   This is read-only on the source — rsync/cp never opens LanceDB programmatically.
STAGING=/tmp/corpus-staging-vX.Y.Z
rm -rf "$STAGING"
mkdir -p "$STAGING/lancedb/nomic-v1"
rsync -a /home/<operator>/n8n/community-brain/lancedb/nomic-v1/ "$STAGING/lancedb/nomic-v1/"

# Step 2: compact the COPY. Source is never touched by lancedb code.
python3 - <<'PYEOF'
import lancedb
from datetime import timedelta
db = lancedb.connect("/tmp/corpus-staging-vX.Y.Z/lancedb/nomic-v1")
table = db.open_table("chunks")
table.optimize()                                            # compact_files()
table.cleanup_old_versions(older_than=timedelta(seconds=0)) # drop _versions/
PYEOF

# Step 3: assert clean v3 state on the compacted copy (no legacy v2 FTS index).
#   Reuses the existing community_brain.query.corpus_verify module.
python3 -m community_brain.cli.verify_corpus_clean_v3 "$STAGING/lancedb/nomic-v1"

# Step 4: tarball + hash + manifest.
cd /tmp
tar -czf corpus-vX.Y.Z.tar.gz -C corpus-staging-vX.Y.Z .
sha256sum corpus-vX.Y.Z.tar.gz > sha256sum.txt
python3 -m community_brain.cli.write_corpus_manifest \
    --staging "$STAGING" --out corpus-manifest.json --version vX.Y.Z
```

The live LanceDB directory is touched ONLY by rsync (which is a read of source bytes, not a LanceDB API call). All mutating LanceDB operations happen on the staging copy. The script verifies clean v3 state after compaction; if verification fails (e.g., a stray v2 FTS index survived), the release aborts before tarballing.

`scripts/release-corpus.sh` lives in the operator repo, not the `community-brain` Python package. The supporting CLIs (`verify_corpus_clean_v3`, `write_corpus_manifest`) are new entries in `community-brain/src/community_brain/cli/` and are part of the implementation scope.

### 5.5 Tarball format and integrity

- **Format:** `tar.gz` (boring, universal). Internal layout: `lancedb/nomic-v1/chunks.lance/...` (no top-level version-prefixed directory; the tarball extracts directly into `./corpus/`).
- **Hashing:** SHA-256 generated by `sha256sum`, published as `sha256sum.txt` alongside the tarball in the Release.
- **Manifest:** `corpus-manifest.json` declares `schema_version`, `embedding_model`, `session_count`, `chunk_count`, `generation_timestamp_utc`, `corpus_version`. Used by `verify-install.sh` to cross-check `/health` at startup.

`download-corpus.sh` behavior:
1. Reads `CORPUS_VERSION` and `EXPECTED_SHA256` constants from the top of itself (the script is the version anchor).
2. Fetches the tarball + sha256sum.txt + manifest.json from the corresponding GitHub Release.
3. Verifies SHA-256 against `EXPECTED_SHA256`. Refuses to extract on mismatch.
4. Extracts into `./corpus/`. Existing `./corpus/` is moved to `./corpus.previous/` before extraction (one rollback level kept).

### 5.6 Read-only mount precondition

The compose stack mounts `./corpus:/data:ro`. This is safe only if the published corpus is in clean v3 state:
- FTS index already built on `bm25_text` column (Stage C v2 / Retrieval v3)
- No legacy v2 FTS index on `full_text` column
- No partial transaction state
- Schema version matches the latest production schema

Server startup calls `verify_corpus_v3_state` (read-only) and `drop_full_text_index_if_present` (mutating but no-op on clean state). If the precondition holds, the mutating call has no work to do and the RO mount works. If the precondition is violated, the mutating call would error against an RO filesystem — but that error indicates a release-pipeline bug, not a recipient problem. The release-time `verify_corpus_clean_v3` CLI is the gate that prevents this.

---

## 6. Install runbook (`INSTALL.md`) structure

### 6.1 Design principles

- **Agent-agnostic Markdown.** No Claude-Code-specific slash commands, no Cursor-specific hooks. Works for {Claude Code, Codex, Cursor, Gemini CLI, Aider, no agent}.
- **Same doc for humans and agents.** Rigor that agents need is good for humans too. Agents read the doc directly; humans read it directly. The "agent path" is just "show this doc to your AI assistant and ask it to do the install."
- **Per-step structure:** prerequisites → literal commands → verification gate → remediation pointer.
- **Idempotent.** Re-running any step is safe.

### 6.2 Section structure

```
# Community Brain — Install Guide

## 0. Before You Start
   - Hardware: ≥8 GB RAM minimum; ≥24 GB unified memory if you plan local-LLM mode
   - Software prereqs: git, Docker (Desktop or CE), Ollama
   - **Windows users:** install Docker Desktop + WSL2 + Ubuntu, and run every command in this guide
     from an Ubuntu WSL2 shell. The distribution ships Bash-shaped tooling; native Windows
     (PowerShell, Git Bash) is unsupported in v1.
   - Pick your inference mode: local (gpt-oss:20b via Ollama) or cloud (OpenAI/OpenRouter/Anthropic/Gemini)
   - If you have an AI assistant (Claude Code / Codex / Cursor / Gemini CLI / Aider):
     give it this file and say "follow this install guide on my machine"

## 1. Install Docker + Ollama
   - macOS subsection: Docker Desktop OR OrbStack; Ollama native installer
   - Windows subsection: Docker Desktop with WSL2 backend; Ollama installed inside Ubuntu WSL
     (`curl -fsSL https://ollama.com/install.sh | sh`); all subsequent commands run in WSL
   - Linux subsection: docker-ce + docker compose v2 plugin; user added to `docker` group;
     Ollama via official installer
   - Verify: `docker --version`, `docker compose version`, `ollama --version`

## 2. Pull the embedding model
   - `ollama pull nomic-embed-text`
   - Verify: `ollama list | grep nomic-embed-text`

## 3. (Optional, local-LLM only) Pull the chat model
   - `ollama pull gpt-oss:20b`
   - Verify: `ollama list | grep gpt-oss`

## 4. Clone the distribution repo
   - `git clone https://github.com/<operator>/community-brain-distribution`
   - `cd community-brain-distribution`
   - Verify: `./verify-install.sh --step 4`

## 5. Configure your .env
   - `cp .env.example .env`
   - Generate `WEBUI_SECRET_KEY` (`openssl rand -hex 32`)
   - Choose inference mode block (uncomment exactly one)
   - Verify: `./verify-install.sh --step 5`

## 6. Download the corpus
   - `./download-corpus.sh`
   - Verify: tarball SHA matches `EXPECTED_SHA256`; extraction populates `./corpus/lancedb/nomic-v1/`

## 7. Start the stack
   - `docker compose up -d`
   - Verify: `./verify-install.sh --step 7` (checks /health, /sessions, ports, schema/manifest match)

## 8. Configure Open WebUI (GUI walkthrough)
   - Open `http://127.0.0.1:3000` in browser
   - Create admin account (first user becomes admin)
   - Add inference connection:
     - Local mode: confirm Ollama auto-discovered
     - Cloud mode: paste OPENAI_API_BASE_URL + key into Connections panel
   - Create custom model "community-brain":
     - Base model: gpt-oss:20b (local) or your chosen cloud model
     - Paste system prompt from `inference-guidelines.md` into the model's system-prompt field
   - Upload filter:
     - Workspace → Functions → Import
     - Select `community_brain_filter.py`
     - Enable the filter globally OR attach it to the custom model
   - Annotated screenshots referenced inline.

## 9. End-to-end validation
   Step 9a (server-side, deterministic):
   - `curl -s http://127.0.0.1:8999/sessions | jq '.sessions | length'`
   - Verify: count matches `session_count` in `corpus/corpus-manifest.json`.
   - `curl -s http://127.0.0.1:8999/health | jq '.schema_version, .embedding_model'`
   - Verify: both match the manifest's schema_version and embedding_model.

   Step 9b (OWUI retrieval smoke test, qualitative):
   - In OWUI chat, select "community-brain" model.
   - Send a content question you know the corpus can answer, e.g.,
     "Summarize a recent discussion about pricing in the coaching calls."
   - Verify: response renders a `[corpus summary: of the N retrieved chunks, ...]` line
     (the filter's per-query summary, NOT a global inventory),
     and citations include session IDs that match values from `/sessions`.

## Troubleshooting
   - See docs/troubleshooting.md (linked)
```

### 6.3 Agent-path affordance

A short section at the top of `INSTALL.md`:

> **If you use an AI coding assistant (Claude Code, Codex, Cursor, Gemini CLI, Aider, etc.):**
> Open this file in that assistant and say: "Follow this install guide on my machine. Run `./verify-install.sh` between major steps. If a step fails verification, fix it before continuing. Ask me for confirmation before any installs that need sudo or before pasting anything I would need to authorize." That's it. The rest of this doc is written so the agent can drive.

This section is the *only* concession to agents. Everything below it is straightforward technical writing that humans and agents read identically.

---

## 7. Verification harness (`verify-install.sh`)

### 7.1 Invocation modes

```bash
./verify-install.sh                  # all checks
./verify-install.sh --step N         # checks for step N only (1-9)
./verify-install.sh --post-install   # final end-to-end smoke check
./verify-install.sh --check-env-drift  # warn if .env is missing keys present in .env.example
```

### 7.2 Per-check output

```
[✓] Step 1.1: Docker installed (24.0.7)
[✓] Step 1.2: Docker Compose v2 (v2.23.0)
[✗] Step 2.1: Ollama not running on http://host.docker.internal:11434
    → Fix: start Ollama (`ollama serve` or open Ollama Desktop)
```

Green ✓ / red ✗ unicode (boring, works on every terminal). One-line remediation hint on failure. Exit code 0 if all pass; non-zero if any fail.

### 7.3 Checks (non-exhaustive)

- Docker + Compose minimum versions
- Ollama reachable on the configured `OLLAMA_BASE_URL`; `nomic-embed-text` model present in `ollama list`
- `.env` exists; `WEBUI_SECRET_KEY` set; exactly one inference mode block uncommented
- Corpus directory exists at `./corpus/lancedb/nomic-v1/chunks.lance/`
- Tarball SHA-256 matches `EXPECTED_SHA256` constant in `download-corpus.sh`
- Containers running; ports bound to 127.0.0.1 (not 0.0.0.0 — guard against accidental LAN exposure)
- `curl 127.0.0.1:8999/health` returns 200 with `status=ok`
- `/health` `schema_version` matches `corpus-manifest.json` `schema_version`
- `/health` `embedding_model` matches `corpus-manifest.json` `embedding_model`
- `/health` `distribution_mode` is `true`
- `curl 127.0.0.1:8999/sessions | jq '.sessions | length'` matches `session_count` in corpus-manifest
- `curl 127.0.0.1:3000` returns OWUI HTML

### 7.4 Same script runs in CI (with fixture corpus + mocked embedding)

`verify-on-pr.yml` in `community-brain-distribution` spins up the stack on `ubuntu-latest`. Full Ollama is too heavy and flaky for CI, so the CI mode substitutes two things:

1. **Fixture corpus**: a tiny pre-built LanceDB (3-5 chunks, known vectors, known schema version) checked into the distribution repo at `tests/fixtures/corpus/`. Used in place of the real downloaded blob.
2. **Mocked embedding endpoint**: a small FastAPI shim (also checked into `tests/fixtures/`, ~50 LOC) that responds to Ollama's `/api/embeddings` shape with canned vectors matching the fixture corpus. The compose file in CI mode points `OLLAMA_BASE_URL` at this shim instead of host Ollama.

The CI workflow:
1. Substitutes the fixture corpus into `./corpus/`.
2. Starts the mock-Ollama container alongside the stack.
3. Runs `verify-install.sh --post-install` — same script the recipient runs, but pointed at the fixture stack.
4. Asserts route shape: `/ingest` and `/reindex` return 404 with `COMMUNITY_BRAIN_DISTRIBUTION_MODE=true`; all five distribution-mode routes return non-404.

Real-Ollama integration is NOT covered by CI; it's covered by the operator's manual pre-flight rehearsal (§11). The CI mode catches doc-drift, image-pinning regressions, schema-version mismatches, and route-shape regressions — not retrieval-quality regressions.

---

## 8. Inference backend configuration

### 8.1 Two consumers, two concerns

| Consumer | Inference need | Configurable? |
|---|---|---|
| `retrieval-server` | Query-time nomic embeddings via Ollama | No — always Ollama |
| `open-webui` | Chat generation (text completion) | Yes — Ollama OR OpenAI-compatible endpoint |

Ollama is always required because the corpus is pre-embedded with `nomic-embed-text` (Ollama's default tag, no `:v1.5` suffix) and query embeddings must match at lookup time. The exact model identifier passed to Ollama at query time is whatever is in `COMMUNITY_BRAIN_EMBED_MODEL` (default `nomic-embed-text`); the corpus manifest declares the model used at ingestion time, and `verify-install.sh` enforces they match.

### 8.2 `.env.example` shape (all overrides commented out)

```bash
# ============================================================
# Always required — uncomment and set:
# ============================================================
OLLAMA_BASE_URL=http://host.docker.internal:11434
WEBUI_SECRET_KEY=  # generate with: openssl rand -hex 32

# ============================================================
# Optional — overrides for image defaults. Leave commented to
# accept the value baked into the published image.
# ============================================================
# COMMUNITY_BRAIN_EMBED_MODEL=nomic-embed-text

# ============================================================
# Chat inference — uncomment EXACTLY ONE block below.
# ============================================================

# --- Option A: Local Ollama chat (requires ~24 GB unified memory) ---
# Make sure `ollama pull gpt-oss:20b` has been run.
# INFERENCE_LOCAL_MODEL=gpt-oss:20b

# --- Option B: Cloud OpenAI-compatible chat ---
# Works with OpenAI, OpenRouter (proxies Anthropic/Gemini/etc.), Together, Groq, etc.
# OPENAI_API_BASE_URL=https://openrouter.ai/api/v1
# OPENAI_API_KEY=sk-or-v1-...
# INFERENCE_CLOUD_MODEL=anthropic/claude-sonnet-4.6
```

Every value is either left commented (image default applies) or set by the recipient. No active values are pre-populated. This matches the operator-tier `.env.example` discipline (empty-string env vars clobber Dockerfile defaults; commented-out values fall through).

Compose passes the relevant env vars into Open WebUI. OWUI natively supports both backends; no custom adapter needed.

### 8.3 Open WebUI custom model

Created once during install (Step 8 of runbook). Configuration:

- **Name:** `community-brain`
- **Base model:** Recipient's chosen chat model (local or cloud)
- **System prompt:** Paste content of `inference-guidelines.md` verbatim. This is the trust contract that tells the answering LLM how to handle the structured `/query` response (ground_truth vs derived_metadata, citation rules, etc.).
- **Filter attached:** `community_brain_filter.py`, uploaded as a Function and attached to this model.

OWUI does not have config-as-code import at startup, so this is a manual GUI step. A v1.1 candidate is `configure-open-webui.sh` (calls OWUI's REST API given an admin token).

---

## 9. Update mechanics

### 9.1 Recipient update procedure

```bash
cd community-brain-distribution
git pull                                  # gets new compose.yml, filter, docs, scripts
./verify-install.sh --check-env-drift     # surfaces new .env keys
./download-corpus.sh                      # no-op if CORPUS_VERSION unchanged; re-fetches if bumped
docker compose pull                       # grabs new image SHAs
docker compose up -d                      # restart with new images
./verify-install.sh --post-install        # confirm green
```

Same sequence regardless of which flow (A, B, or C) was the actual driver of the update. Scripts figure out what changed.

### 9.2 Notification model (v1)

Manual: operator posts in the Skool community when a release ships, mentions what changed.

No in-stack auto-update pings. No version-check phone-home. Recipients pull when they want.

V1.1 candidate: `check-for-updates.sh` that compares local tag to distribution repo's latest tag via GitHub API and prints a diff. Recipients run it when they're curious.

### 9.3 Backward compatibility commitment

The distribution repo follows semantic versioning at the tag level (`tier-b-vMAJOR.MINOR.PATCH`):

- **PATCH bumps:** bug fixes, doc updates, no recipient-side action beyond `git pull` + `docker compose pull`
- **MINOR bumps:** new optional features, additive schema changes (if any), `.env.example` may add new commented-out keys
- **MAJOR bumps:** breaking changes (schema migration, mandatory new `.env` keys, OWUI version that requires re-setup, etc.). Release notes specify migration steps.

Operator commits to: no breaking changes inside a major version. If a breaking change is needed, cut a major version and document migration.

---

## 10. Security posture

### 10.1 Threat model

| Threat | Vector | Mitigation |
|---|---|---|
| Random internet attacker reaches /query | Port exposed | 127.0.0.1 binding only |
| LAN attacker reaches /query | Recipient misconfigures binding | Compose pins 127.0.0.1 by default; verify-install checks |
| Attacker writes to corpus | `/ingest` route | Routes physically removed in distribution-mode build |
| Recipient leaks their inference API key | `.env` committed to git | `.env` is in `.gitignore` from the start; `.env.example` is the template |
| Operator sees recipient queries | Phone-home | None exists; no telemetry; no version-check ping |
| Adversarial recipient redistributes corpus | Corpus blob is unprotected | Accepted: recipients are participants; corpus already in their hands |
| Stale corpus + new server image | Schema mismatch | verify-install.sh checks compatibility; refuses to start on mismatch |

### 10.2 Auth surfaces

- **Retrieval API (`/query`, `/sessions`):** No token. 127.0.0.1 binding is the auth.
- **Open WebUI:** Native auth (first user becomes admin). Signups default to disabled after first user.
- **Inference provider (cloud mode):** Recipient's own API key, stored in their `.env`, never leaves their machine.

### 10.3 What recipients are trusted to do

- Keep `.env` out of git (a `.gitignore` is shipped; pre-commit hook is not).
- Not expose ports to LAN or internet unless they explicitly choose to (changing 127.0.0.1 to 0.0.0.0 in compose is a deliberate action documented as "advanced + unsupported").
- Update when a security-relevant release is announced.

These are reasonable expectations for the audience. No paternalistic guardrails.

---

## 11. Pre-flight discipline (release rehearsal)

Before tagging any release in the operator repo, operator performs a clean-machine rehearsal:

1. Spin up a fresh user account (or fresh VM) with no Docker, no Ollama, no prior state.
2. Walk through `INSTALL.md` from the top, literally — no shortcuts, no operator memory.
3. End with `./verify-install.sh --post-install` returning all green.
4. Run §6.2 Step 9 validation:
   - 9a (server-side): `/sessions` count matches manifest; `/health` schema_version and embedding_model match manifest
   - 9b (OWUI retrieval test): send a content question; verify the filter's per-query `[corpus summary: ...]` line renders and citations resolve to actual corpus sessions

This is lighter than the operator-tier DR rehearsal (no personal-state recovery at stake), but it's the only thing that catches "the runbook says X but the file is now called Y." Bake into the release checklist.

The CI workflow `verify-on-pr.yml` (§7.4) covers structural correctness against a fixture corpus, but a human walkthrough on real hardware catches UX regressions (e.g., new OWUI version changed the menu path for Functions upload) and retrieval-quality regressions that fixture-based CI can't see.

---

## 12. Non-goals (what Tier B does NOT do)

Explicit list, so future maintenance doesn't accidentally drift into scope creep:

- **No `/ingest`** — read-only by design.
- **No n8n stack** — operator-only.
- **No Mac sync / Automator / launchd** — operator-only.
- **No Fathom integration** — operator-only.
- **No multi-tenant** — one OWUI instance, one logical user per machine.
- **No telemetry / phone-home** — zero data collected from recipients, no version-check ping.
- **No automated update notifications** — manual Skool announcement (v1.1 candidate).
- **No SLA / formal support** — best-effort via the Skool community channel.
- **No commercial license** — community redistribution only; operator holds IP and may rescind.
- **No "bring your own corpus"** — recipients get the operator's curated set, period (v1.1 candidate: personal-notes side-table).
- **No mobile UI** — desktop browser only; mobile is "use a mobile browser, no native support."
- **No corpus delta updates** — every corpus release is a full tarball, not a diff. Acceptable while compacted size is <2 GB.
- **No DRM / access control on the corpus blob** — recipients are trusted (participants); operator accepts that copies may circulate.

---

## 13. Future candidates (banked, not in v1)

### v1.1 (post-launch polish)
- `configure-open-webui.sh` — programmatic OWUI configuration via REST API (skips Step 8 GUI walkthrough)
- `check-for-updates.sh` — recipient-pull update notification
- Personal-notes side-table — recipient can `/ingest` their own personal content into a separate LanceDB table that doesn't touch the shipped corpus
- Annotated Loom walkthrough video referenced from README
- Pre-commit hook to block `.env` commits

### v2 (if/when needed)
- Cloudflare R2 hosting (only if corpus crosses 1.5 GB compacted)
- Signed-URL gating on corpus blob (only if operator decides public distribution is wrong)
- Native mobile-friendly UI variant
- Multi-corpus support (multiple curated communities served by one retrieval-server)

---

## 14. Open questions / known unknowns

Items deliberately left unresolved at design time, to be answered in the implementation plan or during implementation:

1. **OWUI version pin baseline.** Which specific OWUI SHA does the v1 release ship with? Needs a test pass against the latest release that the operator has validated.
2. **gpt-oss:20b as the documented local model.** Is this still the right default for local-LLM mode, or has a better local-model emerged that we'd recommend instead?
3. **CI minute consumption.** Public repos have unlimited GitHub Actions minutes, but our smoke install workflow pulls Docker images + runs a stack — minutes-per-run could be 5-10 min. Worth instrumenting after a few runs to confirm we're not burning resources.
4. **Non-Claude-Code agent rehearsal.** The runbook is agent-agnostic in principle, but we should rehearse the install with each of {Codex, Gemini CLI, Aider} at least once to catch agent-specific failures the design didn't anticipate.

Resolved during spec review (no longer open):
- ~~Distribution-mode mechanism~~ — runtime env var for v1 (§1.4, §2.3)
- ~~Compaction script location~~ — operator repo (§5.4)
- ~~Authoritative version axis~~ — distribution repo tag (§1.4, §4.1)
- ~~`/version` endpoint~~ — replaced by extended `/health` (§4.2)
- ~~LanceDB mount path~~ — `./corpus:/data:ro` with `LANCEDB_PATH=/data/lancedb/nomic-v1` (§3.3)
- ~~Embedding model env var~~ — `COMMUNITY_BRAIN_EMBED_MODEL` (untagged `nomic-embed-text`) (§3.3, §8.2)
- ~~Config mount~~ — rely on image-bundled `/app/config`; no host mount (§3.3)
- ~~Compaction "never modifies prod" claim~~ — corrected to filesystem-snapshot-first recipe (§5.4)
- ~~Windows support depth~~ — WSL2 only (§1.4, §6.2 Step 0)
- ~~CI smoke install with real Ollama~~ — fixture corpus + mocked embedding endpoint (§7.4)
- ~~`.env.example` shape~~ — all values commented out, every mode opt-in (§8.2)
- ~~OWUI validation expecting global corpus inventory~~ — split into server-side `/sessions` check + filter per-query summary check (§6.2 Step 9)

---

## 15. Implementation handoff

This spec hands off to a `writing-plans` session to produce the implementation plan. The plan should decompose into discrete tasks suitable for `subagent-driven-development`, covering:

**Server-side changes (in `community-brain/` Python package):**
- Distribution-mode gating in `community_brain.query.retrieval_server` (skip `/ingest` + `/reindex` route registration when `COMMUNITY_BRAIN_DISTRIBUTION_MODE=true`)
- Extended `/health` returning `status`, `server_version`, `schema_version`, `embedding_model`, `distribution_mode`
- Route-shape test asserting absence of `/ingest` and `/reindex` and presence of the five distribution-mode routes when the env var is set
- New CLI: `community_brain.cli.verify_corpus_clean_v3` (asserts FTS index built, no legacy v2 index, no partial transactions)
- New CLI: `community_brain.cli.write_corpus_manifest` (emits `corpus-manifest.json` from a LanceDB path)

**Operator-side scripts (in operator repo `scripts/`):**
- `release-corpus.sh` (filesystem-snapshot → compact → verify clean v3 → tarball → hash → manifest)
- Optional helper to invoke `gh release create` and open the distribution-repo PR

**Operator-repo CI workflows:**
- `build-retrieval-image.yml` (build + push image on `tier-b-retrieval-v*` tag; open PR in distribution repo)
- `sync-curated-files.yml` (copy `community_brain_filter.py` + `docs/inference-guidelines.md` into distribution repo on operator-repo main update)

**New repo creation: `community-brain-distribution`:**
- All files in §3.1 (compose.yml, INSTALL.md, verify-install.sh, .env.example, download-corpus.sh, docs/{screenshots,tour.md,troubleshooting.md})
- `tests/fixtures/corpus/` (tiny pre-built LanceDB)
- `tests/fixtures/mock-ollama/` (FastAPI shim serving canned vectors)
- `.github/workflows/verify-on-pr.yml`
- `.gitignore` blocking `.env`, `corpus/`, `corpus.previous/`

**Release process:**
- Documented operator release checklist (snapshot → image build → distribution PR → corpus PR → tag distribution repo → announce in Skool)
- Pre-flight rehearsal step on a clean Mac VM
- v1.0.0 cut

**Out of scope for the implementation plan (deferred):**
- Anything in §13 (v1.1 and v2 candidates)
- Tier A (community-full) — separate spec

---

**End of design spec.**

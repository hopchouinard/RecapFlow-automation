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

### 1.3 Audience

Members of the operator's public community who participated in the coaching calls. Specific characteristics that drive design:

- They were on the calls — corpus content is not new information to them; the value is searchability, not discovery.
- They build AI-assisted applications — assume they have at least one of `{Claude Code, Codex, Cursor, Gemini CLI, Aider}` installed and functional.
- Mixed technical sophistication, but uniformly comfortable enough with AI coding tools to delegate setup work to an agent if given good instructions.
- Hardware: mixed (Mac/Windows/Linux). Cannot assume Apple Silicon with 24 GB unified memory.

### 1.4 Locked-in decisions (from brainstorming, 2026-05-10)

| Decision | Choice | Rationale |
|---|---|---|
| Corpus content | Full curated corpus, ships as-is | Recipients are participants; consent-by-attendance is the cleanest model |
| Hosting model | 100% recipient self-host | Preserves personal-state philosophy; bounds operator cost; no multi-tenant infra |
| UX shape | Open WebUI + filter + custom model; pluggable inference backend | Matches operator's daily UX; same package supports cloud-LLM and local-LLM modes |
| Platforms | macOS + Windows + Linux | Three-way Docker target; ~zero exclusion |
| Install path | Single rigorous Markdown runbook (agent-agnostic) + human extras + verification harness | Audience-aware: AI assistants drive install for recipients who delegate; humans follow same doc by hand |
| Distribution channel | Public GitHub repo, sibling `community-brain-distribution` | Cooked-product repo separate from operator source |
| Build/release model | Pre-built Docker images on ghcr.io + corpus blob as GitHub Release asset | SHA-pinning discipline; free hosting; `git pull` updates |
| API surface | `/query` + `/sessions` only; no `/ingest` | Read-only contract |
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
      EMBEDDING_MODEL: ${EMBEDDING_MODEL:-nomic-embed-text:v1.5}
      COMMUNITY_BRAIN_DISTRIBUTION_MODE: "true"
      COMMUNITY_BRAIN_ARTIFACT_ROOT: "/data/output"  # unused in read-only mode but defensive
    volumes:
      - ./corpus/lancedb:/app/lancedb:ro
      - ./config:/app/config:ro
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

`extra_hosts: host.docker.internal:host-gateway` is required so containers reach the host's Ollama on all three platforms. We learned this the hard way during operator-tier work; documented in INSTALL.md troubleshooting.

---

## 4. Build and release pipeline

### 4.1 Three independent flows

Releases are not monolithic. Each of the following can be cut independently:

**Flow A: retrieval-server image** (operator-repo CI, triggered by tag)

1. Operator tags `tier-b-retrieval-vX.Y.Z` in operator repo.
2. `.github/workflows/build-retrieval-image.yml` builds the `community-brain` package into a Docker image with `COMMUNITY_BRAIN_DISTRIBUTION_MODE` defaulted on, pushes to `ghcr.io/<operator>/community-brain-retrieval:X.Y.Z` and as `@sha256:...`.
3. Same workflow opens a PR in `community-brain-distribution` updating the `retrieval-server` image SHA in `docker-compose.yml`. Operator reviews + merges.

**Flow B: corpus snapshot** (operator runs locally; CI helper)

1. Operator runs `scripts/release-corpus.sh` (a script in the operator repo) which:
   - SSHes to the VM
   - Opens the live LanceDB read-only
   - Calls `optimize_files()` and `cleanup_old_versions()` into a fresh `/tmp/corpus-vX.Y.Z/lancedb/` directory
   - Tarballs as `corpus-vX.Y.Z.tar.gz`
   - Generates `sha256sum.txt` for the tarball
   - Generates a `corpus-manifest.json` (session count, schema version, generation timestamp, embedding model identifier)
   - SCPs all three back to operator machine
2. Operator runs `gh release create corpus-vX.Y.Z` in `community-brain-distribution`, attaching `corpus-vX.Y.Z.tar.gz`, `sha256sum.txt`, `corpus-manifest.json`.
3. Operator opens a PR in `community-brain-distribution` updating `download-corpus.sh`'s `CORPUS_VERSION` constant and `EXPECTED_SHA256`. Operator reviews + merges.

**Flow C: Open WebUI SHA bump** (operator, ad hoc)

1. When operator decides to bump OWUI (after testing the new version against the filter + alembic migrations), operator manually opens a PR in `community-brain-distribution` with the new SHA.
2. `verify-on-pr.yml` runs in the distribution repo CI: spins up the stack on `ubuntu-latest`, runs `verify-install.sh --post-install`. Catches alembic regressions before merge.

### 4.2 Schema-bump discipline

If a `retrieval-server` release ships a LanceDB schema change (i.e., the new image expects a schema version newer than the latest published corpus), the matching `corpus-vX.Y.Z` Release MUST be published first or simultaneously.

Enforcement mechanisms:
- The corpus tarball's `corpus-manifest.json` declares the schema version that produced it.
- The retrieval-server image declares its expected schema version at startup (already exists in `community-brain.ingestion.schema`).
- `verify-install.sh` checks compatibility before starting the stack; a mismatch refuses the install with a clear "your corpus is schema vN.X, your server expects vN.Y — fetch a newer corpus" message.

Operator-side: never tag a new retrieval-server release for distribution without confirming the corpus is consistent. The release-rehearsal step (§8) catches this if missed.

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

### 5.4 Compaction is required at every release

Reasoning is two-fold:
1. **Privacy:** `_versions/` contains operator-personal ingestion history (timestamps, intermediate-state snapshots from schema migrations, force-reextract operations). Shipping it leaks operator operational history.
2. **Size hygiene:** 4 GB of history is dead weight for recipients who have no way to time-travel into it.

Implementation (in `scripts/release-corpus.sh`):
```python
import lancedb
db = lancedb.connect(SOURCE_PATH)
table = db.open_table("chunks")
table.optimize()                       # compact_files() under the hood
table.cleanup_old_versions(older_than=timedelta(seconds=0))
# Now copy the table directory to a fresh output path
```

The compacted directory is what gets tarballed. The operator's live LanceDB is never modified (the script reads + copies, never operates on the prod path in-place).

### 5.5 Tarball format and integrity

- **Format:** `tar.gz` (boring, universal). Internal layout: `corpus-vX.Y.Z/lancedb/nomic-v1/chunks.lance/`.
- **Hashing:** SHA-256 generated server-side, published as `sha256sum.txt` alongside the tarball in the Release.
- **Manifest:** `corpus-manifest.json` declares schema_version, embedding_model, session_count, generation_timestamp_utc, total_chunks. Used by `verify-install.sh` for compatibility checks.

`download-corpus.sh`:
1. Reads `CORPUS_VERSION` from itself (the script is the version anchor).
2. Fetches the tarball + sha256sum.txt + manifest.json from the corresponding GitHub Release.
3. Verifies SHA-256.
4. Extracts to `./corpus/lancedb/`.
5. Refuses to extract if SHA mismatch.

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
   - Pick your inference mode: local (gpt-oss:20b) or cloud (OpenAI/OpenRouter/Anthropic/Gemini)
   - If you have an AI assistant (Claude Code / Codex / Cursor / Gemini CLI / Aider):
     give it this file and say "follow this install guide on my machine"

## 1. Install Docker + Ollama
   - macOS subsection
   - Windows subsection (WSL2 caveats)
   - Linux subsection (group permissions caveats)
   - Verify: `docker --version`, `docker compose version`, `ollama --version`

## 2. Pull the embedding model
   - `ollama pull nomic-embed-text:v1.5`
   - Verify: `ollama list | grep nomic`

## 3. (Optional, local-LLM only) Pull the chat model
   - `ollama pull gpt-oss:20b`
   - Verify: `ollama list | grep gpt-oss`

## 4. Clone the distribution repo
   - `git clone https://github.com/<operator>/community-brain-distribution`
   - `cd community-brain-distribution`
   - Verify: `./verify-install.sh --step 4`

## 5. Configure your .env
   - `cp .env.example .env`
   - Generate `WEBUI_SECRET_KEY` (instructions inline)
   - Choose inference mode block (uncomment the right one)
   - Verify: `./verify-install.sh --step 5`

## 6. Download the corpus
   - `./download-corpus.sh`
   - Verify: tarball SHA matches manifest; extraction succeeds

## 7. Start the stack
   - `docker compose up -d`
   - Verify: `./verify-install.sh --step 7` (checks /health, /sessions, ports)

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
   - In OWUI chat, select "community-brain" model
   - Send: "What sessions are in the corpus?"
   - Verify: response contains `[corpus summary:]` header + session count matching corpus-manifest
   - Send: "Find a quote from <speaker> about <topic>"
   - Verify: response contains citation with session ID and quote that resolves to corpus

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
- Ollama reachable; required models pulled
- `.env` exists; `WEBUI_SECRET_KEY` set; no commented-out values that should be uncommented for chosen mode
- Corpus directory exists; SHA-256 of `chunks.lance/data/*.lance` files matches manifest
- Schema version in corpus manifest matches what retrieval-server expects (read from a `/version` endpoint)
- Containers running; ports bound to 127.0.0.1 (not 0.0.0.0 — guard against accidental LAN exposure)
- `curl 127.0.0.1:8999/health` returns 200
- `curl 127.0.0.1:8999/sessions | jq '.sessions | length'` matches `session_count` in corpus-manifest
- `curl 127.0.0.1:3000` returns OWUI HTML

### 7.4 Same script runs in CI

`verify-on-pr.yml` in `community-brain-distribution` spins up the stack on `ubuntu-latest` with a fresh checkout and runs `verify-install.sh --post-install`. Any PR that breaks the install fails CI. This is the primary defense against doc-drift and image-pinning regressions.

---

## 8. Inference backend configuration

### 8.1 Two consumers, two concerns

| Consumer | Inference need | Configurable? |
|---|---|---|
| `retrieval-server` | Query-time nomic embeddings via Ollama | No — always Ollama |
| `open-webui` | Chat generation (text completion) | Yes — Ollama OR OpenAI-compatible endpoint |

Ollama is always required because the corpus is pre-embedded with `nomic-embed-text:v1.5` and query embeddings must match at lookup time.

### 8.2 `.env` shape

```bash
# === Always required ===
OLLAMA_BASE_URL=http://host.docker.internal:11434
EMBEDDING_MODEL=nomic-embed-text:v1.5
WEBUI_SECRET_KEY=<random-string-generate-with-openssl-rand-hex-32>

# === Pick ONE chat inference block ===

# Option A — Local Ollama chat
# Comment out OPENAI_API_* lines below; OWUI will use OLLAMA_BASE_URL.
# Make sure `ollama pull gpt-oss:20b` has been run.
INFERENCE_LOCAL_MODEL=gpt-oss:20b

# Option B — Cloud OpenAI-compatible chat
# Works with: OpenAI, OpenRouter (proxies Anthropic/Gemini/etc.), Anthropic-via-OpenRouter,
# Gemini-via-OpenRouter, Together, Groq, etc.
# OPENAI_API_BASE_URL=https://openrouter.ai/api/v1
# OPENAI_API_KEY=sk-or-v1-...
# INFERENCE_CLOUD_MODEL=anthropic/claude-sonnet-4.6
```

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
4. Send the canonical test queries from §6.2 Step 9, confirm:
   - `[corpus summary:]` header appears
   - Session count matches manifest
   - Citations resolve to actual corpus content

This is lighter than the operator-tier DR rehearsal (no personal-state recovery at stake), but it's the only thing that catches "the runbook says X but the file is now called Y." Bake into the release checklist.

The CI workflow `verify-on-pr.yml` covers most of this automatically, but a human walkthrough catches UX regressions (e.g., new OWUI version changed the menu path for Functions upload) that automated tests miss.

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
3. **Compaction script location.** Does `scripts/release-corpus.sh` live in the operator repo or in `community-brain/` (the Python package)? Probably operator repo since it's an operator workflow, not a package capability.
4. **CI cost.** GitHub Actions free tier on private repos has minute limits. Public repos are unlimited, but our smoke install workflow pulls Docker images + runs a stack — minutes-per-run could be 5-10 min. Need to estimate aggregate consumption vs free quota.
5. **What does the agent-path actually look like in practice for non-Claude-Code agents?** The runbook is agent-agnostic in principle, but we should rehearse the install with each of {Codex, Gemini CLI, Aider} at least once to catch agent-specific failures.
6. **Distribution-mode build mechanism.** Should `COMMUNITY_BRAIN_DISTRIBUTION_MODE` be a runtime env var (current proposal) or a build-time flag that produces a fundamentally different image? Runtime is simpler; build-time is more secure (literally cannot enable write routes by setting an env var). Recommendation: runtime for v1, build-time if a threat materializes.

---

## 15. Implementation handoff

This spec hands off to a `writing-plans` session to produce the implementation plan. The plan should decompose into discrete tasks suitable for `subagent-driven-development`, covering:

- Distribution-mode build flag in `community_brain.query.retrieval_server`
- `scripts/release-corpus.sh` (compaction + tarball + manifest + SHA)
- Operator-repo CI workflows: `build-retrieval-image.yml`, `sync-curated-files.yml`
- New repo creation: `community-brain-distribution` (bootstrapping)
- All files in §3.1 of this spec (compose.yml, INSTALL.md, verify-install.sh, .env.example, download-corpus.sh, docs/)
- Distribution-repo CI: `verify-on-pr.yml`
- Release rehearsal in a clean Mac VM
- v1.0.0 cut: tag, build, snapshot, publish, announce

Out of scope for the implementation plan (deferred):
- Anything in §13 (v1.1 and v2 candidates)
- Tier A (community-full) — separate spec

---

**End of design spec.**

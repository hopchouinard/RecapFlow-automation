# Community Brain — Deployment Runbook

This document guides Claude Code (or any operator) through deploying the `retrieval-server` container on the VM via SSH. It's a **runbook**, not a tutorial: follow the steps in order, verify each checkpoint, and escalate when something unexpected happens.

**SSH target:** `n8n-automation` (alias configured on the Mac Mini; resolves via `~/.ssh/config`).

**Scope:** deploying the `community-brain/retrieval-server` Docker Compose service. Does NOT cover n8n, Postgres, or Ollama — those are preexisting infrastructure on the VM.

---

## Environment mapping — CRITICAL READ FIRST

The same repository exists at two different absolute paths on two different hosts. **They must not be confused.**

| Host | Repo root | When it's used |
|---|---|---|
| **Mac Mini** (dev / where Claude Code runs) | `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation` | Committing code, running local tests, editing the runbook itself |
| **VM** (production / where retrieval-server runs) | `/home/pchouinard/n8n` (same as `~/n8n` for user `pchouinard`) | `git pull`, `docker compose build/up`, the deployed service |

**What this means for `git pull` specifically:** the runbook's `git pull` commands run ON THE VM via SSH. They update `/home/pchouinard/n8n` from GitHub `origin/main`. They do NOT touch the Mac Mini checkout, and the Mac Mini checkout does NOT need to be in any particular state for a deploy to succeed — deploy reads from GitHub, not from the local Mac Mini repo.

**What this means for artifact paths:** when `/ingest` receives paths like `/data/output/<date>/...`, those resolve inside the container to files that live on the VM at `/home/pchouinard/n8n/output/<date>/...` (via the Docker volume mount). Mac Mini-side `output/` is never consulted by the deployed service.

Throughout the runbook, commands prefixed with `ssh n8n-automation ...` execute on the VM with its paths. Commands without `ssh n8n-automation` execute on the Mac Mini (used only for local shell variables like `$AUTH_HEADER` and temp files like `/tmp/cb-ingest-body.json`).

---

## 0. Permission model (for Claude acting as operator)

Every step below is tagged with a permission level. Claude MUST respect these.

| Tag | Meaning |
|---|---|
| 🟢 **auto** | Execute without asking. Read-only or reversible operations. |
| 🟡 **confirm** | Pause, show the exact command, wait for user to say "go" (or equivalent). |
| 🔴 **gated** | Do NOT execute even if this document suggests it. User must explicitly authorize the specific command in the current conversation. Examples: `docker volume rm`, deleting `community-brain/lancedb/`, `git push --force`. |

If a step mid-runbook fails in a way this document doesn't explicitly cover, stop and **escalate to the user** — do not improvise destructive recovery.

---

## 1. Prerequisites (verify before any deploy)

### 1.1 — SSH reachability 🟢

```bash
ssh n8n-automation 'echo ok'
```

**Expected:** `ok` on stdout. If SSH fails: stop. The user needs to fix SSH config before anything else.

### 1.2 — VM has Docker Compose v2 🟢

```bash
ssh n8n-automation 'docker compose version'
```

**Expected:** `Docker Compose version v2.x.x`. If v1 or missing: stop and escalate.

### 1.3 — Repo is checked out on the VM 🟢

```bash
ssh n8n-automation 'ls -la ~/n8n/.git/HEAD && git -C ~/n8n remote -v'
```

Assumes repo is at `~/n8n` on the VM (matches the existing convention). If at a different path, adjust all subsequent `cd ~/n8n` commands.

**Expected:** HEAD file exists, remote shows the GitHub URL. If missing: stop, the initial clone hasn't been done.

### 1.4 — Existing services not disturbed 🟢

```bash
ssh n8n-automation 'docker compose -f ~/n8n/docker-compose.yml ps --format "table {{.Service}}\t{{.Status}}"'
```

**Expected:** `n8n` and `db` services running. Note their status. The deployment below must not restart these — only affects the new `retrieval-server` service.

### 1.5 — Ollama is running on the VM host 🟢

```bash
ssh n8n-automation 'curl -sf http://localhost:11434/api/tags >/dev/null && echo ok || echo FAIL'
```

**Expected:** `ok`. If `FAIL`: stop. The retrieval-server depends on Ollama for embeddings. User needs to start it before deploy.

### 1.6 — Disk space 🟢

```bash
ssh n8n-automation 'df -h ~ | tail -1'
```

**Expected:** at least 5 GB free. The first Docker build (pyarrow + lancedb wheels) uses ~2 GB of intermediate layers. Fail-stop if below 5 GB.

### 1.7 — `community-brain/config/.env` exists on the VM 🟢

```bash
ssh n8n-automation 'test -f ~/n8n/community-brain/config/.env && echo exists || echo MISSING'
```

**If MISSING:** stop and report this to the user. They must create `community-brain/config/.env` on the VM manually (see `community-brain/config/.env.example` for the template). Claude does NOT create this file — secrets stay off the conversation transcript.

### 1.8 — `.env` has the required keys populated 🟢

```bash
ssh n8n-automation 'grep -E "^OPENROUTER_API_KEY=[^[:space:]]+$" ~/n8n/community-brain/config/.env >/dev/null && echo ok || echo MISSING_OPENROUTER'
```

**Expected:** `ok`. If `MISSING_OPENROUTER`: stop and ask the user to populate `OPENROUTER_API_KEY` in the `.env` on the VM. The regex checks for a non-empty value after `=`.

`RETRIEVAL_API_KEY` is optional (unset = auth disabled). No check needed.

Do NOT `cat` or `head` the `.env` file — it contains secrets that would end up in the conversation transcript.

---

## 2. First-time deployment

Use this section only when the `retrieval-server` container has never been deployed before (or has been fully torn down).

### 2.1 — Pull latest main 🟢

```bash
ssh n8n-automation 'cd ~/n8n && git fetch origin && git checkout main && git pull --ff-only origin main'
```

**Expected:** `Fast-forward` or `Already up to date.` Record the resulting HEAD SHA:

```bash
ssh n8n-automation 'cd ~/n8n && git rev-parse HEAD'
```

Save this SHA — it's the rollback target if the deploy goes wrong.

### 2.2 — Ensure `community-brain/lancedb/` directory exists 🟢

```bash
ssh n8n-automation 'mkdir -p ~/n8n/community-brain/lancedb && ls -ld ~/n8n/community-brain/lancedb'
```

**Expected:** directory exists, owned by the SSH user. The Docker volume mount requires this directory to exist on the host before the container starts.

### 2.3 — Build the image 🟢

```bash
ssh n8n-automation 'cd ~/n8n && docker compose build retrieval-server'
```

**Expected:** clean build ending with `naming to docker.io/library/recapflow-automation-retrieval-server:latest`. First build takes 3-5 minutes (pyarrow + lancedb wheel compilation). Subsequent builds are faster with layer caching.

**On build failure:** check the output for which layer failed. Common:
- `apt-get` failure → network issue on VM
- `pip install` failure → check Python version (must be 3.11), check pyproject.toml hasn't drifted
- If opaque, escalate.

### 2.4 — Start the service 🟢

```bash
ssh n8n-automation 'cd ~/n8n && docker compose up -d retrieval-server'
```

**Expected:** `Container community_brain_retrieval Started`. The existing `n8n` and `db` containers stay untouched.

### 2.5 — Verify container is running 🟢

```bash
ssh n8n-automation 'docker compose -f ~/n8n/docker-compose.yml ps retrieval-server'
```

**Expected:** STATUS shows `Up N seconds`. If STATUS shows `Restarting` or `Exited`, check logs:

```bash
ssh n8n-automation 'docker compose -f ~/n8n/docker-compose.yml logs --tail=100 retrieval-server'
```

Common startup failures:
- `OPENROUTER_API_KEY not set` → `.env` isn't being picked up (check §7.1)
- LanceDB permission error → host directory perms (check §2.2)
- `Cannot connect to host` for Ollama → not actually a startup failure; happens only on first `/ingest` (see §7.3)

### 2.6 — Health check 🟢

`/health` does NOT require authentication, so use plain curl with explicit status reporting:

```bash
ssh n8n-automation 'curl -s -w "\nHTTP %{http_code}\n" http://127.0.0.1:8999/health'
```

**Expected:** body `{"status":"ok"}` followed by `HTTP 200`. If `HTTP 000`: connection refused, container hasn't bound the port yet; wait 5s and retry. If persistently refused: container crashed; check logs.

---

## 3. Smoke test

Run this immediately after §2 (first-time) and after every §4 (incremental update). Validates that the full ingest → query → sessions pipeline works end-to-end against real Ollama + real OpenRouter.

### 3.0 — Resolve auth mode (ALWAYS FIRST) 🟢

All endpoints except `GET /health` require the `X-API-Key` header **if and only if** `RETRIEVAL_API_KEY` is set to a non-empty value on the VM. Determine this WITHOUT reading the file's content (which would leak the secret into the transcript):

```bash
ssh n8n-automation 'grep -E "^RETRIEVAL_API_KEY=[^[:space:]]+$" ~/n8n/community-brain/config/.env >/dev/null && echo auth_enabled || echo auth_disabled'
```

**If `auth_disabled`:** set the local shell variable to empty:

```bash
AUTH_HEADER=""
```

**If `auth_enabled`:** ask the user for the key value. Claude MUST NOT read `.env` on the VM. Prompt the user:

> "`RETRIEVAL_API_KEY` is set on the VM. Please paste the key value so I can include it in smoke-test requests. (The key won't be echoed back; I'll use it in subsequent curls only.)"

Then bind it to a local shell variable (NOT logged):

```bash
# User supplies the value; store only in local shell
read -r RETRIEVAL_KEY
AUTH_HEADER="-H X-API-Key:${RETRIEVAL_KEY}"
```

Every authenticated curl below references `$AUTH_HEADER`. When it's empty, the `-H` argument collapses into nothing; when set, the header rides on each request.

### 3.1 — Pick a real artifact folder 🟢

```bash
ssh n8n-automation 'ls -1 ~/n8n/output/ | sort | tail -3'
```

**Expected:** at least one `YYYY-MM-DD/` folder containing artifacts from a past n8n run. Pick the most recent. If `output/` is empty, stop and escalate — smoke test requires an existing session artifact.

Ask the user which date to use if more than one is available. Then set this in the local shell:

```bash
SESSION_DATE=2026-04-14  # replace with the chosen date
```

### 3.2 — Verify artifact files exist for that session 🟢

```bash
ssh n8n-automation "ls -1 ~/n8n/output/$SESSION_DATE/"
```

**Expected:** contains at minimum `transcript.txt`, `extracted-signal.md`, `community-post.md`. `prepared-transcript.md` will NOT exist yet in v1 (n8n doesn't produce it until Plan B wires up the prep prompt). For now, we ingest only `extracted_signal` and `community_post` since `prepared_transcript` is absent.

### 3.3 — POST /ingest 🟢

Requires the auth header established in §3.0.

Write the request body to a local temp file first (avoids escape hell across SSH):

```bash
cat > /tmp/cb-ingest-body.json <<EOF
{
  "session_id": "${SESSION_DATE}",
  "session_date": "${SESSION_DATE}",
  "session_title": "Smoke test ingest",
  "artifact_paths": {
    "extracted_signal": "/data/output/${SESSION_DATE}/extracted-signal.md",
    "community_post": "/data/output/${SESSION_DATE}/community-post.md"
  },
  "force_reextract": false
}
EOF
```

Then POST via SSH. The payload goes over stdin so we don't have to quote-escape JSON inside the remote shell:

```bash
cat /tmp/cb-ingest-body.json | \
  ssh n8n-automation "curl -s -w '\nHTTP %{http_code}\n' -X POST http://127.0.0.1:8999/ingest \
    -H 'Content-Type: application/json' \
    ${AUTH_HEADER} \
    --data-binary @-"
```

**Expected:** response body with `"chunks_written": N` (N > 0), `"chunks_failed": 0`, followed by `HTTP 200`. Response shape:

```json
{
  "session_id": "2026-04-14",
  "chunks_written": 5,
  "chunks_by_type": {"extracted_signal": 4, "community_post": 1},
  "chunks_skipped_idempotent": 0,
  "chunks_failed": 0,
  "extraction_model": "google/gemini-3.1-flash-lite-preview",
  "extraction_prompt_version": "chunk-extraction-v1",
  "schema_version": "1.0",
  "warnings": [],
  "unknown_entities_flagged": [...],
  "unknown_speakers_flagged": [...]
}
```

**Failure branches:**
- 400 "no artifact_paths" → JSON body malformed
- 400 "session_id must match..." → `SESSION_DATE` has invalid characters (shouldn't with `YYYY-MM-DD`)
- 403 → API key mismatch
- 500 with `commit_torn_state` → LanceDB commit failed; see §7.4
- 500 with LLM error → OpenRouter unreachable or API key invalid

### 3.4 — POST /query 🟢

Query for something known to be in that session. The user may need to suggest a term they know the session discussed:

```bash
QUESTION="what was discussed about agent frameworks"  # adjust per session content

printf '{"question":"%s","top_k":5}' "$QUESTION" | \
  ssh n8n-automation "curl -s -w '\nHTTP %{http_code}\n' -X POST http://127.0.0.1:8999/query \
    -H 'Content-Type: application/json' \
    ${AUTH_HEADER} \
    --data-binary @-"
```

**Expected:** body with `"total_matched": N` (N > 0), each chunk has `ground_truth`/`derived_metadata`/`provenance`/`similarity`, followed by `HTTP 200`. Verify at least one result's `ground_truth.session_id` matches `$SESSION_DATE`.

### 3.5 — GET /sessions 🟢

```bash
ssh n8n-automation "curl -s -w '\nHTTP %{http_code}\n' ${AUTH_HEADER} http://127.0.0.1:8999/sessions"
```

**Expected:** body with `"total": N` (at least 1) and our session in the `sessions` array, followed by `HTTP 200`.

### 3.6 — Report smoke test outcome 🟢

If all three (§3.3, §3.4, §3.5) pass: deployment is healthy. Report to user: "Smoke test passed. Session `<SESSION_DATE>` ingested (`N` chunks), queryable, listed in /sessions."

If any step fails: stop, report which step, include the error body, and wait for user direction. Do NOT attempt `force_reextract` or other recovery without user authorization.

---

## 4. Incremental update

Use when code on main has advanced and we want the VM running the new version.

### 4.1 — Snapshot LanceDB first 🟡

Pre-deploy backup. Pauses for user confirmation because it's non-trivial but not destructive.

**Use the docker-exec form (host-side `tar czf` fails on container-owned files):**

```bash
ssh n8n-automation 'BAK=~/n8n/community-brain/lancedb-backups/lancedb-$(date -u +%Y%m%dT%H%M%SZ).tgz; \
  mkdir -p ~/n8n/community-brain/lancedb-backups; \
  docker exec community_brain_retrieval tar czf - /data/lancedb > $BAK; \
  ls -lh $BAK'
```

**Expected:** a `.tgz` file in `community-brain/lancedb-backups/`, size depends on corpus. For a corpus of N chunks, roughly N × 10-50 KB (mostly embeddings). Verified 2026-04-28: 184 chunks → 1.2M tarball.

**Why docker exec, not host-side tar?** LanceDB files inside the volume are owned by the container's user (UID inside the container, e.g. `node`), NOT by the SSH user (`pchouinard`). A host-side `tar czf` will fail with `Cannot open: Permission denied` on every `.lance` data file. Running tar **inside the container** sidesteps the ownership mismatch — the container user can read its own files, tar streams to stdout, the SSH session's remote shell redirects that stream to a host-side path. The resulting `.tgz` is written by the SSH user via plain shell redirection (no Docker volume crossing on the write side), so the file lands in `~/n8n/community-brain/lancedb-backups/` owned by `pchouinard` and freely manipulable by host-side tools (`tar tzf`, `ls -lh`, etc.).

**Confirm with user before running:** "About to snapshot LanceDB to `community-brain/lancedb-backups/lancedb-<timestamp>.tgz`. Proceed?"

### 4.2 — Record current deployed SHA 🟢

Before updating, remember what we're rolling back FROM:

```bash
ssh n8n-automation 'cd ~/n8n && git rev-parse HEAD'
```

Save this SHA as `ROLLBACK_SHA`. The user may want to roll back to it.

### 4.3 — Pull latest main 🟢

```bash
ssh n8n-automation 'cd ~/n8n && git fetch origin && git pull --ff-only origin main'
```

**Expected:** fast-forward successful. If it fails (non-fast-forward, local changes on VM), stop and escalate — don't force-merge.

### 4.4 — Check if the update requires rebuild 🟢

Rebuild is needed if any of these changed since the rollback SHA:

- `community-brain/Dockerfile`
- `community-brain/pyproject.toml`
- `community-brain/src/**`

```bash
ssh n8n-automation "cd ~/n8n && git diff --stat $ROLLBACK_SHA..HEAD -- community-brain/Dockerfile community-brain/pyproject.toml community-brain/src/ | tail -1"
```

**If the diff shows no changes:** config-only update, skip to §4.7 (restart). **If there are changes:** proceed to §4.5.

### 4.5 — Build new image 🟢

```bash
ssh n8n-automation 'cd ~/n8n && docker compose build retrieval-server'
```

**Expected:** clean build. Subsequent builds use layer cache, typically 30s-2min.

### 4.6 — Recreate the container 🟢

```bash
ssh n8n-automation 'cd ~/n8n && docker compose up -d retrieval-server'
```

Compose detects the new image and recreates the container. Brief (~2s) service interruption as the container swaps.

### 4.7 — Restart without rebuild (config-only updates) 🟢

If §4.4 showed no code changes (only config / docs), a plain restart picks up the `.env` edits:

```bash
ssh n8n-automation 'cd ~/n8n && docker compose restart retrieval-server'
```

### 4.8 — Verify health post-deploy 🟢

```bash
ssh n8n-automation 'curl -s -w "\nHTTP %{http_code}\n" http://127.0.0.1:8999/health'
```

**Expected:** `{"status":"ok"}` followed by `HTTP 200`. Re-run the smoke test (§3) — note that §3.0's `AUTH_HEADER` resolution must be repeated (it's shell-local and doesn't persist across runbook invocations).

---

## 5. Rollback

When a deploy misbehaves and needs to revert.

### 5.1 — Checkout the prior SHA 🟡

```bash
ssh n8n-automation "cd ~/n8n && git checkout $ROLLBACK_SHA -- community-brain/"
```

Uses the `ROLLBACK_SHA` recorded in §4.2.

**Confirm with user:** "About to roll back `community-brain/` to `<ROLLBACK_SHA>`. The working tree on the VM will have uncommitted changes reflecting this. Proceed?"

Note: this rolls back only `community-brain/` files (so n8n / docker-compose root-level stuff stays current). If the root `docker-compose.yml` also needs rollback, extend the path: `community-brain/ docker-compose.yml`.

### 5.2 — Rebuild and recreate 🟢

```bash
ssh n8n-automation 'cd ~/n8n && docker compose build retrieval-server && docker compose up -d retrieval-server'
```

### 5.3 — Verify rolled-back service is healthy 🟢

```bash
ssh n8n-automation 'curl -s -w "\nHTTP %{http_code}\n" http://127.0.0.1:8999/health'
```

**Expected:** `{"status":"ok"}` + `HTTP 200`.

### 5.4 — LanceDB restore (only if the rollback was triggered by corruption) 🔴

**GATED — DO NOT execute without explicit user authorization.** Restoring LanceDB from snapshot destroys whatever state is currently in `community-brain/lancedb/`.

Procedure (for reference; user must authorize):

```bash
# Stop service first
ssh n8n-automation 'cd ~/n8n && docker compose stop retrieval-server'

# Pick the backup to restore
ssh n8n-automation 'ls -1 ~/n8n/community-brain/lancedb-backups/'

# Replace live state with backup (DESTRUCTIVE)
ssh n8n-automation 'cd ~/n8n/community-brain && \
  rm -rf lancedb && \
  tar xzf lancedb-backups/<chosen>.tgz'

# Restart
ssh n8n-automation 'cd ~/n8n && docker compose up -d retrieval-server'
```

Claude MUST NOT run this without the user typing "yes, restore LanceDB from backup <name>" or equivalent explicit authorization.

---

## 6. Operational recipes

### 6.1 — Tail logs 🟢

```bash
ssh n8n-automation 'docker compose -f ~/n8n/docker-compose.yml logs -f retrieval-server'
```

Ctrl-C to stop.

### 6.2 — Recent logs only 🟢

```bash
ssh n8n-automation 'docker compose -f ~/n8n/docker-compose.yml logs --tail=200 retrieval-server'
```

### 6.3 — Switch extraction model for A/B testing 🟡

Edits `.env` on the VM. The user authorizes which model to switch to.

```bash
# Example: switch chunk-extraction to Claude Haiku 4.5
ssh n8n-automation "cd ~/n8n && \
  sed -i.bak 's|^#\?COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL=.*$|COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL=anthropic/claude-haiku-4-5|' community-brain/config/.env && \
  docker compose restart retrieval-server"
```

Confirm the new value was set (without leaking secrets from the surrounding lines):

```bash
ssh n8n-automation 'grep "^COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL=" ~/n8n/community-brain/config/.env'
```

**Confirm with user before running** which model to switch to.

**Remember:** model swap alone does NOT bump `extraction_prompt_version`. Existing chunks under the old model are skipped by idempotency. Re-extract specific sessions under the new model by re-POSTing /ingest with `"force_reextract": true`.

### 6.4 — Force re-extraction of a session 🟡

Requires `$AUTH_HEADER` established per §3.0 (auth-enabled mode) or left empty (auth-disabled mode).

```bash
SESSION_DATE=2026-04-14  # adjust

cat > /tmp/cb-reextract-body.json <<EOF
{
  "session_id": "${SESSION_DATE}",
  "session_date": "${SESSION_DATE}",
  "session_title": "Re-extraction",
  "artifact_paths": {
    "extracted_signal": "/data/output/${SESSION_DATE}/extracted-signal.md",
    "community_post": "/data/output/${SESSION_DATE}/community-post.md"
  },
  "force_reextract": true
}
EOF

cat /tmp/cb-reextract-body.json | \
  ssh n8n-automation "curl -s -w '\nHTTP %{http_code}\n' -X POST http://127.0.0.1:8999/ingest \
    -H 'Content-Type: application/json' \
    ${AUTH_HEADER} \
    --data-binary @-"
```

**Confirm with user** which session to re-extract and why.

### 6.5 — Corpus stats 🟢

Fetch the sessions JSON to a local temp file, then run a Python script against it. Requires `$AUTH_HEADER` per §3.0.

**Why two steps:** piping `curl | python3 <<'PY' … PY` doesn't work — the heredoc redirects Python's stdin to the script content, so the pipe is discarded and Python parses its own source as JSON (failing with `JSONDecodeError`). The tmp-file pattern avoids the stdin collision.

```bash
ssh n8n-automation "curl -s ${AUTH_HEADER} http://127.0.0.1:8999/sessions" > /tmp/cb-sessions.json

python3 <<'PY'
import json
with open("/tmp/cb-sessions.json") as fh:
    d = json.load(fh)
print(f"sessions: {d['total']}")
total_chunks = sum(sum(s['chunk_counts'].values()) for s in d['sessions'])
print(f"total chunks: {total_chunks}")
PY
```

**Expected output:**
```
sessions: 12
total chunks: 187
```

**If the Python step fails with `JSONDecodeError`:** the curl probably returned an error (auth failure, server down). Check `cat /tmp/cb-sessions.json` — it'll contain the actual error body or be empty.

### 6.6 — Disk usage of LanceDB 🟢

```bash
ssh n8n-automation 'du -sh ~/n8n/community-brain/lancedb/ ~/n8n/community-brain/lancedb-backups/ 2>/dev/null'
```

### 6.7 — Stop the service 🟡

```bash
ssh n8n-automation 'cd ~/n8n && docker compose stop retrieval-server'
```

**Confirm with user** — `n8n` and `db` remain running, but `/query` and `/ingest` become unreachable.

### 6.8 — Start the service 🟢

```bash
ssh n8n-automation 'cd ~/n8n && docker compose start retrieval-server'
```

---

## 7. Troubleshooting

### 7.1 — `.env` not being picked up

**Symptom:** container logs show `OPENROUTER_API_KEY not set in config/.env` even though you believe `.env` has the key.

**Check:** from the VM, verify compose sees the env_file:

```bash
ssh n8n-automation 'cd ~/n8n && docker compose config retrieval-server | grep -A1 env_file'
```

Should show `- path: ./community-brain/config/.env`. If absent, the compose file on the VM is out of date — pull latest.

**Check:** file exists and has non-empty values:

```bash
ssh n8n-automation 'test -f ~/n8n/community-brain/config/.env && grep -c "^[A-Z]" ~/n8n/community-brain/config/.env'
```

Should print a number > 0. If 0, user hasn't uncommented any lines.

**Check:** the container was recreated AFTER the `.env` edit:

```bash
ssh n8n-automation 'docker inspect community_brain_retrieval --format "{{.State.StartedAt}}"'
```

Compare to the `.env` mtime:

```bash
ssh n8n-automation 'stat -c %y ~/n8n/community-brain/config/.env'
```

If `.env` was modified AFTER the container started, restart the container (§4.7).

### 7.2 — `/ingest` returns 500 `commit_torn_state`

**Symptom:** response body has `"error": "commit_torn_state"`.

**Meaning:** LanceDB delete succeeded but add failed. The table is missing the session's chunks.

**Recovery:** the 500 response includes a `recovery` field with the exact curl to retry with `force_reextract: true`. Execute it (requires user confirmation — treat as §6.4).

### 7.3 — Ollama connection refused from inside container

**Symptom:** `/ingest` 500 with `Connection refused` in embedding stage, or `/query` fails the same way.

**Check:** Ollama is up on the VM host:

```bash
ssh n8n-automation 'curl -sf http://localhost:11434/api/tags | head -c 200'
```

**Check:** container can reach Ollama:

```bash
ssh n8n-automation 'docker exec community_brain_retrieval curl -sf http://host.docker.internal:11434/api/tags | head -c 200'
```

If host can reach but container can't: the `extra_hosts: host.docker.internal:host-gateway` directive isn't working. On Linux Docker, this requires Docker 20.10+. Check: `ssh n8n-automation 'docker --version'`.

As a fallback for Linux hosts, set `OLLAMA_BASE_URL=http://172.17.0.1:11434` (Docker bridge gateway IP) in `community-brain/config/.env` and restart.

### 7.4 — Container restart loop

**Symptom:** `docker compose ps` shows `Restarting`.

**Check logs:**

```bash
ssh n8n-automation 'docker compose -f ~/n8n/docker-compose.yml logs --tail=200 retrieval-server'
```

Common causes:
- **Port already bound:** something else on 8999. `ss -tlnp | grep 8999` on the VM.
- **Volume permission denied:** host dir `~/n8n/community-brain/lancedb/` not writable by the container's user.
- **Corrupted LanceDB:** rare; would appear as a LanceDB-specific error on first `/query` or `/ingest`. Consider §5.4 restore.

### 7.5 — OpenRouter rate limit / auth failure

**Symptom:** `/ingest` returns 200 but `chunks_failed > 0` and the failed chunks have `extraction_error` starting with `OpenRouter returned 429` or `401`.

- **429:** rate limit. Wait, or switch to a different model in §6.3.
- **401/403:** invalid OPENROUTER_API_KEY. User fixes `.env`, then §4.7 restart, then §6.4 re-extract.

### 7.6 — Disk full

**Symptom:** /ingest 500 with `No space left on device` in logs.

Check: `ssh n8n-automation 'df -h ~'`.

Cleanup options (escalate to user before destructive actions):
- Old LanceDB backups: `ls -lh ~/n8n/community-brain/lancedb-backups/`
- Docker layer caches: `docker system df` then `docker builder prune` (user authorization)

---

## 8. Failure escalation

Claude MUST escalate to the user (stop and ask) in any of these cases:

- Any step marked 🔴 is about to be executed
- A step marked 🟡 hasn't received user confirmation
- An unexpected error not covered in §7
- Inconsistent state detected (e.g., container says running but port not bound, or `/sessions` returns a session that doesn't exist in LanceDB)
- Any operation that would modify state across multiple services (retrieval-server + n8n + db)
- User's environment (SSH, VM, Docker) fails prerequisites in §1 — don't try to fix it remotely

When escalating: state (a) which step was in progress, (b) the unexpected observation, (c) what the doc suggests as the next step (if anything), (d) what you're blocked on.

---

## Appendix: quick reference

**Repo path mapping (see "Environment mapping" at the top for full context):**

| Host | Absolute path | Tilde form |
|---|---|---|
| Mac Mini | `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation` | (no tilde — not in user home) |
| VM | `/home/pchouinard/n8n` | `~/n8n` (user `pchouinard`) |

**Common paths on the VM:**

| What | Path |
|---|---|
| Repo root | `/home/pchouinard/n8n` (aka `~/n8n`) |
| compose file | `~/n8n/docker-compose.yml` |
| retrieval-server source | `~/n8n/community-brain/src/community_brain/` |
| env file | `~/n8n/community-brain/config/.env` |
| LanceDB (host) | `~/n8n/community-brain/lancedb/` |
| LanceDB (container) | `/data/lancedb/nomic-v1` |
| Artifact output (host) | `~/n8n/output/<YYYY-MM-DD>/` |
| Artifact output (container) | `/data/output/<YYYY-MM-DD>/` |
| LanceDB backups | `~/n8n/community-brain/lancedb-backups/` |

**Common paths on the Mac Mini (used for local shell variables + temp files only, never the deployed service):**

| What | Path |
|---|---|
| Repo root | `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation` |
| Local temp (smoke-test bodies) | `/tmp/cb-*.json` |

**Common endpoints:**

| Endpoint | Purpose |
|---|---|
| `GET /health` | Liveness check |
| `POST /ingest` | Ingest a session's artifacts |
| `POST /query` | Vector search |
| `GET /sessions` | Corpus inventory |
| `GET /sessions/{id}` | One session's metadata |
| `POST /reindex` | V1 minimal: dry-run matching |

---

## Open WebUI custom-model — manual deploy step (v4+)

The system prompt for the answering model is configured manually in Open WebUI's custom-model UI. The repo's `docs/inference-guidelines.md` is the canonical content.

**Why manual:** Open WebUI doesn't expose a programmatic system-prompt API; the only way to configure the prompt is paste-into-textarea via Admin Settings. Treat the Open WebUI custom model as a deployment artifact that must be re-pasted whenever the source file changes.

### Initial setup (one-time, v4 deploy)

1. Open WebUI → Admin Settings → Models → Create new model
2. Base model: `gpt-oss:20b`
3. Custom model name: `community-brain-v4-gpt-oss:20b` (the conspicuous v4 name signals it's distinct from base `gpt-oss:20b` — easy to tell at a glance which model a chat is using)
4. System prompt: paste the entire content of `docs/inference-guidelines.md`
5. Save
6. Open WebUI → Settings → Default chat model → set to `community-brain-v4-gpt-oss:20b` (or instruct users to select it from the model picker for new chats)

### When `inference-guidelines.md` changes

1. Open WebUI → Admin Settings → Models
2. Edit `community-brain-v4-gpt-oss:20b` (or whatever the current custom-model name is)
3. Replace the system prompt with the current content of `docs/inference-guidelines.md`
4. Save

The retrieval-server filter (`community_brain_filter.py`) no longer prepends the inference-guidelines content as of v4 (Task 8). The custom model's system prompt is the single source for that content at runtime.

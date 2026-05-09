# Operator-Tier Packaging and DR Design

**Date:** 2026-05-07
**Status:** Draft (pending user review)
**Scope:** Operator-tier disaster-recovery install for the RecapFlow stack, including the backup strategy that DR depends on.

## Goals

1. A fresh VM can be brought to a working RecapFlow stack in roughly 15–35 minutes given a backup tarball.
2. The backup pipeline is daily, automated, verified, and leverages existing tooling (Arq) instead of introducing a parallel cloud backup stack.
3. The procedure is documented in language that does not assume the current Mac mini implementation, so future hardware changes do not invalidate the runbook.
4. The design explicitly acknowledges the two-node architecture (VM + inference workstation) and provides DR procedures for each node independently.

## Non-Goals

- Community-tier distribution (full or retrieval-only) — separate follow-up specs.
- High availability or multi-VM scaling.
- Inference workstation IaC. Workstation remains hand-built; DR is runbook-driven.
- n8n encryption-key rotation.
- Monitoring/alerting beyond backup freshness checks.
- OS support beyond Ubuntu/Debian on the VM.
- An automated quarterly restore-test harness (recommended in §2; designed in a follow-up spec).

## Architecture

The RecapFlow stack is a two-node system:

```
┌────────────────────────────────────────────┐         ┌──────────────────────────────────┐
│ Inference workstation                      │         │ n8n VM (Proxmox, Ubuntu/Debian)  │
│ (always-on, sufficient unified memory or   │         │                                  │
│  GPU+VRAM for local models)                │         │  Docker Compose stack:           │
│                                            │         │    - n8n                         │
│  Local model host (Ollama, LM Studio,      │◀────────│    - Postgres 17                 │
│  vLLM, ramalama — implementation detail):  │   LAN   │    - retrieval-server            │
│    - embedding model (e.g. nomic-embed)    │  HTTP   │    - open-webui  ← MOVED HERE    │
│    - generation model (e.g. gpt-oss:20B)   │         │                                  │
│                                            │         │  retrieval-server + open-webui   │
│  Local-side responsibilities:              │────────▶│  both call inference workstation │
│    - Zoom chat sync (Automator + launchd)  │  rsync  │  over LAN for embeddings + gen   │
│    - Backup staging on boot volume:        │  (push) │                                  │
│      ~/RecapFlow-backups/                  │         │  VM-side state:                  │
│      (avoids macOS TCC on secondary vols)  │◀────────│    /var/lib/recapflow-backup/    │
│    - Arq backs up boot vol incl. staging   │  rsync  │    (staging dir for nightly      │
│                                            │  (pull) │     snapshots)                   │
│                                            │         │                                  │
│  Continuity fallback: if local inference   │         └──────────────────────────────────┘
│  is unavailable, repoint Open WebUI at     │
│  OpenRouter/OpenAI as temporary measure    │
└────────────────────────────────────────────┘
```

### Key design properties

- **Asymmetric responsibilities.** Inference workstation owns local model serving, sync orchestration, and backup staging. VM owns the entire Docker application stack.
- **Open WebUI moves from workstation Docker Desktop to the VM Docker Compose stack.** Unifies Docker management on one node, captures Open WebUI state in the existing VM staging snapshot, and slims the workstation's responsibilities to model serving + sync + Arq.
- **VM bootstrap touches Docker only.** No GPU drivers, no model downloads. Fresh VM → install Docker → `docker compose up`.
- **Workstation DR is its own runbook.** Re-pull models from registry, restore configs/scripts/SSH keys/state from Arq, restart services. Staging is on the boot volume — no external HDD required.
- **Boot volume staging avoids macOS TCC.** Originally specced as `/Volumes/HDD_4TB_Archive/`; changed post-implementation because launchd UserAgents cannot write to secondary APFS volumes even with FDA granted. See Post-Implementation Addendum.
- **Single-point-of-failure on the inference workstation is accepted.** Continuity story is "repoint Open WebUI at a cloud LLM (OpenRouter/OpenAI)." No warm spare designed.

## Backup Pipeline

### What gets backed up

Runtime state, secrets, and self-contained restore artifacts:

| Source | Target in staging | Notes |
|---|---|---|
| `pg_dump` of n8n Postgres | `staging/postgres/n8n.pgdump` | Custom format (`-F c`), `--no-acl --no-owner`. Carries workflows, encrypted credentials, execution history. |
| `community-brain/lancedb/` | `staging/lancedb/` | Brief retrieval-server pause for clean snapshot. ~3.8GB; dedupes well in Arq. |
| `data/` (n8n internal) | `staging/n8n-data.tar.zst` | **Includes the encryption key.** Without this file, restored credentials are unrecoverable. |
| `n8n-state/` | inside the tar | Backfill + poll state. |
| `output/`, `watch/`, `historical/` | inside the tar | Already in git, but tarball makes restore self-contained. |
| Open WebUI data volume | `staging/openwebui/` | SQLite/Postgres + uploaded files, post-migration to VM. |
| `.env`, `community-brain/config/.env` | `staging/secrets/` mode 600 | Secrets that cannot live in git. |
| `docker-compose.yml`, `workflows/*.json`, `prompts/` | `staging/code-snapshot/` | Redundant with git, but lets restore work even if GitHub is unreachable. |
| `MANIFEST.txt` + per-file SHA-256 | `staging/MANIFEST.txt` | Restore-time integrity check. |

### What is NOT backed up

- Docker images (re-pulled by `docker compose pull`).
- Local model files (re-pulled with the model-host's pull command, e.g. `ollama pull`).
- General source code (in git).
- Logs (`*.log`).
- `.venv`, `__pycache__`, etc.

### Pipeline mechanics

```
VM (daily, e.g. 02:00 local)                      Inference workstation                     Cloud
────────────────────────────────                  ─────────────────────                     ─────

cron → /usr/local/sbin/recapflow-snapshot.sh      launchd timer (~02:30):
  1. mkdir staging/<ISO-timestamp>/
  2. docker exec n8n_db pg_dump → staging/         1. ssh+rsync from VM:
  3. retrieval-server pause                            /var/lib/recapflow-backup/
     rsync lancedb → staging/                          staging/latest/
     retrieval-server unpause                       → ~/RecapFlow-backups/
  4. tar+zstd of data/, n8n-state/,                   staging/<ISO>/         (boot volume;
     output/, watch/, historical/                  2. verify latest symlink   no TCC issue)
  5. cp .env files → staging/secrets/ (chmod 600)  3. verify MANIFEST
  6. cp compose + workflows + prompts
  7. compute sha256, write MANIFEST.txt
  8. update symlink staging/latest
  9. prune local staging older than 7 days

                                                  Arq's existing schedule picks up   ──────▶ encrypted
                                                  ~/RecapFlow-backups/ as part of             cloud
                                                  normal boot-volume backup                   dest
```

### Triggers

- **Scheduled daily** via cron on the VM and launchd on the workstation.
- **On-demand** via `recapflow-snapshot now` (VM) and `recapflow-pull now` (workstation). Used before risky changes, before VM upgrades, before testing the restore path.
- **No event-driven triggers.** Daily granularity matches the workload (handful of sessions/week).

### Retention

- **VM local staging:** rolling 7 days, pruned by the snapshot script.
- **Workstation HDD:** mirrors the VM (rsync `--delete`). Arq handles longer history.
- **Arq cloud:** governed by the operator's existing Arq retention policy. Not redefined here.

### Verification

This section exists because most "I have backups" stories fail here.

- **Per-snapshot postcondition.** Snapshot script exits nonzero unless `MANIFEST.txt` exists, every expected file is present, and every SHA-256 sum matches. A failed snapshot does not propagate to the workstation, intentionally — broken snapshots should not pollute Arq.
- **Freshness alert.** Workstation launchd job checks "is there a snapshot less than 25h old?" and fails loud (notification or email) if not. Catches silent pipeline breakage.
- **Quarterly restore test (recommended).** Dedicated runbook to bring up a throwaway VM from the latest snapshot and verify retrieval-server starts and n8n loads workflows. DR confidence scales with rehearsal. Detailed harness is a follow-up spec.

### LanceDB and Postgres snapshot semantics

- **Postgres:** `pg_dump -F c --no-acl --no-owner` is portable across users and compresses internally.
- **LanceDB:** stores tables as directories with manifest-based versioning. The cleanest backup is to pause retrieval-server briefly (~30 seconds), copy the directory tree, and resume. Pausing at 02:00 local is invisible to query traffic.

## Install / Restore Flow on a Fresh VM

### Operator workflow

```
[On the inference workstation]
1. Verify latest snapshot exists:
     ls ~/RecapFlow-backups/staging/latest/MANIFEST.txt

2. Pack and ship to new VM:
     tar -cf /tmp/recapflow-restore.tar \
       -C ~/RecapFlow-backups/staging/latest/ .
     scp /tmp/recapflow-restore.tar newvm:/tmp/

[On the new VM, after fresh OS install + SSH access]
3. Clone repo:
     git clone https://github.com/hopchouinard/RecapFlow-automation
     cd RecapFlow-automation

4. Run bootstrap:
     ./scripts/bootstrap.sh /tmp/recapflow-restore.tar

5. Verify bootstrap output, browse to http://newvm:5678 to confirm n8n loads.

[Back on the inference workstation]
6. Update VM hostname/IP in workstation-side sync script + launchd job (only if changed).
7. Run a test snapshot to confirm pipeline now points at new VM.
```

### `bootstrap.sh` phases

A single bash script, organized into eight phases. Each phase logs clearly and exits nonzero on failure with a concrete remediation hint.

#### Phase 1 — Preflight (~5 sec)

- Refuse to run as root.
- Validate exactly one positional arg = path to restore tarball; tarball must exist and be readable.
- Detect OS family — Ubuntu/Debian only for v1.
- Confirm we are in the repo root (presence of `docker-compose.yml`).
- **Idempotency check:** if `data/` is non-empty, refuse without `--force`.

#### Phase 2 — Install host prerequisites (~60 sec)

- Install Docker Engine + Compose v2 plugin from the official Docker apt repo (idempotent).
- Install `rsync`, `zstd`, `tar`.
- Add the current user to the `docker` group; print "log out and back in if first install" if needed.

#### Phase 3 — Stage and verify tarball (~30 sec)

- Extract tarball into `./restore-staging/`.
- Verify `MANIFEST.txt` exists and lists every file present.
- Recompute SHA-256 for each file and compare with manifest. Any mismatch = abort.
- Print summary: snapshot timestamp, n8n version, retrieval-server version, files restored.

#### Phase 4 — Restore state into repo paths

- Unpack `restore-staging/n8n-data.tar.zst` into `./data/`. Permissions/ownership preserved.
- Copy `restore-staging/n8n-state/`, `output/`, `watch/`, `historical/` into the repo root.
- Create `./community-brain/lancedb/` and rsync `restore-staging/lancedb/` into it.
- Place `.env` (chmod 600) at repo root and `community-brain/config/.env` (chmod 600).
- Compare restored `docker-compose.yml` against the one in git. Warn loudly on mismatch and use git's by default.

#### Phase 5 — Database restore (ordering-sensitive)

- `docker compose up -d db` (Postgres only; nothing else).
- Wait for `pg_isready` inside the container; timeout 60s with retries.
- `docker cp restore-staging/postgres/n8n.pgdump n8n_db:/tmp/`.
- `docker exec n8n_db pg_restore -U n8n -d n8n --clean --if-exists /tmp/n8n.pgdump`.
- Remove the dump file inside the container.

#### Phase 6 — Bring up the full stack

- `docker compose up -d`.
- Wait for all containers to report healthy or `running` (timeout 120s).

#### Phase 7 — Smoke tests

- HTTP 200 from `http://localhost:5678` (n8n UI).
- HTTP 200 from `http://localhost:8999/health` (retrieval-server).
- HTTP 200 from `http://localhost:8080` (Open WebUI).
- `docker exec n8n n8n list:workflow` returns the expected workflow IDs.
- A sample query against retrieval-server returns at least one result. This proves LanceDB restored AND the inference workstation is reachable.
- Any failure: print which test failed, exit nonzero. Do not print success when anything failed.

#### Phase 8 — Final operator instructions

Print the post-install checklist:

- Workstation hostname/IP update if changed.
- Test sync from workstation to VM.
- Schedule first backup snapshot.
- Verify Arq picks up the staged backup at next run.

### Failure modes and recovery

- **Tarball checksum mismatch:** abort, instruct operator to re-pull from Arq.
- **Postgres restore fails:** keep the DB volume around for investigation. Do not swallow the error.
- **Port already in use (5678, 8999, 8080):** detect in preflight; instruct operator.
- **Inference workstation unreachable:** smoke test 5 fails. Bootstrap completes but flags the dependency as unhealthy; stack is up, retrieval is degraded until the LAN is fixed.
- **Re-run safety:** `./bootstrap.sh --force <tarball>` re-runs from scratch (warns and confirms before clobbering existing state). Without `--force`, refuses if state exists.

### Time budget for a typical DR run

| Phase | Time |
|---|---|
| OS provisioning + SSH (operator, manual) | 5–15 min |
| scp tarball (LAN, ~5GB) | 1–5 min |
| `git clone` + bootstrap phases 1–4 | 2–4 min |
| Postgres restore | 1–2 min |
| Stack startup + image pull (first time) | 3–8 min |
| Smoke tests | < 1 min |
| **Total: fresh OS to working stack** | **~15–35 min** |

## Inference Workstation DR Runbook

### Two failure modes

- **Mode A: workstation died, Arq backup current.** Normal path. Arq restores boot volume including `~/RecapFlow-backups/` staging.
- **Mode B: workstation died AND Arq stale or unreachable.** Slower path. May need an older snapshot or fallback options.

### Procedure (Mode A)

```
1. New hardware with enough unified memory or GPU+VRAM for the chosen models.
   Current sizing: 24GB unified memory or equivalent
   (gpt-oss:20B + nomic-embed-text + headroom).

2. OS install + restore user data from Arq (Apple Migration Assistant or
   manual Arq restore).
   Critical paths to confirm restored:
     ~/scripts/sync-zoom-chats.sh
     ~/Library/LaunchAgents/com.patchoutech.sync-zoom-chats.plist
     ~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist
     ~/Library/Workflows/Applications/Folder Actions/Sync Zoom Chats.workflow
     ~/.ssh/                       (workstation→VM key)
     ~/.zoom-chat-synced            (state — see note below)
     ~/.zoom-chat-sync.log
     ~/RecapFlow-backups/           (staging — on boot volume, included in Arq)

3. Verify staging is present:
     ls ~/RecapFlow-backups/staging/latest/
   If the directory is missing, restore from Arq before proceeding.
   No external HDD required — staging is on the boot volume.

4. Install local-model serving software.
   Current implementation: `brew install ollama` (or DMG installer), then:
     ollama serve &     # or as a launchd job
     ollama pull nomic-embed-text:v1.5
     ollama pull gpt-oss:20b

   Time budget: nomic ~30sec, gpt-oss ~20-40 min depending on bandwidth.

5. Re-add SSH key to keychain (passphrase auth):
     ssh-add --apple-use-keychain ~/.ssh/<key>

6. Verify SSH from workstation to VM:
     ssh vm-host 'echo ok'

7. Restart launchd jobs:
     launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.sync-zoom-chats.plist
     launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist

   No FDA grant needed — staging is on the boot volume.

8. Reattach Arq to its existing destination (config in ~/Library/Arq usually
   restored, but re-validate license + repo password). Confirm ~/RecapFlow-backups/
   is in the backup scope.

9. Verify pipeline:
     ls ~/RecapFlow-backups/staging/latest/MANIFEST.txt
     launchctl kickstart -k gui/$UID/com.patchoutech.recapflow-pull
     tail -20 ~/Library/Logs/recapflow-pull.log
     Expect: "pull complete; latest = ..." with no rsync errors.

10. Verify Open WebUI on VM can reach this workstation:
     curl http://<workstation-LAN-IP>:11434/api/tags  (from VM)
     Should return list of installed models.
     If macOS firewall blocks, allow incoming on port 11434 for Ollama.
```

### Procedure differences for Mode B (Arq stale or unreachable)

```
3a. If ~/RecapFlow-backups/ was not restored by Arq (stale or cloud unavailable):
      - Check if a recent snapshot exists in Arq from a different date
      - As a fallback, trigger a fresh pull from the VM manually:
          launchctl kickstart -k gui/$UID/com.patchoutech.recapflow-pull
      This requires SSH to the VM to be working first (Step 6 must come first
      if you flip the order).
```

### Critical gotcha: `~/.zoom-chat-synced`

This file tracks which Zoom meeting folders have already been synced to the VM. If lost or empty, the sync script treats every existing folder under `~/Documents/Zoom/` as new and re-uploads everything. Effects on the n8n side:

- Duplicate `YYYY-MM-DD-zoom-chat.txt` writes overwrite existing files in `watch/` (no harm if already-processed; the merged-call workflow has output idempotency).
- For dates that haven't been processed yet, the duplicate would re-trigger the workflow. Output dir already exists from last run → behavior depends on whether n8n's file-write nodes overwrite or append. Mitigation: **before bulk re-sync, manually inventory `output/` and pre-mark already-processed dates in the new state file.**

The spec ships a small one-shot helper (`scripts/seed-zoom-synced-from-output.sh`) that scans `output/<YYYY-MM-DD>/` directories on the VM and seeds `~/.zoom-chat-synced` so the post-DR workstation does not trigger a re-sync flood.

### Out of scope for this runbook

- HDD provisioning (file system formatting, partitioning).
- Recovering Arq license + repo password (assumed in operator's password manager).
- Restoring Open WebUI state (lives on the VM now; restored by VM bootstrap).

## Secrets Handling

### Secret inventory

| Secret | Lives in | Backup coverage | Restore order |
|---|---|---|---|
| n8n encryption key | `data/config` on VM | Inside `n8n-data.tar.zst` (encrypted at rest by Arq) | Before n8n container starts |
| `.env` at repo root | VM repo | `staging/secrets/.env` mode 600 | Before `docker compose` invocations |
| `community-brain/config/.env` | VM repo | `staging/secrets/community-brain.env` mode 600 | Before retrieval-server starts |
| OpenRouter / Fathom API keys | n8n credentials table (encrypted in Postgres) | Inside `n8n.pgdump` | After encryption key is restored, before n8n starts |
| SSH keys (workstation → VM) | Workstation `~/.ssh/` | Arq scope on workstation | Restored as part of workstation DR |
| Arq repo password | Operator's password manager | **NOT in any backup** (chicken-and-egg) | Required before any restore can begin |
| `OLLAMA_URL` (LAN target) | `community-brain/config/.env` | As above | Updated post-restore if workstation IP changed |

### Key principles

1. **The encryption key is the keystone.** Restoring `n8n.pgdump` without `data/config` produces a stack with credentials that decrypt to garbage. Bootstrap explicitly orders these: `data/` placement → Postgres restore → n8n start. Any deviation = silent credential corruption.

2. **The backup tarball contains plaintext-equivalent secrets.** All meaningful security boundary for backups is Arq's repo encryption. The Arq repo password is therefore the most security-critical artifact in the entire system. It must live in the operator's password manager with redundancy — losing it makes every backup unrecoverable.

3. **No interactive secret prompts during bootstrap.** All secrets enter the system via the restore tarball. If a `.env` is missing or an expected key is absent, bootstrap fails loud and points the operator at the manifest. Re-runs are safe and reproducible.

4. **No secrets in git, ever.** `.gitignore` already covers `.env*` (with `!.env.example` for templates). A `git-secrets` or `pre-commit` + `detect-secrets` hook is recommended for the operator tier and mandatory before community tier packaging.

5. **Encryption key rotation is out of scope.** Deferred to a future spec when motivation arises.

### Bootstrap-time secret flow

```
restore-staging/secrets/
├── .env                      → install at ./.env (chmod 600)
└── community-brain.env       → install at ./community-brain/config/.env (chmod 600)

restore-staging/n8n-data.tar.zst
└── unpacks to ./data/
    └── config (the encryption key — single most important file)

restore-staging/postgres/n8n.pgdump
└── pg_restore → encrypted credential cells decrypt against ./data/config
```

Note: SSH keys are NOT in the VM-side backup tarball. They are workstation-side state, restored via Arq during workstation DR.

If any of these three are missing or unreadable, bootstrap aborts before bringing up n8n. Better to fail at minute 3 than have a "running" stack with broken credentials at minute 30.

## Known Limitations / Accepted Risks

- **Inference workstation is a single point of failure for AI features.** Mitigation: manual repoint of Open WebUI to OpenRouter/OpenAI. Documented, not designed-around.
- **Boot volume is the local backup stage.** Staging lives at `~/RecapFlow-backups/` (see Post-Implementation Addendum). Boot volume loss = full workstation DR scenario anyway. Mitigation: Arq's cloud copy of the boot volume.
- **Daily snapshot cadence means up to ~24h of state loss in DR.** Acceptable given workload (handful of sessions/week). Can tighten to hourly later if needed.
- **Re-pulling `gpt-oss:20B` on workstation DR is bandwidth-bound** (~13GB). Acceptable since workstation DR is rarer than VM DR.

## Future Work (Prioritized)

1. **Community-full and community-retrieval-only tier specs.** Now unblocked by this design.
2. **Quarterly restore test harness.** Concrete script to spin up a throwaway VM from latest snapshot and exercise smoke tests.
3. **Backup freshness integration with Grafana.** Push snapshot age metric to the existing monitoring VM.
4. **Pre-commit secret scanning.** Mandatory before any community tier ships.
5. **VM bootstrap support for additional OSes** (Fedora, NixOS-style declarative).
6. **Migration to systemd unit + `docker compose up`** to remove manual restart steps if the VM reboots.

## Post-Implementation Addendum (2026-05-08)

The originally-spec'd staging path `/Volumes/HDD_4TB_Archive/RecapFlow-backups/`
proved problematic in production: macOS TCC blocks launchd UserAgents from
writing to secondary APFS volumes regardless of Full Disk Access grants on
the spawned binaries. Manual terminal runs work; scheduled launchd runs do
not.

**Implemented mitigation:** staging moved to `~/RecapFlow-backups/` on the
boot volume. Arq is configured to back up that path. Same encrypted cloud
destination, same retention behavior, no FDA dance required.

The runbooks and scripts reflect this revised location. The external HDD
plays no role in the live backup pipeline anymore (it remains in Arq's
backup scope for unrelated content).

### Open WebUI deployment lessons (2026-05-08 evening)

Discovered during the post-merge troubleshooting of "retrieval functions and custom system prompt missing on the new VM-side Open WebUI":

- **Volume naming.** Compose's default `volumes: open-webui-data:` creates a volume named `<project>_open-webui-data` (e.g. `n8n_open-webui-data`). The Task 1.2 manual migration restored data into the un-prefixed `open-webui-data` volume because that's what the old workstation compose used. Compose was therefore mounting a different, empty volume than the migrated one. Fix: declare `open-webui-data` as `external: true` in compose so it uses the literal name. Bootstrap Phase 5b creates the volume idempotently before `docker compose up`.

- **Image SHA, not tag.** The `:main` and `:0.8.12` tags both pulled different builds with incompatible alembic migration trees. The workstation OW had been running a build whose head revision (`b2c3d4e5f6a7`) was not in the `:0.8.12` migration scripts; alembic raised `ResolutionError` and Open WebUI silently fell back to a fresh DB, wiping all user state. Pinning by image SHA (immutable) keeps the VM on the exact build that produced the migrated webui.db.

- **`host.docker.internal` mapping for the filter.** The community-brain Open WebUI filter's default `retrieval_url` valve is `http://host.docker.internal:8999/query`, set when Open WebUI ran on workstation Docker Desktop. Now that Open WebUI runs in the VM compose network, an `extra_hosts: host.docker.internal:host-gateway` directive on the open-webui service is required for that hostname to resolve to the VM host's published :8999 port. Alternative would be editing the filter's valve via Admin Settings → Functions to point at the compose service name (`http://retrieval-server:8999/query`); we kept the valve untouched and added the compose mapping to preserve user state exactly.

- **Future Open WebUI upgrades require rehearsal.** Bumping the image SHA can break the schema in non-obvious ways. The DR rehearsal checklist now documents a procedure for safely validating an upgrade on a throwaway VM before merging the SHA bump.

## Open Questions

None at design time. Implementation may surface specifics around:

- Exact location of the VM-side staging directory (`/var/lib/recapflow-backup/` is proposed; could move to a non-root path if running fully unprivileged is preferred).
- Whether snapshot pruning lives in the VM script or as a separate cleanup job.
- Whether the freshness alert delivers via email, macOS notification, or pushover.

These are design-during-implementation choices, not blockers for this spec.

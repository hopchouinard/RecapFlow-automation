# Inference Workstation Disaster Recovery Runbook

## Scope

The inference workstation died (hardware failure, theft, file system corruption). You need to bring a new workstation online with:
- Local model serving (Ollama) restored
- Sync orchestration (Zoom chat sync) restored
- Backup pipeline (rsync from VM, Arq) restored
- LAN connectivity to the VM

The VM itself is unaffected and continues to run; only the workstation needs reconstruction.

## Failure modes

- **Mode A: workstation died, attached HDD survived.** Faster path. Backup history intact.
- **Mode B: workstation AND HDD died.** Slower path. Restore HDD from Arq cloud first.

## Prerequisites

- New hardware with enough unified memory or GPU+VRAM for chosen models. Current sizing: 24 GB unified memory or equivalent (gpt-oss:20B + nomic-embed-text + headroom).
- Arq license + repo password (from password manager).
- The VM is operational and reachable on the LAN.

## Procedure (Mode A)

### Step 1: Set up new hardware and restore user data from Arq

Use Apple Migration Assistant (if going Mac-to-Mac) or manual Arq restore. Critical paths to confirm:

```
~/scripts/sync-zoom-chats.sh
~/Library/LaunchAgents/com.patchoutech.sync-zoom-chats.plist
~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist
~/Library/LaunchAgents/com.patchoutech.recapflow-freshness.plist
~/Library/Workflows/Applications/Folder Actions/Sync Zoom Chats.workflow
~/.ssh/                       (workstation→VM key)
~/.zoom-chat-synced            (state — see "Critical gotcha" below)
~/.zoom-chat-sync.log
```

### Step 2: Reattach the external HDD

```
ls /Volumes/HDD_4TB_Archive/
```

If macOS auto-renamed the volume (e.g., "HDD_4TB_Archive 1"), rename back to `HDD_4TB_Archive` in Disk Utility. The path is hard-coded in launchd plists and rsync targets — divergence here silently breaks the pipeline.

### Step 3: Install the local-model serving software

Current implementation: Ollama.

```
brew install ollama  # or DMG installer
ollama serve &       # or via launchd
ollama pull nomic-embed-text:v1.5
ollama pull gpt-oss:20b
```

Time: nomic-embed-text approximately 30 seconds, gpt-oss:20b approximately 20–40 minutes depending on bandwidth.

### Step 4: Re-add SSH key to keychain

```
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

### Step 5: Verify SSH to VM

```
ssh n8n-automation 'echo ok'
```

### Step 6: Re-install the launchd agents

The launchd plists live at `~/Library/LaunchAgents/` but they reference scripts at `~/Library/Scripts/recapflow/` — a boot-volume copy made by the installer script. The repo at `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/` is the source of truth for the scripts; the installer copies them to the boot-volume location. This indirection exists because macOS TCC (Transparency, Consent, and Control) requires launchd UserAgents to call scripts on the boot volume rather than a secondary APFS volume.

```
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
./scripts/install-launchd.sh
```

This copies `recapflow-pull.sh`, `recapflow-freshness-check.sh`, and `lib/*` to `~/Library/Scripts/recapflow/` and loads the launchd agents.

### Step 7: Grant Full Disk Access to /bin/bash

**This step is required.** Without it, the launchd-scheduled pull will fail with `rsync: error: open: Operation not permitted`. Manual interactive runs from Terminal.app work without this because Terminal.app itself has FDA by default — do not let that mislead you into thinking the step is optional.

1. System Settings → Privacy & Security → Full Disk Access.
2. Click `+` and add `/bin/bash`. (You may need to reveal hidden folders with Cmd+Shift+. in the file picker, or navigate via "Go to Folder" → `/bin`.)
3. Toggle the `/bin/bash` entry on.

The freshness check job works without FDA because it only reads from the HDD. The pull job writes to the HDD and requires FDA.

### Step 8: Reattach Arq

Open Arq.app → restore configuration if not auto-recovered → re-validate license + repo password.

### Step 9: Verify the backup pipeline

```
launchctl kickstart -k gui/$UID/com.patchoutech.recapflow-pull
sleep 60
tail -30 ~/Library/Logs/recapflow-pull.log
launchctl kickstart -k gui/$UID/com.patchoutech.recapflow-freshness
sleep 5
cat ~/Library/Logs/recapflow-freshness.log
```

Expected: pull completes with manifest verified, freshness shows "OK: latest snapshot is Xh old".

### Step 10: Verify the VM can reach this workstation

From the VM:

```
ssh n8n-automation 'curl -sf http://<workstation-LAN-IP>:11434/api/tags | head -c 200'
```

Replace `<workstation-LAN-IP>` with the new workstation's IP, discoverable via `ifconfig en0` on the workstation. The default configured in `community-brain/config/.env` is `10.1.50.219`; update that file and restart the retrieval-server container if the IP changed.

Expected: JSON response listing installed models. If unreachable, the macOS firewall may be blocking port 11434 — System Settings → Network → Firewall → allow incoming for the Ollama process.

### Step 11: Seed `~/.zoom-chat-synced` to prevent re-sync flood

If `~/.zoom-chat-synced` was lost (not covered by Arq, or empty file restored), the sync script will re-upload every existing Zoom folder. Run this before allowing the sync launchd job to fire:

```
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
./scripts/seed-zoom-synced-from-output.sh
```

This queries the VM for already-processed dates (approximately 69 dates as of 2026-05) and seeds the state file. See "Critical gotcha" below for the full picture.

## Procedure (Mode B): HDD also dead

Insert between steps 2 and 3:

### Step 2a: Restore HDD contents from Arq

1. Mount a new external HDD at `/Volumes/HDD_4TB_Archive/`.
2. Open Arq → restore `/Volumes/HDD_4TB_Archive/RecapFlow-backups/`.
3. Time budget: depends on cloud bandwidth and snapshot total size. Plan for "leave it overnight."

After restore completes, continue with Step 3.

## Critical gotcha: `~/.zoom-chat-synced`

This file tracks which Zoom meeting folders have been synced to the VM. If lost or empty, the sync script treats every existing folder under `~/Documents/Zoom/` as new.

**Effects:**
- Duplicate uploads to VM's `watch/` overwrite existing files (no harm if already-processed; the merged-call workflow has output idempotency).
- For unprocessed dates, duplicates re-trigger the workflow. Mostly idempotent but has surfaced edge cases.

**Mitigation:** run `seed-zoom-synced-from-output.sh` (Step 11) BEFORE the sync launchd job runs after DR. If you need to suppress sync entirely until you've seeded:

```
launchctl bootout gui/$UID/com.patchoutech.sync-zoom-chats
# ... seed state file ...
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.sync-zoom-chats.plist
```

## Out of scope

- HDD provisioning (formatting, partitioning).
- Recovering Arq license + repo password (assumed in operator's password manager).
- Restoring Open WebUI state — Open WebUI now runs on the VM (migrated 2026-04), not the workstation. Its state is included in the VM snapshot and restored by the VM bootstrap. The workstation Open WebUI container was stopped and kept as a one-cycle rollback only.
- VM-side recovery — separate runbook (`vm-disaster-recovery.md`).

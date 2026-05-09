# VM Disaster Recovery Runbook

## Scope

The n8n VM died (hardware failure, hypervisor loss, accidental destruction). You need a working RecapFlow stack on a fresh VM, restored from the latest backup snapshot.

This runbook does NOT cover the inference workstation — see `workstation-disaster-recovery.md` for that.

## Prerequisites

- A fresh Ubuntu 22.04+ or Debian 12+ VM with sudo access via SSH.
- The inference workstation is operational (Ollama running, models pulled, LAN reachable).
- A recent snapshot exists at `~/RecapFlow-backups/staging/latest/` on the workstation (boot volume).
- The workstation's Arq license + repo password are accessible (in case snapshots are stale and a cloud restore is needed).

## Procedure

### Step 1: Verify a recent snapshot exists

On the workstation:

```
ls -la ~/RecapFlow-backups/staging/latest/
head ~/RecapFlow-backups/staging/latest/MANIFEST.txt
```

Confirm `snapshot_timestamp` is recent. If older than 25h, the pipeline has been broken for a while; see Step 1b below.

### Step 1b (only if snapshots are stale or missing): restore from Arq

1. Open Arq.app.
2. Navigate to the most recent backup of `~/RecapFlow-backups/` (boot volume scope).
3. Restore to either the original location or to `~/RecapFlow-backups-restore/` temporarily.
4. Update `LOCAL_STAGING` env var in subsequent commands accordingly.

### Step 2: Pack and transfer the snapshot

On the workstation:

```
tar -cf /tmp/recapflow-restore.tar \
  -C ~/RecapFlow-backups/staging/latest/ .
scp /tmp/recapflow-restore.tar new-vm-host:/tmp/
```

The tarball is approximately 6 GB.

### Step 3: Clone the repo on the new VM

```
ssh new-vm-host
git clone https://github.com/hopchouinard/RecapFlow-automation ~/n8n
cd ~/n8n
```

The directory name `n8n` matches the production VM's repo location for consistency. The git remote works regardless of local directory name.

### Step 4: Run the bootstrap script

```
./scripts/bootstrap.sh /tmp/recapflow-restore.tar
```

If Docker isn't yet installed on the VM, the script will install it and exit with code 2. Log out, log back in (so docker group membership applies), then re-run the same command.

Watch the output. Each phase logs clearly. If smoke tests fail, the script exits nonzero and prints which test failed.

**LanceDB extraction note:** the bootstrap script extracts the lancedb tar with `--strip-components=1`. If you're ever running a manual restore instead of using bootstrap.sh, you must include that flag or the data lands one directory level too deep and the retrieval server will return 0 chunks.

### Step 5: Restore the snapshot cron

The bootstrap restores everything in the repo + Docker stack but does NOT install the user crontab — that's a per-VM operator action.

```
crontab -e
```

Add the line from `scripts/cron/recapflow-snapshot.user-crontab` (paste the entry, save, quit). Verify:

```
crontab -l | grep snapshot-vm
systemctl is-active cron
```

The cron fires daily at **06:00 UTC** (02:00 EDT / 01:00 EST). This is a user crontab (not `/etc/cron.d/`) — it runs as the operator user, not root. No sudo is required for the snapshot script.

### Step 6: Update the workstation to point at the new VM

If the new VM has a different hostname/IP than the old one:

1. Edit `~/.ssh/config` on the workstation: change the `n8n-automation` block's HostName.
2. Edit `~/Library/Scripts/recapflow/recapflow-pull.sh` (the installed copy — see `scripts/install-launchd.sh`): no change needed if `VM_HOST` env override is set in the plist; otherwise update the script's default.
3. Reload launchd:
   ```
   launchctl bootout gui/$UID/com.patchoutech.recapflow-pull
   launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist
   ```
4. Test SSH connectivity:
   ```
   ssh new-vm-host 'echo ok'
   ```

### Step 7: Take a fresh snapshot on the new VM

```
ssh new-vm-host '~/n8n/scripts/snapshot-vm.sh'
```

This proves the snapshot pipeline is operational on the new VM and gives you a fresh restore point. Expect approximately 12 minutes (5 GB of LanceDB version history is the bulk).

### Step 8: Trigger an off-cycle workstation pull

```
launchctl kickstart -k gui/$UID/com.patchoutech.recapflow-pull
sleep 60
tail -30 ~/Library/Logs/recapflow-pull.log
```

Expected: pull completes, manifest verifies. Staging is on the boot volume so no FDA grant is required.

### Step 9: Verify end-to-end

- Browse to `http://new-vm-host:5678` — n8n loads, workflows present, credentials work.
- Browse to `http://new-vm-host:3000` — Open WebUI loads with migrated state.
- Run a query against the retrieval server (via Open WebUI or `curl localhost:8999/query`) and verify it returns results.

## Time budget

| Phase | Time |
|---|---|
| OS provision + SSH | 5–15 min |
| scp tarball (LAN, ~6 GB) | 1–5 min |
| `git clone` + bootstrap phases 1–4 | 2–4 min |
| Postgres restore | 1–2 min |
| Stack startup + image pulls (first time) | 3–8 min |
| Smoke tests | <1 min |
| Workstation reconfiguration | 5 min |
| Verification | 5 min |
| **Total** | **20–45 min** |

## Common failure modes

### Tarball checksum mismatch

Phase 3 aborts with "checksum mismatch for X". The tarball was corrupted in transit or the source snapshot was incomplete.

Recovery: pull a different snapshot, or restore from Arq cloud.

### Postgres restore fails

Phase 5 errors during `pg_restore`. Most common cause: the dump was created with an incompatible Postgres version. Less common: dump is corrupted.

Recovery: investigate the error, do not blindly retry. The DB volume is preserved for inspection. If the dump is unrecoverable, restore from an older snapshot.

### Inference workstation unreachable

Smoke test 5 fails with "retrieval-server /query did not return expected shape". Stack is otherwise up.

Recovery: not a bootstrap bug. Verify:
- Workstation is on; Ollama serving on port 11434
- Workstation firewall allows incoming on 11434 from the VM
- VM can ping the workstation
- `community-brain/config/.env` has correct `OLLAMA_BASE_URL` value (default in the codebase: `http://10.1.50.219:11434`)

### Port already in use

Phase 1 errors that 5678/8999/3000/5432 is already bound. Some other service is on the VM.

Recovery: identify and stop the conflicting service, or move RecapFlow to different ports (requires editing `docker-compose.yml` and recreating the bootstrap).

### LanceDB data not found by retrieval-server

The container starts but `/query` returns 0 chunks consistently. Likely cause: lancedb tar was extracted incorrectly (one level too deep). Fixed in `bootstrap.sh` via `--strip-components=1` on the lancedb tar extraction. If you're on an older `bootstrap.sh` or ran a manual restore without the flag, re-extract:

```
tar -xf /tmp/recapflow-restore.tar \
  --strip-components=1 \
  -C ~/n8n/community-brain/lancedb/ \
  lancedb/lancedb.tar
```

Then restart the retrieval-server container and retest.

## Out of scope

- Recovering Arq license + repo password (must come from operator's password manager).
- HDD provisioning if the original is dead.
- Reconfiguring the inference workstation (separate runbook).

## Test the procedure (recommended)

Quarterly, run the full DR rehearsal on a throwaway VM. See `dr-rehearsal-operator-checklist.md`.

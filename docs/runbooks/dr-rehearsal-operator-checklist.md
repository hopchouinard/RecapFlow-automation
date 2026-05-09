# DR Rehearsal — Operator Checklist

This checklist is for the actual end-to-end DR rehearsal that requires
provisioning a throwaway VM. Run quarterly (or before major changes
to the snapshot/bootstrap scripts) to validate DR confidence.

The "logical" DR validation (Task 4.3 of operator-tier packaging) verifies
snapshot integrity, manifest checksums, and restore mechanics against temp
paths. It runs as part of the packaging validation pipeline. This checklist
covers the next layer: actually running `bootstrap.sh` end-to-end on a fresh
VM, exercising Postgres restore, Docker stack bring-up, and smoke tests.

## Pre-requisites

- Proxmox access to create a throwaway VM
- Latest snapshot on workstation boot volume: `~/RecapFlow-backups/staging/latest/`
- ~30 min budget (one full bootstrap run)

## Steps

1. Provision a throwaway Ubuntu 22.04 LTS or Debian 12 VM on Proxmox.
   - Username: `pchouinard` (or any sudo-capable user)
   - SSH access enabled
   - 2 vCPUs, 4 GB RAM, 30 GB disk minimum (snapshot is ~6 GB; needs headroom)
   - LAN routing so it can reach the inference workstation on port 11434

2. On workstation, pack a fresh tarball from the latest snapshot:
   ```
   tar -cf /tmp/recapflow-rehearsal.tar \
     -C ~/RecapFlow-backups/staging/latest/ .
   ```

3. Transfer to the throwaway VM:
   ```
   scp /tmp/recapflow-rehearsal.tar pchouinard@<throwaway-vm>:/tmp/
   ```

4. SSH in and clone the repo:
   ```
   ssh pchouinard@<throwaway-vm>
   git clone https://github.com/hopchouinard/RecapFlow-automation
   cd RecapFlow-automation
   ```

5. Run the bootstrap:
   ```
   ./scripts/bootstrap.sh /tmp/recapflow-rehearsal.tar
   ```
   First run may exit code 2 with "log out and back in" if Docker was just
   installed. Log out and re-run. Subsequent runs proceed through all 8 phases.

6. Verify smoke tests pass:
   - `http://<throwaway-vm>:5678` shows n8n with workflows
   - `http://<throwaway-vm>:8999/health` returns 200
   - `http://<throwaway-vm>:3000` shows Open WebUI with migrated state
   - A retrieval-server `/query` returns chunks (proves LanceDB restored AND
     LAN connectivity to inference workstation works)

7. Tear down the throwaway VM. The successful rehearsal IS the deliverable —
   you don't need to keep the VM around.

## What success looks like

- All 8 phases of bootstrap.sh complete without errors
- All 5 smoke tests in Phase 7 pass
- Browser verification of n8n and Open WebUI shows the migrated state
- Total time from "fresh VM with SSH access" to "working stack": 20-45 min

## What failure looks like (and what to do)

- **Tarball checksum mismatch**: snapshot is corrupted; pull a different one or
  restore from Arq cloud.
- **Postgres restore fails**: investigate the error; the DB volume is preserved
  for forensics.
- **Smoke test 5 (retrieval query) fails**: usually means LAN routing or
  workstation Ollama unreachable. Check `community-brain/config/.env`
  OLLAMA_BASE_URL value, check workstation firewall.
- **LanceDB not found at startup**: verify extraction landed at
  `community-brain/lancedb/nomic-v1/` (not nested at
  `community-brain/lancedb/lancedb/nomic-v1/`). The bootstrap uses
  `--strip-components=1` to remove the `lancedb/` prefix from the tar;
  if you see the nested path, the bootstrap version predates that fix.

## When to run

- Quarterly: just for confidence
- After major changes to `bootstrap.sh`, `snapshot-vm.sh`, or `docker-compose.yml`
- After upgrading n8n, Postgres, or LanceDB to a new major version (DB compat
  changes are the most common DR-breaking changes)

## Notes on the logical DR validation (Task 4.3)

The following was validated as part of Task 4.3 (2026-05-08) without a throwaway VM:

- `manifest_verify` passes against the HDD snapshot staging dir
- `n8n-state.tar.zst` extracts to expected top-level dirs: `data`, `historical`,
  `n8n-state`, `output`, `watch`
- `data/config` (encryption key) extracts with mode 600, size 84 bytes
- `lancedb.tar` extracts cleanly with `--strip-components=1` to
  `community-brain/lancedb/nomic-v1/` (97,348 files)
- Secret files install with mode 100600 (owner read/write only)
- OpenWebUI tar has expected structure: `webui.db`, `uploads/`, `vector_db/`,
  `cache/` (845 entries in this snapshot)
- Postgres dump: `file(1)` reports "PostgreSQL custom database dump - v1.16-0";
  magic bytes `PGDMP` confirmed

A bug was found and fixed during this validation: `bootstrap.sh` was missing
`--strip-components=1` on the lancedb tar extraction, which would have caused
the Docker volume mount to see an extra nesting level and fail to find the DB.
Fixed in the same commit as this runbook.

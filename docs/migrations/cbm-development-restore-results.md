# Coordinated development snapshot restore — 2026-09-10

Restored the existing private VM 108 snapshot
`weekly-snapshot-20260909T230655Z` into fresh disposable PostgreSQL and extracted
files/config/corpus under `/srv/dev-data/workspaces`. All backup file hashes
matched the saved manifest before restoration.

The test used an internal Docker network without external routing or published
ports. Credentials were disposable fixture credentials; no provider keys or live
service tokens were supplied. No worker or model/publication handler ran. The
original development containers and state were unchanged.

## Verification

- Four jobs, six sources, 15 artifacts and 32 successful processing ModelCall rows
  restored from PostgreSQL.
- Every source/artifact hash and byte length matched its restored storage object.
- All 32 referenced model responses matched their stored hashes.
- Restored LanceDB contained 38 chunks, all with 768-dimensional embeddings.
- The weekly processing job retained success and no requested Git/distribution
  publication. Its indexing stage was queued/pending, exactly as expected because
  the snapshot predates the separate weekly-corpus exercise. It was not replayed.
- No provider calls, queue replay or model retries occurred.

The disposable database, extracted private copies, temporary credentials and
internal network were removed after verification. Original archives remain.
Metadata evidence is VM 108
`/srv/dev-data/artifacts/cbm-live-development-20260909/weekly-restore-result.json`.
Rehearsal helpers are `restore_completed_weekly.py` and `check_restored_weekly.py`
in `deploy/community-brain/live-development/`; Ruff and diff checks passed.

This verifies the saved development dataset and restore integrity. It does not
verify production archive completeness, external PostgreSQL PITR/ACLs, a fresh
consumer installation, or the later weekly corpus snapshot as one coordinated
recovery point. The previous synthetic rehearsal separately covered queue loss
and simulated recovery. Production data restoration remains a separate gate.

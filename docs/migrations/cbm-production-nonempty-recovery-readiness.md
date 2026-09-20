# Paired nonempty recovery verified

September 10, 2026. Mac management completed the continuation requested by
`cbm-production-bounded-worker-results.md`. No worker, private API, provider call,
queue consumer or job submission was started during this recovery check.

## Database acceptance

A fresh scoped dump restored successfully into a disposable PostgreSQL database
with ordinary connections disabled and PUBLIC CONNECT revoked. Only the existing
local PostgreSQL administrator performed the restore; no queue or provider
credentials were supplied.

All ten table definitions, grants, owners, exact row counts and full-row content
hashes matched production. Revision is `0001_jobs`; owners are
`cbm_prod_migration`. Production schema, counts and full-row hashes were unchanged
before/after dump and restore, and checked again after file-reference verification.

| Table | Restored rows |
|---|---:|
| `alembic_version` | 1 |
| `cb_artifacts` | 9 |
| `cb_attempts` | 2 |
| `cb_jobs` | 2 |
| `cb_model_calls` | 14 |
| `cb_operations` | 2 |
| `cb_outbox` | 4 |
| `cb_rejected_events` | 0 |
| `cb_sources` | 3 |
| `cb_stages` | 10 |

Verified jobs:

- Weekly `f6e9abed-e862-4eb7-a231-e98467adcaba`: eight successful model responses.
- Transcript backfill `91d77409-afed-4625-97cb-748c8b637991`: six successful responses.

Each job has processing succeeded on its first attempt and artifacts ready.
All nonprocessing stages have zero attempts. Both indexing outbox records remain
unsent; the two processing records retain their original sent state. All queued
work remained inert. The disposable database was removed.

## Paired file acceptance

Pinned archive SHA-256:
`8e0ae8cf17ebeea4e0248422fdea4f79eb7ea455fc3b4194e05b1622d8ac4941`.

Independently extracted all 53 files into a fresh private temporary directory,
rejecting links, special entries and unsafe paths. All 53 sizes/hashes matched the
pinned manifest. **All 26 restored database references matched extracted bytes**:
three sources, nine artifacts and fourteen model responses. Detailed reference
IDs, paths, expected hashes and pass results are in the companion JSON.
The temporary extraction was removed; original archive/evidence and live
files/config/corpus hashes remained unchanged. Only the public API and Alloy
were running before and after the file check.

## Recovery artifacts

- DB host dump: `/var/backups/community-brain/20260910T033129Z.dump`.
- Verified VM109 copy: `/srv/community-brain/db-backups/20260910T033129Z.dump`.
- Dump size: 52,127 bytes.
- Dump SHA-256: `9543dbb6eeb49ab7c8a6b37420e0514a2461e24f3924a6ce3f0cc7cf2bb1c60b`.
- Original archive, file manifest and new `paired-recovery-manifest.json`:
  `/srv/community-brain/artifacts/cbm-bounded-production-20260910/` on VM109.
- Completed PBS snapshot: `pbs:backup/vm/109/2026-09-10T03:32:39Z`.
  It captures the paired dump copy, archive, manifest and managed state.

This verifies a nonempty logical database/files recovery pair. It does not claim
a full guest restore, PITR, resumed queue delivery or semantic-quality acceptance.
Cutover, publication and retirement remain gated; the CBM-10 quality backlog
remains open. Unused provider allowance grants no additional execution.

Public companions:

- `cbm-production-nonempty-db-restore-receipt.json`
- `cbm-production-paired-file-reference-receipt.json`
- `cbm-production-paired-recovery-manifest.json`
- `cbm-production-nonempty-backup-copy-receipt.json`

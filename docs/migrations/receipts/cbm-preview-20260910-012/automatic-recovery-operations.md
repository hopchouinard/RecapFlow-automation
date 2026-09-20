# Automatic processing and recovery operations

Request `CBM-AUTOMATIC-20260910-011` activated the future-submission loop on
2026-09-10 at 20:36:53 UTC. Forge independently verified activation and Patrick
accepted the form. Request012 subsequently changes only the frontend and its
recovery pins. Secrets remain authoritative in Infisical; the Mac renders separate
private service bundles. No Infisical management login is installed on VM109.

The VM minute cron invokes the boot guard and the pinned automatic host. Only
new root submissions carrying `new-meeting-full-loop-v1` are eligible. Historical
jobs and three old unsent outbox events remain untouched. The worker uses the
existing US$2 lifetime OpenRouter cap, with no reset or top-up. Publication,
existing-session replacement and service retirement remain gated.

The Mac LaunchAgent `lab.patchoutech.community-brain-management` invokes
`~/.local/lib/community-brain-management/maintain.py` every minute. It serializes
execution with `~/.local/state/community-brain-management/scheduler.lock`, runs
the recovery consumer, and preserves hourly maintenance plus the 20:45 local
pre-PBS copy. The normal 21:00 backup schedule and retention are unchanged.

## Recovery acceptance

The consumer holds runner, manual-worker and submission locks in that order via
an SSH heartbeat lease. Retrieval stays available; writes return503 during the
quiet window. It records intent before capture, database restore, file restore,
off-host copy, PBS backup and final verification. Only actual matching evidence
permits the holder to acknowledge the checkpoint and remove its pending marker.
An uncertain external effect must be reconciled, never blindly repeated.

Private evidence lives in:

- Mac: `~/.local/state/community-brain-management/automatic/{journal,evidence}/<job>`.
- VM109: `/srv/community-brain/artifacts/automatic/<job>` and
  `/srv/community-brain/automation/checkpoints/<job>.json`.
- platform-db: `/var/backups/community-brain/automatic/<job>/`, with the matching
  transferred set under `paired/`.
- PVE1: `/var/lib/community-brain-automatic-pbs/<job>/`, including persisted UPID.

The VM's `community-brain-automatic-pause.service` forces pause on each boot or
restore. Inspect the boot identity, actual jobs, queue and checkpoint evidence
before explicit reconciliation. Never clear attention or pending markers merely
to restart progress. The five Prometheus rules cover stale management, stale
host ticks, attention, pause and prolonged pending checkpoints.

## Deployment controls and rollback

The current frontend is
`/srv/community-brain/workspaces/cbm-preview-20260910-effective/dist`.
The automatic backend remains the immutable
`cbm-automatic-20260910-effective-s01` packet. The installed Mac
`integrations/manual_api_runtime.py` pins both manifests and the manual Compose
runtime. API recreation must use fresh Infisical values through that renderer.
Do not restore a stale `api.env` or silently switch to an older renderer.

Request012 retains all previous hashed assets and includes its active frontend
in `files_adapter.py` recovery inventory. Private before/after deployment controls
are at `/srv/community-brain/artifacts/cbm-preview-20260910-012/{before,after}/`.
Their matching verified off-host copies are on platform-db at
`/var/backups/community-brain/preview-deployment-012-{before,after}/`; the Mac has
the paired management bundles in
`~/.local/state/community-brain-management/preview-012/{before,after}/`.
The `before` copy also closes the outstanding postactivation control preservation
for request011, without replaying its activation.

For a frontend rollback, acquire the same ordered quiet lease and Mac scheduler
lock. Restore only the reviewed prior Compose/static-manifest/renderer pins from
the private before controls, preserving automatic backend and recovery guards;
render fresh identities and recreate the API. Verify HTTPS, auth, retrieval and
unchanged data before releasing the lease. Do not roll back database or corpus
for a frontend regression. The legacy retrieval window remains terminally
superseded; never invoke its original rollback script. No deadline was extended.

## Validation limits

79 local tests pass. The disposable six-phase rehearsal exercised native
PostgreSQL, LanceDB/FTS, SSH copies and lock acknowledgment; its Auth/PBS boundaries
were fixtures. Native database restore and corruption rejection passed separately.
No new production job, paid call, new job-linked PBS snapshot or full guest restore
was performed to certify activation. Production acceptance instead verified idle
eligibility, preserved database/files,1901 indexed rows, scoped API behavior,
archive downloads and active controls. Each future job must obtain its own real
paired recovery receipt before automatic progress continues.

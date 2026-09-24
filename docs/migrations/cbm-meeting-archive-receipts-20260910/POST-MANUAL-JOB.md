# Required management step after each accepted manual job

Owner: Mac management. This procedure is part of manual operation, not an
automatic queue consumer. It owns corpus lint/recovery inspection and backup
coordination; the old mutating lint, snapshot-push and artifact-push schedules
stay disabled. No network publication is included.

## Additional read-only archive recovery inventory (request009)

Every future recovery inventory must include
`/srv/community-brain/meeting-archive-20260910/` (manifest.json plus all481 files).
Its pinned manifest SHA256 is
`3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00`.
Capture and restore it with the active source/static packet
`/srv/community-brain/workspaces/cbm-archive-ui-20260910/`, the effective manual
Compose/runtime manifest and the pinned Mac manual_api_runtime.py. Validate all
481 restored file hashes/bytes and catalog87-date coverage in an isolated directory
before accepting recovery. Keep this archive read-only; never regenerate historical
content to fill a missing recovery file. Missing archive/pin/control coverage stops
acceptance. Existing request006 paired checkpoints retain their original scope;
request009's verified private supplemental archive carries this additional history.
See ../meeting-archive/receipt.md for off-host copies and exact control bindings.

## Per-job procedure

1. Open a new scoped management handoff naming the completed job/stage/generation
   and the accepted artifact evidence. Require an unambiguous durable outcome;
   uncertain provider/worker effects go to reconciliation, never blind rerun.
   Confirm all selected workers exited, the manual lock is free and manual intake
   is idle. List inert outbox events explicitly. Do not dispatch them.
2. Under a new private directory `/srv/community-brain/artifacts/<request-id>/`,
   capture regular-file manifests of `files`, `config`, `corpus`, both active
   runtime packets and `manual-approvals`, including `.started` markers. Record
   sorted relative paths, sizes and SHA256; reject links/special files. Capture
   separate managed-state and manual-runtime-state archives and verify every
   member against those manifests. Keep private logs/content out of relay files.
3. On platform-db, collect deterministic full-table row hashes, counts, schema,
   owners and grants from `community_brain_prod`. The `state()`/`schema()` logic
   in ../manual-recovery/check-database.py is the reference. Start only the
   existing `community-brain-db-backup.service`, identify its newly completed
   custom-format dump, verify its archive listing/checksum, and compare live
   database state again. Recheck the VM109 manifests immediately afterward.
   Any DB or file drift stops pairing; retain evidence and establish a new quiet
   window. Never label separate unverified captures simultaneous.
4. Restore that exact dump to a new disposable template0 database with connection
   limit0 and PUBLIC CONNECT revoked. Compare every application table's exact
   records, schema, owners and each required runtime privilege. Derive all source,
   artifact and model-response file references from the restored database.
   Restore both archives to new private directories, reject unsafe tar members,
   verify every file and every DB reference/hash/size. Check the restored corpus
   and FTS using the pinned image, network=none, read-only mounts and no provider,
   queue or submission credentials. Preserve the real pending-outbox state;
   a fresh queue is required on deliberate application recovery.
5. Recompare current DB/files/runtime manifests before accepting the pair. Remove
   only the disposable database/container/directories after receipt capture.
   Build a paired manifest binding dump, archives, manifests, exact DB fingerprints,
   reference counts, runtime/approval identities, timestamps and consistency limits.
   Today's 3-job/50-reference/79/42-file helpers are fixed-request examples; do not
   rerun their captured assertions against a later job. Prepare successor helpers
   with the new baseline and review their target paths before execution.
6. Copy the exact dump to VM109 `db-backups`, and copy the paired dump/archives/
   manifests off-host to a new root0700 directory below platform-db
   `/var/backups/community-brain/`, using the existing Mac SSH path. Verify received
   sizes/checksums, root0600 files, and retention of prior checkpoints. Take an
   associated VM109 PBS snapshot after the copied set is present, preserving
   existing backups. Record snapshot ID, included disks and freeze/thaw result.
   A logical restore check is not a full guest restore or PITR claim.
7. Return the immutable request receipt and manifest hashes. Record semantic
   artifact acceptance and any canonical-index acceptance separately; a collision
   with an existing session needs its own replacement decision. Each new accepted
   manual state requires this procedure until a reviewed paired-backup automation
   replaces it. Routine nightly dumps/PBS snapshots alone do not satisfy it.

Stop conditions include active writers/intake, lock contention, uncertain stage
outcome, missing/malformed manifests, source drift, missing references, wrong
schema/grants, copy mismatch, unavailable management host or failed restore/PBS.
Keep current production data and previous recovery points intact on failure.

## Dated identity renewal responsibility

Mac management must arrange explicit renewal before the first applicable expiry:
Open WebUI retrieval September17 03:52:50UTC; collector/operator05:03:42UTC;
read/metrics probes06:22:56UTC. Infisical authority metadata is checked hourly;
Prometheus warns within72h and is critical within24h or after expiry. Mac metadata
older than2h is separately visible. Recheck actual authority before each renewal.
Preserve each caller's exact permissions and use old/new acceptance overlap with
coordinated private consumer replacement, then revoke old hashes and verify denial.
Never reuse request006's one-time rotation journal or rotate provider keys as part
of service-token renewal. No autonomous extension or spending-cap change exists.

## Nightly copy ordering

The existing Mac LaunchAgent retains hourly maintenance and also runs at20:45
America/Toronto. Its first task has a210-second ceiling: inspect a successful,
completed dump no older than2h, copy it, and verify source/copy checksums before
20:55 (at least5min before the unchanged21:00PBS job). The next freshness deadline
advances only after a successful scheduled check. An out-of-window rehearsal
cannot advance it. Failure preserves the old deadline and sets an explicit failed
state. The first future calendar execution remains to be observed; live transport
rehearsal and summer/winter/failure tests establish present readiness.

The Mac/user session/network remain dependencies. A sleeping Mac cannot copy;
server-scraped status age and overdue/failed-copy alerts expose that loss of
coverage. PBS is never disabled to conceal it. Existing retention and other VM
schedules are unchanged. Nightly copies are not automatically quiescent pairs.

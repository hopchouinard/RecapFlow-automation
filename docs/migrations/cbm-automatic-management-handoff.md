# CBM-AUTOMATIC-20260910-011

Patrick explicitly answered **“Do the full loop”** after requesting that saving a
new meeting start processing. Request010 is completed and acknowledged. This
request authorizes deployment and activation for future new submissions:
selected Fathom acquisition when needed → recap Markdown → new-session indexing
and FTS → paired recovery checkpoint. Remote publication, existing-session
replacement, recurring Fathom discovery, retirement and final-quality changes
remain gated. Do not create a synthetic production job or replay historical work.
No new user confirmation is needed for routine implementation within this scope.

## Exact reviewed packet

VM109 `/srv/community-brain/workspaces/cbm-automatic-20260910/` contains the
manifest-bound Python helpers, jobs modules and dist. The companion
`cbm-automatic-manifest.json` is an exact copy of packet-manifest.json. Image stays
`community-brain@sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449`.
The rehearsal/ directory contains fake providers and is **test-only**, never mount
it or its environment in a production workload. All runtime paths below refer to
this packet. Keep its immutable source manifest intact; record any effective
merged static manifest separately.

Canonical verification passed:150 Node,907 Python,41 private PostgreSQL/JetStream,
4 frontend unit/component and3 browser tests. The VM108 image rehearsal uses
an internal-only disposable Docker network, private PostgreSQL/JetStream, actual
LanceDB ingestion/FTS, fake model/Fathom/embedding boundaries, no real keys and no
external calls. Its separate receipt reports exact stages and searchable rows.
Both new source paths complete; new files enter the catalog and hash-verified
content endpoints; duplicate submission does not run again; old outbox stays
untouched and the first fixture's rows survive the second fixture unchanged.

## Runtime behavior

The API assigns `config.automation_policy=new-meeting-full-loop-v1` only inside
acceptance of a new root job when CB_AUTOMATIC_PROCESSING=true. Old idempotent
returns and reruns never opt in. A scoped PostgreSQL date advisory lock plus fresh
LanceDB/session-reservation lookup rejects a date already indexed or submitted.
The schema is unchanged. The existing87 meetings/1901 rows are protected.

The root launcher `automatic_host.py` runs as a cron tick, with a nonblocking
exclusive runner.lock and only scoped generation1/attempt0 stages. It never calls
ordinary serve/recover/dispatch. It invokes existing selected-stage inspect and
execute oneshots. Selection is revalidated against the new policy and corpus
before every execution. Old3 unsent indexing events are not eligible. Orphaned
labeled containers and the manual-worker lock block another launch. Durable
.started markers are fsynced before launch. Expired leases fence work into
outcome_unknown; errors persist attention.json. No automatic retry, generation
bump, model reconciliation or marker clearing is allowed.

Acquisition receives only the existing Fathom key; processing/indexing receive
only the existing dedicated model key, plus scoped PG/NATS as required. Scanner
has only runtime PG access and read-only corpus/config. API has no model/Fathom/
queue key. No management credentials enter workers. The existing per-call
allowance checks,20 processing-request and32 indexing-request ceilings remain.
Recheck the provider's actual **US$2 non-resetting total cap** before activation;
last usage $0.392107166, remaining $1.607892834. No key rotation/top-up/reset.
Exhaustion stops for review; an arbitrary larger weekly call is not guaranteed
to fit the remaining balance or request ceilings.

Indexing alone gets corpus/config writes; all workers get immutable packet
mounts, read-only rootfs, UID10001, no capabilities, no-new-privileges and resource
limits. Network publication remains explicitly false. The indexing handler uses
existing new-session reservation, artifact materialization, request journal and
FTS coverage checks. Open WebUI queries reopen the current table. API catalog
merges ready new job files with the preserved archive without changing its manifest.
The UI's automatic wording is conditional on /me. Selected-run progress and the
meeting catalog refresh every15 seconds without another submission/model call.

## Automatic paired recovery hook — complete before enabling submission policy

Adapt the existing Mac maintenance/POST-MANUAL-JOB mechanism into a reviewed
idempotent consumer of `/srv/community-brain/automation/checkpoint-needed.json`.
The launcher creates this only after a new automatic job has indexing=complete,
and refuses to launch another job until its verified checkpoint is acknowledged.
Use the existing management scheduler/access; no new secrets or third-party stack.
The former requirement to open a fresh human handoff for every job is replaced
by this exact job-ID-bound hook. All substantive pairing/restore/off-host checks
from POST-MANUAL-JOB remain required, including PBS before acknowledgment.

For each marker, establish a real quiet window on VM109: acquire exclusive
`automation/runner.lock`, exclusive `files/.manual-worker.lock`, then exclusive
`files/.submission.lock`, holding them through all live DB/files fingerprint and
capture comparisons. Use nonblocking locks and retry later on contention, never
kill writers. API mutating requests hold a shared submission lock; contention
returns503 checkpoint_in_progress_retry_shortly. GET reads stay available. The
management process must abort acceptance if its remote lock holder is lost.
Do not truncate lock files, replace their inodes, or archive an active file writer.

Require the named job's unambiguous complete stage result and no automatic worker
container. Capture the exact new DB/files/config/corpus pair, all DB references,
full FTS, preserved archive, active source/static/renderer/cron/policy controls and
manual approvals/.started journals. Use dynamic counts and row fingerprints, not
old fixed3-job/50-reference assertions. Restore only disposable copies, verify
exact records/privileges/references/hashes, preserve all existing sessions, copy
privately off-host and include the copied set in the associated PBS snapshot.
Keep previous recovery points. No source/model reprocessing occurs in backup.

After success write root0600 atomically:
`automation/checkpoints/<job-id>.json` containing job_id, verified:true,
manifest_sha256 (the64-hex immutable paired manifest hash), receipt/path and time.
Only then remove the matching checkpoint-needed.json under the held runner lock.
Validate the manifest and actual copied set before acknowledgment, not just JSON
shape. Never acknowledge a different job, partial copy, failed restore or unknown
outcome. Recovery of this automation itself must start paused until DB/queue/
corpus/markers are reconciled; don't let restored cron blindly run stale events.

Test this hook with disposable data/control fixtures before activation, including
lock contention, intake mutation denial, holder death, repeated marker delivery,
wrong job/manifest, failed capture/restore/copy/PBS and restart after each boundary.
If the current management access cannot complete the hook, return the concrete
blocker and leave automatic activation held. Do not weaken recovery silently.
Existing Mac sleep/network dependencies must remain visible in monitoring.

## Deployment order and verification

1. Preserve current API overlay, renderer, pins, frontend, Authentik policy and
   runtime controls privately/off-host. Validate the new packet and current state.
   Do not overwrite immutable earlier packets or restore stale api.env.
2. Prepare root0700 automation/ and checkpoints/. Pre-create both files locks as
   UID10001:GID10001 mode0600 (or preserve their existing inode/ownership). Keep
   packet source directories755/files644 under private host ancestors so UID10001
   can read the exact bind mounts. The root cron/helper needs no secret in argv.
3. Install and verify the management checkpoint hook and monitoring first. Record
   host status age, attention state and pending-checkpoint delay in existing
   monitoring; don't conceal failed or stalled work behind API health.
4. Update the current Infisical-rendered API recipe to bind this packet's api.py,
   store.py,runtime.py,archive.py,automatic.py over the installed jobs modules.
   Keep existing manual.py/worker.py packet usage for earlier manual recipes.
   Set CB_AUTOMATIC_PROCESSING=true and CB_CORPUS_ROOT=/state/corpus. Bind new
   dist read-only, retain all earlier hashed static URLs, update effective pins.
   Preserve archive root/pin, hidden synthetic IDs,13 cue rules, read-only corpus/
   config, scoped identities and Patrick's exact established Authentik mapping.
5. Install one cron entry invoking `/usr/bin/python3 <packet>/automatic_host.py`
   each minute as root, with private bounded/rotated logs. It runs up to3 sequential
   stages then exits; overlapping ticks exit via flock. No general worker, no
   new always-running application container, no startup replay. First activation
   must see0 eligible jobs and leave all3 old outbox events untouched. A paused
   initial cron can be validated before enabling the policy; unpause only once
   the whole submission/worker/checkpoint path is ready.
6. Verify HTTPS root/callback/current+retained assets, human/service permissions,
   /me capability,87 preserved meetings/481 files, real job/synthetic hiding,
   retrieval/FTS, model allowance, idle host scan and scope separation. No test
   production upload/submission is needed or authorized. Exclude newly created
   empty lock/control files from preexisting-content invariance checks explicitly;
   all actual DB/source/artifact/corpus/config/archive content must be unchanged.
   Keep terminal legacy ownership, old writers/intake held and publication false.
7. Copy new runtime and management automation controls off-host; update active
   recovery inventory/runbook, automatic recovery pause and receipt. Preserve
   old paired checkpoints and current grants/authority. On validation failure,
   pause new cron, restore reviewed prior API/static policy with current secrets;
   don't undo new accepted jobs/data or clear execution markers. Report any
   accepted work that needs reconciliation instead of attempting rollback replay.

Return safe receipt hashes, exact installed controls, checkpoint-hook tests,
initial idle scan/old-event invariance, budget, health/auth and recovery coverage.
Forge will verify and ask Patrick to use the form for a genuinely new meeting
when one exists. All87 historical meetings are already indexed; don't request
one for reingestion or fabricate a September10 meeting for acceptance.

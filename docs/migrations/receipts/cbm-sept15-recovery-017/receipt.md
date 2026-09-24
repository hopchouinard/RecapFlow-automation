# Request017 completed: September15 recovery checkpoint

Request: CBM-SEPT15-RECOVERY-20260915-017
Actor: home.servers
Completed: 2026-09-17 UTC
Job: 744d0f3f-8da7-4c12-bc15-5ec0a046518d
Paired manifest SHA-256: df1ce04cd7a15e38cc21e1be5fc3ee1fd931489f7a66a351705a6e248970684e

## Result

The exact existing checkpoint is durably acknowledged. Production runner and
Mac scheduled consumer both returned to idle. Monitoring reports enabled=true,
paused=false, pending=false, attention=false. Only the resolved management
attention marker was archived, after the matched acknowledgment was durable.

No processing, indexing, acquisition, publication, provider/model calls, new job,
new PBS backup, credential rotation, or legacy ownership/permission change was
performed by this intervention. Request016's stopped Mac permission work remains
stopped. User-facing production content was already available.

## Root cause and repair

The existing automatic consumer DID run. Capture, database restore, file restore,
and off-host copy phases had completed before it failed in the PBS phase.
The pvesh CLI runs vzdump synchronously and streams worker logs before its final
JSON UPID result. pbs_adapter.api called json.loads on the whole stdout stream,
so a successful PBS task left both management and PVE journals at intent.

Installed a narrow parser repair on PVE1 and in the Mac management library:
only the exact create /nodes/pve1/vzdump call parses the last nonempty output
line as JSON, then validates a PVE1 vzdump VM109 UPID. Other API reads remain
strict JSON; nonzero exit and missing identity remain failures. No automatic
retry was introduced. Four regression tests reproduced the original failure
then passed against the fix. No new live backup was submitted to test it.

Before hash: c2b7bde0f479178c061ef49da4711c8540c70786ddb5b2df29bd6c3097dc134d
After hash: 1a443da18c050e8b77d9177010be0a48859f125c5d467bc842068e76addf4f0e
PVE backup: /usr/local/lib/community-brain-automatic/pbs_adapter.before-request017.py
Mac backup: /Users/pchouinard/.local/state/community-brain-management/request017/pbs_adapter.before.py
Restore those files to roll back only the parser repair; do not recreate a
pending checkpoint or roll back completed journals.

## Reconciliation, not replay

Matched original task UPID:pve1:001E1CBC:0FED0E1D:6AA9D98C:vzdump:109:root@pam:
to snapshot pbs:backup/vm/109/2026-09-15T23:49:32Z by task logs, exact job and
manifest notes, successful completion, both included disks and guest freeze/thaw.
Original operation.json was preserved as operation.before-request017.json before
recording the recovered UPID and reconciled_complete state. Original management
PBS intent was preserved locally before completing it with actual task evidence.

The ordinary strict resume path had two additional reconciliation obstacles:
1. Nightly retention later logged two prunes. Two prior September10 snapshots
   are now absent. The checkpoint task itself used --remove 0 and logged no
   prune; its September15 snapshot still exists. This is explicitly recorded in
   the PBS receipt, not concealed by changing the original snapshot inventory.
2. Four operational files changed while the marker waited: execution.log,
   execution.log.1.gz, management-attention.json and status.json. An explicit,
   one-job reconciliation accepted exactly these four measured differences;
   any other filesystem difference would fail. The attention content and
   awaiting_checkpoint state were matched exactly. General-purpose retention
   and filesystem guards were not weakened.

Under the existing Mac scheduler mutex and supervised runner/manual/submission
quiet locks, reverified BOTH off-host and VM copies against the original paired
manifest, the live PostgreSQL schema/owners/grants/rows/sequences/references,
all application/config/runtime files, corpus, preserved archive, host controls
and Authentik controls. Existing actual restore receipts prove 921 filesystem
entries, 72 references and disposal of the test database/filesystem restore.
Corpus still has 88 sessions, 1924 rows, complete FTS with zero unindexed rows.

Stored the matched PBS receipt and detailed reconciliation evidence with the
pair on both VM109 and the off-host database server. Completed the journal
phases only after these checks, then used the EXISTING quiet-window acknowledgment
handler, including its full VM-side paired-evidence validation. No marker was
cleared before successful acceptance.

Acknowledgment: /srv/community-brain/automation/checkpoints/744d0f3f-8da7-4c12-bc15-5ec0a046518d.json
VM evidence: /srv/community-brain/artifacts/automatic/744d0f3f-8da7-4c12-bc15-5ec0a046518d/
Off-host evidence: /var/backups/community-brain/automatic/744d0f3f-8da7-4c12-bc15-5ec0a046518d/paired/
Archived attention: request017-resolved-management-attention.json in VM evidence.

## Limits and follow-up

No full guest restore or point-in-time-recovery certification is claimed.
Original restore operations were verified from their hashed receipts and current
live parity, not repeated. PBS task and snapshot verified live. Parser regression
is deterministic; its next real backup invocation has not yet occurred.

The bounded reconciliation script is an incident artifact, not a general resume
command; do not rerun it after acceptance. Its exact-match guards intentionally
reject a completed journal. The recorded PBS retention exception is specific to
this incident. Retrying the original pbs_adapter.inspect on this old checkpoint
still encounters its general preservation guard; use the reconciliation receipt
for historical acceptance. A future generalized resume policy should distinguish
operational logs and independently scheduled retention while retaining data,
identity, ownership and actual backup verification.

The repaired adapter and regression tests are included for Forge to preserve in
its owning source/deployment packet. No git commits or pushes were performed.

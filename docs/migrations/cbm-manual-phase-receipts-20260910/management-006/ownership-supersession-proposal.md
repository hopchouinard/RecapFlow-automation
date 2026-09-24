# Proposed ownership supersession, not executed

Request: CBM-MANUAL-RECOVERY-20260910-006. Return this procedure for Forge's final
readiness review. Request006 does **not** authorize disarming/extending the timer,
changing the rollback controller, releasing immutable guards or retiring services.

## Present verified controls

VM101 n8n is stopped; community_brain_retrieval is paused; both restart policies
are `no`. Open WebUI remains running against the accepted new retrieval URL.
All2867 saved inodes remain immutable. The lint cron file is held privately;
only the snapshot-vm and commit-weekly-artifacts entries are removed from the
user crontab. Original container/cron/flag/valve state remains root-private under
`/var/lib/community-brain-window/CBM-RETRIEVAL-20260910-001/`.

VM109 has only API and Alloy running. Manual V2 workers require explicit selections,
durable start markers and the shared file lock. No ordinary worker/outbox sweep,
publication handler or corpus-mutating schedule is enabled. Three unsent indexing
events remain inert. The real September8 session was not indexed or replaced.

The production Mac collector is manual-only and bound to the selected chat/hash.
The exact legacy Zoom association at `/Volumes/NVMe_2TB_Work/Documents/Zoom` stays
disabled; `com.patchoutech.sync-zoom-chats` stays unloaded. Existing scripts and
development configuration are retained. No recurring production collector exists.

VM101 rollback timer remains enabled/active, calendar01:25UTC September11 plus
OnBootSec45/Persistent. Hard deadline is01:30UTC. Controller:
`/usr/local/lib/community-brain-window/window-control.py`.
Mac resume hook: `~/.local/lib/community-brain-management/mac-intake.py`, invoked
by the existing hourly maintain.py. **Both must be superseded together.** Stopping
the timer alone leaves boot/manual execution and the stale Mac restore path.

## Concrete follow-up procedure

1. Require a new immutable handoff naming the accepted recovery/ownership receipt
   and its existing phase approval. Recheck source/target identity, no running
   workers/manual intake, current jobs/outbox, active retrieval, backup paths and
   deadline. Do not begin near the rollback window without sufficient time to
   finish and verify. If final readiness is absent, let existing rollback run.
2. Preserve byte-for-byte private copies of VM101 controller/service/timer/state
   and Mac hook/maintain/state, with hashes and modes. Keep the original restoration
   material and old services/data/backups; do not overwrite commissioning evidence.
3. Prepare and test the exact controller/hook changes in disposable state. Retain
   current deadline behavior until an explicit durable supersession record exists.
   Add a fixed-request terminal `superseded` state that refuses automatic **and
   `--now`** legacy restoration; it must never set mac_resume_allowed. Use one
   shared lock for rollback and supersession, and check the terminal marker while
   holding it. Test timer/boot/manual calls, repeats, missing/corrupt markers,
   interrupted application, stale old status and unreachable management peers.
   A malformed or uncertain state must keep writers/intake disabled and report it.
4. Install the tested Mac hook before any supersession marker. It must preserve
   today's verified rollback behavior until the server reports the fixed-request
   supersession, then permanently refuse old intake auto-resume, even with stale
   local state. Match the saved association by exact path after enumeration.
   Install the tested VM101 controller while its rollback deadline still works.
   Under the shared lock, verify no rollback is active and atomically record the
   accepted ownership request/receipt hash, `phase=superseded`, legacy writers
   disabled, and `mac_resume_allowed=false`. Verify both sides before cancellation.
5. Only after that durable terminal state passes timer/boot/manual no-op checks,
   disable the exact cbm-retrieval-deadline.timer and mask the timer **and service**
   (preserving unit definitions privately). Record inactive/disabled/masked state
   and verify stale direct controller invocation cannot restore old writers.
   Update the Mac maintenance label/status to report the new held ownership state,
   while retaining certificate and backup jobs. No other system unit changes.
6. Keep n8n stopped and old retrieval paused/stopped with restart=no; keep their
   exact legacy cron entries absent and Mac Folder Action/LaunchAgent disabled.
   Leave immutable flags in place unless a specifically justified later change
   requires removing a bounded subset. There is no need to unlock old data to run
   VM109. Record explicit no-manual-legacy-write ownership and verify after boot
   or Compose maintenance; a future legacy Compose recreation must preserve no
   restart and must not be used to resume work casually.
7. Verify new API/TLS/scopes/actual WebUI retrieval, read-only corpus mounts,
   worker exclusion/selection locking, manual intake ownership, latest paired
   checkpoint and monitoring. Recheck that unrelated queue records stayed inert.
   Publish the superseding receipt, concrete manual recovery procedure, hashes and
   residual maintenance gaps. Do not claim live canonical indexing acceptance or
   two-cycle stabilization from this transition alone.

## Deliberate recovery after supersession

Restoring legacy processing becomes a separate controlled management operation,
not a stale timer invocation: stop/drain new submissions and all new workers;
take and verify a fresh paired checkpoint; reconcile any uncertain stage and
new-versus-old corpus differences; choose the data to serve without losing new
work. Verify old retrieval under immutable guards before changing the actual
WebUI valves. Only after accepted old retrieval and single-writer ownership may
the saved legacy flags/cron/container policies and exact Mac intake association
be restored. Never replay today's saved controller wholesale while VM109 can
still write. Keep private restoration secrets in their existing protected paths
and current authority in Infisical.

Publication, existing-session replacement, CBM-09, service/data retirement and
final CBM-10 quality closure remain separate gates. The backup scheduling and
explicit credential-renewal gaps in OPERATIONS.md remain visible to the final
readiness decision; this document does not silently accept them for Patrick.

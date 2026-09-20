# Request024: read-only stabilization diagnosis

Request: `CBM-STABILIZATION-DIAGNOSIS-20260920-024`  
Actor: home.servers  
Completed at: 2026-09-20T02:53:59.470884+00:00  
Outcome: diagnosis and exact current source delivered; no repair or production activation performed.

## Confirmed renewal failure

The deployed `service_renewal_live.py:112` still calls `remote('n8n-automation', webui)` from `check_consumers`. The operation is an SSH command running a read-only SQLite query through `docker exec open-webui python -c ...`. The exact literal inspection was extracted from the current deployed source and reproduced independently, without invoking renewal or its adapter entry points.

- SSH authentication and remote Python execution succeed.
- Inner Docker operation exits **1**, categorized safely as **container_not_running**.
- The remote assertion raises **AssertionError**; SSH returns **1**.
- `secret_store.py:26` deliberately suppresses captured private output and raises the generic **RuntimeError** seen in the scheduler status.
- `open-webui` exists but is **exited**, exit code **0**, stopped at **2026-09-19T04:20:05.394478381Z**. Its last start was September15 at23:40:38 UTC. This diagnosis does not establish who or what stopped it.
- Its data mount remains `/var/lib/docker/volumes/open-webui-data/_data` -> `/app/backend/data`. `webui.db` exists (4,829,184 bytes,0644). A host-side SQLite **mode=ro** query confirms the `community_brain_filter` row exists and is active/global. No valves or credential values were exported.
- Other old-host state: n8n and community_brain_retrieval are stopped; n8n_db is running. Nothing was restarted.

This is a stale live-container dependency in renewal inventory. The stopped consumer still blocks renewal of the entire service-identity set. Restarting the stopped stack or silently dropping a consumer is not an authorized repair.

## Renewal phase and current scheduler state

The authoritative Infisical renewal journal's phase is **completed**. Only its phase was exported. Latest observed scheduler renewal failure is the same six-frame path through policy:53, live:65/live:112 and secret_store:26.

The policy inventories consumers before generating new tokens or saving the next prepared journal. Together with the completed journal, this supports a failure before a new renewal generation is prepared, rather than an interrupted delivery phase. No renewal mode, including `inventory`, was invoked by this diagnosis.

The Mac minute scheduler remains installed and running on its existing schedule. Its observed automatic result is **paused**, monitoring has attention=true, paused=true, pending=false; its most recent hourly maintenance records renewal and management-health as failed. Other listed hourly checks passed. Request024 did not disable or invoke this scheduler. Read-only observations are point-in-time; ordinary scheduled ticks continue independently.

The five identities' September22 20:53:07 UTC expiry and three matching0600 consumer bundles are Forge's request observations, not newly certified by this diagnosis. The existing renewal policy uses seven-day validity and a72-hour lead. Do not treat the failed renewal as an extension of expiry.

## September18 runner error versus September19 boot pause

VM109's preserved attention marker reports **2026-09-18T19:46:24.714428+00:00**, reason `automatic_execution_requires_review`, class **RuntimeError**. It records neither operation, return code nor underlying message.

The current r020 `automatic_host.py` catches the exception, preserves only its class in the first attention marker, and emits only a state summary. Retained cron logs contain idle/paused/attention state JSON and no traceback. The September18 19:44–19:49 UTC journal inspection found no exception class in relevant Community Brain entries. Current execution.log is empty; its compressed predecessor predates this incident (September15), so its older traceback is not evidence for the September18 failure.

**No recorded underlying cause was recovered.** The explicit RuntimeError in the current scanner path is `automatic state inspection failed`, raised on a nonzero scanner subprocess, but the retained evidence cannot prove that was the path or explain the subprocess failure. The old-host OpenWebUI failure must not be presented as the cause of this independent runner incident.

Separately, boot-state.json and paused both identify the current kernel boot ID and boot reconciliation is **false**. The boot guard requires explicit reconciliation after boot/restore. Both pause and attention remain present. No checkpoint-needed or management-attention marker was present in the observed VM109 state.

## Supported reconciliation boundary

The deployed boot guard supports **boot** and **tick**, not a general `reconcile` command. `boot` forces the pause; `tick` enforces the guard and invokes the pinned launcher, including while held for monitoring. Neither is a read-only reconciliation probe.

Existing operator documentation (`automatic-recovery/README.md` and `weekly/README.md` in the operator worktree) establishes this procedure, rather than a validated one-command resume tool:

1. Keep pause and attention intact. Inspect the current boot identity, actual jobs/stages/attempts, queue, manual `.started` markers, running workers, pending checkpoint and private management journal phases.
2. Reconcile uncertain provider/worker/backup effects against durable outcomes. Do not blindly repeat an intent, create a duplicate snapshot, replay an upload, or restore stale credentials.
3. For an approved reconciliation, serialize with the Mac scheduler mutex and acquire the ordered production runner, manual-worker and submission quiet locks through the heartbeat lease. Verify the same boot identity throughout.
4. Verify current runtime/helper pins, fresh credential authority, API readiness and actual paired recovery/checkpoint evidence. Clear only the specifically reconciled condition; a marker's presence is not proof that it is safe to remove.
5. Any candidate implementation, including a safe reconciliation command, must first pass on **VM108**, then be supplied as a concrete production rollout packet for the next authorized phase. Observe subsequent scheduled ticks only after that authorized reconciliation/resume.

There is no currently verified general-purpose deployed utility that establishes all these preconditions and safely changes boot reconciled=false to true. The historical Request016 script is request-specific, not deployed, and tied to different pins/markers; it is not a supported solution for this incident and was not executed. This request does not certify current jobs/queue/checkpoints as safe to resume.

## Current management source and provenance

`management-source.tar.gz` contains **42 exact code/control files**: deployed Mac renewal helpers and recovery adapters, scheduler entry points and safe authentication wrapper code, deployed VM109 boot guard/cron/service and r020 launcher/scanner, and associated repository tests/test support. No `.env`, private journal, database, secret bundle, raw log, or provider output is included. Source literals such as paths and runtime pins are retained unchanged. The archive is a source reference, not an executable rollout packet.

`source-manifest.json` identifies every source path, byte count and SHA-256, plus repository comparisons and local status. The canonical operator repository is `https://github.com/Patchoulab/agent-ops.git`:

- Operator worktree `/Users/pchouinard/.t3/worktrees/agent-ops/forge-inspection-access`, branch `codex/forge-inspection-access`, HEAD **a9dcf247e7aa2176f03fb7319fb1074f0e443acc**.
- The required live/policy/renew entry points, their renewal tests and boot guard match that worktree's **untracked** files. `secret_store.py` is tracked and matches HEAD/worktree. Runtime renderer and lease helpers match **modified** tracked files.
- The separate main checkout at `/Volumes/NVMe_2TB_Work/Development/AOE/act/Home.servers/agent-ops` is HEAD **0e75c3b3476ab3c2dd3869320928191ee4dfe16d**; it does not contain these corresponding implementation files. Neither commit alone reproduces the deployment.
- Deployed `pbs_adapter.py` differs from its worktree file: deployment includes synchronous pvesh output parsing and validated final UPID handling. The exact deployed version is bundled; repository tests are labeled as such, not claimed to match or certify this extra change.
- Mac and VM109 boot_guard.py hashes match. VM109 uses the effective r020 packet, not a guessed repository revision.

Tests were supplied as existing source, not run or represented as VM108 acceptance. No candidate repair was made. Before packaging, local source bytes were rechecked against collected hashes; a live-secret value check found zero matches in exported source. Verification hashes are in `verification-receipts.json`.

## Preserved boundaries and next gate

No service identity rotation, secret-store write, container restart, deployment, processing job, model request, hold clearance, boot reconciliation, permission/TCC change, or uncertain-effect retry was performed. Only local diagnostic artifacts and this authorized handoff response were written. No rollback is needed for runtime because no runtime change was made.

Next: Forge can implement and validate the exact candidate on Community Brain dev **VM108** using this source. Production repair, credential rotation and processing resume remain outside this request. No additional answer from Patrick is needed to complete this read-only delivery.

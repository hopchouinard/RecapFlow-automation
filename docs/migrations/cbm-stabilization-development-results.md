# Stabilization implementation — validated on VM108; management integration pending

Date: 2026-09-20. Source commit: `a6766eb`.
Authorization: Patrick accepted the continuation plan, required development-VM
validation before production changes, and instructed “Start implementing.”

## Implemented

- **S-03:** `/api/v1/me` now separates configured automatic eligibility from
  current processing readiness. The API reads only the public host projection,
  validates its types/states and freshness, and returns a fixed safe status.
  Pause, unreconciled boot, attention, pending recovery, renewal failure/expiry,
  stale management observations and missing/stale host telemetry cannot report
  ready. Private marker contents, token values and management paths stay private.
- The UI refreshes readiness on its normal poll and before submission. While
  unavailable it offers **Save for later processing**, accurately queues the
  meeting and shows current availability. Losing the status request fails closed.
  Form input is captured before awaiting readiness so disabled controls are not
  accidentally omitted. Completed-save notices do not retain stale outage claims.
- **S-01 diagnostics:** scanner failures retain safe error class, return code and
  output hashes without exporting stderr, SQL, credentials or exception messages.
  Timeouts are not retried. The first attention event remains immutable.
- A PostgreSQL-enforced **read-only inspection** is now separate from the existing
  mutating stage selector. It does not fence expired stages, retry a call, claim
  work or send queue messages. Known failed model responses are distinguished
  from unresolved model-call states.
- Locked cron ticks refresh a bounded busy/readiness projection while long calls
  run. Public atomic writes use separate temporary files so concurrent heartbeat
  publication cannot collide. Boot/attention/recovery holds still take precedence.
- **Fresh-build defect repaired:** the original broad Python COPY included Forge's
  `.python-version`. `uv` downloaded Python into `/root`, and UID10001 fell back
  to system Python without application packages. Explicit source COPY operations
  and explicit use of the pinned base image's interpreter eliminate that path.
  The Dockerfile now imports the application as UID10001 during the build.

## Development evidence

All runtime changes were exercised on **community-brain-dev VM108** before any
production promotion. The dedicated source copy is
`/srv/dev-data/workspaces/cbm-stabilization-20260920`.

Application image ID:
`sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b`.

- Real disposable PostgreSQL and JetStream; synthetic manual and Fathom-style
  acquisition paths completed processing/indexing with **two meetings, 16 rows,
  full FTS coverage**, original meeting preserved and old outbox untouched.
- The pre-change `f60a30c` API/host reproduced missing readiness on the same
  simulated attention/boot-held state. The candidate correctly reported the holds.
- Renewal failure, independent boot and attention holds, stale telemetry,
  concurrent projections and busy heartbeats passed. A real refused database
  connection produced only the safe `OperationalError` scanner diagnostic.
- Read-only SQL inspection preserved an expired-running stage without fencing it.
- The actual API factory started as UID10001 in the candidate container. HTTP
  authentication, live pause/ready transitions and the built SPA passed.
- **Six browser tests passed against the UI served by VM108**, using a Forge
  browser over an SSH loopback tunnel. Browser API responses were fixture routes;
  the separate container checks exercised the actual API/database/queue.
- All **60 installed package files and three built frontend files** match Forge;
  **294 source/test/configuration files** match the dedicated VM workspace.
- Final Forge suite: **150 workflow, 1,005 Python application, 70 real DB/queue,
  six frontend unit and six browser tests**, plus TypeScript/Vite build. Python
  emitted 74 warnings. Focused code checks and `git diff --check` passed.

The first development attempts found source-file permission and interpreter
packaging problems; both were corrected before the final successful run. Browser
port publication on the isolated bridge was unavailable under the VM's forwarding
policy; the final frontend test server used guest loopback with host networking.
No firewall or production setting was changed. No paid model call, real Fathom
fetch or private meeting input was used. These fixture meetings do not close the
production weekly-cycle gate.

[Safe receipts and hashes](receipts/cbm-stabilization-dev-20260920/receipt.md)
contain exact results and source/image parity. Rehearsal instructions are in
[the development checker README](../../deploy/community-brain/stabilization/README.md).

## Still required — not claimed complete

**S-01 operational recovery:** production's original September18 attention marker
and September19 boot hold remain. A new read-only production inspection, using
code already exercised on VM108, found one completed automatic job, no running
stages and no unresolved model calls. It does not establish the historical cause
or authorize deleting holds without the remaining management/queue/recovery checks.
The new diagnostics improve subsequent evidence; they cannot reconstruct missing
historical stderr. The actual production runner has not been resumed.

**S-02 renewal:** the archived management source maps the current recorded
`service_renewal_live.py:112` failure to the OpenWebUI inspection on `n8n-automation`.
VM109's probe/operator/collector bundles match its active API identities and remain
0600. This narrows the investigation; it is not a confirmed diagnosis against
current management source. Forge does not have the Mac's SSH/Infisical authority.
The existing authorized relay request **CBM-STABILIZATION-DIAGNOSIS-20260920-024**
asks home.servers for current source and a read-only diagnosis. No response was
available when this implementation record was prepared. No credential rotation,
Mac permission change or workaround was performed. The last observed service-token
expiry remains **September22 20:53:07 UTC**.

**Production integration:** no runtime deployment has occurred. The current
management renderer recreates a base image plus multiple overlays; its current
source must be reconciled with the candidate. The tested application image does
not silently update the separate host launcher's hard-coded image pin or the
management renderer. Any changes to those components must themselves pass VM108
validation before promotion. Do not deploy this candidate by guessing at those
pins or overwriting the existing effective workspace.

## Concrete continuation for this batch

1. Consume Request024's current management source/diagnosis and acknowledge its
   safe receipt under the existing relay protocol. Reproduce the confirmed renewal
   fault on VM108 with scoped fixture consumers before implementing its repair.
2. Validate the exact management renderer/host-image-pin integration on VM108,
   including identity overlap/consumer acceptance/revocation, recovery holds and
   API recreation retaining the new readiness modules/frontend. No change to the
   stopped Request016 Mac permission scope is implied.
3. Build a coherent immutable promotion packet: tested application image above
   (or a newly validated successor), exact host helpers, renderer changes, source
   manifest and before-state/rollback capture. Preserve runtime registries,
   provider policy, source files, completed artifacts and the old excluded outbox.
4. Under the existing management/runner/manual/submission/corpus locks, verify no
   new work or unresolved effects, resolve identity renewal, deploy the tested
   packet, and reconcile the exact attention and current boot evidence through
   the established controls. Observe at least three healthy scheduled ticks.
5. Verify real consumers and UI readiness without submitting a fixture to prod.
   Obtain paired recovery evidence for the changed operational configuration.
   Roll back by restoring the captured image/renderer/helper pins and preserving
   holds if verification fails; never roll back or replay completed meeting data.
6. The next actual weekly meeting, subsequent cycle evidence, source publication,
   pgvector, retirement and final quality acceptance remain separate continuation
   work. No automatic corpus publication was enabled.

No additional routine permission is being requested for the already accepted
stabilization scope. The remaining dependency is management access/source and
validation of those integration changes under Patrick's development-first rule.

# Concrete operator proposal after Request031

Status: preparation only. This packet permits no production action. Keep the
Request029 production compiler and controller refusals and all 21 null evidence
slots. The current implementation is reviewable and testable on synthetic VM108;
it is not an installed production controller.

## Tested mechanism to carry forward

Keep an immutable owner/operation specification with external source and evidence
hashes, actual incumbent ID/configuration, private database server identity,
existing lock/hold bindings and absolute prepare/capture/serving/validation
cutoffs. The Mac must persist pending intent before dispatch and reconcile the
same operation after connection loss. The target must own the maintenance window
independently and reserve recovery time before its serving cutoff. Restoring the
same confirmed stopped incumbent is a state reconciliation, not replay of capture
or activation. Preserve every uncertain attempt and refuse a fresh operation
until authoritative recovery readback resolves it.

This candidate uses a detached systemd service with KillMode=control-group,
Restart=no, RuntimeMaxSec ending 20 seconds before serving expiry,
TimeoutStopSec=8 and ExecStopPost recovery. Actual Mac/SSH and VM process kills,
a frozen supervisor, fence termination and capture expiry exercise that boundary.
The production design must explicitly cover host reboot, unavailable Docker,
changed controls and failed finalization before promising wider availability.

## Proposed next implementation gate

1. Review this source, its raw failures and the retained VM108 receipts. Resolve
   the native Mac fixture portability failure without editing imported Forge
   bytes or weakening metadata rejection. Add a narrowly scoped fixture runner
   only if Mac-local capture tests remain required.
2. Build a production-shaped validator without production data: exact PostgreSQL
   schema/extension/ACL and writer-admission coverage, full component membership,
   private signing/volume identities, and intended production version bindings.
   Do not convert the legacy flat evidence contract by inserting true flags.
3. Review one admission path shared by the installed scheduler, manual operator
   and candidate. Test its durable pending ownership and maintenance recovery,
   including unresolved finalizer conditions and reboot handling, in development.
4. Present the resulting immutable plan and rollback package to Patrick. Name
   target VM109, exact incumbent IDs, operation owner, source hashes, lock order,
   private destination, disk headroom, maintenance cutoff and recovery deadline.
   Request only the next necessary production phase then. No authorization is
   inferred from this development rehearsal.

## Later protected phase, only after explicit authority

Re-read production identity expiry and current hold/volume/container bindings.
The metadata checked on 2026-09-21 at 15:12:47 UTC showed retrieval, collector,
manual-operator and probe identities expiring on 2026-09-22 at 20:53:07 UTC, with
renewal journal phase completed. Do not rotate or renew to make a plan pass;
expired authority is a stop condition requiring its own user decision.

An authorized private preservation phase would quiesce the exact admitted
writers, preserve the original incumbent and signing identity, capture a paired
private DB/files/WebUI bundle, verify a distinct off-host copy and independently
restore it. Private content and signing material must not enter VM108 or the
shared relay. Restore serving by the independently enforced deadline, regardless
of whether comparison finishes. No cutover or processing resume is implied.

A later serving-only proposal still needs actual preserved sessions/signing,
rendered login and disabled-signup checks, intended concurrent capacity evidence,
and any separately authorized bounded provider-spend proof. Keep unknown outcomes
held. Do not resize VMs, delete recovery resources or involve VM101 as a target.
VM101 remains recovery-only; its unrelated services are outside this work.

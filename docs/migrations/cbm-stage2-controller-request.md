# Request035: finish the stage 2 execution controller in development

ID: CBM-STAGE2-CONTROLLER-20260924-035. Target: home.servers.
Deadline: 2026-09-26T18:00:00Z. Request034 consumed and acknowledged.

Patrick authorized the **full stage 2** on September23. Request034 completed
scoped development identity/CA/consumer, browser/recovery and bounded capacity
acceptance, but explicitly did not deliver the production-capable controller,
installer, independent finalizer or VM108 fault matrix. This request closes that
specific remaining stage2 implementation. Existing dev/Mac administration and
read-only production diagnosis apply. No production renewal, installation,
maintenance stop, capture/transfer, secret import, cutover/resume, resize or paid
provider call is authorized. Production identities expired September22 and the
existing renewal reports failure; never bypass that gate or use expired identities.
VM101 remains recovery-only. Preserve all Request029–034 fixtures and journals.

Base on Request033's actual production helper/catalog/service/private mappings
and Request034's accepted final dev source. The final Request034 packet manifest
is `7c5cfba2187e72ea40a6955592278539f7982376abbe647819e466354b3b3825`.
The Request034 `production_admission.py` is a **review refusal core** only; its
`accepted:true` evidence envelopes do not independently prove21 underlying facts.
Do not turn that flag into an enable switch.

Deliver one source-coherent controller/installer/finalizer package:

1. Compile an immutable, externally pinned plan against exact source/config,
   host/mount/incumbent/holds/locks, current authority, private destinations and
   explicit operation/rollback owner. Each of21 evidence slots must bind a real
   immutable receipt and schema, exact member hashes, scope, attempt/capture ID,
   independent observations and expiry. A missing slot or unimplemented semantic
   validator must refuse production; development fixtures may exercise the
   mechanics but never fill production slots. Separate protected-preservation,
   serving and processing-resume authorities; no implicit promotion between them.
2. Provide a staged installer whose dev VM108 dry run and install/uninstall are
   safe, idempotent and bound to the exact packet. Source should be reviewable for
   later VM109 enrollment, but do not install it there. Preserve the incumbent,
   old management source and boot processing pause. Bind Docker startup ordering,
   root-owned control state, lock order and the existing Mac scheduler mutex.
3. Implement a controller with an exclusive durable intent before any effect,
   one common scheduler/manual/capture admission path, exact-incumbent stop and
   same-incumbent recovery, per-phase absolute deadlines and no blind replay on
   SSH or caller loss. A separate VM-owned systemd finalizer must restore serving
   within its bound when the caller/worker/supervisor dies. On failed finalizer,
   changed controls or unavailable Docker/DB, admission stays closed and the
   original/partial state is retained. Never clear paused/attention/checkpoints,
   rewrite unknown outcomes, restart VM101 or perform paid provider calls.
4. Exercise the final source on fresh synthetic VM108 state with actual Docker,
   PostgreSQL, systemd and Mac/SSH transport: normal path; Mac/SSH/worker/guardian
   kill; guardian freeze/expiry; failed finalizer; stale/foreign readback;
   competing scheduler/manual/capture; source/hold/volume drift; authority expiry;
   boot/startup ordering and installer rollback. Report separately which failure
   modes are bounded only while VM/systemd/Docker/storage remain available. Do
   not reboot the shared VM108 baseline or imply a real reboot pass.

Return exact commit/archive/member manifest, independent VM108 source parity,
positive/negative final-byte receipts, preservation/retirement disposition, and a
single stage2 acceptance ledger. If the controller cannot be finished, name the
specific irreducible blocker and deliver all safe source/review work; do not mark
stage2 complete. All21 production slots remain null until a separately authorized
protected preservation phase supplies independently validated production receipts.
No private content or signing bytes in the relay.

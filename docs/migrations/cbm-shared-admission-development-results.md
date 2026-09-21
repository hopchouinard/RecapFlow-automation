# Shared admission development increment

September21, following consumed Request031. Forge implemented a common admission
journal in `deploy/community-brain/shared-admission/admission.py`. Scheduler,
manual and capture callers use the same existing mutex and journal via `invoke`.
Every intent is persisted before dispatch. A killed owner, failed dispatch or
partial directory blocks all entry-point kinds. No expiration automatically
resolves an operation. Fresh identity-bound target readback is required, including
healthy same-incumbent serving, unchanged holds, finalizer evidence, inactive
maintenance service and current boot identity. Resolutions are immutable and
operation IDs cannot be reused. Missing/replaced/linked mutexes are refused.

Nine tests passed locally and on VM108, including twelve malformed readback cases,
actual owner SIGKILL, lock contention, process recreation, cross-kind blocking,
callback failure, partial creation and mutex replacement. A retained synthetic
journal rehearsal also passed. Exact source parity independently verified.
Workspace: `/srv/dev-data/workspaces/cbm-shared-admission-forge-20260921-032`.

This library is not installed into the existing scheduler or Mac entry points.
The observation callback is a trust boundary: its production implementation must
obtain authenticated fresh target observations; a caller-supplied success flag is
not evidence. Rehearsal observations are explicitly synthetic, not service recovery
proof. A changed boot ID requires target recovery verification; the journal does
not itself restart services or guarantee reboot recovery. Existing legacy pending
records must be reconciled by the integration before any new dispatch.

[VM108 tests](receipts/cbm-shared-admission-forge-20260921/vm108-tests.txt),
[retained journal rehearsal](receipts/cbm-shared-admission-forge-20260921/vm108-rehearsal.json).

Request032 carries this tested core to home.servers for actual existing scheduler,
manual and capture adapter integration, authoritative readback/recovery and the
production-shaped synthetic database validator. Keep Request029/031 and all retained
fixtures unchanged. No production changes, protected transfer, resize or provider
spend are authorized by this increment. Production compilation remains disabled.

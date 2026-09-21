# Protected capture controller: Forge development increment

September21, following Request030; production execution remains disabled.

Added `operation.py`: exclusive durable attempt creation, specification hash,
existing-lock ownership, hold comparison, deadline and SIGTERM/SIGINT handling,
readback of running/completed/uncertain attempts, and refusal to replay any existing
attempt. SIGKILL leaves an uncertain intent. Partial data stays in place. Errors
record their type, never private exception text. The core never repairs holds,
acknowledges checkpoints, restarts containers, or dispatches remote commands.

Added `receipt.py`: verify the pinned component bundle, capture/restore intents,
exact receipt fields, component hashes, actual restored tree including metadata,
and exact root member set. Altered flags cannot certify a restore. Database and
application acceptance remain null; no legacy flat-schema conversion is installed.

Verification:49 tests passed locally and on VM108, including real child-process
SIGTERM/SIGKILL, timer expiry, replay denial, hold drift, stream transport, restored
file drift and forged receipt flags. The expected SIGTERM child traceback appears
in the test receipt; the suite exited0. A retained VM108 synthetic operation captured,
streamed, restored, independently compared files, read its journal and rejected
redispatch. Original source and hold identities remained equal. All19 source files
match Forge. No production access beyond the established handoff relay; no service
change, external provider call, capacity resize or private transfer.

Evidence: [tests](receipts/cbm-capture-controller-forge-20260921/vm108-tests.txt),
[retained rehearsal](receipts/cbm-capture-controller-forge-20260921/vm108-rehearsal.json),
[source hashes](receipts/cbm-capture-controller-forge-20260921/source-manifest.json).
VM108 retained workspace:
`/srv/dev-data/workspaces/cbm-capture-controller-forge-20260921-031/`.

This is a development core, not a production maintenance controller. Its timer
interrupts the local Python action; it cannot bound an unmanaged remote process or
guarantee recovery after the owner is killed. Callbacks must not spawn unmanaged
work. No database semantic comparison is inferred from equal file bytes. A separate
host integration must bind Mac mutex, detached target ownership, DB fence lifetime,
SSH loss/readback, bounded incumbent maintenance and restoration of serving state.
That integration must validate a new component-based database evidence contract,
retain all21 production gates and keep compile/controller production refusals.
Request031 asks home.servers to implement and test this on synthetic VM108 state,
then return the exact source and a reviewable production-phase proposal.

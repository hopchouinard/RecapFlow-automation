# Request031: synthetic capture controller

This is a development-only candidate for the existing Mac management entry point
and fresh VM108 fixtures. It is not installed in the deployed management service.
The target is fixed to `community-brain-dev`; production specifications are refused.
No production acceptance slot is filled by these receipts.

## Source and authority

`forge-core/` is the exact 19-file Forge packet received in Request031. Its 15
Request030 files remain byte-identical to `../protected-restore-030/`.
`LINEAGE.json` records every imported hash and the inherited commit. Integration
lives outside that directory. Existing Request029 compiler/controller code and
its 21-slot production template are unchanged.

The only mutable target root is
`/srv/dev-data/workspaces/cbm-capture-controller-20260921-031`.
The Mac uses the existing `scheduler.lock`, plus durable Request031 intent and
pending records. It never edits the installed management source or old validation
checkpoints. A different operation cannot bypass unresolved candidate intent.

## Protocol

1. `fixtures.py prepare` makes a fresh isolated incumbent and existing lock/hold
   files, then binds actual container IDs, image/configuration fingerprints,
   independently observed PostgreSQL system IDs, source packet SHA, owner,
   operation, capture ID and four absolute phase deadlines.
2. `mac.py dispatch SPEC` takes the existing Mac mutex and persists intent before
   SSH. The immutable target operation directory prevents replay even after a
   failed dispatch. `mac.py reconcile SPEC` performs readback only.
3. `target.py` creates a detached systemd service. Its supervisor owns the global
   target lock and the three ordered fixture locks. It preserves every hold and
   stops only the exact isolated incumbent ID after its health check.
4. The managed worker takes a real PostgreSQL SHARE-lock transaction and exported
   snapshot, observes the source, dumps it, compares source observations again,
   captures components and releases the fence. Lost fence, expired capture or
   process failure cannot produce a completed receipt.
5. The same incumbent ID resumes serving before independent database restore and
   evidence validation. A systemd RuntimeMaxSec deadline and ExecStopPost
   finalizer recover independently of the Mac, SSH waiter and supervisor Python
   process. Container recreation is never a recovery mechanism.
6. Only completed/aborted-restored readback with current health, unchanged holds,
   a finalizer receipt and inactive/failed service resolves Mac pending intent.
   Other states remain retained and block replay.

All command output that could contain data remains private on the fixture host.
The relay receives source, hashes, dispositions and safe synthetic verification
metadata, never dumps, production content or signing material.

## Database evidence

`database.py` and `candidate.py` verify the actual restored component tree and
exact evidence member/field sets. Evidence binds dump bytes, capture, manifest,
source packet, operation/owner, source-before bytes, after-observation digest,
independent server identities and a finite evidence interval. Canonical comparison
covers public columns, constraints, indexes, sequence definitions and current
values, table counts and row hashes, unknown outcomes, orphan relationships, FTS
observations and actual artifact-to-file hashes. It does not regenerate state.

`candidate.prepare` returns a preparation contract with all 21 production slots
still null and execution, compilation, controller and installed-adapter flags
false. Evidence expires; a historical receipt remains an audit record, not fresh
permission to execute.

## Reproduction

Run Forge tests with `python3 -B -m unittest discover -s forge-core -p 'test_*.py'`.
VM108 runs them natively. On this Mac, five new Forge receipt fixture setups reject
inherited extended metadata; the raw 49-test suite therefore has five errors.
Do not weaken the preservation library or silently mask this result. The actual
capture/restore runs on VM108, while Mac process and SSH interruptions are real.

`rehearse_host.py LABEL MODE PACKET PACKET_SHA` runs one fresh case. Modes are
normal, sshkill, mackill, fenceloss, workerkill, guardiankill, guardianstop and expiry.
It records actual signals, lock probes, duplicate dispatch refusal and detached
readback. Use a new label each time. Never delete an old attempt to rerun it.
`check_evidence.py SPEC SPEC_SHA TEMPLATE` checks a fresh successful capture before
its validation deadline, retaining all malformed evidence copies.
`check_boundaries.py SPEC SPEC_SHA` probes strict specification and real busy-lock
refusals against a completed fixture without restarting its incumbent.

## Limits

The bounded serving recovery claim assumes the VM, systemd, Docker and filesystem
remain available and bound controls remain unchanged. There is no reboot or
power-loss recovery guarantee, and no independent machine can restart Docker if
this host is unavailable. A changed incumbent/hold, unavailable Docker, stuck
kernel I/O or failed finalizer remains explicitly unresolved. The candidate does
not claim those conditions restore serving within deadline.

The fixed synthetic public schema is not a full production PostgreSQL catalog
validator: extensions, role/ACL policy, other schemas and production writer
admission remain outside this adapter. SHARE locks do not fence arbitrary DDL or
independent sequence manipulation; fixture isolation and repeated observations
are part of the tested boundary. This is not production quiescence proof.

The durable candidate pending record is consumed by this candidate, not by the
already deployed production scheduler. Installing a common production admission
path is still a separate reviewed integration gate. Off-host private recovery,
real WebUI/session/browser acceptance, workload capacity and paid-provider proof
are not supplied here. VM101 remains recovery-only.

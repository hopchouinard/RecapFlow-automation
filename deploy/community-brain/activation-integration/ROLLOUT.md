# Request029 operation and rollback boundaries

The immutable handoff authorizes development integration and read-only production
reconciliation. It does not authorize production installation, protected data or
signing transfer, rotation, ingress, cutover, processing resume or retirement.
Deadline: September 21, 2026 at 20:00 UTC. Recorded production identity expiry:
September 22 at 20:53:07 UTC. Neither time extends authorization.

## Before a serving operation

1. Verify request ownership, deadline, source provenance and sealed packet hashes.
2. Verify actual paired restore observations, not an asserted success flag. Bind
   the original recovery packet and retained artifacts alongside the controller.
3. Acquire the existing Mac scheduler mutex; inspect the persistent pending
   activation pointer. Resolve any prior uncertainty by readback first.
4. Compile/review a new immutable plan and its external hash. Require the current
   incumbent ID/configuration and exact holds, all relevant sealed sources,
   Compose/private configuration/CA/signing hashes and external WebUI volume.
5. Dispatch once. The target controller acquires the VM locks itself and rechecks
   bindings under them. Do not nest it inside a quiet-window lease.

## Lost response and failures

The detached target worker owns locks independently of SSH. The Mac retains its
mutex while reading that same operation's durable result. A timeout, absent result
or absent uncertain candidate never permits a new creation attempt. Preserve
private logs, journal `.tmp` files, intents, failed plans and operation directories.
An existing matching running candidate can be reconciled; an unknown or changed
one cannot be adopted. Known failure results still require inspecting the journal
and exact container state before choosing rollback.

The candidate's persistent pending guard is not installed into the deployed Mac
scheduler in this request. That integration is an explicit production template
slot. The shared Mac mutex is exercised live; the VM108 and VM109 runtime state
roots remain separate throughout this development rehearsal.

## Acceptance and rollback

After activation, verify candidate IDs/configuration, authenticated API subjects
and scope denials, anonymous rejection, the live OpenWebUI filter, and Kuma and
Prometheus observations newer than activation. Test duplicate invocation against
the same journal without recreating candidates. Preserve all holds.

Rollback stops and retains candidates and starts the exact incumbent container.
It does not recreate that container, overwrite replacement data with a backup,
clear holds, rotate credentials or resume processing. Verify incumbent health,
fresh monitoring and identity/configuration equality after rollback. Verify a
new WebUI chat remains in the replacement volume even though the old serving
interface may not display it. Database migrations and divergent application data
are not reversed by a serving rollback.

A rolled-back journal is terminal. Another activation needs a new reviewed plan,
candidate names and journal. Changed holds, changed bound inputs, an absent
uncertain target or changed incumbent require explicit reconciliation.

## Cleanup and delivery

Stop only Request029 fixture containers and its explicit loopback relay. Retain
all private development authority, recovery artifacts, volumes, immutable packet
revisions, failed attempts and journals. Verify pre-existing services and earlier
fixtures against the captured baseline. Verify production runtime/holds and the
protected r020 bytecode remain unchanged. Do not contact VM101.

Return source archive/diff/provenance, exact plan and packet hashes, safe success
and failure receipts, test results, cleanup evidence and the non-deployable
`production-serving-plan.template.json`. Keep private runtime content and signing
material off the relay. Previously approved ingress remains available when its
replacement is ready; this development request does not execute it.

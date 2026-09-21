# Request029 accepted — September 21, 2026

The development activation/compiler and actual Mac/SSH integration are complete
for the recorded tests. Forge verified and acknowledged the response. Production
compilation and serving remain explicitly disabled; the template is not deployable.

## Independent verification and source

Forge verified all 72 delivered artifacts, all 58 actual VM108 packet-v6 members,
and all 255 bound files in each of the normal, readiness-failure and partial-
activation plans. The source rebuild is byte-identical to the retained packet:
`c9326fd4bf149b68fcbc40fb7ab49a2ce23b4c7711a36ea9a5a99e8b41ebbb76`.
All 30 boundary tests passed locally (11 controller and 19 integration/successor).
The receipt also records 30 passing Mac tests, 30 VM108 tests and 293 parent tests.

Unchanged source from agent-ops commit
`db6416c7a2ab679a800a5a3e047a6554295cfc80` is imported under
[`activation-integration`](../../deploy/community-brain/activation-integration/README.md).
Its branch was codex/request029-activation, clean and not pushed at handoff. Earlier
Forge and Request028 implementations remain preserved. Original archives/diffs,
per-file provenance and safe receipts are in the
[evidence directory](receipts/cbm-activation-integration-20260921/receipt.md).

## Accepted development behavior

- The actual Mac mutex and ordered target locks exclude concurrent callers and
  both worker launchers. An actual SSH client was terminated while its detached
  target continued; readback retained ownership and completed the same operation
  without redispatch or recreation. Pending activation also excludes management.
- Duplicate activation preserves IDs, start times and restart counts. Terminal
  rollback refuses another activation. API-readiness and partial API/WebUI failures
  both recover the exact incumbent container/configuration.
- Actual API scope checks, anonymous denial, WebUI filter retrieval, and fresh
  Kuma/Prometheus observations passed after activation and rollback. A synthetic
  chat created through WebUI survives rollback; SQLite integrity passes.
- Paired development DB/state/WebUI restoration passed, with 28 recovered files
  and durable DB observations matching. Holds and plan-bound source/configuration
  remained unchanged. This is not protected production/off-host recovery evidence.
- Actual development Infisical renewal recovered the same generation after a
  lost delivery acknowledgment, retained overlap, accepted all consumers and
  rejected five old tokens. Three recreations preserved image, mounts and holds.

All activation/rollback cases ran on final packet-v6. Renewal ran on v3 and paired
restore on v4; v6 binds those dependencies. Management/profile/consumer/transport/
runtime-contract and policy sources match the renewal-tested versions exactly.
Changed controller/fixture files are explicitly listed in renewal-final-equivalence.
No completed or uncertain work was replayed to disguise revision differences.

Docker's internal-network PortBindings did not open a VM108 host listener. The
test therefore used an explicitly labelled loopback relay to prove the sole running
API identity, plus actual internal-network authenticated/filter/monitor probes.
This is not evidence of production proxy/firewall/ingress behavior. It qualifies
the earlier Forge port-handoff claim: Docker port metadata alone proves no listener.

An upstream adapter bug confused a same-named retained volume with a container.
The integrated adapter now uses explicit container inspection, with a regression
test. Other recorded setup failures and their retained evidence were reconciled
before acceptance; they are not claimed as clean first attempts.

Forge confirmed all 12 Request029 containers are stopped and only the four baseline
dev services run. The receipt verifies baseline dev/production container identities,
configuration/start times/restarts, production holds and r020 bytecode unchanged.
Private state, volumes, failed attempts, journals and operation records are retained.

## Next work and remaining gates

The [production template](receipts/cbm-activation-integration-20260921/production-serving-plan.template.json)
has 21 empty evidence slots. They are not 21 new software features; they group into:

1. **Protected restoration and acceptance:** real database/corpus/artifacts/uploads,
   replacement WebUI volume and external signing key, verified off-host recovery,
   user login/session continuity and disabled signup. Prepare the exact transfer/
   restore procedure and private evidence locations before seeking its separately
   required transfer authorization. Preserve VM101 without starting its stack.
2. **Workload acceptance:** intended capacity, real-provider/budget behavior and
   outstanding Fathom/desktop-intake checks, all validated in development first.
3. **Final deployment bindings:** reviewed paired source/manifests, current authority
   generation, environment/trust/signing hashes, hold/lock identities, exact live
   incumbent, volume ownership, fresh authenticated/filter/monitor acceptance,
   acceptance deadline and rollback owner. Many require a fresh preflight near
   the actual deployment; historical snapshots cannot fill them automatically.
4. **Production phase:** explicit authorization, enabling the reviewed production
   compiler/controller path and installing the paired scheduler pending-operation
   guard. Any enabling change must pass VM108 validation again. The candidate guard
   was tested but is not installed in the production scheduler. Serving activation
   must keep processing held; worker/boot reconciliation remains separate.

The next concrete preparation task is the protected real-data/signing restore and
acceptance packet, alongside the remaining development workload checks. Do not
declare production readiness merely because activation mechanics now pass.

Rollback restores serving through the same incumbent; it does not undo migrations
or reconcile divergent writes. New WebUI chats remain in the replacement volume
and are not automatically available through an older interface. Changed inputs,
holds, incumbent or absent uncertain targets require explicit reconciliation.

The last verified production identity expiry is **September22 at20:53:07 UTC**,
with renewal journal completed. Plan the remaining work against that deadline;
do not use it to bypass validation or reactivate VM101. Previously approved
chat.patchoutech.lab DNS/Traefik/Step CA work needs no repeated approval once ready.
No production installation, transfer, rotation, ingress, cutover or processing
resume occurred. Weekly-cycle and retirement evidence remain outstanding.

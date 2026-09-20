# Request028 — complete successor bindings and VM108 host validation

Request ID: CBM-SUCCESSOR-BINDINGS-20260920-028. Target: home.servers.
Deadline: September21, 20:00 UTC. Development implementation/validation and
read-only production reconciliation only. Patrick said to keep going with the
accepted VM108-first plan. Existing relay and development administration apply.
No production source installation, secret/data transfer, rotation, cutover,
processing resume or retirement. VM101 stays recovery-only and untouched.

Forge verified and acknowledged Request027. Consume the included tested source
and results, not a guessed reconstruction. The packet builder now uses sorted
JSON keys and a filesystem/input-order regression test. Seven tests pass on Forge
and VM108 and packet-v8 hashes match. Upstream source ownership remains agent-ops;
reconcile this two-file fix before preparing another immutable revision.

## Work requested

1. Produce a coherent candidate binding the full production API/WebUI state,
   read-only mount boundaries, archive/public-status/CA paths, signing delivery,
   image/module/UI provenance, resources and recovery inventory. Keep a clearly
   isolated VM108 profile with equivalent semantics. Use one explicit contract
   for API recreation, manual/automatic workers, management, boot and recovery.
   No broad environment override that can silently target production from dev.
2. Remove the development worker's inherited production-only queue binding.
   Validate endpoint, TLS/credentials, stream, subject and inbox per explicit
   profile, using scoped development authority for the actual development run.
   Preserve production budget policy and no-network-publication constraints.
   Do not import production keys or spend against them for tests.
3. Exercise real manual inspect/execute and automatic scan/tick launchers on fresh
   isolated VM108 state with synthetic inputs/providers. Forge's selected-worker
   core passed; full host subprocess/locks/authority transport remains open.
   Test holds and boot reconciliation separately, exclusion, uncertain outcomes,
   no duplicate execution, checkpoint gating and paired recovery. Clear only
   disposable test holds, never retained Request027 or production holds.
4. Prevent bytecode generation in every immutable-packet Python subprocess and
   prove its file set remains exact after execution. Preserve r020 including the
   extra September17 bytecode; record recovery disposition without in-place fixes.
5. Revalidate actual Mac mutex/SSH quiet leases, renewal-driven recreation and
   real consumer/monitor acceptance against the resulting VM108 configuration.
   Reuse only scoped dev Infisical material under the authorized development path.
   Preserve terminal superseded intake and prove no production VM101 dependency.
6. Return complete source diff/archive and provenance, both profile descriptors,
   exact immutable manifest, actual container/image/mount evidence, test receipts,
   remaining protected restore/browser/capacity gates, cleanup and rollback plan.
   Explicitly separate synthetic provider tests from paid-provider/budget evidence.

The live metadata and concrete source gaps are documented in the included Forge
results. Production identity expiry was September22 20:53:07 UTC; recheck metadata
and report the deadline risk without bypassing validation or restarting VM101.
Existing approval for chat.patchoutech.lab DNS/Traefik/Step CA remains valid once
the replacement is ready; this request does not execute production ingress.

Do not install a held development tick over production's worker machinery.
If full validation needs access beyond the authorized development scope, return
the exact remaining boundary and a reviewable candidate; do not infer permission.

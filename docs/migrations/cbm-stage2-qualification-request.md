# Request034: full development qualification of the mapped successor

ID: CBM-STAGE2-QUALIFICATION-20260923-034. Target: home.servers.
Deadline: 2026-09-25T18:00:00Z. Request033 consumed and acknowledged.

Patrick explicitly authorized the full stage 2 on September23. Implement and
validate all application and operational changes on VM108 before any production
promotion. The previous Request033 admission cutoff and recorded credentials
expired September22; refresh read-only metadata. Do not reuse the old window,
renew/rotate production authority, install a production controller, stop the
incumbent, transfer protected data, cut over or resume processing under this task.
No paid provider requests or VM resize without a separately bounded decision.
VM101 remains recovery-only, including WebUI; its unrelated services stay intact.

The exact Request033 source is `deploy/community-brain/production-mapping-integration/`,
manifest `0eec32da7770ff652a2193f87b97c858b334673eacf45820098cfc0697c980c1`.
Retain all sealed Request029–033 fixtures; use fresh exclusive VM108/Mac workspaces.
The Forge checkout remains the canonical source. Return source/patches and safe
receipts through the handoff with hashes; no private credentials/content in relay.

Complete these stage 2 deliverables, with actual dev services and real control
planes wherever scoped development identities are available:

1. Actual Infisical development authority, fresh certificate issuance/deployment
   through the development CA, and successor API/WebUI filter/collector/Kuma/
   Prometheus consumers. Test positive access, expired/wrong/cross-scope rejection,
   same-generation interrupted renewal, independent readback and revocation only
   after every consumer accepts new identity. Log identities by digest/expiry,
   never key bytes. If an actual external service has no scoped dev path, document
   its exact access blocker; do not substitute a successful fixture silently.
2. Build the bounded production-capable controller and installer as reviewable
   source, with explicit phase authorization input, current authority/expiry,
   all21 evidence slots, sealed source/config/private receipt verification,
   exact host/mount/incumbent/hold bindings and independent finalizer/rollback.
   Preserve the current production refusals until the new reviewed path is
   actually qualified. Test source drift, restart/kill, SSH loss, expiry, failed
   finalizer, competing scheduler/manual/capture and uncertain readback on VM108
   final bytes. No production execution or installation by this request.
3. Qualify intended capacity with actual concurrent dev API, WebUI, worker and
   restoration workload; measure latency, memory, CPU, OOM and headroom under a
   declared profile. Existing4GiB VM108 is baseline; if insufficient, return
   measured need and exact resize proposal rather than claiming acceptance.
   Never use private production content or provider keys for load fixtures.
4. Exercise a fresh exact-image synthetic WebUI/API recovery fixture and rendered
   browser acceptance for login, retained synthetic chat/upload, signup-disabled,
   original synthetic signing key versus wrong key, vector/FTS identity and source
   file hashes. Browser access must be actual rendered interaction, not only API
   status. No VM101 restart or real user data transfer.

Return a single stage2 acceptance ledger that separates proven, failed and
unavailable checks. Repeat changed-source checks on VM108; do not replay sealed
attempts or fill production slots with dev receipts. The resulting packet should
state whether the production execution path is reviewable for a later separately
approved protected-preservation phase, and precisely what remains if it is not.

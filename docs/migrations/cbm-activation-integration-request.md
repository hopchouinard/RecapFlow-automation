# Request029 — integrate the tested serving activation controller

Request ID: CBM-ACTIVATION-INTEGRATION-20260921-029. Target: home.servers.
Deadline: September21 at20:00 UTC. Patrick instructed Forge to proceed with the
next task: implement controlled activation/rollback and validate on VM108.
Existing relay and dev administration apply. Development work and read-only
production reconciliation only; no production installation, private data/signing
transfer, rotation, ingress, cutover, processing resume or retirement.

Request028 was verified and acknowledged. Forge implemented the attached
activation controller and exercised an actual API/OpenWebUI port handoff, lost
acknowledgment, duplicate invocation, authentication, retained WebUI write and
same-container rollback on VM108. Ten boundary tests pass. Read the supplied
results, code and receipts; preserve its retained failed attempts and journals.

## Concrete work

1. Reconcile the controller into agent-ops with source provenance and review the
   plan/journal/rollback boundaries. Complete a plan compiler that binds all sealed
   successor/controller files and manifests, Compose/env/CA hashes, current holds,
   exact incumbent ID/configuration, external WebUI volume and actual recovery
   evidence. Refuse missing or stale bindings; never manufacture restore flags.
2. Integrate the Mac scheduler mutex and existing management transport. The
   controller owns ordered VM runner/manual/submission locks itself, so do not
   invoke it inside an existing quiet lease holding those locks. Resolve ownership,
   timeout and lost-SSH-response semantics explicitly; no blind effect replay.
3. Rehearse the complete resulting path with fresh disposable VM108 state and
   scoped development authority. Test actual SSH loss/readback, held/busy workers,
   held boot/attention, duplicate calls, candidate readiness failure, partial
   activation, rollback before and after new WebUI writes, and exact artifact/
   source/configuration preservation. Retain uncertain state for reconciliation.
4. Validate authenticated API/filter behavior and fresh Kuma/Prometheus acceptance
   around activation and rollback. Preserve the existing renewal journal policy;
   if management recreation changes, rerun actual development renewal on that
   final configuration. No production identity or legacy serving dependency.
5. Return a complete, reviewable production serving plan template with explicit
   outstanding evidence slots, plus tested development plan, source/diff/archive,
   exact hashes, before/after and failure receipts, cleanup and rollback limits.
   Do not represent the template as deployable while required protected inputs
   are missing. Activation must not enable automatic processing or bypass the
   successor worker loader's production gate.

Use only authorized development Infisical scope under
/development/community-brain-dev. Production metadata/expiry may be read, but
production keys must not enter tests. Source and safe hashes may enter the relay;
private runtime data, environment values and user content must not.

Production protected restoration, browser/signup/session acceptance, capacity and
real-provider/budget checks remain separate outstanding gates. Existing ingress
approval needs no repeat once its target is ready, but is not executed here.
The last recorded identity expiry is September22 at20:53:07 UTC. Report deadline
risk without extending authorization, reactivating VM101 or bypassing validation.

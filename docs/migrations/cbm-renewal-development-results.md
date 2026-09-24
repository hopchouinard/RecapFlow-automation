# Request024 diagnosis and corrected OpenWebUI migration direction

Patrick confirmed that **OpenWebUI must migrate off n8n-automation**. The old VM
is a temporary recovery fallback pending retirement, with no required production
role. This supersedes historical plans to keep live OpenWebUI there temporarily.

Request024 is complete, verified and acknowledged: nine artifact hashes and all
42 source-file hashes match. Its [receipt](receipts/cbm-renewal-dev-20260920/request024/receipt.md)
confirms renewal uses `docker exec open-webui`, while that container has been
stopped since September19. Its volume/database remain. The renewal journal is
completed; the observed failure precedes preparation of a new generation. The
independent September18 runner error has no recovered underlying cause.

## Work completed, then withdrawn from promotion

Before the scope clarification, a candidate kept the stopped WebUI consumer in
renewal inventory and updated only its stored filter API key transactionally.
Twenty targeted tests passed on Forge and VM108, including drift, observed
concurrent starts, delivery interruptions, overlap and journal resume. A real
VM108 Docker/SQLite fixture reproduced the stopped-container failure and passed
delivery, replay, preservation and integrity checks. Its container/volume were
removed. No live WebUI image/API acceptance or production change occurred.

That candidate would preserve an unwanted production dependency. It was removed
from the active deployment source; exact source remains in the
[unpromoted archive](receipts/cbm-renewal-dev-20260920/renewal-candidate.tar.gz)
with its [test evidence](receipts/cbm-renewal-dev-20260920/verification.json).
Request025 was withdrawn via a shared stop notice before any response existed.
Its immutable original payload remains as history. No legacy credential was
updated, no old service was restarted, and production holds remain unchanged.

## Required continuation

1. Reconcile where OpenWebUI must run in the migrated production solution, its
   existing image/source and protected user-data/configuration preservation.
2. Validate the replacement on VM108: authentication, persisted configuration,
   actual retrieval/filter behavior, renewal and consumer verification, restarts
   and recovery. Tests must not use the dormant old VM as a production consumer.
3. Prepare the coherent production migration and rollback packet, including
   application renderer/host pins and management source reconciliation. Request024
   shows required agent-ops source is untracked/modified; neither recorded commit
   alone reproduces deployment.
4. Migrate the validated replacement and point production renewal/inventory to it.
   Preserve the old VM as a recovery copy without serving traffic or renewal writes.
   Verify production operation no longer requires the old host.
5. Close weekly-cycle/recovery evidence before retiring the old VM. A preserved
   backup does not need to retain an active production service identity; recovery
   must obtain appropriately scoped fresh authority through the managed procedure.

Home.servers acknowledged Request025's withdrawal before execution. Forge verified
and consumed that receipt and posted [Request026](cbm-openwebui-migration-request.md)
for the migration inventory and isolated VM108 rehearsal.
The last known service-token expiry remains September22 20:53:07 UTC. No renewal,
processing resume, actual weekly cycle, model call or publication is claimed here.

Request026 subsequently completed and was consumed. Its actual OpenWebUI baseline
and remaining integration gates are recorded in the
[successor packet](cbm-openwebui-successor-packet.md). No production change occurred.

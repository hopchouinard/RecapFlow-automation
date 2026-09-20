# Request026 — OpenWebUI migration inventory and VM108 rehearsal

Request ID: `CBM-OPENWEBUI-MIGRATION-20260920-026`.
Target: home.servers. Request025 withdrawal has been consumed and acknowledged.

## Authority and intended outcome

Patrick explicitly confirmed that OpenWebUI must migrate off `n8n-automation`.
That VM is retained only as a temporary functionality/recovery backup before
retirement. It must not remain a required production serving, credential-renewal,
scheduler or consumer dependency. Preserve its dormant recovery state.

Patrick authorized stabilization implementation and mandatory development-first
validation. This request covers read-only inventory/source inspection and isolated
development work on Community Brain VM108. It does not authorize production
installation, rotation, DNS/cutover, legacy restart, backup credential updates,
hold clearance, processing resume or retirement. Request025's stopped-legacy
credential-delivery candidate is withdrawn; do not deploy or resume it.

## Work requested

1. Inspect the old installation read-only through existing Mac administration.
   Identify exact image digest/ID, filter source/hash, persistent volumes, app
   version, authentication configuration shape, custom models/prompts, upload and
   vector storage, required integration endpoints and existing preservation copies.
   Inventory the data that must survive migration (users, chats, files, settings,
   functions and models) using counts/schema/paths/hashes, not content exports.
   Do not start the stopped container or write to its volume. Do not copy runtime
   environment values, signing secrets, credentials or private user data to Forge
   or the shared handoff. Return safe source only after checking for embedded values.
2. Reconcile actual production dependencies, including the current renewal adapter,
   scheduler, monitoring and ingress. Identify every old-host reference that must
   move or be removed. Distinguish the intentionally retained backup from production
   consumers. Recheck nonsecret identity expiry and renewal journal phase without
   invoking rotation or inventory modes with side effects. The last known five-token
   expiry is September22 20:53:07 UTC; a failed renewal does not extend it.
3. Prepare an isolated OpenWebUI rehearsal on VM108 using the exact existing image
   and filter version. Transfer an ordinary image export if needed; never use a
   container commit or production volume as the fixture. Use a new disposable volume,
   synthetic user/configuration/data and development-only credentials. No production
   provider calls, real chats, shared production DB/queue, public ingress or legacy
   serving dependency. Test ports must bind VM108 loopback. Preserve existing dev
   services and check available disk/memory before staging the image. Use a dedicated
   `/srv/dev-data/workspaces/cbm-openwebui-migration-20260920` workspace.
4. Exercise the replacement's actual login, persisted functions/settings, retrieval
   integration with an isolated development endpoint, service credential delivery
   and renewal, old-credential rejection, and container restart/recovery. Verify
   the actual application/filter cache, not just SQLite rows or mocked API responses.
   If a model list is needed, use a synthetic fixture without paid inference. Record
   fixture and real-integration boundaries explicitly. Never solve a blocked test by
   pointing it to the dormant old VM. Return exact blockers instead of overstating
   acceptance. Any helper/configuration implementation must be source-controlled as
   a reviewable candidate and tested on VM108; include source/diffs in the response.
5. Prepare the migration/rollback inputs for Forge: exact candidate source/image
   manifest and test receipts; protected production data-transfer and restore steps;
   replacement consumer/renewal routing; endpoint/authentication cutover requirements;
   and checks proving production no longer depends on n8n-automation. Assess VM109
   capacity/placement read-only against the existing Community Brain destination;
   report constraints rather than provisioning another host or choosing a new stack.
   Also identify current renderer/host/image-pin changes needed to preserve the
   already VM108-tested application stabilization image
   `sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b`.
   Do not bypass immutable manifests or modify r020 in place.

If the full development rehearsal cannot finish promptly, publish safe inventory
and the precise remaining dependency in the response while work continues. Aim to
return the development handoff by September21 20:00 UTC, leaving time before expiry.
No expiry deadline authorizes a production shortcut or restoration of the old VM's
production role. Keep any necessary private preservation material in its existing
controlled stores; report paths/checksums only.

## Response and ownership

Claim once and follow PROTOCOL.md. Return `status.json`, `receipt.md`, safe inventory,
source/image hashes, development acceptance results and cleanup/retained-fixture
status under this request's response directory. Separate completed checks, unknowns,
remaining production gates and rollback limits. Forge owns application source and
will reconcile the returned candidate into the canonical checkout. Preserve current
management source provenance: Request024 demonstrated modified/untracked operator
files, so a Git HEAD alone is not an exact deployed-source reference.

Do not remove preserved user data, alter the legacy fallback, or retire VM101.
Production migration follows a concrete reviewed packet and successful VM108
validation; this request is preparation and development only.

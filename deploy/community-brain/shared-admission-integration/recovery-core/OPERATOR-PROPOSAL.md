# Bounded protected capture and independent restore proposal

Status: reviewable preparation; **no capture/transfer authority granted or used**.
Request030 deadline is2026-09-21T20:00:00Z. A later request must name its own capture
ID, authorization and deadline. Expiry is not permission to skip these gates.

## Exact bindings

Current Community Brain is VM109, `pchouinard@10.1.30.21`,
`community-brain-prod`. Incumbent API container ID is
`766a37a09d4ce16a4c69a8d3dd0634bc155de70085efb0eb6aad7d7281c528f6`.
The application consumes `CB_DATABASE_URL`; its authority source is Infisical
project `a508e594-7686-43a1-9b0f-cafa8b348ad4`, environment `prod`, path
`/applications/community-brain`, key `CB_RUNTIME_DATABASE_URL`. The deployed
`integrations/manual_api_runtime.py` explicitly maps those names.
The current database is `community_brain_prod`, server
`platform-db.patchoutech.lab` (`10.1.10.50:5432`), PostgreSQL18.6,
runtime role `cbm_prod_runtime`; public table owner is `cbm_prod_migration`.
Use existing `pchouinard@10.1.10.50` plus `sudo -n -u postgres` for the logical
backup/fence. This avoids exporting a database credential into a new store.
No role, grant, authority value or service identity changes are proposed.

VM109 trees: `/srv/community-brain/{files,config,corpus,meeting-archive-20260910,
automation,automation-public,manual-approvals}`. Private runtime configuration is
`/etc/community-brain-production` (nine existing0600 files). Runtime/management
source includes the exact mounted `workspaces/cbm-workspace-recovery-20260917-effective-r020`,
`workspaces/cbm-workspace-recovery-20260917-frontend`,
`workspaces/manual-20260910` and its Compose overlays, and Mac
`/Users/pchouinard/.local/lib/community-brain-management` plus the corresponding
LaunchAgent plist. Preserve existing bytecode as data; do not import the packet
while inventorying it. Record image IDs and all mounted source hashes.

Dormant WebUI source is the **stopped container**, not a powered-off guest:
VM101 (`n8n-automation`, `pchouinard@10.1.30.10`) still hosts other services.
Container `open-webui`, ID
`83358b76e0544437bd8947ba9a7be94d9fba59559a6dc56bd3c1c0110fb8a33c`,
uses `open-webui-data` at `/var/lib/docker/volumes/open-webui-data/_data`.
It has stayed exited since2026-09-19T04:20:05.394478381Z. Never start it, reboot
VM101 or change its other services. Signing bytes are outside the volume at
`/app/backend/.webui_secret_key`; the17-byte file has SHA256
`7638e389c27761152e8c894b9fff5b328e78964225e51c9514f3273dde931ef5`.
Request030 hashed it in memory on the source host and returned only metadata.
No signing value was transferred or saved to a new store.

Existing backup anchors: VM109's
`/srv/community-brain/db-backups/20260921T003017Z.dump` (62,548bytes), and PBS
`pbs:backup/vm/101/2026-09-21T01:00:01Z`. The protected September9 VM101 snapshot
remains listed. Neither a listing nor the existing DB dump establishes a paired
current restoration. PBS datastore is `PBS1` at `/mnt/datastore/PBS1`, server
`10.1.60.10`; retain its managed snapshots and pruning settings unchanged.

Proposed new off-host location is **outside the managed PBS datastore**:
`root@10.1.60.10:/var/lib/proxmox-backup/cbm-protected-recovery/<capture-id>`.
The root filesystem has about414GiB available. It is an access-controlled private
SSH destination, not a claim of new at-rest encryption or automatic PBS coverage.
Create parent/attempt directories root:root0700; every transport object0600.
Do not write arbitrary files inside `/mnt/datastore/PBS1`.
The Mac internal volume has only about3.9GiB available; it is not a staging target.
The encrypted external NVMe has ownership disabled and is not the selected target.

Proposed independent restore is VM108
`/srv/dev-data/protected-restores/<capture-id>` (root:root0700), with
fresh container `cbm-private-restore-<capture-id>` and a new PostgreSQL18.6
server/database on network `none`, no published ports, restart `no`.
This is a **private offline recovery enclave**, not an application development
clone. No WebUI, model, worker, scheduler or provider starts against the real data.
Protected content/signing may enter this enclave only if the next authorization
explicitly names it. Otherwise this step remains unperformed. The proposed source
capture locations are `/var/backups/cbm-protected-capture/<capture-id>` on VM109
and VM101, and `/var/lib/postgresql/cbm-protected-capture/<capture-id>` on the DB
host. They have not been created.

## Selected scope and limits

Request the following single phase: one consistent current CB database/state pair,
one stopped WebUI volume/signing pair, preservation of exact runtime/control
sources, private off-host copy, and independent offline restore/verification.
Do not include real-data application startup, sanitization for development,
production installation, ingress, rotation, provider calls or processing resume.
Preservation copies retain original content and configuration. **Permitted real
content in ordinary development fixtures: none.** A future sanitized real-data
clone requires a separately named destination, field-level transformation manifest
and authority. An environment variable alone cannot neutralize persisted WebUI
provider URLs, API keys, function valves, tools or OAuth/API sessions.

Use a new ID such as `cbm-protected-20260921-approval01` only after authorization;
reserve it atomically on each host. The private parent manifest names all component
submanifests and their hashes. Never assemble components from different IDs or
attempts. Every failed attempt keeps its own intent, partial objects and disposition.

## Ordered operation and concrete command forms

These are **future operator commands**, not commands executed by Request030.
The operator binds the approved ID/hash/deadline in a private0600 specification.
The source library archive must match the delivered SHA before installation. Its
CLI remains synthetic-only; a reviewed operator wrapper calls the library with
explicit `scope='authorized-private-preservation'`. Do not weaken the CLI guard.

1. Acquire the existing Mac scheduler mutex
   `/Users/pchouinard/.local/state/community-brain-management/scheduler.lock`.
   Refuse unresolved management/pending activation intents. Hold it through the
   complete capture/readback interval. Open existing VM109 locks in order:
   `automation/runner.lock`, `files/.manual-worker.lock`, `files/.submission.lock`.
   Bind inode/device and all three paused/attention/boot marker identities from a
   fresh read. Root remains held. Also freeze Mac intake writes for this bounded
   interval through its existing mutex; no live desktop-intake configuration change.
2. Record a durable intent with incumbent ID/config and rollback owner before the
   separately approved maintenance stop. Execute `docker stop --time 30
   766a37a09d4ce16a4c69a8d3dd0634bc155de70085efb0eb6aad7d7281c528f6` on VM109.
   This stops only the current API writer; Alloy stays running. Verify no other
   worker/container binds the seven source trees read-write and no unreviewed DB
   client remains. VM101 WebUI must already be stopped; never stop/start its other
   services. Abort if its ID or stopped state changed.
3. On platform-db, keep one existing-admin `psql -X -qAt -v ON_ERROR_STOP=1
   -d community_brain_prod` session open under `sudo -n -u postgres`. Issue:

   ```sql
   BEGIN ISOLATION LEVEL REPEATABLE READ;
   SET LOCAL lock_timeout='5s';
   LOCK TABLE public.alembic_version, public.cb_artifacts, public.cb_attempts,
     public.cb_jobs, public.cb_model_calls, public.cb_operations, public.cb_outbox,
     public.cb_rejected_events, public.cb_sources, public.cb_stages IN SHARE MODE;
   SELECT pg_export_snapshot();
   ```

   Recheck this is the complete current public table set; unexpected schema aborts.
   Keep the transaction open through the DB dump and VM109 tree capture. Capture
   canonical schema/table/sequence/relationship observations inside this interval.
   No DDL is allowed by the writer inventory. The returned snapshot ID is metadata,
   not a credential. In a second existing-admin process, run:

   ```text
   sudo -n -u postgres pg_dump -d community_brain_prod -Fc --no-owner --no-acl --snapshot <exported-snapshot> --file /var/lib/postgresql/cbm-protected-capture/<capture-id>/database.dump
   ```

   The wrapper creates the attempt directory postgres:postgres0700 before this
   command and verifies pg_dump18.6. VM109 has no host pg_dump; do not assume it does.
   Transfer the dump privately into the matching VM109 attempt's database component,
   comparing byte length and SHA at both ends. No password appears in arguments.
4. Still inside the writer-free interval, call `recovery.capture(components,
   destination, capture_id, evidence, scope='authorized-private-preservation')`.
   `components` binds the seven exact VM109 trees, `/etc/community-brain-production`,
   the exact runtime sources, and the staged database component. Each component is
   a distinct nonoverlapping directory. Preserve numeric uid/gid/mode/mtime and
   empty roots. Preflight largest file versus memory and ACL/xattr/hard-link needs;
   this version must refuse unsupported metadata. Include the held lock files in
   recovery data but never restore them onto active source filesystems.
5. On VM101, use `docker cp
   83358b76e0544437bd8947ba9a7be94d9fba59559a6dc56bd3c1c0110fb8a33c:/app/backend/.webui_secret_key -`
   **only into a private in-process tar reader**, never stdout/log capture at the
   orchestration boundary. Require exactly the expected regular member; save its
   bytes as0600 in the new private signing component. Retain original metadata in
   its private manifest. Capture the stopped volume as a separate component with
   the library, together with signing. Verify the source key digest, SQLite/WAL
   state, counts and container stopped state before and after. No Infisical write
   or key rotation is involved: this is preservation, not a new credential.
6. Hash and seal the parent private manifest with all submanifest hashes. Release
   the DB fence using `ROLLBACK;` only after all relevant CB source components have
   completed. Recheck holds/inodes/source digests. Restart **the same incumbent ID**
   using `docker start 766a37a09d4ce16a4c69a8d3dd0634bc155de70085efb0eb6aad7d7281c528f6`;
   verify its exact configuration, health and existing authenticated monitoring.
   This does not recreate it or resume processing. Record release before the Mac
   mutex is freed. Planned API maintenance ceiling:10minutes; if exceeded, abandon
   the incomplete capture and restore the incumbent under the same locks.
7. Stream completed bundles over existing SSH to the fresh PBS directory, with no
   Mac disk intermediate. A transport tar contains only bundle metadata and regular
   content-addressed blobs. The receiver rejects absolute/parent paths, duplicate
   entries, links, devices and an unexpected exact member set before acceptance;
   never invoke unrestricted `tar.extractall`. Verify parent/submanifest/object
   hashes on PBS before recording off-host completion. Keep incomplete receiver
   directories and read back them after connection loss; do not resend blindly.
8. Restore **from the PBS copy** into the new VM108 enclave using the pinned parent
   manifest and `recovery.restore(..., expected_scope='authorized-private-preservation')`.
   A new network-none PostgreSQL18.6 container runs `pg_restore -U <fresh-local-role>
   -d <fresh-database> --exit-on-error --no-owner --no-acl` against the copied dump.
   Source numeric ownership is preserved in the original restoration; any runtime
   ownership remap must happen only in a separate clone and be recorded. Compare
   durable records, schema/sequences, unknown outcomes, outbox/artifact/source links,
   exact files and vector/FTS observations. Run SQLite read-only integrity/relationship
   checks and pinned Chroma/LanceDB read-only queries. Never start the application
   to make migrations or indexing "fix" a mismatch.

The production wrapper, reviewed binding of the tested `transport.py` receiver,
and bounded maintenance/readback sequence must receive their final exact source/hash review and interruption test
before a transfer authorization is executable. Request030 validates the underlying
file/DB/session mechanics, not a deployed production orchestration wrapper. This
is an explicit remaining implementation gate, not an invented completed receipt.

## Failure, rollback and retention

Operator and rollback owner: home.servers acting for Patrick; Patrick owns release
and retention decisions. On uncertainty, retain intent and source holds, discover
actual state and read the same attempt. Never resume a partial capture under a new
snapshot, replace a partial restore, clear attention/checkpoints, or restart VM101.
A lost DB fence invalidates the attempt even if files look complete. On uncertain
API restart, inspect its exact ID before doing anything else. No blind redispatch.

Source originals and existing Request026–029/Forge fixtures are retained without
expiration. Proposed new private originals/off-host recovery/failed attempts:
minimum30days and through explicit replacement acceptance, whichever is later;
no automatic deletion. Restored enclave remains stopped and private. Any later
replacement writes are retained separately; serving rollback never overwrites
those writes, reverses migrations or merges divergence automatically.

Current service-identity expiry is2026-09-22T20:53:07Z. Proposed latest start for a
new two-hour bounded phase is18:53:07Z that day, subject to a fresh shorter service
certificate/authority deadline if found. Approval does not extend any identity.
If enough time or any evidence is missing, defer transfer and report the blocked
phase. No production renewal is part of this proposal.

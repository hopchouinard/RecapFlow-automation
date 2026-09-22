# Production mapping closure packet

September22. This is implementation/review work, not production execution authority.
Current baseline: Request032 source manifest
`48675b902dceb1d8ba4fb43e4a362dca0ee68177801431d25ba874ce0ebf01b7`.

## Database: actual census replaces assumed fixture topology

Forge used the incumbent API's existing runtime identity in a repeatable-read,
read-only transaction with10-second statement limits. No application rows or
credentials were exported. PostgreSQL is18.6; database `community_brain_prod`;
observer `cbm_prod_runtime`; only application schema `public`, owned by
`cbm_prod_migration`; only extension `plpgsql` in `pg_catalog`. Both named roles
can log in but are not superusers/role creators/database creators/replication or
RLS-bypass roles. Ten tables and19 indexes; **zero sequences**:

`alembic_version`, `cb_artifacts`, `cb_attempts`, `cb_jobs`, `cb_model_calls`,
`cb_operations`, `cb_outbox`, `cb_rejected_events`, `cb_sources`, `cb_stages`.

No custom types/routines were found. Inspected event triggers, foreign servers,
large objects, policies, publications and extended statistics counted zero.
`observed-profile.json` binds the exact initial metadata census, including observed
ACLs and column types. Forge comparison tests detect changes without declaring
full compatibility or restore acceptance. Runtime-role coverage is preliminary;
administrator census is still needed for subscriptions, cluster/shared objects,
application role membership, writer census and unsupported-class coverage.

The Request032 hard-coded public/app/audit schemas, pgcrypto, fixture role names,
fixture tables and sequence assumptions must not be applied to this database.
Implement a separate explicit application profile with empty sequence support,
actual job/artifact/source/attempt/operation/outbox relationships, model-call and
rejected-event preservation, and unchanged Alembic revision. Use schema-only
source/migrations and synthetic rows for dev fixtures. Shared database server
roles outside this application must not be revoked, terminated or rewritten.

## Management helpers: required complete effect inventory

Installed scheduler source snapshots identify nine logical helpers. Each needs
exact deployed source hash, target/effect list, readback and recovery semantics,
and a VM108 receipt. `mappings.py` validates completeness and rejects missing
proof, replay policies or a legacy production dependency. Shape validation alone
does not verify source/receipt bytes and never enables production execution.

| Helper | Contract to resolve from actual source |
| --- | --- |
| pre-pbs-copy | Paired recovery-copy destinations, atomic completion and partial-copy readback. |
| mac-intake poll | Intake ownership; preserve legacy recovery without restarting it or retaining a production dependency. |
| renew-service-tokens | Current consumer list and successor WebUI replacement; authority generation and uncertain renewal reconciliation. |
| provision-nats-tls | NATS identity/configuration effects and recovery without replacing unrelated shared services. |
| renew-app-tls | Certificate generation, deployment/readback and unchanged-incumbent rollback. |
| copy-backup | Exact off-host destination, verified object identity and incomplete-transfer handling. |
| management-health | Actual health/monitor outputs, publication boundaries and stale-state handling. |
| checkpoint consumer | Existing retained checkpoints and unknown outcomes; admission must never acknowledge them as a capture side effect. |
| monitor publish | Heartbeats may report blocked admission but must not bypass admission to mutate application state. |

Common admission must wrap the complete actual scheduler/manual cycle, with no
nested mutex deadlock and no direct helper bypass. Source lives on the Mac;
Forge does not have that administration access. Request033 requires exact source
and integrated adapters, not another synthetic health-only substitution.

## Service and boot bindings

Fresh read-only VM109 observation confirms incumbent API ID
`766a37a09d4ce16a4c69a8d3dd0634bc155de70085efb0eb6aad7d7281c528f6`, image
`sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449`,
running since September19 21:21:38UTC. Keep exact incumbent for rollback.
Alloy is separate and remains outside maintenance. API restart policy is
`unless-stopped`; a systemd admission target alone cannot control Docker's own
restart behavior. The mapping must explicitly distinguish serving recovery from
processing admission and account for that startup ordering.

Existing enabled `community-brain-automatic-pause.service` requires the state mount,
runs after local filesystems and before cron, and calls the retained boot guard.
That guard marks processing paused/unreconciled on boot; its tick still emits
bounded status through the old automatic launcher. Preserve this safety behavior.
New maintenance recovery must not clear processing holds, checkpoint/attention or
boot reconciliation state. Bind mount, Docker, current machine/boot, locked control
directory, immutable packet and exact incumbent. Validate the integrated service
ordering on isolated VM108 fixtures; persistent installation remains a later phase.

## Private preservation/acceptance contract

Pair PostgreSQL with VM109 files/config/corpus/meeting archive/automation/public
status/manual approvals and private runtime configuration; separately preserve
VM101's dormant WebUI volume plus original signing file outside that volume.
VM101 must remain stopped for WebUI; its unrelated guest services remain untouched.
No regeneration, re-embedding, checkpoint acknowledgement or unknown-outcome replay.

Earlier proposed off-host destination was PBS host10.1.60.10 under
`/var/lib/proxmox-backup/cbm-protected-recovery/<capture-id>` outside its datastore;
recheck ownership, capacity and retention before finalizing. No encryption or
scheduled-backup coverage is implied. The previously proposed offline VM108 private
restore enclave was not authorized; resolve an explicit private destination and
scope in the final plan. Ordinary synthetic development and relay must contain no
private production content or signing material.

Exact component membership, metadata/link policy, source/receiver manifests,
independent DB restore, application relationships/file hashes, vector/FTS identity,
WebUI SQLite/Chroma/uploads and original signing digest must be bound. Keep actual
session/browser acceptance separate from offline restoration. Retain originals,
partial attempts and replacement writes. Serving recovery has an independent
bounded deadline; comparison need not delay restoring the unchanged incumbent.

## Closure and evidence

Forge completed the read-only census, current service/control inventory and
metadata/helper contract checks; five tests passed locally and on VM108. These
are mapping checks, not full adapter/recovery acceptance. No production state was
changed. The census is diagnosis permitted by the standing dev-first policy.
The helper source, admin catalog coverage, final adapter and service/private
bindings require home.servers access. Request033 asks it to close those exact
items and return final source plus VM108 validation, or itemize a specific blocker.
Do not call production mappings complete until that evidence is reconciled.

[Initial census](receipts/cbm-production-mapping-20260922/runtime-catalog-census.json),
[runtime/control bindings](receipts/cbm-production-mapping-20260922/production-runtime-bindings.json),
[existing boot service](receipts/cbm-production-mapping-20260922/production-pause-unit.txt),
[VM108 checks](receipts/cbm-production-mapping-20260922/vm108-tests.txt).

# OpenWebUI and stabilization successor packet — preparation record

Date: September20. Status: **development baseline accepted; not deployable yet**.
Request026 has been verified and acknowledged. This document reconciles its
findings with the accepted continuation; it is not a production execution script.

## Integration follow-up — September20

[The subsequent VM108 integration](cbm-openwebui-integration-results.md) passed
actual Community Brain retrieval through WebUI, the five-identity policy with
real API recreation/WebUI delivery and simulated authority/other consumer bundles,
fresh-volume/Chroma restore, and extended load across a complete synthetic pipeline.
The earlier pending-test statements below describe the Request026 checkpoint.
Request027 subsequently passed actual development Infisical, consumer monitoring
and lease integration. See [management results](cbm-management-integration-results.md)
for accepted evidence and current remaining gates. The imported development renderer
still needs deterministic serialization and production/worker bindings validated
on VM108. The table below retains the original preparation checklist; the linked
results establish which development tests have since passed. Production is unchanged.

## Successor follow-up — Request028

[Forge validation](cbm-successor-validation-results.md) closed cross-filesystem
packet reproducibility and exercised selected-worker execution with synthetic
providers and real development DB/queue/index state. Full host launcher, scoped
transport/budget, production-equivalent mounts and resource bindings remain open.
Request028 carries the actual source/runtime differences to home.servers for the
complete VM108 integration. Protected real restore/browser and promotion gates
remain unchanged.

## Request028 accepted — September21

[The successor results](cbm-successor-bindings-results.md) establish full synthetic
manual/automatic host execution, scoped TLS queue, paired restore and actual
management renewal. Source and final packet are independently reconciled. The
production descriptor is present but the runtime loader deliberately rejects
production execution. Controlled activation/rollback implementation with VM108
validation is next, followed by protected real restoration, browser and capacity/
provider gates. Earlier pending integration statements describe prior checkpoints.

## Serving activation rehearsal — Request029

[Forge's controller](cbm-activation-development-results.md) passed real development
API/WebUI activation and same-incumbent rollback while retaining new WebUI writes
and all processing holds. Request029 integrates the actual Mac/SSH transport and
complete production plan bindings on VM108. This does not close protected real
restoration, browser, capacity/provider or production-phase gates.

## Request029 accepted — September21

[Actual Mac/SSH activation integration](cbm-activation-integration-results.md) passed
and its source/packet/plans are independently verified. The 21 production evidence
slots remain open, grouped into protected restoration/browser acceptance, workload
checks, fresh deployment bindings and the separately authorized production phase.
The production compiler/controller remains disabled; serving success will not clear
processing holds. The next preparation task is the protected real-data/signing
restore packet. Retained WebUI writes are not automatically visible in the old UI.

## Protected restoration packet — Request030

The [prepared restore packet](cbm-protected-restore-packet.md) now specifies current
VM109 data preservation, dormant VM101 WebUI/signing source treatment, separate
sanitized development copies, private evidence and browser/recovery acceptance.
Request030 resolves exact operator bindings and validates any new recovery mechanics
on VM108 before a protected capture/transfer proposal. No real data was moved.

## Request030 accepted — September21

[Preparation results](cbm-protected-restore-preparation-results.md) provide exact
private source/destination bindings and synthetic session/restore evidence. The
strict WebUI inventory is about1.18GB of regular-file bytes; the historical2.34GB
count followed cache links. Data/signing originals were not transferred. Finish
capture-wrapper interruption/deadline handling and component-receipt validation
before requesting the bounded protected phase. Capacity/provider and browser/real
staged-session gates remain open; production compilation stays disabled.

## Accepted source and evidence

The exact seven-file rehearsal source from agent-ops commit
`f7356151a563d4d07f390872efd9265b6b9302bf` is imported at
[`deploy/community-brain/openwebui-development`](../../deploy/community-brain/openwebui-development/README.md).
It remains a development harness. Forge verified all21 receipt artifact hashes,
all7 source hashes, and independently compared the6 Python files to VM108.
Both retained fixture containers are stopped with no OOM recorded.
[The evidence](receipts/cbm-openwebui-dev-20260920/receipt.md) separates real
OpenWebUI operations from synthetic retrieval/model-list responses.

Real OpenWebUI0.8.12 login, exact filter execution/cache, API credential delivery,
old-key rejection, deliberate retrieval failure/recovery, and restart persistence
passed. Synthetic chats, uploads, models and prompts survived restarts. This is
restart persistence evidence, **not a fresh-volume restore test**. No actual
Community Brain retrieval, five-identity Infisical renewal, vector restoration,
production TLS or concurrent processing capacity acceptance is claimed.

The imported image has engine ID
`sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b`.
Its configuration, architecture and ordered layers match the original, as recorded
in image-equivalence.json. Keep that verified identity relationship in the packet;
do not assume the source engine ID is addressable on every destination engine.
Preserve the application stabilization image
`sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b`.

## Remaining implementation and acceptance

| Work | Concrete implementation/acceptance required |
| --- | --- |
| Replacement runtime | Produce an immutable VM109 candidate with pinned WebUI image, owned persistent volume, explicit signing-key delivery, resource limits and loopback staging. Exercise the same configuration on VM108. Keep existing local authentication semantics; do not silently switch to OIDC. |
| Real retrieval integration | Connect WebUI to the actual Community Brain candidate on isolated VM108 state, using a synthetic indexed corpus and scoped development identity. Verify the exact live filter, authentication, context and denied requests through the real backend. No production endpoint or provider spend. |
| Renewal and recreation | Route management to the replacement host/container. Test the complete existing five-identity journal workflow, overlap, interrupted delivery/resume, consumer acceptance, revocation and fresh monitoring with development authority. Prove no SSH or serving request to VM101. API recreation must retain the tested stabilization image/modules/UI. |
| Consistent helper packet | Reconcile run.py and indexing image pins; eliminate superseded r020 module/frontend overlays from the effective candidate; update successor manifests, manual_api_runtime checks, boot launchers, recovery file/image inventory and management controls. Keep r020 immutable and holds intact. |
| Restore | On VM108 rehearse backup to a fresh volume with synthetic relational, upload and vector state plus signing material. Validate database integrity, relationships, hashes, auth, cache and data through the application. Prepare the protected real-data transfer manifest and before/after checks without moving private data into Git or relay files. |
| Capacity | Measure concurrent API/WebUI/worker and restore behavior on VM108 within the destination's memory budget; record peaks, limits, failures and headroom. Idle observations do not establish capacity. Do not provision/resize production to bypass this test. |
| Ingress and monitoring | Prepare a distinct reviewed WebUI hostname/TLS route and authentication/signup policy. Preserve the API endpoint. Add replacement UI readiness checks; replace legacy serving allowlist/routing only after verifying the replacement source address. Preserve backup-host monitoring. |
| Promotion and rollback | Bind exact source/image/configuration hashes and protected before-state. Define ordered locks, staged verification, credential authority, data preservation after new writes, paired recovery and safe aborts. Rollback must not restart VM101 or overwrite replacement data with the dormant copy. |

## Data preservation detail that changes the packet

The old installation has60 chats,111 files,5 models,10 prompts,1 knowledge record,
and a Chroma store with113 collections/1,555 embeddings. Its persistent tree is
approximately2.34GB. These are September20 inventory counts, not a restore result.

The effective signing key is `/app/backend/.webui_secret_key` **outside the data
volume**; the environment setting is empty. A volume-only transfer is incomplete.
Preserve that key through the existing controlled secret authority and include its
safe hash/verification in the migration plan. Keep uploads, vector state, database,
configuration and required trust material. Reconcile persisted endpoint overrides,
including the old host.docker.internal embedding setting, before enabling traffic.
No private user content or secret values belong in source or handoff receipts.

## Production state and ordering

VM101 remains a dormant recovery fallback. No credential delivery or restart to it
is part of this plan. Request026 changed no production services; the automatic
runner remains held. All five service identities were still due to expire
September22 at20:53:07UTC, and the authoritative journal phase was completed.
The expiry is an operational deadline, not permission to bypass development tests.

Implement the replacement runtime and real retrieval/renewal integration first,
then close fresh-volume restore and concurrency acceptance and bind the coherent
promotion packet. Protected production transfer, deployment/cutover and runner
reconciliation follow the appropriate production phase; this preparation does not
execute them. Weekly-cycle evidence and retirement remain outstanding afterward.

## Capture controller development — September21

See [Forge results](cbm-capture-controller-development-results.md):49 tests passed on
VM108 plus retained synthetic recovery. Request031 covers remaining host orchestration
and database evidence validation. Production execution remains disabled.

## Request031 consumed — September21

[Verified integration results](cbm-capture-controller-integration-results.md):32 final
source files independently match VM108; eight recovery scenarios and51 negative
checks passed. Source imported unchanged; Forge49 tests pass. Native Mac fixtures
have five metadata errors. Next is shared scheduler/manual/capture admission and a
production-shaped synthetic database validator, including unresolved recovery.
Production remains disabled; protected transfer is not yet ready for authorization.

## Shared admission increment — September21

[Forge shared admission core](cbm-shared-admission-development-results.md) passed
nine tests on VM108, including actual owner kill and cross-entry-point blocking.
[Request032](cbm-shared-admission-integration-request.md) covers installation into
candidate scheduler/manual/capture paths, authoritative recovery and the remaining
production-shaped synthetic database validator. Production remains disabled.

## Request032 consumed — September21

[Reconciled results](cbm-shared-admission-integration-results.md):49 final source
files independently match VM108. Shared candidate admission, failed-finalizer/startup
handling and expanded PostgreSQL evidence passed. Forge reran58 tests. Mac fixture
errors are resolved. Next is actual helper/catalog/service/private-restore mapping,
then validation of changed bytes on VM108. Production execution remains disabled.

## Actual production mappings — September22

[Mapping closure packet](cbm-production-mappings.md) now binds a fresh read-only
production census and boot/runtime inventory. Actual DB has public/plpgsql, ten
tables,19 indexes and no sequences; Request032 fixture topology is not its profile.
Five mapping checks passed on VM108. Request033 must close real helper/admin catalog/
service/private-restore mappings and return final tested source. Production remains
unchanged and mappings are not complete until that evidence is reconciled.

## Request033 consumed — September22

[Production mappings are closed at candidate level](cbm-production-mapping-integration-results.md):
152 source files independently match VM108, all nine helper proof bindings verified,
and65 Forge tests pass. Next is qualification of the mapped implementation and an
executable bounded production controller. External protocol fixtures are not live
consumer/CA acceptance. Protected transfer, session/vector/capacity acceptance and
persistent enrollment remain unproved; production execution stays disabled.

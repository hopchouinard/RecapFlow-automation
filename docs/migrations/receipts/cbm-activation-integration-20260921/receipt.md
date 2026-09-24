# Request029 verification receipt

Request: `CBM-ACTIVATION-INTEGRATION-20260921-029`  
Actor: `home.servers`  
Returned: 2026-09-21T02:52:54.748546+00:00

## Outcome

Development integration and VM108 verification completed. The claimed request's
five supplied documents were hash-verified before execution. Production runtime,
configuration and holds are unchanged; VM101 was not contacted. No production
installation, protected data/signing transfer, rotation, ingress, cutover,
processing resume or retirement occurred.

Source commit: `db6416c7a2ab679a800a5a3e047a6554295cfc80` on `codex/request029-activation`. Clean; **not pushed**.
Base: `afef7b1dc812ec986640dac88a6d3ad37bec9cb3`. The parent Home.servers gitlink and pre-existing dirty state were
not changed. Full source, source diff, Forge-to-integrated controller diff and
per-file provenance are attached.

## Verification receipts

| Boundary | Verified result |
| --- | --- |
| Plan/compiler | All sealed current and referenced packets, manifests, Compose/environment/CA and external signing configuration, recovery artifacts, incumbent ID/configuration, hold hashes/modes/inodes/devices and external WebUI volume identity bound. Stale/incomplete/drifted plans refused. |
| Mac/VM ownership | Existing Mac scheduler mutex excludes another caller. Target owns runner/manual/submission locks in order, without a nested quiet lease. Each busy lock refused before an activation journal or serving effect. |
| Actual SSH loss | Actual SSH client terminated while detached target worker continued. Independent readback saw all VM locks and the Mac mutex retained, with both worker launchers excluded. Same operation completed; no redispatch or recreation. |
| Duplicate/terminal calls | Duplicate activation preserved IDs, creation/start times and restart counts. Activation after terminal rollback refused. Candidate management entry also refused effects while activation was active. |
| Failure rollback | Deliberate API health-probe failure and API-success/WebUI-health-probe failure both rolled back to the exact incumbent ID and configuration. Candidate containers and failed journals retained. |
| API/filter | Five development subjects accepted with correct scope denials; anonymous access rejected. Actual OpenWebUI application/filter returned the synthetic corpus source. |
| Monitoring | Actual Kuma and Prometheus acceptance newer than activation and rollback; credential bundles consumed by real API probes. |
| New writes | A new synthetic chat created through the replacement WebUI API survives rollback in its external volume; SQLite integrity passes. No old backup copied over it. |
| Restoration/preservation | Paired PostgreSQL, durable-state and WebUI restoration passed. All 28 recovered state files and the post-test database observation match; all 255 bound files per plan and exact holds remain unchanged. |
| Renewal | Real development Infisical cycle resumed the same generation after intentional lost delivery acknowledgment, verified overlap and consumers, then rejected all five old tokens. Three API recreations preserved image, six mounts, limits and holds. |
| Immutable sources | All six packet revisions remain exact with no bytecode. Final packet reproduces byte-for-byte. Renewal policy and production budget helper remain unchanged. |
| Tests | **30 boundary tests on Mac, 30 on VM108, 293 parent tooling tests: all passed.** |
| Cleanup | All 12 Request029 containers stopped and retained; only seven still-running fixture containers needed stopping. Loopback relay stopped, listener closed, VM locks released, no detached controller remains, no pending transport outcome. |
| Baselines | All 32 pre-existing development containers and both production containers retain exact IDs, images, configuration fingerprints, start times and restart counts. Production hold hashes/inodes and protected r020 bytecode unchanged. |

Normal plan SHA256: `69f0eef62aea1e29a34e3ffe2700e1b1cbb4d25ca616cbb934c47260197afeec`  
Readiness-failure plan: `d5880b73dfe9f3659062f9871987d7fa80423a3700eb7b764acdc5e08e79d2cc`  
Partial-activation plan: `fa3284c6422fd9ba58328152b314b7c4eaf965459cf880a90d274ba88d22ca73`  
Final packet manifest: `c9326fd4bf149b68fcbc40fb7ab49a2ce23b4c7711a36ea9a5a99e8b41ebbb76`  
Candidate source archive: `25126133b356d277e8d1437f151458f6d8fa3d5366c9d2887bb57234eeb00706`

The supplied source was integrated into `management-activation-029`. Runtime
packets are retained under
`/srv/dev-data/workspaces/cbm-activation-integration-20260921-029/packet-v1` through
`packet-v6`. Actual activation plans are under `activation-*-packet-v6/`; journals
are in `activation-journals/`, and at-most-once operation records in
`activation-operations/`. The full safe plan/journal/operation set is attached as
`vm108-safe-evidence.tar`. Private runtime/recovery content remains on VM108.

## Versions, failures and evidence limits

Actual renewal used packet-v3, paired restore used packet-v4, and all completed
activation/rollback cases used packet-v6. The final controller binds both original
packet dependencies. Management recreation, profile, consumer, transport, runtime
contract and renewal-policy sources are byte-identical to the renewal-tested
configuration. `renewal-final-equivalence.json` lists exact hashes and changed
controller/fixture files. No completed renewal or workload was replayed to make a
receipt appear to originate on a later revision.

The first volume preparation refused valid relative model-cache symlinks in the
verified WebUI archive. Its partial volume remains retained. The corrected fixture
allows links only within the new disposable volume. A subsequent preflight exposed
an upstream Docker adapter defect: generic `inspect` treated a same-named retained
volume as a candidate container. It refused before any activation journal or
serving effect. Inspection now explicitly requests containers and has a regression
test. Prior packets, plans and failed operation results remain intact.

`early-failures.json` also records the pre-authority Python CA refusal, a correct
Mac mutex refusal, the updated loopback-port test expectation and a local cleanup
serialization error that occurred before SSH existed. These are not represented
as clean first-attempt passes.

VM108 Docker records PortBindings for its internal network without opening a host
listener. The explicit `development_loopback.py` fixture relayed health traffic on
127.0.0.1:19930 and returned the exact sole running API container ID. Authenticated
API/filter and monitoring checks also used real internal-network services.
Endpoint receipts label the relay; Docker metadata alone is not treated as traffic
proof. No production ingress was installed or exercised.

All authority values used in tests came from the authorized development child
`/development/community-brain-dev/request029`; production token keys were not used.
Parent development values were verified unchanged at initialization. The source
and delivery scan found zero matches for the current development authority and
runtime secret values checked. No private data, environment values, signing keys
or management bootstrap credentials are included in the relay package.

## Production template, rollback and remaining gates

`production-serving-plan.template.json` is a **non-deployable review template**,
with the production descriptor, read-only current baseline and **21 outstanding
evidence slots**. Production compilation/serving and the worker loader remain
explicitly disabled. The candidate Mac pending-operation guard was tested but is
not installed into the deployed production scheduler; installation and its
integration remain part of the separately authorized production phase.

Still required: protected real database/corpus/upload/WebUI and external signing
restoration, off-host recovery acceptance, human browser/login/session/signup
acceptance, intended-load capacity, and real-provider/spending-budget checks.
Request029 used synthetic data/providers and did not re-certify paid inference,
Fathom acquisition or desktop intake. Processing stayed held throughout; original
Request028 completed and uncertain work was not resumed or replayed.

Rollback restores serving through the same incumbent container. It retains
replacement data and does not reverse database migrations or reconcile divergent
writes. The new WebUI chat remains in the replacement volume, not automatically
in the incumbent interface. An absent uncertain candidate, changed hold, changed
bound input or changed incumbent still requires explicit reconciliation.

All disposable volumes, private authority, recovery artifacts, failed attempts
and journals remain retained. The final cleanup leaves every Request029 container
stopped. Earlier fixtures are unchanged. Do not replay setup against retained state.

Request deadline: **September 21, 2026 at 20:00 UTC**. Verified production identity
expiry: **September 22, 2026 at 20:53:07 UTC**, with renewal journal completed.
Expiry does not extend authorization or permit bypassing the remaining gates.
Previously approved ingress needs no repeat approval once its target is ready;
this request did not execute it.

Machine-readable summary: `verification-receipts.json`. Exact sizes and SHA256s
for every delivered artifact: `artifact-manifest.json`.

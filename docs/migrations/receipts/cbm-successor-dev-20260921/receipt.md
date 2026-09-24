# Request028 verification receipt

Request: `CBM-SUCCESSOR-BINDINGS-20260920-028`  
Actor: `home.servers`  
Returned: 2026-09-20T23:12:29.258590+00:00

## Outcome and boundaries

Development successor implementation and VM108 validation completed. Production
execution remains disabled. No production application/source/credential/hold,
monitor, collector, DNS, Traefik or Step CA changes were made. VM101 was not
contacted and stays recovery-only. Retained Request026/027/Forge fixtures remain
preserved. This receipt does not authorize a production phase.

The existing `homelab` Infisical project, environment `prod`, was used only for
fresh development material in `/development/community-brain-dev/request028`, as
Patrick authorized. The five identities reuse the policy's subject names but have
new development values. Parent development secrets were unchanged; production
keys were not used for validation. Management bootstrap credentials stay on the Mac.

## Verification receipts

| Boundary | Actual evidence |
| --- | --- |
| Forge reconciliation | Supplied source consumed; sorted builder and input/filesystem-order regression reconciled into agent-ops; seven original tests pass |
| Profiles | Explicit development/production descriptors; six API mounts, only files writable; 2 GiB and 2 CPUs; archive/public-status/CA and external signing paths bound |
| Queue | Real TLS-first authenticated NATS/JetStream; development stream, subject, inbox and principal; wrong password, empty trust store and four cross-profile settings rejected |
| Manual launch | Real inspect/execute subprocesses processed and indexed one synthetic meeting; each stage one attempt; duplicate execute refused |
| Automatic launch | Real scan/tick and manual subprocess chain acquired, processed and indexed the second meeting; first meeting and excluded work unchanged |
| Data/artifacts |17 rows,17 indexed by FTS, zero unindexed; catalog contains two processed meetings plus synthetic archive;13 artifact downloads hash-verified |
| Uncertainty | Third synthetic meeting stopped at outcome_unknown after one attempt; repeated execute refused; no uncertain effect replayed |
| Holds/boot | Held manual launch refused; runner quiet lock excluded automatic launch; wrong boot ID and unresolved attention rejected; only Request028 boot reconciled |
| Checkpoints | Tick stopped at completed work pending checkpoint; no new attempts. Acknowledgment followed actual paired restore, then the next meeting ran and gated again |
| Recovery | Independent PostgreSQL restore and durable-state comparison,62 matching files, captured external signing/runtime files, stopped-volume WebUI backup and restored SQLite integrity |
| Transport | Actual Mac mutex, ordered runner/manual/submission SSH locks, lost-response readback without replay, fail-closed lease loss; API writes503 under lock while retrieval remained available |
| Renewal | Intentional lost delivery acknowledgment; same cycle resumed; old/new overlap verified; actual bundles, WebUI cache, fresh Kuma and Prometheus passed; all five old tokens rejected |
| API recreation | Three recreations retained pinned image,20 module/frontend hashes, exact six mounts, 2 GiB/2 CPUs, read-only root, python -B and identical boot/hold hashes |
| Runtime |18 actual worker-container records verify image, network, limits, read-only packet/root and python -B |
| Integrity/tests | Final packet reproduces byte-for-byte; nine boundary tests pass on Mac and VM108; all14 sealed revisions remain exact with zero bytecode |
| Cleanup | Only seven Request028 containers stopped; no OOM; four baseline services retain exact start timestamps;12 earlier fixture containers remain stopped; Request027 private-file hashes unchanged |

Renewal cycle: `34a1d385-8c47-4a9c-a20d-1edcc0d19824`. Journal completed.
`renewal-acceptance.json`, `worker-runtime-evidence.json`, `test-acceptance.json`,
`cleanup-acceptance.json` and the other named JSON receipts contain the details.

## Source, packet and validation versions

Candidate commit: `6874753111c32bda26ea9f105dae4825ea10f9f8` on `codex/request028-successor`. Clean; not pushed.
Base: `3022cda148f9fd3b1732a687a40ba2220bcc90ef`.
Complete scoped source archive/diff, input provenance, both profile descriptors,
worker provenance and exact immutable manifest are attached.

Final packet: `/srv/dev-data/workspaces/cbm-successor-bindings-20260920-028/packet-v14`

Manifest SHA256: `c977c2a69c794141ef1c1bbf991ad7f44309ef172711e87d0806044679ad8b04`

The successful automatic full host run used packet-v9; manual success was first
recorded on packet-v6, uncertainty on packet-v10 and actual renewal on packet-v13.
Final packet-v14 adds explicit production provider/credential-file bindings.
Its development environment, read-only/indexing container arguments, provider
command/secret mapping and API/WebUI render are verified equal to the executed
configuration. Final VM108 held-launch checks passed. Completed jobs were **not
replayed** to pretend every receipt originated on the final revision. The
version/equivalence limit is explicit in `test-acceptance.json`.

Production descriptor selects the real selected-worker entry, separate acquisition
and bounded-model credential files, the preserved production queue and prior
Ollama endpoint. Production execution still fails closed. The production indexing
budget helper remains SHA256
`932e46c9cfb892c9b6eb51506f5948e8718795ee0f4f16a9ea6e860619bf6db7`;
the unchanged five-identity renewal policy remains
`8406820b5795e67f03ecc7521ab522aef7ff3aae9370ad30257ec286ce35d56c`.

## Current management and production reconciliation

Current management source remains the deployed, non-Git library
`/Users/pchouinard/.local/lib/community-brain-management`;25 captured files
still match the prior source receipt. This candidate was not installed there.
The live production API image and start timestamp match Forge's supplied snapshot.
The r020 extra bytecode remains unchanged:
`084a3fb857c3499d9198dcd40201e524fa5a4c2282e22e74998bd4f4ab21853f`.
It remains protected recovery evidence and still prevents a clean old exact-file-set
check. No file was deleted and no assertion bypassed to conceal that condition.

Metadata check: production renewal journal completed; identity expiry is
**2026-09-22 20:53:07 UTC**. The Request028 deadline is2026-09-21 20:00 UTC.
Expiry does not authorize skipping the remaining validation or restarting VM101.

## Failures, recovery disposition and remaining gates

`failure-reconciliation.json` preserves the bootstrap-lock, negative-test,
builder inclusion/cache, restore ownership/order, catalog and final-binding
findings. Each sealed attempt remains retained; no in-place revision edits or
uncertain-effect replay were used. These are not claimed as clean first attempts.

Private state, backups, external signing material, volumes and dev authority are
retained in the isolated Request028 workspace/folder. Only metadata and hashes
are returned; private data and credential values are excluded. Cleanup leaves
explicit disposable pause/attention markers and the uncertain stage unchanged.
Do not replay setup, clear markers or delete retained state without reconciliation.

Synthetic provider responses and allowance replacements were used. Paid-provider
behavior, spending/budget enforcement, real Fathom acquisition and desktop intake/
upload are **not certified**. The production budget implementation was preserved,
not exercised with production keys. The paired restore is synthetic, not a
protected production restore or an off-host disaster-recovery certification.

Remaining gates: review final production activation bindings; protected full
production data and external signing-material restore; human browser login/session
and signup policy; production-scale capacity and real-provider/budget validation;
and separately authorized source installation, rotation, cutover and processing.
Read `ROLLOUT.md` for ordered before-state, recovery and rollback boundaries.
Existing approval for chat.patchoutech.lab DNS/Traefik/Step CA remains valid when
the replacement is ready. Request028 did not execute ingress.

Artifact hashes and sizes: `artifact-manifest.json`.

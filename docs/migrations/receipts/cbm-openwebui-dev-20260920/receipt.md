# Request026 verification receipt

Request: `CBM-OPENWEBUI-MIGRATION-20260920-026`  
Actor: home.servers  
Completed: 2026-09-20T03:55:46.925641+00:00  
Outcome: read-only migration inventory, isolated VM108 rehearsal and rollout inputs delivered. **No production migration or renewal performed.**

## Verified development acceptance

The real OpenWebUI **0.8.12** application and exact existing filter passed on VM108:

- Real signup/signin; incorrect password rejected.
- Exact function source installed and active/global; settings updated through the authenticated application API.
- Actual application-process filter cache delivered synthetic retrieval context.
- Development credential overlap, delivery, effective cached-key verification, old-key401 and new-key200.
- Deliberate retrieval denial produced unavailable context; restoring acceptance recovered context.
- Container restart preserved login, functions, settings and the renewed live cache.
- A synthetic chat, uploaded file, custom model and prompt survived a further restart; authenticated API reads and file byte hash verified persistence. Upload processing was disabled.
- Internal network had no default route; a TCP attempt to a documentation-only address returned ENETUNREACH. Inference calls to the fixture were denied403.
- Test listeners bound only VM108127.0.0.1:18088/18089. Connections to those ports via VM108's LAN address failed.

`acceptance.json`, `data-recovery-acceptance.json` and `isolation-verification.json` contain exact safe results. Retrieval responses and the model list were **synthetic**, while login, persistence, function installation, cache execution and restarts were real. No real chats, production credentials, shared DB/queue or provider calls entered the fixture. This does not certify production TLS, the real Community Brain retrieval backend, browser UX, vector restore, or the full five-identity Infisical renewal transaction.

## Source and exact image

Candidate repository: `https://github.com/Patchoulab/agent-ops.git`  
Branch: `codex/request026-openwebui`  
Commit: **f7356151a563d4d07f390872efd9265b6b9302bf**  
Base: `a9dcf247e7aa2176f03fb7319fb1074f0e443acc`.

The isolated candidate worktree is clean; nothing was pushed and existing dirty operator work was preserved. `candidate-source.tar.gz` includes seven source/document files. All six Python-file hashes match VM108. `candidate.patch` contains the complete scoped diff. `source-image-manifest.json` records source and image identities; Request024 remains the provenance record for incumbent modified/untracked management code.

Original registry digest: `b8095f79a6a8ffad8f830bdacc9b5b0aef805689b31bca0b065cc2424d3cfaeb`. Original Docker image ID: `ea51ab128ef7f7e1e5d9a6e2cd8bbea2336e6ad408ad185c1e796525c97d9c52`. VM108's imported ID: `08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b`. The ordinary image export/load took318 seconds; ordered filesystem layers, image configuration hash and architecture matched exactly. No container commit or production volume copy was used.

Exact filter SHA-256: `12215e67d72775e3d56baa98fc23093196cc8917d887a18a506f188f26a0dc16`. Its source was checked against old runtime credential values before export. Exported candidate source also contains zero generated development credential values.

## Inventory and preservation

The dormant installation has1 user/auth record,60 chats,131 chat-message rows,111 files,5 models,10 prompts,1 function and1 knowledge record. Its Chroma store contains113 collections and1,555 embeddings. The persistent tree contains683 files and2,339,432,112 bytes; paths, counts, schema/source hashes and aggregate tree checksum are recorded without exporting private content or uploaded filenames.

Old webui.db SHA-256 remains `c4d3953ee249c642be9e0ffb7e7ed8e48adb14ad22531761f038b7ebd71b2b54`. The old container remains exited with the original September19 04:20:05 UTC finish timestamp. Its restart policy remains `no`.

The effective signing key is in **/app/backend/.webui_secret_key**, outside the volume, while its environment setting is empty. Only existence, byte count and checksum were recorded. A volume-only migration would miss it. Existing private September10 SQLite/function/container preservation copies and15 PBS VM101 snapshot entries are inventoried; snapshot listing is not restore validation. The existing protected September9 snapshot and latest observed September20 snapshot remain untouched.

## Dependency and capacity findings

- Renewal inventory/delivery still SSH to n8n-automation and require its stopped OpenWebUI. Move those operations to the replacement; never update backup credentials to keep that dependency alive.
- The Mac legacy-intake source retains an old remote branch, but its local `superseded` phase bypasses it and enforces disabled writers. Preserve that terminal guard.
- The inspected Traefik dynamic configuration has no OpenWebUI route; its old direct port is3000. A reviewed replacement hostname/TLS/authentication route remains required. The API allowlist includes old-host10.1.30.10, and the n8n ingress route still targets its5678 port.
- Kuma30/31 monitor the production API, not old OpenWebUI. Prometheus still has VM101 node-exporter and historical recapflow references. Separate recovery-host monitoring from obsolete serving expectations; do not delete backup coverage indiscriminately.
- VM109 has approximately57 GiB free and2.9 GiB available RAM at inspection. Its API uses approximately703 MiB (2 GiB limit). The rehearsal WebUI used approximately647 MiB idle and reached approximately1.16 GiB in observed startup/test samples; neither is a measured peak under production load. Disk appears sufficient; concurrent worker/API/WebUI memory acceptance remains a gate.

The bundled README contains protected transfer/restore steps, replacement renewal/consumer routing, endpoint/authentication requirements, independence checks and rollback limits. Inventory scope is the installed management source, inspected live ingress/monitoring configurations and existing preservation locations; it is not a claim that every historical lab file has been purged of old addresses.

## Stabilization image must survive recreation

The rollout must preserve the already VM108-tested application image `sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b`. Current production still runs `be0e7d...` with six r020 jobs-module overlays. The README identifies run.py/disposable-index pins, Compose module/frontend mounts, manual_api_runtime manifest assertions, boot launcher and recovery inventory/image pins requiring coordinated successor-packet updates. **Changing only the image would leave old overlaid modules in effect.** Do not modify r020 in place or bypass immutable manifests.

## Test corrections and limits

The first startup attempt safely stopped because the source-engine image ID was not addressable after import. Layer/config equality established the imported image identity before use. That attempt had no WebUI user data; only its empty disposable fixture was cleaned and bootstrap credentials retained privately. The first cold startup exceeded a three-minute readiness window and later became healthy; the candidate now allows a bounded ten-minute wait. A supplemental test initially used the wrong model-list URL; it was corrected to the actual `/api/v1/models/list` route, then verification continued against the already-created records without replaying writes. Final acceptance passed. These are development harness corrections, not production fixes.

## Retained state and production gates

Workspace: `/srv/dev-data/workspaces/cbm-openwebui-migration-20260920`. Both `cbm-r026-webui` and `cbm-r026-fixture` are **stopped**, no OOM was recorded, and both loopback listeners are closed. The isolated network, synthetic volume `cbm-r026-synthetic-data`, ordinary image and private development credentials remain for inspection; private files are0600. The four pre-existing development services remain running with start timestamps preceding this request. No synthetic cleanup requires touching production or VM101.

Live production remains paused, attention is unchanged, and boot reconciled=false. All five live identities still expire **2026-09-22T20:53:07Z**; the authoritative renewal journal phase was **completed** on inspection. No rotation, production deployment, cutover, hold clearance, processing resume, legacy restart, backup credential update, TCC change or retirement occurred.

Next gate: Forge reconciles this candidate into its canonical source and prepares the concrete successor rollout packet. It must cover protected real-data restoration, production endpoint/auth decisions, real retrieval and renewal integration, capacity acceptance and recreation preserving stabilization pins, validated on VM108 before promotion. Real user-data transfer and production acceptance remain gated. An expiry deadline does not authorize restoring VM101's production role.

All named evidence and artifact SHA-256 values are listed in `verification-receipts.json`. No further input is needed to close this preparation/development request.

# Request028: successor bindings and host validation

Development candidate for `CBM-SUCCESSOR-BINDINGS-20260920-028`. Production is
review-only. See the accompanying verification receipts for actual results,
immutable revision/hash, source commit and remaining gates. No production phase
is authorized by this request.

## Contract

`profiles.py` defines explicit development and production profiles. Each fixes the
host, state/private/packet paths, images, network, queue, limits, mount permissions,
external WebUI signing environment, boot launcher and recovery inventory.
`runtime_contract.py` requires an externally pinned exact packet manifest and
rejects production execution. Renderer validation rejects modified profile fields.
The production descriptor is an activation review input, not permission to run.

Both APIs have six explicit state/CA mounts, only files writable, 2 GiB RAM and
2 CPUs. Module and frontend sources come from the pinned stabilization image;
r020 module/UI overlays are absent. Workers get writable corpus/config only for
indexing. The development network is internal with no published ports. WebUI
state lives in a separate named volume; its signing key stays outside that volume
in a private environment file and is included in private recovery capture.

`run.py`, manual and automatic host launchers, management, boot controls and
recovery use this contract. `automatic_host.py` delegates to the real automatic
launcher; there is no held-tick replacement stub. Processing remains separate
from management renewal. A quiet lease excludes workers, so workload validation
releases that lease before worker execution while retaining the Mac mutex.

## Authority and queue

Only `homelab`, environment `prod`, child
`/development/community-brain-dev/request028` is accepted for candidate authority.
Fresh development service identities, queue credentials, a development TLS
certificate/key and a synthetic-provider token are stored there. Production keys
are never fetched. The management login stays on the Mac; delivery uses private
SSH stdin and 0600 files. Parent development values are compared before/after.

Development queue: TLS-first `tls://nats:4222`, stream `CBM_REQUEST028`, subject
`cbm.dev.request028.jobs.stage.ready.v1`, inbox `_INBOX.cbm_request028_worker`.
The dedicated worker principal has explicit publish/subscribe permissions inside
this isolated server. Runtime fields must match the descriptor before connection.
Negative tests use actual invalid credentials and an explicitly empty trust store.

The production queue binding remains separate. The original production indexing
budget helper is preserved byte-for-byte; synthetic validation replaces external
providers and allowance checks only. It does not certify paid calls or budgets.
No worker test enables network publication.

## Source provenance and immutable packets

The base is agent-ops commit `3022cda148f9fd3b1732a687a40ba2220bcc90ef`.
Forge's supplied source is the starting point; its two-file deterministic-builder
fix is reconciled into `management-integration-027` as well. Input archive and
image-file hashes are recorded in the receipts. Worker provenance records both
original and resulting hashes. Incumbent policy/lease sources are preserved;
`incumbent/transport.py` adds `-B` to Python subprocesses.

Mac helpers `stage_packet.py`, `initialize_authority.py` and `workload.py` are
included for replayable administration. Initialization requires a newly generated
private development `nats.key`/`nats.crt` (SAN DNS:nats, serverAuth) in the Mac
Request028 state directory; it refuses an already initialized authority. Staging
creates missing disposable lock inodes without replacing existing ones.

Build with `build_packet.py OUTPUT packet-vN IMAGE_FILES MONITOR_IMAGES`.
Both profile descriptors and every helper are sealed with sorted JSON keys.
Never overwrite an existing revision. Run Python with `-B` and
`PYTHONDONTWRITEBYTECODE=1`. Extra files, bytecode, symlinks and changed bytes fail
verification. Packet directories must be readable by the container UID10001;
private authority/state remains separately restricted.

## Validation scope

`validation_host.py` exercises actual manual inspect/execute, automatic scan/tick,
boot/holds, excluded work, uncertain outcomes, replay refusal, checkpoint gating
and paired disposable recovery. PostgreSQL, JetStream, durable stages, artifacts,
LanceDB and FTS are real; provider responses are synthetic. Recovery is private:
PostgreSQL dump, state, runtime/private files, external signing material and WebUI
volume. Restore comparison uses a separate database and directory.

`manager.py`, `consumers.py` and `kuma.js` exercise actual Infisical renewal and
API recreation, delivered service bundles, WebUI cache and fresh real Kuma and
Prometheus observations. An intentional lost delivery acknowledgment must resume
the same generation, preserve overlap until acceptance, then reject old tokens.
Desktop collector intake/upload is not certified by configuration/scope probes.

## Preserved boundaries

VM101 is untouched and recovery-only. Retained Request026/027/Forge fixtures and
production holds are preserved. Production metadata/source reconciliation is
read-only. The extra September17 r020 bytecode remains protected evidence, not a
file to delete to make an old exact-file-set assertion pass.

Production data/signing restore, browser/session acceptance, full-load capacity,
paid-provider/budget validation and separately authorized installation/rotation/
cutover/processing remain open. Existing chat DNS/Traefik/Step CA approval persists;
Request028 does not execute ingress. See `ROLLOUT.md` for phase boundaries.

## Recorded outcome

Development validation passed; evidence is in `evidence/`. Final immutable packet
is `packet-v14`, manifest
`c977c2a69c794141ef1c1bbf991ad7f44309ef172711e87d0806044679ad8b04`.
All fourteen retained packet revisions have exact file sets and zero bytecode.
The final builder reproduces that manifest; nine boundary tests pass locally
and on VM108, plus seven tests for the reconciled Forge builder fix.

Actual manual and automatic workers completed two synthetic meetings; 17 rows
have complete FTS coverage. The uncertain third meeting remains outcome_unknown
after one attempt, with replay refused. Excluded work stayed untouched. The
catalog served three meetings including the archive, with thirteen content hashes
verified. Paired restore matched the database, 62 files and WebUI SQLite integrity.
The same-generation interrupted renewal passed actual consumer acceptance and
old-token rejection with three contract-preserving API recreations.

Seven Request028 containers are stopped and retained, with explicit disposable
pause/attention markers. Four baseline services retain their original start times;
twelve prior stopped fixture containers and Request027 private files are preserved.
No production changes or VM101 contact occurred. Production expiry metadata was
September22 at20:53:07 UTC. Earlier failures and revision-specific evidence are
recorded, not represented as clean first-attempt passes.

Final source review added explicit production acquisition/model credential-file
and real-provider command bindings. Production execution still fails closed.
Successful full workers ran on packet-v9; renewal ran on packet-v13. The final
packet-v14 has verified identical development environments, worker arguments,
provider command/secret mapping and API/WebUI rendering, plus actual VM108 held
launcher checks. It was not replayed against the already completed jobs.

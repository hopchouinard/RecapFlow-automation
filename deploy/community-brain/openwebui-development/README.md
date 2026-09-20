# Request026: isolated OpenWebUI migration candidate

This is a development harness and rollout input, not production deployment code.
Run only on Community Brain dev VM108. The script enforces its hostname and data
mount. No production credentials, user data, provider access or public ingress
are inputs. Runtime credentials are generated under the private VM108 workspace,
outside this source directory. Nothing is pushed automatically.

## Exact software and isolation

- Existing OpenWebUI version: **0.8.12**.
- Registry reference: `ghcr.io/open-webui/open-webui@sha256:b8095f79a6a8ffad8f830bdacc9b5b0aef805689b31bca0b065cc2424d3cfaeb`.
- Original Docker config image ID: `sha256:ea51ab128ef7f7e1e5d9a6e2cd8bbea2336e6ad408ad185c1e796525c97d9c52`.
- Imported VM108 image ID: `sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b`.
  The ordinary image export/load changed the engine's identifier. The full ordered
  RootFS layer list, image Config hash and architecture match, recorded in the
  response's `image-equivalence.json`. Do not substitute an unverified image.
- Exact filter: `12215e67d72775e3d56baa98fc23093196cc8917d887a18a506f188f26a0dc16`.
- Python fixture image is pinned in `rehearse.py` to the image already on VM108.
- A new internal Docker network and synthetic volume are used. Neither container
  joins existing dev networks. The fixture cannot run inference or access a real
  database/queue. OpenWebUI offline settings prevent dependency downloads.
- This Docker engine does not activate published ports on the internal network.
  `loopback_proxy.py` instead binds only `127.0.0.1:18088` and `:18089` on VM108,
  forwarding to the two isolated containers. It logs no traffic. It is a test
  helper, not a production ingress design. Docker documents internal networks and
  port binding separately: <https://docs.docker.com/reference/cli/docker/network/create/>
  and <https://docs.docker.com/engine/network/port-publishing/>.
- Resource limits: OpenWebUI 1.5 GiB/1.5 CPUs; fixture128 MiB/0.25 CPU. Existing
  dev services remain running. Cold imports require a bounded ten-minute readiness
  allowance on this VM; observed startup exceeded the original three-minute limit.

## Rehearsal commands and boundaries

Workspace: `/srv/dev-data/workspaces/cbm-openwebui-migration-20260920`.
Place these sources in `source/`; verify their hashes and image equivalence first.

```sh
sudo python3 -B /srv/dev-data/workspaces/cbm-openwebui-migration-20260920/source/rehearse.py setup
sudo python3 -B /srv/dev-data/workspaces/cbm-openwebui-migration-20260920/source/rehearse.py test
```

Each command is separate. Setup refuses an existing private fixture; test refuses
an existing start marker. Inspect prior effects before continuation. If only
restart readiness timed out after `acceptance-before-restart.json` was written,
`verify-restart` verifies the existing state without replaying credential changes.

The real application performs signup/signin, function installation, valve updates,
filter invocation through its live application cache, and restart persistence.
An administrator-only synthetic action invokes the exact filter; it does not call
a model or create a real chat. Both retrieval responses and the model list are
fixtures. The test stages development credential overlap, delivers a new key via
the actual functions API, revokes the old key at the fixture, verifies401, checks
unavailable context under deliberate denial and verifies recovery. This does not
certify the five-identity Infisical renewal transaction, production TLS/provider
connectivity, human browser UX, or a restore of real user data.

## Protected production transfer and restore inputs

These are gated preparation steps, **not commands authorized by Request026**:

1. Keep VM101 and its writers dormant. Verify container stopped, database/WAL
   state, volume tree checksum and a recent recoverable backup before copying.
   Existing protected PBS preservation snapshot is
   `pbs:backup/vm/101/2026-09-09T16:08:13Z`; the observed latest scheduled copy was
   `pbs:backup/vm/101/2026-09-20T01:00:05Z`. Listing them is not a restore test.
2. Privately transfer a consistent copy of `open-webui-data` from
   `/var/lib/docker/volumes/open-webui-data/_data`, preserving ownership/modes.
   Include webui.db, uploads, vector_db and trust material. Preserve the cache in
   the recovery copy; do not assume it is safe to discard during a version-pinned
   migration. Compare a private per-file manifest plus aggregate tree digest.
   Do not attach this archive or file names/content to the shared handoff.
3. Preserve `/app/backend/.webui_secret_key` from the stopped container through
   controlled secret storage. The old environment's WEBUI_SECRET_KEY is empty;
   copying only the volume would miss the effective key. Never use `docker commit`
   as an image-transfer shortcut. Retain signing material privately or explicitly
   plan session invalidation; do not silently lose it.
4. Restore to a new replacement-owned volume. Use the verified existing image
   first, not an implicit latest upgrade. Before exposure, verify SQLite integrity,
   schema, row counts, file/vector hashes, user/auth relationships, five custom
   model definitions, ten prompts, settings and the exact global filter. Defer
   real-content verification to a protected session, exporting only safe outcomes.
5. Use a separate loopback staging endpoint with explicit authentication, signup
   policy and provider allowlists. Rendering persisted configuration must account
   for database overrides, not only container environment variables. The old
   `rag.ollama.url` uses host.docker.internal, while the environment's Ollama target
   is10.1.50.219:11434; reconcile that mapping before enabling embeddings/inference.
   Other URLs found in persisted configuration include inactive defaults and must
   not all be enabled merely because they exist.
6. At the approved cutover, capture a fresh replacement-owned recovery pair and
   private off-host copy. The September10 SQLite preservation copy alone omits
   uploads/vector state and is not a complete current migration backup.

## Consumer routing, authentication and retirement boundary

- Replace both `service_renewal_live.py` old-host operations (inventory:112 and
  delivery:153) with the explicit replacement host/container. Update any matching
  delivery helper target and the old8999 URL allowance. Preserve independent
  service subjects/scopes, staged overlap, new-cache acceptance, old rejection,
  and fresh monitoring. No renewal credentials go to the dormant backup.
- The hourly scheduler invokes renewal. Its legacy Mac intake hook also contains
  a remote fallback reference, but the current local phase is `superseded`, which
  returns before fetch. Retain that terminal no-resume guard; do not restore its
  old branch. Reconcile/remove obsolete branches through reviewed source changes.
- Current Traefik active files contain no OpenWebUI route; the old container binds
  host port3000 directly. A replacement hostname/TLS/authentication route needs a
  concrete reviewed choice. Do not repoint the Community Brain API hostname to
  OpenWebUI or silently change existing local user authentication to OIDC.
- Traefik's Community Brain API allowlist still contains10.1.30.10/32. Replace that
  consumer permission after proving the replacement's observed source address;
  then prove the old source no longer has the production consumer role.
- The n8n ingress route still points at10.1.30.10:5678. It is an obsolete serving
  reference to address in the reviewed migration packet, not a reason to restart
  n8n. Historical backup files containing old addresses are preservation evidence.
- Kuma30/31 target the Community Brain HTTPS health/retrieval endpoints, not old
  OpenWebUI. No dedicated OpenWebUI monitor was found in the inspected monitor set.
  Add replacement UI/auth readiness coverage in the cutover packet while retaining
  existing API monitoring. Prometheus still scrapes VM101's node exporter and has
  historical recapflow rules/runbooks. Classify those as recovery-host coverage
  versus obsolete serving expectations; do not blindly remove backup monitoring.
- Prove independence with old-host serving unavailable: replacement login and
  retrieval, renewal inventory/delivery/cache/revocation, scheduler completion,
  monitoring and recovery must all pass without SSH or traffic to VM101. Review
  source/config references and observed network destinations. This is a future
  production acceptance gate, not a claim made by the synthetic rehearsal.

## VM109 placement and stabilization pins

VM109 has4 GiB RAM, approximately2.9 GiB available at inspection, and57 GiB free
on `/srv/community-brain`. Its API consumed approximately703 MiB under a2 GiB
limit; Alloy used53 MiB under128 MiB. The image plus full existing WebUI volume
fits observed disk space, including staged duplication. Memory is tighter:
reserve headroom for the API, worker/embedding peaks, OS and recovery. An idle
snapshot is not load acceptance. Report this constraint instead of provisioning
a new host; measure concurrency on VM108 and specify limits in the rollout.

The application stabilization image already present on VM108 is
`sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b`.
Request026 does not redeploy or recertify that application image. Current
production still uses `be0e7d...`, with r020 files mounted over image modules.
Installing the new image alone would therefore be insufficient.

Forge's immutable successor packet must reconcile:

1. `production-staging/run.py` CB_IMAGE and `disposable_index_host.py` image pins;
   the effective packet's `run.py` and manual-host imports.
2. `compose.production-manual.yml` six r020 jobs-module mounts and the frontend
   mount. Review their precedence against the tested stabilization image; do not
   overlay old modules/UI onto it. Point to a new reviewed successor packet or
   remove only superseded mounts with explicit tests.
3. `runtime-manifest.json`, the successor effective/frontend manifests and all
   file/byte hashes; `manual_api_runtime.py` expected manifests/paths, used by
   renewal to recreate the API from fresh authority.
4. Mac and VM boot_guard launcher paths, recovery `files_adapter.py` image and
   inventory paths, management control manifests, and corresponding source/live
   copies. Preserve boot pause, attention and uncertain-effect rules.

Do not modify r020 in place, bypass its manifest assertions, or restore stale
api.env. A recreation test on VM108 must prove the renderer preserves the new
image and intended modules after credential renewal.

## Rollback limits

Before user traffic, a failed replacement can be stopped and its staged volume
retained for diagnosis. After writes, preserve the replacement data first; rollback
must use a compatible replacement runtime and current identities, with explicit
data/schema reconciliation. Never overwrite new user data with the dormant copy,
reenable VM101, or restore expired credentials as an automatic rollback. Retirement,
production rotation/cutover and processing resume require the next authorized
packet and successful VM108 acceptance. No expiry deadline removes these gates.

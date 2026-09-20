# CBM-MANUAL-PREP-20260910-003 — preparation completed, activation held

Mac management verified both request document hashes and prepared only the
management prerequisites. **No API restart, upload, processing/indexing activation,
retrieval change, deadline change or legacy writer restoration occurred.**

## Private identity delivery

Infisical remains authoritative: `homelab` / `prod` / `/applications/community-brain`.
Existing live `CB_SERVICE_IDENTITIES` and human grants are unchanged. The independent
pending records are in **`CB_MANUAL_PREP_SERVICE_IDENTITIES`**, containing the three
existing records plus these two new identities:

| Subject | Scope | Permissions | Initial expiry UTC |
|---|---|---|---|
| `community-brain-prod-mac-collector` | `community-brain` | `sources:upload` | 2026-09-17 05:03:42 |
| `community-brain-prod-manual-operator` | `community-brain` | `sources:upload`, `jobs:submit`, `jobs:read`, `artifacts:read` | 2026-09-17 05:03:42 |

Secrets: `CB_PROD_MAC_COLLECTOR_TOKEN`, `CB_PROD_MAC_COLLECTOR_EXPIRES_AT`,
`CB_PROD_MANUAL_OPERATOR_TOKEN`, `CB_PROD_MANUAL_OPERATOR_EXPIRES_AT`.
The initial seven-day lifetime follows the current retrieval identity convention;
Mac management owns explicit rotation and coordinated server/client delivery before
expiry. No automatic renewal or lifetime extension was installed.

Root-private VM109 directory `/etc/community-brain-production/manual-preparation/`
(mode 0700, files 0600, owner root:root):

- `server-identities.json`: pending complete identity map, hashes only.
- `api.env.pending`: private API bundle with pending map; current `api.env` unchanged.
- `collector-client.env`: only collector token and expiry.
- `operator-client.env`: only manual operator token and expiry.

Mac private configuration:
`/Users/pchouinard/Library/Application Support/CommunityBrainProduction/collector.pending.json`
(user 501, mode 0600 in 0700 directory). It targets
`https://community-brain.patchoutech.lab`, but is explicitly **disabled**, requires
activation, and has no selected recording. There is no active `collector.json`.
Infisical equality, unrelated authority preservation and private modes passed.
Never print these private bundles or commit them; public delivery evidence and its
hashes are in `identity-preparation.json` and `receipt-manifest.json`.

## Concrete collector preparation and activation blocker

Existing development configuration, tooling and legacy Zoom sync were preserved.
Production tools are staged separately under the Mac production directory's
`tools/`. The existing restricted `ZoomCollector` implementation was copied without
change (SHA256 `aa3b8f69e4bbf822baf188779b74d0129b38cf4d9ab1bd0e70d1e54cdff96988`).
A thin production runner requires a private active config and a management-approved
selection binding meeting ID, relative Zoom path, SHA256 and approval request ID.
It cannot accept a caller-selected destination/key, submit jobs or retry uploads.
The public lab root is explicit for its Python TLS client.

`python3 "${HOME}/Library/Application Support/CommunityBrainProduction/tools/manual_upload.py" check-config`
passed without network access. The `upload` command was verified to refuse the
inactive configuration before constructing a client or reading any selected file.
No source was selected or uploaded, and no Fathom credential was provisioned.

**Activation blocker:** the current nginx collector proxy restricts routes/methods,
not JSON source kind. Existing development chat-only authorization comes from
`sources:upload:chat` in the API. With the requested `sources:upload`, the API allows
transcript and alias uploads too. The client sending only chat is not a security
boundary. Therefore these broad pending collector records must not be activated
assuming that the existing proxy enforces chat-only access.

Forge must either supply a tested, non-bypassable chat-only server restriction or
post a corrected scoped request selecting the already-supported
`sources:upload:chat` permission. The finding was published during preparation as
`collector-guard-finding.md`; no wider active grant was introduced.

Follow-up activation sequence, after that resolution:

1. Forge supplies tested image/helper hashes, upload mount permissions, restricted
   route/identity enforcement, stage eligibility and rollback evidence. Check that
   non-chat requests cannot bypass the collector restriction on another route.
2. Management merges only the approved new records into the **then-current**
   authoritative identity map and renders the appropriate API bundle. Do not
   blindly copy a stale `api.env.pending`: probe rotation or other legitimate
   changes may have occurred since preparation. Preserve human/retrieval/probe
   identities. API reload requires the separate verified staging handoff.
3. Run verified-TLS health and missing/invalid-key checks; verify collector chat-only
   enforcement, forbidden transcript/alias operations and restricted non-upload
   routes. Confirm manual operator scopes independently. No model invocation.
4. After an explicit recording/file choice, privately write `selection.json` with
   exactly `approved_request_id`, `meeting_id`, `relative_path`, `sha256`. Reconcile
   the approved destination and identity, then create active `collector.json` with
   `enabled=true`, `activation_required=false`, `chat_only_guard_verified=true`.
   These settings describe verified management state; they do not replace server
   authorization. Keep Folder Actions disabled and the old LaunchAgent unloaded.
5. Execute one manual upload, verify returned source identity/hash/bytes and server
   deduplication/storage metadata. Do not automatically retry an uncertain response.
   Job submission remains a distinct, explicitly selected operator action. No old
   development recording is silently reused as production approval.

## Proposed steady-state controls after ownership passes

These controls are proposed, **not applied by this preparation**:

- Preserve legacy containers, data, keys and backups. Keep n8n stopped and restart
  policy `no`; once new ownership is verified, stop rather than leave the old
  retrieval container paused indefinitely, retaining its exact restart recipe.
  This is preservation of inactive services, not retirement or volume removal.
- Keep old lint, artifact Git pull/push and snapshot cron entries disabled; preserve
  their originals under the existing management state. Do not reinstall them while
  releasing temporary guards. Keep old Zoom Folder Action disabled and previously
  unloaded LaunchAgent unloaded. One manually invoked production collector is the
  intake owner; one eligible-stage-controlled VM109 worker owns corpus writes.
- Before cancelling the timer, record a verified superseding ownership receipt and
  update both the VM101 rollback controller and Mac intake-resume hook so neither
  can restore legacy writers from an obsolete state. Validate that transition with
  failure checks; only then disarm the timer. Do not merely disable the timer while
  leaving stale automatic restore logic. Remove temporary immutable flags only
  where needed, restoring saved per-inode flags without enabling legacy writers.
- Preserve the operator no-manual-write rule for the archived old tree. Runtime
  permissions must keep the new single-writer boundary enforceable. Remote
  publication stays disabled, and synthetic pending events remain excluded.

## Paired checkpoint and recovery plan

Existing verified baseline remains unchanged:
`/srv/community-brain/artifacts/cbm-bounded-production-20260910/paired-recovery-manifest.json`,
SHA256 `8fd86be9ceb61dc24fa018c49cf049119eb93a01845688e1e69d53a6cd7e28aa`.
It references database dump `20260910T033129Z.dump`, 53 managed files and 26 verified
source/artifact/response references. PBS checkpoint remains
`pbs:backup/vm/109/2026-09-10T03:32:39Z`. It is a prior baseline, not a claim that a
new post-ownership checkpoint or restore test was performed in this request.

After manual ownership verification, drain the new eligible writer and create a
paired PostgreSQL dump plus files/**canonical corpus**/config manifest under one
checkpoint ID. Record image/runtime public hashes, row/reference hashes, corpus
version/dimensions/FTS coverage and eligible-stage/outbox state. Copy the pair
off-host and retain PBS coverage of the VM plus its paired DB dump. Infisical
remains secret authority; do not place raw runtime credentials in public manifests.

Restore into a separate database and isolated file/corpus copy with workers and
network publication disabled. Verify all DB-to-file references, corpus hashes and
retrieval. Use a fresh isolated queue; do not replay existing pending messages or
mark production synthetic events indexed. Only explicit reconciled eligible work
may run after recovery is approved. Keep the prior checkpoint until the replacement
passes. No PITR or full-guest restore guarantee is inferred.

## Lifecycle and current hold

Read-only lifecycle inspection confirmed:

- Existing probes expire **September 11 02:05:38 UTC**. If staging monitoring
  continues, explicitly rotate read/metrics probe secrets and expiry in Infisical,
  coordinate API plus Kuma/Prometheus credential refresh and verify authorization
  before expiry. The general renderer now preserves independent identities; merge
  pending manual identities against fresh authority after any such rotation.
- WebUI retrieval identity expires **September 17 03:52:50 UTC**. Coordinate its
  API hash and private WebUI key refresh before expiry, preserving all other valves.
- New manual/collector identities expire **September 17 05:03:42 UTC**. Rotate each
  independently; do not couple their credentials to human, retrieval or probe keys.
- Existing hourly Mac maintenance handles application/NATS certificates and backup
  copies; its latest recorded checks passed. It does **not** rotate these tokens.
  The intake rollback hook was added after that last maintenance run.

The writer hold remains active. Rollback still starts **September 11 01:25 UTC**,
with hard deadline **01:30 UTC**. No immutable flag, old schedule, active retrieval
valve, API process or deadline was changed. If readiness is not verified in time,
let that rollback execute; a pending manual preparation bundle is not authority to
extend the hold. No additional approval question is needed for this preparation;
the guard correction and verified activation handoff are the next prerequisites.

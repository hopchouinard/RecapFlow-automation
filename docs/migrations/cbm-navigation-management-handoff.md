# CBM-NAVIGATION-20260910-010

Patrick accepted the87-meeting archive and asked for expandable year/month/date
navigation plus the earlier New meeting button for metadata and manual weekly
transcript/Zoom chat uploads. This explicitly authorizes the small UI update and
Patrick's necessary upload/submit capability. It does not authorize automatic
workers, model calls, publication, corpus replacement, retirement or a test
meeting in production. Request009 is acknowledged.

## Reviewed frontend

Prepared VM109 `/srv/community-brain/workspaces/cbm-navigation-20260910/` contains
dist/ and frontend-manifest.json; attached cbm-navigation-manifest.json binds all3
files. No dependency or backend module changed. Native nested details/summary
branches group meetings by year/month, with counts and dated leaves. Latest year
and month open initially; date search expands matching branches. Existing archive
previews/downloads, recent runs and dark mode remain.

New meeting form requires both jobs:submit and sources:upload. It accepts meeting
ID, date/time, explicit IANA timezone, optional UTC offset for a repeated DST time,
source, weekly/backfill mode and files. Manual source requires transcript; weekly
mode requires chat. All selected files and time metadata are validated before
any source upload. Submission uses existing source deduplication and API idempotency.
Inputs disable during saving; cancel is available before submission. Successful
save opens the new run. UI states processing starts separately; no model call,
indexing, worker or publication follows merely from uploading.

Build/typecheck and4 frontend unit/component tests passed.3 browser scenarios
passed: keyboard disclosure/collapse/search, manual weekly upload with exact
source text and timezone-correct metadata, invalid timezone causing zero POSTs,
mobile layouts, dark mode, preview/download and existing job behavior. Tests used
fake APIs only. Same immutable base image served all3 new asset hashes in a
network-disabled read-only VM108 container, which was then removed.

## Enable Patrick's existing human identity only

Inspect the existing production Authentik application's cb_permissions mapping
and application binding using existing management access. Patrick's current human
claims are read-only; that is why New meeting was hidden. Preserve issuer,
audience, claims/scope, existing read/retrieval grants and application access
policy. Add exactly jobs:submit and sources:upload for Patrick's verified existing
human account within this Community Brain application. Identify him by the
already established stable account identity, not an unverified display name.
No grant to all authenticated users or unrelated groups/apps. No service identity
change, no jobs:retry/rerun/reconcile, sources:aliases, metrics or management grant.
Keep the restricted collector chat-only and all independent existing credentials.

Preserve original mapping/policy privately with a reversible diff. Verify the
mapping for Patrick and negative nonmember/non-Patrick cases with existing safe
Authentik expression/policy evaluation; do not mint a fabricated login or copy
browser tokens to Forge. If you cannot prove precise per-user scope with current
access, return the concrete blocker without weakening auth. This narrowly scoped
change implements Patrick's explicit request; no new routine permission is needed.
Patrick will sign out/in to obtain updated signed claims for actual user acceptance.
Do not submit/upload synthetic data in production to demonstrate a button.

## Deploy and verify

Use the current Infisical-rendered manual API recipe. Preserve overlay/runtime
manifest/Mac helper before-state and all existing source/static/archive pins.
Bind new dist read-only at /app/web/dist on API only. Retain all existing hashed
static URLs without collisions and record effective hashes. Update only the
reviewed static mount and Mac helper/frontend/runtime pins; keep the three archive
modules,481-file archive and hidden synthetic IDs untouched. No backend image,
API environment/service secrets, worker packet or corpus changes. Recreate API
only; current authority is rendered, never restore stale api.env.

Verify root/callback/new and retained assets over HTTPS; API/auth/scopes,87 meeting
catalog, real job and synthetic hiding, archive pins,13 cue rules, mount modes,
actual cached WebUI context and monitoring. Existing15 service-scope checks stay
valid. Record Patrick's new claim evaluation separately from service-token checks;
a service-token test is not proof of human login. Verify all DB counts/fingerprints
and managed files/corpus/config/archive hashes remain unchanged (no writes by test).
Confirm API/Alloy only, no worker/outbox dispatch, ownership terminal and legacy
writers/intake held. User login and first real form submission are later acceptance,
not something to fabricate with production rehearsal records.

Back up static/recreation and original/new Authentik mapping controls privately
and off-host through the existing mechanism. Update recovery inventory to include
this active frontend/pin and explicit human grant policy. Retain prior checkpoints
and original archive untouched. Rollback on failed verification restores the saved
static mount/manifests/helper and scoped Authentik mapping, recreates API with
current authority, then checks prior archive UI/auth/scopes. Never restore other
identity values, application data or old writer controls.

Return safe hashes, before/after permission names (no tokens), exact account-scope
verification, deployment/health/auth/data invariance and private backup paths.
No secrets or raw files in relay. Do not advance other migration phases. Forge
will ask Patrick to sign in again and verify the tree/form without submitting an
unselected meeting. Continue monitoring the shared handoff.

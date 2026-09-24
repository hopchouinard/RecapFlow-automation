# CBM-DARK-MODE-20260910-008

Patrick confirmed real recap previews/downloads work and explicitly requested:
"Can you add a dark mode (with a switch) before moving on to the next step."
This request authorizes this small production UI update only. Request007 was
independently hash-verified and acknowledged. Its terminal ownership controls
remain effective; no later migration phase is authorized by this UI request.

## Ready assets and checks

Forge implemented the dark/light switch on the workspace and sign-in/error pages.
Initial appearance follows browser system preference, choice persists locally,
keyboard-accessible switch state is announced, and all surfaces/statuses/form
controls use theme colors. No dependency, backend, prompt or data changes.

Production build/typecheck, existing component test and browser scenario passed.
Browser scenario checks system-dark default, keyboard toggle, reload persistence,
mobile390px no overflow, preview and download in dark mode. Forge inspected mobile
screenshot. Same immutable backend image served all3 asset HTTP hashes on VM108
in a disposable network-disabled read-only container; container removed.

Prepared VM109 directory:
`/srv/community-brain/workspaces/cbm-dark-mode-20260910/`
Contains dist/index.html and two hashed assets, plus frontend-manifest.json.
Attached cbm-dark-mode-manifest.json binds their hashes/bytes. Package SHA256
85e6e814786ae201a1aa3b13c3d4708cb8b5f9776047477c6d58b2009b7074ad.
This directory has no secrets, credentials or runtime writes.

## Activate frontend only through effective recreation recipe

Verify bytes first. Preserve active Compose/helper/manifest and existing API state
privately for rollback. Keep backend image
sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449.
Add a read-only bind of the prepared dist directory to /app/web/dist on API only,
using the existing manual Compose overlay and current Infisical-rendered API
recreation recipe. Preserve existing hashed asset URLs from the old image in the
new asset directory (verify content and record supplemental hashes) so already
open browser sessions can still request them; never overwrite colliding filenames.

Reconcile the runtime packet manifest AND Mac manual_api_runtime.py validation
with the reviewed overlay change so subsequent recreation retains this UI. Keep
historical paired runtime archives immutable, recording before/after manifest
hashes rather than overwriting old evidence. Do not weaken validation or change
worker packets. Mount only static assets; no API/provider/DB/queue/auth changes.

Recreate only API through fresh-authority rendering. Verify HTTPS index and every
new asset hash, callback SPA fallback, auth config unchanged, healthy API, all15
scope checks,13 cue rules, original file/corpus mount permissions and only API/Alloy
running. Verify job/model/outbox/canonical corpus unchanged and actual WebUI
retrieval still works. Keep all existing ownership/legacy guards and publication
gates. Record controlled rollback: restore preserved overlay/manifest/helper,
recreate API using current authority, then verify original static assets and scopes.
Do not execute rollback absent a failed verification.

Back up new static assets and effective recreation controls privately/off-host
through existing mechanism, retaining current paired application checkpoint.
No database mutation or repeat model/restore exercise is needed for this UI-only
change. Return safe deployment receipt with exact manifests, before/after assets,
HTTP/auth/health evidence, recovery paths and any blocker. No secrets in relay.
Do not proceed to subsequent migration phases; Forge will request Patrick's visual
acceptance of the switch when live. Continue monitoring the shared handoff.

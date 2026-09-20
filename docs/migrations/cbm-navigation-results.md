# Date navigation and manual meeting form — September10,2026

Patrick accepted the preserved-file view/downloads, then requested expandable
year/month/date navigation and the New meeting form for manual weekly uploads.
Implementation and isolated verification are complete. Production request
CBM-NAVIGATION-20260910-010 completed at17:55:53UTC and Forge verified and
acknowledged its receipt.

## Implemented

The meeting sidebar groups dated leaves into native keyboard-accessible year and
month disclosures with counts. Latest year/month expand initially; older branches
can expand/collapse independently. Date search expands matching branches and
preserves the selected file view. UTC formatting prevents calendar dates shifting
with the browser timezone. Dark mode, previews/downloads and real-run links remain.

New meeting is available to callers with both jobs:submit and sources:upload.
The form collects meeting ID, wall date/time, IANA timezone, optional repeated-time
UTC offset, source, recap mode and transcript/chat files. Manual transcript is
required for manual source; weekly mode requires chat. The time helper resolves
selected-zone offsets independently of browser timezone, rejects DST gaps and
requires an explicit offset for repeated times. All files/time metadata validate
before uploading. Existing backend source deduplication and job idempotency remain.
Successful save opens the new run. No automatic worker/model/publication activation.

Production Patrick claims were read-only, explaining the missing button. The
handoff requests adding exactly jobs:submit and sources:upload to his verified
existing human identity in this application. It preserves all existing identity
boundaries and grants no retry/rerun/reconcile, alias, metrics or management scope.
Fresh user login is required after the mapping changes. No synthetic production
upload or job is authorized as a deployment test.

## Verification and staged artifacts

Build/typecheck,4 frontend unit/component tests and3 browser scenarios passed.
Coverage includes keyboard branch toggles, search expansion, mobile layout,
literal Markdown/download, dark mode, manual weekly files and exact metadata,
invalid timezone with zero POSTs, seasonal offsets, DST gaps and repeated times.
The test include glob was widened to include .test.ts as well as .test.tsx so the
timezone tests execute in the standard command. No dependencies/backend changes.

The three static assets passed HTTP hash/size checks on VM108 using the existing
base image, read-only files and network disabled. Disposable container removed.
Ready bundle on both VMs: workspaces/cbm-navigation-20260910/; VM108's full path
is under /srv/dev-data and VM109's under /srv/community-brain. Safe asset hashes
are cbm-navigation-manifest.json. The management handoff specifies preservation
of all prior static URLs, archive/module pins, scoped auth verification, unchanged
DB/files/corpus and private off-host recovery of UI and Authentik mapping controls.

Management verified the stable Patrick account by both database ID and UUID;
only the matching active member receives jobs:submit and sources:upload in this
application. Six positive/negative expression cases and actual provider previews
passed. No other human or service identity gained these permissions. Existing
read grants and application policy remain unchanged. No browser token was minted.

Eleven static/root/callback HTTPS checks,15 service scope checks,87 meeting dates,
481 preserved download hashes and six real-run artifact hashes passed. Synthetic
jobs remain hidden, DB and file/corpus/config/archive fingerprints unchanged,
API/Alloy healthy, monitoring and actual WebUI retrieval verified. Private off-host
static/mapping/control recovery copies and inventory were verified.
Forge independently verified every returned receipt hash and fetched all3 new
assets over verified HTTPS matching its build. Safe receipts are under
cbm-navigation-receipts-20260910/. Patrick must sign out/in for new signed claims;
human tree/form acceptance is still pending. No historical
reprocessing, new real recording, provider spend, publication or retirement.

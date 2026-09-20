# Request019 — approved Fathom importer production deployment

Patrick reviewed the successful isolated live acquisition and explicitly said:
"Yes, deploy this in production". Apply the tested call-URL/ID resolution and
inclusive +/-10-minute recording-start tolerance, including the UI entry changes.
No additional approval is pending. Request018 is complete and acknowledged.

Verified immutable packet:
/srv/community-brain/workspaces/cbm-fathom-production-20260917/
packet-manifest.json matches companion cbm-fathom-production-manifest.json.
Six files: dist/index.html,two dist/assets files,jobs/acquisition.py,
selected_fathom.py,manual-host-mount.patch. This is a PARTIAL overlay, never replace
the whole current effective weekly packet with it.

Under existing Mac scheduler and ordered runner/manual/submission quiet locks,
verify no active/eligible job or pending checkpoint. Build a new effective packet
from current r016 (or latest inspected equivalent), preserving every management
fix. Add jobs/acquisition.py and replace selected_fathom.py. Apply the ONE-LINE
manual_host.py patch adding acquisition.py to the existing jobs-module read-only
mount loop; preserve every other launcher line. This ensures real acquisition
workers load the new importer rather than the old module baked into the image.
Verify actual resulting container arguments/module paths, not only copied bytes.
Image remains pinned; no provider credential moves to API or frontend.

Create effective frontend directory retaining all previous hashed assets; replace
root only, fail on differing same-name asset collisions. Update current renderer,
launcher/runtime/frontend/recovery pins and inventory together. Recreate API only
as needed with freshly rendered Infisical authority. Preserve akadmin/pchouinard
access, existing weekly$5 guards, scheduled token renewal, Signal theme and
z-ai/glm-5.3-flash extraction configuration. Capture before/after current controls
privately and verify off-host copies. Preserve historical checkpoint receipts.
No production meeting submission, transcript fetch, model call or reindex needed.

Behavior: form accepts full https://fathom.video/calls/<ID> or numeric ID. It
normalizes URLs before source/job submission. Importer matches native recording_id
or call ID from trusted Fathom meeting url/share_url and requests transcript using
resolved native recording_id. Exact selected identity remains mandatory; this is
not a nearest-meeting search. Recording start must be within600seconds inclusive
of entered timestamp; supplied timezone/date stay authoritative job metadata.
Metadata created-time query uses a surrounding bounded date window because it is
not a recording-start filter. Five metadata pages maximum, one transcript per
selected worker guard, extras disabled. No unrelated transcript fetch.

Evidence:20 acquisition tests including real SelectedFathom request guard,
numeric and full URL, +/-600 accepted, +/-601 rejected; frontend6 tests and3
browser scenarios/build/typecheck passed. Live isolated VM108 test:
call821559116 -> recording183401214, entered22:00UTC, recorded21:56:10UTC,
one metadata and one transcript request,86144bytes SHA256
76c44ab52cd4105d6c4d9fd0762c5d4a6e72f9ffc10721175f4969368a918cd5.
No model calls or production writes. Do not copy its private transcript to production.

Validate installed importer and wrapper with fixture HTTP transport in a disposable
container using actual effective worker mounts and NO service/provider credentials:
full URL and numeric ID resolve correct endpoint, +/-10minute boundary holds.
Verify trusted HTTPS assets, both human claim policy controls, API automatic flag,
idle healthy runner, corpus88sessions/1924rows/zero unindexed, unchanged real job
and artifact fingerprints/model-call counts. Returned receipt must explicitly
confirm the new acquisition module is mounted in the real worker launch path.

Return safe hashed completion receipt, effective pins, tests and private control
backup paths. Do not replay September15 processing. Request016 Mac permission
work stays stopped. Publication,replacement,retirement and broader migration gates
remain unchanged. Manual-transcript fallback and friendlier acquisition errors
are not included in this patch and must not be claimed fixed.

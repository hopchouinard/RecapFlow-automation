# Development collector activation — 2026-09-09

Management delivery in `cbm-collector-management-ready.md` was read and verified.
The development HTTPS endpoint is now active:
`https://community-brain-dev.patchoutech.lab`.

## Completed on Forge / VM 108

- Certificate fingerprint matched the management handoff; SAN and expiry agree.
  Private-key/public-certificate match and 0600 delivery modes passed without
  printing key material.
- The appended collector identity has exactly `sources:upload:chat`, the expected
  subject/scope and expiry `1789069401`. Existing identity entries and every other
  runtime value matched management's preserved snapshot.
- Recreated only the development API, which became healthy. Model/publication
  flags remain disabled; existing browser OIDC settings are unchanged.
- Added only UFW TCP 443 rules from `10.1.10.60` and `10.1.50.219` to `10.1.30.20`.
  Existing SSH rules were preserved. Started the dedicated pinned nginx proxy.
- Forge verified the HTTPS chain and hostname using the public trusted lab root
  obtained over authenticated VM SSH. Forge's default CA bundle lacks this lab
  root; verification was never disabled. `/health` returned 200, an unauthenticated
  source POST returned 401, and `/api/v1/jobs` returned 404 at the restricted proxy.
- No worker, job submission, model request, production change or remote publication
  was introduced by activation. Existing main API remains on guest loopback 8090.

Certificate expires September 10 at **23:49:29 UTC**; collector token expires
September 10 at **19:43:21 UTC**. This remains a bounded rehearsal without automatic
renewal. Use the dedicated management lifecycle operation for renewal or retirement.

## Manual Mac exercise still needs Mac-side execution

Forge attempted existing-address SSH with batch mode and strict host-key checking
to `pchouinard@10.1.50.219`; TCP port 22 timed out. No reachable Mac execution
channel or Mac filesystem access is available here. The raw collector token stays
only on the Mac as required. Do not transfer it to Forge or VM 108.

Reviewed code is staged on VM 108 under:
`/srv/dev-data/workspaces/cbm-rehearsal-20260909/deploy/community-brain/collector-development/`:

- `manual_upload.py`: private credential loading, TLS/auth checks, fixed meeting
  and source-hash guard, metadata-only receipt.
- `acquisition.py`: the actual restricted collector implementation, including
  checking the hash on the exact in-memory content sent to the backend.

Use the existing Mac management SSH identity to copy these two nonsecret files
into `~/Library/Application Support/CommunityBrainDevelopment/tools/`. Confirm
that tool path and the selected **relative** path under `~/Documents/Zoom` locally.
Do not scan unrelated recording contents or substitute another chat file.
Use a Python environment with `httpx` and the lab CA trusted by that Python
environment (set `SSL_CERT_FILE` to the management-approved public CA bundle if
needed; native macOS trust alone does not prove Python trust).

Once those local paths are confirmed, invoke:

```sh
python3 "$HOME/Library/Application Support/CommunityBrainDevelopment/tools/manual_upload.py" "$CBM_SELECTED_ZOOM_RELATIVE_PATH"
```

The runner reads the already-delivered private Mac credential JSON. It verifies
HTTPS health, unauthenticated upload denial, authenticated transcript/alias upload
denial (403), and hidden job routes (404). Then it uploads only the file matching
SHA-256 `5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084`
for recording `181075701`. Expected size is 6,804 bytes and deduplicated source ID
is `23d9780b-513e-4782-96d2-97211e31e855`. Source upload does not submit a job.

Return only the JSON receipt/check booleans and confirmed tool/relative paths.
No token, raw chat or private credential file is needed. A failed check stops
without an automatic upload retry. This live allowed/denied collector-token
verification has **not yet run**; Forge's unauthenticated checks do not substitute
for it. Eighteen local collector/auth tests passed during preparation.

Pre-upload database baseline: four jobs, 32 processing ModelCall rows, six sources.
The separate indexing journals are not included in that ModelCall count. The
deduplicated manual upload should leave all three counts unchanged.

Staged script SHA-256 values:

- `manual_upload.py`: `fd8523c5d6797a0cc05e31ec236e0735611cba120b9e0b02877ac8343a400772`.
- `acquisition.py`: `aa3b8f69e4bbf822baf188779b74d0129b38cf4d9ab1bd0e70d1e54cdff96988`.

## Manual Mac exercise completed — 2026-09-10

Patrick returned the Mac execution receipt. The reviewed script hashes matched;
TLS health, unauthenticated-upload denial, authenticated non-chat upload denial
and hidden job routes all passed. The allowed chat upload returned the existing
source ID `23d9780b-513e-4782-96d2-97211e31e855`, 6,804 bytes, and the exact
selected SHA-256. Upload was deduplicated.

Confirmed Mac paths:

- Tool: `/Users/pchouinard/Library/Application Support/CommunityBrainDevelopment/tools/manual_upload.py`.
- Relative Zoom file: `2026-09-08 19.41.15 AI Developer Accelerator Coaching Call/2026-09-08-zoom-chat.txt`.

Mac-side counts matched the pre-upload baseline. Forge independently rechecked
four jobs, 32 processing ModelCall rows and six sources, and read/hash-verified
the selected source privately. No new job, model processing or source duplicate
was introduced. Live collector acceptance is complete for this one selected file;
the Mac checks are operator-supplied evidence, with database/storage verification
performed independently on VM 108. No recurring sync or production cutover occurred.

The bounded endpoint and credentials retain their documented September 10
expiries. This completion does not install renewal, alter retention or revoke
credentials automatically. Remote publication remains disabled.

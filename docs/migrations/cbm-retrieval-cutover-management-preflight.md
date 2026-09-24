# Retrieval cutover: management preflight and scoped identity

Patrick approved the retrieval-only cutover phase on September 10, 2026. This
handoff requests its required preflight using the Mac's existing VM101,
Traefik and Infisical management access. Forge has VM108/109 administration and
a read-only infrastructure broker, not those management capabilities. No further
routine approval or transfer of management credentials is needed.

**Hold the active Open WebUI endpoint switch until Forge verifies source parity,
freshness ownership and the prepared target.** Processing activation, publication
and retirement remain outside this phase. Existing bounded jobs' indexing events
must remain inert.

## Open WebUI inspection and reversible connection preparation

Identify the actual live VM101 container and persisted Community Brain filter,
its enablement/model assignment and all valve settings. Privately preserve the
exact filter source/hash, valve values and a consistent copy of its application
state sufficient to restore those settings. Report nonsecret setting names,
source hash, current retrieval URL and rollback procedure. Never print its API
key or copy the WebUI DB/other secrets into Forge or Git. Compare the live filter
source to the preserved and current repository version; do not re-upload it as
part of the connection change (uploads can reset unrelated valves).

Repository evidence: `Filter.Valves.retrieval_url` is a complete endpoint and
`_retrieve_chunks` posts to it directly, using `X-API-Key` from `api_key`. The new full
value is **`https://community-brain.patchoutech.lab/retrieval/query`**. Preserve
all other valves, prompts, model selections and filter content. Verify this
contract against the actual live filter before preparing its change.

Observe the outgoing IP from the actual Open WebUI runtime and verify its DNS and
lab CA trust. Add only that verified source to the Community Brain Traefik router
allowlist, preserving the existing entries and all guest source restrictions.
Do not broaden subnet ingress. If a trust/config update requires recreating
Open WebUI, report its exact impact first and preserve the private rollback state;
prefer a scoped trust delivery that can be verified before the active setting changes.

Create an independent Infisical-managed `retrieval:read` identity for scope
`community-brain`, subject `community-brain-openwebui`. Use a seven-day initial
expiry with explicit Mac rotation ownership, replacement before expiry and
coordinated server/client refresh. This is distinct from the one-day probes and
from any development/submission key. Persist authority in
`homelab/prod /applications/community-brain`, and report expiry and renewal
procedure. Do not expose the raw token to Forge or use it in process arguments.

Add only its hash/permission/expiry record to VM109's API identity map, preserving
existing identities. Render through Infisical and coordinate the brief API reload
using the already approved standalone staging invocation (same immutable image,
read-only mounts and disabled model/publication flags). Verify current probes and
Patrick's existing claims remain valid. Prepare the raw token privately on VM101
for a temporary connection test; do not replace the active filter valve yet.

From the actual Open WebUI runtime, test the new full URL using the scoped key
and verified HTTPS. Use one of the already exercised retrieval-only questions;
record status, result IDs and source path, never returned transcript text or the
key. Check missing/invalid key denial. This test uses query embeddings only and
must not call a chat-generation model. Restore/remove only temporary probe state.

## Fresh source inventory and drift delivery

Read current source corpus/config/registries and schedules on VM101. Report the
actual absolute paths, table row/session/schema/dimension counts, embedding-model
provenance, extraction-status counts, current FTS row coverage, and hashes for
all corpus/config files. Also enumerate active n8n/manual ingestion, lint/cron,
artifact-push and other corpus writers, their schedules, active jobs and any
last-run state. Do not infer no writers from a quiet process list alone. Read-only
inspection must not rebuild an index or invoke ingestion.

Compare against the September 9 source preservation and the pinned delivered
management manifest `4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7`.
Report changed/added/deleted files and rows separately from the known derived
candidate differences: 13 approved divider exclusions and rebuilt FTS coverage.
Preserve all newer source content. New failed chunks or identity/schema changes
must not be silently folded into the old exclusion policy.

If files/data differ, deliver only the relevant fresh data-only corpus/config and
provenance inputs, with before/after file hashes and a path/size/hash manifest, to
VM108 `/srv/dev-data/artifacts/cbm-retrieval-cutover-source/`, root-private.
Use the same allowlist/data-only policy as the preserved-corpus handoff. No n8n
DB, environment, credentials, `.git`, WebUI database or runtime code is delivered.
If source bytes are unchanged, an exact verified comparison receipt is sufficient;
do not recopy unchanged private data merely to produce a new archive.

This initial inventory must not start a prolonged writer pause. Report the exact
pause/resume mechanism and all writer paths so Forge can establish the final
bounded cutover window or a tested refresh policy. Do not switch live retrieval
while old-host writes can silently make its new target stale. The phase explicitly
holds the endpoint change if freshness ownership cannot be established.

## Return receipt

Return public settings/source hashes, private rollback/token paths, identity
expiry/renewal, observed client IP, narrow route change, actual-runtime TLS/auth
checks, source drift comparison and data-only delivery paths if required. Identify
unfinished checks precisely. Confirm the active Open WebUI URL remains unchanged,
no model generation/ingestion/publication ran, and old services were preserved.

The existing probes expire September 11 at 02:05:38 UTC. Keep their explicit
renewal requirement visible; issuing the new retrieval identity does not renew
monitoring or submission tokens. After this receipt Forge can verify the final
candidate and set out the exact switch/rollback sequence within the approved phase.

# Acquisition-only Fathom rehearsal

Status: **acquisition-only rehearsal completed**. No model processing authorized.
Authorization: [Fathom access handoff](cbm-fathom-access.md), 2026-09-09.

Patrick explicitly permits reuse of the existing n8n Fathom credential, now
managed in Infisical. This supersedes the earlier request for an independently
scoped development key. Provider access remains that of the shared credential;
only the rehearsal's use is restricted. No n8n credential binding, production
service or provider setting was changed. Rotation remains coordinated with n8n.

## Configuration and isolation

`deploy/community-brain/compose.acquisition-development.yml` adds only a profiled
one-shot `acquisition-worker` to the private development project. Its explicit
environment mapping receives `CB_FATHOM_API_KEY` from the VM's root-owned mode
0600 `/etc/community-brain-development/fathom.env`. The VM-only
`live-development/acquisition_config.py` validates combined Compose using both
private `--env-file` inputs and `config --quiet`; it never starts a container.
No management identity or secret was obtained on Forge or printed.

The acquisition worker has no OpenRouter credential, corpus mount, published
port, restart policy, polling loop or publication adapter. Model calls and network
publication are explicitly false. The API/SPA receives no Fathom credential.
The existing healthy API and private database/JetStream state remain intact.

`live-development/acquisition_worker.py` accepts the selected job ID, numeric
recording ID and exact stored start timestamp. It requires a fresh, queued
acquisition stage for that recording in the development scope. Weekly mode with
no chat leaves processing waiting for input after the transcript is saved.
The model transport always raises; only one acquisition event is consumed.

The Fathom request guard permits HTTPS GET metadata lookup and a single direct
transcript GET for the selected recording. It limits metadata pagination to five
pages within the adapter's two-day window, disables transcript, summary, action
item, highlight and CRM inclusion on metadata requests, and rejects unrelated
recordings, media routes and all mutations. Meeting timestamp verification still
precedes transcript retrieval. Lookup date filtering is based on provider
`created_at`, so delayed recording creation may require a reviewed lookup window;
do not silently broaden the search if no match is found.

Metadata flags and date semantics were checked against
[the Fathom meeting-list reference](https://developers.fathom.ai/api-reference/meetings/list-meetings).
These application restrictions do not imply provider-enforced credential scope.

## Verification completed

- Combined Compose v2 validation passed on VM 108 using private inputs; no worker
  was started and no Fathom metadata/transcript API request was made in this turn.
- Private rendered file ownership/mode verified without printing its value.
- Running API environment checked for absence of the Fathom key; no acquisition
  worker is running.
- Sixteen acquisition/rehearsal tests passed with mocked provider requests,
  including wrong-recording rejection, metadata inclusion controls, exactly one
  transcript fetch, blocked mutations/media/unselected reads and denied models.
- Changed code passed Ruff; `git diff --check` passed. Earlier changes preserved.

## Next action after selection

Ask Patrick for one recording URL/ID, or title and date. If lookup is needed,
use a narrow metadata-only candidate list before choosing anything ambiguous.
Do not create an acquisition job or fetch a transcript until the selection is
explicit. Resolve its actual recording ID/start time, submit the acquisition-only
job with a stable idempotency key, and run this worker once with that same identity.

Report only identity/time-match verification, stage status, private source path,
size and hash. Never print the credential or raw transcript in chat. Keep the
worker stopped afterward. Any model processing of this real recording requires
Patrick's separate explicit approval. No recurring polling, remote publication,
production deployment or cutover is authorized by this rehearsal.

## Recording selected; lookup date pending

Patrick selected `https://fathom.video/calls/812746883` on 2026-09-09. The next
required input is the recording date (timezone if known), to establish a narrow
metadata lookup window. No recording timestamp is inferred from its numeric ID.
The provider's documented API exposes meeting metadata through a date-filtered
list; no direct recording-metadata endpoint is documented in its API index.

The acquisition worker now includes an explicit `--lookup` mode, still using the
credential only inside this one-shot service. It accepts at most a three-day
window, examines at most five metadata pages, emits only the selected recording's
ID/title/start/end, and excludes transcript and summary inclusion. It creates no
job and never fetches a transcript. Nine focused rehearsal tests passed,
including broad-window rejection before network and omission of unrelated
metadata. No live lookup or acquisition was started while awaiting the date.

## Completed selected acquisition — 2026-09-09

Patrick supplied the recording URL and confirmed September 8, 2026 in Toronto.
The metadata lookup used `2026-09-08T04:00:00Z` through
`2026-09-10T04:00:00Z`, with content inclusion disabled. Toronto was on EDT
(UTC−04:00) for this date; the IANA zone `America/Toronto` was used.

Identity verification:

- Selected call URL: `https://fathom.video/calls/812746883`.
- Exact provider metadata URL matched that selection. The URL call number differs
  from the API recording ID: **`181075701`**. Lookup was corrected and regression
  tested to resolve this mapping rather than assume the numbers are interchangeable.
- Title: AI Developer Accelerator — Coaching Call.
- Start: **2026-09-08 21:54:33 UTC / 17:54:33 Toronto**.
- End: 2026-09-08 23:41:19 UTC / 19:41:19 Toronto.
- Job: `33cc7538-e326-4f74-93ef-f2fcbb5c1624`, scope `community-brain-dev`.

The acquisition worker first encountered an old terminal notification from the
synthetic exercise and exited before claiming the selected job or fetching its
transcript. The runner now acknowledges only verified terminal duplicates whose
stage/job/outbox/generation agree, with a ten-message ceiling; it refuses unrelated
active work. This does not execute another job or introduce recurring polling.
The next invocation completed the acquisition stage on its **first claimed
attempt**. Exactly the selected transcript was requested after metadata/time match.

Output verification:

- Source ID: `27969d75-10a9-4a46-8cf4-b63d1d7035d9`.
- Size: **112,886 bytes**, **1,196 formatted lines**.
- SHA-256: `79540c3f3f08a09dee48d5784026e0f980ec8a9fb85414091fdffba61fe18f75`.
- Private container path: `/state/files/c09d074305074e88915573e4a9cd910c`.
- Persistent location: VM 108 Docker volume `cbm-live-development_files`, object
  `c09d074305074e88915573e4a9cd910c`. Do not copy raw contents into chat or Git.
- A storage read verified the recorded hash. Acquisition is `succeeded`;
  processing is `waiting_for_input` (no chat supplied). **Zero model calls and
  zero generated artifacts** for this job; indexing remains blocked and Git/
  distribution are `not_requested`. No real recording was added to retrieval.

The one-shot worker is removed. No recurring polling, provider mutations, media
download, model processing, remote publication or production change occurred.
The healthy API has no Fathom credential; shared credential management remains
in Infisical with n8n's encrypted operational copy unchanged.

Safe metadata/receipt evidence is in the private VM artifact directory:
`fathom-selected-metadata.json`, `fathom-acquisition-job.json`,
`fathom-acquisition-result.log`, and `fathom-acquisition-receipt.json`.
Twenty focused acquisition/rehearsal tests passed. Ruff and `git diff --check`
passed; no full suite rerun was needed for these isolated helper changes.

The next step requires Patrick's explicit approval before sending this recording
to OpenRouter. A transcript-only processing run can use the existing backfill
mode without inventing a Zoom chat, and must remain within the provider's existing
US$5 total cap. Otherwise leave the acquired source waiting. Do not infer model
processing approval from the permission to retrieve the transcript.

### Subsequent explicit processing approval

Patrick subsequently approved transcript-only OpenRouter processing under the
existing US$5 total cap. A separate backfill child completed with nine successful
requests and three verified artifacts; the original acquisition job and source
remain unchanged. See [processing results](cbm-recording-processing-results.md)
for cost, hashes and evidence. Indexing of this recording remains unexecuted and
remote publication remains disabled.

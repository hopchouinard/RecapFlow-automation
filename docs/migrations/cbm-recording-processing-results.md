# Selected recording processing — 2026-09-09

Patrick explicitly approved transcript-only OpenRouter processing of the selected
Fathom call within the existing US$5 total development cap. The bounded run
completed on VM 108. Frozen `processing-v1` prompts were unchanged.

## Identity and execution

- Call URL: `https://fathom.video/calls/812746883`; API recording `181075701`.
- Meeting start: September 8, 2026 at 17:54:33 America/Toronto (21:54:33 UTC).
- Acquisition parent: `33cc7538-e326-4f74-93ef-f2fcbb5c1624`.
- Processing child: `acd77c69-10d8-4079-9514-35ca5cc0c9fc`.
- Mode: `transcript_backfill`; no Zoom chat was invented or additional transcript fetched.
- Source: `27969d75-10a9-4a46-8cf4-b63d1d7035d9`, 112,886 bytes, unchanged.
- Source SHA-256: `79540c3f3f08a09dee48d5784026e0f980ec8a9fb85414091fdffba61fe18f75`.

All nine model requests succeeded on their first attempt, with no retries or
unresolved intents. Processing succeeded and all three artifacts are ready.
The one-shot worker exited successfully and was removed. The acquisition parent
retains its waiting-for-input processing state and has no model calls itself.

## Verified artifacts

Storage hashes and authenticated API downloads agreed for every artifact:

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `prepared-transcript.md` | 64,534 | `802637a522f5ec0000a4ade8c4a6fc9e526e09ccd8de5ec5178ce5a97560f545` |
| `extracted-signal.md` | 14,167 | `fb4f9676f0a3ed0c1fbd0ad4af79b0a357c97fbf29a728934f16551a01998f76` |
| `community-post.md` | 12,711 | `700ecc70aa4cfc3fd0ecceecea3b50c94cd64e648aacd19118100da0475678b8` |

Contents remain in private VM storage and are available through the authenticated
development workspace. These checks establish delivery and integrity, not a
semantic quality sign-off. The development alias snapshot is not a validation
of the production alias registry.

## Cost and boundaries

This run cost **US$0.60421275**. Provider-confirmed cumulative usage is
**US$0.62528478**, leaving **US$4.37471522** under the non-resetting US$5 key limit.
The runner enforced a twelve-request ceiling and checked allowance before each call.

No indexing or embedding of this recording was executed. Its indexing stage is
pending; Git and distribution are `not_requested`. No remote publication,
recurring Fathom polling, production deployment or cutover occurred. Only the
healthy API and disposable PostgreSQL/JetStream services remain running, with
the API bound to VM loopback.

A local, provider-free indexing preflight counted 21 prepared-transcript chunks,
six extracted-signal chunks and two community-post chunks. Indexing would require
30 extraction requests without retries, followed by Ollama embeddings into the
isolated development corpus. That additional processing awaits explicit approval
and will need a matching bounded request ceiling before execution.

## Evidence and remaining review

Metadata-only evidence is saved under
`/srv/dev-data/artifacts/cbm-live-development-20260909/` on VM 108:
`recording-processing-job.json`, `recording-processing.log`,
`recording-processing-result.json`, `recording-artifact-verification.json`, and
`allowance-final.json`. The earlier completed snapshot predates this recording
and does not contain these new source/output objects.

Twenty-four focused guard/deployment tests passed; Ruff and `git diff --check`
passed. The selected-recording guard covers scope, parent, source, mode, recording
ID and timestamp. No broad suite rerun was needed for these rehearsal helper changes.

[CBM-10's explicit final quality backlog](cbm-final-quality-backlog.md) remains
the last step of the whole migration. Q-03 records the Fathom turn-header/splitter
mismatch; this successful run does not close that finding. Q-01 and Q-02 also
remain open. No frozen prompt or splitter was changed to address them here.

## Subsequently approved indexing and retrieval — 2026-09-09

Patrick explicitly approved the proposed isolated indexing exercise. The same
child's indexing stage completed on its first attempt: **29 chunks written,
zero failed**, comprising 21 prepared-transcript, six extracted-signal and two
community-post chunks. All **30 extraction requests** have matching private
response receipts. The runner enforced exactly that request ceiling, a separate
recording journal, selected-recording identity checks and allowance verification
before each request. Existing intents or a previous stage attempt prevent an
automatic repeat.

The isolated LanceDB corpus now contains **38 chunks**: the original nine
synthetic chunks plus this recording's 29, all with 768-dimensional embeddings
from the retained Ollama dependency. Extraction used
`google/gemini-3.1-flash-lite-preview`. The development registry flagged 33 unknown
speaker strings; this is not a validated production registry or a speaker-identity
quality sign-off. The registry and frozen prompts were not changed.

Two authenticated reader queries returned five results each for the September 8
date filter, with provenance and both BM25 and vector contributions. An unmatched
date range returned no chunks. Legacy read transport passed; missing credentials
returned 401 and mutation routes returned 404. Result content was not printed or
copied to Forge. These checks validate retrieval plumbing and filtering, not a
semantic ranking-equivalence evaluation.

Indexing cost **US$0.03412550**. Provider-confirmed cumulative usage is now
**US$0.65941028**, leaving **US$4.34058972** under the same non-resetting US$5 cap.
The worker exited successfully and was removed. Git/distribution remain
`not_requested`; remote publication, recurring intake and production changes
remain prohibited. Authenticated artifact download/hash checks were repeated
after indexing.

Additional VM evidence: `recording-indexing.log`, `recording-indexing-result.json`,
`recording-retrieval-result.json` and updated `allowance-final.json`. Private
request/response accounting is `/state/files/recording-indexing-calls.jsonl`.
Twenty-five focused guard/deployment tests and Ruff passed. A local file-mode
issue prevented the first retrieval-check container from reading its helper;
setting that nonsecret helper to 0644 resolved it before any retrieval request.
An initial diagnostic used the wrong embedding column name; the corrected
`embedding` check verified all 29 vectors without modifying corpus data.

The real transcript-backfill path is now rehearsed through acquisition,
processing, indexing and authenticated retrieval. A real weekly path still needs
Patrick's matching Zoom chat selection and approval for processing the combined
inputs. Do not infer permission to read arbitrary Mac files, install a recurring
collector, or rerun the recording from this indexing approval. CBM-10 stays last.

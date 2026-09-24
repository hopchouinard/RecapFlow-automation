# Selected real weekly rehearsal — prepared 2026-09-09

Patrick supplied `2026-09-08-zoom-chat.txt` for the selected September 8 call.
The attachment was verified as nonempty UTF-8, without NUL characters, and
uploaded through the authenticated development source API. No new job was
submitted and no worker or model call was started.

## Selected inputs

- Fathom call URL `812746883`, API recording `181075701`.
- Start `2026-09-08T21:54:33Z`, local date September 8, America/Toronto.
- Parent acquisition job `33cc7538-e326-4f74-93ef-f2fcbb5c1624`.
- Existing transcript source `27969d75-10a9-4a46-8cf4-b63d1d7035d9`.
- Chat source `23d9780b-513e-4782-96d2-97211e31e855`, **6,804 bytes / 157 lines**.
- Chat SHA-256 `5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084`.

The source API's returned size and hash matched the attachment exactly. Meeting
association is Patrick's explicit selection, not independent proof from the
chat's contents. No raw chat was printed or placed in the repository. The private
VM delivery copy is `selected-weekly-chat.txt`, mode 0600, in
`/srv/dev-data/artifacts/cbm-live-development-20260909/`; source receipt metadata
is `weekly-chat-source.json`. The durable API source is separate from this copy.

## Concrete next exercise awaiting approval

Create a separate `weekly` rerun of the acquisition parent, using its existing
transcript and development alias snapshot plus this exact chat source. Preserve
the completed transcript-only child and its artifacts. Use frozen `processing-v1`
to generate the six weekly artifacts, including the compressed post and weekly
invite; verify authenticated downloads and hashes, then remove the bounded worker.

Recheck allowance before execution and each paid request. The last verified
remaining allowance was US$4.34058972 under the non-resetting US$5 total key cap.
No new Fathom fetch is needed. Combined-input model processing requires Patrick's
approval because the earlier processing approval was explicitly transcript-only.

Do not run indexing for this new job: the development corpus already reserves
September 8 for the completed backfill child. Any comparison/indexing of weekly
outputs needs a separate isolated corpus or an explicitly reviewed replacement;
never overwrite the current session implicitly. Remote publication, recurring
intake and production changes remain prohibited. CBM-10's quality review stays
the final step of the whole migration.

## Approved execution completed — 2026-09-09

Patrick explicitly approved this combined-input exercise. Weekly child
`7bce1799-dd0f-40fa-a444-a7797ff38b1b` completed processing with **15 requests,
all successful on their first attempt**. The weekly splitter produced three
preparation and three signal-map requests, followed by reduction, six post
sections, compression and the invite. Frozen weekly prompts/models remained
unchanged. The worker enforced a 20-request ceiling, verified the selected
transcript/chat identity and checked remaining allowance before each paid call.

All six artifacts passed storage and authenticated download SHA-256 checks:

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `transcript.txt` | 112,886 | `79540c3f3f08a09dee48d5784026e0f980ec8a9fb85414091fdffba61fe18f75` |
| `prepared-transcript.md` | 69,854 | `f27db30016e1c73362215071bdade5fc49ac70526a9c3b42135a1c995fe99d27` |
| `extracted-signal.md` | 18,448 | `132b4e9ee701c70b16f87681c4ce637f78871b862494007b9511b6e85a6b259f` |
| `community-post.md` | 16,418 | `c74b068c9dea60d0990a0b5c54d87b9c3bf6a459b43a6c51406b16d262d5d289` |
| `community-post-compressed.md` | 14,769 | `c768ca35b762d4955eb0fd7424288b0b6f56b6e582930df9f043b7fbf0176251` |
| `2026-09-15-weekly-invite.md` | 1,631 | `5273d8e31870ed17d7598005d6e4671e2054c29ae334c55368459d9659bdb8b1` |

Both immutable source hashes were reverified. This is integrity and structural
execution evidence, not semantic quality acceptance. CBM-10 remains last.

Receipt cost is **US$0.32885985**. After a brief provider usage-reporting lag,
the key total reconciled to **US$0.98827013**, leaving **US$4.01172987** under
the non-resetting US$5 total limit. No retries or unresolved intents remain.
The bounded worker exited 0 and was removed. Indexing is pending with no worker;
Git and distribution are `not_requested`. No corpus replacement or publication
was performed. Twenty-six focused guard/deployment checks, Ruff and diff checks
passed.

Metadata evidence is in the private VM artifact directory: `weekly-processing-job.json`,
`weekly-processing.log`, `weekly-processing-result.json`,
`weekly-artifact-verification.json`, and updated `allowance-final.json`.

### Coordinated private backup

With all workers stopped, the API was briefly stopped while PostgreSQL and
files/config/corpus were captured. It restarted healthy on loopback. Snapshot:
`/srv/dev-data/artifacts/cbm-live-development-20260909/weekly-snapshot-20260909T230655Z`.
Directory mode 0700 and file mode 0600 keep source and response contents private.

| File | SHA-256 |
| --- | --- |
| `database.dump` | `388111668820d1777b7003eafc6c26f5ffb3fc5e6d1cf5704ffc2af08ae2ee1a` |
| `files.tar.gz` | `45f4399654f8885eab05d5489b60ff4d7e582ed4582c53629fb540ec2c089145` |
| `config.tar.gz` | `11560f9af1569433f7a46350629a77f0b2f1165fd9e0a68e028f128df220f8ec` |
| `corpus.tar.gz` | `3a3bc285bd196b643a36d5b4396f840e5c19a49945e2614a9c5cfc64f68da8f0` |

`pg_restore --list` and all tar archive listings passed. This snapshot has not
undergone a full restore test. Queue contents are not backed up here; recovery
must reconstruct eligible delivery from durable records with model/publication
disabled, following the deployment recovery packet.

### Next isolated indexing proposal

A provider-free parser/chunker preflight counted 30 chunks (21 prepared,
six signal, three post), requiring 31 extraction requests without retries plus
Ollama embeddings. Three paragraphs exceeded the 1,500-token target and were
retained as oversized chunks by the existing behavior (1,905 / 1,824 / 1,749
estimated tokens). No splitter change or additional paid call was made.
Proposed destination: a separate development corpus, preserving the current
backfill corpus and leaving the main retrieval API unchanged. Await approval
before this additional processing; remote publication remains disabled.

## Approved isolated weekly indexing completed

Patrick approved the separate-corpus proposal. Indexing completed on the first
claimed attempt with **30 chunks, zero failures and 31 request/response pairs**.
All vectors have 768 dimensions; extraction used the retained Gemini configuration
and embeddings used the existing Ollama dependency. Chunk counts matched preflight.
The copied development registry flagged 28 unknown speaker strings; production
registry and semantic-quality validation remain outstanding, not silently accepted.

Destination volumes are `cbm-live-development_weekly-corpus` and
`cbm-live-development_weekly-config`. The initializer copied the development
configuration and established a job-specific isolation marker. The worker did
not mount the original corpus or configuration. Before execution, resolved
Compose checks verified these mounts and the temporary API's absent host ports
and provider credentials. Its only paid-call journal is
`/state/files/weekly-indexing-calls.jsonl`, with an enforced 31-request ceiling.

Two authenticated queries against the temporary weekly API returned five results
each, with provenance, correct date filtering and vector/BM25 contributions.
An excluded date returned no results; legacy authentication succeeded, missing
authentication returned 401 and mutation routes returned 404. All **27 files in
the original corpus matched their before/after hashes**. The original API was
not reconfigured or restarted for this exercise. Worker and temporary weekly API
were removed; the normal loopback API remains healthy.

Indexing cost **US$0.03618950**. After provider reporting caught up, cumulative
usage reconciled to **US$1.02445963**, leaving **US$3.97554037** under the US$5
non-resetting cap. Git and distribution remain `not_requested`; there was no
remote publication, recurring intake or production change.

Preparation fixes occurred before any job claim or paid call: Compose needed an
explicit file for the inherited API service, and initialization needed ownership
set to root before chmod, then transferred to runtime UID. Recovery initialization
accepts only the exact marker plus a byte-identical copied config, refusing any
existing corpus data. Neither issue required replaying an external effect.
Twenty-six focused guard/deployment tests, Ruff and diff checks passed.

Private evidence: `weekly-indexing.log`, `weekly-indexing-result.json`,
`weekly-retrieval-result.json`, `main-corpus-before-weekly.json` and updated
`allowance-final.json`. Completed weekly volume archives passed tar read checks:

| Archive | SHA-256 |
| --- | --- |
| `weekly-corpus-completed.tar.gz` | `1b9353eb016c8970be4fb01affb14cf3e9d533dec278d07a3864e29cadcc10ce` |
| `weekly-config-completed.tar.gz` | `24e8462f1d92ea970184f0b58ec5625cf3477739c546b0d2bd776a62ca89dd4f` |

These supplemental volume archives are not a new coordinated database snapshot
or a full restore test. The earlier coordinated snapshot predates weekly indexing.
CBM-10 remains the final quality-review step.

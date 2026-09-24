# Bounded production worker results — September 10, 2026

**Both approved synthetic jobs succeeded on their first processing attempt.**
The dedicated non-resetting US$2 key spent **US$0.04381715**, leaving
**US$1.95618285**. No additional processing is authorized by unused allowance.
The private submission API and bounded worker have been removed. Only the public
read-only staging API and Alloy remain running.

| Mode | Job ID | Model requests | Artifacts |
|---|---|---:|---:|
| Weekly | `f6e9abed-e862-4eb7-a231-e98467adcaba` | 8 | 6 |
| Transcript backfill | `91d77409-afed-4625-97cb-748c8b637991` | 6 | 3 |

Both jobs used `production-synthetic-20260910` and the exact existing synthetic
fixture bytes. The API also froze the preserved speaker-alias block as the third
source. No Fathom recording, historical transcript or Mac chat was processed.
Frozen model IDs were available at preflight; the key had zero prior usage.

## Execution and verification

The temporary API had no host port or model key and used a separate short-lived
submission identity. It was removed after recording exactly two job IDs. The
bounded worker used the existing immutable production image with reviewed mounted
helpers, verified both source sets and fresh stage state, and dispatched only
those processing events through the scoped TLS-first queue connection. No general
consumer loop or retry was started. Each job had a 12-request ceiling.

All 14 durable model responses succeeded and their file hashes verified, alongside
all three sources and nine artifacts. Both jobs have `processing=succeeded` and
`artifacts=ready`. All nonprocessing stages have zero attempts. Indexing remains
pending; no indexing event was dispatched. No corpus, config, acquisition, Git or
distribution handler ran. Preserved corpus/config hashes are unchanged.

The independent read identity downloaded and verified every artifact through the
public staging API on the guest. Patrick can inspect the two jobs using the
existing read-only browser login. No board publication was performed.

Provider key usage initially lagged saved response cost. A later key-information
check matched exactly at US$0.04381715; both sources now reconcile. No inference
request was used to perform that check. The key and all tokens remained private
on VM109. Temporary credentials expire September 11 at 02:05:38 UTC; no renewal
or implicit additional model allowance was granted.

Targeted regression verification: 16 tests passed (five bounded-runner tests with
real disposable DB/queue and 11 deployment tests); helper Ruff and diff checks
passed. The previous broader DB/queue suite passed 28 tests. Application image
bytes were unchanged; private `helper-hashes.json` records the execution helpers.

## Managed-state recovery checkpoint

With all writer processes stopped, captured `files`, `config` and `corpus` in a
53-file archive. Every source hash matched before/after capture. Extracted into a
fresh disposable directory and verified every hash; removed that test directory.

Private evidence root on VM109:
`/srv/community-brain/artifacts/cbm-bounded-production-20260910/`

- `jobs.json`, `approval/jobs.json`: the two explicit IDs.
- `preflight.json`, `allowance.json`: numeric provider receipts.
- `helper-hashes.json`, `worker-started`, `worker.log`: execution evidence and
  restart refusal marker. Do not remove the marker to retry.
- `job-verification.log`, `durable-audit.log`: metadata and verified references.
- `managed-state.tar.gz`, `managed-state-manifest.json`, `file-restore-result.json`.
- Archive SHA-256: `8e0ae8cf17ebeea4e0248422fdea4f79eb7ea455fc3b4194e05b1622d8ac4941`.

Repository receipts: `cbm-production-bounded-audit.json` and
`cbm-production-bounded-allowance.json`. Private logs and archives are not Git
publication inputs.

## Required Mac management continuation: nonempty DB restore

Use the existing scoped backup procedure to dump `community_brain_prod` now, while
writers remain stopped, then copy and hash-verify the dump on VM109. Pair it with
the above managed-state archive in a recovery receipt. Do not restart any worker
or submit work between these captures. The read-only public API may stay running.

Restore the dump into a disposable database, without queue consumers or provider
credentials. Verify revision `0001_jobs`, all ten table definitions/grants/owners,
and exact row counts against production. Expected key counts: two jobs, three
sources, nine artifacts and 14 successful model responses. Check both job IDs,
first-attempt processing success, ready artifacts and zero nonprocessing attempts.
Verify all restored source/artifact/response references against the independently
extracted 53-file archive. Queued indexing/outbox records must remain inert:
restore acceptance does not authorize delivery or model/indexing execution.

Confirm the production source schema/counts stayed unchanged; remove only the
disposable restore database/copy. Preserve original evidence and backups. Return
the paired manifest, dump/hash/path, complete reference-check result and off-host
copy receipt; capture the coordinated artifacts in the existing PBS procedure.
No further routine approval is needed for this already approved recovery step.

The earlier ten-table restore verified an empty jobs database; it does not close
this nonempty recovery check. No full guest restore or PITR is claimed. Cutover,
publication and retirement remain gated. CBM-10's explicit quality backlog stays
last; successful synthetic processing does not close its semantic findings.

## Recovery continuation completed

The [nonempty recovery receipt](cbm-production-nonempty-recovery-readiness.md)
closes the management continuation above: exact table definitions/grants/owners,
row counts and full-row hashes matched; all 26 references matched the 53-file
archive. Production was unchanged and disposable copies were removed. Forge
independently rechecked the copied dump SHA-256 on VM109. Paired PBS checkpoint:
`pbs:backup/vm/109/2026-09-10T03:32:39Z`. This completes the approved bounded phase,
not a full guest restore or cutover. Next proposal: controlled retrieval cutover
with explicit final drift, freshness/ownership and rollback prerequisites.

# Preserved corpus rehearsal — 2026-09-10

The management-delivered data-only archive was restored and inspected on VM 108.
Production, the original preservation archive and both existing development
corpora remain unchanged. No generation call, re-extraction, re-embedding or
remote publication occurred. Only four query embeddings used the retained Ollama
endpoint for the representative queries, plus the excluded-date query embedding.

## Preservation and delivery integrity

Delivery directory: `/srv/dev-data/artifacts/cbm-preserved-corpus-rehearsal/`.

- Management manifest SHA-256:
  `4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7`.
- Archive SHA-256:
  `ecb100f2e4af7c3ae4350392158f936a2756ea1852fc1d6728812237502275a3`.
- Verified **2,627 files / 108,764,895 bytes**, before opening the corpus and again
  after retrieval/export checks.
- Management's source provenance identifies preserved commit
  `b6f1aa46996d4ab7ccbbaed567864cc2d71f433a` and September 9 capture.
  Its manifest reports 2,624 files matching the original durable-file inventory;
  three preserved raw transcripts are covered by the workspace archive rather
  than that narrower inventory. This distinction is retained, not reported as
  2,627 independent original durable-file hash matches.

The fresh private copy is
`/srv/dev-data/workspaces/cbm-preserved-20260910/delivery/`. Paths were normalized
to corpus/config/output/historical without changing file contents. The explicit
data allowlist accommodates delivered `meta.json`, legacy signal Markdown and
nonsecret canonicalization proposals. It rejects unexpected paths, links,
duplicates and mismatched bytes. Normalized manifest SHA-256:
`81ea69b8d6d650ac3c6285fe72cafa6a38973f037af2ee84be7bd96362c2acd8`.

## Corpus and retrieval

- **87 sessions / 1,914 rows**, schema 1.1, 768-dimensional Arrow vector field.
- FTS validation passed using the development image's LanceDB 0.34.0. Management
  had independently inspected the archive with reader 0.30.2. The model identity
  `nomic-embed-text` comes from preserved code/config provenance; vector dimensions
  alone do not identify a model.
- **1,901 successful / 13 failed extraction rows**.
- All **260 source-file references** resolve directly to delivered output files.
  Mapping verifies file presence, not a fresh semantic validation of each chunk.
- Four authenticated queries covered unfiltered content, September 8, early-2025
  sessions and second-quarter-2026 sessions. Each returned five results with
  ground truth/provenance, BM25 and vector contributions and correct date filtering.
  Every returned row had successful extraction status.
- An excluded date returned no chunks; missing auth returned 401, legacy read
  auth worked, and ingestion mutation routes returned 404.

The API was temporary, had no host port or provider generation key, mounted the
preserved data read-only and used the existing scoped development reader token.
It was removed after checks. Main API and corpus mounts were not changed.
These query checks demonstrate compatibility/filtering, not exhaustive ranking
equivalence or a semantic quality sign-off.

## Consumer export blocker and proposed disposition

The actual strict exporter refused with `corpus_has_failed_chunks`, creating no
package. Inspection found that **all 13 failed rows have exactly three bytes of
ground-truth text: `---`**, a Markdown divider. All are prepared-transcript chunks
under preserved `chunk-extraction-v3`, previously attempted with
`google/gemma-4-31b-it`. They contain no meeting prose to recover with a model.

| Session | Divider-only failed rows |
| --- | ---: |
| 2026-05-05 | 2 |
| 2026-05-12 | 3 |
| 2026-06-02 | 3 |
| 2026-06-23 | 2 |
| 2026-07-07 | 2 |
| 2026-09-08 | 1 |

Recommended migration disposition: keep the complete 1,914-row preserved corpus,
and build a separately versioned consumer candidate containing only the 1,901
successful rows. Record the exact excluded IDs/content hashes in the candidate's
provenance; preserve all 87 sessions and verify every retained row unchanged.
Do not weaken the export guard or silently repair/drop rows from the source.
This changes the consumer dataset policy and awaits Patrick's decision; it is
not a request to approve another routine test. No filtered candidate was created.

The permanent cause/prevention belongs to [Q-04 in the final quality backlog](cbm-final-quality-backlog.md),
which remains last. No frozen parser/chunker/prompt behavior was changed here.

## Evidence and limits

Management delivery remains private. Metadata receipts in its directory include
`restore-delivery-receipt.json`, `retrieval-result.json`, and
`post-rehearsal-integrity.json`. Private results under the isolated workspace's
`results/` include `inspection/inspection.json`, `provenance-map.json`,
`provenance-summary.json`, `export-probe-result.json`, and
`failed-chunk-repair-candidates.json` (the latter was named before discovering
that every candidate was only a divider; no repair was attempted).

Sixteen manifest/path-validator tests passed, with Ruff and diff checks. A local
numeric-owner setup issue was corrected before inspection; it did not touch the
delivered files. Runtime corpus/retrieval/export checks ran on actual preserved
data. Consumer-package reopening remains blocked by the policy decision above.

## Approved consumer candidate completed — 2026-09-10

Patrick approved the exact divider-only exclusion policy. Built a fresh table
containing **1,901 successful rows / all 87 sessions**, excluding only the 13
approved failed IDs after checking status, type, session and exact divider
content/hash. Every retained value and Arrow schema matched the source, both
before packaging and after reopening a fresh consumer installation. The complete
1,914-row preserved corpus and delivery hashes remain unchanged. The strict
exporter was not weakened; no extraction or embedding regeneration occurred.

Private candidate directory:
`/srv/dev-data/artifacts/cbm-preserved-corpus-rehearsal/consumer-candidate-v1/`.
Files are 0600 under a 0700 directory. The package is local, not published.

| Artifact | SHA-256 |
| --- | --- |
| `corpus-preserved-20260909-success-only-v1.tar.gz` (12,352,503 bytes) | `5e4f37d6459d820f506fe0b5d6d4db42204dcab26a3bb89592dd8f81fb9707fb` |
| `corpus-manifest.json` | `cc59522ba9fac2861f62e09599e82c6606edd4f2552824f7f5c66046d080361d` |
| `candidate-provenance.json` | `6eb1744080dbe3892f4d13730a89872f2ac6ee9fb1ffc7901c19bb737b620b42` |

The package manifest references the provenance sidecar by hash. That sidecar
records source management/normalized manifests, exact excluded IDs/content hashes
and approved policy. Existing manifest/consumer structure is otherwise preserved.
The archive contains a freshly constructed table, not excluded rows hidden in old
table versions. `build-result.json` records validation.

### Index coverage and controlled retrieval comparison

Fresh consumer retrieval passed the four authenticated query/filter tests, but
initially changed ranking versus the preserved index (four of twenty rank
positions matched). Investigation found:

- Preserved FTS metadata exists, but LanceDB reports **0 indexed / 1,914 unindexed
  current rows**. The earlier FTS check tested presence, not current coverage.
- Candidate coverage is **1,901 indexed / 0 unindexed rows**.
- A vector-only diagnostic using one identical stored query vector returned
  identical top-ten IDs from source and candidate.
- A separate full 1,914-row control copy with a newly built FTS index returned
  **the same top-five IDs in the same order as the candidate for all four queries
  (20/20 positions)**. This isolates the observed ranking change to index rebuilding
  in this sample, not divider exclusions. It is not an exhaustive semantic quality
  evaluation or a claim that the preserved index never returns results.

Source, candidate and control were served through temporary authenticated APIs
with no host ports or generation keys; all were removed. Comparison used only
query embeddings from retained Ollama. Production index bytes were never touched.
The full control exists only in the isolated development workspace.

Evidence beside the delivery: `source-comparison-retrieval-result.json`,
`candidate-retrieval-result.json`, `control-retrieval-result.json`, and
`candidate-comparison-result.json`. Require explicit index coverage checks in
production preparation; index-name presence alone is insufficient. Automatic
coverage maintenance/guard behavior is carried in Q-05 of the final quality backlog.

The initial complete-row scan hit the container's file-descriptor ceiling before
building anything; rerunning the disposable build with `nofile=8192` succeeded.
No host-wide resource limit changed. Twenty-two targeted delivery/exclusion checks
passed. Canonical `scripts/verify-forge.sh` also passed: **150 Node, 887 Python,
23 DB/queue, one component and one browser test**, plus the frontend build.
Python retained 70 existing warnings. No remote publication or production phase
transition has occurred.

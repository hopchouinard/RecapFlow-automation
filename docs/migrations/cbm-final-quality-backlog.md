# CBM-10 — Final migration output-quality review

Owner: Patrick Chouinard. Decision recorded 2026-09-09.
Status: **open, deliberately deferred to the last step of the whole migration**.

Patrick chose to preserve prompt parity throughout the migration and explicitly
requested that these findings be addressed at its end. Schedule this review after
CBM-08 deployment/cutover/stabilization and CBM-09's separately gated retrieval
transition, and after any subsequently added migration work. Keep this ticket
last if the plan grows. It is not a prerequisite for the current development
rehearsal. Production deployment and cutover still require separate authorization.

Do not mark the whole migration complete while this checklist remains unresolved.
Each item needs a documented fix and validation, or Patrick's explicit acceptance
of the remaining limitation. Deferral now is not acceptance or closure.

## Evidence shared by both findings

- Live development job: `f453deaf-0638-4580-9fe6-2b5a47cb1133`.
- Meeting: `live-development-synthetic-20260909`; synthetic inputs only.
- Version: unchanged `processing-v1` prompt/config snapshot.
- Date: 2026-09-09; eight first-attempt model requests; six artifacts passed hashes.
- [Live exercise results](cbm-live-development-results.md).
- Private VM evidence: `/srv/dev-data/artifacts/cbm-live-development-20260909/`.
  `fixture-result.json` identifies artifacts/hashes; `bounded-worker.log` records
  request hashes, models and usage. Original outputs remain immutable in the
  `cbm-live-development_files` volume, with metadata in the development database.
- Structural validation passed. These are semantic quality findings; do not
  misreport them as a migration behavior mismatch or a transport failure.

## Explicit issue checklist

### Q-01 — A declarative sentence is incorrectly annotated as a question

- [ ] **Open.** Affected output: `prepared-transcript.md`.
- Artifact ID: `57395d28-7bfd-412f-a0a7-4b3770fac488`.
- SHA-256: `04ccbc07c1f0b43552881c5b04a6a718759e4d384b0e39da05cb919e6cb7cb06`.
- Source: “A successful startup alone does not prove that stored notes can be
  recovered.” This is a statement; the synthetic transcript asks no question.
- Observed: the preparation model wraps that sentence in `<Q>...</Q>`.
- Expected: retain it as a statement. Use question annotations only for actual
  questions supported by the source; avoid changing the speaker's intent.
- Impact: downstream question/answer extraction or retrieval may treat the
  statement as an unanswered question. That downstream effect has not yet been
  demonstrated; do not count it as an observed retrieval failure. The subsequent
  live retrieval rehearsal did return the incorrectly tagged statement in
  `ground_truth.full_text`; this confirms propagation of the annotation, not
  an independently demonstrated question-classification failure.
- Final-step work: reproduce with the preserved fixture; evaluate a separately
  versioned preparation-prompt and/or validation improvement. Include genuine
  questions, rhetorical questions and ordinary statements in the evaluation.
- Acceptance: this source sentence is no longer question-tagged, genuine questions
  remain recognized, timestamps/speakers/source meaning are preserved, and the
  representative evaluation records before/after results and any regressions.

### Q-02 — Preservation instruction is paraphrased inaccurately

- [ ] **Open.** Affected outputs: `community-post.md` and
  `community-post-compressed.md`.
- Community-post artifact ID: `7b4ccec8-d4f2-4b9f-83e6-17bf9724a984`.
- SHA-256: `7cd2b761f3cb1df6784c08c61be0ed5601c0af57af841df73806981aba5507b9`.
- Compressed-post artifact ID: `632053c8-f2ce-4e44-91ce-7481d16c5239`.
- SHA-256: `9bb4a612b8fa5bcec25d4f4f9fe97bcfad0eac014787cc15cf88fb090a8f20dd`.
- Source: preserve/“keep the original transcript”; separately, test recovery while
  the old service is still working.
- Observed: both posts say “keep the original transcript running throughout,”
  conflating preservation of a document with operation of a service.
- Expected: preserve the transcript and keep the old service operational as
  distinct actions. Compression must not carry forward or introduce this error.
- Impact: the publishable summaries misstate the source instruction. The live
  lexical retrieval check subsequently returned the same inaccurate phrase in
  its top community-post chunk, confirming that the error is also retrievable.
- Final-step work: trace the first inaccurate transformation, evaluate separately
  versioned summary/compression prompt or validation changes, and compare each
  derivative artifact against the original source, not just its preceding stage.
- Acceptance: both outputs distinguish document preservation from service uptime,
  retain the original commitments, introduce no unsupported action, and pass a
  representative source-fidelity review with recorded before/after evidence.

### Q-03 — Backfill splitting does not recognize native Fathom turn headers

- [ ] **Open.** Observed during preflight for approved processing job
  `acd77c69-10d8-4079-9514-35ca5cc0c9fc`, recording `181075701`.
- Input source ID: `27969d75-10a9-4a46-8cf4-b63d1d7035d9`; SHA-256:
  `79540c3f3f08a09dee48d5784026e0f980ec8a9fb85414091fdffba61fe18f75`.
  Original content stays in private VM storage; do not reproduce it here.
- Observed: the preserved Fathom formatter emits `[HH:MM:SS] Speaker: text`,
  while the frozen historical splitter recognizes `HH:MM:SS - Speaker` headers.
  The 112,886-byte acquired source therefore yields one roughly 31,357-token
  block for both preparation and signal mapping, despite a 15,000-token target.
- Impact: larger individual requests and ineffective target-halving for this
  input shape. This is a deterministic format-compatibility limitation in the
  preserved behavior; it does not by itself prove output loss or provider failure.
- Final-step work: evaluate a lossless, provenance-tracked input normalization
  or a separately versioned splitter that accepts both header forms. Preserve
  the original acquired source and frozen v1 behavior for comparison.
- Acceptance: representative native Fathom and historical inputs split at actual
  speaker turns, preserve text/speakers/timestamps and order, respect the token
  target except for explicitly handled oversized individual turns, and show
  measured cost/latency/retry results without degrading output fidelity.

### Q-04 — Divider-only prepared-transcript chunks reach extraction

- [ ] **Open.** Preserved-corpus rehearsal found 13 failed prepared-transcript rows
  across six sessions whose entire `full_text` is the three-byte Markdown divider
  `---`. See [exact scope and evidence](cbm-preserved-corpus-results.md).
- Impact: useless extraction work, failed rows and rejection by the strict
  all-success consumer exporter. Query success guards correctly exclude them.
- Final-step work: trace divider-only segment/chunk creation, distinguish structural
  Markdown from meaningful content, and implement prevention under a reviewed new
  version. Preserve frozen v1 and original artifacts/corpus for comparison.
- Acceptance: meaningful prose and Markdown are preserved, divider-only chunks do
  not reach provider extraction, representative historical/current fixtures show
  no source-text loss, and migration-time exclusions have explicit provenance.
- No model retry, source deletion, parser change or export-policy relaxation was
  performed during this read-only rehearsal.

### Q-05 — FTS presence checks do not establish current-row coverage

- [ ] **Open.** Preserved corpus has FTS metadata but reports zero indexed and
  1,914 unindexed current rows. A fresh index changes rankings; a fresh full-data
  control and approved filtered candidate match exactly for four queries.
  See [controlled evidence](cbm-preserved-corpus-results.md).
- Impact: a structural presence check can pass an index with incomplete coverage;
  query behavior may differ from a fully indexed copy. Do not infer exhaustive
  lexical correctness from one successful hybrid response.
- Final-step work: review lifecycle/maintenance and read-only validation so index
  coverage drift is visible and handled without silent mutation on read paths.
- Acceptance: meaningful drift fixtures, explicit coverage/maintenance policy,
  reproducible ranking checks and monitoring. Preserve the original index for
  comparison; no production rebuild was performed during this rehearsal.
- Interim migration requirement: explicitly verify candidate index coverage during
  deployment preflight. The approved consumer candidate has 1,901/1,901 indexed rows.

### Q-06 — Runtime query configuration paths can silently disable cue features

- [ ] **Open for final validation.** September 10 manual image checks found
  `query_local` defaulting cue rules and speaker aliases to absent `/app/config`
  paths, while the migrated files were correctly preserved under `/state/config`.
  Live read-only inspection confirmed both environment overrides were unset.
- Operational correction: the manual staging overlay explicitly selects the
  existing preserved files. VM108 exact-image checks load 13 cue rules and pass
  authenticated hybrid retrieval. This changes no prompts, source rows or query
  algorithm; production activation and its receipt are tracked separately.
- Final-step acceptance: representative cue-aware and speaker-name queries must
  use the intended rule/alias files after image/container recreation; compare
  rankings/provenance against a correctly configured preservation control and
  make missing/malformed runtime configuration visible in deployment validation.
- Q-05 additional evidence: the disposable manual index appended 8 rows that were
  initially unindexed by FTS. Explicit copy-only maintenance established 1,909/1,909
  coverage. The manual worker now performs this maintenance under the corpus lock;
  the final general lifecycle/monitoring review remains open.

## Final-stage closure checklist

- [ ] Revisit Q-01 through Q-06 plus every new quality finding added during migration.
- [ ] Preserve `processing-v1` and its historical outputs; implement any accepted
  changes under a new explicit version with provenance and reversible selection.
- [ ] Keep migration parity tests for v1; add meaningful regression fixtures and
  a representative evaluation for the new version, including downstream retrieval
  if annotations or prepared content change.
- [ ] Review API preview/download and consumer-output compatibility, filenames,
  dates, speaker attribution, source fidelity, retry behavior and measured cost.
- [ ] Record disposition, implementation version, evidence and review date for
  each issue. Any new paid evaluation needs available approved development budget.
- [ ] Obtain Patrick's final output-quality review; carry no silent deferrals into
  a declaration that the whole migration is complete.

Append future findings with stable Q identifiers, exact source/output evidence,
impact, expected behavior and acceptance criteria. Do not broaden this list with
unverified defects or silently remove a finding after a later successful sample.

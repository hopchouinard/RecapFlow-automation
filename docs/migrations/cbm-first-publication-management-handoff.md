# Request023 — approved first manual publication

Patrick explicitly approved cbm-first-publication-phase-proposal.md with “Yes I
approve.” Execute this single publication after the checks below. No further
approval is pending within the exact scope. Request022 is acknowledged. Refresh
the short-lived App token before the run; its previous expiry is not readiness.

## Immutable inputs delivered on VM109

Code: /srv/community-brain/workspaces/cbm-first-publication-20260917/
Verify packet-manifest.json against the companion packet manifest and every file.
This is an isolated oneshot packet, NOT an overlay for API or weekly workers.

Private run: /srv/community-brain/artifacts/first-publication-20260917/
- approval/plan.json and checkpoint.json (matching existing verified receipt).
- repos/operator.git and consumer.git: prepared local Git objects, not pushes.
- candidate/: exactly three validated v1.2.0 distribution assets.
- journal/: empty at delivery, writable only by selected UID10001/root.

The root is root-owned0700; input directories/files are UID10001-owned0700/0600
so containers can read their explicit mounts. Code contains no credentials and
is readable by UID10001. All inputs mount read-only; only journal is writable.
Production files mount read-only. No live corpus/config mount or provider key.

Plan canonical fingerprint (sorted compact JSON, not formatted file SHA):
a7ac3cf3f0d2ee31c184f956b6c1c2fd61545d8c3d23179ca8506a53ad506759.

Operator main:
base dd29e82aa21f3e52d0ea7a96561f8dec9af28055
approved commit 82167b30b2d72ae8ebb9a64a557991b30be442c3
Only output/2026-09-15/<six approved files> changes.

Consumer main:
base a192f7832e70d60a10de838aa4136b5f3432f15b
approved commit e2eca50575571a23657192163842c02331c85c96
Only the two approved download-corpus.sh pins change; executable mode preserved.

Selected job 744d0f3f-8da7-4c12-bc15-5ec0a046518d; v1.2.0;88 sessions/1,924 rows.
Archive SHA256783466593d3077b227d715c0efe8ac9266db7e28a745251d24c0dd2148d0b109.
Plan binds all six artifact hashes, three asset hashes, identity and checkpoint.
No other dates/files, Forge source changes, repositories or branches are approved.

## Evidence completed by Forge

Exact candidate and both prepared Git commits validated in the pinned production
image on VM108, UID10001, network disabled and no credentials. Parent commit,
changed paths, file types, content hashes and archive identity passed.
Full verification passed150 workflow,975 application Python,68 DB/queue,
6 frontend-unit and5 browser tests plus TypeScript/Vite build. Later focused
15 tests passed after strengthening existing-tag verification (overlap, including
one additional adapter test). These are isolated tests, not production results.

Real disposable PostgreSQL/JetStream tests execute both selected publication
stages through Worker using local Git and a mocked release: no additional model
rows, sources or artifacts; lost release response leaves distribution unknown
and consumer main at its previous installer. Local Git tests verify no force
push, exact path/parent/content pins, drift rejection and write-guard fencing.

The actual consumer candidate passed installation/88-session read-only API tests
on its pinned image with mocked embeddings and read-only tokenizer cache. This
is package/route compatibility, not semantic-ranking or full user-UI acceptance.

## Management execution contract

1. Verify every packet/input hash, Git object parent/tree/file scope, repository
   bases/protection and absent v1.2.0 tag/release/draft. Verify no active/eligible
   work, unknown outcome, outstanding checkpoint or attention marker. Confirm
   selected files and current corpus still match the reviewed checkpoint. On
   drift, report it rather than rebase/rebuild/overwrite the approved candidate.
2. Hold Mac scheduler mutex and ordered VM runner/manual-worker/submission/corpus
   writer locks across pre-capture, all six commands and post-capture. Host launcher
   intentionally does not reacquire these locks: management owns them. Preserve
   the current automatic-processing configuration and restore any temporary
   maintenance controls after verified completion. Capture before-state privately.
3. Mint a fresh App installation token from Infisical's publisher authority using
   exact repo IDs1176379254/1249770482, contents:write/metadata:read. Reverify scope
   and expiry; atomically refresh publication.env only. Keep its stored publication
   flag false. The host passes true only to the approved oneshot and sets model
   calls false. Signing/bootstrap material must remain management-only.
4. Verify actual launcher args using publisher_host.command with captured private
   env dicts in memory, without printing values. API.env contributes only DB URL;
   worker.env contributes only NATS URL/user/password; publication.env contributes
   only token/expiry/App/installation/repo IDs. Nothing is added to running services.
   Same pinned image as r020. Recheck mount permissions, CA trust and modules with
   a credential-free container before running any command that enqueues work.
5. Execute, sequentially, using the new packet's publisher_host.py:

   preflight git
   enqueue git
   execute git
   preflight distribution
   enqueue distribution
   execute distribution

   Example invocation: python3 /srv/community-brain/workspaces/cbm-first-publication-20260917/publisher_host.py preflight git

   STOP on any nonzero command. Do not execute a later command or rerun a started
   execution. Inspect launcher.log, journal, durable DB states and remote receipts.
   Enqueue uses a fixed idempotency key and writes a selection; execute requires
   that selection and creates an exclusive started marker. Never delete markers,
   clear unknown outcomes or force an additional generation to make progress.
6. Git stage pushes only prepared recap commit to operator main, without force.
   Distribution pushes the prepared consumer commit as lightweight tag v1.2.0,
   publishes/verifies the three release assets, then fast-forwards consumer main.
   Thus main keeps the old usable installer until the new package is live. Tag
   creation makes the exact new installer commit available to the release first.
   Release confirmation checks the actual tag commit, because GitHub ignores
   target_commitish when a tag already exists (official documentation below).
7. Every external write checks the live stage claim and token validity. A failed
   Git write or lost HTTP response stops with an uncertain outcome. This is not a
   distributed transaction: a recap commit/tag/release may exist before another
   step fails. Preserve previous installer/release and reconcile rather than roll
   back public history or repeat effects. Report partial completion precisely.
8. Verify both remote main SHAs, the tag commit, all six Git file hashes, release
   assets and consumer installer pins via actual published endpoints. Perform a
   fresh isolated download/install with actual URLs/checksum and pinned consumer
   image, read-only corpus and tokenizer cache if needed. No generative calls;
   fixture embeddings are sufficient for route checks but not ranking claims.
   Check public availability anonymously as appropriate to the existing public
   distribution contract. No further files, image bump or workflow edit is included.
9. Verify job git complete/distribution released and receipts match remote effects.
   Sources/artifacts/model rows and corpus remain unchanged; publication stages,
   attempts, operations/outbox and journal are the expected DB changes. Capture
   paired post-publication recovery/config/export/receipt state with verified
   off-host recovery evidence, preserving the old checkpoint as history. Confirm
   normal runner healthy/idle and API/weekly workers still publication-disabled.
   Allow the selected token to expire or revoke it through the managed contract;
   no background publisher or unattended renewal is authorized by this run.

Return hashed safe receipt with before/after control and data fingerprints,
exact remote commits/tag/release IDs/asset hashes, durable stage receipts,
public-install results, recovery-copy evidence, token disposition and remaining
limitations. Never return secret values, transcript text, environment dumps or
private signing material. Request016 remains stopped; retirement, historical
replacement, CBM-09 and final CBM-10 remain separate gates.

GitHub release reference:
https://docs.github.com/en/rest/releases/releases

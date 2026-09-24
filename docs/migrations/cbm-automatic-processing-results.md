# Automatic new-meeting implementation — deployed and independently verified

Patrick approved the full loop: a new saved meeting automatically acquires its
selected transcript when needed, generates Markdown, and indexes for search.
The full loop is enabled in production. Forge independently verified activation
at20:38UTC: automatic policy true, current HTTPS assets, installed cron, reconciled
boot and idle runner. The shared management status was stale; Forge has delivered
its acceptance directly. Final management receipt publication remains administrative
closure for request CBM-AUTOMATIC-20260910-011, not a pending Forge approval.

## Verified implementation

- API assigns automatic eligibility transactionally only to new root submissions.
  Existing jobs, idempotent returns and reruns are never opted in. Protected corpus
  dates and already-submitted dates are rejected before creating another job.
- A single cron launcher uses the selected-stage worker, durable launch markers,
  scoped generation/attempt checks and lease fencing. It never sweeps old outbox
  events or retries uncertain model work. Failures persist an attention hold.
- Fathom credentials stay acquisition-only; model credentials stay processing/
  indexing-only. Existing US$2 lifetime cap and per-request allowance/ceilings remain.
- Successful indexing refreshes FTS. Newly generated files join the year/month/date
  catalog. The form describes and starts automatic work only when the API enables
  it, and the browser refreshes run progress without submitting again.
- Completion blocks the next job until a verified paired recovery acknowledgment.
  The API shares a submission lock with the management backup boundary. The
  management checkpoint consumer and monitoring are activation prerequisites.

`scripts/verify-forge.sh` passed:150 workflow tests,907 Python tests,41 private
PostgreSQL/JetStream tests,4 frontend unit/component tests,3 browser scenarios,
and production frontend build/typecheck. Follow-up launcher lint and8 targeted
host/transition tests passed after import/check=False cleanup.

VM108 ran the pinned production image with the reviewed modules/static assets on
an internal-only Docker network and disposable PostgreSQL/JetStream. Fake Fathom,
model and embedding boundaries produced two new meetings through actual LanceDB
indexing:16 searchable rows,16 FTS-indexed,0 unindexed. All new artifact contents
matched their hashes; the first meeting's rows survived the second unchanged.
The old fixture job/outbox was untouched. No external calls or real credentials;
disposable containers/network removed. See cbm-automatic-rehearsal.json.

The immutable packet lives at
`/srv/community-brain/workspaces/cbm-automatic-20260910/` on VM109. All27 packet
file hashes/sizes were independently verified after transfer. See
cbm-automatic-manifest.json and cbm-automatic-management-handoff.md.

## Earlier activation prerequisites (historical)

Management must install/test the automatic paired-checkpoint hook, update the
Infisical-backed API renderer/pins, activate the minute cron, and verify idle
new-submission selection, unchanged existing data/old events, budget and monitoring.
Forge must validate its receipt before reporting the feature live. Then Patrick
can use a genuinely new meeting for acceptance when one exists. All87 historical
meetings are already indexed; neither their reprocessing nor synthetic production
submissions are needed to demonstrate the feature.

Remote publication, existing-session replacement, retirement, CBM09/final CBM10,
and the explicit final-quality backlog remain separate gates. Current corpus,
preserved Markdown and prior recovery points remain intact.

## Management progress and reviewed supplement01

At18:42UTC management reported22 passing lease/journal primitive tests and verified
provider usage$0.392107166/remaining$1.607892834 under the unchanged US$2 cap. The
actual capture/restore/copy/PBS consumer, supervision/acknowledgment, monitoring
and integration tests are still incomplete. No cron, worker or automatic API
flag has been installed; this is not deployment readiness.

Forge delivered immutable supplement01 under request011/supplements/01 (hashes in
cbm-automatic-supplement-01.json). It exempts exact read-only POST /retrieval/query
from the backup write barrier while retaining downstream authentication, and
labels temporary scanners for the same quiet-window/orphan inspection as workers.
Six private PostgreSQL/JetStream automatic tests and four host tests passed after
these changes. Management will build a pinned effective production subset that
excludes rehearsal/ and applies these replacements; the original27-file packet
and request manifest remain unchanged. The canonical source contains the fixes.

## Management progress02 — request remains incomplete

Management ended its second active session at19:02:18UTC. Forty Mac/Linux tests
and a disposable real SSH lease check passed; supplement01 was verified and an
inactive25-file production subset was staged at
`/srv/community-brain/workspaces/cbm-automatic-20260910-effective-s01/`, manifest
SHA256 fe84d7ec0271c7ba979bb783eeaac9b107e4b10b0a1ccc9b023a822c963e9e53.
Dynamic capture/restore/copy/PBS, final acknowledgment, monitoring/boot pause and
end-to-end recovery integration remain unfinished. No activation receipt exists;
Forge has not acknowledged request011. The shared HANDOFF.md now explicitly asks
for continuation of implementation from progress02 on the next active turn.

## Live acceptance —20:38UTC

The automatic policy is true and the minute cron invokes the installed boot guard.
Boot reconciliation reports zero pending queue messages and zero eligible work.
Runner status is idle with no attention/checkpoint hold. Trusted HTTPS serves the
exact new frontend assets. API has no worker/provider credentials.

All nine application-table fingerprints match Forge's preactivation baseline.
All managed-file/config/corpus/archive fingerprints also match, excluding the
explicitly tracked lock files. Three jobs,29 model-call records and three old
unsent indexing events remain unchanged;87 sessions/1901 rows retain complete
FTS coverage, and all481 preserved artifact entries remain visible. No production
test meeting or model call was introduced. See cbm-automatic-live-verification.json.

Forge's verification has been delivered to the shared request and HANDOFF.md now
explicitly removes any approval dependency on Forge. Management must publish its
final receipt to close its own stale status; Forge has not fabricated that receipt
or its hash acknowledgment. First real new-meeting acceptance awaits actual new
inputs; historical reprocessing and remote publication remain excluded.

# Acceptance cases and limits

Every case records request/capture ID, UTC interval, source/image/manifest hashes,
actual observations, scope, operator and a pass/fail/blocked outcome. A missing
result is null or blocked. A synthetic result never fills a protected production
slot. The safe relay sees aggregate counts/digests and private evidence pointers;
raw rows, prompts, uploads, credentials, responses and signing bytes stay private.

## Evidence completed in Request030

- Fresh synthetic PostgreSQL18.6 source and independent restore server, network
  `none`, no published ports: canonical row digests for seven representative
  tables, unknown attempt, sent/pending outbox, relationships and FTS query match.
  An attempted INSERT times out under the actual exported-snapshot SHARE fence.
- File/private-manifest transport and restore: empty required tree, synthetic
  upload/vector bytes, SQLite relationship and integrity, relative contained link,
  numeric ownership/mode/mtime, all controls/locks preserved. Repeated restore into
  an existing target is refused and new writes remain. Corruption, incomplete
  copies, traversal, linked ancestors, hard links, devices, extra members and
  wrong scope/hash are negative cases. No checkpoint acknowledgement or worker.
- Actual pinned WebUI image, newly created account/chat and synthetic signing key:
  old session and login accepted after restoration; chat retained; persisted signup
  disabled; anonymous and signup refused; wrong key refuses the old session.
  Source remains stopped and unchanged; each restored runtime uses network `none`.
- Inherited budget helper tested with synthetic transport: exhausted/nonfinite/
  wrong-policy allowance, allowance timeout, wrong endpoint, request ceiling,
  rechecked allowance and unknown-response journal/reopening refusal. Real calls0.

These fixtures do not reproduce the production job schema or certify production
LanceDB/Chroma counts, real upload relationships, provider behavior or browser UI.
The HTTP session exercise is not a rendered browser test. Actual real signing is
never a development credential.

## Protected offline recovery acceptance, next authorized transfer phase

1. Restore from the verified PBS private copy, not from the source staging bundle.
   All parent/component/blob hashes and exact sets, ownership, modes, empty trees,
   links and signing digest match. Separate preservation originals from any clone.
2. PostgreSQL: pg_restore exits0 into an independently identified fresh server.
   Compare schema, table/sequence observations, jobs/stages/attempts/operations,
   model-call journals, sent/unsent outbox, sources/artifacts and rejected events.
   No new attempt, changed unknown outcome, duplicate publication or provider call.
   Compare canonical records, not pg_dump file equality across independently taken
   dumps. Confirm every durable file reference resolves within the restored roots.
3. Corpus: compare LanceDB schema/version, rows, embedding dimensions and vector
   bytes, session/source provenance and FTS indexed/unindexed counts. Query a fixed
   private acceptance set read-only using the pinned runtime; no re-embedding or
   FTS rebuilding to make the result pass.
4. WebUI: SQLite `integrity_check` and declared plus logical relationships for
   user/auth/chat/messages/files/knowledge/models/prompts/functions; upload file
   resolution/bytes; Chroma collection/embedding totals and fixed query results.
   Refresh the baseline, do not force it to match old counts. Check valid cache
   links resolve within the preserved component. Do not execute retained functions.
5. External signing: exact original bytes/digest verified only in private storage.
   No session/browser claim yet: the offline enclave has no application startup.
6. Controls: before/after source hold and lock hashes/modes/inodes/devices match.
   Recovery control files live only under the enclave. Any failure retains all
   originals/partial targets and leaves production processing held.

## Browser/session acceptance, later staged deployment

Operator: Patrick performs the real-account browser checks; home.servers records
safe receipts. No user password or session cookie enters Forge, source or relay.
Before ingress admission, on the authorized staged replacement:

- Effective startup AND persisted signup setting false; anonymous data APIs refused.
- Existing real session from before migration remains valid with the original key;
  a fresh intended-user login works. Compare identity and retained chat count without
  exposing account identifiers or content in the safe receipt.
- Open selected retained chats/files, retrieve known private provenance, verify
  effective filter endpoint/credential and no obsolete VM101 serving dependency.
- A failed real session requires explicit reconciliation; no silent key rotation,
  forced account creation or data overwrite. Wrong-key rejection is already tested
  synthetically and must never be tested by changing the active production key.

Rendered synthetic browser behavior remains a distinct unperformed case. It can
be run next on a fresh fixture through a bounded loopback-only path with a new
synthetic account; no current fixture needs reactivation to pretend it was tested.

## Capacity proposal

VM108 currently has4,004,576KiB RAM (about3.82GiB) and approximately29.8GiB free
on `/srv/dev-data`. Existing profile maxima: API2GiB/2CPU, worker1,572,864,000bytes/
2CPU, WebUI1.5GiB/1.5CPU. Those three memory limits total about4.96GiB before the
OS, monitors and restore server. Sequential small-fixture success is insufficient
for simultaneous acceptance on this4GiB host.

Proposed bounded capacity phase: approved VM1088GiB sizing (or a separate8GiB
isolated development guest), at least4vCPU and20GiB free after preserving existing
fixtures. No resize/reboot occurred in Request030. Confirm this sizing/window
before mutation. Keep existing service limits initially; restore PostgreSQL512MiB.
Use new synthetic content only and deny external provider/queue/publication egress.

Workload: restore a2.5GiB WebUI-shaped dataset with111 uploads and at least1,555
synthetic vector records while the API handles4 concurrent read/retrieval clients,
WebUI handles2 logged-in readers, and one synthetic worker processes one newly
identified synthetic job. Run30minutes after warmup, including one full restore
and controlled candidate rollback retaining one new chat/file. No production or
previous completed/uncertain meeting is eligible.

Proposed acceptance thresholds, requiring owner agreement: zero OOM/restarts,
zero lost writes,0.1% maximum request failure rate (expected denials excluded),
read API p95<=2s, retrieval p95<=5s with synthetic provider, WebUI p95<=3s, restore
<=10minutes. Sample cgroup current/peak memory, CPU throttling, IO, host memory and
disk each second; maintain at least1GiB host MemAvailable and20% disk free.
Abort at<512MiB available or<10GiB free, any OOM, unexpected external connection,
changed prior fixture or missing journal. Report observed thresholds separately
from approval. The first Request030 WebUI120-check readiness timeout is retained;
its successful1.5CPU retry took about302s across three sequential startups and
verification. Neither result establishes steady-state capacity.

## Real-provider and intake proposal

No scoped paid development identity/spend authorization was bound to Request030.
The production US$5 weekly key must not be reused. Do not fetch it to investigate.
Use new scoped identities under
`/development/community-brain-dev/protected-acceptance/<approved-id>` and a new
synthetic meeting ID; no production identity, meeting replay or desktop-intake
configuration change.

Proposed paid allowance: a dedicated non-management OpenRouter key with the
existing helper's exact US$5 weekly policy and BYOK included; request this policy
explicitly rather than weakening the helper. Separately bound this exercise to
**at most3 model requests and US$0.10 total estimated maximum**, one-at-a-time,
<=512 input and128 output tokens per call, no automatic retry. Before approval,
select one available model and bind its current primary-source price/token limits
and permitted endpoint to prove that ceiling. No model selection or price claim
is made by this packet. Reduce the call count/limits if the verified bound cannot
fit. Owner may instead decline all paid tests; the production slot remains absent.

Cases: valid allowance and one successful synthetic request; provider denial with
no job advance; locally injected response loss after intent recording, leaving
`outcome_unknown` and preventing replay. Actual quota exhaustion/foreign endpoint
and unknown outcome negative cases should use the tested synthetic transport to
avoid unnecessary paid calls. Record allowance before each real request and actual
usage/response privately, plus safe journal hashes. If a provider cannot enforce a
bounded request cost or allowance read fails, abort before the call.

Intake: use a dedicated dev acquisition identity restricted to one synthetic test
meeting; read only that fixture, then verify duplicate idempotency and response-loss
reconciliation. If the provider cannot scope that access, return a new bounded
approval proposal. Never expose the production Fathom key or reconfigure live Mac
intake. No live paid/acquisition call ran in Request030.

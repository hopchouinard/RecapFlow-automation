# Weekly operation transition — deployed; follow-up findings pending

Patrick approved US$5 per week on the dedicated production key, automatically
renewed scoped service tokens rather than permanent tokens, and resolving the
runner stop. One form submission must initiate selected transcript acquisition,
Markdown generation, LanceDB indexing and automatic paired recovery acceptance.

Forge changed only the automatic helper budget guards. Processing and indexing
require exact limit5/resetweekly, finite positive remaining <=5, BYOK accounting
and a non-management key. Existing request ceilings and durable journals persist.
Original manual/development rehearsal packets retain their original policies.

50 targeted tests passed, covering both guards, malformed/exhausted/wrong-policy
metadata, weekly reset without resetting a job request ceiling, automatic host
recovery boundaries and existing indexing journals. git diff --check passed.
Two-file immutable overlay on VM109:
`/srv/community-brain/workspaces/cbm-weekly-20260911/`.
Manifest: cbm-weekly-manifest.json. Management must merge with current effective
helpers and pins, not replace them with this partial packet.

The live runner has a latched attention.json with generic reason
`automatic_execution_requires_review`. Its checked_at is overwritten on each
cron tick and cannot establish onset. No execution.log was present. Explicit
installed effective-s01 scan('next') returned completed=[],next=null,attention=false.
That scanner can fence expired stages: it is not universally read-only. No
eligible work was reported. Root cause is not yet established. No marker was
removed, worker resumed, paid call made, or provider policy changed by Forge.

Approved request CBM-WEEKLY-20260911-015 is posted in shared HANDOFF. It requests
controlled reconciliation, coordinated budget rollout, seven-day service tokens
renewed at least48h before expiry, verified consumer overlap/revocation, recovery
pin updates and tests. Infisical management authority stays on the Mac.
Request was unclaimed at the latest inspection; a home.servers turn is needed.
Do not declare Tuesday ready until its live completion evidence is verified.
The first fresh production job remains final end-to-end automatic acceptance.
Publication, historical replacement, retirement and broader migration gates persist.

## Request015 completion and independent verification

Management completed015 at2026-09-11T20:21:00Z. Forge verified all nine evidence
files and independently checked actual OpenRouter limit5/resetweekly, remaining
4.607892834 and unchanged lifetime usage0.392107166. Automatic processing is enabled,
runner idle with no stop markers; catalog87/481 preserved. Receipt reports1901 FTS
rows and unchanged DB/managed files. No jobs/model calls were initiated.

All five scoped service tokens were rotated with old-token rejection and live
consumer checks. Seven-day lifetimes retained, expiry2026-09-18T20:10:30Z and
renewal due2026-09-15T20:10:30Z (72h lead, exceeding requested48h). Existing scheduler
performed not_due check. Future automatic rotation is fixture-tested; the actual
future due event has not occurred. Runner transient root cause remains unknown;
reconciliation and three scheduled idle ticks passed, first-failure timestamp and
exception-class preservation installed. No claim of a new production full-loop job.

Request016 closes two explicit findings: legacy Mac intake-ownership scheduled
check failure (old writers still stopped), and stale indexing journal budget label.
Forge corrected the label locally and51 targeted tests pass; one-file overlay is
in request016 documents. Management follow-up remains pending. No user permission
needed beyond waking home.servers if idle. Safe receipts: receipts/cbm-weekly-20260911-015.
Independent probe: cbm-weekly-live-verification.json.

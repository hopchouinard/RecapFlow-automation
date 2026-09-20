# CBM-MANUAL-OWNERSHIP-20260910-007: completed

Mac management completed the approved maintenance prerequisites and conditional
manual ownership transition on 2026-09-10. No new job, upload, provider call,
index dispatch, publication, corpus replacement or retirement occurred.

## Ownership and independent rollback

At 06:55:45.048581 UTC, the atomic VM101 terminal record committed manual
ownership with `guard_active=true`, `mac_resume_allowed=false` and the accepted
request006 recovery receipt SHA256
`3172c4c082c7cce4f5bba5952ec4549bb91a40f806e861c3b8f6d125ede2bd67`.
Mac terminal refusal was persisted and verified before the deadline timer and
service were disabled and masked at 06:56:50 UTC. Both remain inactive/masked.
The previous deadline is superseded under request007, not extended. The historical
deadline field remains in the immutable terminal evidence; it is no longer armed.

The exact controller and Mac policy passed 18 tests before terminal commitment.
A subsequent small lock correction makes a pre-terminal deadline wait for transient
status-lock contention instead of losing its invocation. The resulting 19 tests
passed, including a real-process contention test. The final controller SHA256 is
`0815f77faa1abb19b763f7d8947f4c74c34695d5ef9fa18e997506cdbdb9bf1f`.
The terminal record retains its original commit-time code hash and test count;
controller-install.json records the later revision separately. Live status,
rollback and forced rollback all returned terminal refusal without changing state
at 07:04:42 UTC. Masked-unit starts were separately denied. Crash-before/after
commit, missing/corrupt state, stale/unreachable Mac peer, failed prerequisites,
late transition and legacy pre-terminal semantics are covered by isolated tests.

Legacy n8n is stopped; old retrieval is paused; both restart policies remain no.
All 2,867 original protected inodes remain immutable. Old lint and publication
cron entries remain held. The Mac exact Zoom folder action is disabled and the
old sync LaunchAgent unloaded. Other folder associations and global Folder Actions
were not changed. New manual collection remains explicitly selected.

## Maintenance readiness

The existing Mac LaunchAgent retains hourly execution and adds 20:45 local
America/Toronto execution. A bounded first task verifies a successful complete DB
dump no older than two hours, copies it and verifies its unchanged checksum before
20:55, ahead of unchanged 21:00 PBS scheduling. Existing retention is preserved.
The live transport rehearsal succeeded without advancing scheduled freshness.
Twelve policy cases and four isolated failure scenarios passed. The first actual
evening calendar run remains to be observed. Mac sleep/session/network remain
dependencies and are exposed through stale/overdue monitoring, not concealed.

Existing Prometheus node-exporter now exposes eight management/expiry series.
The rules file retains existing rules and adds stale management, overdue/failed
copy, 72-hour expiry warning and 24-hour expiry critical alerts. Promtool passed;
all four new rules were healthy/inactive. No exporter restart was necessary.
The existing maintenance runner passed all six tasks with its configured Infisical
bootstrap environment. No autonomous identity renewal or provider-key rotation
was added.

Actual active identity expiries remain September 17 UTC: Open WebUI 03:52:50;
collector and operator 05:03:42; read and metrics probes 06:22:56. All secrets remain
authoritative in Infisical. No Infisical login was delivered to VM109 or Forge.
Mac management owns explicit renewal and the post-job paired recovery procedure
in POST-MANUAL-JOB.md. Each newly accepted manual state requires a fresh scoped
pairing receipt; routine nightly snapshots alone do not establish that pair.

## Application, recovery and evidence

Fifteen live TLS/auth checks passed: health, valid retrieval/read/metrics access,
missing/invalid denial and collector/operator scope denials. Only API and Alloy
containers are running. API remains healthy with 13 cue rules, writable files,
read-only corpus/config, no provider/queue keys and processing/publication flags
disabled. Existing real Open WebUI function checks returned ten sources using the
new retrieval URL. Kuma health/retrieval monitors and both Prometheus targets are up.

The existing 1,901-row/87-session corpus and all 13 corpus/config file hashes are
unchanged. DB preflight retains three jobs, 29 model calls and three unsent index
events, with exact fingerprints matching request006. No canonical replacement or
outbox dispatch occurred. Request006's verified dump, paired archives and PBS
snapshot `pbs:backup/vm/109/2026-09-10T06:28:34Z` were retained and rechecked;
no redundant restore was performed and no full guest restore/PITR is claimed.

Private original VM101 controls remain under
`/var/lib/community-brain-window/CBM-RETRIEVAL-20260910-001/ownership-007-before/`.
Mac originals remain under
`~/.local/state/community-brain-management/ownership-007-before/`.
Three root0600 off-host recovery archives are verified under platform-db
`/var/backups/community-brain/ownership-007/`; exact paths, sizes and hashes are
in control-recovery-copies.json. The final supplement preserves the current lock
revision and maintenance helpers; initial archives are retained unchanged.

Deliberate legacy recovery requires a new explicit decision and reviewed procedure:
stop and reconcile new manual writers first, preserve current data, inspect the
private original controls/paired checkpoints, then coordinate server and exact Mac
intake restoration. Never unmask units, clear terminal state or invoke the saved
legacy controller merely to test recovery. The accepted request006 recovery and
supersession proposal remain the governing detailed recovery evidence.

Publication, canonical corpus replacement, ordinary continuous workers, legacy
service/data retirement and subsequent phases remain gated. Artifact-preview and
semantic-quality acceptance remain separate Forge/user work. No question or new
approval is needed to consume this receipt.

Companion hashes are listed in receipt-manifest.json. Historical preflight and
installation receipts describe their capture times; final-checks.json and the
final revision entry describe the resulting deployed state.

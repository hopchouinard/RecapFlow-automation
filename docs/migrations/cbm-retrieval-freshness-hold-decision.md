# Retrieval freshness: bounded extended writer hold decision

Status: **approved by Patrick on September 10, 2026**. Approval explicitly covers
the extended legacy-writer hold through September 11 at 01:30 UTC, with rollback
before prior writers resume if the new ownership plan is not ready. It does not
approve extending that deadline or activating new processing.

Execute through [the final management handoff](cbm-retrieval-final-window-handoff.md).
Forge has reverified target integrity and health; the actual source freeze and
endpoint change require Mac management's existing access. They have not occurred
merely because this approval was recorded.

## Evidence established

Verified all 14 receipt-file hashes in the management receipt manifest. At
2026-09-10 03:57:11 UTC, all 2,627 allowlisted source files matched preservation.
Rechecked VM109's installed candidate and configuration: all package/config hashes
still match. The known target differences remain 13 approved divider exclusions
and freshly built FTS coverage. No new source policy is needed on that evidence.

The live Open WebUI filter differs from the Forge repository version. Its preserved
live source must stay unchanged; use only its actual URL/key valve mechanism. The
management probe exercised the live container's Requests client with verified lab
trust. Existing Forge filter tests apply to repository code, not proof of that
live source's complete behavior. A real live-filter check remains necessary.

The source inspection preceded daily 04:00 UTC lint. Its current parity cannot be
assumed after that schedule. Repeat writer inspection and hashes after drain.

## Approved hold

Mac management owns one explicit no-write window from cutover preparation until
**September 11, 2026 at 01:30 UTC at the latest**. This leaves time before existing
probe credentials expire at 02:05:38 UTC. Record the start time, exact previous
states and deadline before changing anything.

During that hold:

- No legacy manual/scheduled processing, ingestion, lint, canonicalization,
  artifact Git pull/push, repo edits or Zoom-to-old-host sync may write the corpus
  or its inputs. Patrick and management must respect the operator no-write hold.
- Drain and stop only legacy n8n; preserve/remove only the documented lint and
  artifact/snapshot cron entries. Identify and pause only the applicable Zoom
  Folder Action, drain its sync, and preserve its actual association state. The
  unloaded Zoom LaunchAgent must remain unloaded on restoration.
- Preserve the old retrieval service for rollback. Management must implement a
  verified write barrier for its ingestion/manual writer paths. A bounded pause
  of the drained old retrieval container during the actual endpoint switch is
  acceptable only with immediate rollback/unpause on failure. Never freeze an
  in-flight writer merely to make a hash inventory appear stable.
- Capture final source hashes after all writers drain. If they changed, stop
  before switching and deliver the data-only differences to Forge for candidate
  verification. Do not silently exclude new failures or rewrite source indexes.
- With source/target parity established, perform the approved exact valve-only
  switch, live-filter retrieval check and Patrick's real user acceptance. Preserve
  the rollback URL/key and all other valves. New processing/indexing stays disabled.

## Deadline and failure behavior

Management must prepare and validate a deadline rollback/recovery procedure before
starting the hold; do not rely on a chat session staying alive. Unless a separately
approved processing/refresh ownership plan is verified before the deadline, restore
the old retrieval URL/key **before** restoring old writers and intake to their exact
prior states. Check the old retrieval path succeeds before reopening intake. If
rollback verification fails, keep writes held, alert Patrick, and resolve the
failure; never resume divergent writers behind the new endpoint.

Do not extend the hold silently. A successful retrieval-only switch during this
window does not authorize the production processing/indexing phase. No remote
publication, retirement, credential revocation or model generation is included.
The held legacy schedules are restored only as previously configured; no disabled
workflow or unloaded LaunchAgent is newly activated.

If the hold cannot be safely established, leave Open WebUI on its existing endpoint
and complete a tested corpus-refresh or processing-ownership plan before attempting
a lasting retrieval switch. An immediate switch followed by uncoordinated old-host
writes is not an acceptable freshness policy.

## Trust and lifecycle controls

Before any future WebUI recreation, persist the combined CA bundle setting for the
actual live Requests client and verify on the replacement container. The current
in-place certifi modification survives restart but not recreation. Preserve the
live filter; do not upload Forge's different source to address trust.

Dedicated retrieval identity expires September 17 at 03:52:50 UTC; existing probes
expire September 11 at 02:05:38 UTC. Neither this decision nor the writer hold
renews credentials. CBM-10's quality backlog remains the last migration step.

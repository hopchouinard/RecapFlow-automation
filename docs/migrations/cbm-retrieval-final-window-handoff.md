# Execute approved retrieval window and conditional valve-only switch

Patrick approved both the retrieval-only cutover phase and the extended freshness
hold. **No further routine approval is needed.** Mac management executes the steps
below with its existing VM101/Mac/Traefik/Infisical access. Forge cannot apply the
legacy writer controls or edit the live WebUI configuration through its read-only
broker. No management credentials need transferring.

Hard deadline: **September 11, 2026, 01:30 UTC**. Existing probes expire 35 minutes
later, at 02:05:38 UTC. Do not begin this procedure after the deadline or extend it.
The approved duration is an upper bound, not a requirement to wait until then.

## 1. Prepare recovery before holding anything

Preserve the exact current URL/key and all other valves of the actual live
`community_brain_filter`, plus the earlier rollback state at VM101
`/var/backups/community-brain-retrieval-preflight/20260910T034646Z/`. Capture any
newer relevant settings without overwriting the earlier evidence. Preserve live
filter source hash `12215e67d72775e3d56baa98fc23093196cc8917d887a18a506f188f26a0dc16`;
do not upload the different Forge source. Record an idempotent valve-only rollback
that preserves newer chats/settings and verifies its loaded effect.

Before starting the hold, arm and verify a durable deadline rollback using the
management environment's existing execution facilities, surviving loss of the
interactive session. Persist exact hold state, original scheduling/intake settings,
rollback configuration and deadline privately. Demonstrate the deadline handler's
ordering without mutating the active endpoint during its test:

1. Restore the old retrieval service's ability to serve reads, under a continuing
   no-write guard; no corpus writer or intake resumes yet.
2. Restore old URL/key through the existing valve mechanism, preserving other
   settings; invalidate/reload only the applicable filter configuration if needed.
3. Verify the actual loaded filter retrieves through the old endpoint successfully.
4. Only then restore held writer/intake settings to their exact prior states.

If rollback fails, retain the write hold and alert Patrick. Do not reopen writes
behind an unverified endpoint. Mac intake must remain paused if it cannot obtain
confirmation of successful server rollback. Do not rely solely on a Mac user
session or on Forge returning in chat. If safe deadline execution cannot be
established, stop before holding writers and report the specific limitation.

Cancel that deadline only after a separately approved and verified processing or
refresh ownership plan supersedes it, with a recorded receipt. Cutover success
alone is not permission to cancel the rollback or retain an indefinite hold.

## 2. Establish and prove the write barrier

Use the exact paths/states in
`cbm-retrieval-management-receipts-20260910/README.md`:

- Remove the saved lint entry from cron.d entirely and preserve its original mode.
  Today's 04:00 lint may already have run: inspect it, and drain any active work.
- Preserve/remove only the weekly artifact pull/push and snapshot cron entries.
  Do not execute them to test the pause and do not alter unrelated cron entries.
- Prevent new legacy submissions, drain executions, then stop only n8n.
- Identify the exact Zoom folder/action association, preserve/disable only that
  association and drain sync. Do not globally disable Folder Actions. Leave the
  already-unloaded Zoom LaunchAgent unloaded.
- Establish a verified barrier against old retrieval `/ingest`, container CLI
  ingestion/lint and manual host writers; document the mechanism and its restore.
  Do not equate absence of processes with a write barrier. Management and Patrick
  own a no-manual-write rule throughout the window.
- Prefer preserving old read service behind an effective mutation barrier. If
  achieving the barrier requires pausing the drained old retrieval container,
  minimize that interruption to the immediate switch and unpause on abort. Do not
  leave old WebUI pointing to a paused backend while awaiting a later chat reply.

Record drained execution/process state and exact controls. If any writer cannot
be controlled, do not switch. No new ingestion, generation or publication is allowed.

## 3. Final data check while the barrier is active

Repeat the complete 2,627-file comparison with pinned source manifest
`4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7`.
Capture a timestamped final source checkpoint and verify a before/after hash pass.
The 03:57 comparison is not sufficient after today's lint schedule.

Forge rechecked VM109 on September 10 at approximately 04:14 UTC: installed
candidate/config hashes match; immutable image and read-only mounts match; HTTPS
health is successful. Recheck those target hashes, full FTS coverage and health at
execution time. Expected target: 1,901 success rows, 87 sessions, schema 1.1,
768 dimensions, FTS 1,901 indexed/0 unindexed. Target package archive SHA-256:
`5e4f37d6459d820f506fe0b5d6d4db42204dcab26a3bb89592dd8f81fb9707fb`.
Only the known 13-divider exclusions and rebuilt FTS distinguish the target.

If the source is unchanged and target passes, proceed without another approval.
If source/config/row differences are detected, **do not switch**: restore any
interrupted old read service and safely release this attempted window back to its
saved old states, recording that outcome. Deliver data-only differences and their
manifest to Forge. Do not silently apply new exclusions, re-embed or overwrite
source/target to force parity. A changed candidate needs review before a new window.

Retain the final source checkpoint plus VM109's paired recovery manifest/PBS
checkpoint `pbs:backup/vm/109/2026-09-10T03:32:39Z`. New backup work must not trigger
scheduled publication or ingestion.

## 4. Switch the exact two valves and verify the live integration

Immediately before switching, restage the dedicated Open WebUI retrieval token
privately from Infisical. Confirm subject/scope/permission and September 17
03:52:50 UTC expiry against the server hash record. Never print or place the token
in process arguments, Forge source or public receipts. Remove temporary copies
after successful client delivery.

Change only:

- `retrieval_url`: from `http://10.1.30.10:8999/query` to
  **`https://community-brain.patchoutech.lab/retrieval/query`**.
- `api_key`: to the dedicated `community-brain-openwebui` identity.

Preserve the live filter, global assignment, enabled state, models, top_k, timeout,
min_score and all other settings. Verify the live application has loaded the new
valves; a database edit alone does not prove an in-memory filter was refreshed.
Avoid container recreation. If required, carry forward the persistent CA bundle
setting first and verify the actual Requests client's trust after recreation.
Never disable TLS verification. Preserve current chats/settings in rollback.

Run the **actual loaded live filter's retrieval path**, using the new effective
valves, against an already approved fixture query. A standalone Requests POST
alone does not establish that the active filter now uses the target. Record the
effective URL, response status and returned IDs/provenance, plus an emitted-context
success indicator without transcript text. Do not invoke chat generation. Verify
missing/invalid key denial with a separate probe and current monitoring UP.

On any failed acceptance, immediately execute the prepared rollback before
restoring old writers. On success, leave writers held under the armed deadline
and return the receipt promptly so Patrick can verify through his actual WebUI
session. That user acceptance remains pending until he reports it.

## 5. Return public receipt

Include start/deadline, rollback-handler evidence, exact previous and held writer
states, final source and target hashes, backup/checkpoint paths, actual valve
switch time, live filter hash/effective URL, runtime retrieval result IDs, CA
verification, monitoring statuses and whether the deadline remains armed.
Include rollback/resume status if the window aborted. Keep all secrets private.

Confirm no processing/indexing/publication started, synthetic outbox stayed inert,
old services were preserved, and no retirement occurred. Do not resume legacy
writers behind the new endpoint or claim permanent freshness from a point-in-time
comparison. Further processing ownership and final CBM-10 quality work remain gated.

# CBM-RETRIEVAL-20260910-001 — completed conditional retrieval switch

Actor: home.servers / Mac management. UTC date: 2026-09-10.
**The live WebUI filter now retrieves from the new endpoint. Patrick's real user
acceptance is pending. Legacy writers remain held under the independent rollback.**
No new phase is inferred from this result.

## Execution and acceptance

All request document SHA-256 hashes verified; atomic claim acquired at 04:26 UTC.
Mac Zoom intake held at 04:38:31 UTC; VM101 writer hold began 04:38:52 UTC.
Only the actual live filter's `retrieval_url` and `api_key` changed, at
**04:41:18 UTC**, with live application acceptance at **04:41:20 UTC**.
Effective URL: `https://community-brain.patchoutech.lab/retrieval/query`.

Source remains SHA256
`12215e67d72775e3d56baa98fc23093196cc8917d887a18a506f188f26a0dc16`.
Name, metadata, global assignment, enabled state and other valves are unchanged.
No filter upload, WebUI restart/recreation, model selection or chat-generation
request occurred. A temporary, unassigned, administrator-only action invoked the
actual running application's `process_filter_functions` and cached filter object;
it was deleted immediately after each check. This exercised the actual inlet and
emitted source context, not merely a standalone HTTP request or database read.

The live filter uses **httpx**, and its default client passed verified HTTPS with
the previously installed lab CA. Retrieval returned `ok`, with source context and
10 results. IDs and provenance are in `switch-receipt.json`; example:
`2026-02-18:signal:general`, `/data/output/2026-02-18/extracted-signal.md`.
Independent actual-client probes: valid key 200, missing key 401, invalid key 401.
Dedicated Infisical identity matched the live server hash/scope/permission/expiry;
the raw token traveled on stdin only and was stored only in its intended live
valve. No temporary raw token file or secret was put in this relay.

Health, authenticated retrieval and metrics passed; both Kuma monitors and both
Prometheus targets are UP. Two existing jobs, 14 recorded model calls and two unsent
outbox events remain unchanged. VM109 runs only API and Alloy; no worker, indexing,
processing, publication or retirement was activated.

## Freshness and recovery checkpoint

Today's 04:00 lint finished by 04:11:17. The post-lint preliminary comparison and
final held comparisons at 04:39:20/04:39:22 UTC match all **2,627** allowed files to
manifest `4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7`.
No added, changed or deleted source/config files or source rows. Known target
transformations remain the 13 approved divider exclusions and rebuilt FTS.
No fresh candidate derivation or data-only drift delivery was needed.

Final checkpoint on VM101, root-private:
`/var/lib/community-brain-window/CBM-RETRIEVAL-20260910-001/source-checkpoint.tar`
(112,691,200 bytes), SHA256
`a043726758eb1e8783bdb7406ee0d38914104d8aeefcb51d2a7036635568beba`.
Its adjacent `source-checkpoint-manifest.json` records every file; all 2,627 archive
member hashes were checked against the final manifest. Source bytes were checked
again immediately before the switch.

Installed VM109 candidate and all 13 configuration files passed exact hashes;
archive SHA256 remains
`5e4f37d6459d820f506fe0b5d6d4db42204dcab26a3bb89592dd8f81fb9707fb`.
Read-only table checks: 1,901 success rows, 87 sessions, schema 1.1, 768 dimensions,
FTS **1,901 indexed / 0 unindexed**. Frozen image, read-only mounts and disabled
model/publication flags passed. Existing paired recovery manifest/PBS checkpoint
`pbs:backup/vm/109/2026-09-10T03:32:39Z` are retained unchanged.

## Held writers and exact restoration

- The exact `Zoom` Folder Action at `/Volumes/NVMe_2TB_Work/Documents/Zoom` was
  enabled and is now disabled. Its `Sync Zoom Chat` and `Sync Zoom Chats` script
  enabled settings are preserved. No sync process was active. Other Folder Actions
  remain untouched; the previously unloaded Zoom LaunchAgent remains unloaded.
- Lint cron moved out of `/etc/cron.d` into private state, with original mode saved.
  Only user cron lines for daily 06:00 snapshot and Wednesday 06:30 artifact
  commit/pull/push were removed; unrelated lines/comments remain unchanged.
- n8n executions drained, then only `n8n` stopped. Both n8n and old retrieval
  restart policies changed from `unless-stopped` to `no` for the hold, preventing
  reboot from reopening their writers automatically.
- Persistent filesystem immutable flags guard **2,867 inodes** across corpus,
  config, raw transcripts, output, historical, watch and n8n-state. Original flags
  and inode identities are saved. Host write-open denial was verified. This blocks
  ordinary host/container writes; Patrick and management must not deliberately
  remove those guards or perform privileged manual edits during the window.
- Old retrieval is preserved **paused**, so `/ingest` and container CLI cannot run;
  a Docker CLI attempt was rejected as paused. It was paused immediately before
  the switch, which accepted in roughly 1.5 seconds. A separate recovery-read test
  briefly unpaused it under the immutable guard, returned HTTP 200 from the old
  endpoint, and re-paused it without changing active valves.

## Independent deadline and rollback

Hard deadline remains **2026-09-11 01:30 UTC**. To allow recovery to finish before
that deadline, the armed VM101 timer starts rollback at **01:25 UTC** with a
300-second service timeout. It is persistent, enabled, and also checks on boot.
It does not depend on either conversation, a Mac GUI session or a Forge reply.
No deadline cancellation or extension was performed.

Units: `cbm-retrieval-deadline.timer` / `cbm-retrieval-deadline.service`.
Controller: `/usr/local/lib/community-brain-window/window-control.py`.
Private state/rollback: `/var/lib/community-brain-window/CBM-RETRIEVAL-20260910-001/`.
It includes current online WebUI DB backup, exact function/valves, original cron,
inode flags and prior container policies. Earlier preflight rollback is untouched.

The controller verifies the immutable guard, restores old read service under that
guard, restores only the saved URL/key through the WebUI valve API, verifies the
actual loaded filter's old-endpoint retrieval/context, **then** restores original
filesystem flags, cron and prior container states. It preserves newer chats and
unrelated settings. Ordering and four injected pre-resume failure cases passed;
old read service under the actual guard also passed. Systemd unit validation and
an actual pre-deadline service invocation passed without changing the endpoint.

On rollback failure, state records failure and Mac intake cannot resume without
verified server success. A critical system log is emitted; the existing hourly
Mac management job checks server state and issues a Mac notification if deadline
recovery remains unconfirmed. It resumes only the saved Zoom association after
confirmed server rollback. No new relay daemon, account or credential was created.
Loss of Mac availability can delay intake restoration safely; it cannot reopen
intake ahead of server confirmation. The hook is
`~/.local/lib/community-brain-management/mac-intake.py`, with private state under
`~/.local/state/community-brain-window/`. The existing maintenance script backup is
`~/.local/lib/community-brain-management/maintain.before-retrieval-window.py`.

Manual early recovery, if needed, is the fixed VM101 command:
`sudo python3 /usr/local/lib/community-brain-window/window-control.py rollback --now`.
Verify `phase=restored`, `rollback_verified=true`, `mac_resume_allowed=true`, then
run the Mac intake `poll` hook. Never resume writers independently of verified
old-filter recovery. Never remove the claim or rerun the completed switch.

## Remaining gates

Patrick's actual WebUI acceptance is pending. Further processing/refresh ownership,
indexing, publication, retirement and CBM-10 quality work remain gated. A successful
retrieval switch does not cancel the rollback. Any superseding ownership plan must
be separately approved, verified and receipted before cancelling it.

Existing probes still expire **September 11 02:05:38 UTC**. Dedicated WebUI identity
still expires **September 17 03:52:50 UTC**; neither was renewed. WebUI recreation
must carry the persistent CA bundle configuration; no recreation occurred here.
Safe supporting receipt hashes are listed in `receipt-manifest.json`.

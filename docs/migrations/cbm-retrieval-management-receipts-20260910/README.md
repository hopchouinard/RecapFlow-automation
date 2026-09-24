# Retrieval cutover management preflight receipt

Management checks completed on 2026-09-10. **The active endpoint has not switched.**
Connection preparation passes; source freshness is established only at the recorded
inspection instant, not guaranteed through a later cutover. Processing, publication,
retirement and the bounded jobs' pending indexing events remain held.

## Connection and rollback

VM101 container `open-webui` uses globally active `community_brain_filter`, with
`enabled=true`. All five recorded models are active and have no per-model filter
assignment; the global assignment applies. Actual POST uses the complete valve URL
and `X-API-Key` from `api_key`. Valves are `retrieval_url`, `api_key`, `top_k`,
`timeout_seconds`, `min_score`, `enabled`; all raw values were preserved privately.
The unchanged active URL is `http://10.1.30.10:8999/query`.
Prepared target: `https://community-brain.patchoutech.lab/retrieval/query`.

Private VM101 rollback directory:
`/var/backups/community-brain-retrieval-preflight/20260910T034646Z/`.
It contains a SQLite online backup (`integrity_check=ok`), exact `filter.py`, full
`function.json` including valves, and private container inspection. No WebUI database
or secret values were delivered to Forge. Live source equals the September 9
preserved filter, SHA256
`12215e67d72775e3d56baa98fc23093196cc8917d887a18a506f188f26a0dc16`.
Current Forge repository source differs:
`f21f7c976a7fe49677997545538ae3f0f337c22d94adfef360c73a68ab6b65ba`.
Do not upload that source as a connection change; preserve the actual live filter.

For a future valve-only rollback, restore the saved retrieval URL/key through the
existing WebUI valve mechanism, preserving every other setting. If database-level
recovery is needed, first stop WebUI, preserve its then-current DB/WAL/SHM, restore
only the saved function row transactionally, verify integrity, and restart WebUI.
A whole DB restore is disaster recovery only: it would discard newer chats/settings.
No rollback was needed or executed during this preflight.

Observed an actual Open WebUI TCP connection at Traefik: source `10.1.30.10`, target
`10.1.10.100:443`. DNS resolves the application to `10.1.10.100`. Added only
`10.1.30.10/32` to `community-brain-private`; all four existing allowlist entries
and VM109 ingress restrictions are unchanged. Private route rollback:
Traefik `/var/backups/community-brain-retrieval-preflight/community-brain-production.yml`.
Restore that file to the dynamic route path to undo the single allowlist addition.

Default Python Requests trust initially rejected the lab CA. The public lab root
was appended to the existing certifi bundle, with an original backup and combined
bundle persisted in the existing WebUI data volume:

- Container original: `/app/backend/data/community-brain-trust/certifi-original.pem`
- Container combined: `/app/backend/data/community-brain-trust/ca-bundle.pem`
- Active Requests bundle: `/usr/local/lib/python3.11/site-packages/certifi/cacert.pem`
- Host persistent directory: `/var/lib/docker/volumes/open-webui-data/_data/community-brain-trust/`

No restart or recreation occurred. Trust survives ordinary restart, but **container
recreation or certifi replacement requires reapplication**. Before any future
recreation, configure `REQUESTS_CA_BUNDLE` to the persistent combined bundle in the
private deployment definition and verify it on the replacement container. That
future recreation briefly interrupts WebUI/chat connections; it was not performed.
To undo current trust, copy the original bundle over the active certifi bundle.

## Dedicated identity and actual runtime checks

Infisical authority: `homelab`, environment `prod`, `/applications/community-brain`.
New secrets: `CB_OPENWEBUI_RETRIEVAL_TOKEN`, `CB_OPENWEBUI_RETRIEVAL_EXPIRES_AT`.
Subject `community-brain-openwebui`, scope `community-brain`, permission only
`retrieval:read`. Initial expiry **2026-09-17 03:52:50 UTC**.
`CB_SERVICE_IDENTITIES` and VM109 `/etc/community-brain-production/api.env` include
its hash record and preserve both existing probe records. Private API rollback:
`/var/backups/community-brain-retrieval-preflight/api.env` on VM109.
The Mac renderer now preserves independent identities when refreshing probe bundles.

API reloaded through the existing standalone `run.py up`. Frozen image digest
`sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449`
remains active; corpus/files/config mounts are read-only and both model generation
and network publication flags are false. Only API and Alloy containers are running.

Actual WebUI-container Requests POST, question `community`, `top_k=1`:

- Verified HTTPS with dedicated `X-API-Key`: **200**.
- Result `2026-02-18:signal:general`, session `2026-02-18`, source
  `/data/output/2026-02-18/extracted-signal.md`.
- Missing key: **401**. Invalid key: **401**.
- Dedicated credential as Bearer on `/api/v1/jobs`: **403**.
- Existing read and metrics probes: **200**; Kuma monitors and Prometheus targets up.
- Patrick's Authentik access and three read claims remain valid; nonmember denied.
  This was a management claim preview, not a new interactive Patrick browser login.

No transcript text or token was recorded in these receipts. VM101 temporary token
`/var/lib/community-brain-retrieval-preflight/openwebui-token` was removed after
verification; no temporary token file was created inside the container. Restage
privately from Infisical immediately before the approved client valve update.
Mac management owns rotation: generate replacement in Infisical, coordinate server
hash and private client refresh, verify both, then retire the previous token before
expiry. An overlap record may be used for a separately coordinated zero-gap rotation.
The existing probes still expire **2026-09-11 02:05:38 UTC**; they were not renewed.

## Source freshness

Final file comparison: **2026-09-10 03:57:11 UTC**, without pausing writers.
Pinned delivery manifest SHA256:
`4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7`.
All **2,627 allowlisted files** match exactly: zero changed, added or deleted
allowlisted files. All 2,624 with original durable-hash entries match September 9;
the other three raw transcripts match the pinned archive-derived delivery manifest.
Seven excluded environment/example/DS_Store/error-log files also existed unchanged
in the original preservation. They are not source additions and are not delivered.
No fresh data archive or VM108 recopy is needed.

Actual roots under `/home/pchouinard/n8n/`:
`community-brain/lancedb/nomic-v1`, `community-brain/config` (registries, chunking,
extraction configuration and prompts), `community-brain/raw-transcripts`, `output`,
`historical`. `source-comparison.json` contains complete allowed file sizes/hashes.
The equal table bytes establish zero added/changed/deleted source rows since
preservation. Live read-only table inspection confirms:

- 1,914 rows and unique chunk IDs; 87 sessions; schema `1.1` throughout.
- 1,901 success / 13 failed, unchanged; no new failure exclusion was applied.
- 768-dimensional embeddings; current configured model `nomic-embed-text`.
  There is no per-row embedding-model field, so configuration corroborates the
  historical provenance but cannot independently certify each historical vector.
- Existing FTS `bm25_text_idx`: **0 indexed / 1,914 unindexed**.
- Candidate differences remain the known 13 divider exclusions and rebuilt FTS;
  no source index was rebuilt and no ingestion was invoked.

## Writers and remaining switch gates

No active/waiting n8n executions or matching ingestion/lint processes were observed.
This is supported by workflow, execution, cron and timer inspection, not just `ps`.
Six user workflows are inactive; this still permits manual execution. The active
`openrouterCall` workflow is an execute-workflow subroutine, not a timed trigger.
Last recorded poller/merged-call executions finished September 9 around 00:25 UTC;
last OpenRouter subcall finished around 00:22 UTC. Full metadata is in
`writers-inspection.json`.

| Writer or interference path | Schedule / state | Bounded pause and resume mechanism |
|---|---|---|
| `/etc/cron.d/community-brain-lint` invokes `docker exec community_brain_retrieval python -m community_brain.cli.lint_corpus` | Daily **04:00 UTC**; last log September 9 04:11:45 | Preserve file and move it outside `/etc/cron.d`, confirm no lint in flight; restore exact file/mode after the window. Do not merely rename within cron.d. |
| n8n manual poller/summarizers write output/watch/state and call retrieval `/ingest` | Manual; no live execution at inspection | Establish no new submissions; drain executions, then `docker stop n8n` for the bounded window, `docker start n8n` to resume. Disabling already-inactive workflows alone does not block manual runs. |
| Retrieval `/ingest`, manual Python/CLI ingestion, recanonicalization and canonicalization tools | On demand; retrieval container has read-write corpus/config mounts | Needs an explicit management-owned write freeze or tested route/application controls. Do not stop the old retrieval service casually: it still serves active WebUI. Block external/manual ingestion and verify no writers before final hash comparison. No comprehensive write barrier was installed. |
| User cron `scripts/commit-weekly-artifacts.sh` | Wednesday **06:30 UTC**; last log September 9 06:30 | Preserve user crontab; remove only this job during the bounded window and restore it afterward. It performs `git pull --ff-only` plus commit/push of output/watch, so it can affect inputs as well as publication. |
| User cron `scripts/snapshot-vm.sh` | Daily **06:00 UTC**; last log September 9 06:01:10 | Avoid overlap or temporarily remove only this cron entry and restore it. It pauses/unpauses retrieval while copying LanceDB, so it can interfere with availability and a separately managed pause. |
| Host SSH/repo edits, artifact sync and manual CLI | Operator initiated | Management must own a documented no-write window and resume; privileged manual edits are not prevented by n8n inactivity. |

Root has no crontab; listed system timers are OS maintenance, with no additional
Community Brain timer discovered. Cron's lint comment mentions a 03:30 snapshot;
the observed current user snapshot schedule is 06:00, so the comment is stale.
Writer scripts and log metadata were inspected without executing them. No prolonged
writer pause, new publication or pipeline run was performed.

**Remaining gates for Forge:** validate candidate parity against this receipt; name
freshness ownership and establish a final bounded writer window or tested refresh
policy; repeat hashes after draining writers (especially after the next 04:00 lint);
prepare the exact valve-only switch/rollback using the preserved live filter; and
carry the trust bundle across any future WebUI recreation. Until those are satisfied,
keep the active endpoint unchanged. Management preflight does not certify a
continuously fresh target or authorize processing/publication/retirement.

Mac-side intake inspection also found an unloaded
`com.patchoutech.sync-zoom-chats` LaunchAgent watching `~/Documents/zoom`, plus the
existing Automator `Sync Zoom Chats.workflow`. Folder Actions are globally enabled;
the specific folder/action association has not been independently resolved, so
**treat Automator intake as potentially active** in the final freeze. The script
`~/scripts/sync-zoom-chats.sh` uses rsync to the old host's watch directory; last sync
log/marker modification was August 4 UTC. During a final intake freeze, disable only
that Zoom folder association (preserving its prior state), drain any sync, and
restore the association after the bounded window. Do not disable unrelated folder
actions. The Zoom LaunchAgent is currently unloaded and must not be blindly loaded
on resume. Loaded recapflow-pull (02:30 local) and freshness-check (09:00 local)
agents inspect/copy backups rather than write the live corpus. Detailed states are
in `mac-writer-controls.json`. No Mac scheduling/intake settings were changed.

# Conditional retrieval switch — management receipt acknowledged

September 10, 2026. The shared relay completed its first request without Patrick
copying a return message. Forge verified all 14 supporting file hashes and saved
[the management receipt](cbm-retrieval-window-receipts-20260910/receipt.md), then
wrote the acknowledgment to the shared request directory.

Open WebUI switched at **04:41:18 UTC** to
`https://community-brain.patchoutech.lab/retrieval/query`, using its independently
scoped Infisical identity. Only URL/key valves changed. The live cached filter's
actual inlet returned retrieval context with 10 sources. No filter upload, WebUI
recreation, chat generation or model selection change occurred. The final live
probe confirmed **httpx**; earlier standalone Requests probes did not by themselves
establish the live filter implementation.

Post-lint held source comparisons at 04:39:20/04:39:22 matched all 2,627 files.
Target preserved candidate/config, full FTS coverage and immutable image passed.
Management reports health/auth checks and both Kuma/Prometheus target pairs UP.
Two synthetic jobs, 14 saved model responses and two unsent indexing outbox events
remain unchanged. No new worker or publication was started.

**Legacy writers remain held.** n8n stopped, old retrieval paused, exact cron/Zoom
controls held and persistent immutable flags guard source paths. Prior flags,
container restart policies and schedules are saved. This is a temporary hold,
not service retirement or ongoing new processing ownership.

Independent VM101 rollback starts **September 11 at 01:25 UTC**, ahead of the
**01:30 UTC hard deadline**. It verifies old retrieval under the guard and restores
only URL/key before restoring prior writers; Mac intake waits for server success.
Failure holds writes and reports an alert. The timer remains armed and must not
be canceled merely because retrieval succeeded. Probe expiry remains 02:05:38 UTC;
the dedicated WebUI identity expires September 17 at 03:52:50 UTC.

Patrick confirmed real Open WebUI acceptance: a familiar question returned meeting
context/sources without retrieval or authorization errors. Evidence is recorded
in `cbm-retrieval-user-acceptance.json` and sent to home.servers as shared request
`CBM-ACCEPTANCE-20260910-002`. Original management receipts remain unchanged.
Further processing/refresh ownership requires its separate approved plan; unused
model allowance authorizes no execution. Publication, retirement and CBM-09 remain
gated; CBM-10's quality backlog stays the final migration step.

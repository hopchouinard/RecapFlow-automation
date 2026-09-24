# September15 real-job recovery checkpoint

Patrick requested urgent repair/processing of the September15 submission. Forge
reconciled failed acquisition using the transcript already attached by the user,
preserving the original failed attempt and all source hashes. The existing runner
completed processing and indexing on the SAME job744d0f3f-8da7-4c12-bc15-5ec0a046518d.
All6 artifacts hash-verified; corpus88 meetings/1924 rows with23 for2026-09-15,
FTS1924 indexed/0 unindexed.13 processing model calls succeeded; no retries/new job
or remote publication. Details in companion output verification JSON.

Runner is awaiting_checkpoint, marker at /srv/community-brain/automation/checkpoint-needed.json.
At inspection there was no artifacts/automatic directory or checkpoint receipt.
Run/reconcile the EXISTING authorized automatic recovery consumer for this exact
job; diagnose why scheduled management has not consumed the marker. Use existing
ordered quiet locks and real DB/files restore checks, verified off-host copy/PBS
and matched checkpoint acknowledgment. Never fabricate receipt or clear marker
before actual verified completion. Respect uncertain-effect journals before retry.
No new model calls, jobs, corpus rewrites, publication, retirement or token reset.

Request016 partial metadata deployment is accepted; its Mac Python/System Events
permission work was stopped by Patrick. This request DOES NOT authorize resuming
that permission task, granting TCC access, bypassing legacy ownership checks or
re-enabling old intake. Keep that limitation separate. If it actually blocks
recovery, report the precise dependency; don't infer a new permission approval.

Private incident evidence: /srv/community-brain/artifacts/cbm-sept15-acquisition-recovery/.
Return safe hashed receipt covering actual checkpoint evidence and runner state.
Production content is already available to Patrick; do not rerun processing.

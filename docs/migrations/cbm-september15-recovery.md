# September15 acquisition recovery

Patrick requested urgent repair of job744d0f3f-8da7-4c12-bc15-5ec0a046518d.
Submitted identity: Fathom821559116,2026-09-15T22:00:00Z,America/Toronto.
Acquisition attempt failed at23:28:12UTC with generic pipeline_failed. A bounded
metadata-only lookup did not locate that recording ID. No transcript API or
additional unrelated recording lookup was performed during diagnosis.

The user-supplied transcript was already attached at23:33:23UTC (73,733 bytes,
SHA256558c713fc4fc89d30c9c42b3355db70c0c58b7a69b9ca232fab85240775bd5dc).
The job had chat,aliases,transcript and queued processing but failed acquisition
still blocked the automatic selector; no model calls existed before recovery.

Under runner/manual/submission exclusive locks and no active worker/checkpoint,
Forge verified the exact job/source identity and storage hash. Acquisition was
reconciled as satisfied by user_supplied_transcript_after_failed_acquisition.
Its failed attempt was preserved; processing generation1/attempt0 was unchanged.
The original attention marker and intent/completion receipts are private on VM109
under /srv/community-brain/artifacts/cbm-sept15-acquisition-recovery/.
Only this resolved marker was removed. Existing minute cron resumed the same job.
No duplicate job, source replacement, acquisition retry or remote publication.

Processing succeeded: all6 artifacts hash-verified;13 processing calls succeeded.
Indexing complete:88 sessions/1924 rows,23 new-session rows,zero unindexed.
Recovery checkpoint verified and acknowledged under request017 on September17. Existing US$5 weekly guard remains. Request016's Mac System Events
permission work was stopped at Patrick's direction; this incident does not resume
that unrelated permission task. Legacy writers remain disabled.


## Request017 closure

Forge verified all nine receipt-file hashes and independently matched the live
checkpoint acknowledgment to the exact paired-manifest SHA256
`df1ce04cd7a15e38cc21e1be5fc3ee1fd931489f7a66a351705a6e248970684e`.
Live job processing=succeeded,artifacts=ready,indexing=complete;88 catalog meetings,
automatic processing enabled,runner idle,no paused/attention/pending markers.
Four supplied parser regression tests passed locally. Repaired management adapter,
patch and tests are preserved byte-for-byte in receipts/cbm-sept15-recovery-017/;
the deployed adapter remains owned by the Mac/PVE management code, not the app image.

The existing September15 PBS backup succeeded but synchronous pvesh log output
caused JSON parsing to fail before its UPID was recorded. Management repaired the
narrow vzdump parser and reconciled actual snapshot/task/restore/offhost evidence,
without replaying processing or backup. Receipt records the incident-specific
acceptance of four changed operational files and independently scheduled pruning
of two older snapshots. General guards remain; no full guest restore/PITR claim.
The next actual invocation of the repaired PBS parser remains unobserved.

Evidence: receipts/cbm-sept15-recovery-017/receipt.md and
cbm-september15-checkpoint-verification.json. The successful meeting required
manual acquisition reconciliation and backup reconciliation; this is not proof
that the next Fathom-ID submission is fully unattended. Request016's separate Mac
permission work remains stopped at Patrick's direction.

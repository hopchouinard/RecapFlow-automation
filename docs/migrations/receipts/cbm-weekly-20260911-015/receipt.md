# CBM-WEEKLY-20260911-015

The existing dedicated OpenRouter key now has a US$5 weekly allowance, resets
weekly, includes BYOK usage, and remains a non-management key. Its lifetime spend
remained US$0.392107166 throughout this deployment. No account credit purchase,
model request, new meeting, publication, historical replacement or retirement
occurred.

## Effective deployment

The new `/srv/community-brain/workspaces/cbm-weekly-20260911-effective` packet
retains every effective-s01 file. Only Forge's two approved budget files and the
management first-failure marker preservation in `automatic_host.py` differ.
Original packets remain intact. The API Compose mounts, native cron boot guard,
Mac renderer pins and recovery inventory now reference the new packet. The
Signal frontend, image and automatic form capability remain enabled and unchanged.

- Effective manifest: `6d897bb3f8913e234f24c581502275d98bdfe070518acc61a8036a556562b260`
- Manual runtime manifest: `eb362aa06e30ff05f49638bc86451b006ad12c4274100333226d2ca48b3fb690`
- Compose: `b0fdb076bc2a614863a172ca1997a941fc5c3009e6e5adaf928ca62389b08a03`

## Renewal and ownership

`integrations/renew-service-tokens.py` is invoked by the existing Mac maintenance
LaunchAgent's hourly work; no second scheduler was added. Tokens retain their
separate subjects, scopes and seven-day lifetimes. Renewal becomes due 72 hours
before expiry. A nonsecret local status file records progress; the resumable
secret-bearing journal exists only as `CB_SERVICE_RENEWAL_JOURNAL` in Infisical.
That journal drops token values after successful completion.

The renewal holds the Mac scheduler mutex and production runner/manual/submission
quiet lease. It inventories the real consumers, stages new credentials in
Infisical, verifies old/new API overlap, delivers the new credentials, checks live
Open WebUI retrieval and fresh Kuma/Prometheus results, then removes old API
acceptance and checks rejection. Partial delivery retains overlap and resumes the
same cycle without minting another generation or extending its expiry. An expired
or excessively old interrupted cycle requires reconciliation. Never recover by
copying an old API environment over fresh authority.

Active delivery targets are the Mac production collector configuration, VM109's
existing private collector/operator/probe bundles, Open WebUI's existing retrieval
filter valves, Kuma monitor31, and Prometheus's existing token file. Authentik
human login and OIDC policy are unchanged. No Open WebUI recreation was necessary;
trusted HTTPS succeeded from its live process. Temporary Kuma admin JWTs expire
after180 seconds.

The controlled live rotation completed with an actual interrupted-delivery resume.
Kuma's adapter originally raced the server's asynchronous handler registration;
it now waits for the application `info` event before logging in. This is covered
by `test_renewal_kuma.cjs`. New service credentials expire
**2026-09-18T20:10:30Z**, with renewal due **2026-09-15T20:10:30Z**.
The existing scheduler performed the new check at20:15 UTC and reported `not_due`.
Future clock-driven rotation is fixture-tested, not claimed as already observed.
Prometheus's renewal failure/staleness rules are installed, healthy and inactive;
the existing imminent-expiry alerts remain.

## Runner reconciliation and validation

The first stop's cause is **unreproduced transient/unknown**. The former launcher
swallowed exceptions and rewrote the attention marker every tick.638 idle ticks
preceded the latch, but the original error cannot be recovered. The installed
scanner passed in the actual cron environment. All three existing jobs have no
automatic policy; there were no pending automatic jobs, checkpoints, management
journals, unacknowledged or redelivered queue messages, or worker containers.
Existing manual started markers and jobs were preserved. Reconciliation occurred
under the ordered quiet lease with unchanged boot identity.

Three scheduled cron ticks at20:16:04,20:17:05 and20:18:05 UTC were idle and healthy.
The runner is unpaused with no attention or pending checkpoint. The new marker
preserves the first timestamp and only the exception class, never raw errors or
credentials.

Validation:79 existing recovery tests,7 renewal tests with every durable-effect
interruption boundary, the Kuma readiness regression,3 actual marker checks,
21 live API/auth checks,14 frontend assets,481 archive downloads across87 meetings,
and1,901 fully FTS-indexed corpus rows. Database table/schema fingerprints and
managed data files are identical before/after, including3 jobs,4 attempts and29
model-call records. The next fresh real meeting remains the first production
automatic end-to-end acceptance; none was submitted here.

One separate limitation remains: the existing `legacy-intake-ownership` Mac hook
reported failure during the scheduled hourly cycle, so that whole cycle is not
reported as green. The saved Folder Actions configuration still has Zoom disabled,
the old n8n container remains stopped and old retrieval paused. Its exact runtime
check failure remains unconfirmed; no legacy control was loosened or re-enabled.

## Recovery and relay

Private before/after controls, including current management code and runtime pins,
were verified on VM109, the Mac and platform-db:

- VM109: `/srv/community-brain/artifacts/cbm-weekly-20260911-015/{before,after}`
- Mac: `~/.local/state/community-brain-management/weekly-015/{before,after}`
- platform-db: `/var/backups/community-brain/weekly-015-{before,after}`

Exact sizes/hashes accompany the handoff receipt. Original attention, boot, cron
and management evidence is preserved in the VM109 request artifact directory.
Before/after copies are controls and fingerprint verification, not a claim that a
new PBS snapshot or another production database restore ran during request015.

To roll back the weekly policy, first pause and hold the ordered quiet lease,
restore the prior effective-s01 launcher/runtime/renderer pins, coordinate the
provider policy back to the corresponding US$2 total guard, render **fresh**
Infisical identities and verify the API before resuming. Do not restore old tokens,
data, attempts or outbox events. The independently superseded retrieval rollback
deadline and boot/restore pause rules are unchanged.

The safe receipt is in VM109's
`/srv/community-brain/handoff/responses/CBM-WEEKLY-20260911-015/receipt.md`.


Nonblocking packet note for Forge: the approved indexing helper retains an old `lifetime_limit_usd: 2` diagnostic journal header; the actual request guard enforces US$5 weekly. This metadata was not silently changed in the immutable sender overlay. Forge reported50 targeted tests; management did not rerun those absent test sources.

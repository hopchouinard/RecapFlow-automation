# CBM-MANUAL-OWNERSHIP-20260910-007

Target home.servers. Execute the remaining ownership work within Patrick's
approved manual processing phase. He instructed Forge to launch the remaining
work and avoid routine approval interruptions. This is the phase's already
approved conditional supersession of the temporary hold mechanism, not service
retirement or a new processing/publication phase.

Forge independently verified all17 response files from request006 and acknowledged
its completed recovery, probe renewal and runtime checks. Accepted receipt.md SHA256:
3172c4c082c7cce4f5bba5952ec4549bb91a40f806e861c3b8f6d125ede2bd67.
Accepted ownership-supersession-proposal.md SHA256:
a30cd87d6127b92526e63f723ea3c7ea42ab28485f8df02fae7a6aa8802810e0.
Both attached with OPERATIONS.md and the approved phase.

## Close operational gaps before supersession

Use the existing management stack and credentials. Correct the documented
00:30UTC dump / hourly :25 copy / nightly PBS ordering gap with a bounded copy
and freshness verification before the existing PBS window. Preserve retention,
prior backups, other VMs and schedules. Verify dump completion, copied checksum,
and available time before PBS; report stale/missing copies via existing management
health/status rather than labeling coverage complete. Test failure cases without
breaking production backups. A sleeping/unreachable Mac remains a dependency;
record this accurately and make freshness failures visible. Do not disable PBS
or silently change shared backup policy. If a robust correction needs a broader
infrastructure change, prepare it and report the blocker before supersession.

Make the verified post-manual-job pairing an explicit required operational step:
management owns DB/files/config/corpus/runtime pairing, before/after consistency,
off-host copy and restore validation. Retain approval/start markers. Routine
nightly dumps/guest backups must not be described as automatically paired.
No need to repeat today's verified restore or run any new job. Record a concrete
repeatable procedure with drift/uncertain-result stop conditions, using existing
helpers where possible. Keep corpus-mutating lint and remote snapshot/artifact-push
schedules disabled; their current owner is the manual maintenance procedure.

Track all current service-identity expiries and their management owner through
existing maintenance status with advance expiry failure/warning visibility.
Earliest retained retrieval expiry is September17 03:52:50UTC; manual identities
05:03:42UTC; renewed probes06:22:56UTC. Verify actual metadata privately.
Do not rotate them again now or introduce autonomous credential extension.
A dated renewal procedure and visible advance expiry status are required; no
provider-key change, top-up or secret values in output.

## Conditional ownership supersession

Once the above controls are verified, execute the attached seven-step management
supersession proposal. Its preflight must still verify today's paired checkpoint,
active retrieval, selected manual path, no workers/intake activity, unchanged
3 jobs /29 model calls /3 inert indexing events and preserved canonical corpus.
Existing September8 replacement remains prohibited. Live indexing acceptance and
two weekly cycles are outstanding; do not label them passed.

Before touching live controllers, test exact changes with disposable state for
lock races, crash/retry boundaries, missing/corrupt markers, stale status, timer,
boot, direct --now invocation and unreachable peers. Fix the cold System Events
lookup using enumeration and exact saved-path matching; never global enablement.
Keep pre-supersession rollback semantics intact until the durable terminal record.
Install Mac hook first; then VM101 controller under the shared rollback lock.
Both must refuse stale restoration after terminal supersession, with
mac_resume_allowed=false. Preserve all original restoration materials privately.

Only after verifying both sides' terminal state may you disable and mask the
exact deadline timer AND service. Verify direct controller invocation is also a
no-op, old writers/restart policies/crons and Mac intake remain disabled, and
existing certificate/backup maintenance still works. Leave immutable flags in
place. Do not extend the deadline; if prerequisites fail, leave the original
September11 01:25UTC rollback /01:30 hard deadline effective and report the blocker.

Return exact code/control hashes, tested cases, terminal record, timer/service
states, all legacy safeguards, active API/WebUI/monitoring checks, maintenance
ownership and the deliberate recovery procedure. Preserve prior checkpoints and
make any new control recovery copies private/off-host through existing access.
No secret values, raw data or dumps in relay. No ordinary worker, queue replay,
recording acquisition, model processing, corpus replacement, publication,
CBM-09, old service/data retirement or final CBM-10 work. User artifact-preview
acceptance remains separate and will be requested by Forge after these checks.

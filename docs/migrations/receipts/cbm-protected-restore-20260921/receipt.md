# Request030 verification receipt

Request: `CBM-PROTECTED-RESTORE-PREP-20260921-030`.
Actor: home.servers. Completed preparation: 2026-09-21T12:42:43.466718+00:00.
Deadline:2026-09-21T20:00:00Z. All six sealed input documents match request.json.

## Outcome and boundary

Preparation artifacts and fresh synthetic mechanics are delivered. **No protected
production capture/transfer, installation, rotation, ingress, cutover or processing
resume occurred.** VM101's WebUI remains stopped and recovery-only; the guest's
other services were not stopped. No production credential/signing value or content
was copied into a new store. Source-side metadata hashing returned only digests,
counts and identities. No paid provider call, live intake change or authority
extension occurred. No source branch was pushed and no parent gitlink was changed.

The packet is **not an executable production transfer approval**. Exact production
wrapper binding, pending-operation/maintenance deadline and interruption/readback
validation remain before that phase can be dispatched. The concrete scope,
commands, source/destination identities, rollback and retention proposal is in
`OPERATOR-PROPOSAL.md`. `ACCEPTANCE-PLAN.md` separates completed synthetic evidence
from private recovery, browser, capacity and provider gates. This limit is explicit;
no preparation result is substituted into a production acceptance slot.

## Verified results

- **39 Mac boundary tests,39 VM108 boundary tests,293 parent tooling tests pass.**
  Mac fixtures stub Linux extended-metadata observation; VM108 uses the real check.
  Corrupt/truncated/foreign-scope/wrong-hash bundles, path traversal, escaping links,
  linked ancestors, extra files, existing targets, unsupported extended metadata,
  busy/replaced locks and hold drift are negative cases. Artifacts contain exact
  test output, not just passing flags.
- Actual PostgreSQL18.6 logical dump and independent-server restore preserve all
  seven representative synthetic tables, one unknown-outcome attempt, sent/pending
  outbox, source/artifact relationships and FTS query result. The exported-snapshot
  SHARE fence rejects a real attempted concurrent INSERT. No worker runs.
  Database receipt manifest: `17cee34e8e36cc31116384e1c8ca0d0e20c866abbe0e55a513660a6e6dcf9c33`.
- Final source-v6 captures and verifies a fresh component bundle, passes it through
  the strict stream receiver, independently restores it, and preserves all held
  controls. Restored database dump bytes match the independently restored
  PostgreSQL attempt04. Final manifest: `711afb4bc4393216cd39a70de534b5a9d4b77c5714b8fa726c66e2ca3191bba3`.
  Empty directories, ownership/modes/mtime and contained relative links match.
  An existing restore destination is refused; its new write remains intact.
- The actual pinned WebUI image passes synthetic preservation tests: old session200,
  fresh login200, retained chat200, anonymous401, signup403 with effective persisted
  signup disabled, wrong signing key401. The original stopped fixture is unchanged.
  Session manifest: `c729c6c05ea9cacd7541b1b84d108aee92a2fe474172f29917a5a255d9f8643f`. Final source-v6 independently
  verifies/restores that preserved bundle again. No rendered browser, real account,
  real upload or protected real-session continuity is claimed.
- Six synthetic tests exercise the unchanged inherited budget helper, including
  exhausted/invalid allowance, allowance timeout, ceiling, wrong endpoint and
  unknown-response/reopening refusal. External allowance/provider calls:0.
- Actual Request029 `compile_plan` refuses production before creating a plan.
  All21 production evidence slots stay null. `compiler-reconciliation.json` maps
  the incompatible new/legacy receipt layouts and required validator work.
- All11 Request030 containers are stopped and retained with network `none` and no
  published ports. No OOM was reported. All44 pre-existing VM108 containers and
  both production containers retain their IDs/images/config/start/restart state.
  All Request026–029/Forge fixtures and uncertain attempts remain in place.

## Refreshed private bindings and storage

Current CB database: `community_brain_prod` on `10.1.10.50:5432`, PostgreSQL18.6,
runtime role `cbm_prod_runtime`, owner `cbm_prod_migration`. It has4 jobs,20 stages,
9 attempts,9 sources,21 artifacts,12 outbox rows and42 model-call rows. Canonical
row digests were computed inside the existing API container in a repeatable-read,
read-only transaction; no rows were exported. Existing admin socket access on the
DB host supports the proposed future dump without copying its password.

Dormant WebUI SQLite is unchanged at SHA256
`c4d3953ee249c642be9e0ffb7e7ed8e48adb14ad22531761f038b7ebd71b2b54`:
1 user,60 chats,111 files,5 models,10 prompts. Chroma counts/hash and signing digest
also match the initial observation. The current strict full-tree inventory has
637 regular files,166 directories,46 contained links,
1178802835 actual regular-file bytes, largest file145217532bytes,
and no extended attributes. The earlier approximately2.34GB estimate follows
cache links and double-counts referenced bytes; this is a counting distinction,
not evidence of deleted data. Exact private filename manifest remains source-side
in memory; only aggregate digest `517b1c5a7b8a467641f50d06bb3f08b06d7d4d3cd7c272a07295c9c71728d3dc`
was returned.

Proposed off-host private receiver:
`root@10.1.60.10:/var/lib/proxmox-backup/cbm-protected-recovery/<capture-id>`,
outside the managed PBS datastore, root0700/files0600. About414GiB is available;
no directory or data was created there. Existing PBS VM101 snapshots remain listed,
including protected recovery anchors; their existence is not restoration proof.
Independent private offline restore proposal is
`VM108:/srv/dev-data/protected-restores/<capture-id>` on new isolated state.
No real-data application startup or ordinary dev copy is included. Retention is
proposed at least30days and through explicit acceptance, with no automatic deletion.
The Mac internal disk is unsuitable staging space (about3.9GiB free); the encrypted
external NVMe has ownership enforcement disabled and is not the selected target.

## Preservation limits, failed attempts and remaining gates

Six durable production trees match their initial digests; the three protected
paused/attention/boot files and retained r020 bytecode also match. The aggregate
`automation` tree digest changed. Its periodic `status.json` heartbeat is the only
file there with an mtime during this request, consistent with the existing paused
tick under the runner lock. Per-file starting hashes for every automation member
were not captured, so **whole automation-tree equality is not certified**.
`preservation-limits.json` records this separately from the preserved holds.

Retained early attempts: PostgreSQL initial bind ownership prevented startup;
fixed using fresh paths/containers. Earlier paired/fence attempts reused a logical
capture label and are noncanonical; final attempt04 and source-v6 have distinct
IDs/manifests. First WebUI readiness attempt timed out and cleanup stopped it
(OOMKilled=false); a fresh1.5CPU/300-check attempt passed all three sequential
runtime checks in about302seconds. Extended-metadata Mac test failures were fixed
with an explicit unit fixture boundary; native VM108 validation passes. These are
recorded in source-provenance.json, not erased or relabeled as first-try success.

Remaining: reviewed/interruption-tested production capture wrapper; explicit
protected capture/transfer authorization; off-host restoration of actual protected
data and signing; actual LanceDB/Chroma/relationship acceptance; rendered browser
and real staged-session checks; full-workload capacity; scoped paid development
identities and spend approval; all21 production slots plus a separately reviewed
production validator. Current4GiB VM108 cannot certify the simultaneous profile's
approximately4.96GiB aggregate service limits plus restore/OS headroom. The packet
proposes an approved8GiB capacity phase and an explicitly bounded provider test
(max3 requests/US$0.10 exercise cap, with verified model cost bounds before approval).
Neither resizing nor paid testing occurred.

Production service-identity expiry refreshed at12:41UTC:
**2026-09-22T20:53:07Z**, renewal journal completed. No generation was extended.
About32hours remain at this receipt; a new two-hour phase must start no later than
18:53:07Z that day and obey any shorter fresh deadline. Missing gates mean defer,
not restart VM101 or bypass validation. Previously approved ingress still waits
for a ready replacement.

## Source, receipts and delivery

Local source commit `4c16f84ef8e5d77dcb01953ee5635ceb27c646d9`, branch
`codex/request030-protected-restore`, based on Request029
`db6416c7a2ab679a800a5a3e047a6554295cfc80`. Fifteen source files; clean tracked
worktree, not pushed. Source archive SHA256
`205dc9237d6666a1c7530a0a9f498992c232694906b09254e200d0ba07f12ee3`.
`source.diff`, `source-provenance.json` and `source-v6-manifest.json` identify exact
source/evidence revisions. The inherited indexing budget helper is byte-identical.

`verification-receipts.json` is the structured summary. `artifact-manifest.json`
lists every safe artifact's SHA256 and size. Test logs, source/diff, metadata,
actual DB/session/transport receipts, compiler refusal/reconciliation and cleanup
receipts accompany this document. Private dumps, blobs, accounts, sessions, signing
material and all retained fixture state remain only in the Request030 VM108 private
workspace. The relay directory and files retain root0700/0600 permissions.

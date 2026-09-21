# Protected restore and acceptance packet — preparation

Prepared September21, 2026, from the verified Request026–029 inventories and
source. Status: **procedure and acceptance requirements prepared; transfer not
executed or authorized by this packet**. Request030 resolves the remaining exact
operator bindings before a protected-transfer decision. Production remains held.

## Sources, ownership and destinations

| Component | Authoritative source | Required treatment |
| --- | --- | --- |
| Current jobs, stages, sources, outbox and artifact records | Current Community Brain database used by VM109, resolved privately through CB_RUNTIME_DATABASE_URL | Capture a consistent logical backup. Restore only into a new isolated database for rehearsal; never overwrite the serving database with a test copy. Confirm exact server/database/version/role privately before commands are finalized. |
| Current files, config, corpus and archive | VM109 /srv/community-brain/files, config, corpus and meeting-archive-20260910 | Pair with the DB under a verified writer-free interval. Preserve vectors, FTS, source/artifact identities and hashes. No reprocessing, re-embedding or old-VM corpus replacement. |
| Operational controls | VM109 automation, automation-public, manual-approvals, exact runtime/management packets and private configuration | Preserve original bytes, ownership, modes and lock identities. Archive control state for recovery; never restore its locks over the active filesystem or reconcile boot as part of a data test. |
| Existing WebUI user data | Dormant VM101 volume open-webui-data, last inventoried at /var/lib/docker/volumes/open-webui-data/_data | Capture from the stopped source without starting/updating it. Restore into a new replacement-owned volume, never back into the source or over a retained candidate volume. |
| Existing WebUI signing key | Dormant container /app/backend/.webui_secret_key, outside the volume | Preserve separately through the approved private authority/transfer path. An empty WEBUI_SECRET_KEY environment does not mean there is no key. No value in Forge, relay, arguments or logs. |
| Off-host recovery | Existing protected backup facilities and verified private archives | Resolve exact fresh recovery location, protection/retention and independent restore destination. Backup existence or pg_restore listing alone is not restore acceptance. |

VM101's September20 counts (1 user,60 chats,111 files,5 models,10 prompts,
113 Chroma collections and1,555 embeddings) are comparison baselines, not current
acceptance targets. The inventory measured approximately2.34GB. Refresh metadata
and record drift; do not force a new snapshot to match historical counts.

## Phase sequence and release points

1. **Read-only preflight:** home.servers identifies exact source container/volume,
   database authority, writer inventory, image/configuration identity, backup paths,
   storage headroom and private destination ownership. Report metadata only. Verify
   VM101 stays stopped and no current production dependency is introduced.
2. **Prepare the operation:** select a unique capture ID and new private directories,
   database and volume names. Bind the final source hashes, exact commands, ordered
   locks, current authority generation, recovery owner and abort conditions. Test
   any new capture/restore/sanitization operation on synthetic VM108 state first.
3. **Protected capture/transfer phase, after its authorization:** under the Mac mutex
   and checked ordered VM locks, verify all relevant writers are excluded. Capture
   the current DB plus durable trees, control metadata and external runtime/signing
   material; record start/end observations and hashes. A failed or uncertain capture
   gets its own retained record. Never silently combine different capture attempts.
4. **Verify the recovery copy:** transfer through the approved private channel with
   hashes at both ends; establish an off-host protected copy. Independently restore
   DB/files/WebUI into fresh isolated destinations and compare durable content.
   Do not enable schedules, dequeue jobs, publish, call providers or clear markers.
5. **Development acceptance:** use scoped development identities and synthetic
   signing material. If a real-data clone is needed, its destination and permitted
   content must be explicit in the transfer scope. Keep the preserved original
   immutable, and sanitize only a separate test copy. Record every configuration
   substitution and private provenance; isolate networking before opening the copy.
6. **Replacement staging, later authorized production deployment:** use the same
   validated mechanics to stage the protected real WebUI data and signing material
   into replacement-owned state. Keep source data and current VM109 DB/files intact.
   Bind fresh authority values rather than expired credentials from backups.
   Perform post-deployment verification before admitting traffic; it is not a venue
   for testing a new restore procedure.
7. **Acceptance/activation:** require the evidence below and a fully bound serving
   plan. The existing activation controller preserves holds. Processing resume,
   weekly-cycle evidence and retirement remain separate decisions.

## Private manifest and safe receipt contract

Every capture and restore record must identify:

- Capture ID, source host/container/database/volume identity, timestamps, exact
  image/source versions and writer-exclusion evidence.
- Component files with size/hash, relative path, ownership/mode and contained-link
  policy; exact sets including empty required trees and external signing material.
  Private filenames and DB rows remain in the protected manifest, not the relay.
- Source and destination component digests, independent DB observation comparison,
  restored volume/database identity, restore tool version and actual checks run.
- Original versus sanitized-copy identities and a complete transformation manifest.
  Sanitized content must not be compared byte-for-byte to an unsanitized original
  without accounting for the changes, or presented as a preservation archive.
- Off-host copy identity and a successful independent restore receipt, protection
  policy, owner and retention disposition.
- Explicit scope: synthetic development, authorized private-data rehearsal, or
  production post-deployment verification. Missing results stay missing; no true
  flag may stand in for an actual restore or browser result.

The relay receives capture/receipt IDs, aggregate counts, component/manifest hashes,
private evidence locations, pass/fail and limits. It receives no user content,
uploads, plaintext credentials, DB dumps, signing material or provider responses.

## Acceptance checks

| Area | Required result |
| --- | --- |
| PostgreSQL | Independent restore succeeds; schema/version and canonical durable records match. Job/stage attempts, outcome_unknown records, outbox/publication state and artifact/source relationships remain unchanged. No worker execution. |
| Durable files/corpus | Exact file set and hashes match; files referenced by DB records exist. LanceDB schema, embeddings, session counts and FTS coverage match without regeneration. Read-only retrieval returns expected provenance on the validated runtime. |
| WebUI preservation | SQLite integrity plus relational/user/chat/upload/model/prompt/function/knowledge relationships match. Upload bytes, vector files and Chroma query results match. Valid contained cache symlinks work; escaping links are rejected. |
| Credentials/configuration | Inventory persisted endpoint/token overrides privately. On the dev copy, replace production service/provider credentials before startup; disable automatic processing/egress. Preserve original configuration unchanged in protected recovery state. |
| Signing/session mechanics | Dev synthetic pre-restore session survives restore with the same synthetic key; wrong key is rejected. Original key preservation is verified privately during the authorized production transfer, then existing user sessions are checked after staging. Production signing material is not a development test credential. |
| Browser | Intended user can sign in, use retained chats/files and retrieve context; anonymous access denied, signup explicitly disabled in effective persisted/startup configuration. Test synthetic browser behavior on VM108 first; real identity/session continuity requires the protected staged deployment. |
| Recovery/rollback | Independent off-host restoration works. Rollback retains replacement writes and all journals; it neither undoes migrations nor merges divergent data automatically. Define explicit recovery choice after writes. |
| Capacity | Measure full intended API/WebUI/worker/restore workload on VM108 with the proposed limits, no OOM, adequate agreed headroom and accepted latency. Record concurrency, sizes, peak memory/disk, duration and failures; idle memory is insufficient. |
| Provider/intake | Validate the scoped dev allowance/unknown-outcome/budget mechanics and necessary real provider/intake behavior under existing spending limits. No production keys, unauthorized paid run or replay of completed/uncertain meetings. |

## Existing implementation limits

Request029's recovery helpers are evidence of synthetic mechanics, not a production
transfer script. In particular, validation_host.paired stops and restarts a fixture
WebUI, and finish_pair writes checkpoint acknowledgments and clears a fixture
checkpoint-needed marker. **Do not point either helper at VM101 or production
state.** Request030 must separate capture/restore verification from those fixture
control effects and validate the final operation on VM108.

The existing production compiler/controller remains disabled. Its 21-slot template
is not filled by this preparation document. The new private manifest contract must
be reconciled with the compiler's actual receipt schema; do not merely rename a
synthetic receipt or set its flags to true.

## Unresolved bindings for Request030

Exact current database/source/container identities; current backup and independent
restore destinations; disk headroom; private authority/signing delivery method;
the permitted sanitized real-data test scope; ownership/link restoration rules;
precise capture/restore commands and cleanup boundaries; effective persisted WebUI
endpoint/credential substitutions; capacity workload/thresholds; real-provider test
budget and browser acceptance operator. Return a concrete bounded phase proposal
with these resolved before requesting capture/transfer authorization.

The last recorded service-identity expiry is September22 at20:53:07 UTC. Recheck
metadata and report scheduling risk. Deadlines do not authorize a legacy restart,
production renewal, data transfer or validation bypass. Previously approved
chat.patchoutech.lab DNS/Traefik/Step CA still waits for a ready replacement.

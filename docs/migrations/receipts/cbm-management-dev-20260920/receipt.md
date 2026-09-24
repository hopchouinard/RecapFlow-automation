# Request027 verification receipt

Request: `CBM-MANAGEMENT-INTEGRATION-20260920-027`  
Actor: home.servers  
Completed: 2026-09-20T21:41:10.640715+00:00

## Outcome

Development management integration passed. This receipt does **not** certify a
production rollout or authorize it. No production service/key/source/hold,
monitor, collector, DNS or Traefik configuration was changed. The authorized
Infisical development child folder was created inside the shared homelab project.

## Authority amendments from Patrick

- homelab may be used, but only the development material under
  `/development/community-brain-dev`; production keys remain excluded. Actual
  generated identities and the development journal used environment `prod`,
  child folder `/development/community-brain-dev/request027`. The original
  separate-project restriction is superseded; org discovery403 is not a blocker.
- `chat.patchoutech.lab` DNS on UniFi, Traefik routing and Step CA issuance are
  authorized when a ready replacement target exists. No further approval is
  needed for those actions. Production source installation, data/signing transfer,
  rotation and cutover are still separate gates. The isolated development fixture
  has no published ports and needs no such route.

## Verification receipts

| Boundary | Observed result |
| --- | --- |
| Infisical | Real read/save/read equality; five generated development identities; parent development values unchanged |
| Transport | Real Mac scheduler mutex, ordered SSH lease locks, lost-response reconciliation without replay and lease-loss refusal |
| API lock | Actual write middleware returned503 under the quiet lease; retrieval remained available |
| Consumers | Actual API/WebUI filter cache, dedicated Kuma and Prometheus; delivered probe/operator/collector bundles used by API probes |
| Interrupted renewal | Intentional lost delivery acknowledgment preserved overlap; a later stale Kuma heartbeat also stopped revocation |
| Resume/revocation | Same cycle `9ff979a4-a49d-4588-8ace-bee8e967a668` resumed; fresh consumers passed; all five old tokens rejected; journal completed |
| Recreation | Pinned stabilization image,20 module/frontend files, no old overlays and identical pause/attention/boot marker hashes |
| Worker holds | Manual launcher refused held execution; real automatic entry excluded by runner lock; no worker execution claimed |
| Source |25 installed management files still match Request024; terminal superseded intake guard preserved/tested |
| Tests/build | Six boundary tests passed on Mac and VM108; generic builder reproduced the final immutable packet byte-for-byte |
| Cleanup | Only six Request027 containers stopped; no OOM; four pre-existing services retain their exact start timestamps; both earlier fixture groups remain stopped |

Real services were exercised against synthetic data. Embeddings/model-list are
deterministic fixtures. Desktop intake/upload, paid-provider calls, worker
execution, production restore and post-migration human browser sessions were
not tested. These are explicit limits, not simulated passes.

## Candidate and packet

Commit: `3022cda148f9fd3b1732a687a40ba2220bcc90ef` on `codex/request027-management`. Clean worktree; not pushed.
Base: `f7356151a563d4d07f390872efd9265b6b9302bf`.
Source archive, scoped diff, source provenance and safe evidence are attached.
The unchanged policy SHA256 is
`8406820b5795e67f03ecc7521ab522aef7ff3aae9370ad30257ec286ce35d56c`.

Final VM108 packet:
`/srv/dev-data/workspaces/cbm-management-integration-20260920-027/packet-v7`

Manifest SHA256:
`19c85b5cbece351f9c9c09606ab3ccaa35065fd4bcee35f65e8ab2cb502d08a9`

The descriptor binds API/worker image, verified WebUI image relationship,
helper/module/frontend hashes, external signing environment, held boot entry,
recovery images/files and management controls. r020 is not modified. Worker
helpers are scoped to the development image/network/state and remove old module
mounts; the indexing budget helper is unchanged. Review the final production
binding and validate execution before enabling a worker release.

## Failures retained in the record

- Initial lease acquisition timed out before any WebUI setup effect; bounded
  response timing was adjusted while retaining fail-closed behavior.
- Strict umask removed Prometheus directory group access. Explicit directory0750
  and file0640 modes corrected the development adapter.
- Fresh Kuma2.4 needed database setup. An early inspection created an empty
  SQLite database; it was verified empty and preserved as
  `cbm-r027_kuma/_data/kuma.empty-before-initialization.db`, then Kuma initialized
  its own fresh schema. The adapter now uses read-only SQLite inspection.
- Calling resume after add started Kuma's monitor twice and led to repeated
  stat_hourly uniqueness errors. The duplicate start was removed and only
  development Kuma was restarted with its database retained. Renewal preserved
  overlap until fresh acceptance succeeded.

## Retention, remaining gates and expiry

Private state remains on VM108 under the dedicated workspace and its named
volumes, and the scoped development authority remains in Infisical. Private
artifact locations, permissions and checksums are in `cleanup-acceptance.json`;
values and databases are not in this handoff. Prior packet revisions are retained
for diagnosis. No stopped fixture should have setup replayed without inspecting
its markers and state.

Read `rollout-rollback.md` for protected before-state, data/signing-key transfer,
ordered locks, staged verification and recovery. Production descriptor/worker
execution, resource sizing, protected restore and browser acceptance remain gates.
DNS/Traefik/certificate authorization is recorded; no ready production WebUI
target was deployed by this request.

Production metadata rechecked September20: completed journal, expiry
**September22 at20:53:07 UTC**. The September21 at20:00 UTC request deadline is
met. r020's recorded members match, but an extra
`__pycache__/run.cpython-314.pyc` would fail its exact-file-set gate. It was not
removed and the assertions were not weakened. Expiry permits no bypass.

Artifact checksums: `artifact-manifest.json`.

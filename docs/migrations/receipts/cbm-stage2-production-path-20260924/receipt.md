# Request036 verification receipt

Request `CBM-STAGE2-PRODUCTION-PATH-20260924-036` was claimed. All six delivered
documents matched their declared SHA-256 hashes. This is a **partial** response.
Stage 2 is incomplete; production admission remains closed.

## Source and parity

- Isolated `agent-ops` branch: `codex/request036-production-path`.
- Exact unpushed commit: `d5b013b6a9e37704516b50d31ab8f15f1950ed21`.
- `source.tar`: SHA-256 `04a1f7b4c4531aa8fb77e75af19677a88777c23ccaf3cb02adc89d0b70176cb1`.
- `source-members.json`: SHA-256 `80b0600bf9340acb47de1c7f1ce5c4b1e879b87e44d762d165b2a481bf4d77e1`, 11 members.
- VM108 received the exact archive: SHA-256 `04a1f7b4c4531aa8fb77e75af19677a88777c23ccaf3cb02adc89d0b70176cb1`; all 11 extracted member hashes matched the manifest. The final committed bytes were tested there.
- No parent gitlink update or push occurred. The existing Request035 branch/source and the preexisting parent worktree submodule deletions were not touched.

## Review and development checks

- Read-only VM109 observation: SHA-256 `a6e247ac7e9d0000019b87ef6c07a01ec3178b81f50a03f59cbb526fc06a8fa8`. Machine `a22c8cab9edc4333a2dcc78e5b35a604`, `/srv/community-brain` ext4 UUID `d5113805-c76b-4955-b13a-6482ce6f6ac9`, exact incumbent `766a37a09d4ce16a4c69a8d3dd0634bc155de70085efb0eb6aad7d7281c528f6`, exact image `sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449`, running. All six control/lock hashes, modes, owners and inode/device identities matched Request033's historical binding at observation time. Only metadata/hashes were read.
- Source-pinned review plan: SHA-256 `c6eca8a57d97e2c03781d2438c6ed1e814e75f2bc8bc8072d6a4995d15878b5d`. It binds the source archive and every member, Request033 contract, live VM109 observation, incumbent fingerprint, control and lock identities, historical private destinations, Mac mutex, operation, phase deadlines and rollback owner. It leaves all 21 production slots and all three authorities null; current authority generation and deadline are null. `require_executable` refused it with `review plan is never executable`.
- Review tests: 4/4 passed locally and 4/4 from the exact archived source on VM108. Negatives cover stale observation, foreign lock inode and altered source archive.
- Fresh VM108 fixture `/srv/dev-data/workspaces/cbm-stage2-production-20260924-036`: Request030's exact library captured a synthetic corpus, verified the content-addressed bundle, and restored the file plus empty directory with exact tree equality. Receipt SHA-256 `48335360ed053f038554977bfa0dd7b006fefa04b4bb84a96afe29c53508ec92`; capture manifest SHA-256 `34a80b7b3708a1de5552b57bf49d5758fcae7624ecb48ebfef5c2ba546e837e0`. The hold remained unchanged. This was one local file phase, not a DB, Docker, PBS or production recovery rehearsal. Its 120-second deadline did not expire; hard cancellation inside a blocking capture is not implemented.

## Exact incomplete gates

No semantic production receipt validator or per-slot positive/negative matrix is complete (0/21). The current production authority generation, separate protected-preservation/serving/resume authorizations, and a new deadline are absent; the historical identity expired September 22. Request033's private destinations have not been created. The staged VM109 installer/controller/finalizer, production DB fence and off-host transfer, independent finalizer, and the requested VM108 Docker/PostgreSQL/systemd/Mac-SSH fault matrix remain unimplemented. The Request035 controller is still development-only. There was no VM109 installation, stop, capture, private transfer, provider call, cutover, resume, resize, or VM101 action.

`acceptance-ledger.json` is the single status ledger. `source-delivery.json`, `source.tar`, `source-members.json`, `vm109-observation.json`, `review-plan.json`, and `vm108-preservation-receipt.json` are the referenced receipts. No production evidence slot has been filled from a development fixture.

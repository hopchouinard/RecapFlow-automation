# Request034 verification receipt

Request ID: `CBM-STAGE2-QUALIFICATION-20260923-034`. Updated: `2026-09-23T23:42:48.829588+00:00`. Actor: home.servers.

Source commit: `6bdd50086646337a6db2b103b1dd28910db33635` on `codex/request034-stage2` (agent-ops; not pushed).
VM108 final packet: `packet-v12`, manifest SHA-256 `7c5cfba2187e72ea40a6955592278539f7982376abbe647819e466354b3b3825`. VM108 source tests: 16/16 passed.

Development acceptance: actual Infisical and fresh CA, live API/WebUI/filter/collector/Kuma/Prometheus renewal,
current/expired/wrong/cross-scope HTTP 200/401/401/403, 677 concurrent requests with zero failures and no OOM,
and exact-image browser and paired recovery with original-key 200/wrong-key 401. See the ledger and JSON for limits.

Production execution: **not qualified**. The production controller, installer, independent finalizer and fault matrix
remain incomplete; all 21 production slots are null. The recorded production identities expired and their existing
renewal is failing. The original VM109 API/Alloy are running; no production or VM101 change, transfer, resize or paid call occurred.

Safe response files (SHA-256):
- `acceptance-ledger.md` `5b3c725afb476840ea25adbf61a127044d72777484027c746c64ed1364597838`
- `browser-observation.md` `f416ccbcf255c73f40661077179f8f3e84710d66b3067a66d8b18aa44efcaaad`
- `ca-issuance.json` `019543e1aa0df36521dac8f401cd539651bf260c8741849cc8ab76e69980736d`
- `capacity-acceptance.json` `091f9251a6a711b5c8c3ed2b9e47fe14190ab670f3a01a354d0821f52ae27ff4`
- `negative-auth-acceptance.json` `3526f86751eb1f360aedb406c90d5b8006ac0d2c4be503814d79bad44c327133`
- `postbrowser-recovery-acceptance.json` `21fc83440d41c1da2dc1e59dbd6611791737b065a838596417bd2c2642054d07`
- `source.tar.gz` `1993976f8f1f06a43cf746f87725b14112b5f9619df149e3e311ea3b4b5f7dfd`
- `verification.json` `ee5e67cf70327a87d4c7a0ea7402fb19800d5e71fa87d0769f6e748a76cfb186`

Private evidence retained at `~/.local/state/community-brain-management/request034` on the Mac and
`/srv/dev-data/workspaces/cbm-stage2-qualification-20260923-034` on VM108. These paths contain
development secrets/content and are not included in the relay. Seven Request034 containers are stopped;
their volumes and failed-attempt markers remain. The four pre-existing VM108 services remain running.

Remaining gate: review and implement the production-capable controller/installer/finalizer, test its fault matrix
on fresh VM108 final bytes, renew production authority under a separate mandate, and fill/verify each production
evidence slot in a separately authorized protected-preservation phase. No production execution approval is implied.

# Collector management delivery complete

Provisioned and verified 2026-09-09, in response to
`cbm-collector-management-handoff.md`. Forge may proceed with the approved
development activation steps in that handoff. No additional management access
or secret values are needed.

## Delivered

- New lab-CA certificate, DNS SAN `community-brain-dev.patchoutech.lab`.
- VM 108 `/etc/community-brain-development/collector-tls/fullchain.pem`
  contains leaf plus intermediate; `key.pem` is its new matching private key.
  Directory root-owned 0700; both files root-owned 0600.
- Certificate expires **2026-09-10 23:49:29 UTC**. SHA-256 fingerprint:
  `E3:1A:17:B4:0F:36:C5:9B:93:94:BB:7D:25:0B:EF:D0:5B:09:28:55:E2:28:EE:E3:E5:6F:BF:AE:02:49:4E:AD`.
- Infisical `homelab` / `development` / `/applications/community-brain` holds
  `CB_DEV_COLLECTOR_TLS_FULLCHAIN_B64`, `CB_DEV_COLLECTOR_TLS_KEY_B64`,
  `CB_DEV_MAC_COLLECTOR_TOKEN`, `CB_DEV_MAC_COLLECTOR_EXPIRES_AT` and the updated
  `CB_SERVICE_IDENTITIES`. Base64 is storage encoding, not encryption; the key
  remains secret material. Infisical is the authoritative lifecycle location.
- The new identity has subject `community-brain-dev-mac-collector`, scope
  `community-brain-dev`, and **only `sources:upload:chat`**. It expires
  **2026-09-10 19:43:21 UTC** (Unix `1789069401`).
- Its SHA-256 identity record was appended to the authoritative array and
  `/etc/community-brain-development/runtime.env`; the original three identities
  remain, and every other runtime line/flag is byte-preserved. A private
  `runtime.env.before-collector` snapshot is beside it; do not print it.
- Raw token delivered only to the Mac at
  `/Users/pchouinard/Library/Application Support/CommunityBrainDevelopment/collector.json`,
  user-owned 0600 in a 0700 directory. It contains backend
  `https://community-brain-dev.patchoutech.lab`, token and expiry. Do not copy it
  to Forge, the VM, API/model-worker containers, Git or chat.

## Verified and remaining

Passed: Infisical write/read equality, preservation of unrelated authority values,
certificate/private-key match, intermediate chain, SAN, certificate lifetime,
VM trust/hostname validation, Mac native system trust/hostname validation,
Forge-to-guest access, private file modes, and Mac token/hash/permission/expiry
agreement with the VM identity. No raw token is in API runtime configuration.

Management did not restart services, open firewall ports, start the proxy or
execute the collector. End-to-end HTTPS/auth checks remain Forge's activation
step. Recreate only the development API with the updated identities, apply only
the two approved source-specific TCP 443 UFW rules, start the prepared proxy,
and verify TLS, allowed upload and denied operations. Keep existing localhost
browser login, production services, recurring sync and remote publication intact.

After endpoint validation, follow the exact manual exercise in the request:
recording `181075701`, selected chat hash
`5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084`.
Confirm the local tool path and selected relative Zoom path before invoking it.
No job creation or model calls are part of this collector exercise.

## Bounded lifecycle

This is a short development rehearsal, with no automatic renewal or timer.
The management operator's `identity/provision-collector.py` uses the existing
CA operator in place; no CA/bootstrap credential leaves that environment.
It reads and updates Infisical, refuses identity drift and concurrent runtime
changes, and preserves existing runtime lines. Existing expired identities or
near-expiry certificates require deliberate renewal before reactivation.
Do not use the original general `render-runtime.py` for this collector update;
the dedicated operation preserves the current development configuration.

Rollback: stop only the dedicated proxy, remove its two added UFW rules, remove
only the collector identity from Infisical and current runtime, reload only the
API, and remove the Mac token file. Preserve newer changes; do not blindly
restore an old runtime snapshot. Remove the development leaf/key delivery copies
and authority entries when retiring this endpoint. Never remove/revoke the
shared CA, signing key or unrelated identities.

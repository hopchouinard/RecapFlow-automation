# CBM-DARK-MODE-20260910-008: completed

The requested frontend dark-mode switch is deployed at
https://community-brain.patchoutech.lab. The API alone was recreated through the
existing Mac Infisical renderer; the backend image and entire API environment,
including auth configuration, are unchanged. No new processing, provider activity,
job submission, publication, corpus replacement or retirement occurred.

All three supplied assets matched the verified Forge manifest. Two prior hashed
assets were copied from the running image and retained without collisions, so
already-open browser sessions retain their old asset URLs. The five effective
files are bound read-only at /app/web/dist on API only. Worker packets are unchanged.
The runtime packet still validates all 14 files. The installed Mac recreation
helper now additionally pins the reviewed runtime manifest and five-file frontend
manifest and verifies every asset before rendering/recreating. Future recreation
therefore retains and checks the new UI. Historical paired archives are untouched.

## Verified results

Seven HTTPS checks passed: index and all four hashed assets match their exact
SHA256/size, and root/callback SPA responses match the new index. Fifteen live
scope/health checks passed, including absent/invalid credentials, collector scope
denials, operator read and metrics denial, and read/retrieval/metrics identities.
The API is healthy with 13 cue rules; original files/config/corpus mount modes
are unchanged. Only API and Alloy are running. Both Prometheus targets are up;
Kuma health/retrieval are up. The actual cached Open WebUI function retains its
source hash and new retrieval URL, returns ten sources and emits context.

All ten database table fingerprints, counts and schema match the captured
predeployment state: three jobs, 29 model calls and seven outbox records. Every
stored file, corpus file and config file matches its predeployment manifest.
Ownership remains terminal on VM101 and Mac. The old timer/service remain
inactive/masked; legacy writers, cron and Mac intake remain held, including all
2,867 immutable inodes. No rollback deadline was extended or rearmed.

Forge's prepared-build evidence covers system preference, keyboard switch,
persisted choice, mobile layout and preview/download in dark mode. Management
verified deployed bytes and live service behavior; Patrick's visual acceptance
of the switch remains separate. No claim of additional browser testing here.

## Exact bindings and recovery

Runtime manifest before:
270fda6f14ec92fc284d428155d887df1f7a3d2f49652410c378d8027e446c7d

Runtime manifest after:
4592ab2491d6e70a8b3e4c91ce743a612b719720ed0aec54e439848525c88d1d

Effective static manifest:
8de0f1355aace950ada0bc57a9e3a90d41c10cd8b90291d33054c80603f61b50

Current Mac recreation helper:
3bbd1d052d6adb5b248ea2c3271094285913e574a1d635ab0f78dfb3e983f0ee

Full before/new/effective asset hashes are in preparation.json. Runtime paths:
/srv/community-brain/workspaces/manual-20260910/ and
/srv/community-brain/workspaces/cbm-dark-mode-20260910/.

Private VM109 originals, inspection state and new static/control archive are under
/srv/community-brain/artifacts/cbm-dark-mode-20260910/.
The original Mac helper is retained under
~/.local/state/community-brain-management/dark-mode-008-before/.
Two verified root0600 archives under platform-db
/var/backups/community-brain/dark-mode-008/ preserve old/new static and effective
recreation controls. Exact sizes/checksums are in recovery-copies.json. Existing
paired application recovery and PBS checkpoints remain retained; no database
restore or new full-VM restore exercise was necessary for this static-only change.

Controlled UI rollback, only if required by a failed verification or explicit
follow-up: preserve current evidence; atomically restore the saved manual Compose
overlay and runtime manifest from the VM109 before/ directory, and restore the
original Mac manual_api_runtime.py to both its operator checkout and installed
management path. Validate the original 14-file manifest. Run the existing
Infisical-backed manual_api_runtime.py using current authoritative credentials;
never restore api.env.before over live configuration. Verify the original index
and assets against preparation.json, all 15 scopes, health/mounts and actual
WebUI retrieval. Leave the prepared dark-mode directory and all checkpoints
intact. No worker or legacy-control restoration belongs to this UI rollback.
Rollback was not needed and was not executed.

All checks passed; no blocker. Subsequent migration phases remain held pending
Patrick's separate direction. Companion hashes are in receipt-manifest.json.

# Request019 scoped rollback

Request: CBM-FATHOM-20260917-019

Run only if rollback is required. Do not restore data, old credentials, Authentik,
or whole historical archives. Those would overwrite independent current state.

1. Acquire the Mac scheduler mutex, then the existing supervised VM109
   runner/manual/submission quiet locks in that order. Verify no active or eligible
   job and no pending checkpoint. Reconcile any newly submitted work first.
2. Save the current controls privately. Set a request-specific deployment pause.
3. Compare current runtime/launcher pins to effective-pins.json. Restore only
   compose.production-manual.yml and runtime-manifest.json from the request019
   before deployment-controls archive. This restores the r016 API mounts and
   previous Signal frontend. Keep all packet directories and hashed assets.
4. Restore only boot_guard.py and files_adapter.py from that before archive.
   Restore the corresponding source/live Mac files and manual_api_runtime.py
   from before-local-controls/. Verify source and installed byte parity. These
   originals include request017 recovery and request018 human-access controls;
   do not restore or replace other library files.
5. Fetch fresh authority from Infisical and run the restored API renderer. Never
   restore api.env or provider secrets from the archive. Wait for Docker health
   to be healthy, then verify trusted HTTPS assets, automatic capability, both
   human access policies, and unchanged data/database fingerprints.
6. Remove only the rollback-owned pause after verification. Confirm the scheduled
   runner returns idle; preserve any independent attention/checkpoint state.
7. Capture new current controls and verify off-host copies. Keep historical
   captures and this receipt immutable.

Before archive on VM109:
/srv/community-brain/artifacts/cbm-fathom-20260917-019/before/deployment-controls.tar.gz
Off-host verified copy:
/var/backups/community-brain/fathom-019-before/deployment-controls.tar.gz
Mac originals:
/Users/pchouinard/.local/state/community-brain-management/request019/before-local-controls/

Rollback returns to the prior Fathom acquisition behavior, including its missing
worker importer mount. It does not change publication, replacement, retirement,
budget, token renewal, or the stopped request016 Mac-permission work.

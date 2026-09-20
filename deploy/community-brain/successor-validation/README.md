# Successor validation on VM108

This fixture executes the imported Request027 manual_worker.execute adapter with
real disposable PostgreSQL, JetStream, artifacts and LanceDB. It reuses the
established synthetic automatic-loop inputs. Processing/model, Fathom, embedding,
allowance-audit and queue-connection boundaries are explicitly replaced with test
fixtures. It does not certify host launchers, production TLS/scopes or paid budgets.

Copy this directory, management-development and automatic-rehearsal with their
repository-relative paths into a dedicated VM108 workspace. Make only that source
tree traversable/readable by container UID10001 (rsync --chmod=D755,F644). Keep its
parent private. Run compose.dev.yml with --abort-on-container-exit and
--exit-code-from check, retain logs/exit status, then run compose down. State is
disposable tmpfs; no ports, production identities or external provider access.

The packet builder is tested separately with test_boundaries.py. Build the same
revision on Forge and VM108 using the Request027 stabilization-image-files.json
and monitor-image-equivalence.json receipts; compare manifest bytes. Never replace
a sealed revision or install this development packet in production.

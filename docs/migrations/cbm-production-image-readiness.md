# Production image readiness — September 10, 2026

**Image prepared, verified and loaded on VM 109. API startup and ingress remain
held.** The remaining integrations in
[the management receipt](cbm-production-management-readiness.md) are still required.
No production container was created or started, migration applied, corpus
installed, or ingress changed during image preparation.

## Frozen source and image

The build uses an explicit 83-file source snapshot, not a claimed clean Git
commit. Existing tracked/untracked changes, including concurrent standards and
handoff edits, remain intact. The snapshot includes application source/migrations,
locked dependency manifests, frontend source, Docker build files and rehearsal/
staging definitions. It excludes private runtime files, credentials, corpora,
artifacts, caches and local dependencies. All 83 file hashes still matched the
checkout after canonical verification. `source-manifest.json` records each path,
size/hash and the base Git revision; the snapshot contains uncommitted changes.

- Tag: `community-brain:production-candidate-20260910`
- Immutable image: `community-brain@sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449`
- Image archive SHA-256: `f8d080c1856116b1bdf881a92fe2c6180b5b39764c66d79e5562014f052f1831`
- Source archive SHA-256: `b0316943b786c0d459ab51d4104313b80b502403b3b00c4b76d1203ec780b064`
- Source manifest SHA-256: `bcb0617cd44f237dbd7de7958bb027f17447128934b82cfa0e32d51d6508aebd`

Use the immutable reference for later startup. The image was built on VM 108 in
`/srv/dev-data/workspaces/cbm-production-source-20260910`. Production received
the saved image through Forge SSH streaming; no registry push or remote release
was performed. Archive checksum and loaded image identity matched on VM 109.
The Dockerfile pins Node/Python bases; uv uses a version tag and OS packages use
the repository state at build time, so the retained image is the exact tested
deliverable, not a claim that a future rebuild is byte-identical.

## Verification

- Canonical `scripts/verify-forge.sh`: 150 Node tests, 889 Python tests (70 existing
  warnings), 23 DB/queue tests, one component test and one Playwright test passed;
  frontend build passed.
- Built image booted on VM 108 against fresh disposable PostgreSQL and JetStream,
  with an internal-only network, no host ports, and model/publication flags false.
- Explicit Alembic migration, health, unauthorized denial, authenticated identity
  and empty jobs listing, SPA/callback responses, JetStream publish/read passed.
- The first smoke invocation could not read the mounted fixture script (0600).
  Changed only that nonsecret fixture's mode to 0644 and reran successfully.
- Removed the test project's containers, network and two disposable volumes.
  The existing live development stack remains running.
- VM 109 state UUID matched the management receipt. After image load,
  `docker ps -a` returned no containers. No application runtime credentials were
  read or required for this work.

## Retained evidence and next step

Private VM 109 directory, root-owned 0700, files 0600:
`/srv/community-brain/artifacts/cbm-production-image-20260910/`

Contains `image.tar.gz`, `source.tar.gz`, `source-manifest.json`, `build.log`,
`verification.log`, `smoke.log` and this receipt. VM 108 retains the source build
context, build/smoke logs and image archive under its workspaces/artifacts roots.

Management must complete the PostgreSQL roles/TLS/backup checks, JetStream scoped
transport/ACLs, Infisical runtime delivery, production OIDC claims, ingress and
monitoring checks listed in its readiness receipt. Report public settings,
private runtime paths and verification evidence without secret values. After
that handoff, Forge can apply the explicit migration, install and verify the
approved corpus/config mapping, and start the staging API within the authorized
phase. Keep startup and ingress held until those prerequisites are satisfied.
Cutover, remote publication and retirement remain separately gated. CBM-10's
explicit quality backlog stays last in the migration.

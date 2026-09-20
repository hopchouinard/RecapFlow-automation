# VM108 stabilization rehearsal

Run only in a dedicated source copy on `community-brain-dev`. Preserve existing
`cbm-live-development` services. `compose.dev.yml` uses a separate internal
network, disposable PostgreSQL/JetStream tmpfs, a private `/state` tmpfs and no
provider credentials. The synthetic fixtures are the established automatic-loop
rehearsal; they are not production weekly-cycle evidence.

On Forge, prepare two baseline code files from commit `f60a30c` for comparison:

```sh
mkdir -p /tmp/cbm-stabilization-baseline
git show f60a30c:community-brain/src/community_brain/jobs/api.py > /tmp/cbm-stabilization-baseline/api.py
git show f60a30c:deploy/community-brain/automatic/automatic_host.py > /tmp/cbm-stabilization-baseline/automatic_host.py
```

Include those files under `baseline/` in the dedicated VM108 copy; do not commit
the duplicate baseline directory. Copy only source/tests/configuration fixtures,
never `.env`, virtual environments, private runtime files or production data.
Make source directories traversable and source files readable by UID10001.

From that VM108 copy:

```sh
docker build -t community-brain:stabilization-20260920 -f deploy/community-brain/Dockerfile .
docker compose -f deploy/community-brain/stabilization/compose.dev.yml up --abort-on-container-exit --exit-code-from check
docker compose -f deploy/community-brain/stabilization/compose.dev.yml down
```

The checker exercises real durable delivery and indexing for two synthetic
meetings, preserves excluded work, compares old/new readiness on the same held
state, checks independent boot/attention holds and stale/failed-renewal behavior,
tests concurrent public projections and busy heartbeats, and proves that the
read-only diagnostic does not fence expired stages. A real refused database
connection must produce a safe `OperationalError` diagnostic. Finally it boots
the actual API factory under UID10001 and checks HTTP authentication, live
readiness changes and the built SPA over loopback.

For browser verification, build the Dockerfile's `web` target and run Vite in a
separate disposable VM108 container on guest loopback, port5178. Use host networking
with Vite explicitly bound to127.0.0.1; publishing a port on the isolated Docker
network did not work with the development VM's forwarding policy. No firewall
change is required. The browser harness runs on Forge through an SSH loopback
forward, with the application served by VM108:

```sh
# Forge: keep this foreground tunnel open while testing.
ssh -N -L 127.0.0.1:15178:127.0.0.1:5178 community-brain-dev
# In web/ on Forge:
CBM_DEV_BROWSER_URL=http://127.0.0.1:15178 npm run test:e2e
```

Browser API responses are synthetic route fixtures; the separate container
checker exercises the actual API/PostgreSQL/JetStream. No real OIDC sign-in,
Fathom acquisition or paid model request is implied by these tests. Remove only
the named rehearsal/browser containers and tunnel afterward; retain image/source
hashes, logs and safe result receipts for the production packet.

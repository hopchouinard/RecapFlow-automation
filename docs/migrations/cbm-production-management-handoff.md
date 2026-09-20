# Production management provisioning — authorized September 10, 2026

Patrick approved [this phase](cbm-production-phase-gate.md). Execute from the Mac
management environment using its existing operator access. No further routine
approval or transfer of management credentials to Forge is needed. Forge can
inspect infrastructure but cannot provision through `forge-infra-read`.

## Create the new target

- Recheck Home.servers inventory, IP ownership and Proxmox capacity. Candidate:
  **PVE1 VM 109, `community-brain-prod`, 10.1.30.21/24, VLAN 30**. The broker still
  returned nextid 109 at 01:07 UTC September 10; this is not a reservation.
- Use the verified Ubuntu cloud-image provisioning procedure used for VM 108:
  2 vCPU, 4 GiB RAM, 32 GiB OS + 64 GiB state, both on `local-lvm`. Verify the
  current image checksum and guest agent; do not blindly clone template 9000.
- Derive gateway, resolver and bridge from the existing VLAN 30 configuration.
  Create the matching address reservation and host DNS record
  `community-brain-prod.patchoutech.lab`. Keep application DNS separate:
  `community-brain.patchoutech.lab` uses the existing private Traefik ingress.
- Mount managed state persistently at `/srv/community-brain`; require the mount
  before Docker starts. Put Docker/containerd storage on the data disk as in the
  development host. Create private `files`, `config`, `corpus` directories for
  UID/GID 10001 and a separate root-owned build/artifact staging directory.
- Install Forge's existing public SSH identity under a scoped administration
  account with Docker/passwordless sudo access. Deliver a verified host key and
  configure the Forge alias `community-brain-prod`; do not copy private keys.
- SSH: only Forge 10.1.10.60 and the existing Mac administrator 10.1.50.219.
  Initially bind API to loopback. Before private Traefik ingress, restrict guest
  port 8090 to the actual proxy source and verify Docker forwarding rules too.
  Confirm the source address in management inventory rather than assuming it.
- Establish PBS backup and mount/reboot checks. Record backup identity, schedule,
  retention and disk alerts; an application VM backup does not include shared DB.

## Scoped platform resources

Provision only `community_brain_prod` on platform-db (10.1.10.50), with a separate
schema/migration owner and runtime login. The runtime role must not own the
database/schema or have DDL, superuser, role creation, or cross-application access.
After explicit Alembic migration, grant the runtime role DML and sequence use on
application objects. Set matching default privileges for the migration owner.
Check both allowed operations and denied DDL/cross-application access. Preserve
other applications' grants. Require verified TLS and record DB backup/PITR policy.
No new shared development database is needed for this staging phase.

On platform-events (10.1.10.54), create a separate production account and scoped
identity for `COMMUNITY_BRAIN_PROD`, subject `cbm.prod.jobs.stage.ready.v1`, durable
`community-brain-worker`. Review `jetstream.example.json` and
`consumer.example.json` against server limits. Allow only necessary scoped stream,
consumer, ACK and reply subjects; verify unrelated subjects are denied. Record
TLS/auth method and account quotas. No worker connects during API-only staging.

Use Infisical `homelab/prod`, `/applications/community-brain`, with separate API,
migration and future worker identities and source-IP/TTL restrictions. Render
root-owned private runtime files under `/etc/community-brain-production`, mode
0600 in a 0700 directory. Report paths and variable names only. Never print keys,
connection URLs containing passwords, raw tokens or rendered Compose environment.
The API bundle contains only its runtime DB URL, public OIDC settings and hashed
service identities. Migration DB credentials are delivered separately. Do not
onboard model, Fathom, Git or publisher credentials into the staging API.

Create a separate Authentik public SPA client for production, code flow + PKCE
S256, exact redirect `https://community-brain.patchoutech.lab/callback`, and exact
origin `https://community-brain.patchoutech.lab`. Record issuer/audience/JWKS and
client ID. Use `cb_scope=community-brain`. During staging grant Patrick only
`jobs:read`, `artifacts:read`, `retrieval:read`; no submit/retry/rerun/reconcile,
source upload or corpus publication. Restrict access to the intended user/group;
check nonmembership denial. Service probes use independent expiring read-only
identities; metrics identity gets only `metrics:read`. Raw probe tokens remain
private for scoped verification, not in the application environment.

Install the lab trust bundle, configure step-ca issuance/renewal and private
Traefik route, and record expiry/renewal checks. Do not create public Internet
ingress. Configure Kuma health and authenticated retrieval monitoring plus the
existing metrics/logging stack without request bodies or credentials in logs.

## Application continuation on Forge

Use standalone `deploy/community-brain/compose.production-staging.yml`, never
merge it with the worker candidate or root n8n Compose. Its mounts are read-only;
no worker or provider/publication secret is present. Public ingress remains held
until source restrictions and production claims have been verified.

Forge will freeze a reviewed source snapshot and record its file manifest/image
digest, build and smoke-test the image on VM 108, then load that immutable image
on the new guest. Source is currently uncommitted; preserve concurrent edits and
do not label the current development image as the production build. No Git push
or remote release is part of this handoff. Apply Alembic explicitly with the
migration identity, then remove it from the API runtime.

Initial data mapping: create an empty new jobs database; install the approved
1,901-row/87-session consumer candidate into the new corpus directory and copy
preserved configuration/registries without modification. Keep the full original
1,914-row archive and 13-row exclusion provenance privately. Legacy artifacts
remain preservation material; do not invent successful job attempts to display
them in the new UI. The initial jobs workspace will therefore be empty.

Candidate package on VM 108:
`/srv/dev-data/artifacts/cbm-preserved-corpus-rehearsal/consumer-candidate-v1/`.
Archive SHA-256:
`5e4f37d6459d820f506fe0b5d6d4db42204dcab26a3bb89592dd8f81fb9707fb`.
Verify every delivered hash, all 1,901 retained rows, schema 1.1, 768-dimensional
vectors, nomic-embed-text provenance and **1,901 indexed / 0 unindexed FTS rows**.
Compare authenticated retrieval with the freshly indexed development control.
No historical model processing or re-embedding is authorized here.

## Return a readiness receipt

Report VM ID/name/IP, SSH alias/account and verified host key, OS/image checksum,
state mount/ownership, Docker and reboot results, backup evidence, firewall and
Traefik source restrictions, public OIDC settings, private runtime file paths,
DB role/schema/TLS details, JetStream account/ACL checks, identity expiry/renewal,
and monitoring readiness. List unfinished checks explicitly. Do not include any
secret values. A ready guest may be handed back before all integrations finish so
Forge can continue independent build and staging work.

Do not change VM 101, old intake/Mac production sync, active workflows, Open WebUI
endpoint, live corpus, or consumer distribution. Cutover, remote publication,
service retirement and the later pgvector phase retain separate gates. The
explicit CBM-10 quality backlog remains the last step of the whole migration.

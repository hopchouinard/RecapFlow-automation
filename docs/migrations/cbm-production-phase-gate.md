# Production phase gate — approved 2026-09-10

Patrick explicitly approved production provisioning and staged deployment on
September 10: “yes I approve the phase transition.” This supersedes the older
preparation-only restrictions for the new production target. Cutover, remote
publication and service retirement remain separately gated.

Execution handoff: [production management provisioning](cbm-production-management-handoff.md).
Forge infrastructure access remains read-only; approval does not create a write
capability. VM109 is now provisioned and API staging acceptance is complete; see
`cbm-production-api-readiness.md` and the post-API management receipt. The original
plan below records the approved scope rather than current completion status.

## Evidence available

Real OIDC login, selected Fathom acquisition, weekly/backfill processing, scoped
Mac intake, authenticated artifact downloads, isolated indexing/retrieval,
development snapshot restore and the preserved 87-session corpus were exercised.
The approved consumer candidate retains all 1,901 successful rows unchanged and
records 13 divider-only exclusions; local package installation passed. Fresh full
corpus/control and filtered-candidate retrieval agree for four queries. Canonical
verification passed 150 Node, 887 Python, 23 DB/queue, one component and one browser
test, plus frontend build. This is not exhaustive production acceptance.

## Approved next phase: production provisioning and staged deployment

- Keep VM 108 as development. Candidate production VM: **PVE1 VM 109**, 2 vCPU,
  4 GiB RAM, 32 GiB OS + 64 GiB managed state on `local-lvm`.
- Candidate guest address **10.1.30.21 on VLAN 30**; candidate application hostname
  **community-brain.patchoutech.lab**. The public application DNS/ingress route
  should use the approved private Traefik path and lab CA; the guest API remains
  loopback or source-restricted behind that proxy.
- Read-only September 10 inspection: PVE1 had roughly 17.7 GiB unused RAM and
  336 GiB physically unused thin-pool space; `nextid` returned 109. No matching
  DHCP reservation or DNS entry was observed for the candidate address/name.
  These are advisory observations, not reservations or proof an offline static
  device cannot use that address. Management must recheck inventory before creation.
- Shared platform PostgreSQL/JetStream require separate application roles,
  identities and ACLs, following the deployment packet. Confirm backup/PITR,
  TLS and least-privilege denial checks. No shared service was changed here.
- New production Authentik client/claims and Infisical identities are required;
  do not promote short-lived development test tokens or the US$5 rehearsal key.
- Review and freeze the source revision, preserving concurrent repository edits,
  before building the production image. Current implementation remains local and
  uncommitted; no branch push/release has been performed. Build and validate the
  pinned image from the reviewed source, then stage application services with
  model execution, autonomous intake and remote publication disabled.
- Restore verified data into a new production target only after the import mapping
  and index policy are recorded. Do not fabricate historical job attempts. Verify
  full current-row FTS coverage; the preserved FTS metadata alone is insufficient.
  Candidate exclusions apply only as explicitly approved, with their provenance.
- Confirm production monitoring, backup/restore procedures, identity/certificate
  renewal, ingress and actual production-user login before any cutover proposal.

This phase authorizes scoped production resource creation and application
staging. Management provisioning remains necessary because Forge's infrastructure
broker is read-only; management credentials need not be transferred.

## Still held for a separate cutover checkpoint

No change to the current intake owner, Mac production sync, Open WebUI endpoint,
active n8n workflows, live production data, external corpus release, or old-service
retirement. Cutover requires final drift capture/sync, explicit destination/identity
verification, rollback checkpoint and authorization. Observe two successful weekly
cycles and restore evidence before considering retirement. CBM-09 remains separate;
CBM-10 and Q-01 through Q-05 remain the final migration-quality review.

Use [the deployment packet](cbm-07-deployment-packet.md) for operation order and
the newer rehearsal documents for current evidence. Approval of this gate does
not waive unresolved preflight checks or authorize broad platform changes.

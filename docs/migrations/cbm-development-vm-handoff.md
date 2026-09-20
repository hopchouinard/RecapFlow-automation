# Development VM handoff: ready

Patrick explicitly approved provisioning and Forge administration of this isolated
development VM on 2026-09-09. This supersedes the earlier inspection-only and
preparation-only restriction for **VM 108 only**. Production deployment and
cutover remain prohibited.

## Connect from Forge

```bash
ssh community-brain-dev
ssh community-brain-dev sudo -n id
ssh community-brain-dev docker compose version
```

This works now in the existing session. The SSH alias uses the dedicated key
`~/.ssh/community_brain_dev_ed25519`; no SSH agent or Proxmox write access is
needed. The remote user is `cbmdev`, with Docker access and passwordless sudo
on this VM. The key is limited to connections from Forge and is stored in
Infisical under `homelab/prod/development/community-brain-dev`; Forge holds its
private runtime copy. Do not put the key in Git or copy it into containers.

## Environment

- PVE1 VM 108, `community-brain-dev.patchoutech.lab`, `10.1.30.20`.
- Ubuntu 26.04.1 LTS, 2 vCPU, fixed 4 GiB RAM, onboot enabled.
- 32 GiB OS + 64 GiB ext4 development disk on local-lvm.
- Docker 29.1.3, Compose 2.40.3, Buildx, Git, rsync, Python venv and QEMU agent.
- `/srv/dev-data/workspaces` and `/srv/dev-data/artifacts` belong to `cbmdev`.
  Docker and containerd state live on that disk and require its mount at startup.
- Static IP on VLAN 30; matching DNS A record and DHCP reservation exist.
- SSH ingress is allowed from Forge and the existing Mac administrator address.
  Application ports should bind to guest loopback and be reached over SSH tunnels.
  Docker also blocks new forwarded connections from the guest NIC, including
  accidental all-interface publications. No public or Traefik route exists.

## Continue here

Keep the canonical source checkout and active work on Forge. Sync a build context
into `/srv/dev-data/workspaces` on the development VM, then perform the standalone
image boot rehearsal with disposable PostgreSQL and JetStream, health checks,
and authenticated API checks. One build/rehearsal at a time within the VM budget.
You are authorized to administer and deploy disposable development containers on
this VM. Preserve the repository's concurrent changes and use its accepted stack.

Use development fixtures only. Shared production databases, NATS streams, live
intake, n8n secret extraction, production publication, and cutover remain outside
this authorization. Real secrets remain Infisical-managed; no production
application credentials were transferred. No application stack is running yet.

## Completed operator checks

PVE1 SSD SMART passed. Switch uplink path permits VLAN 30; no switch or persistent
hypervisor network changes were needed. The guest uses a freshly downloaded,
checksum-verified official Ubuntu cloud image, not template 9000. Reboot passed:
cloud-init has zero warnings/errors, Docker/containerd/QEMU agent are active,
and no systemd units failed. Forge SSH, sudo, DNS, container startup and an HTTP
200 through an SSH tunnel were verified. Direct network access to the deliberately
published test container timed out. The test container was removed.

Baseline PBS backup `vm/108/2026-09-09T18:50:07Z` completed with guest-agent
freeze/thaw. No nightly schedule changed; a full restore was not tested.
Home.servers inventory/diagram were regenerated and all 293 tests passed.
The operator source and runbook live in agent-ops under
`platform-services/community-brain-dev/`. Infrastructure inspection continues
through `forge-infra-read`; the existing broker remains read-only.

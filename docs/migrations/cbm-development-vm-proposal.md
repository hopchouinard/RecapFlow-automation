# Development VM placement proposal

Initial telemetry: 2026-09-09T18:01:33Z. Direct broker inspection: 2026-09-09T18:26–18:27Z. Read-only; nothing provisioned or reserved.

## Evidence

Source: existing Prometheus at `http://10.1.10.30:9090`, Proxmox exporter job
`proxmox-cluster`. Samples were approximately 11 seconds old. Seven-day queries
contained 40,293 samples per node. These are sampled observations, not guaranteed
future capacity or physical disk health checks.

| Host | Logical CPUs | Current CPU | RAM total / used GiB | Seven-day peak RAM GiB | Seven-day peak CPU |
| --- | ---: | ---: | ---: | ---: | ---: |
| PVE1 | 12 | 1.6% | 30.77 / 8.73 | 8.92 | 10.4% |
| PVE2 | 4 | 6.2% | 15.40 / 12.40 | 15.04 | 91.4% |
| PVE3 | 4 | 15.7% | 31.22 / 25.09 | 26.53 | 85.7% |

PVE1 `local-lvm`: active LVM-thin, 347.9 GiB total and reported free.
PVE1 `pve-vm`: active local LVM, 3726.0 GiB total, 2662.5 GiB free.
`pbs`: shared backup storage, 1397.3 GiB free (same datastore shown per node;
do not add the three copies). Physical media type and thin-pool metadata health
are not exposed by these metrics.

Live guest metadata locates Forge as QEMU VM 105 on PVE3. VM 103 `docker-dev`
exists but is stopped; its data/purpose have not been inspected and it should
not be repurposed implicitly. PVE1 has stopped Ubuntu 26.04 cloud-init template
9000, a candidate after checking template configuration and currency.

Inventory source: `hopchouinard/home-servers`, `inventory/inventory.yaml` on main,
read through the GitHub connector. Its generated views/README are not fully
current (Forge is absent; docker-dev references disagree), so telemetry takes
precedence for observed runtime placement. Network inventory defines Services
as `10.1.30.0/24`. Forge currently uses `10.1.10.60/24`, gateway/DNS `10.1.10.1`.

## Proposed configuration

- Host PVE1; new QEMU VM `community-brain-dev`, hostname
  `community-brain-dev.patchoutech.lab`; candidate VM ID **108**, returned by
  `nextid` at inspection time. Recheck before allocation; it is not reserved.
- 2 vCPU, fixed 4 GiB RAM initially; one build/rehearsal at a time. Keep build
  concurrency bounded because PVE1 also hosts shared platform services.
- 32 GiB OS disk plus 64 GiB development-data disk on PVE1 `local-lvm`.
  Use ext4 for development data and place Docker/containerd state, build cache,
  and disposable application volumes there. Confirm runtime data-root paths.
  The larger `pve-vm` pool is an alternative if physical-media/operational policy
  favors it; current development capacity does not require it.
- One VirtIO NIC with proposed `bridge=vmbr0,tag=30`. PVE1 has active
  `vmbr0` on `nic0`; UniFi confirms Services VLAN 30 and gateway `10.1.30.1`.
  PVE1 VLAN transport remains unverified: the broker does not expose its switch
  port profile or full bridge VLAN settings. DNS `10.1.30.1` remains the proposed
  gateway resolver; custom DHCP DNS is disabled, and a guest DHCP/DNS test remains.
- Proposed IP `10.1.30.20/24`, with a DHCP reservation for the new unique MAC.
  Services dynamic range is `.50–.254`. No candidate IP/name matches appeared in
  the returned UniFi reservation/user, active-client or DNS records, or current
  Home.servers YAML. Offline undocumented static hosts remain possible; the IP
  is neither reserved nor proven unused.
- SSH from Forge and approved admin sources; initial application access through
  SSH forwarding with API bound to guest loopback. Later add the internal Traefik
  HTTPS route for browser/OIDC rehearsal. No public ingress or LAN DB/NATS ports.
- Disposable PostgreSQL and JetStream inside the development Compose project.
  No shared production databases, streams, secrets or intake.
- PBS may protect useful VM state after a scoped backup policy is set. Rebuildable
  caches/fixtures need not be treated as authoritative application backups.

Existing PVE1 non-template guest memory maxima total 24 GiB. Adding 4 GiB gives
28 GiB, leaving about 2.77 GiB outside those configured maxima for host overhead.
Adding the future production VM as well requires another capacity review; current
low usage is not an unlimited reservation.

## Direct inspection via approved broker

Read `forge-infrastructure-access.md` and
`/usr/local/share/forge-inspection/README.md`. All requested broker operations
succeeded. This resolves the earlier missing inspection-access question; no SSH
identity, credential copying, or permission change was needed.

- Nodes/resources reconfirmed PVE1: 12 logical CPUs, about 8.73 GiB RAM used of
  30.77 GiB. Node status identifies Ryzen 5 7430U, six physical cores, about
  22.0 GiB available RAM and zero swap use. PVE2/PVE3 remain more constrained.
- `storage pve1`: `local-lvm` enabled/active, 347.9 GiB available; `pve-vm`
  enabled/active, 2662.5 GiB available. `Fast` and `Main` are disabled/inactive,
  so neither is a candidate. PBS reports 1304.1 GiB available; the prior
  telemetry value was total minus used, not the API's allocatable availability.
- `lvmthin pve1`: VG `pve`, LV `data`, zero reported data use;
  metadata 18,661,297 / 3,808,428,032 bytes (0.49%). No capacity pressure is
  evident. This does not constitute a physical-disk/SMART health inspection.
- Template 9000 is a stopped QEMU template named `ubuntu-2604-cloudinit-template`,
  with 2 cores, 2 GiB RAM, QEMU agent enabled, VirtIO SCSI, serial console,
  3584 MiB root disk and cloud-init drive on `pve-vm`. Its NIC is untagged on
  `vmbr0`; the new VM must explicitly set its own MAC, VLAN and cloud-init values.
  No pending change was shown in the projected pending response. Template name
  and configuration do not verify disk contents, patch level or sanitization.
- UniFi returned 95 reservation/user records, 42 active clients and 29 explicit
  DNS records. Both client-local DNS fields and explicit DNS records were checked.
  None matched `10.1.30.20` or `community-brain-dev`. Existing n8n is `.30.10`.
- For comparison only, existing n8n VM 101 on PVE2 uses `vmbr0,tag=30` and is
  observed on Services. This validates the lab's convention, not PVE1's uplink.
- The Home.servers source YAML was re-read via GitHub; no candidate address/name
  was present. Inventory omissions are not proof that an offline static host
  does not exist.

## Remaining checks before provisioning

1. Confirm PVE1's switch uplink and bridge carry VLAN 30. The supported broker
   has no switch-port/bridge-VLAN detail operation; obtain this through the
   approved operator environment. Do not change the hypervisor network merely
   to make this proposal fit. If VLAN 30 is not carried, review the network
   change separately rather than silently placing development on Management.
2. Confirm template sanitization/provenance, or prepare a verified fresh Ubuntu
   cloud image instead. The current read-only projections cannot inspect its disk.
3. Check physical storage health through the operator environment, recheck the
   candidate IP/VM ID, and reserve them only as part of authorized provisioning.
4. At initial guest boot validate DHCP, internal DNS and permitted SSH routing;
   then run the disposable container rehearsal. No shared production dependencies.

VM provisioning is not authorized by the inspection-access installation. The
concrete candidate above is ready for review subject to these stated checks.

Queries used: `pve_node_info`, `pve_guest_info`, `pve_up`, `pve_storage_info`,
`pve_storage_shared`, `pve_cpu_usage_limit`, `pve_cpu_usage_ratio`,
`pve_memory_size_bytes`, `pve_memory_usage_bytes`, `pve_disk_size_bytes`,
`pve_disk_usage_bytes`, `time() - timestamp(pve_up)`, and seven-day
`max_over_time`, `avg_over_time`, `count_over_time` on node CPU/memory metrics.

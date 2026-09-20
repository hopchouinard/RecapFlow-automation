# Forge infrastructure access

Read `/usr/local/share/forge-inspection/README.md` before inspecting Proxmox,
UniFi, candidate VM capacity, bridges, templates, DHCP reservations or DNS.
That installed operator guide defines the supported commands and boundaries.

The executable is `/usr/local/bin/forge-infra-read`. Start with:

```bash
forge-infra-read pve nodes
forge-infra-read pve network pve1
forge-infra-read unifi networks
```

The broker is already running on Forge and works for Codex and Claude under
`t3code`, including an existing session. No SSH identities, connector, sudo,
or copied API tokens are needed. This access was verified on 2026-09-09.

Continue the inventory checks in `cbm-development-vm-proposal.md`. The access
setup does not provision that VM or authorize production deployment/cutover.
Application migration decisions and preservation evidence remain in
`forge-development-handoff.md`; its development work in progress was preserved.

The service reads Infisical-rendered credentials under a separate system account.
If a command fails, report its operation and error to the operator. Do not try to
recover credentials from protected runtime files or widen permissions.

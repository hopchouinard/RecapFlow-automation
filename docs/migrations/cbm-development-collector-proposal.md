# Development Mac collector: next intake rehearsal proposal

The selected real backfill and weekly paths have passed acquisition/processing,
artifact download, indexing and authenticated retrieval on VM 108. The remaining
live intake gap is the restricted Mac collector; chat arrived by manual attachment.

## Proposed access for approval

- Development backend: `https://community-brain-dev.patchoutech.lab`, using the
  existing VM 108 DNS identity and a lab-CA certificate. Terminate HTTPS through
  an explicitly approved development proxy path to VM loopback port 8090.
- Limit access to approved Mac/Forge addresses or the existing approved private
  ingress path; no public Internet exposure. The actual proxy/firewall placement
  must be reviewed before applying network configuration.
- Infisical-managed development identity with only `sources:upload:chat`, scope
  `community-brain-dev`, an explicit expiry and separate subject. Deliver the
  plaintext token only to the Mac collector; deliver its hash/permission record
  to the development API. Do not reuse the broad operator test token.
- One manually invoked upload of Patrick's selected September 8 chat from
  `~/Documents/Zoom`, using recording ID `181075701`. List/read/upload stay confined
  to that root with symlink/path checks. Do not install a timer, folder action,
  recurring poller or change the existing production sync target.
- Verify the uploaded source hash against the selected attachment, denial of
  transcript/alias uploads and other privileged API operations, and preservation
  of the original production intake owner. Upload alone must not launch model
  processing. No further model call is needed for this intake check.

The collector implementation currently requires a fixed HTTPS destination; do
not weaken it to accept plain HTTP just to reuse the browser tunnel. HTTPS ingress
and the collector identity have not been provisioned by this migration agent.
This proposal is a development integration gate, not production cutover approval.

After approval, the management environment must supply the selected proxy/CA
path and provision the scoped identity through Infisical. Prepare the exact Mac
invocation against that endpoint before asking Patrick to execute it. No management
credential or Mac SSH key needs to be transferred to Forge.

## Approved; infrastructure preparation completed

Patrick approved this scope. The proxy and manual upload runner are prepared;
Compose/nginx checks passed on VM 108. DNS and existing firewall source addresses
were verified. See [the exact management handoff](cbm-collector-management-handoff.md)
for certificate and Infisical delivery. Forge has no issuance/provisioning
credentials, so the endpoint and collector identity are not yet active. This is
a missing-access dependency, not another approval request.

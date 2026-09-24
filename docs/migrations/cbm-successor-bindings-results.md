# Request028 accepted — September 21, 2026

Forge verified and acknowledged Request028. The full development host/management
integration gap is closed for the recorded synthetic runs. Production activation,
protected real restoration and production readiness remain incomplete.

## Independent source and evidence checks

All 42 returned artifacts match their hashes and sizes. Forge independently read
all 50 members of the retained VM108 packet-v14 and verified its exact file set.
An independent build from the imported source reproduces its manifest bytes:
`c977c2a69c794141ef1c1bbf991ad7f44309ef172711e87d0806044679ad8b04`.
All nine boundary tests also pass locally. The seven Request028 containers are
currently stopped; only the four pre-existing development services are running.

The source from agent-ops commit
`6874753111c32bda26ea9f105dae4825ea10f9f8` is imported unchanged at
[`successor-development`](../../deploy/community-brain/successor-development/README.md).
Its upstream branch is codex/request028-successor, clean and not pushed at handoff.
The earlier Request027 implementation remains preserved. Original archives and
all safe receipts are retained in the
[evidence directory](receipts/cbm-successor-dev-20260921/receipt.md).

## What passed and what those results mean

- Real manual inspect/execute and automatic scan/tick subprocess chains completed
  two synthetic meetings. Thirteen artifact downloads matched hashes; 17 rows had
  complete FTS coverage. Prior work remained unchanged.
- Actual authenticated TLS-first NATS used scoped development stream, subject,
  inbox and credentials. Wrong credentials, absent trust and cross-profile
  bindings were rejected.
- Duplicate execution was refused. A third synthetic meeting stopped after one
  uncertain attempt and was not replayed. Holds, current boot ID, runner exclusion
  and completed-work checkpoint gating were exercised on disposable state only.
- A separate PostgreSQL restore matched durable state, 62 files matched, and
  stopped-volume WebUI restoration passed SQLite integrity checks. External
  signing/runtime material was captured privately. This is synthetic recovery
  evidence, not real-data or off-host disaster recovery acceptance.
- Actual Mac mutex/SSH quiet leases and Infisical renewal retained overlap after
  a lost acknowledgment, resumed the same generation, verified WebUI/Kuma/
  Prometheus and rejected five old tokens. Three API recreations preserved image,
  20 module/frontend hashes, six mounts, limits and exact hold/boot hashes.
- Eighteen worker-container records check image, network, limits, read-only packet
  and Python -B. All 14 sealed revisions remained exact without bytecode.

Manual success was first recorded on v6, automatic success on v9, uncertainty on
v10 and renewal on v13. Final v14 adds explicit production provider/file bindings.
The returned evidence establishes equivalent development environments, container
arguments, provider mapping and API/WebUI render, plus final held-launch checks.
It does not claim a new full execution on v14. Do not replay retained completed or
uncertain work to manufacture that claim. Any subsequent operational change must
receive fresh VM108 validation on isolated state before promotion.

## Remaining implementation and acceptance, in order

1. **Finish production activation implementation and validate it on VM108.** The
   production descriptor now binds mounts, resources, queue, provider credential
   files, boot entry and signing paths. But runtime_contract.load still admits
   only the development descriptor/hostname and production execution is disabled.
   This is a reviewable contract, not a deployable production launcher. Prepare
   controlled install/recreate/rollback with current authority and exact holds,
   including the existing API port owner, replacement serving restrictions and
   paired management/runtime source. Exercise that path in development first.
2. **Complete the protected restoration packet and acceptance.** Preserve the
   real WebUI volume and external signing key, obtain verified recovery points,
   restore into replacement-owned state, and verify user data, vectors, uploads,
   login/session continuity and disabled signup. Transfer remains a separately
   authorized phase; no real content or key was moved by Request028.
3. **Close capacity and real-provider/budget gates for the intended workload.**
   Synthetic providers and allowance replacements do not certify paid inference,
   Fathom acquisition, desktop intake, spending enforcement or production scale.
   Keep all required tests in development and within existing spending limits.
4. **Execute the controlled production phase only after acceptance and its
   authorization.** Installation, production renewal, traffic cutover and later
   processing/boot reconciliation remain separate from development success.
   Weekly-cycle evidence and retirement still follow; VM101 must not become a
   production dependency again.

The last returned production identity expiry is September22 at20:53:07 UTC and
the journal was completed. This deadline needs planning during activation work;
it is not permission to skip tests. The old API runtime and r020 bytecode hash
remain unchanged. Preserve the old exact-file-set failure as recovery evidence.

Previously approved chat.patchoutech.lab DNS/Traefik/Step CA work can proceed when
the replacement is ready without repeating that approval. Request028 changed no
production source, runtime, identities, holds, ingress, monitors or legacy state.

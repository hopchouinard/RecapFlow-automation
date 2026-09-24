# Fathom credential reuse handoff

## Authorization update, 2026-09-09

Patrick explicitly authorized reusing the existing n8n Fathom access and moving
its credential into Infisical for this acquisition rehearsal. This supersedes
the earlier requirement for a new development-only Fathom credential. It does
not authorize production cutover, remote publication, broad polling, or changes
to Fathom webhooks/account settings. No test recording has been selected yet.

## Secret authority and delivery

- Infisical project: `homelab` (`a508e594-7686-43a1-9b0f-cafa8b348ad4`).
- Environment: `development`.
- Path: `/applications/community-brain`.
- Key: `CB_FATHOM_API_KEY`.
- VM 108 private rendered copy: `/etc/community-brain-development/fathom.env`.
- Access: existing Forge `ssh community-brain-dev`, with `sudo -n`.

This is the **same credential as n8n**, not an independently scoped development
key. The dedicated Infisical environment does not narrow the provider's access.
Infisical is now authoritative for management/rotation. n8n retains its existing
encrypted operational copy; its workflow bindings and credential have not been
removed, rotated or converted to direct Infisical retrieval. Rotation must be
coordinated with n8n until that consumer is retired or migrated.

The management renderer read the persisted value back from Infisical and
verified delivery to a root-owned 0600 file under a root-owned 0700 directory.
No broad Infisical identity was installed on Forge or the guest. Use the rendered
copy through the existing approved delivery mechanism; do not attempt to obtain
management bootstrap credentials for direct Infisical access.

Management refresh command, run from the operator checkout with its existing
private `INFISICAL_ENV_FILE` configured:

```sh
bash platform-services/community-brain-dev/identity/run.sh render-fathom.py
```

That renderer reads Infisical only. `migrate-fathom.py` is the one-time selected
n8n credential import, not the normal refresh mechanism. It refuses to overwrite
a differing Infisical value. The decrypted export used transient container RAM
storage, removed after extraction; secret values were not printed or committed.

## Forge application steps

1. Read this handoff and `cbm-live-development-access.md`. Preserve the existing
   seven changed files and current development state.
2. In the separate live-development Compose configuration, pass
   `CB_FATHOM_API_KEY` only to the acquisition worker from the private file.
   For Compose interpolation, use both existing runtime and Fathom `--env-file`
   inputs with explicit per-service environment mappings. Do not expose this key
   to the API, SPA, Hermes, Mac collector, logs or repository. Validate with
   `docker compose config --quiet`, never dump resolved configuration.
3. Ask Patrick for one recording URL/ID, or its title/date. If needed, offer a
   short metadata-only candidate list in a narrow date range. Do not fetch a
   transcript or start an acquisition job until he chooses the recording.
4. Limit Fathom activity to meeting lookup and direct transcript retrieval for
   that recording. Do not create/delete webhooks, use asynchronous delivery
   callbacks, download media, enable recurring polling, or fetch unrelated calls.
5. Run the acquisition-only rehearsal into isolated development state. Keep
   workers stopped outside the explicit run and remote publication disabled.
   Credential reuse is not new approval to send a real transcript to OpenRouter;
   obtain explicit approval for that recording's model processing if needed.
6. Report recording identity/time match, acquisition result and output paths;
   never report the key or raw transcript content in chat.

## Evidence and limits

- Infisical write/read equality passed.
- Authenticated Fathom meeting metadata GET returned HTTP 200, with transcript
  and summary inclusion disabled; no transcript was fetched.
- Forge-to-VM access and root-owned 0600 key file verified.
- No paid model calls, worker startup, production modification or publication.
- Provider-enforced read-only/single-recording scope was **not** established.
  Fathom documents API keys as scoped to the creating user's accessible meetings;
  sharing this key shares that access. Read-only use here is the operational
  restriction above, not a claim about a narrower provider credential.

Source: [Fathom API key access](https://developers.fathom.ai/quickstart).

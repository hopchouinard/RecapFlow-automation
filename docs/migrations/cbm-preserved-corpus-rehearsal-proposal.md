# Next rehearsal: preserved production corpus, isolated on VM 108

**Approved by Patrick on 2026-09-10.** Routine implementation, isolated development
verification and follow-through do not require further approval. Ask only for
major changes, project phase transitions, or missing information/access. Production
deployment/cutover and remote publication remain prohibited.

The selected live backfill/weekly/collector paths and development snapshot restore
have passed. The remaining representative-data gap is restoration and retrieval
compatibility for the preserved production corpus and its registries/artifacts.

## Proposed scope requiring approval

Have the management environment extract a **data-only subset** of the verified
September 9 preservation copy into a private delivery archive for VM 108. Prefer
the existing Mac preservation copy at
`/Users/pchouinard/RecapFlow-backups/migration/2026-09-09-community-brain/`;
do not stop or modify live production services to make this rehearsal input.

Include only:

- The complete preserved LanceDB directory and its existing vector/FTS files.
- Matching nonsecret retrieval/ingestion config, speaker aliases and entity registry.
- Matching preserved output/historical Markdown and transcript artifacts needed
  to verify corpus provenance and downstream package compatibility.
- A manifest with preservation identity/time, paths, sizes and SHA-256 values,
  observed session count, schema and embedding model/dimensions. The original
  inventory observed 87 sessions; validate rather than force this count.

Exclude n8n databases, `.env`, encryption keys, private credentials, `.git`, agent
stores, SSH keys, executable runtime environments and WebUI databases. Do not copy
the whole preservation archive into development. Preserve the original archive.

Suggested delivery directory:
`/srv/dev-data/artifacts/cbm-preserved-corpus-rehearsal/`, mode 0700, files 0600.
No raw dataset should be copied into Forge, Git or chat. Report only delivery paths
and manifest verification. Management must report missing/ambiguous source paths
instead of synthesizing artifacts or editing corpus state.

## Execution once authorized and delivered

Restore into a separate disposable corpus/config/files area on VM 108. Preserve
the existing development corpora and serving API. Verify manifest hashes, schema,
sessions, dimensions and provenance, then test retrieval and build/reopen a local
consumer package. Query embeddings may use the already-retained Ollama endpoint;
no generation calls, re-extraction, re-embedding or source repair are included.

Keep model processing and network publication disabled. Do not import legacy
outputs as fabricated successful job attempts. Record discrepancies for reviewed
mapping/recovery work and keep CBM-10's semantic-quality review last. This scope
does not authorize production deployment, cutover, publication, retirement, new
shared-platform credentials or copying unrelated production data.

## Delivery dependency and prepared tools

On September 10 the approved data-only subset was not present on VM 108. Forge
has no reachable Mac execution channel; its existing SSH alias grants access to
VM 108 only, and the infrastructure broker cannot transfer preservation data.
Management delivery has been requested as an access dependency, not another
authorization gate. No credential transfer is needed.

Tools staged under the VM build context's
`deploy/community-brain/preserved-rehearsal/`:

- `verify_delivery.py`: validates every file hash/size, origin identifiers,
  manifest completeness, selected data paths, and absence of symlinks/path escape.
- `inspect_corpus.py`: opens LanceDB without repair, checks schema/FTS/counts,
  preserves the source delivery, and builds/reopens a local consumer package only
  if the retained strict export checks permit it. Non-success extraction records
  are reported as a package blocker, never removed or reprocessed automatically.

Suggested normalized delivery layout is `corpus/lancedb/nomic-v1/`, `config/`,
`output/`, `historical/`, plus `manifest.json`. Config is limited to known
nonsecret YAML registries/configuration and Markdown extraction prompts. The
manifest format expected by the prepared validator is:

```json
{
  "preservation_id": "2026-09-09-community-brain",
  "source_archive_manifest_sha256": "1d873beab28d5d9309dcc6ed74dda31431b6e354b9b436edf097cbc32c9876ba",
  "metadata": {"session_count": 87, "schema_version": "1.1", "embedding_model": "nomic-embed-text", "embedding_dimensions": 768},
  "files": [{"path": "config/speaker-aliases.yaml", "bytes": 0, "sha256": "REPLACE_WITH_ACTUAL_FILE_HASH"}]
}
```

The example size/hash and session count must be replaced with measured values;
include every delivered file except the manifest itself. Origin metadata alone
does not prove preservation integrity: management must verify the selected source
archive against the existing preserved manifest before extracting/copying it.
If management already prepared a different manifest/layout, report it and adapt
the validator to the actual verified delivery instead of redoing the transfer.

Sixteen credential-free validator tests passed; the new live corpus/package
inspection is prepared but cannot be validated against the preservation dataset
until it arrives. No production corpus or raw artifact was copied into Forge.

# Request030 protected restoration preparation

This directory prepares recovery mechanics and a bounded next phase. It does not
install a production runtime, enable production compilation, transfer private
production state, rotate identities, admit traffic or resume processing.

`recovery.py` provides capture, verification and independent restoration with
explicit scope. Its CLI accepts only the fresh Request030 VM108 workspace and
synthetic-development scope. The library's separate
`authorized-private-preservation` scope is a prepared interface for a later
explicitly authorized operator invocation; it is not an authorization source.
The production activation compiler/controller remain unchanged and disabled.

- Capture creates a new directory exclusively and writes intent before content.
  It records exact component roots, empty directories, file bytes/hashes,
  uid/gid/mode/mtime, and contained relative links. Original paths remain private.
- Files with multiple hard links, special files, privileged modes, escaping,
  absolute or dangling links, overlapping components and linked destination
  ancestors are refused. Supported links must resolve to a manifest member;
  links through another linked directory are conservatively refused.
- Each file is observed through a non-following descriptor; identity/stat drift
  and a changed complete tree fail the attempt. This is a drift detector, not a
  substitute for excluding writers throughout the capture interval.
- `quiet()` opens existing locks without creating or replacing them. The caller
  supplies the reviewed order. Holds retain their bytes, uid/gid/mode/inode/device.
  No process, worker, boot, checkpoint or restart action exists in the primitive.
- Restore requires an externally pinned manifest hash, exact bundle/blob sets,
  scope agreement and a fresh destination. It verifies every component after
  restoring numeric ownership and modes. Failed/partial targets are retained;
  never repeat a mutation against them. Completion files and directory entries
  are fsynced. Readback/verification is the only retry against the same attempt.
- Private manifests and blobs remain behind a mode0700 outer directory; blobs and
  journals are0600. Restored inner permissions match the original, including0755
  public subtrees. They never override the private outer boundary. ACLs/xattrs,
  sparse allocation and original hard-link identity are outside this version;
  preflight must reject sources requiring those features, not silently discard
  them. File reads currently buffer one file in memory; a later private operation
  must bound the largest file against available memory before using this version.

`pg_fence.py` tests an exported PostgreSQL snapshot under SHARE locks on the
complete reviewed table set. The synthetic attempted concurrent write must time
out. The fence stays alive through dump and file capture and rolls back on exit.
It refuses hosts/container names outside Request030 development. The future
operator procedure uses the equivalent native PostgreSQL commands under the
existing database administrator, without copying a database password.

`rehearse.py` uses fresh, network-none PostgreSQL containers and a synthetic state
pair. It restores into a different PostgreSQL server and compares canonical table
row digests, unknown attempts, outbox state, relationships and FTS behavior. Its
small fixture is not the production schema, actual LanceDB/Chroma acceptance, or
a full workload capacity result. `webui_session.py` tests the pinned real WebUI
image through its HTTP API using new synthetic accounts, signing material and
chat data. It explicitly reports that no rendered browser or real user session
was tested. Containers stop in cleanup; volumes, data and attempts remain.

`contract.py` maps the actual new receipt to Request029's requirements without
filling slots. The older compiler expects `packet_manifest`, `restored_files`,
`database.sql`, tar files and legacy observations. The new schema cannot be
renamed into that schema. A production validator remains separate reviewed work.
`private-manifest.schema.json` describes the actual private manifest. Database,
application, off-host, browser, capacity and provider results are separate pinned
receipts, never inferred from the tree comparison.

`indexing_budget.py` is an unchanged copy of the inherited production helper,
SHA256 `932e46c9cfb892c9b6eb51506f5948e8718795ee0f4f16a9ea6e860619bf6db7`.
Its tests use synthetic transports. No external allowance query or paid model call
runs here. Its fixed US$5 weekly allowance is a production contract, not a grant
to spend development funds.

Mac unit fixtures stub the Linux extended-metadata observation because Apple
provenance metadata is outside this Linux restore contract. VM108 tests exercise
the real extended-metadata check. Native Mac preservation needs a separately
reviewed metadata-preserving archive; it is not certified by those unit tests.

Run local boundaries with `python3 -B -m unittest discover -p 'test_*.py' -v`.
VM fixtures are single-use entry points, not idempotent setup commands. Inspect
retained outcomes instead of rerunning them. Consult the delivered provenance and
verification receipts for the exact source revision used by each attempt.

See `OPERATOR-PROPOSAL.md` for private bindings, commands, gates and retention;
`ACCEPTANCE-PLAN.md` separates synthetic results from later acceptance.

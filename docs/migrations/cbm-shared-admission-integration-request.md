# Request032: finish common admission and database validation in development

ID: CBM-SHARED-ADMISSION-20260921-032. Target: home.servers.
Deadline:2026-09-22T16:00:00Z. Request031 is consumed and acknowledged.

Patrick instructed proceeding with the next task. Existing Mac administration,
read-only production inspection, synthetic VM108 administration and relay are
available. No production installation/maintenance/renewal/rotation/capture/transfer,
private signing/data copy, cutover/resume, VM resize or paid-provider work is
requested. Preserve VM101 recovery and its unrelated services. Expiry is not an
exception to authorization. Do not renew production identities for this request.

Forge supplies its VM108-tested shared admission core and evidence. Import exact
bytes with lineage; integrate outside immutable Request029/031 and Forge sources.
This is a library with a synthetic readback fixture, not an installed adapter.

1. Implement one candidate admission path used by the actual scheduler, manual
   management and capture entry points, using the existing Mac mutex and a shared
   durable journal. Integrate a copy of the actual installed scheduler source;
   do not install into production. Detect prior activation/request031/manual
   unresolved state before dispatch; never silently migrate/clear it. Bind owner,
   operation/source/target/hold/incumbent identities. Preserve pending state when
   callers or transport die. Authenticate readback from the target and verify
   current identity and boot/finalizer state rather than supplying fixture flags.
2. Exercise actual entry points on fresh synthetic VM108 services. A killed capture
   caller must block scheduler/manual dispatch; safe authoritative recovery may
   allow a new operation but never replay the old effect. Test legacy pending
   conflicts, competing processes and stale/foreign/tampered readback. Resolve
   Request031's missing reboot/startup reconciliation and failed-finalizer handling:
   implement fail-closed boot reconciliation and prove startup ordering with
   isolated fixtures. Do not reboot the shared dev VM or alter its baseline stack
   merely to run this test. Clearly distinguish startup-path tests from an actual
   VM reboot, and retain any limitation; never claim unconditional availability.
3. Extend the database evidence contract using production-shaped synthetic state:
   multiple application schemas, extensions, roles/membership/ACL/default ACLs,
   schema/table/sequence definitions and values, writer admission, file/component
   membership and signing/volume/version identities. Bind independent restored
   server and exact dump/source observations. Use actual PostgreSQL18.6 isolated
   servers, retain unknown outcomes and test missing/extra/changed permissions,
   DDL/sequence writers and concurrent clients. A SHARE table lock alone is not
   writer exclusion. Record supported catalog coverage and reject unsupported
   object classes; do not infer complete production coverage from fixture equality.
4. Resolve the five native Mac fixture metadata errors with an explicit synthetic
   fixture runner if needed. Do not suppress production metadata rejection or
   edit imported Forge bytes. Distinguish platform fixture adaptation from proof
   that arbitrary Mac metadata can be preserved.

Return the final exact source archive/manifest/commit (no push), VM108 byte parity,
positive/negative receipts from final source, pending/retention dispositions and
an updated concrete operator plan. Keep all21 production slots null and existing
production compiler/controller refusals. Name any remaining code gap precisely;
if ready, provide an immutable proposal for the next necessary production phase,
with owner, bindings, private destination, maintenance/recovery deadline and rollback.
No private content/signing material in the relay or ordinary development fixtures.

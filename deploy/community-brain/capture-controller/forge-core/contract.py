"""Evidence mapping only; never fills a production slot from development data."""
import json
from pathlib import Path

PROOFS={
'protected_database_restore_and_durable_state_comparison':'Pinned dump plus canonical schema/table/sequence/relationship observations from an independent restored database; holds and unknown outcomes unchanged.',
'protected_corpus_vectors_uploads_and_artifact_hash_comparison':'Pinned exact file and empty-directory manifests, LanceDB/FTS schema/count/query and DB-to-file referential checks without regeneration.',
'restored_external_webui_volume_identity_and_sqlite_integrity':'Pinned restored volume identity and SQLite integrity/relationships plus upload and Chroma observations.',
'external_signing_material_preservation_and_session_continuity':'Private original signing digest and authorized staged deployment using that key; existing real session accepted and wrong key rejected.',
'paired_off_host_recovery_copy_and_verified_restore_receipt':'Receiver-verified off-host component hashes and an actual independent restore from that off-host copy.',
'login_existing_sessions_and_disabled_signup_browser_acceptance':'Rendered browser sign-in, retained content and disabled signup using intended real identity on the staged replacement.',
'intended_workload_capacity_acceptance':'Measured concurrent API, WebUI, worker and restore workload with approved headroom and latency.',
'real_provider_and_spending_budget_acceptance':'Scoped dev provider identities, bounded allowance, real request/response and unknown-outcome receipts; production keys excluded.'}


def reconcile(template, receipt):
    if template.get('deployable') is not False or template.get('production_execution_enabled') is not False:
        raise ValueError('production template must remain disabled')
    if any(v is not None for v in template['required_evidence'].values()):
        raise ValueError('preparation must not prefill production evidence')
    if receipt.get('schema')!='cbm.restore-receipt/1' or receipt.get('scope')!='synthetic-development' or receipt.get('production_qualified') is not False:
        raise ValueError('unexpected preparation receipt')
    return {'schema':'cbm.preparation-reconciliation/1','production_compilation_enabled':False,
            'legacy_schema_compatible':False,'adapter_installed':False,
            'reason':'Request029 evidence_files expects flat restored_files, packet_manifest, database.sql, state.tar, private-runtime.tar, webui.tar and legacy database observations. Request030 binds content-addressed components and separate observations. No automatic conversion or true-flag substitution is valid.',
            'missing_slots':list(template['required_evidence']),
            'recovery_slot_requirements':PROOFS,
            'development_receipt_capture_id':receipt['capture_id'],
            'development_receipt_manifest_sha256':receipt['manifest_sha256'],
            'remaining_compiler_work':'A separately reviewed production-only validator must verify immutable private component manifests, exact sets and reference hashes, independent observations, scope/authorization/expiry, current holds and volume identities. Keep compile_plan and controller production refusals until all 21 slots pass.'}

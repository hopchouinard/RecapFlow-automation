"""Request034 production admission review core; no installer or executor.

This module can reject a proposed later production plan. It cannot authorize,
install, or perform one. An external, reviewed hash and live observations are
required inputs; development receipts never fill production evidence slots.
"""
import hashlib
import json
import re
from pathlib import Path

CONTRACT = Path(__file__).with_name('production-contract.json')
SLOTS = (
 'separate_production_phase_authorization',
 'reviewed_source_commit_and_archive_sha256',
 'sealed_runtime_packet_path_and_exact_manifest_sha256',
 'paired_mac_management_source_and_manifest_sha256',
 'current_authority_generation_and_expiry_metadata',
 'all_compose_environment_ca_and_signing_file_hashes',
 'current_paused_attention_boot_hash_mode_inode_device',
 'runner_manual_submission_lock_inode_device',
 'exact_incumbent_api_id_image_config_fingerprint_and_health',
 'legacy_webui_serving_and_volume_ownership_disposition',
 'protected_database_restore_and_durable_state_comparison',
 'protected_corpus_vectors_uploads_and_artifact_hash_comparison',
 'restored_external_webui_volume_identity_and_sqlite_integrity',
 'external_signing_material_preservation_and_session_continuity',
 'paired_off_host_recovery_copy_and_verified_restore_receipt',
 'login_existing_sessions_and_disabled_signup_browser_acceptance',
 'intended_workload_capacity_acceptance',
 'real_provider_and_spending_budget_acceptance',
 'fresh_auth_api_filter_kuma_prometheus_acceptance',
 'deployed_scheduler_pending_activation_interlock',
 'explicit_acceptance_deadline_and_rollback_owner',
)
HEX = re.compile(r'^[0-9a-f]{64}$')

def digest(raw): return hashlib.sha256(raw).hexdigest()

def exact_file(path, expected):
 p = Path(path)
 if not HEX.fullmatch(expected) or p.is_symlink() or not p.is_file():
  raise ValueError('unsealed or linked member')
 raw=p.read_bytes()
 if digest(raw)!=expected:raise ValueError('source or receipt drift')
 return raw

def exact_tree(root, manifest_path, manifest_digest):
 root=Path(root);manifest=Path(manifest_path)
 if root.is_symlink() or not root.is_dir() or manifest.is_symlink():raise ValueError('linked source')
 entries=json.loads(exact_file(manifest,manifest_digest))
 if not isinstance(entries,dict) or not entries:raise ValueError('empty source manifest')
 expected={Path(name) for name in entries}
 if any(p.is_absolute() or '..' in p.parts or str(p) in ('.','') for p in expected):raise ValueError('unsafe source member')
 actual={p.relative_to(root) for p in root.rglob('*') if p.is_file() or p.is_symlink()}
 if actual!=expected:raise ValueError('source member drift')
 for name,sha in entries.items():exact_file(root/name,sha)
 return len(entries)

def review(plan, authority, observed, evidence, *, now, reviewed_plan_sha256):
 """Pure fail-closed admission review, never an execution approval."""
 raw=(json.dumps(plan,sort_keys=True,separators=(',',':'))+'\n').encode()
 if digest(raw)!=reviewed_plan_sha256:raise ValueError('plan was not externally reviewed')
 if plan.get('phase')!='protected-preservation' or plan.get('target')!='community-brain-prod':
  raise ValueError('wrong phase or target')
 authorization=plan.get('authorization',{})
 if authorization.get('scope')!='separate-production-phase' or not authorization.get('id'):
  raise ValueError('missing separate authorization')
 deadline=plan.get('acceptance_deadline_epoch')
 if not isinstance(deadline,(int,float)) or isinstance(deadline,bool) or not now<deadline<=now+7200:
  raise ValueError('expired or unbounded admission')
 if authorization.get('expires_epoch',0)<deadline:raise ValueError('authorization expires before deadline')
 if authority.get('environment')!='production' or authority.get('readback') is not True or authority.get('expires_epoch',0)<deadline+300:
  raise ValueError('current production authority unavailable or expired')
 c=json.loads(CONTRACT.read_text())
 for key in ('machine_id','incumbent_id','incumbent_image'):
  if observed.get(key)!=c[key] or plan.get(key)!=c[key]:raise ValueError('exact host or incumbent changed')
 if observed.get('mount_uuid')!=c['state_mount']['uuid'] or plan.get('mount_uuid')!=c['state_mount']['uuid']:
  raise ValueError('state mount changed')
 if observed.get('holds')!=plan.get('holds') or not isinstance(plan.get('holds'),dict) or set(plan['holds'])!={'paused','attention','boot'}:
  raise ValueError('processing holds changed')
 if observed.get('locks')!=plan.get('locks') or not isinstance(plan.get('locks'),dict) or set(plan['locks'])!={'runner','manual','submission'}:
  raise ValueError('writer locks changed')
 if set(evidence)!=set(SLOTS):raise ValueError('all 21 evidence slots required')
 for slot in SLOTS:
  item=evidence[slot]
  if not isinstance(item,dict) or item.get('scope')!='production' or item.get('accepted') is not True or not HEX.fullmatch(item.get('receipt_sha256','')):
   raise ValueError('unaccepted or nonproduction evidence: '+slot)
 if plan.get('production_execution_enabled') is not False:
  raise ValueError('Request034 cannot enable production')
 return {'schema':'cbm.stage2-admission-review/1','evidence_slots':21,'phase_reviewed':True,
         'production_execution_enabled':False,'installer_available':False,'controller_available':False}

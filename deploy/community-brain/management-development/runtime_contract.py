"""One successor descriptor for API, worker image, boot and recovery controls.

Processing stays held in Request027. No caller may clear holds or use the old
r020 launcher as a fallback. This module is not installed on production.
"""
import hashlib
import json
from pathlib import Path
from successor import validate,verify,API_IMAGE,DEV_ROOT

PACKET=Path(__file__).resolve().parent

def load(expected):
 verify(PACKET,expected)
 value=json.loads((PACKET/'descriptor.json').read_text());validate(value)
 for name,item in value['helper_files'].items():
  raw=(PACKET/name).read_bytes();assert len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256']
 provenance=json.loads((PACKET/'worker-helper-provenance.json').read_text())
 for name,item in provenance.items():assert hashlib.sha256((PACKET/'workers'/name).read_bytes()).hexdigest()==item['candidate_sha256']
 assert value['worker_image']==value['api_image']==API_IMAGE
 assert value['boot_launcher']==str(PACKET/'automatic_host.py')
 assert value['recovery_images']==sorted(set([value['api_image'],value['webui_image'],value['postgres_image'],*value['monitor_images'].values()]))
 return value

def held(value):
 root=Path(value['holds_root'])/'automation'
 boot=json.loads((root/'boot-state.json').read_text())
 return (root/'paused').exists() or (root/'attention.json').exists() or not boot.get('reconciled',False)

def controls(value):
 return {'api_image':value['api_image'],'worker_image':value['worker_image'],
 'boot_launcher':value['boot_launcher'],'worker_host':str(PACKET/'workers/manual_host.py'),'indexing_audit_helper':str(PACKET/'workers/indexing_budget.py'),'module_source':value['module_source'],
 'frontend_source':value['frontend_source'],'recovery_images':value['recovery_images'],
 'recovery_private_paths':[str(Path(DEV_ROOT)/'state'),str(Path(DEV_ROOT)/'private'),
                         'docker-volume:cbm-r027_webui','docker-volume:cbm-r027_pg','docker-volume:cbm-r027_kuma'],
 'management_source_files':sorted(json.loads((PACKET/'packet-manifest.json').read_text())),
 'external_signing_environment':value['external_signing_environment'],
 'processing_held':held(value),'production_activation_allowed':False}

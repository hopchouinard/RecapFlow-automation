"""Explicit fixed profiles. Production is a review artifact, never a dev override."""
from pathlib import Path
import copy
import re

API_IMAGE='sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b'
WEBUI_IMAGE='sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b'
DEV_ROOT='/srv/dev-data/workspaces/cbm-stage2-qualification-20260923-034'
DEV_HOST='pchouinard@10.1.30.20'


def profile(name,revision="packet-v1"):
 if not re.fullmatch(r"packet-v[1-9][0-9]*",revision):raise ValueError("invalid immutable revision")
 if name not in ('development','production'):raise ValueError('explicit known profile required')
 dev=name=='development'
 root=DEV_ROOT+'/state' if dev else '/srv/community-brain'
 private=DEV_ROOT+'/private' if dev else '/etc/community-brain-production'
 packet=DEV_ROOT+'/'+revision if dev else '/srv/community-brain/workspaces/cbm-successor-20260923-034/'+revision
 queue={'url':'tls://nats:4222' if dev else 'tls://platform-events.patchoutech.lab:4223',
        'stream':'CBM_REQUEST034' if dev else 'COMMUNITY_BRAIN_PROD',
        'subject':'cbm.dev.request034.jobs.stage.ready.v1' if dev else 'cbm.prod.jobs.stage.ready.v1',
        'inbox':'_INBOX.cbm_request034_worker' if dev else '_INBOX.cbm_prod_worker',
        'consumer':'community-brain-worker','tls_handshake_first':True,
        'ca_file':'/run/certs/queue-ca.pem' if dev else '/run/certs/ca-bundle.pem',
        'authority_path':'/development/community-brain-dev/request034' if dev else '/applications/community-brain',
        'credential_keys':['CB_NATS_USER','CB_NATS_PASSWORD']}
 mounts=[{'source':root+'/files','target':'/state/files','read_only':False},
         {'source':root+'/config','target':'/state/config','read_only':True},
         {'source':root+'/corpus','target':'/state/corpus','read_only':True},
         {'source':root+('/meeting-archive' if dev else '/meeting-archive-20260910'),'target':'/state/meeting-archive','read_only':True},
         {'source':root+'/automation-public','target':'/state/automation-public','read_only':True},
         {'source':private+'/ca-bundle.pem' if dev else '/etc/ssl/certs/ca-certificates.crt','target':'/run/certs/ca-bundle.pem','read_only':True}]
 return {'schema':2,'request_id':'CBM-STAGE2-QUALIFICATION-20260923-034','profile':name,'revision':revision,
  'host':DEV_HOST if dev else 'pchouinard@10.1.30.21','hostname':'community-brain-dev' if dev else 'community-brain-prod',
  'execution_allowed':dev,'root':root,'private':private,'packet':packet,
  'compose_project':'cbm-r034' if dev else 'community-brain-successor',
  'network':'cbm-r034_default' if dev else 'community-brain-production-staging_default',
  'api_container':'cbm-r034-api' if dev else 'community-brain-successor-api',
  'webui_container':'cbm-r034-webui' if dev else 'community-brain-successor-webui',
  'api_image':API_IMAGE,'worker_image':API_IMAGE,'webui_image':WEBUI_IMAGE,
  'api_mounts':mounts,'queue':queue,'api_memory':2147483648,'api_cpus':2,
  'worker_memory':1572864000,'worker_cpus':2,'webui_memory':1610612736,'webui_cpus':1.5,
  'retrieval_url':'http://api:8090/retrieval/query',
  'api_environment':private+'/api.env','signing_environment':private+'/webui.env',
  'webui_data':'cbm-r034_webui' if dev else 'community-brain-successor-webui',
  'database_authority_key':'CB_RUNTIME_DATABASE_URL',
  'module_source':'pinned-image','frontend_source':'pinned-image',
  'python':['python','-B'],'host_python':['python3','-B'],
  'boot_launcher':packet+'/workers/automatic_host.py',
  'provider_mode':'synthetic' if dev else 'budgeted-external',
  'provider':{'ollama_url':'http://provider:8999' if dev else 'http://10.1.50.219:11434',
    'command':['python','-B','/packet/fixture/synthetic_worker.py' if dev else '/packet/workers/manual_worker.py','execute'],
    'acquisition_file':'provider.env' if dev else 'acquisition.env',
    'model_file':'provider.env' if dev else 'bounded-model.env',
    'acquisition_key':'CB_SYNTHETIC_PROVIDER_TOKEN' if dev else 'CB_FATHOM_API_KEY',
    'model_key':'CB_SYNTHETIC_PROVIDER_TOKEN' if dev else 'CB_OPENROUTER_API_KEY'},
  'runtime_evidence':DEV_ROOT+'/runtime-evidence' if dev else root+'/automation/runtime-evidence',
  'network_publication':False,'automatic_resume':False,
  'recovery_paths':[root+'/files',root+'/config',root+'/corpus',mounts[3]['source'],root+'/automation',root+'/automation-public',root+'/manual-approvals',private,packet],
  'recovery_components':['paired PostgreSQL snapshot','API/worker/WebUI images','WebUI volume','external signing key','authority journal and consumer state','management code and boot controls'],
  'production_promotion_ready':False}


def validate(value):
 expected=profile(value.get('profile'),value.get('revision'))
 if any(value.get(k)!=v for k,v in expected.items()):raise ValueError('profile contract changed')
 return value


def development(value):
 validate(value)
 if value['profile']!='development' or not value['execution_allowed']:raise ValueError('production execution not authorized')
 return value


def render(value):
 validate(value)
 mounts=[{'type':'bind','source':m['source'],'target':m['target'],'read_only':m['read_only']} for m in value['api_mounts']]
 api={'container_name':value['api_container'],'image':value['api_image'],'read_only':True,'user':'10001:10001',
 'cap_drop':['ALL'],'security_opt':['no-new-privileges:true'],'tmpfs':['/tmp:uid=10001,gid=10001'],
 'env_file':[value['api_environment']],'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'volumes':mounts,
 'mem_limit':value['api_memory'],'cpus':value['api_cpus'],
 'command':['python','-B','-m','uvicorn','community_brain.jobs.runtime:app','--factory','--host','0.0.0.0','--port','8090','--no-access-log']}
 webui={'container_name':value['webui_container'],'image':value['webui_image'],'env_file':[value['signing_environment']],
 'volumes':['webui:/app/backend/data'],'mem_limit':value['webui_memory'],'cpus':value['webui_cpus'],
 'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'cap_drop':['ALL'],'security_opt':['no-new-privileges:true']}
 if value['profile']=='production':
  api['ports']=['10.1.30.21:8090:8090'];webui['ports']=['10.1.30.21:3000:8080']
 network={'internal':True} if value['profile']=='development' else {'external':True,'name':value['network']}
 return {'name':value['compose_project'],'services':{'api':api,'webui':webui},'networks':{'default':network},'volumes':{'webui':{'name':value['webui_data']}}}


def provider_plan(value,stage):
 validate(value)
 if stage not in ('acquisition','processing','indexing'):raise ValueError('unknown selected stage')
 p=value['provider'];acquisition=stage=='acquisition'
 return {'file':p['acquisition_file' if acquisition else 'model_file'],
         'key':p['acquisition_key' if acquisition else 'model_key'],
         'environment_key':'CB_FATHOM_API_KEY' if acquisition else 'CB_OPENROUTER_API_KEY',
         'command':p['command'],'ollama_url':p['ollama_url']}

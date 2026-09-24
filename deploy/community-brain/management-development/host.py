"""VM108 candidate host adapter. Payloads arrive on SSH stdin; never argv."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import secrets
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from successor import API_IMAGE, DEV_ROOT, render, verify

ROOT=Path(DEV_ROOT)
PACKET=Path(__file__).resolve().parent
PRIVATE=ROOT/'private'
COMPOSE=['docker','compose','-f',str(ROOT/'compose.json')]
OPENER=urllib.request.build_opener(urllib.request.ProxyHandler({}))

def command(args, payload=None, timeout=180):
 p=subprocess.run(args,input=None if payload is None else json.dumps(payload),capture_output=True,text=True,timeout=timeout)
 if p.returncode:raise RuntimeError('development command failed: '+args[0]+'; private output suppressed')
 return p.stdout.strip()

def atomic(path,value,mode=0o600):
 path.parent.mkdir(mode=0o700,parents=True,exist_ok=True)
 temp=path.with_name('.'+path.name+'.tmp');temp.write_text(value);temp.chmod(mode);temp.replace(path)

def container(service):return command(COMPOSE+['ps','-aq',service])
def address(service,port):
 row=json.loads(command(['docker','inspect',container(service)]))[0]
 net=row['NetworkSettings']['Networks'];assert set(net)=={'cbm-r027_default'}
 return 'http://'+net['cbm-r027_default']['IPAddress']+':'+str(port)

def call(path,token=None,body=None):
 h={'Content-Type':'application/json'}
 if token:h['Authorization']='Bearer '+token
 req=urllib.request.Request(address('api',8090)+path,headers=h,data=None if body is None else json.dumps(body).encode())
 try:
  with OPENER.open(req,timeout=30) as r:return r.status,r.read() if path=='/metrics' else json.load(r)
 except urllib.error.HTTPError as e:return e.code,json.load(e)

def ready_api():
 for _ in range(90):
  try:
   if call('/health')[0]==200:return
  except (OSError,ValueError):pass
  time.sleep(1)
 raise RuntimeError('development API readiness timeout')

def lib():
 spec=importlib.util.spec_from_file_location('rehearse',PACKET/'fixture/rehearse.py')
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 m.ROOT=ROOT;m.SOURCE=PACKET/'fixture';m.WEBUI=container('webui');m.BASE=address('webui',8080)
 m.RETRIEVAL='http://api:8090/retrieval/query';m.call.__defaults__=(None,None,m.BASE)
 return m

def environment(values):
 env={'CB_DATABASE_URL':'postgresql+psycopg://fixture@pg/integration','CB_STORAGE_ROOT':'/state/files',
 'CB_PIPELINE_CONFIG_DIR':'/state/config','COMMUNITY_BRAIN_CONFIG_DIR':'/state/config',
 'CB_CORPUS_ROOT':'/state/corpus','LANCEDB_PATH':'/state/corpus/lancedb/nomic-v1',
 'CB_CORPUS_SCOPE':'community-brain','CB_OIDC_ISSUER':'https://fixture.invalid','CB_OIDC_AUDIENCE':'fixture',
 'CB_OIDC_CLIENT_ID':'fixture','CB_OIDC_JWKS_URL':'https://fixture.invalid/jwks',
 'CB_SERVICE_IDENTITIES':values['CB_SERVICE_IDENTITIES'],'CB_ENABLE_RETRIEVAL':'true',
 'COMMUNITY_BRAIN_DISTRIBUTION_MODE':'true','OLLAMA_BASE_URL':'http://provider:8999',
 'CB_ENABLE_MODEL_CALLS':'false','CB_ENABLE_NETWORK_PUBLICATION':'false','CB_AUTOMATIC_PROCESSING':'true','CB_AUTOMATION_ROOT':'/state/automation',
 'CB_WEB_DIST':'/app/web/dist'}
 assert all("'" not in x and '\n' not in x for x in env.values())
 atomic(PRIVATE/'api.env',''.join(k+"='"+v+"'\n" for k,v in env.items()))

def holds():
 return {n:hashlib.sha256((ROOT/'state'/n).read_bytes()).hexdigest() for n in
 ['automation/paused','automation/attention.json','automation/boot-state.json']}

def inspect_runtime():
 value=json.loads((PACKET/'descriptor.json').read_text())
 row=json.loads(command(['docker','inspect',container('api')]))[0]
 assert row['Image']==API_IMAGE
 assert not any('/site-packages/' in m['Destination'] or m['Destination']=='/app/web/dist' for m in row['Mounts'])
 code="import sys,json,pathlib,hashlib;d=json.load(sys.stdin);assert all(pathlib.Path(p).stat().st_size==s['bytes'] and hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()==s['sha256'] for p,s in d.items());print(json.dumps({'verified_files':len(d)}))"
 proof=json.loads(command(['docker','exec','-i',container('api'),'python','-B','-c',code],value['image_files']))
 return {'image':row['Image'],'no_old_overlays':True,**proof,'holds':holds()}

def setup(values):
 assert not PRIVATE.exists(),'existing private state: reconcile; no replay'
 PRIVATE.mkdir(mode=0o700)
 environment(values)
 credentials={'email':'request027@example.invalid','password':secrets.token_urlsafe(32)}
 atomic(PRIVATE/'credentials.json',json.dumps(credentials))
 env={'WEBUI_SECRET_KEY':secrets.token_urlsafe(48),'WEBUI_AUTH':'true','ENABLE_SIGNUP':'true',
 'OFFLINE_MODE':'true','HF_HUB_OFFLINE':'1','TRANSFORMERS_OFFLINE':'1','ENABLE_OLLAMA_API':'false',
 'ENABLE_OPENAI_API':'true','OPENAI_API_BASE_URL':'http://provider:8999/v1','OPENAI_API_KEY':secrets.token_urlsafe(24),
 'RAG_EMBEDDING_ENGINE':'ollama','OLLAMA_BASE_URL':'http://provider:8999','ANONYMIZED_TELEMETRY':'false',
 'DO_NOT_TRACK':'true','SCARF_NO_ANALYTICS':'true'}
 atomic(PRIVATE/'webui.env',''.join(k+'='+v+'\n' for k,v in env.items()))
 descriptor=json.loads((PACKET/'descriptor.json').read_text());compose=render(descriptor)
 compose['services'].update({
 'pg':{'image':descriptor['postgres_image'],'environment':{'POSTGRES_USER':'fixture','POSTGRES_DB':'integration','POSTGRES_HOST_AUTH_METHOD':'trust'},'volumes':['pg:/var/lib/postgresql'],'mem_limit':'192m','healthcheck':{'test':['CMD-SHELL','pg_isready -U fixture -d integration'],'interval':'2s','timeout':'2s','retries':30}},
 'provider':{'image':API_IMAGE,'read_only':True,'volumes':[str(PACKET/'fixture')+':/source:ro'],'command':['python','-B','/source/provider.py'],'mem_limit':'96m'},
 'prometheus':{'image':descriptor['monitor_images']['prometheus'],'volumes':[str(PRIVATE/'prometheus')+':/etc/prometheus:ro'],'command':['--config.file=/etc/prometheus/prometheus.json','--storage.tsdb.path=/prometheus'],'mem_limit':'160m'},
 'kuma':{'image':descriptor['monitor_images']['kuma'],'volumes':['kuma:/app/data'],'mem_limit':'256m'},
 })
 compose['volumes'].update(pg={},kuma={})
 atomic(ROOT/'compose.json',json.dumps(compose,indent=2))
 for p in [ROOT/'state',ROOT/'state/files',ROOT/'state/config',ROOT/'state/corpus']:
  p.mkdir(exist_ok=True);os.chown(p,10001,10001)
 for p in (ROOT/'state/files').glob('.*lock'):os.chown(p,10001,10001)
 command(COMPOSE+['up','-d','pg','provider'])
 command(COMPOSE+['run','--rm','--no-deps','-v',str(PACKET/'fixture')+':/source:ro','api','python','-B','/source/seed.py'])
 command(COMPOSE+['up','-d','api','webui']);ready_api()
 return {'api_ready':True,'webui_started':True,'holds':holds()}

def install(values):
 m=lib();m.ready();state=json.loads((PRIVATE/'credentials.json').read_text())
 marker=PRIVATE/'install-started';assert not marker.exists();marker.touch(mode=0o600)
 m.api('POST','/api/v1/auths/signup',{'name':'Request027 development','email':state['email'],'password':state['password']})
 token=m.login(state)
 for fid,name in [('community_brain_filter','community_brain_filter.py'),('cbm_request026_probe','probe_action.py')]:
  m.api('POST','/api/v1/functions/create',{'id':fid,'name':fid,'content':(PACKET/'fixture'/name).read_text(),'meta':{}},token)
 m.api('POST','/api/v1/functions/id/community_brain_filter/toggle',token=token)
 m.api('POST','/api/v1/functions/id/community_brain_filter/toggle/global',token=token)
 valves=m.api('GET','/api/v1/functions/id/community_brain_filter/valves',token=token)
 valves.update(retrieval_url=m.RETRIEVAL,api_key=values['CB_OPENWEBUI_RETRIEVAL_TOKEN'])
 m.api('POST','/api/v1/functions/id/community_brain_filter/valves/update',valves,token)
 assert m.probe(token,values['CB_OPENWEBUI_RETRIEVAL_TOKEN'])['source_count']==1
 return {'actual_api_and_webui_filter':True,'synthetic_source_found':True}

def accept(values):
 before=holds()
 descriptor=json.loads((PACKET/'descriptor.json').read_text())
 current=json.loads((ROOT/'compose.json').read_text())
 for name in ('api','webui'):assert current['services'][name]==render(descriptor)['services'][name]
 environment(values)
 command(COMPOSE+['up','-d','--no-deps','--force-recreate','api']);ready_api()
 result=inspect_runtime();assert before==result['holds']
 return result

def verify_tokens(values,revoked=False):
 specs=json.loads((PACKET/'identity-specs.json').read_text())
 for key,_,_,_ in specs:
  path='/metrics' if key=='CB_METRICS_PROBE_TOKEN' else '/api/v1/me';body=None;expected=200
  if key=='CB_OPENWEBUI_RETRIEVAL_TOKEN':path='/retrieval/query';body={'question':'synthetic'}
  if key=='CB_PROD_MAC_COLLECTOR_TOKEN':expected=403
  assert call(path,values[key],body)[0]==(401 if revoked else expected),'identity authentication mismatch'
  if not revoked:
   denied='/api/v1/jobs' if key=='CB_METRICS_PROBE_TOKEN' else '/metrics'
   assert call(denied,values[key])[0]==403,'cross-scope permission mismatch'
 return {'subjects':5,'old_rejected':revoked,'scope_denials':not revoked}

def lock_probe(values):
 status,body=call('/api/v1/jobs',values['CB_PROD_MANUAL_OPERATOR_TOKEN'],{})
 assert status==503 and body=={'code':'checkpoint_in_progress_retry_shortly'}
 assert call('/retrieval/query',values['CB_OPENWEBUI_RETRIEVAL_TOKEN'],{'question':'synthetic'})[0]==200
 return {'api_submission_blocked_by_quiet_lease':True,'retrieval_available':True}

def worker_hold_probe(values):
 expected=sys.argv[1];before=holds()
 env={**os.environ,'CBM_PACKET_SHA256':expected,'PYTHONDONTWRITEBYTECODE':'1'}
 manual=subprocess.run(['python3','-B',str(PACKET/'workers/manual_host.py'),'execute','unapproved'],env=env,capture_output=True,text=True,timeout=30)
 assert manual.returncode!=0 and 'processing held; no worker launch permitted' in manual.stderr
 automatic=subprocess.run(['python3','-B',str(PACKET/'workers/automatic_host.py')],env=env,capture_output=True,text=True,timeout=30)
 assert automatic.returncode==0 and automatic.stdout==''
 assert holds()==before
 return {'manual_launcher_rejected_while_held':True,'automatic_launcher_excluded_by_real_runner_lock':True,'holds_unchanged':True,'worker_execution_tested':False}

def cache(values):
 m=lib();state=json.loads((PRIVATE/'credentials.json').read_text())
 assert m.probe(m.login(state),values['CB_OPENWEBUI_RETRIEVAL_TOKEN'])['source_count']==1
 return {'live_webui_cache':True}

def webui_deliver(journal):
 m=lib();state=json.loads((PRIVATE/'credentials.json').read_text());token=m.login(state)
 valves=m.api('GET','/api/v1/functions/id/community_brain_filter/valves',token=token)
 key='CB_OPENWEBUI_RETRIEVAL_TOKEN'
 assert valves['api_key'] in [journal['old'][key],journal['updates'][key]]
 assert valves['retrieval_url']==m.RETRIEVAL
 valves['api_key']=journal['updates'][key]
 m.api('POST','/api/v1/functions/id/community_brain_filter/valves/update',valves,token)
 return cache(journal['updates'])

def main():
 os.umask(0o077)
 assert socket.gethostname()=='community-brain-dev' and os.geteuid()==0 and Path('/srv/dev-data').is_mount()
 expected=sys.argv[1];mode=sys.argv[2];verify(PACKET,expected)
 payload=json.load(sys.stdin)
 from runtime_contract import load,controls
 descriptor=load(expected)
 from automatic_host import tick
 from boot_guard import inspect as boot_inspect
 operations={'worker-hold-probe':worker_hold_probe,'lock-probe':lock_probe,'controls':lambda x:controls(descriptor),'tick':lambda x:tick(expected),'boot-inspect':lambda x:boot_inspect(expected),'setup':setup,'install':install,'accept':accept,'tokens':verify_tokens,'revoked':lambda x:verify_tokens(x,True),'cache':cache,'webui-deliver':webui_deliver,'inspect':lambda x:inspect_runtime()}
 if mode not in operations:
  from consumers import operations as consumer_operations
  operations.update(consumer_operations())
 result=operations[mode](payload)
 print(json.dumps(result))
if __name__=='__main__':main()

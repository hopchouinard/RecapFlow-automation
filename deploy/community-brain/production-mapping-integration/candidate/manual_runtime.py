"""Seal-first manual API renderer contract; no production executor in this phase."""
import hashlib,json,os
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def validate_packet(root,manifest_sha256):
 root=Path(root);manifest=root/'runtime-manifest.json'
 if root.is_symlink() or manifest.is_symlink() or sha(manifest)!=manifest_sha256:raise ValueError('runtime manifest identity')
 expected=json.loads(manifest.read_bytes());actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p!=manifest}
 if actual!=set(expected):raise ValueError('runtime members differ; retain original, do not delete bytecode')
 for n,h in expected.items():
  p=root/n
  if p.is_symlink() or '__pycache__' in p.parts or p.suffix=='.pyc' or not p.resolve().is_relative_to(root.resolve()) or sha(p)!=h:raise ValueError('runtime source changed or executable bytecode present')
 return expected

def render(values,binding):
 """Only identity generation may change; incumbent and all other env remain pinned."""
 required={'packet','manifest_sha256','incumbent_id','incumbent_image','incumbent_fingerprint','current_environment','generation','deadline','rollback_owner','scope','executor_manifest_sha256','unit'}
 if set(binding)!=required or binding['scope']!='synthetic-development':raise ValueError('production compiler remains disabled')
 validate_packet(binding['packet'],binding['manifest_sha256'])
 old=binding['current_environment'];api={'CB_DATABASE_URL':values['CB_RUNTIME_DATABASE_URL'],'CB_SERVICE_IDENTITIES':values['CB_SERVICE_IDENTITIES']}
 api.update({k:values[k] for k in ('CB_OIDC_ISSUER','CB_OIDC_AUDIENCE','CB_OIDC_CLIENT_ID','CB_OIDC_JWKS_URL')})
 if {k:v for k,v in old.items() if k!='CB_SERVICE_IDENTITIES'}!={k:v for k,v in api.items() if k!='CB_SERVICE_IDENTITIES'}:raise ValueError('non-identity environment drift')
 if any(not isinstance(v,str) or any(c in v for c in ("'",'\n','\r')) for v in api.values()):raise ValueError('unsafe environment value')
 identities=json.loads(api['CB_SERVICE_IDENTITIES'])
 if len(identities) not in (5,10) or any(r['scope']!='community-brain' for r in identities):raise ValueError('authority shape')
 if not all(len(binding[k])==64 for k in ('incumbent_id','incumbent_fingerprint')):raise ValueError('incumbent binding')
 return {'environment':api,'generation':binding['generation'],'incumbent_id':binding['incumbent_id'],'incumbent_image':binding['incumbent_image'],'incumbent_fingerprint':binding['incumbent_fingerprint'],'packet_manifest_sha256':binding['manifest_sha256'],'rollback_owner':binding['rollback_owner'],'deadline':binding['deadline'],'production_execution_enabled':False}

def recreate(values,binding=None):
 """Development-only Docker clone; retain exact incumbent for explicit rollback.

 Caller must hold shared admission and target supervisor/finalizer ownership.
 The public entry requires a private binding file beneath the Request033 root.
 """
 import subprocess,time,copy,http.client,socket
 from helper_contracts import current_cycle
 current_cycle()
 root=Path('/srv/dev-data/workspaces/cbm-production-mapping-20260922-033')
 path=Path(os.environ['CBM_MANUAL_BINDING']) if binding is None else Path(binding)
 if path.is_symlink() or not path.resolve().is_relative_to(root) or path.stat().st_uid!=0 or path.stat().st_mode&511!=384:raise ValueError('private development binding required')
 b=json.loads(path.read_bytes());plan=render(values,b)
 from helper_contracts import verify_sources
 if b['executor_manifest_sha256']!=verify_sources() or not b['unit'].startswith('cbm-r033-render-'):raise ValueError('supervised source binding')
 props=subprocess.check_output(['systemctl','show',b['unit'],'--property=MainPID,ExecStopPost,RuntimeMaxUSec'],text=True)
 fields=dict(x.split('=',1) for x in props.splitlines() if '=' in x)
 if int(fields['MainPID'])!=os.getpid() or 'renderer_finalize.py' not in fields['ExecStopPost'] or str(path) not in fields['ExecStopPost'] or fields['RuntimeMaxUSec']=='infinity':raise ValueError('independent bounded finalizer required')
 if time.time()>=b['deadline']:raise ValueError('maintenance deadline expired')
 row=json.loads(subprocess.check_output(['docker','inspect',b['incumbent_id']]))[0]
 fingerprint=hashlib.sha256(json.dumps({k:row[k] for k in ('Id','Image','Config','HostConfig','Mounts')},sort_keys=True).encode()).hexdigest()
 if fingerprint!=b['incumbent_fingerprint'] or row['Image']!=b['incumbent_image'] or not row['Name'].startswith('/cbm-r033-') or row['HostConfig']['NetworkMode']!='none' or row['Mounts']:raise ValueError('exact isolated incumbent required')
 journal=path.parent/('generation-'+b['generation']);journal.mkdir(mode=0o700)
 def save(name,value):
  p=journal/name
  with p.open('x') as f:json.dump(value,f);f.flush();os.fsync(f.fileno())
  p.chmod(0o600)
 save('intent.json',{'incumbent_id':row['Id'],'generation':b['generation'],'deadline':b['deadline'],'replay_allowed':False})
 class Unix(http.client.HTTPConnection):
  def connect(self):
   self.sock=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM);self.sock.settimeout(10);self.sock.connect('/var/run/docker.sock')
 def api(method,url,body=None):
  c=Unix('localhost',timeout=10);c.request(method,url,body=None if body is None else json.dumps(body),headers={'Content-Type':'application/json'});r=c.getresponse();data=r.read();c.close()
  if r.status>=300:raise ValueError('isolated Docker operation failed; private response suppressed')
  return json.loads(data) if data else {}
 if not b['generation'].replace('-','').isalnum() or len(b['generation'])>60:raise ValueError('generation name')
 config=copy.deepcopy(row['Config']);config['Image']=row['Image'];current=dict(x.split('=',1) for x in config['Env']);current.update(plan['environment']);config['Env']=[k+'='+v for k,v in sorted(current.items())];config['HostConfig']=copy.deepcopy(row['HostConfig']);config['HostConfig']['RestartPolicy']={'Name':'no','MaximumRetryCount':0}
 name='cbm-r033-generation-'+b['generation'];replacement=None
 try:
  replacement=api('POST','/containers/create?name='+name,config)['Id'];save('created.json',{'replacement_id':replacement,'name':name})
  api('POST','/containers/'+row['Id']+'/stop?t=2');api('POST','/containers/'+replacement+'/start')
  for _ in range(30):
   if time.time()>=b['deadline']:raise ValueError('serving deadline')
   p=subprocess.run(['docker','exec',replacement,'python','-B','-c',"import urllib.request;assert urllib.request.urlopen('http://127.0.0.1:8080',timeout=1).status==200"],capture_output=True,timeout=3)
   if p.returncode==0:break
   time.sleep(.1)
  else:raise ValueError('replacement serving failed')
  actual=json.loads(subprocess.check_output(['docker','inspect',replacement]))[0];environment=dict(x.split('=',1) for x in actual['Config']['Env'])
  if any(environment[k]!=v for k,v in plan['environment'].items()):raise ValueError('generation readback mismatch')
  save('accepted.json',{'replacement_id':replacement,'exact_incumbent_retained':row['Id'],'environment_sha256':hashlib.sha256(json.dumps(plan['environment'],sort_keys=True).encode()).hexdigest(),'production_qualified':False})
  return {'replacement_id':replacement,'incumbent_id':row['Id'],'journal':str(journal)}
 except BaseException:
  if replacement:
   try:api('POST','/containers/'+replacement+'/stop?t=1')
   except ValueError:pass
  api('POST','/containers/'+row['Id']+'/start');save('rollback.json',{'incumbent_id':row['Id'],'reason':'generation not accepted; partial attempt retained'});raise

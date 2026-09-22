"""Execute deployed algorithms with scoped filesystem and transport fixtures.

Remote APIs/CA/AppleScript are explicit test doubles. Embedded filesystem writers,
source policy, scheduler ordering and durable admission execute actual source.
This is not live consumer acceptance or production helper invocation.
"""
import ast,base64,contextlib,datetime,hashlib,io,json,os,runpy,shlex,subprocess,sys,tempfile,types,unittest.mock as mock
from pathlib import Path
from helper_contracts import *
REAL_RUN=subprocess.run

def module(path,name):
 m=types.ModuleType(name);m.__file__=str(path);exec(compile(path.read_text(),str(path),'exec'),m.__dict__);return m

def synthetic_authority(policy):
 values={};records=[]
 for key,exp,subject,permissions in policy.SPECS:
  values[key]='SYNTHETIC-'+key;values[exp]=str(int(__import__('time').time())+86400)
  records.append({'subject':subject,'scope':'community-brain','permissions':permissions,'sha256':sha(values[key].encode()),'expires_at':int(values[exp])})
 values[policy.IDENTITIES]=json.dumps(records);return values
class Environment:
 def __init__(self,root):
  self.root=root;self.home=root/'home';self.home.mkdir();self.state=self.home/'.local/state/community-brain-management';self.state.mkdir(parents=True)
  self.effects=[];self.transport_calls=[];self.cycle=None;self.source_copy=root/'source';__import__('shutil').copytree(MAC,self.source_copy)
  self.integrations=self.source_copy/'platform-services/community-brain-prod/integrations';self.automatic=self.source_copy/'platform-services/community-brain-prod/automatic-recovery'
  self.policy=module(INTEGRATIONS/'service_renewal_policy.py','service_renewal_policy');self.values=synthetic_authority(self.policy)
  self.state.joinpath('pre-pbs-state.json').write_text(json.dumps({'state':'verified','next_due_epoch':__import__('time').time()+86400}));self.state.joinpath('service-renewal-status.json').write_text(json.dumps({'state':'completed','checked_at':__import__('time').time()}))
  self.dump=b'EXPLICIT SYNTHETIC TRANSPORT BYTES; real PG capture is separately tested';self.dump_name=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ.dump');self.dump_info={'name':self.dump_name,'bytes':len(self.dump),'sha256':sha(self.dump),'native_dump_exit_status':0}
  self.secret=types.ModuleType('secret_store');self.secret.read=lambda:dict(self.values);self.secret.save=self.save_authority;self.secret.remote=self.remote
 def save_authority(self,updates):
  self.values.update(updates);p=self.root/'authority.json';p.write_text(json.dumps(self.values));p.chmod(0o600);self.effects.append(p)
 def remap(self,code,host):
  # Path/host identities only. The embedded algorithm is unchanged.
  for path in ['/var/lib/prometheus/node-exporter','/srv/community-brain','/mnt/HDD_2TB_Main/traefik/dynamic','/opt/platform-services/compose/community-brain-nats-tls','/etc/community-brain-production']:
   dest=self.root/'hosts'/host/path.lstrip('/');dest.mkdir(parents=True,exist_ok=True);code=code.replace(path,str(dest))
  return code
 def remote(self,host,code,payload=None):
  self.transport_calls.append({'host':host,'code_sha256':sha(code.encode())})
  if host=='n8n-automation':raise ValueError('retired VM101 consumer forbidden')
  return self.execute_remote(host,code,payload)
 def execute_remote(self,host,code,payload=None):
  code=self.remap(code,host)
  # The source's actual remote file-writing code runs; infrastructure CLI calls
  # below are recorded fixtures, never real production SSH/Docker/CA calls.
  output=io.StringIO()
  def proc(args,*a,**kw):
   if args[0] in ('docker','pg_restore','systemctl'):
    self.transport_calls.append({'fixture_command':args});return subprocess.CompletedProcess(args,0,stdout=b'',stderr=b'')
   raise ValueError('unmapped remote command')
  with mock.patch('sys.stdin',io.StringIO(json.dumps(payload))),contextlib.redirect_stdout(output),mock.patch('subprocess.run',proc):
   exec(compile(code,'<deployed-remote-writer>','exec'),{'__name__':'__main__'})
  self.effects.extend(p for p in (self.root/'hosts').rglob('*') if p.is_file())
  return output.getvalue()
 def run_process(self,args,*a,**kw):
  if args[0]=='openssl':return subprocess.CompletedProcess(args,0,stdout=b'',stderr=b'') # existing synthetic certificate, no issue branch
  if args[0]=='osascript':return subprocess.CompletedProcess(args,0,stdout='false\n',stderr='')
  if args[0]=='launchctl':return subprocess.CompletedProcess(args,1,stdout=b'',stderr=b'')
  if args[0]=='ssh':
   tokens=shlex.split(args[-1]);code=tokens[-1];host=next(x for x in args if x in ('pchouinard@10.1.10.50','pchouinard@10.1.30.21','root@10.1.10.4','traefik'))
   if 'Completed' in code:raise ValueError('unexpected')
   if "native_dump_exit_status" in code:return subprocess.CompletedProcess(args,0,stdout=json.dumps(self.dump_info),stderr='')
   if "'size':p.stat().st_size" in code:return subprocess.CompletedProcess(args,0,stdout=json.dumps({'name':self.dump_name,'size':len(self.dump)}),stderr='')
   if 'sys.stdout.buffer.write' in code:
    kw['stdout'].write(self.dump);return subprocess.CompletedProcess(args,0)
   if 'sys.stdin.buffer.read' in code:
    data=kw['stdin'].read();mapped=self.remap(code,host);out=io.StringIO();inp=types.SimpleNamespace(buffer=io.BytesIO(data))
    with mock.patch('sys.stdin',inp),contextlib.redirect_stdout(out):exec(compile(mapped,'<actual-copy-writer>','exec'),{})
    self.effects.extend(p for p in (self.root/'hosts').rglob('*') if p.is_file());return subprocess.CompletedProcess(args,0,stdout=out.getvalue(),stderr='')
   if 'pct' in tokens and 'python3' in tokens:
    out=self.remote(host,code,json.loads(kw['input']));return subprocess.CompletedProcess(args,0,stdout=out,stderr='')
   if 'root=pathlib.Path' in code or 'checkpoint-needed.json' in code:
    # consumer/monitor reads are tested using real local fixture controls.
    mapped=self.remap(code,host);out=io.StringIO()
    def output(cmd,*a,**k):
     if cmd[:2]==['docker','inspect']:return json.dumps([{'Config':{'Env':['CB_AUTOMATIC_PROCESSING=false']}}]).encode()
     if cmd[:2]==['docker','ps']:return b''
     raise ValueError('unexpected monitoring command')
    with mock.patch('subprocess.check_output',output),contextlib.redirect_stdout(out):
     try:exec(compile(mapped,'<actual-control-readback>','exec'),{})
     except SystemExit as e:assert e.code in (0,None)
    self.effects.extend(p for p in (self.root/'hosts').rglob('*') if p.is_file());return subprocess.CompletedProcess(args,0,stdout=out.getvalue() if kw.get('text') else out.getvalue().encode(),stderr='')
   raise ValueError('unmapped SSH request')
  if len(args)>1 and Path(args[1]).name=='maintain-hourly.py':
   out=io.StringIO()
   with contextlib.redirect_stdout(out):
    try:runpy.run_path(str(self.source_copy/'maintain-hourly.py'),run_name='__main__')
    except SystemExit as e:assert e.code==0
   return subprocess.CompletedProcess(args,0,stdout=out.getvalue(),stderr='')
  if args[0]=='/bin/bash' and Path(args[1]).name=='run.sh':
   name=Path(args[2]).stem
   if name not in HELPERS:raise ValueError('wrapper helper outside allowlist')
   action=(lambda:renewal(self)) if name=='renew-service-tokens' else (lambda:self.execute(name))
   receipt=self.cycle.helper(name,action,self.readback);return subprocess.CompletedProcess(args,0,stdout=json.dumps(receipt),stderr='')
  if len(args)>1 and Path(args[1]).name in ('pre-pbs-copy.py','mac-intake.py','consumer.py'):
   name={'pre-pbs-copy.py':'pre-pbs-copy','mac-intake.py':'legacy-intake-ownership','consumer.py':'checkpoint-consumer'}[Path(args[1]).name]
   if self.cycle:self.cycle.helper(name,lambda:self.execute(name),self.readback)
   return subprocess.CompletedProcess(args,0,stdout=json.dumps({'state':'paused'}),stderr='')
  if args[0] in ('python3',sys.executable) and Path(args[1]).name=='copy-backup.py':
   out=self.execute('copy-backup');return subprocess.CompletedProcess(args,0,stdout=out,stderr='')
  raise ValueError('unmapped subprocess: '+str(args[:2]))
 def execute(self,name):
  path=self.source_copy/HELPERS[name].relative_to(MAC);out=io.StringIO()
  argv=[str(path)]+(['--rehearse'] if name=='pre-pbs-copy' else ['poll'] if name=='legacy-intake-ownership' else [])
  with mock.patch.dict(sys.modules,{'secret_store':self.secret,'manage':types.SimpleNamespace(CTX=None,PROJECT='synthetic')}),mock.patch.object(Path,'home',return_value=self.home),mock.patch('subprocess.run',self.run_process),mock.patch('subprocess.check_output',lambda args,**kw:self.run_process(args,**kw).stdout),mock.patch.object(sys,'argv',argv),contextlib.redirect_stdout(out):
   old=sys.path[:];sys.path[:0]=[str(self.integrations),str(self.automatic),str(self.source_copy)]
   try:
    try:runpy.run_path(str(path),run_name='__main__')
    except SystemExit as e:
     # Health intentionally reports critical_24h from synthetic expiring tokens.
     assert e.code in (None,0) or name=='management-health' and e.code==1,(name,e.code)
   finally:sys.path[:]=old
  self.effects.extend(p for p in self.state.rglob('*') if p.is_file());return out.getvalue()
 def readback(self):
  return {'files':{str(p.relative_to(self.root)):sha(p.read_bytes()) for p in sorted(set(self.effects)) if p.exists()},'transport_contracts':self.transport_calls,'external_services':'explicit scoped fixtures; not live acceptance'}

def renewal(env):
 policy=env.policy
 class Adapter:
  def read(self):return dict(env.values)
  def save(self,v):env.save_authority(v)
  def inventory(self,v):policy.validate(v)
  def accept(self,v):
   env.accepted=json.loads(v[policy.IDENTITIES]);(env.root/'accepted-authority.json').write_text(json.dumps(env.accepted))
  def verify_tokens(self,v,accepted=True):
   for key,_,subject,_ in policy.SPECS:
    found=any(r['subject']==subject and r['sha256']==sha(v[key].encode()) for r in env.accepted);assert found==accepted
  def verify_overlap(self,j):self.verify_tokens(j['old']);self.verify_tokens(j['updates'])
  def deliver(self,j):
   # Exact successor roles; original VM101 is never contacted.
   for key,_,subject,_ in policy.SPECS:
    p=env.root/('consumer-'+subject+'.json');p.write_text(json.dumps({'token':j['updates'][key],'target':'vm109-successor' if 'openwebui' in subject else subject}));p.chmod(0o600);env.effects.append(p)
  def verify_consumers(self,j):
   self.verify_tokens(j['updates'])
   for key,_,subject,_ in policy.SPECS:assert json.loads((env.root/('consumer-'+subject+'.json')).read_bytes())['token']==j['updates'][key]
  def verify_revoked(self,j):self.verify_tokens(j['old'],False)
 adapter=Adapter();result=policy.run(adapter,__import__('time').time(),force=True);assert result['state']=='completed';assert len(env.accepted)==5
 return result

def run(root,mutex):
 root=Path(root);root.mkdir(mode=0o700);env=Environment(root/'fixture') if False else None
 fixture=root/'fixture';fixture.mkdir();env=Environment(fixture);results={}
 # Retained terminal ownership means the actual policy never calls VM101.
 policy=module(MAC/'mac_intake_policy.py','mac_intake_policy');p=env.home/'.local/state/community-brain-window';p.mkdir(parents=True)
 (p/'CBM-RETRIEVAL-20260910-001.json').write_text(json.dumps({'request_id':policy.ORIGINAL,'path':'/Volumes/NVMe_2TB_Work/Documents/Zoom','phase':'superseded','ownership':{'request_id':policy.REQUEST,'accepted_recovery_receipt_sha256':policy.RECEIPT,'legacy_writers_disabled':True}}))
 for k in ('CB_NATS_TLS_FULLCHAIN_B64','CB_NATS_TLS_KEY_B64','CB_APP_TLS_FULLCHAIN_B64','CB_APP_TLS_KEY_B64'):env.values[k]=base64.b64encode(b'SYNTHETIC CERTIFICATE FIXTURE').decode()
 control=env.root/'hosts/pchouinard@10.1.30.21/srv/community-brain/automation';control.mkdir(parents=True);(control/'paused').write_text('preserve');(control/'attention.json').write_text('{}');(control/'checkpoint-needed.json').write_text('{"job_id":"retained"}')
 holds={p.name:sha(p.read_bytes()) for p in control.iterdir()}
 with Cycle(root/'journal',mutex,root.name+'-helpers','manual',verify_sources()) as cycle:
  for name in HELPERS:
   if name=='renew-service-tokens':action=lambda:renewal(env)
   else:action=lambda n=name:env.execute(n)
   results[name]=cycle.helper(name,action,env.readback)
  assert holds=={p.name:sha(p.read_bytes()) for p in control.iterdir() if p.name in holds}
  cycle.finish()
 # Run the installed scheduler control flow, including actual hourly task list.
 with Cycle(root/'journal',mutex,root.name+'-scheduler','scheduler',verify_sources()) as cycle:
  env.cycle=cycle
  old=sys.path[:];sys.path[:0]=[str(env.integrations),str(env.automatic),str(env.source_copy)]
  try:
   with mock.patch.object(Path,'home',return_value=env.home),mock.patch('subprocess.run',env.run_process):
    import scheduler_adapter
    status=scheduler_adapter.run(cycle)
   assert status['hourly']=='passed' and status['automatic']['state']=='paused',status
   cycle.finish()
  finally:sys.path[:]=old;env.cycle=None
 receipt={'scheduler_actual_algorithm':status,'helpers':results,'actual_deployed_algorithms':True,'external_boundary_fixtures':True,'production_helpers_invoked':False,'holds_and_checkpoint_preserved':True,'legacy_network_calls':0,'renewal_policy_actual':True,'renewal_live_adapter_acceptance':False,'scope':'deployed algorithm and filesystem writer tests; not production endpoint acceptance'}
 write_new(root/'helper-receipts.json',receipt);print(json.dumps({'helper_count':len(results),'receipt':str(root/'helper-receipts.json'),'external_boundary_fixtures':True}))
if __name__=='__main__':run(*sys.argv[1:])

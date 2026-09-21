"""Bounded validation on disposable Request029 state. Never production."""
import hashlib,json,os,subprocess,sys,tarfile
from pathlib import Path
from host import ROOT,PRIVATE,PACKET,COMPOSE,command,atomic,call,address,OPENER,holds
from run import contract,container_args,worker_environment,invoke
from successor import verify

def data(operation='inspect'):
 return json.loads(invoke(container_args(),worker_environment(),['python','-B','/packet/fixture/data_check.py',operation],log=PRIVATE/('data-'+operation+'.log')))

def launch(args,*,outcome='success',expect_failure=False):
 env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','CBM_TEST_OUTCOME':outcome}
 result=subprocess.run(['python3','-B',str(PACKET/'workers/manual_host.py'),*args],env=env,capture_output=True,text=True,timeout=300)
 (PRIVATE/'last-manual.log').write_text(result.stderr)
 if expect_failure:
  assert result.returncode!=0,'expected refused execution';return {'refused':True}
 if result.returncode:raise RuntimeError('manual launcher failed; inspect private outcome')
 return json.loads(result.stdout)

def submit(values,date,fathom=False):
 import urllib.request
 token=values['CB_PROD_MANUAL_OPERATOR_TOKEN'];meeting='request029-'+date
 sources={}
 for kind in ['chat'] if fathom else ['transcript','chat']:
  status,body=call('/api/v1/sources',token,{'meeting_id':meeting,'kind':kind,'content':'Synthetic '+kind})
  assert status==201 or status==200,(status,body)
  sources[kind]=body['id']
 body={'identity':{'meeting_id':meeting,'local_date':date,'started_at':date+'T22:00:00Z','timezone':'America/Toronto','provider':'fathom' if fathom else 'manual'},'mode':'weekly','sources':sources}
 req=urllib.request.Request(address('api',8090)+'/api/v1/jobs',headers={'Authorization':'Bearer '+token,'Content-Type':'application/json','Idempotency-Key':meeting},data=json.dumps(body).encode())
 with OPENER.open(req,timeout=30) as r:
  assert r.status==202;job=json.load(r)['id']
 return job

def manual(values):
 marker=ROOT/'manual-validation-intent';assert not marker.exists();marker.touch()
 excluded=data('excluded')['excluded_job']
 job=submit(values,'2026-09-11')
 stages=[]
 for stage in ('processing','indexing'):
  selection=launch(['inspect',job,stage,'1'])['selection']
  result=launch(['execute',selection]);assert result['state']=='succeeded',result
  stages.append(result)
  launch(['execute',selection],expect_failure=True)
 proof=data();old=next(j for j in proof['jobs'] if j['id']==excluded)
 assert old['outbox_sent']==0 and all(s['attempts']==0 for s in old['stages'])
 assert proof['fts']['num_unindexed_rows']==0
 result={'actual_manual_inspect_execute':True,'stages':stages,'duplicate_execute_refused':True,'excluded_job':excluded,'proof':proof}
 atomic(ROOT/'manual-acceptance.json',json.dumps(result))
 return result

def automatic(values):
 from automation import tick
 expected=os.environ['CBM_PACKET_SHA256']
 # The manual job is automatically eligible; completion must gate the next meeting.
 before=data();result=tick(expected)
 assert result['state']=='awaiting_checkpoint',result
 assert data()==before
 return {'checkpoint_gate':True,'no_new_attempts':True,'state':result,'proof':before}

def paired(values):
 # Invoked under management's live quiet lease: writer locks are held throughout.
 marker=ROOT/'paired-recovery';marker.mkdir(mode=0o700)
 before=data();atomic(marker/'before.json',json.dumps(before))
 with (marker/'database.sql').open('xb') as output:
  p=subprocess.run(COMPOSE+['exec','-T','pg','pg_dump','-U','fixture','--no-owner','integration'],stdout=output,stderr=subprocess.PIPE,timeout=90)
 assert p.returncode==0
 with tarfile.open(marker/'state.tar','w') as tar:
  for name in ('files','config','corpus','meeting-archive','automation','automation-public','manual-approvals'):
   tar.add(ROOT/'state'/name,arcname=name)
 with tarfile.open(marker/'private-runtime.tar','w') as tar:
  tar.add(PRIVATE,arcname='private');tar.add(PACKET,arcname='packet');tar.add(ROOT/'compose.json',arcname='compose.json')
 # Capture the WebUI volume while this disposable WebUI is stopped, paired with external signing material.
 from host import container
 webui=container('webui')
 row=json.loads(command(['docker','inspect',webui]))[0]
 source=Path(next(m['Source'] for m in row['Mounts'] if m['Destination']=='/app/backend/data'))
 command(['docker','stop',webui])
 try:
  with tarfile.open(marker/'webui.tar','w') as tar:tar.add(source,arcname='webui')
 finally:command(['docker','start',webui])
 signing_digest=hashlib.sha256((PRIVATE/'webui.env').read_bytes()).hexdigest()
 # Independent restore destination and database; live fixture remains unchanged.
 restored=marker/'restored';restored.mkdir(mode=0o755);restored.chmod(0o755)
 with tarfile.open(marker/'state.tar') as tar:tar.extractall(restored,filter='data')
 command(COMPOSE+['exec','-T','pg','createdb','-U','fixture','integration_restore'])
 with (marker/'database.sql').open('rb') as incoming:
  p=subprocess.run(COMPOSE+['exec','-T','pg','psql','-U','fixture','-d','integration_restore','-v','ON_ERROR_STOP=1'],stdin=incoming,capture_output=True,timeout=90)
 assert p.returncode==0
 return finish_pair(marker)

STATE_TREES=('files','config','corpus','meeting-archive','automation','automation-public','manual-approvals')

def state_manifest(root):
 files={}
 for name in STATE_TREES:
  tree=root/name
  if not tree.is_dir() or tree.is_symlink():
   raise ValueError('Missing or linked recovery tree: '+name)
  for path in tree.rglob('*'):
   if path.is_symlink():raise ValueError('Linked recovery member')
   if path.is_file():files[str(path.relative_to(root))]=hashlib.sha256(path.read_bytes()).hexdigest()
 return files

def verify_restored_state(original,restored):
 expected=state_manifest(original)
 if state_manifest(restored)!=expected:
  raise ValueError('Restored durable and control state differ')
 return expected

def finish_pair(marker):
 before=json.loads((marker/'before.json').read_text());restored=marker/'restored'
 files=verify_restored_state(ROOT/'state',restored)
 for name in ('files','config','corpus'):
  for path in [restored/name,*(restored/name).rglob('*')]:
   assert not path.is_symlink();os.chown(path,10001,10001)
 signing_digest=hashlib.sha256((PRIVATE/'webui.env').read_bytes()).hexdigest()
 from host import container
 row=json.loads(command(['docker','inspect',container('webui')]))[0]
 source=Path(next(m['Source'] for m in row['Mounts'] if m['Destination']=='/app/backend/data'))
 env=worker_environment();env['CB_DATABASE_URL']='postgresql+psycopg://fixture@pg/integration_restore'
 args=container_args();i=args.index(str(ROOT/'state/files')+':/state/files:rw');args[i]=str(restored/'files')+':/state/files:rw'
 for name in ('config','corpus'):
  i=args.index(str(ROOT/'state'/name)+':/state/'+name+':ro');args[i]=str(restored/name)+':/state/'+name+':ro'
 actual=json.loads(invoke(args,env,['python','-B','/packet/fixture/data_check.py','inspect'],log=PRIVATE/'restore.log'))
 atomic(marker/'restored-observation.json',json.dumps(actual))
 for proof in (actual,before):
  for job in proof['jobs']:job['stages'].sort(key=lambda stage:stage['name'])
 assert actual==before
 webui_files=0
 with tarfile.open(marker/'webui.tar') as tar:
  tar.extractall(marker/'webui-restore',filter='data')
  for member in tar:
   if member.isfile():
    other=marker/'webui-restore'/member.name
    assert hashlib.sha256(other.read_bytes()).digest()==hashlib.sha256(tar.extractfile(member).read()).digest()
    webui_files+=1
 import sqlite3
 restored_db=sqlite3.connect('file:'+str(marker/'webui-restore/webui/webui.db')+'?mode=ro',uri=True)
 assert restored_db.execute('pragma integrity_check').fetchone()==('ok',);restored_db.close()
 manifest={'webui_restore_integrity':True,'webui_files':webui_files,'signing_environment_sha256':signing_digest,'database_sha256':hashlib.sha256((marker/'database.sql').read_bytes()).hexdigest(),'restored_files':files,'packet_manifest':os.environ['CBM_PACKET_SHA256'],'restore_equal':True}
 raw=json.dumps(manifest,sort_keys=True).encode();atomic(marker/'manifest.json',raw.decode());digest=hashlib.sha256(raw).hexdigest()
 for j in before['jobs']:
  if j['indexing']=='complete':atomic(ROOT/'state/automation/checkpoints'/ (j['id']+'.json'),json.dumps({'job_id':j['id'],'verified':True,'manifest_sha256':digest}))
 (ROOT/'state/automation/checkpoint-needed.json').unlink(missing_ok=True)
 return {'paired_postgresql_and_state_restore':True,'database_and_durable_state_equal':True,'verified_files':len(files),'manifest_sha256':digest,'private_recovery_retained':True,'production_restore_certified':False}

def auto_execute(values):
 from automation import tick
 marker=ROOT/'automatic-validation-intent';assert not marker.exists();marker.touch()
 job=submit(values,'2026-09-12',True);before=data()
 result=tick(os.environ['CBM_PACKET_SHA256']);assert result['state']=='stage_completed',result
 after=data();j=next(j for j in after['jobs'] if j['id']==job)
 assert j['indexing']=='complete' and after['fts']['num_unindexed_rows']==0
 old=next(j for j in before['jobs'] if j['meeting_id']=='request029-2026-09-11')
 assert old==next(j for j in after['jobs'] if j['id']==old['id'])
 gated=tick(os.environ['CBM_PACKET_SHA256']);assert gated['state']=='awaiting_checkpoint'
 assert data()==after
 return {'actual_automatic_scan_tick':True,'job_id':job,'proof':after,'first_meeting_preserved':True,'checkpoint_gate':True}

def uncertain(values):
 # Second completed meeting stays checkpoint-gated; test an explicit manual selection.
 marker=ROOT/'uncertain-validation-intent';assert not marker.exists();marker.touch()
 job=submit(values,'2026-09-13');selection=launch(['inspect',job,'processing','1'])['selection']
 launch(['execute',selection],outcome='uncertain',expect_failure=True)
 before=data();j=next(j for j in before['jobs'] if j['id']==job)
 assert any(s['name']=='processing' and s['state']=='outcome_unknown' and s['attempts']==1 for s in j['stages'])
 launch(['execute',selection],expect_failure=True);assert data()==before
 return {'actual_uncertain_provider_outcome':True,'no_duplicate_execution':True,'proof':before,'paid_provider_or_budget_certified':False}

def boot_checks(expected):
 from boot_guard import inspect,enforce,reconcile
 from runtime_contract import held
 v=contract();state=ROOT/'state/automation';before=holds()
 assert held(v)
 launch(['execute','unapproved'],expect_failure=True)
 try:reconcile(expected,'wrong-boot-id')
 except ValueError:pass
 else:raise AssertionError('wrong boot accepted')
 atomic(state/'attention.json',json.dumps({'reason':'disposable boot acceptance test'}))
 try:reconcile(expected,Path('/proc/sys/kernel/random/boot_id').read_text().strip())
 except ValueError:pass
 else:raise AssertionError('unresolved attention accepted')
 (state/'attention.json').unlink()
 assert holds()==before
 enforced=enforce(expected);assert enforced['held'] and not enforced['reconciled']
 reconciled=reconcile(expected,Path('/proc/sys/kernel/random/boot_id').read_text().strip())
 assert not held(v) and reconciled['reconciled']
 return {'held_manual_refused':True,'wrong_boot_rejected':True,'unresolved_attention_rejected':True,'boot_enforced':enforced,'disposable_only_reconciled':reconciled}

def catalog(values):
 import urllib.request
 token=values['CB_READ_PROBE_TOKEN'];status,body=call('/api/v1/meetings',token)
 assert status==200
 count=0
 for meeting in body['items']:
  for artifact in meeting['artifacts']:
   req=urllib.request.Request(address('api',8090)+artifact.get('url','/api/v1/meeting-artifacts/'+artifact['id']+'/content'),headers={'Authorization':'Bearer '+token})
   with OPENER.open(req,timeout=30) as response:raw=response.read();assert response.status==200
   assert hashlib.sha256(raw).hexdigest()==artifact['sha256'];count+=1
 assert len(body['items'])==3 and count>1
 return {'actual_catalog_meetings':len(body['items']),'verified_artifact_downloads':count,'archive_and_processed_meetings':True}

def operations(expected):
 from boot_guard import inspect,enforce,reconcile
 from provisioning import resume_setup
 return {'catalog-proof':catalog,'validate-boot':lambda _:boot_checks(expected),'setup-resume':resume_setup,'boot-enforce':lambda _:enforce(expected),'boot-reconcile':lambda _:reconcile(expected,Path('/proc/sys/kernel/random/boot_id').read_text().strip()),'validate-manual':manual,'validate-checkpoint':automatic,'validate-recovery':paired,'recovery-resume':lambda _:finish_pair(ROOT/'paired-recovery'),'validate-automatic':auto_execute,'validate-uncertain':uncertain,'data-inspect':lambda _:data()}

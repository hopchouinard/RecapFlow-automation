"""Exclusive actual-Docker/PostgreSQL development fixture. Never VM109."""
import json
import os
from pathlib import Path
import stat
import sys
import time
from common import DEV_ROOT,command,create,docker_fingerprint,docker_row,encode,file_identity,host_identity,read_json,sha,verify_packet

PY_IMAGE='sha256:9534e5a8e315485d4061ed659af0fd78a284c015f9b73661b41d6bab25604534'
PG_IMAGE='sha256:4ef4dbc939d61acea57712655ddb4b4ab27419c913f94cca0cd57cb3ea3c2280'
INCUMBENT_NAME='cbm-r035-incumbent'
PG_NAME='cbm-r035-pg'
HOLD_NAMES=('automation/paused','automation/attention.json','automation/boot-state.json','automation/checkpoint.json')
LOCK_NAMES=('automation/runner.lock','files/.manual-worker.lock','files/.submission.lock')

def sql(query,*,container=PG_NAME):
 return command(['docker','exec','-i',container,'psql','-X','-qAt','-U','fixture','-d','fixture','-v','ON_ERROR_STOP=1'],input=query.encode(),timeout=15).decode().strip()

def ready_pg():
 for _ in range(60):
  try:
   command(['docker','exec',PG_NAME,'pg_isready','-U','fixture','-d','fixture'],timeout=3)
   return
  except (RuntimeError,TimeoutError):time.sleep(1)
 raise RuntimeError('synthetic PostgreSQL readiness timeout')

def ready_incumbent(ident):
 code="import urllib.request;assert urllib.request.urlopen('http://127.0.0.1:8080',timeout=2).status==200"
 for _ in range(30):
  try:
   command(['docker','exec',ident,'python','-B','-c',code],timeout=5)
   return
  except (RuntimeError,TimeoutError):time.sleep(.3)
 raise RuntimeError('synthetic incumbent readiness timeout')

def controls(root=DEV_ROOT):
 root=Path(root)
 return {'holds':{n:file_identity(root/'state'/n) for n in HOLD_NAMES},
         'locks':{n:file_identity(root/'state'/n) for n in LOCK_NAMES}}

def setup(packet_sha):
 os.umask(0o077)
 host=host_identity(DEV_ROOT,'synthetic-development')
 root=DEV_ROOT
 marker=root/'fixture-setup.intent'
 if marker.exists() or (root/'fixture.json').exists():raise ValueError('retained fixture; no replay')
 for name in (INCUMBENT_NAME,PG_NAME):
  p=__import__('subprocess').run(['docker','inspect','--type','container',name],capture_output=True)
  if p.returncode==0:raise ValueError('container name already occupied')
 create(marker,encode({'packet_manifest_sha256':packet_sha,'host':host,'replay_allowed':False}))
 state=root/'state'
 for name in ('automation','files','corpus','config'):(state/name).mkdir(parents=True,mode=0o700,exist_ok=False)
 for name in LOCK_NAMES:create(state/name,b'')
 create(state/'automation/paused',b'{"reason":"synthetic_stage2_held"}\n')
 create(state/'automation/attention.json',b'{"state":"synthetic_attention_retained"}\n')
 create(state/'automation/boot-state.json',encode({'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip(),'reconciled':False}))
 create(state/'automation/checkpoint.json',b'{"state":"unacknowledged_synthetic"}\n')
 create(state/'corpus/source.txt',b'Request035 synthetic corpus. No production content.\n')
 create(state/'config/profile.json',b'{"provider":"synthetic","paid_calls":false}\n')
 (root/'control').mkdir(mode=0o700)
 (root/'journal').mkdir(mode=0o700)
 create(root/'control/admission.json',encode({'open':False,'reason':'fixture setup; no reviewed operation'}))
 command(['docker','run','-d','--name',PG_NAME,'--network','none','--restart','no','--memory','384m','--cpus','0.5',
         '-e','POSTGRES_HOST_AUTH_METHOD=trust','-e','POSTGRES_USER=fixture','-e','POSTGRES_DB=fixture',
         '-v','cbm-r035-pg:/var/lib/postgresql',PG_IMAGE],timeout=45)
 ready_pg()
 sql("CREATE ROLE cbm_runtime LOGIN; CREATE ROLE cbm_migration LOGIN; GRANT CONNECT ON DATABASE fixture TO cbm_runtime,cbm_migration; CREATE TABLE IF NOT EXISTS stage2_items(id integer primary key, label text not null); INSERT INTO stage2_items(id,label) VALUES (1,'synthetic') ON CONFLICT DO NOTHING;")
 ident=command(['docker','run','-d','--name',INCUMBENT_NAME,'--network','none','--restart','unless-stopped',
               '--memory','64m','--cpus','0.25','--read-only','--cap-drop','ALL','--security-opt','no-new-privileges',
               PY_IMAGE,'python','-B','-m','http.server','8080','--bind','127.0.0.1'],timeout=45).decode().strip()
 ready_incumbent(ident)
 row=docker_row(ident)
 if row['Image']!=PY_IMAGE or row['Name']!='/'+INCUMBENT_NAME or row['Mounts'] or row['HostConfig']['NetworkMode']!='none':
  raise ValueError('unexpected synthetic incumbent')
 pg_id=command(['docker','inspect','--format','{{.Id}}',PG_NAME]).decode().strip()
 proof={'schema':'cbm.stage2-fixture/1','scope':'synthetic-development','host':host,
        'packet_sha256':packet_sha,'incumbent_id':ident,'incumbent_image':PY_IMAGE,
        'incumbent_fingerprint':docker_fingerprint(row),'postgres_id':pg_id,'postgres_image':PG_IMAGE,
        'controls':controls(root),'database_acl_before':sql("SELECT datacl::text FROM pg_database WHERE datname='fixture'"),
        'database_system_identifier':command(['docker','exec',PG_NAME,'pg_controldata','/var/lib/postgresql/18/docker'],timeout=10).decode(errors='replace').split('Database system identifier:')[-1].splitlines()[0].strip(),
        'paid_provider_requests':0,'vm101_changes':False,'production_changes':False}
 create(root/'fixture.json',encode(proof))
 return {'fixture_sha256':sha(encode(proof)),'incumbent_id':ident,'postgres_id':pg_id,
         'exact_images':True,'root':str(root),'host':host}

def inspect():
 proof=read_json(DEV_ROOT/'fixture.json')
 if host_identity(DEV_ROOT,'synthetic-development')!=proof['host']:raise ValueError('host drift')
 row=docker_row(proof['incumbent_id'])
 if row['Image']!=proof['incumbent_image'] or docker_fingerprint(row)!=proof['incumbent_fingerprint']:
  raise ValueError('incumbent drift')
 if controls()!=proof['controls']:raise ValueError('control drift')
 pg=docker_row(proof['postgres_id'])
 if pg['Image']!=proof['postgres_image']:raise ValueError('PostgreSQL image drift')
 return {'incumbent_running':row['State']['Running'],'postgres_running':pg['State']['Running'],
         'controls_equal':True,'host_equal':True,'incumbent_id':row['Id'],'postgres_id':pg['Id']}

if __name__=='__main__':
 mode=sys.argv[1]
 expected=sys.argv[2]
 verify_packet(Path(__file__).resolve().parent,expected,owner_uid=0)
 if mode=='setup':print(json.dumps(setup(expected)))
 elif mode=='inspect':print(json.dumps(inspect()))
 else:raise SystemExit(2)

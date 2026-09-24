"""VM-owned independent recovery. Never removes holds, journals, or partials."""
import json
import os
from pathlib import Path
import sys
import time
from common import DEV_ROOT,command,docker_fingerprint,docker_row,encode,host_identity,read_json,replace,sha,verify_packet
from controller import ACTIVE,ADMISSION,held_locks,release
from fixture_vm import controls,sql

def finalize(packet_sha):
 verify_packet(Path(__file__).resolve().parent,packet_sha,owner_uid=0)
 if not ACTIVE.exists():return {'state':'no_intent'}
 active=read_json(ACTIVE)
 directory=DEV_ROOT/'journal'/active['attempt']
 intent=read_json(directory/'intent.json')
 if sha(encode(intent))!=active['intent_sha256']:raise ValueError('intent integrity failed')
 plan=read_json(DEV_ROOT/'plan.json')
 if sha(encode(plan))!=intent['plan_sha256'] or plan['packet_manifest_sha256']!=packet_sha:
  raise ValueError('plan integrity failed')
 result=directory/'result.json'
 if result.exists():return read_json(result)
 outcome={'attempt':intent['attempt'],'intent_sha256':active['intent_sha256'],
          'finalizer_at':time.time(),'serving_restored':False,'admission_open':False,
          'partial_retained':True,'database_restored':False,'incumbent_restored':False,
          'errors':[]}
 locks=None
 try:
  if host_identity(DEV_ROOT,'synthetic-development')!=plan['host']:
   raise ValueError('host/mount drift')
  if controls()!=plan['controls']:raise ValueError('protected control drift')
  if (DEV_ROOT/'control/fault.json').exists() and read_json(DEV_ROOT/'control/fault.json').get('mode')=='finalizer_fail':
   raise RuntimeError('synthetic finalizer failure')
  locks=held_locks()
  try:
   pg=docker_row(intent['postgres_id'])
   if pg['Image']!=plan['postgres_image'] or not pg['State']['Running']:
    raise ValueError('exact PostgreSQL unavailable')
   sql('GRANT CONNECT ON DATABASE fixture TO cbm_runtime, cbm_migration;')
   acl=sql("SELECT datacl::text FROM pg_database WHERE datname='fixture'")
   if acl!=read_json(DEV_ROOT/'fixture.json')['database_acl_before']:
    raise ValueError('database ACL restoration mismatch')
   outcome['database_restored']=True
  except BaseException as exc:outcome['errors'].append('database: '+type(exc).__name__+': '+str(exc))
  try:
   row=docker_row(intent['incumbent_id'])
   if row['Image']!=plan['incumbent_image'] or docker_fingerprint(row)!=plan['incumbent_fingerprint']:
    raise ValueError('exact incumbent changed')
   if not row['State']['Running']:
    command(['docker','start',row['Id']],timeout=20)
   row=docker_row(row['Id'])
   if not row['State']['Running']:raise ValueError('same incumbent did not start')
   command(['docker','exec',row['Id'],'python','-B','-c',
            "import urllib.request;assert urllib.request.urlopen('http://127.0.0.1:8080',timeout=2).status==200"],timeout=10)
   outcome['incumbent_restored']=True
  except BaseException as exc:outcome['errors'].append('incumbent: '+type(exc).__name__+': '+str(exc))
  if controls()!=plan['controls']:outcome['errors'].append('protected controls changed during finalization')
  outcome['serving_restored']=outcome['database_restored'] and outcome['incumbent_restored'] and not outcome['errors']
 except BaseException as exc:outcome['errors'].append(type(exc).__name__+': '+str(exc))
 finally:
  if locks is not None:release(locks)
  replace(ADMISSION,encode({'open':False,'reason':'finalizer complete' if outcome['serving_restored'] else 'finalizer failed; manual reconciliation required',
                            'attempt':intent['attempt']}))
  replace(result,encode(outcome))
 return outcome

def guardian(packet_sha):
 verify_packet(Path(__file__).resolve().parent,packet_sha,owner_uid=0)
 if not ACTIVE.exists():return {'state':'idle'}
 active=read_json(ACTIVE)
 intent=read_json(DEV_ROOT/'journal'/active['attempt']/'intent.json')
 if sha(encode(intent))!=active['intent_sha256']:raise ValueError('intent changed')
 result=DEV_ROOT/'journal'/active['attempt']/'result.json'
 if result.exists():return {'state':'retained_result'}
 now=time.time()
 if now<intent['restore_deadline']:
  return {'state':'within_bound','seconds_remaining':intent['restore_deadline']-now}
 # The independent timer kills a frozen worker. systemd also runs ExecStopPost.
 # Kill only the main process. Killing the cgroup also kills ExecStopPost.
 import subprocess
 subprocess.run(['systemctl','kill','--kill-whom=main','--signal=KILL','cbm-r035-worker.service'],
                capture_output=True,timeout=8)
 command(['systemctl','start','--no-block','cbm-r035-finalizer.service'],timeout=8)
 return {'state':'deadline_expired','worker_killed':True,'finalizer_requested':True}

if __name__=='__main__':
 os.umask(0o077)
 mode=sys.argv[1]
 if mode=='finalize':out=finalize(sys.argv[2])
 elif mode=='guardian':out=guardian(sys.argv[2])
 else:raise SystemExit(2)
 print(json.dumps(out,sort_keys=True))

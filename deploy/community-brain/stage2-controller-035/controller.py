"""One-shot development admission and worker; every effect follows durable intent."""
import fcntl
import json
import os
from pathlib import Path
import re
import sys
import time
from common import DEV_ROOT,command,create,docker_row,encode,locked_file,read_json,replace,sha,verify_packet
from fixture_vm import LOCK_NAMES,controls,sql
from plan import load_pinned

ACTIVE=DEV_ROOT/'journal/active.json'
ADMISSION=DEV_ROOT/'control/admission.json'
KIND={'scheduler','manual','capture'}
ATTEMPT=re.compile(r'^r035-[a-z0-9-]{8,56}$')

def held_locks():
 acquired=[]
 try:
  for name in LOCK_NAMES:
   fd,identity=locked_file(DEV_ROOT/'state'/name)
   acquired.append((fd,name,identity))
  return acquired
 except BaseException:
  for fd,_,_ in acquired:os.close(fd)
  raise

def release(locks):
 for fd,_,_ in reversed(locks):os.close(fd)

def read_active():
 return read_json(ACTIVE) if ACTIVE.exists() else None

def admission(kind,attempt,expected,packet_sha):
 if kind not in KIND or not ATTEMPT.fullmatch(attempt):raise ValueError('kind/attempt invalid')
 verify_packet(Path(__file__).resolve().parent,packet_sha,owner_uid=0)
 plan=load_pinned(expected,packet_sha)
 locks=held_locks()
 try:
  if ACTIVE.exists():
   prior=read_active()
   result=DEV_ROOT/'journal'/prior['attempt']/'result.json'
   if not result.exists() or read_json(result).get('serving_restored') is not True:
    raise ValueError('unresolved prior intent; admission closed')
  if (DEV_ROOT/'journal'/attempt).exists():raise ValueError('attempt replay refused')
  if read_json(ADMISSION).get('open') is not False:raise ValueError('admission state changed')
  directory=DEV_ROOT/'journal'/attempt
  directory.mkdir(mode=0o700)
  now=time.time()
  intent={'schema':'cbm.stage2-intent/1','scope':'synthetic-development','attempt':attempt,'kind':kind,
          'plan_sha256':expected,'packet_manifest_sha256':packet_sha,'created_at':now,
          'overall_deadline':now+plan['deadlines_seconds']['overall'],
          'restore_deadline':now+plan['deadlines_seconds']['restore'],
          'phase_deadlines':{'stop':now+plan['deadlines_seconds']['stop'],
                             'db':now+plan['deadlines_seconds']['stop']+plan['deadlines_seconds']['db'],
                             'work':now+plan['deadlines_seconds']['stop']+plan['deadlines_seconds']['db']+plan['deadlines_seconds']['work']},
          'incumbent_id':plan['incumbent_id'],'postgres_id':plan['postgres_id'],
          'rollback_owner':plan['rollback_owner'],'replay_allowed':False}
  create(directory/'intent.json',encode(intent))
  create(ACTIVE,encode({'attempt':attempt,'intent_sha256':sha(encode(intent))})) if not ACTIVE.exists() else replace(ACTIVE,encode({'attempt':attempt,'intent_sha256':sha(encode(intent))}))
  replace(ADMISSION,encode({'open':False,'reason':'durable intent','attempt':attempt}))
 finally:release(locks)
 # The VM owns this systemd worker/finalizer. A lost SSH reply leaves the intent
 # visible; the caller may only read back the exact attempt, never submit again.
 try:command(['systemctl','start','--no-block','cbm-r035-worker.service'],timeout=8)
 except BaseException:
  command(['systemctl','start','--no-block','cbm-r035-finalizer.service'],timeout=8)
  raise
 return {'attempt':attempt,'intent_sha256':sha(encode(intent)),'admission':'closed','worker_started':True}

def worker(packet_sha):
 verify_packet(Path(__file__).resolve().parent,packet_sha,owner_uid=0)
 active=read_active()
 if not active:raise ValueError('no active intent')
 directory=DEV_ROOT/'journal'/active['attempt']
 intent=read_json(directory/'intent.json')
 if sha(encode(intent))!=active['intent_sha256']:raise ValueError('intent changed')
 plan=load_pinned(intent['plan_sha256'],packet_sha)
 if time.time()>intent['overall_deadline']:raise ValueError('deadline expired')
 locks=held_locks()
 try:
  if controls()!=plan['controls']:raise ValueError('controls drift before effect')
  if time.time()>intent['phase_deadlines']['stop']:raise ValueError('stop phase deadline')
  row=docker_row(intent['incumbent_id'])
  if not row['State']['Running']:raise ValueError('incumbent not initially serving')
  create(directory/'phase-stop.json',encode({'at':time.time(),'incumbent_id':row['Id'],'deadline':intent['phase_deadlines']['stop']}))
  command(['docker','stop','--time','8',row['Id']],timeout=plan['deadlines_seconds']['stop'])
  row=docker_row(row['Id'])
  if row['State']['Running']:raise ValueError('exact incumbent stop unconfirmed')
  if controls()!=plan['controls'] or time.time()>intent['phase_deadlines']['db']:
   raise ValueError('control drift or DB phase deadline')
  create(directory/'phase-db.json',encode({'at':time.time(),'postgres_id':intent['postgres_id'],'deadline':intent['phase_deadlines']['db']}))
  sql('REVOKE CONNECT ON DATABASE fixture FROM cbm_runtime, cbm_migration;')
  if controls()!=plan['controls'] or time.time()>intent['phase_deadlines']['work']:
   raise ValueError('control drift or work phase deadline')
  create(directory/'phase-work.json',encode({'at':time.time(),'operation':'synthetic no-op','paid_calls':0,
                                         'deadline':intent['phase_deadlines']['work']}))
  # Fault injection is restricted to the synthetic fixture, never the product.
  fault=DEV_ROOT/'control/fault.json'
  if fault.exists():
   mode=read_json(fault).get('mode')
   if mode=='worker_wait':time.sleep(120)
   if mode=='worker_fail':raise RuntimeError('synthetic worker failure')
  return {'attempt':intent['attempt'],'worker':'finished','finalizer':'systemd-owned'}
 finally:release(locks)

def readback(attempt,expected_intent):
 if not ATTEMPT.fullmatch(attempt):raise ValueError('bad attempt')
 active=read_active()
 if not active or active!={'attempt':attempt,'intent_sha256':expected_intent}:
  raise ValueError('foreign or stale readback')
 directory=DEV_ROOT/'journal'/attempt
 intent=read_json(directory/'intent.json')
 if sha(encode(intent))!=expected_intent:raise ValueError('intent readback drift')
 result=read_json(directory/'result.json') if (directory/'result.json').exists() else None
 return {'attempt':attempt,'intent_sha256':expected_intent,'result':result,
         'incumbent_running':docker_row(intent['incumbent_id'])['State']['Running'],
         'admission':read_json(ADMISSION)}

if __name__=='__main__':
 os.umask(0o077)
 mode=sys.argv[1]
 if mode=='admit':out=admission(*sys.argv[2:6])
 elif mode=='worker':out=worker(sys.argv[2])
 elif mode=='readback':out=readback(sys.argv[2],sys.argv[3])
 else:raise SystemExit(2)
 print(json.dumps(out,sort_keys=True))

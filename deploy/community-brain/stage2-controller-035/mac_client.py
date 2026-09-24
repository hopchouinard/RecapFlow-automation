"""Mac-only shared scheduler mutex and no-replay SSH admission/readback."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from common import encode,sha

LOCAL=Path.home()/'.local/state/community-brain-management'
REQUEST=LOCAL/'request035'
PIN=REQUEST/'external-plan-pin.json'
PENDING=REQUEST/'pending-attempt.json'
HOST='pchouinard@10.1.30.20'
ROOT='/srv/dev-data/workspaces/cbm-stage2-controller-20260924-035'
HEX=re.compile(r'^[0-9a-f]{64}$')

def current_packet():
 pin=json.loads(PIN.read_text())
 revision=pin['revision']
 if not re.fullmatch(r'packet-v[1-9][0-9]*',revision):raise ValueError('unsafe packet revision')
 return ROOT+'/'+revision

def remote(args):
 p=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8',HOST,
                   ' '.join(__import__('shlex').quote(x) for x in ['sudo','python3','-B',current_packet()+'/controller.py',*args])],
                  capture_output=True,timeout=20)
 if p.returncode:raise RuntimeError('SSH outcome uncertain; readback required')
 return json.loads(p.stdout)

def pin(plan_sha,packet_sha,revision):
 if not HEX.fullmatch(plan_sha) or not HEX.fullmatch(packet_sha):raise ValueError('invalid hash')
 if not re.fullmatch(r'packet-v[1-9][0-9]*',revision):raise ValueError('invalid packet revision')
 identity=json.loads((REQUEST/(revision+'-identity.json')).read_text())
 if identity['manifest_sha256']!=packet_sha or identity['remote_path']!=ROOT+'/'+revision:
  raise ValueError('packet identity mismatch')
 if PIN.exists() and PENDING.exists():raise ValueError('pending attempt blocks pin revision')
 p=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8',HOST,
                   "sudo cat "+ROOT+'/plan.json'],capture_output=True,timeout=12,check=True)
 if sha(p.stdout)!=plan_sha:raise ValueError('external plan hash mismatch')
 plan=json.loads(p.stdout)
 if plan['packet_manifest_sha256']!=packet_sha or plan['scope']!='synthetic-development':
  raise ValueError('plan scope or packet changed')
 if PIN.exists():
  old=PIN.read_bytes()
  archived=REQUEST/('retired-pin-'+sha(old)+'.json')
  fd=os.open(archived,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
  with os.fdopen(fd,'wb') as out:out.write(old);out.flush();os.fsync(out.fileno())
 temp=PIN.with_suffix('.tmp')
 fd=os.open(temp,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
 with os.fdopen(fd,'wb') as out:out.write(encode({'plan_sha256':plan_sha,'packet_manifest_sha256':packet_sha,'revision':revision,'scope':'synthetic-development'}));out.flush();os.fsync(out.fileno())
 os.replace(temp,PIN)
 return {'external_plan_pin_sha256':sha(PIN.read_bytes()),'plan_sha256':plan_sha}

def admit(kind,attempt):
 if PENDING.exists():raise ValueError('pending attempt needs readback; no replay')
 pinned=json.loads(PIN.read_text())
 lock=LOCAL/'scheduler.lock'  # Request029's existing Mac mutex.
 with lock.open('a') as stream:
  fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
  if PENDING.exists():raise ValueError('pending attempt needs readback')
  fd=os.open(PENDING,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
  with os.fdopen(fd,'wb') as out:
   out.write(encode({'kind':kind,'attempt':attempt,'plan_sha256':pinned['plan_sha256'],
                     'packet_manifest_sha256':pinned['packet_manifest_sha256'],'outcome':'unknown'}));out.flush();os.fsync(out.fileno())
  result=remote(['admit',kind,attempt,pinned['plan_sha256'],pinned['packet_manifest_sha256']])
  if os.environ.get('CBM_R035_DROP_ACK')=='1':
   raise RuntimeError('synthetic SSH acknowledgement lost; exact readback required')
  temp=PENDING.with_suffix('.tmp')
  fd=os.open(temp,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
  with os.fdopen(fd,'wb') as out:
   out.write(encode({**json.loads(PENDING.read_text()),'intent_sha256':result['intent_sha256'],'outcome':'admitted'}))
   out.flush();os.fsync(out.fileno())
  os.replace(temp,PENDING)
  return result

def readback():
 pending=json.loads(PENDING.read_text())
 if 'intent_sha256' not in pending:
  # Read the pinned active intent identity, never retry an uncertain admission.
  code="import json,pathlib;root=pathlib.Path('"+ROOT+"');active=json.loads((root/'journal/active.json').read_text());intent=json.loads((root/'journal'/active['attempt']/'intent.json').read_text());print(json.dumps({'active':active,'intent':intent}))"
  p=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8',HOST,
                    __import__('shlex').join(['sudo','python3','-B','-c',code])],capture_output=True,timeout=12)
  if p.returncode:raise RuntimeError('unknown SSH outcome retained')
  fetched=json.loads(p.stdout)
  active=fetched['active']
  if active['attempt']!=pending['attempt']:raise ValueError('foreign active attempt')
  if sha(encode(fetched['intent']))!=active['intent_sha256'] or fetched['intent']['plan_sha256']!=pending['plan_sha256'] or fetched['intent']['packet_manifest_sha256']!=pending['packet_manifest_sha256']:
   raise ValueError('foreign or changed intent')
  pending['intent_sha256']=active['intent_sha256']
 result=remote(['readback',pending['attempt'],pending['intent_sha256']])
 if result['attempt']!=pending['attempt'] or result['intent_sha256']!=pending['intent_sha256']:
  raise ValueError('foreign readback')
 if result['result'] is not None and result['result']['serving_restored']:
  PENDING.unlink()
 return result

if __name__=='__main__':
 os.umask(0o077)
 mode=sys.argv[1]
 if mode=='pin':result=pin(sys.argv[2],sys.argv[3],sys.argv[4])
 elif mode=='admit':result=admit(sys.argv[2],sys.argv[3])
 elif mode=='readback':result=readback()
 else:raise SystemExit(2)
 print(json.dumps(result,sort_keys=True))

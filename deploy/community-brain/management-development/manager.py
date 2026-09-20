"""Mac-only candidate renewal driver; exact Request024 policy and real authority."""
import fcntl
import json
import os
from pathlib import Path
import secrets
import sys
import tempfile
import time
from uuid import uuid4
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent/'incumbent'))
from authority import Authority,PROJECT,ENVIRONMENT,DEVELOPMENT_PATH
from successor import DEV_HOST,DEV_ROOT
from transport import command
from lease_supervisor import LeaseSupervisor
from service_renewal_policy import run,IDENTITIES,PENDING
LOCAL=Path.home()/'.local/state/community-brain-management/request027'

class Adapter:
 def __init__(self,lease,identity):
  self.lease=lease;self.identity=identity
  self.authority=Authority(PROJECT,ENVIRONMENT,DEVELOPMENT_PATH,lease)
  self.monitor_after=time.time()-120;self.recreations=[];self.fail=False
 def remote(self,mode,payload,timeout=240):
  with tempfile.TemporaryFile() as incoming,tempfile.TemporaryFile() as outgoing:
   incoming.write(json.dumps(payload).encode());incoming.seek(0)
   wrapper='import sys,runpy,json,traceback\nsys.path.insert(0,sys.argv[1]);sys.argv=[sys.argv[1]+"/host.py",*sys.argv[2:]]\ntry:runpy.run_path(sys.argv[0],run_name="__main__")\nexcept Exception as e:print(json.dumps({"adapter_error":type(e).__name__,"frames":[{"file":f.filename.rsplit("/",1)[-1],"line":f.lineno} for f in traceback.extract_tb(e.__traceback__)]}))'
   self.lease.run(command(DEV_HOST,['python3','-B','-c',wrapper,self.identity['remote_path'],self.identity['manifest_sha256'],mode]),timeout=timeout,stdin=incoming,stdout=outgoing)
   outgoing.seek(0);result=json.load(outgoing)
   if 'adapter_error' in result:raise RuntimeError(json.dumps(result))
   return result
 def read(self):return self.authority.read()
 def save(self,updates):self.authority.save(updates)
 def accept(self,values):self.recreations.append(self.remote('accept',values))
 def inventory(self,values):
  self.check_collector(values);self.remote('tokens',values);self.remote('cache',values)
  self.remote('consumers-verify',{'values':values,'after':self.monitor_after})
 def verify_overlap(self,journal):
  self.remote('tokens',journal['old']);self.remote('tokens',journal['updates'])
 def collector(self,values,old=None):
  p=LOCAL/'dev-collector.json'
  if old is not None:
   before=json.loads(p.read_text());assert before['token'] in [old['CB_PROD_MAC_COLLECTOR_TOKEN'],values['CB_PROD_MAC_COLLECTOR_TOKEN']]
  else:assert not p.exists()
  value={'enabled':True,'base_url':'http://api:8090','token':values['CB_PROD_MAC_COLLECTOR_TOKEN'],'expires_at':int(values['CB_PROD_MAC_COLLECTOR_EXPIRES_AT']),'scope':'development-only'}
  tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(value));tmp.chmod(0o600);tmp.replace(p)
 def check_collector(self,values):
  p=LOCAL/'dev-collector.json';v=json.loads(p.read_text())
  assert p.stat().st_mode&0o777==0o600 and v['enabled'] and v['scope']=='development-only'
  assert v['token']==values['CB_PROD_MAC_COLLECTOR_TOKEN'] and v['expires_at']==int(values['CB_PROD_MAC_COLLECTOR_EXPIRES_AT'])
 def deliver(self,journal):
  self.monitor_after=time.time();self.collector(journal['updates'],journal['old'])
  self.remote('webui-deliver',journal)
  if self.fail:
   self.fail=False;raise RuntimeError('intentional lost delivery acknowledgment')
  self.remote('consumers-deliver',journal)
 def verify_consumers(self,journal):
  self.check_collector(journal['updates']);self.remote('tokens',journal['updates'])
  self.remote('cache',journal['updates'])
  self.remote('consumers-verify',{'values':journal['updates'],'after':self.monitor_after})
 def verify_revoked(self,journal):self.remote('revoked',journal['old'])

def main(mode):
 os.umask(0o077)
 identity=json.loads((LOCAL/'packet-v7-identity.json').read_text())
 with (LOCAL/'isolated-scheduler.lock').open('a') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  job,nonce=str(uuid4()),secrets.token_hex(32)
  holder=command(DEV_HOST,['python3','-B',identity['remote_path']+'/incumbent/quiet_window.py',DEV_ROOT+'/state',job,nonce,'60'])
  with LeaseSupervisor(holder,job,nonce,interval=3,reply_timeout=20) as lease:
   adapter=Adapter(lease,identity);values=adapter.read()
   if mode=='setup':
    result=adapter.remote('setup',values,timeout=300);adapter.collector(values)
   elif mode=='install':result=adapter.remote('install',values,timeout=660)
   elif mode in ('monitors-setup','monitors-resume','worker-hold-probe','lock-probe','controls','tick','boot-inspect','accept'):result=adapter.remote(mode,values,timeout=240)
   elif mode=='inventory':adapter.inventory(values);result={'passed':True}
   elif mode=='renewal-resume':
    journal=json.loads(values[PENDING]);assert journal['phase']=='overlap_verified'
    assert len(json.loads(values[IDENTITIES]))==10
    adapter.verify_overlap(journal)
    result=run(adapter,time.time());assert result['cycle']==journal['cycle']
    assert len(json.loads(adapter.read()[IDENTITIES]))==5
    result.update(passed=True,authority='actual Infisical',same_generation_resume=True,old_and_new_overlap_verified=True,old_credentials_rejected=True,actual_monitor_consumers=True,api_recreations=adapter.recreations,production_changes=False,limits=['Synthetic corpus and embedding/model-list fixture','Collector configuration and authenticated scope probes; no desktop intake or upload exercised','Earlier interrupted attempt retained overlap after stale Kuma heartbeat'])
   elif mode=='renewal':
    marker=LOCAL/'renewal-started';assert not marker.exists();marker.touch(mode=0o600)
    adapter.fail=True
    try:run(adapter,time.time(),force=True)
    except RuntimeError as e:assert str(e)=='intentional lost delivery acknowledgment'
    else:raise AssertionError('lost delivery acknowledgment not exercised')
    persisted=adapter.read();journal=json.loads(persisted[PENDING])
    assert journal['phase']=='overlap_verified' and len(json.loads(persisted[IDENTITIES]))==10
    adapter.verify_overlap(journal)
    result=run(adapter,time.time());assert result['cycle']==journal['cycle']
    assert len(json.loads(adapter.read()[IDENTITIES]))==5
    result.update(passed=True,authority='actual Infisical',same_generation_resume=True,old_and_new_overlap_verified=True,old_credentials_rejected=True,actual_monitor_consumers=True,api_recreations=adapter.recreations,production_changes=False,limits=['Synthetic corpus and embedding/model-list fixture','Collector configuration and authenticated scope probes; no desktop intake or upload exercised'])
   else:raise ValueError('unknown mode')
   (LOCAL/(mode+'-acceptance.json')).write_text(json.dumps(result,indent=2)+'\n')
   print(json.dumps(result))
if __name__=='__main__':main(sys.argv[1])

"""Publish safe host/management checkpoint status through the existing exporter."""
import json
import subprocess
from transport import command,VM


def publish(*,failed=False):
    code='FAILED='+repr(failed)+'\n'+r'''
import pathlib,json,time,datetime,subprocess,os,tempfile
root=pathlib.Path('/srv/community-brain/automation')
def read(name):
 p=root/name
 return json.loads(p.read_text()) if p.exists() else {}
def timestamp(value):return datetime.datetime.fromisoformat(value.replace('Z','+00:00')).timestamp() if value else 0
if FAILED:
 p=root/'management-attention.json'
 if not p.exists():
  fd,tmp=tempfile.mkstemp(dir=root,prefix='.management-attention.')
  with os.fdopen(fd,'w') as f:os.fchmod(f.fileno(),0o600);json.dump({'reason':'checkpoint_management_failed_requires_reconciliation','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},f);f.flush();os.fsync(f.fileno())
  os.replace(tmp,p)
status=read('status.json');pending=read('checkpoint-needed.json')
api=json.loads(subprocess.check_output(['docker','inspect','community-brain-production-staging-api-1']))[0]
enabled='CB_AUTOMATIC_PROCESSING=true' in api['Config']['Env']
workers=bool(subprocess.check_output(['docker','ps','-q','--filter','label=cbm.automatic-stage=true']).strip())
values={'management_last_success_timestamp_seconds':time.time() if not FAILED else 0,
 'host_last_tick_timestamp_seconds':timestamp(status.get('checked_at')),
 'checkpoint_pending_since_timestamp_seconds':timestamp(pending.get('requested_at')),
 'attention':int((root/'attention.json').exists() or (root/'management-attention.json').exists()),
 'paused':int((root/'paused').exists()),'enabled':int(enabled),'worker_running':int(workers)}
p=pathlib.Path('/var/lib/prometheus/node-exporter/community-brain-automatic.prom')
body=''.join('community_brain_automatic_'+k+' '+str(v)+'\n' for k,v in values.items())
fd,tmp=tempfile.mkstemp(dir=p.parent,prefix='.cbm-automatic-')
with os.fdopen(fd,'w') as f:os.fchmod(f.fileno(),0o644);f.write(body);f.flush();os.fsync(f.fileno())
os.replace(tmp,p)
print(json.dumps({'enabled':enabled,'pending':bool(pending),'attention':bool(values['attention']),'paused':bool(values['paused'])}))
'''
    result=subprocess.run(command(VM,['python3','-c',code]),capture_output=True,text=True,timeout=30)
    if result.returncode:raise RuntimeError('automatic management monitoring unavailable')
    return json.loads(result.stdout)


if __name__=='__main__':print(json.dumps(publish()))

"""Existing scheduler entry; isolated mode inventories without rotating."""
import fcntl
import json
import os
from pathlib import Path
import secrets
import sys
import time
import traceback
from uuid import uuid4
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'automatic-recovery'))
from lease_supervisor import LeaseSupervisor
from transport import VM, command
from checkpoint_acceptance import atomic
from service_renewal_live import Adapter
from service_renewal_policy import run, due, validate

STATE=Path.home()/'.local/state/community-brain-management'


def main():
    os.umask(0o077)
    handles=[]
    for name in ([] if os.environ.get('CBM_SCHEDULER_LOCK_HELD')=='1' else ['scheduler.lock'])+['renewal.lock']:
        f=(STATE/name).open('a');handles.append(f)
        fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
    mode=os.environ.get('CBM_RENEW_MODE','scheduled')
    assert mode in ('scheduled','inventory','force')
    from secret_store import read
    values=read()
    if mode=='scheduled' and not due(values,time.time()):
        result={'state':'not_due','next_due':min(r['expires_at'] for r in validate(values))-3*86400}
    else:
        job,nonce=str(uuid4()),secrets.token_hex(32)
        with LeaseSupervisor(command(VM,['python3','-B','-u','/usr/local/lib/community-brain-automatic/quiet_window.py',
                             '/srv/community-brain',job,nonce,'30']),job,nonce,interval=3,reply_timeout=10) as lease:
            adapter=Adapter(lease)
            if mode=='inventory':
                adapter.inventory(values);result={'state':'inventory_verified','subjects':5}
            else:result=run(adapter,time.time(),force=mode=='force')
    result['checked_at']=time.time()
    atomic(STATE/'service-renewal-status.json',result)
    print(json.dumps(result))


if __name__=='__main__':
    try:main()
    except Exception as error:
        # Exception class only: adapters/HTTP failures can carry sensitive data.
        frames=[{'file':Path(f.filename).name,'line':f.lineno} for f in traceback.extract_tb(error.__traceback__)]
        atomic(STATE/'service-renewal-status.json',{'state':'failed','error_class':type(error).__name__,'frames':frames,'checked_at':time.time()})
        print('Service renewal failed; overlap/consumer state retained for reconciliation',file=sys.stderr)
        raise SystemExit(1) from None

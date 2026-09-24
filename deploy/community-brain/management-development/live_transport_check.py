"""Real Mac -> VM108 SSH/lease checks; no runtime consumer or authority writes."""
import fcntl
import hashlib
import json
from pathlib import Path
import secrets
import subprocess
import sys
import time
from uuid import uuid4

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent / 'incumbent'))
from lease_supervisor import LeaseSupervisor, LeaseLost
from transport import Transport, command
from successor import DEV_HOST, DEV_ROOT


def main(output):
    local = Path(output).parent
    lock = local / 'isolated-scheduler.lock'
    with lock.open('a') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        other = subprocess.run([sys.executable, '-B', '-c',
            'import fcntl,sys; f=open(sys.argv[1],"a"); fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)',
            str(lock)], capture_output=True)
        assert other.returncode != 0
        job, nonce = str(uuid4()), secrets.token_hex(32)
        holder = command(DEV_HOST, ['python3', '-B', DEV_ROOT+'/packet/incumbent/quiet_window.py',
            DEV_ROOT+'/state', job, nonce, '15'])
        with LeaseSupervisor(holder, job, nonce, interval=1, reply_timeout=5) as lease:
            transport = Transport(lease)
            # Verify every real remote advisory lock is held by the lease.
            code = 'ROOT='+repr(DEV_ROOT+'/state')+'\n'+'''
import pathlib,fcntl,json
held=[]
for n in ('automation/runner.lock','files/.manual-worker.lock','files/.submission.lock'):
 with (pathlib.Path(ROOT)/n).open('r+') as f:
  try:fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:held.append(n)
print(json.dumps({'held':held}))
'''
            locked = transport.json(DEV_HOST, code)
            assert len(locked['held']) == 3
            effect = DEV_ROOT+'/state/transport-effect.json'
            intent = local / 'transport-intent.json'
            assert not intent.exists(), 'inspect prior isolated effect; do not replay'
            intent.write_text(json.dumps({'state':'intended','remote_path':effect}))
            intent.chmod(0o600)
            # The real SSH effect happens, but its process exits before replying.
            code = 'PATH='+repr(effect)+'\n'+'''
import pathlib,json,os
p=pathlib.Path(PATH);assert not p.exists();p.write_text(json.dumps({'executions':1}));p.chmod(0o600)
os._exit(23)
'''
            try:
                transport.json(DEV_HOST, code)
            except RuntimeError:
                pass
            else:
                raise AssertionError('lost response did not fail closed')
            observed = transport.json(DEV_HOST,
                'import pathlib,json;print((pathlib.Path('+repr(effect)+')).read_text())')
            assert observed == {'executions':1}
            intent.write_text(json.dumps({'state':'reconciled_by_readback','executions':1}))
            lease._terminate(lease.process)
            try:
                lease.check()
            except LeaseLost:
                pass
            else:
                raise AssertionError('lost lease accepted')
        result = {'real_ssh':True,'isolated_scheduler_mutex_exclusion':True,
            'ordered_remote_locks_held':locked['held'],'lost_effect_response_detected':True,
            'effect_reconciled_without_replay':True,'remote_effect_executions':1,
            'lost_lease_fails_closed':True,
            'limits':['Dedicated development lock files; application lock participation not yet tested.',
                      'No credential delivery, renewal, Infisical or monitor acceptance claimed.']}
        Path(output).write_text(json.dumps(result,indent=2)+'\n')
        Path(output).chmod(0o600)
        print(json.dumps(result))


if __name__ == '__main__':
    main(sys.argv[1])

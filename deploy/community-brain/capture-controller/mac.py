"""Candidate Mac entry point. Existing scheduler mutex, durable intent, no replay."""
import fcntl,json,os,shlex,subprocess,sys,time
from pathlib import Path
import common as c
r=c.r
STATE=Path.home()/'.local/state/community-brain-management/request031'
MUTEX=Path.home()/'.local/state/community-brain-management/scheduler.lock'

def remote(s,sha,operation):
    path=str(Path(s['packet'])/'target.py');spec=str(c.ROOT/'specs'/(s['operation_id']+'.json'))
    args=['sudo','-n','python3','-B',path,operation,spec,sha]
    return ['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8',c.HOST,shlex.join(args)]

def readback(s,sha):
    p=subprocess.run(remote(s,sha,'readback'),capture_output=True,timeout=15)
    if p.returncode:raise RuntimeError('remote readback unavailable; pending retained')
    return json.loads(p.stdout)

def finish(s,sha):
    value=readback(s,sha)
    safe=value.get('state') in ('completed','aborted_restored') and value.get('live_verified') and value.get('finalizer_seen') and value.get('service_state') in ('inactive','failed')
    if safe:
        c.atom(STATE/(s['operation_id']+'-readback.json'),value)
        pending=json.loads(r.stable_bytes(STATE/'pending.json'))
        if pending['spec_sha256']!=sha or pending['owner_id']!=s['owner_id']:raise ValueError('foreign pending intent')
        (STATE/'pending.json').rename(STATE/(s['operation_id']+'-resolved-intent.json'))
    return value,safe

def main():
    mode,specfile=sys.argv[1:];s=json.loads(r.stable_bytes(Path(specfile)));sha=r.sha(r.stable_bytes(Path(specfile)))
    if sys.platform!='darwin' or s.get('scope')!='synthetic-development':raise ValueError('Mac synthetic scope only')
    if not Path(s['packet']).is_relative_to(c.ROOT) or '/' in s['operation_id']:raise ValueError('foreign packet')
    STATE.mkdir(mode=0o700,exist_ok=True)
    fd=os.open(MUTEX,os.O_RDWR|os.O_NOFOLLOW)
    try:
        fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        if mode=='dispatch':
            if (STATE/'pending.json').exists():raise ValueError('unresolved pending operation; reconcile only')
            if (STATE/(s['operation_id']+'-intent.json')).exists():raise ValueError('local operation cannot replay')
            intent={'owner_id':s['owner_id'],'operation_id':s['operation_id'],'spec_sha256':sha,'at':time.time(),'pid':os.getpid()}
            r.write_new(STATE/(s['operation_id']+'-intent.json'),r.encode(intent));r.write_new(STATE/'pending.json',r.encode(intent))
            # The SSH waiter is disposable; target systemd owns the actual operation.
            client=subprocess.Popen(remote(s,sha,'dispatch-wait'),stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
            c.atom(STATE/'client.json',dict(intent,ssh_pid=client.pid))
            try:client.wait(timeout=max(1,s['deadlines']['validate_by']-time.time()+10))
            except subprocess.TimeoutExpired:client.kill();client.wait()
        elif mode=='reconcile':
            pending=json.loads(r.stable_bytes(STATE/'pending.json'))
            if pending['spec_sha256']!=sha or pending['owner_id']!=s['owner_id']:raise ValueError('foreign pending owner')
        else:raise ValueError('unknown management operation')
        limit=s['deadlines']['validate_by']+20
        while True:
            value,safe=finish(s,sha)
            if safe:print(json.dumps(value));return
            if time.time()>=limit or value.get('state') in ('uncertain','absent','refused'):raise RuntimeError('unresolved target state; pending retained')
            time.sleep(.3)
    finally:os.close(fd)

if __name__=='__main__':main()

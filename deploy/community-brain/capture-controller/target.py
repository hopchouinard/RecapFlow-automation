"""Detached VM108 supervisor plus independent systemd recovery finalizer."""
import fcntl,json,os,signal,subprocess,sys,time
from pathlib import Path
import common as c
import database as db
r=c.r

def restore_serving(s):
    op=Path(s['operation'])
    if not (op/'stop-intent.json').exists():return c.healthy(s)
    row=c.verify_incumbent(s)
    if not row['State']['Running']:
        # Reconcile the exact stopped ID; never create or replace a container.
        c.event(op,'restart_intent',container_id=row['Id'],observed_state=row['State']['Status'])
        c.command(['docker','start',row['Id']],timeout=4)
    for _ in range(8):
        if c.healthy(s):
            c.atom(op/'serving-restored.json',{'container_id':row['Id'],'fingerprint':s['incumbent']['fingerprint'],'healthy':True,'at':time.time()})
            return True
        time.sleep(.15)
    return False

def terminal(s,sha,outcome,reason):
    op=Path(s['operation']);holds=r.hold_state(s['holds'])==s['hold_bindings']
    health=c.healthy(s)
    value={'schema':'cbm.capture-terminal/1','operation_id':s['operation_id'],'owner_id':s['owner_id'],'spec_sha256':sha,'state':outcome if health and holds else 'uncertain','reason':reason,'incumbent_healthy':health,'holds_equal':holds,'at':time.time(),'replay_allowed':False,'production_qualified':False}
    if (op/'serving-restored.json').exists():value['serving_restored_at']=json.loads(r.stable_bytes(op/'serving-restored.json'))['at']
    c.atom(op/'terminal.json',value)
    c.atom(c.ROOT/'active.json',{'operation_id':s['operation_id'],'spec_sha256':sha,'state':value['state']})
    return value

def supervisor(spec_path,sha):
    s=c.load_spec(spec_path,sha);op=Path(s['operation'])
    fd=os.open(c.ROOT/'controller.lock',os.O_RDWR|os.O_NOFOLLOW)
    fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
    worker=None
    try:
        active=c.ROOT/'active.json'
        if active.exists():
            old=json.loads(r.stable_bytes(active))
            if old['state'] not in ('completed','aborted_restored'):raise ValueError('unresolved target owner')
        with r.quiet(s['locks'],s['holds']):
            if r.hold_state(s['holds'])!=s['hold_bindings']:raise ValueError('hold binding changed')
            c.atom(active,{'operation_id':s['operation_id'],'spec_sha256':sha,'state':'running'})
            if not c.healthy(s):raise ValueError('incumbent not healthy')
            if time.time()>=s['deadlines']['prepare_by']:raise ValueError('prepare deadline expired')
            r.write_new(op/'guardian.json',r.encode({'pid':os.getpid(),'owner_id':s['owner_id'],'operation_id':s['operation_id'],'spec_sha256':sha,'at':time.time()}))
            r.write_new(op/'stop-intent.json',r.encode({'container_id':s['incumbent']['id'],'fingerprint':s['incumbent']['fingerprint'],'at':time.time()}))
            c.event(op,'stop_intent',container_id=s['incumbent']['id'])
            c.command(['docker','stop','--time','1',s['incumbent']['id']],timeout=4)
            if c.verify_incumbent(s)['State']['Running']:raise ValueError('incumbent stop unconfirmed')
            worker=subprocess.Popen([sys.executable,'-B',str(Path(__file__).with_name('worker.py')),str(spec_path),sha],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            r.write_new(op/'worker.json',r.encode({'pid':worker.pid,'at':time.time()}))
            reason='worker_failure';completed=False
            while worker.poll() is None:
                now=time.time()
                captured=(op/'capture-ready.json').exists()
                if captured and not (op/'serving-restored.json').exists():
                    if not restore_serving(s):raise ValueError('serving restoration failed')
                if now>=s['deadlines']['capture_by'] and not captured:
                    reason='capture_deadline';break
                if now>=s['deadlines']['validate_by']:
                    reason='validation_deadline';break
                if (op/'fence.json').exists() and not (op/'fence-release-intent.json').exists():
                    if not db.fence_alive(s,json.loads(r.stable_bytes(op/'fence.json'))):
                        reason='database_fence_lost';break
                time.sleep(.15)
            if worker.poll() is None:
                worker.terminate()
                try:worker.wait(timeout=1)
                except subprocess.TimeoutExpired:worker.kill();worker.wait(timeout=1)
            db.release_fence(s)
            if not restore_serving(s):raise ValueError('incumbent recovery unavailable')
            if worker.returncode==0 and (op/'worker-result.json').exists():
                result=json.loads(r.stable_bytes(op/'worker-result.json'))
                db.verify_evidence(op/'evidence',s,result['manifest_sha256'])
                completed=True;reason='verified_capture_and_database_restore'
            terminal(s,sha,'completed' if completed else 'aborted_restored',reason)
    except BaseException as exc:
        c.event(op,'supervisor_error',error_type=type(exc).__name__)
        if worker and worker.poll() is None:
            worker.kill();worker.wait(timeout=2)
        # systemd ExecStopPost owns independent recovery after this process exits.
        raise
    finally:os.close(fd)

def finalize(spec_path,sha):
    s=c.load_spec(spec_path,sha,check_time=False);op=Path(s['operation'])
    fd=os.open(c.ROOT/'controller.lock',os.O_RDWR|os.O_NOFOLLOW)
    try:
        fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        # A refused competing unit must never finalize another owner's operation.
        active=c.ROOT/'active.json'
        if active.exists() and json.loads(r.stable_bytes(active))['operation_id']!=s['operation_id']:
            c.atom(op/'refusal.json',{'state':'refused','reason':'different_active_owner','spec_sha256':sha});return
        with r.quiet(s['locks'],s['holds']):
            db.release_fence(s)
            if not (op/'stop-intent.json').exists():
                v=terminal(s,sha,'aborted_restored','pre_stop_refusal')
                c.atom(op/'finalizer.json',{'verified':True,'at':time.time(),'incumbent_healthy':v['incumbent_healthy'],'terminal_state':v['state']});return
            if not restore_serving(s):raise ValueError('exact incumbent restoration failed')
            if (op/'terminal.json').exists():
                old=json.loads(r.stable_bytes(op/'terminal.json'))
                if old['spec_sha256']!=sha:raise ValueError('terminal identity mismatch')
                c.atom(op/'finalizer.json',{'verified':True,'at':time.time(),'incumbent_healthy':c.healthy(s),'terminal_state':old['state']})
            else:
                v=terminal(s,sha,'aborted_restored','detached_service_recovery')
                c.atom(op/'finalizer.json',{'verified':True,'at':time.time(),'incumbent_healthy':v['incumbent_healthy'],'terminal_state':v['state']})
    except BaseException as exc:
        c.atom(op/'recovery-unresolved.json',{'error_type':type(exc).__name__,'at':time.time(),'spec_sha256':sha,'replay_allowed':False})
        raise
    finally:os.close(fd)

def dispatch(spec_path,sha):
    s=c.load_spec(spec_path,sha);op=Path(s['operation'])
    # mkdir is the permanent no-replay barrier, including a failed dispatch.
    op.mkdir(mode=0o700)
    r.write_new(op/'spec.json',r.stable_bytes(Path(spec_path)))
    r.write_new(op/'dispatch-intent.json',r.encode({'owner_id':s['owner_id'],'operation_id':s['operation_id'],'spec_sha256':sha,'at':time.time()}))
    log=op/'private.log';r.write_new(log,b'')
    unit='cbm-r031-'+s['operation_id']
    runtime=max(1,s['deadlines']['serving_by']-time.time()-20)
    executable=str(Path(__file__).resolve())
    post='/usr/bin/python3 -B '+executable+' finalize '+str(op/'spec.json')+' '+sha
    args=['systemd-run','--unit',unit,'--property=Type=exec','--property=Restart=no','--property=KillMode=control-group',
          '--property=RuntimeMaxSec='+str(runtime),'--property=TimeoutStopSec=8','--property=TimeoutStartSec=8',
          '--property=ExecStopPost='+post,'--property=StandardOutput=append:'+str(log),'--property=StandardError=append:'+str(log),
          '/usr/bin/python3','-B',executable,'supervise',str(op/'spec.json'),sha]
    c.command(args,timeout=10)
    return {'dispatched':True,'operation_id':s['operation_id'],'spec_sha256':sha,'unit':unit,'runtime_max_seconds':runtime,'replay_allowed':False}

def readback(spec_path,sha):
    s=c.load_spec(spec_path,sha,check_time=False);op=Path(s['operation'])
    if not op.exists():return {'state':'absent','replay_allowed':False}
    intent=json.loads(r.stable_bytes(op/'dispatch-intent.json'))
    if intent['spec_sha256']!=sha or intent['owner_id']!=s['owner_id']:raise ValueError('readback identity mismatch')
    for name in ('terminal.json','refusal.json','recovery-unresolved.json'):
        if (op/name).exists():
            value=json.loads(r.stable_bytes(op/name))
            value.setdefault('state','uncertain')
            value['service_state']=c.command(['systemctl','show','cbm-r031-'+s['operation_id']+'.service','--property=ActiveState','--value']).decode().strip()
            value['finalizer_seen']=(op/'finalizer.json').exists()
            value['live_verified']=c.healthy(s) and r.hold_state(s['holds'])==s['hold_bindings']
            return value
    unit='cbm-r031-'+s['operation_id']+'.service'
    state=c.command(['systemctl','show',unit,'--property=ActiveState','--value']).decode().strip()
    return {'state':'running' if state in ('activating','active','deactivating') else 'uncertain','service_state':state,'operation_id':s['operation_id'],'spec_sha256':sha,'replay_allowed':False}

def dispatch_wait(path,sha):
    print(json.dumps(dispatch(path,sha)),flush=True)
    s=c.load_spec(path,sha,check_time=False)
    while time.time()<s['deadlines']['validate_by']+10:
        value=readback(path,sha)
        if value.get('finalizer_seen') and value.get('service_state') in ('inactive','failed'):return value
        time.sleep(.3)
    return {'state':'uncertain','replay_allowed':False}

if __name__=='__main__':
    op,path,sha=sys.argv[1:]
    functions={'dispatch':dispatch,'supervise':supervisor,'finalize':finalize,'readback':readback,'dispatch-wait':dispatch_wait}
    value=functions[op](path,sha)
    if value is not None:print(json.dumps(value))

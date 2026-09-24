"""Actual explicit manual host subprocess. Intent markers prohibit replay."""
import json,os,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from run import HERE,contract,read_env,container_args,worker_environment,invoke
from runtime_contract import held
from profiles import provider_plan

def main():
    os.umask(0o077);v=contract();root=Path(v['root'])
    if held(v):raise RuntimeError('processing held; no worker launch permitted')
    operation=sys.argv[1]
    if operation not in ('inspect','execute'):raise ValueError('inspect or execute required')
    approvals=root/'manual-approvals';approvals.mkdir(mode=0o700,exist_ok=True)
    env=worker_environment();env['CB_AUTOMATIC_ONLY']=os.environ.get('CB_AUTOMATIC_ONLY','false')
    if operation=='inspect':
        from uuid import UUID
        job=str(UUID(sys.argv[2]));stage=sys.argv[3];generation=int(sys.argv[4])
        assert stage in {'acquisition','processing','indexing'} and generation>=1
        destination=approvals/f'{job}-{stage}-{generation}.json';assert not destination.exists()
        args=container_args();command=['python','-B','/packet/workers/manual_worker.py','inspect',job,stage,str(generation)]
    else:
        destination=Path(sys.argv[2]);assert destination.resolve().parent==approvals.resolve() and not destination.is_symlink()
        selected=json.loads(destination.read_text());stage=selected['stage'];assert stage in {'acquisition','processing','indexing'}
        # Write-before-effect. Neither a timeout nor a lost SSH reply permits replay.
        with destination.with_suffix('.started').open('x') as f:f.write('execution intent; reconcile before further action\n');f.flush();os.fsync(f.fileno())
        queue=read_env('worker.env')
        if 'CB_NATS_URL' in queue and queue['CB_NATS_URL']!=v['queue']['url']:raise ValueError('private queue URL/profile mismatch')
        env.update({key:queue[key] for key in v['queue']['credential_keys']})
        plan=provider_plan(v,stage)
        env[plan['environment_key']]=read_env(plan['file'])[plan['key']]
        env['CB_ENABLE_MODEL_CALLS']='false' if stage=='acquisition' else 'true'
        if v['profile']=='development':
            env['CB_SYNTHETIC_OUTCOME']=os.environ.get('CBM_TEST_OUTCOME','success')
            assert env['CB_SYNTHETIC_OUTCOME'] in ('success','uncertain')
        args=container_args(indexing=stage=='indexing')
        if env['CB_AUTOMATIC_ONLY']=='true':args+=['--label','cbm.r029.automatic-stage=true']
        destination.chmod(0o644)
        args+=['-v',str(destination)+':/approval/selection.json:ro']
        command=plan['command']
    raw=invoke(args,env,command,log=destination.with_suffix('.log'))
    if operation=='inspect':
        value=json.loads(raw)
        with destination.open('x') as f:json.dump(value,f,sort_keys=True)
        print(json.dumps({'selection':str(destination)}))
    else:print(raw.decode().strip())
if __name__=='__main__':main()

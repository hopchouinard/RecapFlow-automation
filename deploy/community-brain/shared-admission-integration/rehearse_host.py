"""Real Mac entry-point, transport/process death, startup and legacy conflict tests."""
import copy,json,os,secrets,shlex,signal,subprocess,sys,time
from pathlib import Path
import common as c
import shared
STATE=shared.STATE;SOURCE=Path(__file__).resolve().parent

def ssh(args,code=None,timeout=40):
    return subprocess.run(['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes','-o','ConnectTimeout=8',c.HOST,shlex.join(args)],input=code,capture_output=True,text=True,timeout=timeout)

def save(name,value):c.atom(STATE/name,value)

def properties(unit):
    p=ssh(['sudo','-n','systemctl','show',unit+'.service','--property=ActiveState,SubState,Result,ExecMainStatus,ExecMainStartTimestampMonotonic,ExecMainExitTimestampMonotonic,After,Requires']);assert p.returncode==0,p.stderr
    return dict(x.split('=',1) for x in p.stdout.splitlines() if '=' in x)

def startup(value,label):
    s=value['spec'];path=value['path'];sha=value['spec_sha256'];base='cbm-r032-start-'+label
    boot=base+'-boot'
    p=ssh(['sudo','-n','systemd-run','--no-block','--unit='+boot,'--property=Type=oneshot','--property=RemainAfterExit=yes','/usr/bin/python3','-B',s['packet']+'/boot_reconcile.py',s['packet_sha256']]);assert p.returncode==0,p.stderr
    for unit,mode,extra in [(base,'startup',['--property=Requires='+boot+'.service','--property=After='+boot+'.service']),(base+'-probe','startup-probe',['--property=Requires='+base+'.service','--property=After='+base+'.service'])]:
        p=ssh(['sudo','-n','systemd-run','--no-block','--unit='+unit,'--property=Type=oneshot','--property=RemainAfterExit=yes',*extra,'/usr/bin/python3','-B',s['packet']+'/target.py',mode,path,sha]);assert p.returncode==0,p.stderr
    limit=time.time()+30
    while time.time()<limit:
        boot_state=properties(boot);start=properties(base);probe=properties(base+'-probe')
        if boot_state['ActiveState']=='failed' or start['ActiveState']=='failed' or probe['ActiveState']=='failed':break
        if start['SubState']=='exited' and probe['SubState']=='exited':break
        time.sleep(.1)
    passed=start['SubState']=='exited' and probe['SubState']=='exited'
    ordered=passed and int(probe['ExecMainStartTimestampMonotonic'])>=int(start['ExecMainExitTimestampMonotonic'])>0
    if passed:
        assert ordered and boot_state['SubState']=='exited'
        assert int(start['ExecMainStartTimestampMonotonic'])>=int(boot_state['ExecMainExitTimestampMonotonic'])>0
    result={'boot_unit':boot,'boot':boot_state,'startup_unit':base,'probe_unit':base+'-probe','startup':start,'probe':probe,'passed':passed,'dependency_order_verified':ordered,'actual_vm_reboot':False}
    save(label+'-startup.json',result);return result

def prepare(label,kind,exercise,version):
    packet=c.admission.read(STATE/(version+'.json'))
    p=ssh(['sudo','-n','python3','-B',packet['path']+'/fixtures.py','prepare',label,packet['path'],packet['manifest_sha256'],exercise,kind]);assert p.returncode==0,p.stderr
    v=json.loads(p.stdout);path=STATE/(label+'-spec.json');c.r.write_new(path,c.r.encode(v['spec']))
    assert startup(v,label)['passed']
    return v,path

def invoke(kind,path,mode='dispatch',wait=True):
    args=[sys.executable,'-B',str(SOURCE/(kind+'.py')),mode,str(path)]
    if wait:
        p=subprocess.run(args,capture_output=True,text=True,timeout=340)
        return {'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    out=path.with_name(path.stem+'-client.stdout');err=path.with_name(path.stem+'-client.stderr')
    return subprocess.Popen(args,stdout=out.open('w'),stderr=err.open('w'))

def raw(v,mode='readback'):
    p=ssh(['sudo','-n','python3','-B',v['spec']['packet']+'/target.py',mode,v['path'],v['spec_sha256']]);assert p.returncode==0,p.stderr
    return json.loads(p.stdout)

def marker(v,name):return ssh(['sudo','-n','test','-f',v['spec']['operation']+'/'+name]).returncode==0

def wait_ready(v,caller):
    until=time.time()+60
    while time.time()<until:
        if marker(v,'interrupt-ready.json'):return
        if caller.poll() is not None:raise ValueError('caller exited before interruption window')
        time.sleep(.1)
    raise ValueError('interruption marker missing')

def terminal(v):
    until=v['spec']['deadlines']['serving_by']+10
    while time.time()<until:
        result=raw(v)
        if result.get('finalizer_seen') and result.get('service_state') in ('inactive','failed'):
            assert result['state'] in ('completed','aborted_restored') and result['live_verified']
            assert result['serving_restored_at']<=v['spec']['deadlines']['serving_by'];return result
        time.sleep(.3)
    raise ValueError('bounded serving recovery unconfirmed')

def interruption(label,mode,version):
    sched,sp=prepare(label+'s','scheduler','normal',version);manual,mp=prepare(label+'m','manual','normal',version)
    value,cp=prepare(label+'c','capture','failed_finalizer' if mode=='finalizer' else 'wait_for_interrupt',version)
    s=value['spec'];caller=invoke('capture',cp,wait=False);wait_ready(value,caller);actions=[]
    busy=invoke('manual',mp);assert busy['returncode']!=0 and 'BlockingIOError' in busy['stderr'];actions.append({'case':'existing_mutex_contention','rejected':True})
    ids=c.admission.read(STATE/'client.json');assert ids['operation_id']==s['operation_id']
    if mode=='finalizer':
        code="from pathlib import Path\nimport json,os,signal\nf=Path("+repr(s['fixture'])+")/'finalizer-fault'\nf.open('xb').write(b'explicit synthetic process failure')\nop=Path("+repr(s['operation'])+")\nos.kill(json.loads((op/'guardian.json').read_bytes())['pid'],signal.SIGKILL)\n"
        p=ssh(['sudo','-n','python3','-B','-'],code);assert p.returncode==0,p.stderr
        os.kill(caller.pid,signal.SIGKILL);caller.wait(timeout=5)
        for _ in range(80):
            value_raw=raw(value)
            if value_raw.get('state')=='uncertain' and value_raw.get('service_state')=='failed':break
            time.sleep(.1)
        else:raise ValueError('actual finalizer failure not observed')
        actions.append({'case':'actual_finalizer_failed','readback':value_raw})
    elif mode=='sshkill':
        os.kill(ids['ssh_pid'],signal.SIGKILL);caller.wait(timeout=30);assert caller.returncode!=0
        actions.append({'case':'actual_ssh_client_sigkill','pid':ids['ssh_pid']})
    else:
        os.kill(caller.pid,signal.SIGKILL);caller.wait(timeout=5);actions.append({'case':'actual_mac_caller_sigkill','pid':caller.pid})
    for kind,path in [('scheduler',sp),('manual',mp),('capture',cp)]:
        refused=invoke(kind,path);assert refused['returncode']!=0 and 'unresolved operation' in refused['stderr'];actions.append({'case':kind+'_blocked_by_shared_intent','rejected':True})
    early=invoke('capture',cp,'reconcile');assert early['returncode']!=0;actions.append({'case':'unsafe_readback_does_not_resolve','rejected':True})
    if mode=='finalizer':
        failed=startup(value,label+'failed');assert not failed['passed'];assert int(failed['probe'].get('ExecMainStartTimestampMonotonic','0'))==0
        code="from pathlib import Path\nimport json\nf=Path("+repr(s['fixture'])+")\np=f/'startup-ready.json'\nv=json.loads(p.read_bytes())\nv['boot_id']='00000000-0000-0000-0000-000000000000'\np.write_text(json.dumps(v))\n(f/'finalizer-fault').unlink()\n"
        p=ssh(['sudo','-n','python3','-B','-'],code);assert p.returncode==0,p.stderr
        stale=invoke('capture',cp,'reconcile');assert stale['returncode']!=0
        recovered=startup(value,label+'recovered');assert recovered['passed'];actions.append({'case':'failed_startup_blocks_dependent_effect','probe_never_started':True});actions.append({'case':'current_boot_startup_recovers_failed_finalizer','ordered':True,'actual_vm_reboot':False})
    restored=terminal(value);resolved=invoke('capture',cp,'reconcile');assert resolved['returncode']==0,resolved
    no_replay=invoke('capture',cp);assert no_replay['returncode']!=0
    actions.append({'case':'resolved_operation_cannot_replay','rejected':True})
    for kind in ('scheduler','manual'):
        fresh,p=prepare(label+'next'+kind,kind,'normal',version);result=invoke(kind,p);assert result['returncode']==0 and json.loads(result['stdout'])['state']=='completed',result
        actions.append({'case':'fresh_'+kind+'_after_authoritative_recovery','passed':True,'operation_id':fresh['spec']['operation_id']})
    result={'label':label,'mode':mode,'operation_id':s['operation_id'],'packet_sha256':s['packet_sha256'],'actions':actions,'terminal':restored,'reconciliation':resolved,'shared_journal_resolved':True,'actual_vm_reboot':False}
    save(label+'-interruption.json',result);print(json.dumps(result))

def legacy_conflicts(label,version):
    v,p=prepare(label,'manual','normal',version);results=[]
    for name in ('activation-pending.json','pending.json','manual-pending.json'):
        marker=STATE/'legacy-conflicts'/name;c.r.write_new(marker,c.r.encode({'synthetic_unresolved':True}))
        try:
            result=invoke('manual',p);assert result['returncode']!=0 and 'pending conflict' in result['stderr'];assert not (STATE/'journal'/v['spec']['operation_id']).exists()
            results.append({'marker':name,'rejected_before_intent':True,'sha256':c.r.sha(c.r.stable_bytes(marker))})
        finally:marker.rename(STATE/(label+'-retained-'+name))
    result=invoke('manual',p);assert result['returncode']==0,result
    out={'legacy_conflicts':results,'original_legacy_files_changed':False,'fresh_operation_after_test_marker_retention':result}
    save(label+'-legacy-checks.json',out);print(json.dumps(out))

if __name__=='__main__':
    label,mode,version=sys.argv[1:]
    if mode=='legacy':legacy_conflicts(label,version)
    else:interruption(label,mode,version)

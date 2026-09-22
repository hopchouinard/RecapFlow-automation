import hashlib,json,os,subprocess,sys,time
from pathlib import Path
import service_recovery as s
ROOT=s.ROOT

def cmd(args):return subprocess.check_output(args,text=True).strip()
def props(unit):return dict(x.split('=',1) for x in cmd(['systemctl','show',unit,'--property=ActiveState,SubState,ExecMainStartTimestampMonotonic,ExecMainExitTimestampMonotonic,Result']).splitlines() if '=' in x)
def unit(name,mode,path,requires=None,finalizer=False):
 args=['systemd-run','--no-block','--unit='+name,'--property=Type=oneshot']
 if requires:args+=['--property=Requires='+requires+'.service','--property=After='+requires+'.service']
 if finalizer:args+=['--property=RuntimeMaxSec=30','--property=TimeoutStopSec=5','--property=ExecStopPost=/usr/bin/python3 -B '+str(s.HERE/'service_recovery.py')+' finalize '+str(path)]
 else:args+=['--property=RemainAfterExit=yes']
 cmd(args+['/usr/bin/python3','-B',str(s.HERE/'service_recovery.py'),mode,str(path)])
def wait(name):
 for _ in range(200):
  p=props(name)
  if p['ActiveState']=='failed' or p['SubState']=='exited':return p
  time.sleep(.1)
 raise ValueError('unit completion timeout')
def run(label):
 root=ROOT/('services-'+label);root.mkdir(mode=0o700);a=root/'automation';a.mkdir(mode=0o700)
 for name in ('attention.json','checkpoint-needed.json'):p=a/name;p.write_text('{"synthetic":"retained"}');p.chmod(0o600)
 (root/'recovery.lock').touch(mode=0o600)
 name='cbm-r033-inc-'+label;ident=cmd(['docker','run','-d','--name',name,'--network','none','--restart','unless-stopped','--memory','64m','--cpus','0.25','--read-only','--cap-drop','ALL','--user','10001:10001','python:3.11-slim','python','-B','-m','http.server','8080'])
 row=s.inspect(ident);spec={'root':str(root),'incumbent_id':ident,'incumbent_name':name,'fingerprint':s.fingerprint(row),'persistent_holds':{p.name:s.sha(p) for p in a.iterdir()},'packet_sha256':s.sha(s.HERE/'packet-manifest.json')};path=root/'spec.json';s.atomic(path,spec)
 base='cbm-r033-'+label;units=[];previous=None
 for suffix,mode in [('pause','pause'),('docker','docker-ready'),('recovery','recover'),('cron','probe')]:
  current=base+'-'+suffix;unit(current,mode,path,previous);units.append(current);previous=current
 assert wait(previous)['SubState']=='exited'
 ordering=[props(u) for u in units]
 assert all(int(ordering[i+1]['ExecMainStartTimestampMonotonic'])>=int(ordering[i]['ExecMainExitTimestampMonotonic'])>0 for i in range(3))
 (root/'probe.json').rename(root/'initial-probe.json')
 (root/'finalizer-fault').write_text('explicit fixture failure')
 maintenance=base+'-maintenance';unit(maintenance,'maintenance',path,finalizer=True);units.append(maintenance)
 for _ in range(100):
  if (root/'interrupt-ready.json').exists():break
  time.sleep(.1)
 else:raise ValueError('maintenance did not start')
 cmd(['systemctl','kill','--signal=KILL',maintenance]);assert wait(maintenance)['ActiveState']=='failed'
 failed=base+'-failed-recovery';unit(failed,'recover',path);units.append(failed);probe=base+'-failed-cron';unit(probe,'probe',path,failed);units.append(probe)
 assert wait(failed)['ActiveState']=='failed';assert int(props(probe)['ExecMainStartTimestampMonotonic'])==0;assert not (root/'probe.json').exists()
 (root/'finalizer-fault').rename(root/'retained-finalizer-fault')
 recovered=base+'-reconciled';unit(recovered,'recover',path);units.append(recovered);probe=base+'-reconciled-cron';unit(probe,'probe',path,recovered);units.append(probe)
 assert wait(probe)['SubState']=='exited';assert (a/'paused').exists();s.load(path)
 value={'incumbent_id':ident,'incumbent_name':name,'spec':spec,'initial_ordering':ordering,'units':units,'failed_finalizer_blocked_dependent_effect':True,'exact_incumbent_restored':True,'persistent_attention_checkpoint_equal':True,'processing_stays_paused':True,'restart_policy':'unless-stopped','docker_daemon_restarted':False,'actual_vm_reboot':False,'test_scope':'actual transient unit ordering and exact container state; docker-ready explicitly models daemon availability'}
 s.atomic(ROOT/(label+'-service-receipt.json'),value);print(json.dumps(value))
if __name__=='__main__':run(sys.argv[1])

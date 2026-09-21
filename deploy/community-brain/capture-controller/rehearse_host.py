import json,subprocess,sys,time,os,signal,shlex
from pathlib import Path
STATE=Path.home()/'.local/state/community-brain-management/request031'
SOURCE=Path(__file__).resolve().parent
ROOT='/srv/dev-data/workspaces/cbm-capture-controller-20260921-031'
HOST='pchouinard@10.1.30.20'
def ssh(args):
 return subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8',HOST,shlex.join(args)],capture_output=True,text=True,timeout=30)
label,mode,packet,packet_sha=sys.argv[1:]
exercise='normal' if mode=='normal' else 'wait_for_interrupt'
p=ssh(['sudo','-n','python3','-B',packet+'/fixtures.py','prepare',label,packet,packet_sha,exercise])
if p.returncode:raise RuntimeError(p.stderr)
value=json.loads(p.stdout);spec=STATE/(label+'-spec.json')
sys.path.insert(0,str(SOURCE));import common
spec.write_bytes(common.r.encode(value['spec']));os.chmod(spec,0o600)
s=value['spec'];op=s['operation'];sha=value['spec_sha256']
out=STATE/(label+'-stdout.txt');err=STATE/(label+'-stderr.txt')
with out.open('w') as stdout,err.open('w') as stderr:
 client=subprocess.Popen([sys.executable,'-B',str(SOURCE/'mac.py'),'dispatch',str(spec)],stdout=stdout,stderr=stderr)
 actions=[]
 if mode!='normal':
  for _ in range(50):
   check=ssh(['sudo','-n','test','-f',op+'/interrupt-ready.json'])
   if check.returncode==0:break
   if client.poll() is not None:raise RuntimeError('client exited before interrupt marker')
   time.sleep(.15)
  else:raise RuntimeError('no interruption window')
  duplicate=ssh(['sudo','-n','python3','-B',packet+'/target.py','dispatch',value['path'],sha])
  actions.append({'test':'duplicate_target_dispatch','rejected':duplicate.returncode!=0,'exception':duplicate.stderr.splitlines()[-1] if duplicate.stderr else ''})
  lockcode="import fcntl,json,os; s=json.loads(open("+repr(value['path'])+").read()); out=[]\nfor path in s['locks']:\n fd=os.open(path,os.O_RDWR)\n try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB);out.append(False)\n except BlockingIOError:out.append(True)\n finally:os.close(fd)\nprint(json.dumps(out))"
  locks=ssh(['sudo','-n','python3','-B','-c',lockcode])
  actions.append({'test':'existing_vm_locks_held','blocked':json.loads(locks.stdout)})
  competing=subprocess.run([sys.executable,'-B',str(SOURCE/'mac.py'),'dispatch',str(spec)],capture_output=True,text=True)
  actions.append({'test':'competing_mac_dispatch','returncode':competing.returncode,'rejected':competing.returncode!=0})
  if mode in ('sshkill','mackill'):
   ids=json.loads((STATE/'client.json').read_text());pid=ids['ssh_pid'] if mode=='sshkill' else client.pid
   os.kill(pid,signal.SIGKILL);actions.append({'signal':'SIGKILL','target':mode,'pid':pid,'at':time.time()})
   if mode=='mackill':
    client.wait(timeout=5)
    blocked=subprocess.run([sys.executable,'-B',str(SOURCE/'mac.py'),'dispatch',str(spec)],capture_output=True,text=True)
    actions.append({'test':'durable_pending_after_caller_death','rejected':blocked.returncode!=0,'reason':blocked.stderr.splitlines()[-1]})
    client=subprocess.Popen([sys.executable,'-B',str(SOURCE/'mac.py'),'reconcile',str(spec)],stdout=stdout,stderr=stderr)
  elif mode in ('guardiankill','guardianstop','workerkill'):
   name='worker' if mode=='workerkill' else 'guardian';v=ssh(['sudo','-n','cat',op+'/'+name+'.json']);pid=json.loads(v.stdout)['pid']
   sig='STOP' if mode=='guardianstop' else 'KILL';p=ssh(['sudo','-n','kill','-'+sig,str(pid)])
   actions.append({'signal':sig,'target':name,'pid':pid,'returncode':p.returncode,'at':time.time()})
  elif mode=='fenceloss':
   v=json.loads(ssh(['sudo','-n','cat',op+'/fence.json']).stdout)
   q="SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid="+str(v['pid'])+" AND application_name='"+v['application_name']+"';"
   p=ssh(['sudo','-n','docker','exec',v['container_id'],'psql','-X','-qAt','-U','fixture','-d','fixture','-c',q]);actions.append({'action':'terminate_actual_database_fence','returncode':p.returncode,'result':p.stdout.strip(),'at':time.time()})
 client.wait(timeout=150)
result={'label':label,'mode':mode,'returncode':client.returncode,'stdout':out.read_text(),'stderr':err.read_text(),'actions':actions,'spec_sha256':sha,'operation_id':s['operation_id']}
if result['stdout']:
 result['readback']=json.loads(result['stdout'].splitlines()[-1]);result['restored_within_deadline']=result['readback'].get('serving_restored_at',float('inf'))<=s['deadlines']['serving_by']
if client.returncode or result.get('readback',{}).get('state')!=('completed' if mode=='normal' else 'aborted_restored') or not result.get('restored_within_deadline') or not result['readback'].get('live_verified'):raise AssertionError(result)
(STATE/(label+'-client-result.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

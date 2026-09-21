import sys,json,subprocess,shlex,time
from pathlib import Path
STATE=Path.home()/'.local/state/community-brain-management/request032'
SOURCE=STATE/'sealed/packet-v6'
sys.path.insert(0,str(SOURCE))
import rehearse_host as h
v,p=h.prepare('database6','capture','normal','packet-v6')
s=v['spec']
args=['sudo','-n','python3','-B',s['packet']+'/concurrent_clients.py',v['path'],v['spec_sha256']]
client=subprocess.Popen(['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes',h.c.HOST,shlex.join(args)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
for _ in range(100):
 if h.ssh(['sudo','-n','test','-f',s['fixture']+'/concurrent-clients/ready.json']).returncode==0:break
 if client.poll() is not None:raise RuntimeError(client.communicate())
 time.sleep(.1)
else:raise RuntimeError('clients not ready')
result=h.invoke('capture',p);h.save('database6-result.json',result)
assert result['returncode']==0 and json.loads(result['stdout'])['state']=='completed',result
out,err=client.communicate(timeout=15);assert client.returncode==0,(out,err)
h.save('database6-concurrent.json',json.loads(out))
r=h.ssh(['sudo','-n','python3','-B',s['packet']+'/check_database.py',v['path'],v['spec_sha256'],'/srv/dev-data/workspaces/cbm-shared-admission-20260921-032/preparation-template.json'],timeout=180)
assert r.returncode==0,r.stderr
h.save('database6-checks.json',json.loads(r.stdout))
print('database6 capture, concurrent clients and database negatives passed',flush=True)
for label,mode in [('caller6','mackill'),('transport6','sshkill'),('recovery6','finalizer'),('legacy6','legacy')]:
 if mode=='legacy':h.legacy_conflicts(label,'packet-v6')
 else:h.interruption(label,mode,'packet-v6')
 print(label+' passed',flush=True)

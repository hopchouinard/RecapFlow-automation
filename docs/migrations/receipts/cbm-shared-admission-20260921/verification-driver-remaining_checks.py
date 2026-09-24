import subprocess,sys
from pathlib import Path
s=Path.home()/'.local/state/community-brain-management/request032';p=s/'sealed/packet-v6'
for label,mode in [('transport6','sshkill'),('recovery6','finalizer'),('legacy6','legacy')]:
 r=subprocess.run([sys.executable,'-B',str(p/'rehearse_host.py'),label,mode,'packet-v6'],capture_output=True,text=True)
 (s/(label+'-harness.txt')).write_text(r.stdout+r.stderr);print(label,r.returncode,flush=True);assert r.returncode==0,r.stderr
for module in ('check_readback.py','check_local_source.py'):
 r=subprocess.run([sys.executable,'-B',str(p/module),str(s/'legacy6-spec.json')],capture_output=True,text=True)
 (s/(module+'.txt')).write_text(r.stdout+r.stderr);print(module,r.returncode,flush=True);assert r.returncode==0,r.stderr
r=subprocess.run([sys.executable,'-B',str(s/'unmanaged_check.py')],capture_output=True,text=True)
(s/'unmanaged6-harness.txt').write_text(r.stdout+r.stderr);print('unmanaged',r.returncode,flush=True);assert r.returncode==0,r.stderr

import sys,json,subprocess,shlex,select,time
from pathlib import Path
STATE=Path.home()/'.local/state/community-brain-management/request032';sys.path.insert(0,str(STATE/'sealed/packet-v6'));import rehearse_host as h
v,p=h.prepare('unmanaged6','capture','normal','packet-v6');s=v['spec'];container=s['database']['source']['id']
args=['sudo','-n','docker','exec','-i','-e','PGAPPNAME=unreviewed-writer',container,'psql','-X','-qAt','-U','fixture','-d','cbm_app','-v','ON_ERROR_STOP=1']
client=subprocess.Popen(['ssh','-o','BatchMode=yes',h.c.HOST,shlex.join(args)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
try:
 client.stdin.write("BEGIN;SELECT 'READY';\n");client.stdin.flush()
 assert select.select([client.stdout],[],[],10)[0] and client.stdout.readline().strip()=='READY'
 result=h.invoke('capture',p);h.save('unmanaged6-result.json',result)
 assert result['returncode']==0 and json.loads(result['stdout'])['state']=='aborted_restored',result
 q=h.ssh(['sudo','-n','cat',s['operation']+'/writer-admission-refused.json']);assert q.returncode==0,q.stderr
 refusal=json.loads(q.stdout);assert refusal['observation']['unexpected_backends']==1
 assert not h.marker(v,'worker-result.json') and client.poll() is None
 client.stdin.write('ROLLBACK;\nSELECT 1;\n\\q\n');client.stdin.flush();client.wait(timeout=10)
 assert client.returncode==0,client.stderr.read()
 h.save('unmanaged6-checks.json',{'unexpected_administrative_backend_rejected':True,'capture_aborted_before_worker_result':True,'serving_and_writer_controls_restored':True,'unrelated_backend_not_blindly_terminated':True,'owned_test_backend_rolled_back_explicitly':True,'refusal':refusal})
 print('unmanaged backend refused and safe recovery verified')
finally:
 if client.poll() is None:client.stdin.close();client.wait(timeout=10)

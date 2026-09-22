"""Independent, idempotent exact-incumbent rollback for the isolated renderer."""
import json,subprocess,sys,time
from pathlib import Path
from helper_contracts import verify_sources,write_new
import service_recovery as s

def finalize(path):
 if (s.ROOT/'retired.json').exists():raise ValueError('retired candidate root; no rollback effects')
 path=Path(path)
 if path.is_symlink() or not path.resolve().is_relative_to(s.ROOT):raise ValueError('development rollback binding')
 b=json.loads(path.read_bytes());root=path.parent
 if b['executor_manifest_sha256']!=verify_sources():raise ValueError('rollback source changed')
 row=s.inspect(b['incumbent_id'])
 if s.fingerprint(row)!=b['incumbent_fingerprint']:raise ValueError('rollback incumbent changed')
 created=root/('generation-'+b['generation'])/'created.json'
 if created.exists():
  new=json.loads(created.read_bytes());r=s.inspect(new['replacement_id'])
  if r['Name'].lstrip('/')!=new['name'] or new['name']!='cbm-r033-generation-'+b['generation']:raise ValueError('replacement identity changed')
  if r['State']['Running']:subprocess.run(['docker','stop','--time','1',r['Id']],check=True,capture_output=True)
 if not row['State']['Running']:subprocess.run(['docker','start',row['Id']],check=True,capture_output=True)
 for _ in range(20):
  p=subprocess.run(['docker','exec',row['Id'],'python','-B','-c',"import urllib.request;urllib.request.urlopen('http://127.0.0.1:8080',timeout=1)"],capture_output=True)
  if p.returncode==0:break
  time.sleep(.1)
 else:raise ValueError('incumbent health unavailable')
 value={'incumbent_id':row['Id'],'verified':True,'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip(),'at':time.time()}
 write_new(root/('finalizer-'+str(time.time_ns())+'.json'),value);return value
if __name__=='__main__':print(json.dumps(finalize(sys.argv[1])))

"""Bound service/boot/finalizer integration. Executable only in Request033 dev root."""
import hashlib,importlib.util,json,os,subprocess,sys,time,fcntl
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=Path('/srv/dev-data/workspaces/cbm-production-mapping-20260922-033')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def atomic(p,v):
 tmp=p.with_name('.'+p.name+'-'+str(time.time_ns()));tmp.write_text(json.dumps(v,sort_keys=True)+'\n');tmp.chmod(0o600);os.replace(tmp,p)
def inspect(ident):return json.loads(subprocess.check_output(['docker','inspect','--type','container',ident]))[0]
def fingerprint(row):return hashlib.sha256(json.dumps({k:row[k] for k in ('Id','Image','Config','HostConfig','Mounts')},sort_keys=True).encode()).hexdigest()
def load(path):
 p=Path(path)
 if p.is_symlink() or not p.resolve().is_relative_to(ROOT):raise ValueError('development-only service boundary')
 s=json.loads(p.read_bytes());r=Path(s['root'])
 if not r.is_relative_to(ROOT) or r.is_symlink() or __import__('socket').gethostname()!='community-brain-dev':raise ValueError('scope')
 if r.stat().st_uid!=0 or r.stat().st_mode&511!=448:raise ValueError('locked root ownership')
 manifest=json.loads((HERE/'packet-manifest.json').read_bytes())
 if sha(HERE/'packet-manifest.json')!=s['packet_sha256']:raise ValueError('source packet')
 for n,h in manifest.items():
  if (HERE/n).is_symlink() or sha(HERE/n)!=h:raise ValueError('source drift')
 row=inspect(s['incumbent_id'])
 if row['Name'].lstrip('/')!=s['incumbent_name'] or fingerprint(row)!=s['fingerprint']:raise ValueError('incumbent/source identity')
 for name,h in s['persistent_holds'].items():
  if sha(r/'automation'/name)!=h:raise ValueError('processing/checkpoint hold drift')
 return s,r,row

def run(mode,path):
 if (ROOT/'retired.json').exists():raise ValueError('retired candidate root; no service effects')
 s,r,row=load(path);boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip();fd=os.open(r/'recovery.lock',os.O_RDWR|os.O_NOFOLLOW)
 try:
  fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
  if mode=='pause':
   sys.path.insert(0,str(HERE/'deployed-mac/platform-services/community-brain-prod/automatic-recovery'))
   spec=importlib.util.spec_from_file_location('actual_boot_guard',HERE/'production-boot-guard.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
   m.enforce(r/'automation',boot,force=True)
   atomic(r/'admission.json',{'open':False,'boot_id':boot});atomic(r/'pause.json',{'boot_id':boot,'at_ns':time.time_ns(),'source_sha256':sha(HERE/'production-boot-guard.py')})
  elif mode in ('docker-ready','recover','finalize'):
   pause=json.loads((r/'pause.json').read_bytes())
   if pause['boot_id']!=boot or not (r/'automation/paused').exists():raise ValueError('current boot processing pause required')
   if mode!='docker-ready' and (r/'finalizer-fault').exists():raise ValueError('explicit failed-finalizer fixture; admission remains closed')
   if not row['State']['Running']:subprocess.run(['docker','start',s['incumbent_id']],check=True,capture_output=True)
   for _ in range(30):
    p=subprocess.run(['docker','exec',s['incumbent_id'],'python','-B','-c',"import urllib.request;assert urllib.request.urlopen('http://127.0.0.1:8080',timeout=1).status==200"],capture_output=True)
    if p.returncode==0:break
    time.sleep(.1)
   else:raise ValueError('serving recovery failed')
   atomic(r/(mode+'.json'),{'boot_id':boot,'at_ns':time.time_ns(),'incumbent_id':s['incumbent_id'],'verified':True})
   if mode!='docker-ready':atomic(r/'admission.json',{'open':True,'boot_id':boot,'incumbent_id':s['incumbent_id'],'packet_sha256':s['packet_sha256']})
  elif mode=='probe':
   a=json.loads((r/'admission.json').read_bytes())
   if not a.get('open') or a['boot_id']!=boot or a['incumbent_id']!=s['incumbent_id']:raise ValueError('admission closed')
   atomic(r/'probe.json',{'at_ns':time.time_ns(),'processing_paused':(r/'automation/paused').exists()})
  elif mode=='maintenance':
   atomic(r/'admission.json',{'open':False,'boot_id':boot});atomic(r/'stop-intent.json',{'incumbent_id':s['incumbent_id'],'at_ns':time.time_ns()})
   subprocess.run(['docker','stop','--time','1',s['incumbent_id']],check=True,capture_output=True)
   atomic(r/'interrupt-ready.json',{'pid':os.getpid()});time.sleep(120)
  else:raise ValueError('unknown service operation')
  return {'mode':mode,'boot_id':boot,'processing_holds_preserved':True,'actual_vm_reboot':False}
 finally:os.close(fd)
if __name__=='__main__':print(json.dumps(run(*sys.argv[1:])))

"""Closed adapter boundary around actual deployed logic, never arbitrary helper names."""
import hashlib,json,os,time,fcntl
from pathlib import Path
HERE=Path(__file__).resolve().parent
MAC=HERE/'deployed-mac'
INTEGRATIONS=MAC/'platform-services/community-brain-prod/integrations'
AUTOMATIC=MAC/'platform-services/community-brain-prod/automatic-recovery'
HELPERS={'pre-pbs-copy':INTEGRATIONS/'pre-pbs-copy.py','legacy-intake-ownership':MAC/'mac-intake.py','renew-service-tokens':INTEGRATIONS/'renew-service-tokens.py','provision-nats-tls':INTEGRATIONS/'provision-nats-tls.py','renew-app-tls':INTEGRATIONS/'renew-app-tls.py','copy-backup':INTEGRATIONS/'copy-backup.py','management-health':INTEGRATIONS/'management-health.py','checkpoint-consumer':AUTOMATIC/'consumer.py','monitor-publish':AUTOMATIC/'monitor_status.py'}
DEADLINES={'pre-pbs-copy':210,'legacy-intake-ownership':45,'renew-service-tokens':180,'provision-nats-tls':180,'renew-app-tls':180,'copy-backup':180,'management-health':180,'checkpoint-consumer':1200,'monitor-publish':30}
def canonical(v):return (json.dumps(v,sort_keys=True,indent=2)+'\n').encode()
def sha(v):return hashlib.sha256(v).hexdigest()
def write_new(path,value):
 fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
 with os.fdopen(fd,'wb') as f:f.write(canonical(value));f.flush();os.fsync(f.fileno())
 d=os.open(path.parent,os.O_RDONLY);os.fsync(d);os.close(d)
def verify_sources():
 m=json.loads((HERE/'deployed-manifest.json').read_bytes())
 for n,h in m.items():
  p=MAC/n
  if p.is_symlink() or sha(p.read_bytes())!=h:raise ValueError('deployed helper source changed')
 packet=HERE/'packet-manifest.json'
 if packet.exists():
  expected=json.loads(packet.read_bytes());actual={str(p.relative_to(HERE)) for p in HERE.rglob('*') if p.is_file() and p!=packet}
  if actual!=set(expected):raise ValueError('unknown candidate member')
  for n,h in expected.items():
   if (HERE/n).is_symlink() or sha((HERE/n).read_bytes())!=h:raise ValueError('candidate source changed')
  return sha(packet.read_bytes())
 return sha(canonical({str(p.relative_to(HERE)):sha(p.read_bytes()) for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts}))
_CURRENT=None
def current_cycle():
 if _CURRENT is None:raise ValueError('no shared admission capability')
 _CURRENT.check();return _CURRENT
class Cycle:
 """Existing mutex stays continuously owned; each helper has intent before effects.

 The scheduler may hand the same open-file description to a nested adapter. A
 caller-supplied environment flag is insufficient. Unknown outcomes never replay.
 """
 def __init__(self,state,mutex,operation,kind,source_sha):
  self.state=Path(state);self.mutex=Path(mutex);
  mac=Path.home()/'.local/state/community-brain-management';vm=Path('/srv/dev-data/workspaces/cbm-production-mapping-20260922-033')
  if self.mutex==mac/'scheduler.lock':self.state=mac/'request033/journal'
  elif self.mutex==vm/'fixture-mutex':self.state=vm/'journal'
  self.operation=operation;self.kind=kind;self.source_sha=source_sha;self.fd=None
  if kind not in ('scheduler','manual','capture') or not operation.replace('-','').isalnum():raise ValueError('closed operation/kind required')
 def __enter__(self):
  if (self.state.parent/'retired.json').exists():raise ValueError('retired candidate root; no new effects')
  self.fd=os.open(self.mutex,os.O_RDWR|os.O_NOFOLLOW);self.identity=os.fstat(self.fd)
  try:
   fcntl.flock(self.fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
   if self.source_sha!=verify_sources():raise ValueError('source manifest mismatch')
   from legacy_admission import check
   self.legacy=check(self.mutex)
   self.state.mkdir(mode=0o700,parents=True,exist_ok=True)
   for p in self.state.iterdir():
    if p.is_dir() and not (p/'resolved.json').exists():raise ValueError('unresolved shared helper cycle; no replay')
   self.op=self.state/self.operation;self.op.mkdir(mode=0o700)
   write_new(self.op/'intent.json',{'operation':self.operation,'kind':self.kind,'owner_pid':os.getpid(),'source_sha256':self.source_sha,'mutex_device':self.identity.st_dev,'mutex_inode':self.identity.st_ino,'at':time.time()})
   global _CURRENT
   if _CURRENT is not None:raise ValueError('nested admission forbidden')
   _CURRENT=self;self.receipts={};return self
  except BaseException:os.close(self.fd);self.fd=None;raise
 def check(self):
  if self.fd is None:raise ValueError('helper invocation outside admission')
  st=self.mutex.stat()
  if (st.st_dev,st.st_ino)!=(self.identity.st_dev,self.identity.st_ino):raise ValueError('mutex identity changed')
  if verify_sources()!=self.source_sha:raise ValueError('source changed during cycle')
 def helper(self,name,execute,readback):
  self.check()
  if name not in HELPERS:raise ValueError('unknown helper')
  path=self.op/(name+'.intent.json');write_new(path,{'helper':name,'source_sha256':sha(HELPERS[name].read_bytes()),'deadline':time.time()+DEADLINES[name]})
  started=time.monotonic();execute();self.check()
  if time.monotonic()-started>DEADLINES[name]:raise ValueError('helper deadline exceeded; retain uncertainty')
  proof=readback()
  if not isinstance(proof,dict) or not proof:raise ValueError('actual effect readback required')
  receipt={'helper':name,'source_sha256':sha(HELPERS[name].read_bytes()),'effect_readback':proof,'at':time.time(),'production_qualified':False};write_new(self.op/(name+'.receipt.json'),receipt);self.receipts[name]=receipt;return receipt
 def finish(self):
  self.check();write_new(self.op/'resolved.json',{'receipts':{k:sha(canonical(v)) for k,v in self.receipts.items()},'state':'verified','replay_allowed':False});return self.receipts
 def __exit__(self,*args):
  global _CURRENT
  if _CURRENT is self:_CURRENT=None
  if self.fd is not None:os.close(self.fd);self.fd=None

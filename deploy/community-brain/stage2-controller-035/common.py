"""Small fail-closed primitives shared by the staged controller and finalizer."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import stat
import subprocess

HEX=re.compile(r'^[0-9a-f]{64}$')
ID=re.compile(r'^[a-z][a-z0-9-]{7,63}$')
DEV_ROOT=Path('/srv/dev-data/workspaces/cbm-stage2-controller-20260924-035')
PROD_ROOT=Path('/srv/community-brain/maintenance-035')
DEV_HOST='community-brain-dev'
DEV_MOUNT='4a18b6bd-e3d7-40c7-b310-add6598c9438'

def encode(value):return (json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
def sha(raw):return hashlib.sha256(raw).hexdigest()

def no_links(path):
 p=Path(path).absolute()
 for member in (p,*p.parents):
  if member.is_symlink():raise ValueError('linked path refused')
 return p

def stable_bytes(path):
 p=no_links(path)
 fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
 with os.fdopen(fd,'rb') as stream:
  before=os.fstat(stream.fileno())
  if not stat.S_ISREG(before.st_mode) or before.st_nlink!=1:raise ValueError('special or hard-linked file')
  raw=stream.read()
  after=os.fstat(stream.fileno())
 fields=lambda s:(s.st_dev,s.st_ino,s.st_uid,s.st_gid,s.st_mode,s.st_size,s.st_mtime_ns,s.st_ctime_ns)
 if fields(before)!=fields(after) or fields(after)!=fields(p.lstat()):raise ValueError('unstable file')
 return raw

def read_json(path):return json.loads(stable_bytes(path))

def create(path,raw,mode=0o600):
 p=no_links(path)
 fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,mode)
 with os.fdopen(fd,'wb') as stream:
  stream.write(raw)
  stream.flush()
  os.fsync(stream.fileno())
 sync(p.parent)

def replace(path,raw,mode=0o600):
 p=no_links(path)
 tmp=p.with_name('.'+p.name+'.'+str(os.getpid())+'.tmp')
 create(tmp,raw,mode)
 os.replace(tmp,p)
 sync(p.parent)

def sync(directory):
 fd=os.open(no_links(directory),os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
 try:os.fsync(fd)
 finally:os.close(fd)

def locked_file(path):
 p=no_links(path)
 fd=os.open(p,os.O_RDWR|os.O_NOFOLLOW)
 s=os.fstat(fd)
 if not stat.S_ISREG(s.st_mode) or s.st_nlink!=1:
  os.close(fd)
  raise ValueError('unsafe lock')
 try:
  fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BaseException:
  os.close(fd)
  raise
 current=p.stat()
 if (current.st_dev,current.st_ino)!=(s.st_dev,s.st_ino):
  os.close(fd)
  raise ValueError('lock inode replaced')
 return fd,(s.st_dev,s.st_ino)

def check_lock(fd,path,identity):
 a=os.fstat(fd)
 b=no_links(path).stat()
 if (a.st_dev,a.st_ino)!=(b.st_dev,b.st_ino) or identity!=(a.st_dev,a.st_ino):
  raise ValueError('held lock replaced')

def file_identity(path):
 p=no_links(path)
 s=p.stat()
 if not stat.S_ISREG(s.st_mode) or s.st_nlink!=1:raise ValueError('unsafe control')
 return {'sha256':sha(stable_bytes(p)),'mode':stat.S_IMODE(s.st_mode),
         'uid':s.st_uid,'gid':s.st_gid,'inode':s.st_ino,'device':s.st_dev}

def command(args,*,input=None,timeout=30):
 p=subprocess.run(args,input=input,capture_output=True,timeout=timeout)
 if p.returncode:raise RuntimeError('bounded command failed: '+args[0]+'; private output suppressed')
 return p.stdout

def host_identity(root,scope):
 root=no_links(root)
 if scope=='synthetic-development':
  if root!=DEV_ROOT or socket.gethostname()!=DEV_HOST or os.geteuid()!=0 or not Path('/srv/dev-data').is_mount():
   raise ValueError('development host or root mismatch')
  expected=DEV_MOUNT;mount='/srv/dev-data'
 elif scope=='production':
  if root!=PROD_ROOT or os.geteuid()!=0 or not Path('/srv/community-brain').is_mount():
   raise ValueError('production root mismatch')
  contract=read_json(Path(__file__).with_name('production-contract.json'))
  machine=Path('/etc/machine-id').read_text().strip()
  if machine!=contract['machine_id']:raise ValueError('production machine mismatch')
  expected=contract['state_mount']['uuid'];mount='/srv/community-brain'
 else:raise ValueError('unknown scope')
 actual=command(['findmnt','-no','UUID',mount]).decode().strip()
 if actual!=expected:raise ValueError('mount UUID changed')
 return {'hostname':socket.gethostname(),'mount_uuid':actual,
         'machine_id':Path('/etc/machine-id').read_text().strip()}

def verify_packet(root,expected,*,owner_uid=None):
 root=no_links(root)
 if not HEX.fullmatch(expected) or not root.is_dir():raise ValueError('packet pin/root')
 if owner_uid is not None and root.stat().st_uid!=owner_uid:raise ValueError('packet owner')
 manifest=root/'packet-manifest.json'
 raw=stable_bytes(manifest)
 if sha(raw)!=expected:raise ValueError('packet manifest changed')
 entries=json.loads(raw)
 if not isinstance(entries,dict) or not entries:raise ValueError('empty packet')
 actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() or p.is_symlink()}
 if actual!=set(entries)|{'packet-manifest.json'}:raise ValueError('packet member set changed')
 for name,item in entries.items():
  rel=Path(name)
  if rel.is_absolute() or '..' in rel.parts or str(rel)!=name:raise ValueError('unsafe packet member')
  p=root/rel
  if p.is_symlink() or p.stat().st_mode&0o222 or p.stat().st_nlink!=1:raise ValueError('mutable or linked packet member')
  member=stable_bytes(p)
  if len(member)!=item['bytes'] or sha(member)!=item['sha256']:raise ValueError('packet member drift')
 return {'manifest_sha256':expected,'files':len(entries)}

def docker_row(ident):
 if not HEX.fullmatch(ident):raise ValueError('Docker identity must be exact')
 row=json.loads(command(['docker','inspect','--type','container',ident],timeout=10))[0]
 if row['Id']!=ident:raise ValueError('Docker identity changed')
 return row

def docker_fingerprint(row):
 return sha(encode({k:row[k] for k in ('Id','Image','Config','HostConfig','Mounts')}))

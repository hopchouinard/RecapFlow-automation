"""Mac-only exclusive VM108 packet transfer. Never invokes the packet."""
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
from build_packet import build,archive
from common import DEV_ROOT

REVISION=sys.argv[1]
LOCAL=Path.home()/'.local/state/community-brain-management/request035'
LOCAL.mkdir(mode=0o700,parents=True,exist_ok=True)
PACKET=LOCAL/REVISION
MANIFEST=build(PACKET,REVISION)
ARCHIVE=LOCAL/(REVISION+'.tar.gz')
ARCHIVE_SHA=archive(PACKET,ARCHIVE)
CODE="""import io,os,pathlib,sys,tarfile
os.umask(0o077)
base=pathlib.Path('/srv/dev-data/workspaces/cbm-stage2-controller-20260924-035')
base.mkdir(mode=0o700,exist_ok=True)
assert base.stat().st_uid==0 and base.stat().st_mode&0o777==0o700
root=base/sys.argv[1]
root.mkdir(mode=0o700)
with tarfile.open(fileobj=io.BytesIO(sys.stdin.buffer.read()),mode='r:gz') as tar:
 for member in tar:
  p=pathlib.PurePosixPath(member.name)
  if not member.isfile() or p.is_absolute() or '..' in p.parts or member.mode!=0o444:
   raise ValueError('unsafe packet member')
  target=root/member.name
  target.parent.mkdir(parents=True,exist_ok=True)
  with target.open('xb') as out:out.write(tar.extractfile(member).read())
  target.chmod(0o444)
for p in sorted(root.rglob('*'),reverse=True):
 if p.is_dir():p.chmod(0o555)
root.chmod(0o555)
"""
with ARCHIVE.open('rb') as incoming:
 p=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8','pchouinard@10.1.30.20',
                   shlex.join(['sudo','python3','-B','-c',CODE,REVISION])],stdin=incoming,capture_output=True,timeout=60)
if p.returncode:raise RuntimeError('exclusive VM108 staging failed: '+p.stderr.decode(errors='replace')[-500:])
identity={'revision':REVISION,'manifest_sha256':MANIFEST,'archive_sha256':ARCHIVE_SHA,
          'remote_path':str(DEV_ROOT/REVISION),'files':len(json.loads((PACKET/'packet-manifest.json').read_text()))}
(LOCAL/(REVISION+'-identity.json')).write_text(json.dumps(identity,indent=2)+'\n')
(LOCAL/(REVISION+'-identity.json')).chmod(0o600)
print(json.dumps(identity))

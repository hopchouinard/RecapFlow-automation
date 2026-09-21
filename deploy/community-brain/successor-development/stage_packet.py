import sys,json,tarfile,subprocess,shlex,hashlib,os
from pathlib import Path
os.umask(0o077)
source=Path(__file__).resolve().parent
local=Path.home()/'.local/state/community-brain-management/request028'
sys.path.insert(0,str(source))
from build_packet import build
from profiles import DEV_ROOT,DEV_HOST
revision=sys.argv[1];packet=local/revision
sha=build(packet,revision,json.loads((local/'documents/stabilization-image-files.json').read_text()),json.loads((local/'documents/monitor-image-equivalence.json').read_text()))
archive=local/(revision+'.tar')
with tarfile.open(archive,'w') as tar:
 for p in sorted(packet.rglob('*')):
  if p.is_file():tar.add(p,arcname=str(p.relative_to(packet)))
code="import pathlib,sys,tarfile,io,os;os.umask(0o077);base=pathlib.Path("+repr(DEV_ROOT)+");base.mkdir(mode=0o700,exist_ok=True);state=base/'state';state.mkdir(exist_ok=True);(state/'files').mkdir(exist_ok=True);(state/'automation').mkdir(exist_ok=True);[(state/n).touch(mode=0o600) for n in ('automation/runner.lock','files/.manual-worker.lock','files/.submission.lock') if not (state/n).exists()];root=base/"+repr(revision)+";assert not root.exists();root.mkdir(mode=0o755);root.chmod(0o755);t=tarfile.open(fileobj=io.BytesIO(sys.stdin.buffer.read()));t.extractall(root,filter='data');[p.chmod(0o444 if p.is_file() else 0o755) for p in root.rglob('*')]"
with archive.open('rb') as stream:
 p=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8',DEV_HOST,shlex.join(['sudo','python3','-B','-c',code])],stdin=stream,capture_output=True)
assert p.returncode==0,('stage failed',p.stderr.decode())
identity={'manifest_sha256':sha,'remote_path':DEV_ROOT+'/'+revision,'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
(local/(revision+'-identity.json')).write_text(json.dumps(identity,indent=2)+'\n')
(local/'packet-identity.json').write_text(json.dumps(identity,indent=2)+'\n')
print(json.dumps({**identity,'files':len(json.loads((packet/'packet-manifest.json').read_text()))}))

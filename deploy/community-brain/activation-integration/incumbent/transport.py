"""Private SSH transport under the live lease; no credential material in arguments."""
import hashlib
import json
from pathlib import Path
import shlex
import tempfile

VM = "pchouinard@10.1.30.21"
DB = "pchouinard@10.1.10.50"
PVE = "root@10.1.10.4"


def command(host, args, *, sudo=True):
    return ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8",
            "-o", "ServerAliveInterval=5", "-o", "ServerAliveCountMax=2", host,
            shlex.join((["sudo", "-n"] if sudo and not host.startswith('root@') else []) + args)]


class Transport:
    def __init__(self, lease):
        self.lease = lease

    def json(self, host, code, *, timeout=30):
        with tempfile.TemporaryFile() as output:
            self.lease.run(command(host, ["python3", "-B", "-c", code]), timeout=timeout, stdout=output)
            output.seek(0)
            return json.load(output)

    def adapter(self, host, name, operation, job, extra=(), *, timeout=240):
        path = "/usr/local/lib/community-brain-automatic/" + name
        with tempfile.TemporaryFile() as output:
            self.lease.run(command(host, ["python3", "-B", path, operation, job, *extra]), timeout=timeout, stdout=output)
            output.seek(0)
            return json.load(output)

    def download(self, host, source, destination):
        destination = Path(destination)
        code = "import pathlib,sys; p=pathlib.Path(" + repr(source) + "); assert p.is_file() and not p.is_symlink(); sys.stdout.buffer.write(p.read_bytes())"
        with destination.open("xb") as output:
            destination.chmod(0o600)
            self.lease.run(command(host, ["python3", "-B", "-c", code]), timeout=120, stdout=output)
        with destination.open("rb") as stream:
            return {"bytes": destination.stat().st_size, "sha256": hashlib.file_digest(stream, "sha256").hexdigest()}

    def deliver(self, source, host, destination, expected=None):
        source = Path(source)
        with source.open("rb") as stream:
            actual = {"bytes": source.stat().st_size, "sha256": hashlib.file_digest(stream, "sha256").hexdigest()}
        if expected is not None and expected != actual:
            raise ValueError("local transfer file mismatch")
        code = "PATH=" + repr(destination) + "\nEXPECTED=" + repr(actual) + "\n" + r'''
import pathlib,sys,hashlib,os,tempfile
p=pathlib.Path(PATH);p.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
assert not p.is_symlink() and p.parent.stat().st_mode&0o777==0o700
def check(q):
 with q.open('rb') as f:return q.stat().st_size==EXPECTED['bytes'] and hashlib.file_digest(f,'sha256').hexdigest()==EXPECTED['sha256']
if p.exists():
 assert check(p) and p.stat().st_mode&0o777==0o600
 while sys.stdin.buffer.read(1024*1024):pass
else:
 fd,tmp=tempfile.mkstemp(dir=p.parent,prefix='.'+p.name+'.')
 with os.fdopen(fd,'wb') as f:
  os.fchmod(f.fileno(),0o600)
  while data:=sys.stdin.buffer.read(1024*1024):f.write(data)
  f.flush();os.fsync(f.fileno())
 assert check(pathlib.Path(tmp))
 os.link(tmp,p);os.unlink(tmp)
 fd=os.open(p.parent,os.O_RDONLY);os.fsync(fd);os.close(fd)
'''
        with source.open("rb") as stream:
            self.lease.run(command(host, ["python3", "-B", "-c", code]), timeout=120, stdin=stream)
        return actual

    def verify_set(self, host, directory, expected):
        code = "DIRECTORY=" + repr(directory) + "\nEXPECTED=" + repr(expected) + "\n" + r'''
import pathlib,json,hashlib
p=pathlib.Path(DIRECTORY);assert not p.is_symlink() and p.stat().st_mode&0o777==0o700
for name,spec in EXPECTED.items():
 assert '/' not in name and name not in ('.','..')
 q=p/name;assert not q.is_symlink() and q.is_file() and q.stat().st_uid==0 and q.stat().st_mode&0o777==0o600 and q.stat().st_size==spec['bytes']
 with q.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==spec['sha256']
print(json.dumps({'verified':True,'files':len(EXPECTED)}))
'''
        return self.json(host, code, timeout=120)

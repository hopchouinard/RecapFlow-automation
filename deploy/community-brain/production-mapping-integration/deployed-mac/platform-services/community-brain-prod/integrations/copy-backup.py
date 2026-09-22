"""Mac transfer of latest scoped DB dump into the PBS-covered application state disk."""
import subprocess,json,tempfile,hashlib,shlex
from pathlib import Path
opts=['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8']
def command(host,code):return opts+[host,'sudo python3 -c '+shlex.quote(code)]
listing="import pathlib,json; p=sorted(pathlib.Path('/var/backups/community-brain').glob('*.dump'))[-1]; print(json.dumps({'name':p.name,'size':p.stat().st_size}))"
r=subprocess.run(command('pchouinard@10.1.10.50',listing),capture_output=True,text=True,check=True)
info=json.loads(r.stdout);name=info['name'];assert name.endswith('.dump') and '/' not in name
with tempfile.TemporaryFile() as f:
 code="import pathlib,sys; sys.stdout.buffer.write(pathlib.Path('/var/backups/community-brain/"+name+"').read_bytes())"
 r=subprocess.run(command('pchouinard@10.1.10.50',code),stdout=f,stderr=subprocess.DEVNULL)
 assert r.returncode==0
 assert f.tell()==info['size']
 f.seek(0);sha=hashlib.file_digest(f,'sha256').hexdigest();f.seek(0)
 code="""import pathlib,sys,hashlib,os
root=pathlib.Path('/srv/community-brain/db-backups');root.mkdir(mode=0o700,exist_ok=True);root.chmod(0o700)
name=NAME
p=root/(name+'.partial')
fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0o600)
with os.fdopen(fd,'wb') as f:
 while chunk:=sys.stdin.buffer.read(1024*1024):f.write(chunk)
with p.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==SHA
os.replace(p,root/name)
for old in sorted(root.glob('*.dump'))[:-14]:old.unlink()
print('verified')
""".replace('NAME',repr(name)).replace('SHA',repr(sha))
 r=subprocess.run(command('pchouinard@10.1.30.21',code),stdin=f,capture_output=True,text=True)
 assert r.returncode==0 and r.stdout.strip()=='verified','Private backup transfer failed'
receipt={'off_host_path':'/srv/community-brain/db-backups/'+name,'sha256':sha,'bytes':info['size'],'verified':True,'pbs_capture':'VM109 existing nightly 21:00 America/Toronto job; next snapshot captures this copy','retention_copies':14}
Path(__file__).with_name('backup-copy-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))

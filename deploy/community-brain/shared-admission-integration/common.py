"""Fixed development boundary and immutable operation bindings."""
import hashlib,json,os,socket,subprocess,sys,time,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'recovery-core'))
sys.path.insert(0,str(Path(__file__).parent/'forge-admission'))
import admission
import recovery as r
ROOT=Path('/srv/dev-data/workspaces/cbm-shared-admission-20260921-032')
HOST='pchouinard@10.1.30.20'

def atom(path,value):
    path=Path(path);tmp=path.with_name('.'+path.name+'.'+str(os.getpid()))
    r.write_new(tmp,r.encode(value));os.replace(tmp,path)
    fd=os.open(path.parent,os.O_RDONLY)
    try:os.fsync(fd)
    finally:os.close(fd)

def command(args,data=None,timeout=8):
    result=subprocess.run(args,input=data,capture_output=True,timeout=timeout)
    if result.returncode:raise RuntimeError('command failed; output suppressed')
    return result.stdout

def inspect(name):
    return json.loads(command(['docker','inspect','--type','container',name]))[0]

def fingerprint(row):
    value={k:row[k] for k in ('Id','Image','Config','HostConfig')}
    value['Mounts']=sorted(row['Mounts'],key=lambda m:m['Destination'])
    return r.sha(r.encode(value))

def packet(root,expected):
    root=r.no_links(root);raw=r.stable_bytes(root/'packet-manifest.json')
    if r.sha(raw)!=expected:raise ValueError('source manifest mismatch')
    entries=json.loads(raw)
    actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    if actual!=set(entries)|{'packet-manifest.json'}:raise ValueError('source member mismatch')
    for n,h in entries.items():
        p=r.no_links(root/n)
        if not p.is_relative_to(root) or r.sha(r.stable_bytes(p))!=h:raise ValueError('source bytes mismatch')

def load_spec(path,expected,check_time=True):
    if check_time and (ROOT/'retired.json').exists():raise ValueError('retired synthetic root')
    path=r.no_links(path);raw=r.stable_bytes(path)
    if r.sha(raw)!=expected:raise ValueError('specification hash mismatch')
    s=json.loads(raw)
    required={'schema','scope','owner_id','operation_id','capture_id','packet','packet_sha256','operation','fixture','locks','holds','hold_bindings','incumbent','database','deadlines','exercise','kind','machine_id','host_boot_id','volume','signing_sha256'}
    if set(s)!=required or s['schema']!=1 or s['scope']!='synthetic-development':raise ValueError('production/unknown specification refused')
    if socket.gethostname()!='community-brain-dev':raise ValueError('VM108 only')
    import re
    for k in ('owner_id','operation_id','capture_id'):
        if not re.fullmatch('[a-z0-9][a-z0-9-]{7,70}',s[k]):raise ValueError('invalid operation identity')
    for p in [s['packet'],s['operation'],s['fixture'],*s['locks'],*s['holds']]:
        if not r.no_links(p).is_relative_to(ROOT):raise ValueError('foreign operation path')
    if Path(s['operation'])!=ROOT/'operations'/s['operation_id']:raise ValueError('operation path mismatch')
    fixture=Path(s['fixture'])
    if s['locks']!=[str(fixture/'controls'/n) for n in ('runner.lock','manual.lock','submission.lock')]:raise ValueError('lock order mismatch')
    if s['holds']!=[str(fixture/'controls'/n) for n in ('paused','attention.json','boot-state.json','checkpoint-needed.json')]:raise ValueError('hold set mismatch')
    ds=s['deadlines']
    if set(ds)!={'prepare_by','capture_by','serving_by','validate_by'}:raise ValueError('deadline set mismatch')
    vals=[ds[k] for k in ('prepare_by','capture_by','serving_by','validate_by')]
    if any(type(v) not in (int,float) or not math.isfinite(v) for v in vals) or not all(a<b for a,b in zip(vals,vals[1:])):raise ValueError('invalid deadlines')
    if check_time and (vals[0]<=time.time() or vals[-1]>time.time()+600 or ds['serving_by']-time.time()<12):raise ValueError('stale or unbounded specification')
    if s['kind'] not in ('scheduler','manual','capture'):raise ValueError('unknown entry point')
    if s['machine_id']!=machine_id():raise ValueError('target machine identity mismatch')
    if s['exercise'] not in ('normal','hold_for_expiry','wait_for_interrupt','wait_for_fence_loss','failed_finalizer'):raise ValueError('unknown exercise')
    packet(s['packet'],s['packet_sha256'])
    if Path(__file__).resolve().parent!=Path(s['packet']):raise ValueError('executing source packet not bound')
    for key in ('source','restore'):
        identity=s['database'][key]
        row=inspect(identity['id'])
        if not identity['name'].startswith('cbm-r032-pg-') or row['Id']!=identity['id'] or row['Name'].lstrip('/')!=identity['name'] or row['Image']!=identity['image'] or row['HostConfig']['NetworkMode']!='none' or row['HostConfig']['PortBindings']:raise ValueError('foreign database')
    if not s['incumbent']['name'].startswith('cbm-r032-inc-'):raise ValueError('foreign incumbent')
    return s

def verify_incumbent(s):
    row=inspect(s['incumbent']['id'])
    if row['Name'].lstrip('/')!=s['incumbent']['name'] or fingerprint(row)!=s['incumbent']['fingerprint']:raise ValueError('incumbent changed')
    if row['HostConfig']['NetworkMode']!='none' or row['HostConfig']['PortBindings']:raise ValueError('incumbent isolation changed')
    volume=s['volume'];state=Path(s['fixture'])/'state';st=state.stat()
    if volume!={'path':str(state),'device':st.st_dev,'inode':st.st_ino,'mountpoint':'/srv/state'}:raise ValueError('volume identity drift')
    mounts=[m for m in row['Mounts'] if m['Destination']=='/srv/state']
    if len(mounts)!=1 or mounts[0]['Source']!=str(state) or mounts[0]['RW']:raise ValueError('volume binding drift')
    if r.sha(r.stable_bytes(Path(s['fixture'])/'private/signing.key'))!=s['signing_sha256']:raise ValueError('signing identity drift')
    return row

def healthy(s):
    row=verify_incumbent(s)
    if not row['State']['Running']:return False
    try:command(['docker','exec',row['Id'],'python','-B','-c',"import urllib.request; assert urllib.request.urlopen('http://127.0.0.1:8080',timeout=1).status==200"],timeout=3)
    except (RuntimeError,subprocess.TimeoutExpired):return False
    return True

def event(op,kind,**fields):
    p=Path(op)/'events.jsonl'
    with p.open('ab') as f:
        os.chmod(p,0o600);f.write(r.encode(dict(event=kind,at=time.time(),**fields)).replace(b'\n',b' ')+b'\n');f.flush();os.fsync(f.fileno())


def machine_id():
    return Path('/etc/machine-id').read_text().strip()

def boot_id():
    return Path('/proc/sys/kernel/random/boot_id').read_text().strip()

def admission_spec(s):
    return {'scope':s['scope'],'kind':s['kind'],'operation_id':s['operation_id'],'owner_id':s['owner_id'],
            'packet_sha256':s['packet_sha256'],'target':'community-brain-dev','incumbent_id':s['incumbent']['id'],
            'holds_sha256':admission.digest(s['hold_bindings']),'deadline_epoch':s['deadlines']['validate_by']}

def ready_path(s):return Path(s['fixture'])/'startup-ready.json'

def ready(s,sha):
    gate=json.loads(r.stable_bytes(ROOT/'boot-admission.json'))
    if gate.get('admission_open') is not True or gate.get('boot_id')!=boot_id() or gate.get('machine_id')!=machine_id():raise ValueError('boot admission is closed')
    v=json.loads(r.stable_bytes(ready_path(s)))
    if v['boot_id']!=boot_id() or v['machine_id']!=machine_id() or v['spec_sha256']!=sha or v['packet_sha256']!=s['packet_sha256']:
        raise ValueError('startup reconciliation required')
    return v

"""One actual candidate admission path for scheduler, manual and capture callers."""
import json,os,shlex,subprocess,sys,time,secrets
from pathlib import Path
import common as c
r=c.r;a=c.admission
BASE=Path.home()/'.local/state/community-brain-management'
STATE=BASE/'request032'
MUTEX=BASE/'scheduler.lock'

def command(s,mode,*extra):
    path=str(c.ROOT/'specs'/(s['operation_id']+'.json'));sha=r.sha(r.encode(s))
    return ['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes','-o','ConnectTimeout=8','-o','ServerAliveInterval=5','-o','ServerAliveCountMax=2',c.HOST,
            shlex.join(['sudo','-n','python3','-B',str(Path(s['packet'])/'target.py'),mode,path,sha,*extra])]

def verify_observation(s,challenge,v):
    if set(v)!={'challenge','target_spec_sha256','packet_sha256','machine_id','current_boot_id','startup','finalizer','proof','incumbent_fingerprint','writer_controls_restored'}:raise ValueError('unknown authenticated observation field')
    sha=r.sha(r.encode(s))
    if v['challenge']!=challenge or v['target_spec_sha256']!=sha or v['packet_sha256']!=s['packet_sha256'] or v['machine_id']!=s['machine_id'] or v['incumbent_fingerprint']!=s['incumbent']['fingerprint']:raise ValueError('foreign/tampered observation')
    boot=v['current_boot_id'];startup=v['startup'];final=v['finalizer']
    if not startup or not final or startup.get('boot_id')!=boot or startup.get('machine_id')!=s['machine_id'] or startup.get('spec_sha256')!=sha or startup.get('packet_sha256')!=s['packet_sha256'] or startup.get('original_boot_id')!=s['host_boot_id']:raise ValueError('current startup reconciliation missing')
    if final.get('boot_id')!=boot or final.get('spec_sha256')!=sha or final.get('verified') is not True or v['proof']['boot_id']!=boot or v['writer_controls_restored'] is not True:raise ValueError('current finalizer/writer recovery missing')
    a.Gate(STATE/'journal',MUTEX).proof(c.admission_spec(s),v['proof'],time.time())
    return v['proof']

def observe(s):
    challenge=secrets.token_hex(32);p=subprocess.run(command(s,'observe',challenge),capture_output=True,timeout=25)
    if p.returncode:raise RuntimeError('authenticated SSH observation unavailable; intent retained')
    v=json.loads(p.stdout);proof=verify_observation(s,challenge,v)
    c.atom(STATE/(s['operation_id']+'-observation.json'),v)
    return proof

def legacy_observation(s):
    args=['sudo','-n','python3','-B',str(Path(s['packet'])/'legacy_target.py')]
    p=subprocess.run(['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes','-o','ConnectTimeout=8',c.HOST,shlex.join(args)],capture_output=True,timeout=20)
    if p.returncode:raise ValueError('legacy readback unavailable')
    return json.loads(p.stdout)

def legacy_guard(s):
    pins=a.read(STATE/'legacy-retirement.json')
    expected=BASE/'request029/activation-pending.json'
    members={p for p in BASE.rglob('*.json') if p.name in ('pending.json','activation-pending.json','manual-pending.json') and ('request032' not in p.parts or 'legacy-conflicts' in p.parts)}
    if members!={expected}:raise ValueError('legacy/manual/request031 pending conflict')
    for name,sha in pins['local_files'].items():
        if r.sha(r.stable_bytes(r.no_links(name)))!=sha:raise ValueError('legacy pending identity changed')
    if legacy_observation(s)!=pins['target']:raise ValueError('legacy retired disposition changed; do not clear/migrate')

def dispatch(s):
    p=subprocess.Popen(command(s,'dispatch-wait'),stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    c.atom(STATE/'client.json',{'operation_id':s['operation_id'],'owner_pid':os.getpid(),'ssh_pid':p.pid,'at':time.time()})
    try:p.communicate(timeout=max(1,s['deadlines']['validate_by']-time.time()+10))
    except subprocess.TimeoutExpired:p.kill();p.communicate()
    # Return status is never authoritative; a fresh challenged readback follows.

def load(path,kind):
    raw=r.stable_bytes(r.no_links(path));s=json.loads(raw)
    if sys.platform!='darwin' or s['scope']!='synthetic-development' or s['kind']!=kind:raise ValueError('candidate entry point/scope mismatch')
    if Path(s['packet']).parent!=c.ROOT or Path(s['operation'])!=c.ROOT/'operations'/s['operation_id']:raise ValueError('foreign candidate target')
    a.validate(c.admission_spec(s))
    packet=a.read(STATE/(Path(s['packet']).name+'.json'))
    if packet['manifest_sha256']!=s['packet_sha256']:raise ValueError('local source manifest identity mismatch')
    local=Path(__file__).resolve().parent
    actual={str(p.relative_to(local)) for p in local.rglob('*') if p.is_file()}
    if actual-set(packet['files']) not in (set(),{'packet-manifest.json'}):raise ValueError('unknown local source member')
    for name,sha in packet['files'].items():
        if r.sha(r.stable_bytes(r.no_links(local/name)))!=sha:raise ValueError('executing Mac source differs from packet')
    pin=a.read(STATE/'host-bindings.json')['mutex'];st=r.no_links(MUTEX).stat()
    if pin!={'device':st.st_dev,'inode':st.st_ino,'uid':st.st_uid,'gid':st.st_gid,'mode':st.st_mode&511}:raise ValueError('existing Mac mutex identity changed')
    return s

def execute(kind,path,action=None,reconcile=False):
    s=load(path,kind);gate=a.Gate(STATE/'journal',MUTEX)
    with gate.locked():
        legacy_guard(s)
        spec=c.admission_spec(s)
        if reconcile:return gate.reconcile(spec,lambda:observe(s))
        return gate.invoke(spec,lambda:(action(s) if action else dispatch(s)),lambda:observe(s))

def cli(kind):
    mode,path=sys.argv[1:]
    if mode not in ('dispatch','reconcile'):raise ValueError('unknown mode')
    print(json.dumps(execute(kind,path,reconcile=mode=='reconcile')))

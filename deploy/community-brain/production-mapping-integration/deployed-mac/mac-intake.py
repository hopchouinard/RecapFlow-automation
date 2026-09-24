"""Existing hourly hook, with exact-path enumeration and terminal ownership refusal."""
import pathlib,json,subprocess,datetime,os,sys,traceback,time
from mac_intake_policy import decide
P=pathlib.Path.home()/'.local/state/community-brain-window/CBM-RETRIEVAL-20260910-001.json'
LAST_OPERATION='start'
def apple(code):
    global LAST_OPERATION
    LAST_OPERATION='folder_action_set' if 'set enabled' in code else 'folder_action_query'
    return subprocess.check_output(['osascript','-e',code],text=True,timeout=15,stderr=subprocess.PIPE).strip()
def report(state,error=None):
    root=pathlib.Path.home()/'.local/state/community-brain-management'
    value={'state':state,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'operation':LAST_OPERATION}
    if error is not None:
        value['error_class']=type(error).__name__
        value['frames']=[{'file':pathlib.Path(f.filename).name,'line':f.lineno} for f in traceback.extract_tb(error.__traceback__)]
        value['returncode']=getattr(error,'returncode',None)
        value['timeout']=getattr(error,'timeout',None)
        raw=getattr(error,'stderr',None)
        if raw:
            p=root/'legacy-intake-error.private.log';p.write_text(raw.decode() if isinstance(raw,bytes) else raw);p.chmod(0o600)
    p=root/'legacy-intake-status.json';t=p.with_suffix('.tmp');t.write_text(json.dumps(value,indent=2)+'\n');t.chmod(0o600);t.replace(p)
def exact_action(value=None):
    # Enumeration forces System Events to load its associations before exact matching.
    path='/Volumes/NVMe_2TB_Work/Documents/Zoom'
    apple('tell application "System Events" to get {name, path, enabled} of every folder action')
    suffix='get enabled of item 1 of matches' if value is None else 'set enabled of item 1 of matches to '+str(value).lower()
    code='tell application "System Events"\nset matches to {}\nrepeat with candidate in (get every folder action)\nif ((get path of candidate) as text) is "'+path+'" then set end of matches to contents of candidate\nend repeat\nif (count of matches) is not 1 then error "Exact legacy association missing or ambiguous"\n'+suffix+'\nend tell'
    return apple(code)
def disabled():
    if exact_action()!='false':exact_action(False)
    assert exact_action()=='false'
    assert subprocess.run(['launchctl','print','gui/'+str(os.getuid())+'/com.patchoutech.sync-zoom-chats'],capture_output=True).returncode!=0,'Legacy LaunchAgent unexpectedly loaded'
def resume(value):
    if exact_action()!=str(value).lower():exact_action(value)
    assert exact_action()==str(value).lower()
def save(d):
    t=P.with_suffix('.tmp');t.write_text(json.dumps(d,indent=2)+'\n');t.chmod(0o600)
    with t.open('rb') as f:os.fsync(f.fileno())
    t.replace(P)
    fd=os.open(P.parent,os.O_RDONLY)
    try:os.fsync(fd)
    finally:os.close(fd)
def fetch():
    r=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8','n8n-automation','sudo python3 /usr/local/lib/community-brain-window/window-control.py status'],capture_output=True,text=True,timeout=15)
    assert r.returncode==0,'Server control state unavailable; do not resume';return json.loads(r.stdout)
def main():
    assert sys.argv[1:] in [[],['poll']]
    d=json.loads(P.read_text());assert d['path']=='/Volumes/NVMe_2TB_Work/Documents/Zoom'
    print(json.dumps({'intake_state':decide(d,fetch,save,disabled,resume),'legacy_launchagent_unchanged':True}))
if __name__=='__main__':
    try:
        main();report('passed')
    except Exception as error:
        report('failed',error)
        raise SystemExit('Legacy intake state unconfirmed; no automatic resume. Inspect management status.') from None

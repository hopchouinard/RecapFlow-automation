"""Preserve and independently recheck the existing retired Request029 disposition."""
import hashlib,json,subprocess,shlex
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=Path.home()/'.local/state/community-brain-management'
def check(mutex):
 if Path(mutex)!=BASE/'scheduler.lock':return {'scope':'isolated fixture mutex'}
 v=json.loads((HERE/'legacy-bindings.json').read_bytes());st=Path(mutex).stat()
 if v['mutex']!={'device':st.st_dev,'inode':st.st_ino,'uid':st.st_uid,'gid':st.st_gid,'mode':st.st_mode&511}:raise ValueError('installed mutex changed')
 members={str(p) for p in BASE.rglob('*.json') if p.name in ('pending.json','activation-pending.json','manual-pending.json') and ('request032' not in p.parts or 'legacy-conflicts' in p.parts)}
 if members!={str(BASE/'request029/activation-pending.json')}:raise ValueError('unreviewed legacy pending')
 for name,h in v['local_files'].items():
  p=Path(name)
  if p.is_symlink() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise ValueError('legacy state changed')
 journal=BASE/'request032/journal'
 if {p.name for p in journal.iterdir()}!=set(v['previous_journal']):raise ValueError('previous shared journal changed')
 for name,h in v['previous_journal'].items():
  if hashlib.sha256((journal/name/'resolution.json').read_bytes()).hexdigest()!=h:raise ValueError('previous resolution changed')
 packet='/srv/dev-data/workspaces/cbm-shared-admission-20260921-032/packet-v6'
 code="import pathlib,json,hashlib,runpy; p=pathlib.Path("+repr(packet)+"); m=p/'packet-manifest.json'; assert hashlib.sha256(m.read_bytes()).hexdigest()=="+repr(v['previous_packet_sha256'])+"; assert all(hashlib.sha256((p/n).read_bytes()).hexdigest()==h for n,h in json.loads(m.read_bytes()).items()); runpy.run_path(str(p/'legacy_target.py'),run_name='__main__')"
 # legacy_target imports sibling modules; use its sealed directory as sys.path.
 code="import sys;sys.path.insert(0,"+repr(packet)+");"+code
 r=subprocess.run(['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes','-o','ConnectTimeout=8','pchouinard@10.1.30.20','sudo -n python3 -B -c '+shlex.quote(code)],capture_output=True,timeout=25)
 if r.returncode or json.loads(r.stdout)!=v['target']:raise ValueError('retired target readback changed or unavailable')
 return {'legacy_retained':True,'prior_shared_journal_resolved':True,'fresh_authenticated_readback':True}

"""Inherited descriptor plus durable owner/source intent; env flag alone is not authority."""
import json,os,sys,subprocess
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from helper_contracts import verify_sources
ALLOWED={'renew-service-tokens.py','provision-nats-tls.py','renew-app-tls.py','copy-backup.py','management-health.py'}
def check(name):
 if name not in ALLOWED or os.environ.get('CBM_SCOPE')!='synthetic-development':raise ValueError('closed helper/scope boundary')
 fd=int(os.environ['CBM_ADMISSION_FD']);st=os.fstat(fd);p=Path(os.environ['CBM_ADMISSION_INTENT'])
 if p.is_symlink() or p.stat().st_uid!=os.getuid() or p.stat().st_mode&511!=384:raise ValueError('private intent required')
 v=json.loads(p.read_bytes())
 parent=os.getppid();grandparent=int(subprocess.check_output(['ps','-o','ppid=','-p',str(parent)],text=True).strip())
 root=Path(os.environ['CBM_DEVELOPMENT_ROOT']).resolve()
 allowed=[Path.home()/'.local/state/community-brain-management/request033',Path('/srv/dev-data/workspaces/cbm-production-mapping-20260922-033')]
 if not any(root.is_relative_to(a) for a in allowed) or not Path(os.environ['INFISICAL_ENV_FILE']).resolve().is_relative_to(root):raise ValueError('isolated environment source required')
 if v['owner_pid'] not in (parent,grandparent) or (v['mutex_device'],v['mutex_inode'])!=(st.st_dev,st.st_ino) or v['source_sha256']!=verify_sources():raise ValueError('foreign owner/mutex/source')
 if (p.parent/'resolved.json').exists():raise ValueError('resolved operation cannot invoke helper')
 return True
if __name__=='__main__':check(sys.argv[1])

"""Every new boot starts paused; a restored schedule never implies reconciliation."""
import json
import os
from pathlib import Path
import subprocess
import sys
from checkpoint_acceptance import atomic

ROOT = Path('/srv/community-brain/automation')
LAUNCHER = '/srv/community-brain/workspaces/cbm-workspace-recovery-20260917-effective-r020/automatic_host.py'


def enforce(root, boot_id, *, force=False):
    root=Path(root);root.mkdir(parents=True,exist_ok=True,mode=0o700)
    path=root/'boot-state.json'
    existing=json.loads(path.read_text()) if path.exists() else None
    if force or existing is None or existing.get('boot_id')!=boot_id:
        atomic(root/'paused',{'reason':'boot_or_restore_requires_explicit_reconciliation','boot_id':boot_id})
        atomic(path,{'boot_id':boot_id,'reconciled':False})
    if not json.loads(path.read_text()).get('reconciled'):
        if not (root/'paused').exists():
            atomic(root/'paused',{'reason':'boot_or_restore_requires_explicit_reconciliation','boot_id':boot_id})
        return False
    return not (root/'paused').exists()


if __name__=='__main__':
    os.umask(0o077)
    os.environ['PYTHONDONTWRITEBYTECODE']='1'
    boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    operation=sys.argv[1]
    if operation not in ('boot','tick'):raise SystemExit(2)
    enforce(ROOT,boot,force=operation=='boot')
    if operation=='tick':
        # Even a paused tick updates bounded host status through the launcher's
        # normal runner lock, preserving the monitoring heartbeat.
        raise SystemExit(subprocess.run(['/usr/bin/python3','-B',LAUNCHER],check=False).returncode)

"""Explicit disposable-development boot reconciliation; never an automatic resume."""
from pathlib import Path
import json,os
from runtime_contract import load

def atomic(path,value):
    p=path.with_suffix('.tmp');p.write_text(json.dumps(value,sort_keys=True));p.chmod(0o600);p.replace(path)

def inspect(expected):
    v=load(expected);root=Path(v['root'])/'automation'
    stored=json.loads((root/'boot-state.json').read_text());boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    return {'boot_matches':stored.get('boot_id')==boot,'reconciled':stored.get('reconciled',False),'launcher':v['boot_launcher'],'held':(root/'paused').exists(),'production_changes':False}

def enforce(expected):
    v=load(expected);root=Path(v['root'])/'automation';boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    p=root/'boot-state.json';before=json.loads(p.read_text())
    if before.get('boot_id')!=boot or not before.get('reconciled'):
        atomic(root/'paused',{'reason':'new_boot_requires_explicit_reconciliation','boot_id':boot})
        atomic(p,{'boot_id':boot,'reconciled':False})
    return inspect(expected)

def reconcile(expected,boot_id):
    v=load(expected);root=Path(v['root'])/'automation';actual=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    if boot_id!=actual or (root/'attention.json').exists():raise ValueError('boot or attention remains unresolved')
    atomic(root/'boot-state.json',{'boot_id':actual,'reconciled':True,'scope':'disposable-request028'})
    (root/'paused').unlink(missing_ok=True)
    return inspect(expected)

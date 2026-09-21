"""Retain a VM108-only journal rehearsal; observations are synthetic fixtures."""
import json
from pathlib import Path
import socket
import sys
import time
import admission as a

root=a.path(sys.argv[1])
if socket.gethostname()!='community-brain-dev' or not root.is_relative_to(Path('/srv/dev-data/workspaces')):raise ValueError('VM108 only')
root.mkdir(mode=0o700);(root/'journal').mkdir(mode=0o700);(root/'scheduler.lock').touch(mode=0o600)
spec=dict(scope='synthetic-development',kind='capture',operation_id='capture-retained001',owner_id='forge-retained001',packet_sha256=a.digest({p.name:p.read_text() for p in Path(__file__).parent.glob('*.py')}),target='community-brain-dev',incumbent_id='2'*64,holds_sha256='3'*64,deadline_epoch=time.time()+60)
a.create(root/'spec.json',spec)
with a.Gate(root/'journal',root/'scheduler.lock').locked() as gate:
    gate.begin(spec)
    blocked=[]
    for kind in ('scheduler','manual','capture'):
        try:gate.begin({**spec,'kind':kind,'operation_id':kind+'-blocked001'})
        except ValueError:blocked.append(kind)
        else:raise AssertionError('unresolved admission bypass')
    proof=dict(spec_sha256=a.digest(spec),state='aborted_restored',incumbent_id=spec['incumbent_id'],holds_sha256=spec['holds_sha256'],target=spec['target'],observed_epoch=time.time(),boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),finalizer_seen=True,service_inactive=True,healthy=True)
    gate.reconcile(spec,lambda:proof)
    assert not gate.unresolved()
summary=dict(blocked_entry_points=blocked,resolved_after_readback=True,observation_source='synthetic fixture; no container or service effects',production_execution=False)
a.create(root/'summary.json',summary);print(json.dumps(summary))

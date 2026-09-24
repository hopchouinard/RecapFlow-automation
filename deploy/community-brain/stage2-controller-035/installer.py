"""VM108-only reversible systemd enrollment; production output is review-only."""
import json
import os
from pathlib import Path
import sys
from common import DEV_ROOT,create,encode,host_identity,read_json,sha,stable_bytes,verify_packet

UNIT_ROOT=Path('/etc/systemd/system')
NAMES=('cbm-r035-worker.service','cbm-r035-finalizer.service',
       'cbm-r035-guardian.service','cbm-r035-guardian.timer')

def units(packet_sha):
 p=str(Path(__file__).resolve().parent)
 common='RequiresMountsFor=/srv/dev-data\nAfter=docker.service\nRequires=docker.service\nConditionPathExists='+str(DEV_ROOT/'state/automation/paused')+'\nConditionPathExists='+str(DEV_ROOT/'fixture.json')+'\n'
 worker='[Unit]\nDescription=Request035 synthetic one-shot worker\n'+common+'[Service]\nType=oneshot\nExecStart=/usr/bin/python3 -B '+p+'/controller.py worker '+packet_sha+'\nExecStopPost=/usr/bin/systemctl start --no-block cbm-r035-finalizer.service\nTimeoutStartSec=160\nTimeoutStopSec=15\nKillMode=control-group\n'
 finalizer='[Unit]\nDescription=Request035 independent same-incumbent finalizer\n'+common+'[Service]\nType=oneshot\nExecStart=/usr/bin/python3 -B '+p+'/finalizer.py finalize '+packet_sha+'\nTimeoutStartSec=90\n'
 guardian='[Unit]\nDescription=Request035 independent deadline guardian\n'+common+'[Service]\nType=oneshot\nExecStart=/usr/bin/python3 -B '+p+'/finalizer.py guardian '+packet_sha+'\nTimeoutStartSec=20\n'
 timer='[Unit]\nDescription=Request035 deadline guardian tick\nConditionPathExists='+str(DEV_ROOT/'fixture.json')+'\n[Timer]\nOnBootSec=10s\nOnUnitActiveSec=10s\nAccuracySec=1s\nUnit=cbm-r035-guardian.service\n[Install]\nWantedBy=timers.target\n'
 return dict(zip(NAMES,(worker,finalizer,guardian,timer)))

def execute(mode,packet_sha):
 host=host_identity(DEV_ROOT,'synthetic-development')
 packet=Path(__file__).resolve().parent
 verified=verify_packet(packet,packet_sha,owner_uid=0)
 proposed=units(packet_sha)
 marker=DEV_ROOT/'control/installer.json'
 current={name:(UNIT_ROOT/name).read_text() if (UNIT_ROOT/name).exists() else None for name in NAMES}
 if any(value not in (None,proposed[name]) for name,value in current.items()):
  raise ValueError('foreign systemd unit collision')
 if mode=='dry-run':
  return {'scope':'synthetic-development','host':host,'packet':verified,
          'units_sha256':{n:sha(v.encode()) for n,v in proposed.items()},
          'existing':{n:current[n] is not None for n in NAMES},'mutated':False}
 if mode=='install':
  if marker.exists() and read_json(marker)['packet_manifest_sha256']!=packet_sha:
   raise ValueError('different installed packet')
  for name,value in proposed.items():
   path=UNIT_ROOT/name
   if not path.exists():create(path,value.encode(),0o644)
  __import__('subprocess').run(['systemctl','daemon-reload'],check=True,timeout=15)
  __import__('subprocess').run(['systemctl','start','cbm-r035-guardian.timer'],check=True,timeout=15)
  if not marker.exists():create(marker,encode({'packet_manifest_sha256':packet_sha,'units_sha256':{n:sha(v.encode()) for n,v in proposed.items()},'host':host}))
  return {'installed':True,'idempotent':True,'packet_manifest_sha256':packet_sha,'guardian_timer_active':True}
 if mode=='uninstall':
  if marker.exists() and read_json(marker)['packet_manifest_sha256']!=packet_sha:raise ValueError('installed packet mismatch')
  active=DEV_ROOT/'journal/active.json'
  if active.exists():
   attempt=read_json(active)['attempt']
   result=DEV_ROOT/'journal'/attempt/'result.json'
   if not result.exists() or not read_json(result).get('serving_restored'):
    raise ValueError('unresolved intent blocks uninstall')
  __import__('subprocess').run(['systemctl','stop','cbm-r035-guardian.timer'],check=False,timeout=15)
  for name in NAMES:
   path=UNIT_ROOT/name
   if path.exists():path.unlink()
  __import__('subprocess').run(['systemctl','daemon-reload'],check=True,timeout=15)
  if marker.exists():marker.unlink()
  return {'installed':False,'retained_fixture':True,'retained_journal':True,'retained_packet':True}
 raise ValueError('unsupported mode')

if __name__=='__main__':
 os.umask(0o077)
 print(json.dumps(execute(sys.argv[1],sys.argv[2]),sort_keys=True))

"""VM101 entry point. Legacy rollback retained until the atomic terminal state."""
import pathlib,importlib.util,json,sys,os
from ownership_control import Controller
assert os.geteuid()==0
ROOT=pathlib.Path('/var/lib/community-brain-window/CBM-RETRIEVAL-20260910-001')
spec=importlib.util.spec_from_file_location('legacy_window',str(ROOT/'ownership-007-before/window-control.py'))
legacy=importlib.util.module_from_spec(spec);spec.loader.exec_module(legacy)
def verify_live():
    assert legacy.run(['systemctl','is-active','cbm-retrieval-deadline.timer']).strip()=='active'
    assert not legacy.inspect('n8n')['State']['Running'] and legacy.inspect('community_brain_retrieval')['State']['Paused']
    assert all(legacy.inspect(n)['HostConfig']['RestartPolicy']['Name']=='no' for n in ['n8n','community_brain_retrieval'])
    entries=json.loads((ROOT/'inode-flags.json').read_text());assert len(entries)==2867
    assert all(pathlib.Path(x['path']).stat().st_ino==x['inode'] and legacy.flags(x['path'])&legacy.IMMUTABLE for x in entries)
    assert legacy.run(['crontab','-u','pchouinard','-l'])==(ROOT/'user-cron.held').read_text()
    assert not pathlib.Path('/etc/cron.d/community-brain-lint').exists()
    assert legacy.live()['effective_url']=='https://community-brain.patchoutech.lab/retrieval/query'
command=sys.argv[1];assert sys.argv[2:] in [[],['--now']] and (not sys.argv[2:] or command=='rollback')
result=Controller(ROOT,legacy,verify_live).execute(command,force='--now' in sys.argv)
print(json.dumps(result))

"""Candidate boot check never reconciles a boot or clears a hold."""
from pathlib import Path
import json
from runtime_contract import load

def inspect(expected):
 value=load(expected)
 recorded=json.loads((Path(value['holds_root'])/'automation/boot-state.json').read_text())
 boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
 return {'boot_matches':recorded.get('boot_id')==boot,'reconciled':recorded.get('reconciled',False),
         'launcher':value['boot_launcher'],'launch_enabled':False,'holds_modified':False}

"""Verify immutable content before any candidate host operation."""
import json,hashlib,socket
from pathlib import Path
from profiles import validate,development
from successor import verify
PACKET=Path(__file__).resolve().parent

def load(expected):
    verify(PACKET,expected)
    value=json.loads((PACKET/'descriptor.json').read_text());development(value)
    if socket.gethostname()!=value['hostname']:raise ValueError('host/profile mismatch')
    for name,item in value['helper_files'].items():
        raw=(PACKET/name).read_bytes()
        assert len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256']
    return value

def held(value):
    root=Path(value['root'])/'automation'
    boot=json.loads((root/'boot-state.json').read_text())
    return (root/'paused').exists() or (root/'attention.json').exists() or not boot.get('reconciled',False) or boot.get('boot_id')!=Path('/proc/sys/kernel/random/boot_id').read_text().strip()

def controls(value):
    return {**value,'processing_held':held(value),'packet_files':sorted(json.loads((PACKET/'packet-manifest.json').read_text()))}

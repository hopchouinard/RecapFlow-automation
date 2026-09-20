"""Descriptor-based successor host entry; old r020 is never imported or altered."""
from pathlib import Path
import json
import sys
import shlex
import os
from successor import API_IMAGE,DEV_ROOT
HERE=Path(__file__).resolve().parent
IMAGE=API_IMAGE

def read_env(name):
    load(os.environ['CBM_PACKET_SHA256'])
    if name not in {"api.env","worker.env","acquisition.env","bounded-model.env"}:raise ValueError("unknown development environment")
    p=Path(DEV_ROOT)/"private"/name
    assert p.stat().st_mode&0o777==0o600 and not p.is_symlink()
    return dict(x.split("=",1) for x in shlex.split(p.read_text()))

from runtime_contract import load,controls
from host import accept

def main(expected,operation,payload):
 value=load(expected)
 if operation=='api-up':return accept(payload)
 if operation=='controls':return controls(value)
 if operation=='tick':
  from automatic_host import tick
  return tick(expected)
 raise ValueError('Request027 authorizes API management and held ticks only')
if __name__=='__main__':
 print(json.dumps(main(sys.argv[1],sys.argv[2],json.load(sys.stdin))))

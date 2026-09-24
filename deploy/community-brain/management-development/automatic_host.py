"""Successor development tick: ordered runner lock, holds stay terminal.

Request027 validates management while processing remains held. A future reviewed
processing launcher is required; removing holds never enables this candidate.
"""
import fcntl
import json
from pathlib import Path
from runtime_contract import load,held

def tick(expected):
 value=load(expected)
 with (Path(value['holds_root'])/'automation/runner.lock').open('a') as lock:
  try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:return {'state':'quiet_lease_busy'}
  return {'state':'held' if held(value) else 'processing_not_authorized'}
if __name__=='__main__':
 import sys
 print(json.dumps(tick(sys.argv[1])))

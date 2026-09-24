"""Verified launcher dispatch. The management quiet lease can exclude this tick."""
import json,os,subprocess
from pathlib import Path
from runtime_contract import load

def tick(expected):
 value=load(expected)
 result=subprocess.run(['python3','-B',str(Path(__file__).parent/'workers/automatic_host.py')],env={**os.environ,'CBM_PACKET_SHA256':expected,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True,timeout=600)
 if result.returncode:raise RuntimeError('automatic tick requires reconciliation')
 return json.loads(result.stdout) if result.stdout.strip() else {'excluded_by_runner_lock':True}

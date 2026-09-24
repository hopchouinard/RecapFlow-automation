"""The indexing helper and API use the same sealed image and helper inventory."""
from runtime_contract import load
from pathlib import Path

def plan(expected):
    value=load(expected)
    return {'image':value['worker_image'],
            'host':str(Path(__file__).resolve().parent/'workers/manual_host.py'),
            'audit_helper':str(Path(__file__).resolve().parent/'workers/indexing_budget.py'),
            'execute_allowed':False}

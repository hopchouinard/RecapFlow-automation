"""Read-only retirement evidence for the exact existing Request029 fixture."""
import json
from pathlib import Path
import common as c
r=c.r
ROOT=Path('/srv/dev-data/workspaces/cbm-activation-integration-20260921-029')

def observe():
    operation=ROOT/'activation-operations/normal-terminal-refusal'
    result=json.loads(r.stable_bytes(operation/'result.json'))
    request=json.loads(r.stable_bytes(operation/'request.json'))
    if result['request']!=request or result['state']!='reconciliation_required':raise ValueError('legacy operation changed')
    journal=r.no_links(request['journal']);plan=r.no_links(request['plan'])
    if not journal.is_relative_to(ROOT) or not plan.is_relative_to(ROOT):raise ValueError('foreign legacy reference')
    j=json.loads(r.stable_bytes(journal));p=json.loads(r.stable_bytes(plan))
    if j['phase']!='rolled_back' or j['plan_sha256']!=request['sha256'] or r.sha(r.stable_bytes(plan))!=request['sha256']:raise ValueError('legacy rollback unverified')
    rows={}
    names=[p['incumbent']['container'],*[x['container'] for x in p['candidates']]]
    for name in names:
        if not name.startswith('cbm-r029-'):raise ValueError('nonfixture legacy container')
        row=c.inspect(name)
        if row['State']['Running']:raise ValueError('legacy fixture not retired')
        rows[name]={'id':row['Id'],'fingerprint':c.fingerprint(row),'running':False}
    if rows[p['incumbent']['container']]['id']!=p['incumbent']['id']:raise ValueError('legacy incumbent replaced')
    return {'target':'community-brain-dev','machine_id':c.machine_id(),'phase':'rolled_back','disposition':'retired_synthetic_fixture_no_replay',
            'files':{str(x):r.sha(r.stable_bytes(x)) for x in (operation/'request.json',operation/'result.json',journal,plan)},'containers':rows,'holds':r.hold_state(p['holds'])}

if __name__=='__main__':print(json.dumps(observe()))

"""Read-only VM108 persisted signup and session verification."""
import json
from pathlib import Path
import socket
import sys
ROOT=Path('/srv/dev-data/workspaces/cbm-stage2-webui-20260923-034')
if socket.gethostname()!='community-brain-dev' or not ROOT.joinpath('restore.json').exists():raise ValueError('development restore required')
sys.path.insert(0,str(ROOT/'source'))
import run
m=run.lib();m.ready()
state=json.loads((ROOT/'private/credentials.json').read_text());token=m.login(state)
config=m.api('GET','/api/v1/auths/admin/config',token=token)
if config['ENABLE_SIGNUP'] is not False:raise ValueError('signup remains enabled')
status,_=m.call('POST','/api/v1/auths/signup',{'name':'Denied','email':'denied-stage2@example.invalid','password':'synthetic-denied'},base=m.BASE)
if status not in (400,401,403):raise ValueError('signup unexpectedly accepted')
print(json.dumps({'signup_disabled_persisted':True,'unauthorized_signup_status':status,'existing_login':True,'production_change':False}))

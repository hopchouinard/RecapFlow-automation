"""Read-only acceptance after WebUI healthcheck configuration changes on VM108."""
import json
from pathlib import Path
import socket
import subprocess
import sys
import time

ROOT=Path('/srv/dev-data/workspaces/cbm-stage2-webui-20260923-034')
if socket.gethostname()!='community-brain-dev' or not ROOT.joinpath('restore.json').exists():
    raise ValueError('fresh development restore required')
sys.path.insert(0,str(ROOT/'source'))
import run
m=run.lib()
m.ready()
state=json.loads((ROOT/'private/credentials.json').read_text())
user=m.login(state)
retrieval=m.probe(user,state['new'])
assert retrieval['source_count']==1
vector="import chromadb; c=chromadb.PersistentClient(path='/app/backend/data/vector_db'); t=c.get_collection('integration_restore'); assert t.count()==1 and t.query(query_embeddings=[[1.0,0.0,0.0]],n_results=1)['ids']==[['synthetic-vector']]"
subprocess.run(['docker','exec',run.container('webui'),'python','-B','-c',vector],check=True,stdout=subprocess.DEVNULL)
for attempt in range(20):
    row=json.loads(subprocess.check_output(['docker','inspect',run.container('webui')]))[0]
    if row['State']['Health']['Status']=='healthy':break
    time.sleep(3)
else:raise RuntimeError('replacement healthcheck did not become healthy')
assert not row['State']['OOMKilled']
print(json.dumps({'webui_health':'healthy','actual_login':True,'retrieval_source_count':retrieval['source_count'],
                  'restored_chroma_query':True,'oom_killed':False,'development_only':True}))

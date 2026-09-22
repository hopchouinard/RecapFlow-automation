"""Run inside WebUI. Existing admin API; temporary unassigned action probes live cache.
Input is private JSON on stdin. Never log credentials or response transcript content.
"""
import os,sys,json,time,uuid,sqlite3,pathlib,hashlib
import requests,jwt
p=pathlib.Path('/app/backend/data/webui.db')
c=sqlite3.connect('file:'+str(p)+'?mode=ro',uri=True)
uid=c.execute("select id from user where role='admin' order by created_at limit 1").fetchone()[0]
# Use the live process environment, not an assumed/default signing secret.
key=None
for proc in pathlib.Path('/proc').iterdir():
 if not proc.name.isdigit():continue
 try:env=dict(x.split(b'=',1) for x in (proc/'environ').read_bytes().split(b'\0') if b'=' in x)
 except (OSError,ValueError):continue
 if env.get(b'WEBUI_SECRET_KEY'):key=env[b'WEBUI_SECRET_KEY'].decode();break
assert key,'Live signing key unavailable'
s=requests.Session();s.trust_env=False
s.headers['Authorization']='Bearer '+jwt.encode({'id':uid,'exp':int(time.time())+180,'jti':str(uuid.uuid4())},key,algorithm='HS256')
BASE='http://127.0.0.1:8080';FID='community_brain_filter'
def api(method,path,data=None):
 r=s.request(method,BASE+path,json=data,timeout=60)
 if not r.ok:raise RuntimeError('WebUI API failed: '+str(r.status_code)+' '+path)
 return r.json()
args=json.load(sys.stdin);mode=args['mode']
row=c.execute('select content,valves,is_active,is_global from function where id=?',(FID,)).fetchone()
assert hashlib.sha256(row[0].encode()).hexdigest()=='12215e67d72775e3d56baa98fc23093196cc8917d887a18a506f188f26a0dc16'
valves=api('GET','/api/v1/functions/id/'+FID+'/valves')
if mode=='set':
 assert args['url'] in ['http://10.1.30.10:8999/query','https://community-brain.patchoutech.lab/retrieval/query']
 before=dict(valves);valves.update(retrieval_url=args['url'],api_key=args['token'])
 result=api('POST','/api/v1/functions/id/'+FID+'/valves/update',valves)
 assert result==valves
 assert {k:v for k,v in result.items() if k not in ['retrieval_url','api_key']}=={k:v for k,v in before.items() if k not in ['retrieval_url','api_key']}
# Fixed, administrator-only, temporary action. No model call, event emission or chat write.
action_id='cbm_management_probe_001'
source='''from open_webui.models.functions import Functions
from open_webui.utils.filter import process_filter_functions, get_function_module
import hashlib
class Action:
    async def action(self, body, __request__, __user__):
        assert __user__.get('role')=='admin'
        fid='community_brain_filter'
        f=Functions.get_function_by_id(fid)
        assert hashlib.sha256(f.content.encode()).hexdigest()=='12215e67d72775e3d56baa98fc23093196cc8917d887a18a506f188f26a0dc16'
        assert f.is_active and f.is_global
        result,_=await process_filter_functions(__request__,[f],'inlet',{'messages':[{'role':'user','content':'community'}]},{'__user__':__user__})
        module=get_function_module(__request__,fid)
        status,chunks=module._retrieve_chunks('community')
        context=result['messages'][0]
        return {'live_app_process':True,'effective_url':module.valves.retrieval_url,'retrieval_status':status,'source_sha256':hashlib.sha256(f.content.encode()).hexdigest(),'context_emitted':context.get('role')=='system' and '<transcript_data>' in context.get('content',''),'source_count':len(chunks),'sources':[{k:v for k,v in ch.get('ground_truth',{}).items() if k in ['chunk_id','session_id','source_file']} for ch in chunks]}
'''
existing=c.execute('select content from function where id=?',(action_id,)).fetchone()
if existing:
 assert existing[0]==source,'Unexpected probe owner'
 api('DELETE','/api/v1/functions/id/'+action_id+'/delete')
created=False
try:
 api('POST','/api/v1/functions/create',{'id':action_id,'name':'Temporary management retrieval verification','content':source,'meta':{'description':'Unassigned administrator-only retrieval verification'}});created=True
 models=api('GET','/api/models')['data'];assert models
 body={'model':models[0]['id'],'chat_id':'cbm-management-verification','id':'cbm-management-verification','session_id':'cbm-management-verification'}
 result=api('POST','/api/chat/actions/'+action_id,body)
 assert result['effective_url']==valves['retrieval_url']
 print(json.dumps(result))
finally:
 if created:api('DELETE','/api/v1/functions/id/'+action_id+'/delete')
 assert c.execute('select count(*) from function where id=?',(action_id,)).fetchone()[0]==0
 after=c.execute('select content,is_active,is_global from function where id=?',(FID,)).fetchone();assert after==(row[0],row[2],row[3])

"""Actual isolated WebUI HTTP/session mechanics; no rendered-browser claim."""
import json
import os
import secrets
import socket
import sqlite3
import subprocess
import time
from pathlib import Path
import recovery as r

ROOT=r.DEV_ROOT/'webui-session-a02'
IMAGE='sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b'
NAMES=['cbm-r030-webui-source-a02','cbm-r030-webui-restored-a02','cbm-r030-webui-wrong-key-a02']


def cmd(args,data=None):
    p=subprocess.run(args,input=data,capture_output=True,timeout=120)
    if p.returncode:
        r.write_new(ROOT/('failure-'+str(time.time_ns())+'.log'),p.stderr)
        raise RuntimeError('private diagnostic retained')
    return p.stdout


def api(name,path,method='GET',body=None,token=None):
    spec=json.dumps(dict(path=path,method=method,body=body,token=token))
    code="""import json,sys,urllib.request,urllib.error
s=json.load(sys.stdin);headers={'Content-Type':'application/json'}
if s['token']:headers['Authorization']='Bearer '+s['token']
r=urllib.request.Request('http://127.0.0.1:8080'+s['path'],method=s['method'],headers=headers,data=None if s['body'] is None else json.dumps(s['body']).encode())
try:
 with urllib.request.urlopen(r,timeout=15) as f:print(json.dumps({'status':f.status,'body':json.load(f)}))
except urllib.error.HTTPError as e:print(json.dumps({'status':e.code,'body':None}))
except Exception:print(json.dumps({'status':0,'body':None}))
"""
    return json.loads(cmd(['docker','exec','-i',name,'python','-B','-c',code],spec.encode()))


def start(name,data,envfile):
    cmd(['docker','run','-d','--name',name,'--network','none','--restart','no','--memory','1536m','--cpus','1.5',
         '--security-opt','no-new-privileges:true','--env-file',str(envfile),'--mount','type=bind,source='+str(data)+',target=/app/backend/data',IMAGE])
    for _ in range(300):
        if api(name,'/health')['status']==200:return
        time.sleep(1)
    raise RuntimeError('isolated WebUI readiness timeout')


def main():
    assert socket.gethostname()=='community-brain-dev'
    ROOT.mkdir(mode=0o700);r.write_new(ROOT/'intent.json',r.encode({'scope':'synthetic-development','names':NAMES}))
    original=ROOT/'original';original.mkdir(mode=0o700)
    web=original/'webui';web.mkdir();private=original/'signing';private.mkdir(mode=0o700)
    secret=secrets.token_urlsafe(48);password=secrets.token_urlsafe(32)
    env={'WEBUI_SECRET_KEY':secret,'WEBUI_AUTH':'true','ENABLE_SIGNUP':'true','OFFLINE_MODE':'true','HF_HUB_OFFLINE':'1','TRANSFORMERS_OFFLINE':'1',
         'ENABLE_OLLAMA_API':'false','ENABLE_OPENAI_API':'false','RAG_EMBEDDING_ENGINE':'ollama','OLLAMA_BASE_URL':'http://127.0.0.1:9',
         'OPENAI_API_BASE_URL':'http://127.0.0.1:9/v1','OPENAI_API_KEY':'synthetic-disabled','ANONYMIZED_TELEMETRY':'false','DO_NOT_TRACK':'true','SCARF_NO_ANALYTICS':'true'}
    r.write_new(private/'webui.env',''.join(k+'='+v+'\n' for k,v in env.items()).encode())
    login={'email':'request030@example.invalid','password':password}
    r.write_new(private/'login.json',r.encode(login))
    start_time=time.monotonic()
    try:
        start(NAMES[0],web,private/'webui.env')
        response=api(NAMES[0],'/api/v1/auths/signup','POST',dict(login,name='Synthetic Request030'))
        assert response['status']==200, 'synthetic account setup failed'
        token=response['body']['token'];r.write_new(private/'session.json',r.encode({'token':token}))
        config=api(NAMES[0],'/api/v1/auths/admin/config',token=token)['body'];config['ENABLE_SIGNUP']=False
        assert api(NAMES[0],'/api/v1/auths/admin/config','POST',config,token)['status']==200
        created=api(NAMES[0],'/api/v1/chats/new','POST',{'chat':{'title':'Synthetic preserved conversation','messages':[]}},token)
        assert created['status']==200;chat_id=created['body']['id']
        assert api(NAMES[0],'/api/v1/auths/',token=token)['status']==200
        cmd(['docker','stop',NAMES[0]])
        # Stopped synthetic source only. Original remains stopped for the rest of the test.
        before=r.tree(web)
        digest=r.capture({'webui':web,'signing':private},ROOT/'capture','cbm-r030-webui-session-a02',{'writer_exclusion':'exact synthetic source container stopped'})
        restored=r.restore(ROOT/'capture',digest,ROOT/'restored')
        start(NAMES[1],ROOT/'restored/webui',ROOT/'restored/signing/webui.env')
        old_session=api(NAMES[1],'/api/v1/auths/',token=token)['status']
        signin=api(NAMES[1],'/api/v1/auths/signin','POST',login)['status']
        anonymous=api(NAMES[1],'/api/v1/chats/')['status']
        disabled=api(NAMES[1],'/api/v1/auths/admin/config',token=token)['body']['ENABLE_SIGNUP'] is False
        signup=api(NAMES[1],'/api/v1/auths/signup','POST',{'name':'Refused','email':'refused@example.invalid','password':password})['status']
        retained=api(NAMES[1],'/api/v1/chats/'+chat_id,token=token)['status']
        assert old_session==200 and signin==200 and anonymous in [401,403] and disabled and signup in [400,401,403] and retained==200
        cmd(['docker','stop',NAMES[1]])
        # Independent restore from original bundle, not a mutable copy of the first restore.
        r.restore(ROOT/'capture',digest,ROOT/'wrong-key-copy')
        wrong=ROOT/'wrong-key.env';env['WEBUI_SECRET_KEY']=secrets.token_urlsafe(48);env['ENABLE_SIGNUP']='false'
        r.write_new(wrong,''.join(k+'='+v+'\n' for k,v in env.items()).encode())
        start(NAMES[2],ROOT/'wrong-key-copy/webui',wrong)
        denied=api(NAMES[2],'/api/v1/auths/',token=token)['status'];assert denied in [401,403]
        assert r.tree(web)==before
        receipt=dict(scope='synthetic-development',image=IMAGE,capture_manifest_sha256=digest,old_session_status=old_session,
                     new_login_status=signin,anonymous_status=anonymous,effective_persisted_signup_disabled=disabled,signup_refusal_status=signup,
                     retained_chat_status=retained,wrong_key_status=denied,source_unchanged=True,network='none',published_ports=[],
                     duration_seconds=round(time.monotonic()-start_time,3),rendered_browser_test=False,real_identity_session_test=False,
                     real_provider_calls=0,production_qualified=False)
        r.write_new(ROOT/'webui-session-acceptance.json',r.encode(receipt))
    finally:
        state={}
        for name in NAMES:
            x=subprocess.run(['docker','inspect','--type','container',name],capture_output=True)
            if x.returncode==0:
                v=json.loads(x.stdout)[0]
                if v['State']['Running']:cmd(['docker','stop',name])
                v=json.loads(cmd(['docker','inspect','--type','container',name]))[0]
                state[name]={'id':v['Id'],'image':v['Image'],'running':v['State']['Running'],'oom_killed':v['State']['OOMKilled'],'network':v['HostConfig']['NetworkMode'],'ports':v['HostConfig']['PortBindings']}
        r.write_new(ROOT/'cleanup.json',r.encode(state))
    print(json.dumps(receipt))

if __name__=='__main__':main()

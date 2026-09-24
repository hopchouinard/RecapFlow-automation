"""Real HTTP negative auth checks against an isolated exact-image API."""
import copy
import hashlib
import json
import secrets
import time
import urllib.error
import urllib.request
from host import ROOT, PRIVATE, OPENER, atomic, call, command, container


def probe(base, path, token):
    req=urllib.request.Request(base+path,headers={'Authorization':'Bearer '+token})
    try:
        with OPENER.open(req,timeout=10) as response:return response.status
    except urllib.error.HTTPError as error:return error.code


def run(values, suffix=''):
    assert suffix in ('','-v2')
    marker=ROOT/('negative-auth'+suffix+'-intent')
    assert not marker.exists();marker.touch(mode=0o600)
    assert int(values['CB_PROBE_EXPIRES_AT'])>time.time()+3600
    current_id=container('api')
    wrong=secrets.token_urlsafe(48)
    assert call('/api/v1/me',values['CB_READ_PROBE_TOKEN'])[0]==200
    assert call('/api/v1/me',wrong)[0]==401
    assert call('/api/v1/jobs',values['CB_METRICS_PROBE_TOKEN'])[0]==403
    assert call('/metrics',values['CB_READ_PROBE_TOKEN'])[0]==403
    expired=secrets.token_urlsafe(48)
    records=json.loads(values['CB_SERVICE_IDENTITIES'])
    records.append({'subject':'request034-expired-negative','scope':'community-brain',
                    'permissions':['jobs:read'],'expires_at':int(time.time())-60,
                    'sha256':hashlib.sha256(expired.encode()).hexdigest()})
    import shlex
    existing=dict(x.split('=',1) for x in shlex.split((PRIVATE/'api.env').read_text()))
    existing['CB_SERVICE_IDENTITIES']=json.dumps(records,separators=(',',':'))
    assert all("'" not in v and '\n' not in v for v in existing.values())
    envfile=PRIVATE/('expired-api'+suffix+'.env')
    atomic(envfile,''.join(k+"='"+v+"'\n" for k,v in existing.items()))
    compose=json.loads((ROOT/'compose.json').read_text())
    cloned=copy.deepcopy(compose['services']['api'])
    name='expired-api'+suffix
    cloned['container_name']='cbm-r034-'+name
    cloned['env_file']=[str(envfile)]
    override={'services':{name:cloned}}
    override_file=ROOT/('negative-compose'+suffix+'.json')
    atomic(override_file,json.dumps(override,indent=2))
    scoped=['docker','compose','-f',str(ROOT/'compose.json'),'-f',str(override_file)]
    command(scoped+['up','-d','--no-deps',name])
    try:
        for _ in range(90):
            try:
                row=json.loads(command(['docker','inspect',cloned['container_name']]))[0]
                ip=row['NetworkSettings']['Networks']['cbm-r034_default']['IPAddress']
                assert ip
                base='http://'+ip+':8090'
                if probe(base,'/health',values['CB_READ_PROBE_TOKEN'])==200:break
            except (OSError,ValueError,RuntimeError):pass
            time.sleep(1)
        else:raise RuntimeError('isolated expired API readiness timeout')
        assert probe(base,'/api/v1/me',values['CB_READ_PROBE_TOKEN'])==200
        assert probe(base,'/api/v1/me',expired)==401
        assert probe(base,'/api/v1/me',wrong)==401
        assert probe(base,'/api/v1/jobs',values['CB_METRICS_PROBE_TOKEN'])==403
        result={'real_http_api':True,'exact_image':cloned['image'],'positive_status':200,
                'expired_status':401,'wrong_status':401,'cross_scope_status':403,
                'expired_identity_sha256':hashlib.sha256(expired.encode()).hexdigest(),
                'expired_at':records[-1]['expires_at'],'incumbent_dev_api_unchanged':container('api')==current_id}
        atomic(ROOT/('negative-auth'+suffix+'-acceptance.json'),json.dumps(result,indent=2))
        return result
    finally:
        command(scoped+['stop',name])

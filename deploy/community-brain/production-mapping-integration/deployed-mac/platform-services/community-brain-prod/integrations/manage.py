import os,json,ssl,urllib.request,urllib.error
from pathlib import Path
CTX=ssl.create_default_context(cafile='/etc/ssl/cert.pem')
CTX.load_verify_locations(str(Path(__file__).resolve().parents[2]/'forge-inspection/lab-root-ca.crt'))
PROJECT=os.environ['INFISICAL_PROJECT_ID']
def api(system,path,method='GET',body=None):
 base,token=(os.environ['CBM_AUTH_URL'],os.environ['CBM_AUTH_TOKEN']) if system=='auth' else (os.environ['INFISICAL_API_URL'],os.environ['INFISICAL_TOKEN'])
 req=urllib.request.Request(base.rstrip('/')+'/'+path.lstrip('/'),data=None if body is None else json.dumps(body).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json','Accept':'application/json'},method=method)
 try:
  with urllib.request.urlopen(req,context=CTX,timeout=30) as r:return json.load(r)
 except urllib.error.HTTPError as e:
  raise RuntimeError(f'{system} {method} {path} HTTP {e.code}') from None

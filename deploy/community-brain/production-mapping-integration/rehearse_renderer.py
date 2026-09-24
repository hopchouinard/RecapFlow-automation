import hashlib,json,os,subprocess,sys,time
from pathlib import Path
from helper_contracts import Cycle,verify_sources,write_new,sha
from candidate.manual_runtime import recreate
import service_recovery as services
from rehearse_helpers import module,synthetic_authority,INTEGRATIONS

def run(label):
 root=services.ROOT/('renderer-'+label);root.mkdir(mode=0o700);packet=root/'runtime';packet.mkdir();(packet/'run.py').write_text('print("synthetic immutable runtime")\n');write_new(packet/'runtime-manifest.json',{'run.py':sha((packet/'run.py').read_bytes())})
 policy=module(INTEGRATIONS/'service_renewal_policy.py','policy');values=synthetic_authority(policy);values.update(CB_RUNTIME_DATABASE_URL='postgresql://synthetic.invalid/synthetic',CB_OIDC_ISSUER='https://synthetic.invalid',CB_OIDC_AUDIENCE='synthetic',CB_OIDC_CLIENT_ID='synthetic',CB_OIDC_JWKS_URL='https://synthetic.invalid/jwks')
 env={'CB_DATABASE_URL':values['CB_RUNTIME_DATABASE_URL'],'CB_SERVICE_IDENTITIES':values['CB_SERVICE_IDENTITIES']};env.update({k:values[k] for k in ('CB_OIDC_ISSUER','CB_OIDC_AUDIENCE','CB_OIDC_CLIENT_ID','CB_OIDC_JWKS_URL')})
 args=['docker','run','-d','--name','cbm-r033-renderer-'+label,'--network','none','--restart','no','--memory','64m','--cpus','0.25','--read-only']
 for k,v in env.items():args+=['-e',k+'='+v]
 ident=subprocess.check_output(args+['python:3.11-slim','python','-B','-m','http.server','8080'],text=True).strip();row=services.inspect(ident)
 b={'packet':str(packet),'manifest_sha256':sha((packet/'runtime-manifest.json').read_bytes()),'incumbent_id':ident,'incumbent_image':row['Image'],'incumbent_fingerprint':services.fingerprint(row),'current_environment':env,'generation':label,'deadline':time.time()+90,'rollback_owner':'home.servers','scope':'synthetic-development','executor_manifest_sha256':verify_sources(),'unit':'cbm-r033-render-'+label+'.service'};binding=root/'binding.json';write_new(binding,b)
 mutex=services.ROOT/'fixture-mutex'
 with Cycle(root/'journal',mutex,label+'-renderer','manual',verify_sources()) as cycle:
  holder={}
  def effect():holder.update(recreate(values,binding))
  cycle.helper('renew-service-tokens',effect,lambda:holder);cycle.finish()
 replacement=holder['replacement_id'];assert not services.inspect(ident)['State']['Running'];assert services.inspect(replacement)['State']['Running']
 # Explicit acceptance-test rollback, exact original container kept intact.
 subprocess.run(['docker','stop','--time','1',replacement],check=True,capture_output=True);subprocess.run(['docker','start',ident],check=True,capture_output=True);assert services.fingerprint(services.inspect(ident))==b['incumbent_fingerprint']
 receipt={'incumbent_id':ident,'replacement_id':replacement,'actual_docker_generation_and_environment_readback':True,'original_exact_container_restored':True,'original_configuration_equal':True,'original_and_replacement_retained':True,'production_invoked':False,'scope':'synthetic renderer; real production browser/session acceptance remains separate'};write_new(services.ROOT/(label+'-renderer-receipt.json'),receipt);print(json.dumps(receipt))
if __name__=='__main__':run(sys.argv[1])

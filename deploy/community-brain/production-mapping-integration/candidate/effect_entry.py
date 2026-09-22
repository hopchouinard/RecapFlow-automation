"""Only scoped development transport is selectable in this mapping phase."""
import os,sys,json
from pathlib import Path
from wrapper_guard import check
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from rehearse_helpers import Environment,renewal
if __name__=='__main__':
 name=sys.argv[1];check(name);root=Path(os.environ['CBM_DEVELOPMENT_ROOT'])/('effect-'+name.removesuffix('.py'));root.mkdir(mode=0o700)
 env=Environment(root)
 if name=='renew-service-tokens.py':value=renewal(env)
 else:value=env.execute(name.removesuffix('.py'))
 print(json.dumps({'helper':name,'scope':'synthetic-development','readback':env.readback()}))

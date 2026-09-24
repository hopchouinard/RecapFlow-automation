"""Render a new isolated VM108 fixture from the pinned WebUI integration source."""
from pathlib import Path
import hashlib,json,shutil,sys
BASE=Path(__file__).resolve().parents[1]
ORIGINAL=BASE/'openwebui-integration'
DEVELOPMENT=BASE/'openwebui-development'
WORKSPACE=Path('/srv/dev-data/workspaces/cbm-stage2-webui-20260923-034')
PROJECT='cbm-stage2-webui-034'
OLD_ROOT='/srv/dev-data/workspaces/cbm-openwebui-integration-20260920'
OLD_PROJECT='cbm-integration-dev'

def render(out):
    out=Path(out)
    if out.exists():raise FileExistsError('fixture source immutable')
    out.mkdir(mode=0o700)
    source=out/'source';source.mkdir(mode=0o755)
    manifest={}
    for base in (DEVELOPMENT,ORIGINAL):
        for file in sorted(base.glob('*.py')):
            data=file.read_bytes()
            if file.name in ('run.py','isolation.py','rehearse.py'):
                content=data.decode().replace(OLD_ROOT,str(WORKSPACE)).replace(OLD_PROJECT,PROJECT)
                # The imported WebUI helper has a different original workspace.
                content=content.replace('/srv/dev-data/workspaces/cbm-openwebui-migration-20260920',str(WORKSPACE))
                data=content.encode()
            target=source/file.name
            target.write_bytes(data);target.chmod(0o644)
            manifest[str(target.relative_to(out))]=hashlib.sha256(data).hexdigest()
    compose=(ORIGINAL/'compose.yml').read_text().replace(OLD_PROJECT,PROJECT).encode()
    (out/'compose.yml').write_bytes(compose)
    manifest['compose.yml']=hashlib.sha256(compose).hexdigest()
    (out/'source-manifest.json').write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n')
    return manifest

if __name__=='__main__':
    manifest=render(sys.argv[1]);print(json.dumps({'files':len(manifest),'workspace':str(WORKSPACE)}))

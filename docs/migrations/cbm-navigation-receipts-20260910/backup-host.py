import pathlib,tarfile,hashlib,json
root=pathlib.Path('/srv/community-brain');p=root/'artifacts/cbm-navigation-20260910/controls-and-static.tar.gz';assert not p.exists()
with tarfile.open(p,'w:gz') as t:
 for name in ['workspaces/cbm-navigation-20260910','workspaces/manual-20260910/compose.production-manual.yml','workspaces/manual-20260910/runtime-manifest.json','workspaces/manual-20260910/production-staging/manual_host.py','artifacts/cbm-navigation-20260910/before','artifacts/cbm-navigation-20260910/old-dist','artifacts/cbm-navigation-20260910/api-inspect.private.json','artifacts/cbm-navigation-20260910/api.env.before','artifacts/cbm-navigation-20260910/data-manifest-before.json','artifacts/cbm-navigation-20260910/preparation.json']:t.add(root/name,arcname=name)
p.chmod(0o600);print(json.dumps({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}))

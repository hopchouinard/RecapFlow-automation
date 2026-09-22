import pathlib,shutil,subprocess,json,hashlib
root=pathlib.Path('/srv/dev-data/workspaces/cbm-production-mapping-20260922-033');source=root/'packet-v7';tests=root/'source-negatives-v7';tests.mkdir(mode=0o700)
results=[]
for n in ['candidate/manual_runtime.py','candidate/service_renewal_live.py','helper_contracts.py','capture_adapter.py','service_recovery.py','private_contract.py','deployed-mac/maintain.py','deployed-remote/vm109/usr/local/lib/community-brain-automatic/boot_guard.py','extra-member.py','__pycache__/injected.cpython-311.pyc']:
 dest=tests/str(len(results));shutil.copytree(source,dest)
 p=dest/n
 if not p.exists() and n.startswith('deployed-remote/'):
  p=next((dest/'deployed-remote').rglob('*.py'));n=str(p.relative_to(dest))
 p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():p.chmod(0o600);p.write_bytes(p.read_bytes()+b'\n# changed source rejection\n')
 else:p.write_bytes(b'unknown member')
 r=subprocess.run(['python3','-B',str(dest/'verify_mapping.py')],capture_output=True)
 assert r.returncode!=0,n
 results.append({'changed_member':n,'actual_subprocess_exit':r.returncode,'refused':True})
print(json.dumps({'source_manifest_sha256':hashlib.sha256((source/'packet-manifest.json').read_bytes()).hexdigest(),'actual_changed_byte_cases':results,'count':len(results),'effect_invoked':False}))

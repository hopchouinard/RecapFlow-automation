"""Build an immutable local packet. Does not install or execute anything remotely."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
from successor import descriptor,seal,verify,DEV_ROOT
sys.path.insert(0,str(Path(__file__).parent/'incumbent'))
from service_renewal_policy import SPECS

NAMES=['authority.py','successor.py','host.py','consumers.py','kuma.js','test_boundaries.py',
 'runtime_contract.py','run.py','automatic_host.py','boot_guard.py','indexing.py','manager.py',
 'incumbent-manifest.json','worker-helper-provenance.json']

def build(output,revision,image_files,monitor_images):
 if not re.fullmatch(r'packet-v[1-9][0-9]*',revision):raise ValueError('invalid packet revision')
 output=Path(output);output.mkdir(mode=0o700)
 source=Path(__file__).resolve().parent
 for name in NAMES:shutil.copyfile(source/name,output/name)
 for name in ['incumbent','fixture','workers']:shutil.copytree(source/name,output/name)
 value=descriptor(image_files,{})
 value.update(postgres_image='sha256:4ef4dbc939d61acea57712655ddb4b4ab27419c913f94cca0cd57cb3ea3c2280',monitor_images={k:v['development_image'] for k,v in monitor_images.items()})
 value.update(worker_image=value['api_image'],boot_launcher=DEV_ROOT+'/'+revision+'/automatic_host.py',recovery_images=sorted(set([value['api_image'],value['webui_image'],value['postgres_image'],*value['monitor_images'].values()])))
 value['helper_files']={str(p.relative_to(output)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in output.rglob('*') if p.is_file()}
 (output/'descriptor.json').write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')
 (output/'identity-specs.json').write_text(json.dumps(SPECS,sort_keys=True,indent=2)+'\n')
 identity=seal(output);verify(output,identity)
 return identity

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('output');parser.add_argument('revision');parser.add_argument('image_files');parser.add_argument('monitor_images');args=parser.parse_args()
 print(build(args.output,args.revision,json.loads(Path(args.image_files).read_text()),json.loads(Path(args.monitor_images).read_text())))

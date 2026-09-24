import copy,hashlib,json,os,shutil,tempfile,unittest,sys,subprocess
from pathlib import Path
import private_contract as p
class Private(unittest.TestCase):
 def test_exact_membership_signing_metadata_and_links(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d).resolve();components={}
   for n in p.COMPONENTS:
    q=root/n;q.mkdir();components[n]=q
   key=components['webui-signing']/'webui_secret_key';key.write_bytes(b'SYNTHETIC ORIGINAL SIGNING');h=hashlib.sha256(key.read_bytes()).hexdigest()
   (components['webui-volume']/'empty').mkdir();(components['webui-volume']/'blob').write_bytes(b'synthetic');(components['webui-volume']/'link').symlink_to('blob')
   # Explicit synthetic fixture normalization only; production rejection unchanged.
   if sys.platform=='darwin':
    from unittest.mock import patch
    original=p.recovery.extended_names
    adaptation=patch.object(p.recovery,'extended_names',side_effect=lambda path:[] if Path(path).is_relative_to(root) else original(path));adaptation.start();self.addCleanup(adaptation.stop)
   before=p.inspect_components(components,h);self.assertTrue(p.verify_restore(before,copy.deepcopy(before))['offline_only'])
   with self.assertRaises(ValueError):p.inspect_components({k:v for k,v in components.items() if k!='config'},h)
   key.write_bytes(b'changed')
   with self.assertRaises(ValueError):p.inspect_components(components,h)
   key.write_bytes(b'SYNTHETIC ORIGINAL SIGNING');(components['webui-volume']/'escape').symlink_to('/etc/passwd')
   with self.assertRaises(ValueError):p.inspect_components(components,h)
 def test_actual_extended_metadata_remains_refused(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d).resolve();f=root/'native';f.write_bytes(b'synthetic')
   if sys.platform=='darwin':subprocess.run(['/usr/bin/xattr','-w','user.request033','synthetic',str(f)],check=True)
   else:os.setxattr(f,'user.request033',b'synthetic')
   with self.assertRaises(ValueError):p.recovery.tree(root)
 def test_changed_metadata_and_destination_refused(self):
  with self.assertRaises(ValueError):p.verify_restore({'mode':384},{'mode':420})
  b={'machine_id':'m','mount_uuid':'u','parent':'/private','child':'/private/attempt','owner_uid':0,'mode':448,'minimum_free_bytes':1024,'retention':'until explicit disposition','network':'none','production_transfer_authorized':False}
  o={'machine_id':'m','mount_uuid':'u','parent':'/private','available_bytes':2048,'child_exists':False};self.assertFalse(p.validate_destination(b,o)['transfer_authorized'])
  for key,value in [('machine_id','foreign'),('mount_uuid','foreign'),('available_bytes',1),('child_exists',True)]:
   with self.assertRaises(ValueError):p.validate_destination(b,{**o,key:value})
if __name__=='__main__':unittest.main()

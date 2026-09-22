import hashlib,json,tempfile,unittest
from pathlib import Path
from candidate.manual_runtime import render,validate_packet
class Renderer(unittest.TestCase):
 def test_exact_member_and_changed_byte_refusal(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/'run.py').write_text('pass\n');m={'run.py':hashlib.sha256((p/'run.py').read_bytes()).hexdigest()};(p/'runtime-manifest.json').write_text(json.dumps(m));h=hashlib.sha256((p/'runtime-manifest.json').read_bytes()).hexdigest();validate_packet(p,h)
   (p/'run.py').write_text('changed\n')
   with self.assertRaises(ValueError):validate_packet(p,h)
   (p/'run.py').write_text('pass\n');(p/'unlisted.pyc').write_bytes(b'retained bytecode')
   with self.assertRaises(ValueError):validate_packet(p,h)
   self.assertTrue((p/'unlisted.pyc').exists())
 def test_production_never_compiles(self):
  with self.assertRaises(ValueError):render({}, {'scope':'production'})
if __name__=='__main__':unittest.main()

import importlib.util,unittest,types,json
from pathlib import Path
from unittest.mock import patch
s=importlib.util.spec_from_file_location('adapter',Path(__file__).with_name('pbs_adapter.py'));a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
class CliOutput(unittest.TestCase):
 def test_vzdump_stream_followed_by_upid(self):
  upid='UPID:pve1:001E1CBC:0FED0E1D:6AA9D98C:vzdump:109:root@pam:'
  output=('INFO: Starting Backup of VM 109\nINFO: Backup job finished successfully\n'+json.dumps(upid)+'\n').encode()
  with patch.object(a.subprocess,'run',return_value=types.SimpleNamespace(returncode=0,stdout=output)):
   self.assertEqual(a.api('create','/nodes/pve1/vzdump'),upid)
 def test_no_task_identity_fails_closed(self):
  with patch.object(a.subprocess,'run',return_value=types.SimpleNamespace(returncode=0,stdout=b'INFO: Backup job finished successfully\n')):
   with self.assertRaises(ValueError):a.api('create','/nodes/pve1/vzdump')
 def test_nonzero_exit_fails_even_with_task_id(self):
  with patch.object(a.subprocess,'run',return_value=types.SimpleNamespace(returncode=1,stdout=b'"UPID:pve1:x"')):
   with self.assertRaises(RuntimeError):a.api('create','/nodes/pve1/vzdump')
 def test_get_remains_strict(self):
  with patch.object(a.subprocess,'run',return_value=types.SimpleNamespace(returncode=0,stdout=b'log\n{"status":"OK"}')):
   with self.assertRaises(ValueError):a.api('get','/nodes/pve1/tasks/x/status')
if __name__=='__main__':unittest.main()

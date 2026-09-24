"""Unit evidence only; these tests cannot certify live authority or consumers."""
import copy
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
import sys


class Boundaries(unittest.TestCase):
    def setUp(self):
        # These packets intentionally ship standalone modules with identical names.
        # Isolate their imports so a combined collector cannot reuse another packet.
        modules = patch.dict(sys.modules)
        modules.start()
        self.addCleanup(modules.stop)
        here = Path(__file__).resolve().parent
        local_names = {p.stem for folder in here.parent.glob('management-*')
                       for p in folder.glob('*.py')} | {'incumbent'}
        for name in list(sys.modules):
            if name.split('.')[0] in local_names and not name.startswith('test_'):
                del sys.modules[name]
        paths = patch.object(sys, 'path', [str(here), *sys.path])
        paths.start()
        self.addCleanup(paths.stop)
        global Authority, PROJECT, ENVIRONMENT, DEVELOPMENT_PATH
        global API_IMAGE, descriptor, render, seal, verify
        from authority import Authority, PROJECT, ENVIRONMENT, DEVELOPMENT_PATH
        from successor import API_IMAGE, descriptor, render, seal, verify

    def value(self):
        return descriptor({'image': API_IMAGE, 'files': {
            '/app/community-brain/jobs/api.py': {'bytes': 1, 'sha256': 'fixture'},
            '/app/web/dist/index.html': {'bytes': 1, 'sha256': 'fixture'}}}, {})

    def test_packet_bytes_ignore_filesystem_and_input_mapping_order(self):
        from build_packet import build
        image_files = {'image': API_IMAGE, 'files': self.value()['image_files']}
        monitors = {'kuma': {'development_image': 'sha256:fixture-kuma'},
                    'prometheus': {'development_image': 'sha256:fixture-prometheus'}}
        original = Path.rglob
        def reversed_walk(path, pattern):
            return iter(reversed(list(original(path, pattern))))
        with tempfile.TemporaryDirectory() as temp:
            first, second = Path(temp)/'first', Path(temp)/'second'
            expected = build(first, 'packet-v8', image_files, monitors)
            image_files['files'] = dict(reversed(list(image_files['files'].items())))
            with patch.object(Path, 'rglob', reversed_walk):
                actual = build(second, 'packet-v8', image_files,
                               dict(reversed(list(monitors.items()))))
            self.assertEqual(actual, expected)
            for path in first.rglob('*'):
                if path.is_file():
                    self.assertEqual(path.read_bytes(),
                                     (second/path.relative_to(first)).read_bytes())

    def test_only_explicitly_authorized_development_folder_accepted(self):
        Authority(PROJECT, ENVIRONMENT, DEVELOPMENT_PATH, None)
        for project, environment, path in [
            (PROJECT, ENVIRONMENT, '/applications/community-brain'),
            (PROJECT, ENVIRONMENT, '/development/community-brain-dev'),
            (PROJECT, 'development', DEVELOPMENT_PATH),
            ('69b4a69f-e8f9-4a2f-a1f2-9293ff668f44', ENVIRONMENT, DEVELOPMENT_PATH),
            ('11111111-1111-4111-8111-111111111111', ENVIRONMENT, DEVELOPMENT_PATH),
        ]:
            with self.assertRaises(ValueError):
                Authority(project, environment, path, None)

    def test_terminal_intake_never_fetches_old_host(self):
        from incumbent.mac_intake_policy import decide,REQUEST,ORIGINAL,RECEIPT
        local={'request_id':ORIGINAL,'phase':'superseded','ownership':{
            'request_id':REQUEST,'accepted_recovery_receipt_sha256':RECEIPT,'legacy_writers_disabled':True}}
        def forbidden(*args):raise AssertionError('terminal intake crossed old-host boundary')
        disabled=[]
        self.assertEqual(decide(local,forbidden,forbidden,lambda:disabled.append(True),forbidden),'superseded')
        self.assertEqual(disabled,[True])

    def test_no_old_module_or_ui_overlays(self):
        rendered = render(self.value())
        self.assertEqual(rendered['services']['api']['image'], API_IMAGE)
        self.assertEqual(len(rendered['services']['api']['volumes']), 6)
        self.assertEqual(rendered['services']['api']['mem_limit'],2147483648)
        self.assertNotIn('ports', rendered['services']['api'])
        self.assertTrue(rendered['networks']['default']['internal'])

    def test_old_host_or_image_or_signing_path_cannot_enter_renderer(self):
        for key, wrong in [('host', 'n8n-automation'), ('api_image', 'old'),
                           ('signing_environment', '/etc/production.env'),
                           ('execution_allowed', False)]:
            value = self.value();value[key] = wrong
            with self.assertRaises(ValueError):render(value)

    def test_provider_profiles_cannot_select_each_others_provider(self):
        from profiles import profile,provider_plan
        dev,prod=profile('development'),profile('production')
        for stage in ('acquisition','processing','indexing'):
            d,p=provider_plan(dev,stage),provider_plan(prod,stage)
            self.assertIn('/packet/fixture/synthetic_worker.py',d['command'])
            self.assertIn('/packet/workers/manual_worker.py',p['command'])
            self.assertEqual(d['key'],'CB_SYNTHETIC_PROVIDER_TOKEN')
            self.assertNotEqual(d['file'],p['file'])
            self.assertEqual(p['ollama_url'],'http://10.1.50.219:11434')
        altered=copy.deepcopy(dev);altered['provider']=prod['provider']
        with self.assertRaises(ValueError):provider_plan(altered,'processing')

    def test_production_profile_review_only(self):
        from profiles import profile,development
        prod=profile('production');dev=profile('development')
        self.assertEqual([m['read_only'] for m in prod['api_mounts']], [m['read_only'] for m in dev['api_mounts']])
        self.assertEqual(prod['api_memory'],dev['api_memory'])
        with self.assertRaises(ValueError):development(prod)
        self.assertEqual(render(prod)['networks']['default']['external'],True)

    def test_packet_acceptance_and_content_tampering(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp);(root/'run.py').write_text('pass\n')
            expected = seal(root);verify(root, expected)
            (root/'run.py').write_text('exit()\n')
            with self.assertRaises(ValueError):verify(root, expected)

    def test_unmanifested_bytecode_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp);(root/'run.py').write_text('pass\n');expected=seal(root)
            (root/'__pycache__').mkdir();(root/'__pycache__/run.pyc').write_bytes(b'bytecode')
            with self.assertRaises(ValueError):verify(root, expected)


if __name__ == '__main__':
    unittest.main()

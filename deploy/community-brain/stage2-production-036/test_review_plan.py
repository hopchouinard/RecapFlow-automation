import hashlib
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest

import review_plan as p


class ReviewPlanTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        member = b'bound source\n'
        out = io.BytesIO()
        with tarfile.open(fileobj=out, mode='w') as bundle:
            row = tarfile.TarInfo('source.py')
            row.size = len(member)
            bundle.addfile(row, io.BytesIO(member))
        archive = root / 'source.tar'
        archive.write_bytes(out.getvalue())
        manifest = root / 'members.json'
        manifest.write_bytes(p.canonical({'source.py': p.sha(member)}))
        self.source = dict(commit='a' * 40, archive_path=str(archive),
                           archive_sha256=p.sha(archive.read_bytes()),
                           member_manifest_path=str(manifest),
                           member_manifest_sha256=p.sha(manifest.read_bytes()))
        c = json.loads((p.MAPPING / 'production-contract.json').read_text())
        b = json.loads((p.MAPPING / 'production-runtime-bindings.json').read_text())
        self.observation = dict(schema='cbm.vm109-read-only/1', observed_at=1000,
            machine_id=c['machine_id'], state_mount=c['state_mount'],
            incumbent=dict(id=c['incumbent_id'], image=c['incumbent_image'],
                           running=True, restart_policy='unless-stopped',
                           config_fingerprint='b' * 64),
            controls={name: {k: v for k, v in value.items() if k != 'exists'}
                      for name, value in b['controls'].items()})

    def test_review_binds_exact_readback_but_refuses_execution(self):
        plan = p.compile_review(self.observation, self.source, now=1000)
        self.assertEqual(21, len(plan['production_evidence']))
        self.assertTrue(all(value is None for value in plan['production_evidence'].values()))
        self.assertEqual(3, len(plan['authorities']))
        self.assertTrue(all(value is None for value in plan['authorities'].values()))
        with self.assertRaisesRegex(ValueError, 'never executable'):
            p.require_executable(plan, now=1000)

    def test_stale_observation_refused(self):
        with self.assertRaisesRegex(ValueError, 'stale'):
            p.compile_review(self.observation, self.source, now=1301)

    def test_foreign_lock_identity_refused(self):
        self.observation['controls']['automation/runner.lock']['inode'] += 1
        with self.assertRaisesRegex(ValueError, 'control/lock drift'):
            p.compile_review(self.observation, self.source, now=1000)

    def test_archive_member_mutation_refused(self):
        Path(self.source['archive_path']).write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'source archive or member manifest drift'):
            p.compile_review(self.observation, self.source, now=1000)


if __name__ == '__main__':
    unittest.main()

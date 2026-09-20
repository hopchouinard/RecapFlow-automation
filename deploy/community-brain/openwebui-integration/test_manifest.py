"""Recovery manifest must preserve internal links without following escaping links."""
from pathlib import Path
import tempfile
import unittest
from run import tree


class ManifestTests(unittest.TestCase):
    def test_internal_link_is_preserved_as_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'blob').write_bytes(b'synthetic')
            (root/'snapshot').mkdir();(root/'snapshot/model').symlink_to('../blob')
            manifest=tree(root)
            self.assertEqual(manifest['snapshot/model'],{'type':'symlink','target':'../blob'})
            self.assertEqual(manifest['blob']['type'],'file')

    def test_escaping_link_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent=Path(tmp);root=parent/'volume';root.mkdir()
            (parent/'outside').write_bytes(b'outside')
            (root/'escape').symlink_to('../outside')
            with self.assertRaisesRegex(AssertionError,'escapes'):tree(root)

    def test_file_change_changes_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'data').write_bytes(b'before');before=tree(root)
            (root/'data').write_bytes(b'after')
            self.assertNotEqual(tree(root),before)


if __name__=='__main__':unittest.main()

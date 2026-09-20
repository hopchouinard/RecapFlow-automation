"""Initialize only the fresh approved weekly volumes, without external access."""

import os
import shutil
from pathlib import Path

config = Path("/state/config")
corpus = Path("/state/corpus")
marker = corpus / "approved-weekly-isolated"
expected = "7bce1799-dd0f-40fa-a444-a7797ff38b1b\n"
if list(config.iterdir()) or list(corpus.iterdir()):
    assert set(corpus.iterdir()) == {marker} and marker.read_text() == expected

    def contents(root):
        assert not any(p.is_symlink() for p in root.rglob("*"))
        return {
            str(p.relative_to(root)): p.read_bytes()
            for p in root.rglob("*")
            if p.is_file()
        }

    assert contents(config) == contents(Path("/original-config")), (
        "Modified config requires review"
    )
else:
    shutil.copytree("/original-config", config, dirs_exist_ok=True)
    marker.write_text(expected)
for root in (config, corpus):
    for p in [root, *root.rglob("*")]:
        assert not p.is_symlink()
        os.chown(p, 0, 0)
        p.chmod(0o700 if p.is_dir() else 0o600)
        os.chown(p, 10001, 10001)
print("Fresh weekly corpus and copied development config initialized")

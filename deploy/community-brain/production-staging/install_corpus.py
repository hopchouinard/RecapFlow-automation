"""Install only the approved immutable candidate and hashed config into empty roots."""

import hashlib
import json
import os
import tarfile
from pathlib import Path

ROOT = Path("/srv/community-brain")
INPUT = ROOT / "artifacts/cbm-staging-inputs"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with path.open("xb") as out:
        out.write(content)
    os.chmod(path, 0o600)


def main():
    os.umask(0o077)
    corpus, config = ROOT / "corpus", ROOT / "config"
    assert not list(corpus.iterdir()) and not list(config.iterdir())
    package = INPUT / "consumer-candidate-v1"
    assert (
        digest(package / "corpus-manifest.json")
        == "cc59522ba9fac2861f62e09599e82c6606edd4f2552824f7f5c66046d080361d"
    )
    assert (
        digest(package / "candidate-provenance.json")
        == "6eb1744080dbe3892f4d13730a89872f2ac6ee9fb1ffc7901c19bb737b620b42"
    )
    assert (
        digest(INPUT / "manifest.json")
        == "81ea69b8d6d650ac3c6285fe72cafa6a38973f037af2ee84be7bd96362c2acd8"
    )
    manifest = json.loads((package / "corpus-manifest.json").read_text())
    archive = package / ("corpus-" + manifest["corpus_version"] + ".tar.gz")
    assert (
        digest(archive)
        == manifest["archive_sha256"]
        == "5e4f37d6459d820f506fe0b5d6d4db42204dcab26a3bb89592dd8f81fb9707fb"
    )
    files = {}
    with tarfile.open(archive) as tar:
        for member in tar:
            assert (
                member.isfile()
                and member.name not in files
                and member.name in manifest["files"]
            )
            assert (corpus / member.name).resolve().is_relative_to(corpus)
            content = tar.extractfile(member).read()
            assert hashlib.sha256(content).hexdigest() == manifest["files"][member.name]
            files[member.name] = content
    assert set(files) == set(manifest["files"])
    source = json.loads((INPUT / "manifest.json").read_text())
    configs = {r["path"]: r for r in source["files"] if r["path"].startswith("config/")}
    actual = {
        str(p.relative_to(INPUT)) for p in (INPUT / "config").rglob("*") if p.is_file()
    }
    assert actual == set(configs)
    for name, row in configs.items():
        path = INPUT / name
        assert (
            not path.is_symlink()
            and digest(path) == row["sha256"]
            and path.stat().st_size == row["bytes"]
        )
    for name, content in files.items():
        write(corpus / name, content)
    for name in configs:
        write(ROOT / name, (INPUT / name).read_bytes())
    for directory in (corpus, config):
        for path in [directory, *directory.rglob("*")]:
            assert not path.is_symlink()
            os.chown(path, 10001, 10001)
            os.chmod(path, 0o700 if path.is_dir() else 0o600)
    receipt = {
        "corpus_files": len(files),
        "config_files": len(configs),
        "all_hashes_verified": True,
        "originals_preserved": True,
    }
    (INPUT / "installation-result.json").write_text(json.dumps(receipt) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()

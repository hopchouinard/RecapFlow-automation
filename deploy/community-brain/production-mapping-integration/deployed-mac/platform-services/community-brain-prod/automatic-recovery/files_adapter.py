"""Exact private archive capture/restore. No model, queue or application writes."""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
from uuid import UUID

IMAGE = "community-brain@sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449"
ROOT = Path("/srv/community-brain")
FOLDERS = [
    "srv/community-brain/files", "srv/community-brain/config", "srv/community-brain/corpus",
    "srv/community-brain/automation-public",
    "srv/community-brain/manual-approvals", "srv/community-brain/automation",
    "srv/community-brain/meeting-archive-20260910", "etc/community-brain-production",
    "srv/community-brain/workspaces/manual-20260910", "srv/community-brain/workspaces/manual-20260910-v2",
    "srv/community-brain/workspaces/cbm-archive-ui-20260910",
    "srv/community-brain/workspaces/cbm-navigation-20260910",
    "srv/community-brain/workspaces/cbm-automatic-20260910-effective-s01",
    "srv/community-brain/workspaces/cbm-weekly-20260911-effective",
    "srv/community-brain/workspaces/cbm-weekly-20260911-effective-r016",
    "srv/community-brain/workspaces/cbm-fathom-20260917-effective-r019",
    "srv/community-brain/workspaces/cbm-workspace-recovery-20260917-effective-r020",
    "srv/community-brain/workspaces/cbm-automatic-20260910-frontend",
    "srv/community-brain/workspaces/cbm-preview-20260910-effective",
    "srv/community-brain/workspaces/cbm-signal-20260910-effective",
    "srv/community-brain/workspaces/cbm-fathom-20260917-frontend",
    "srv/community-brain/workspaces/cbm-workspace-recovery-20260917-frontend",
    "usr/local/lib/community-brain-automatic", "etc/systemd/system/community-brain-automatic-pause.service",
    "etc/cron.d/community-brain-automatic",
    "etc/logrotate.d/community-brain-automatic",
]


def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def relative(name):
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or not path.parts or str(path) != name:
        raise ValueError("unsafe archive/reference path")
    return path


def inventory(root, folders):
    root = Path(root)
    result = {}
    for folder in folders:
        relative(folder)
        base = root / folder
        if not base.exists() or base.is_symlink():
            raise ValueError("missing or linked recovery input")
        for path in [base, *sorted(base.rglob("*"))] if base.is_dir() else [base]:
            info = path.lstat()
            if not (stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode)):
                raise ValueError("special archive input")
            key = str(path.relative_to(root))
            value = {"kind": "directory" if path.is_dir() else "file", "mode": stat.S_IMODE(info.st_mode), "uid": info.st_uid, "gid": info.st_gid}
            if path.is_file():
                if info.st_nlink != 1:
                    raise ValueError("hardlinked archive input")
                value.update(bytes=info.st_size, sha256=sha(path))
            result[key] = value
    return result


def write_json(path, value):
    with Path(path).open("x") as stream:
        os.fchmod(stream.fileno(), 0o600)
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())


def capture(root, folders, directory, job):
    directory = Path(directory)
    directory.mkdir(mode=0o700, parents=True, exist_ok=False)
    before = inventory(root, folders)
    archive = directory / "managed-state.tar.gz"
    with archive.open("xb") as stream:
        os.fchmod(stream.fileno(), 0o600)
        with tarfile.open(fileobj=stream, mode="w:gz", dereference=False) as tar:
            for name in sorted(before):
                tar.add(Path(root) / name, arcname=name, recursive=False)
        stream.flush()
        os.fsync(stream.fileno())
    if inventory(root, folders) != before:
        raise RuntimeError("archive inputs changed during capture")
    result = {"job_id": job, "folders": folders, "files": before,
              "archive": {"sha256": sha(archive), "bytes": archive.stat().st_size}}
    write_json(directory / "files-capture.json", result)
    return result


def extract_verified(directory, destination, expected_job):
    directory, destination = Path(directory), Path(destination)
    saved = json.loads((directory / "files-capture.json").read_text())
    if saved["job_id"] != expected_job:
        raise ValueError("wrong archive job")
    archive = directory / "managed-state.tar.gz"
    if sha(archive) != saved["archive"]["sha256"] or archive.stat().st_size != saved["archive"]["bytes"]:
        raise ValueError("archive digest mismatch")
    destination.mkdir(mode=0o700, exist_ok=False)
    seen = set()
    directories = []
    with tarfile.open(archive, "r:gz") as tar:
        for member in tar:
            path = relative(member.name)
            expected = saved["files"].get(str(path))
            if expected is None or str(path) in seen or not (member.isdir() or member.isfile()):
                raise ValueError("unexpected or duplicate archive member")
            if member.mode != expected["mode"] or member.uid != expected["uid"] or member.gid != expected["gid"]:
                raise ValueError("archive permission/owner mismatch")
            if ("directory" if member.isdir() else "file") != expected["kind"]:
                raise ValueError("archive type mismatch")
            seen.add(str(path))
            target = destination.joinpath(*path.parts)
            target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            if member.isdir():
                target.mkdir(mode=0o700, exist_ok=True)
                directories.append((target, expected))
                continue
            if member.size != expected["bytes"]:
                raise ValueError("archive file size mismatch")
            with tar.extractfile(member) as source, target.open("xb") as output:
                shutil.copyfileobj(source, output)
            if sha(target) != expected["sha256"]:
                raise ValueError("restored file hash mismatch")
            if os.geteuid() == 0:
                os.chown(target, expected["uid"], expected["gid"])
            target.chmod(expected["mode"])
    if seen != set(saved["files"]):
        raise ValueError("archive member set differs")
    for path, expected in reversed(directories):
        if os.geteuid() == 0:
            os.chown(path, expected["uid"], expected["gid"])
        path.chmod(expected["mode"])
    if inventory(destination, saved["folders"]) != saved["files"]:
        raise ValueError("restored inventory differs")
    return saved


def check_references(root, references):
    for ref in references:
        name = relative(ref["path"])
        p = Path(root) / "srv/community-brain/files" / name
        if p.is_symlink() or sha(p) != ref["sha256"] or (ref["size"] is not None and p.stat().st_size != ref["size"]):
            raise ValueError("database file reference differs")


CORPUS_CODE = r'''
import lancedb,json,hashlib
t=lancedb.connect('/copy/srv/community-brain/corpus/lancedb/nomic-v1').open_table('chunks')
rows=t.search().limit(None).to_arrow().to_pylist()
sessions={}
for row in rows:
 if row['extraction_status']!='success' or row['schema_version']!='1.1':raise ValueError('invalid corpus row')
 sessions.setdefault(row['session_id'],[]).append(json.dumps(row,sort_keys=True,separators=(',',':')))
fingerprints={str(k):hashlib.sha256('\n'.join(sorted(v)).encode()).hexdigest() for k,v in sessions.items()}
stats=[t.index_stats(i.name) for i in t.list_indices()]
if not any(s.index_type=='FTS' and s.num_indexed_rows==len(rows) and s.num_unindexed_rows==0 for s in stats):raise ValueError('incomplete FTS')
if t.schema.field('embedding').type.list_size!=768:raise ValueError('wrong dimensions')
print(json.dumps({'rows':len(rows),'sessions':fingerprints,'fts_indexed':len(rows),'fts_unindexed':0,'dimensions':768}))
'''


def corpus(root):
    result = subprocess.run(["docker", "run", "--rm", "--network", "none", "--user", "10001:10001",
                             "--read-only", "--tmpfs", "/tmp", "--cap-drop", "ALL", "--security-opt",
                             "no-new-privileges", "--memory", "1g", "-v", str(Path(root)/'srv/community-brain/corpus') + ":/copy/srv/community-brain/corpus:ro",
                             IMAGE, "python", "-c", CORPUS_CODE], capture_output=True, timeout=90)
    if result.returncode:
        raise RuntimeError("isolated corpus verification failed; private output suppressed")
    return json.loads(result.stdout)


def preserve_sessions(current, prior):
    if current["dimensions"] != prior["dimensions"] or any(current["sessions"].get(k) != v for k, v in prior["sessions"].items()):
        raise ValueError("previously indexed session changed or disappeared")


def verify_preserved(current):
    baseline = json.loads(Path('/usr/local/lib/community-brain-automatic/baseline-corpus.json').read_text())
    preserve_sessions(current, baseline)
    for path in (ROOT / 'automation/checkpoints').glob('*.json'):
        accepted = json.loads(path.read_text())
        prior_dir = ROOT / 'artifacts/automatic' / accepted['job_id']
        if sha(prior_dir / 'paired-manifest.json') != accepted['manifest_sha256']:
            raise ValueError('prior checkpoint manifest changed')
        manifest = json.loads((prior_dir / 'paired-manifest.json').read_text())
        if sha(prior_dir / 'corpus-before.json') != manifest['files']['corpus-before.json']['sha256']:
            raise ValueError('prior corpus evidence changed')
        preserve_sessions(current, json.loads((prior_dir / 'corpus-before.json').read_text()))
    archive = ROOT / 'meeting-archive-20260910'
    if sha(archive / 'manifest.json') != '3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00':
        raise ValueError('preserved archive manifest changed')
    manifest = json.loads((archive / 'manifest.json').read_text())
    entries = {a['id']:a for meeting in manifest['meetings'] for a in meeting['artifacts']}
    if len(entries) != 481 or {p.name for p in (archive/'files').iterdir()} != set(entries):
        raise ValueError('preserved archive set changed')
    for name,info in entries.items():
        p=archive/'files'/name
        if p.is_symlink() or sha(p)!=info['sha256'] or p.stat().st_size!=info['bytes']:
            raise ValueError('preserved archive content changed')


def restore(directory, job, temporary_parent):
    directory=Path(directory)
    captured = json.loads((directory / "database-capture.json").read_text())
    assert captured["job_id"] == job
    with tempfile.TemporaryDirectory(prefix=".cbm-auto-restore-", dir=temporary_parent) as temporary:
        dest = Path(temporary) / "restored"
        saved = extract_verified(directory, dest, job)
        check_references(dest, captured["references"])
        restored = corpus(dest)
        assert restored == json.loads((directory / "corpus-before.json").read_text())
    assert not dest.exists()
    result={"job_id": job, "files_verified": len(saved["files"]),
            "archive_sha256": saved["archive"]["sha256"], "capture_sha256": sha(directory / "files-capture.json"),
            "references_verified": len(captured["references"]), "corpus": restored,
            "temporary_restore_removed": True, "network_disabled": True}
    write_json(directory / "files-restore.json",result)
    return result


if __name__ == "__main__":
    os.umask(0o077)
    try:
        operation, job = sys.argv[1:3]
        if str(UUID(job)) != job:
            raise ValueError("invalid job")
        directory = ROOT / "artifacts/automatic" / job
        if operation == "capture":
            if subprocess.check_output(["docker", "ps", "-q", "--filter", "label=cbm.automatic-stage=true"]).strip():
                raise RuntimeError("automatic worker/scanner still running")
            capture(Path("/"), FOLDERS, directory, job)
            current=corpus(Path("/"));verify_preserved(current)
            write_json(directory / "corpus-before.json", current)
        elif operation == "restore":
            restore(directory,job,ROOT/'artifacts')
        elif operation == "verify":
            saved = json.loads((directory / "files-capture.json").read_text())
            assert saved["job_id"] == job and inventory(Path("/"), saved["folders"]) == saved["files"]
            assert corpus(Path("/")) == json.loads((directory / "corpus-before.json").read_text())
        else:
            raise ValueError("unknown operation")
        print(json.dumps({"job_id": job, "operation": operation, "passed": True}))
    except Exception:
        print("Filesystem checkpoint adapter failed; reconcile private intent", file=sys.stderr)
        raise SystemExit(1) from None

"""Mac management checkpoint consumer. Only pending, completed automatic jobs.

Run under the existing Mac scheduler's local mutex. Production capture/restore
and uncertain external effects are journaled; no automatic replay on ambiguity.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
import time
from uuid import UUID

from checkpoint_acceptance import REQUIRED, atomic
from checkpoint_journal import Journal
from lease_supervisor import LeaseSupervisor
from transport import VM, DB, PVE, Transport, command
import management_controls

REMOTE = "/srv/community-brain"
LOCAL = Path.home() / ".local/state/community-brain-management/automatic"


def spec(path):
    path = Path(path)
    with path.open("rb") as stream:
        return {"bytes": path.stat().st_size, "sha256": hashlib.file_digest(stream, "sha256").hexdigest()}


def read_marker():
    code = r'''
import pathlib,json
p=pathlib.Path('/srv/community-brain/automation/checkpoint-needed.json')
root=p.parent
if (root/'paused').exists():print(json.dumps({'control_state':'paused'}));raise SystemExit(0)
if (root/'attention.json').exists() or (root/'management-attention.json').exists():print(json.dumps({'control_state':'attention_required'}));raise SystemExit(0)
if p.exists():
 assert not p.is_symlink() and p.stat().st_uid==0 and p.stat().st_mode&0o777==0o600
 value=json.loads(p.read_text());print(json.dumps(value))
else:print('null')
'''
    result = subprocess.run(command(VM, ["python3", "-c", code]), capture_output=True, timeout=20)
    if result.returncode:
        raise RuntimeError("cannot inspect pending checkpoint")
    return json.loads(result.stdout)


class Recovery:
    def __init__(self, job, marker, lease):
        self.job, self.marker, self.lease = job, marker, lease
        self.transport = Transport(lease)
        self.local = LOCAL / "evidence" / job
        self.local.mkdir(mode=0o700, parents=True, exist_ok=True)
        self.vm = REMOTE + "/artifacts/automatic/" + job
        self.db = "/var/backups/community-brain/automatic/" + job
        self.offhost = self.db + "/paired"
        self.journal = Journal(LOCAL / "journal", job, marker, lease.check)

    def pull(self, host, source, name):
        return self.transport.download(host, source, self.local / name)

    def push(self, name, host=VM, directory=None):
        return self.transport.deliver(self.local / name, host, (directory or self.vm) + "/" + name)

    def capture(self):
        current = self.transport.json(VM, "import json,pathlib; print(pathlib.Path('/srv/community-brain/automation/checkpoint-needed.json').read_text())")
        if current != self.marker:
            raise ValueError("pending marker changed before capture")
        self.transport.adapter(DB, "database_adapter.py", "capture", self.job)
        self.transport.adapter(VM, "files_adapter.py", "capture", self.job)
        for name in ("database.dump", "database-capture.json"):
            self.pull(DB, self.db + "/" + name, name)
            self.push(name)
        self.transport.deliver(self.local / "database.dump", VM,
                               REMOTE + "/db-backups/automatic-" + self.job + ".dump")
        management_controls.capture(self.local, self.job, self.transport)
        for name in ("management-controls.tar.gz", "management-controls.json", "host-controls.json"):
            self.push(name)
        return {"job_id": self.job, "database_directory": self.db, "files_directory": self.vm}

    def database_restore(self):
        self.transport.adapter(DB, "database_adapter.py", "restore", self.job)
        self.pull(DB, self.db + "/database-restore.json", "database-restore.json")
        self.push("database-restore.json")
        return {"job_id": self.job, "receipt": spec(self.local / "database-restore.json")}

    def files_restore(self):
        self.transport.adapter(VM, "files_adapter.py", "restore", self.job)
        self.pull(VM, self.vm + "/files-restore.json", "files-restore.json")
        return {"job_id": self.job, "receipt": spec(self.local / "files-restore.json")}

    def offhost_copy(self):
        for name in sorted(REQUIRED):
            if not (self.local / name).exists():
                self.pull(VM, self.vm + "/" + name, name)
        manifest = {"job_id": self.job, "files": {name: spec(self.local / name) for name in sorted(REQUIRED)},
                    "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "consistency": "Ordered quiet lease held throughout live capture and comparisons; logical restore verified separately from PBS."}
        atomic(self.local / "paired-manifest.json", manifest)
        self.push("paired-manifest.json")
        expected = {**manifest["files"], "paired-manifest.json": spec(self.local / "paired-manifest.json")}
        for name in sorted(expected):
            self.transport.deliver(self.local / name, DB, self.offhost + "/" + name, expected[name])
        self.transport.verify_set(DB, self.offhost, expected)
        self.transport.verify_set(VM, self.vm, expected)
        atomic(self.local / "offhost-copy.json", {"job_id": self.job, "verified": True,
                                                  "directory": self.offhost, "files": expected})
        self.push("offhost-copy.json")
        self.push("offhost-copy.json", DB, self.offhost)
        return {"job_id": self.job, "manifest_sha256": expected["paired-manifest.json"]["sha256"]}

    def pbs(self):
        manifest_hash = spec(self.local / "paired-manifest.json")["sha256"]
        # Re-read actual paired files immediately before the snapshot request.
        self.verify_copies()
        mount = self.transport.json(VM, "import subprocess,json; print(subprocess.check_output(['findmnt','-J','-T','/srv/community-brain/artifacts','-o','TARGET,SOURCE,FSTYPE']).decode())")
        if mount["filesystems"] != [{"target": "/srv/community-brain", "source": "/dev/sdb", "fstype": "ext4"}]:
            raise ValueError("checkpoint state disk mapping changed")
        self.transport.adapter(PVE, "pbs_adapter.py", "start", self.job, (manifest_hash,), timeout=120)
        deadline = time.monotonic() + 600
        while time.monotonic() < deadline:
            receipt = self.transport.adapter(PVE, "pbs_adapter.py", "inspect", self.job, (manifest_hash,), timeout=45)
            if receipt.get("status") == "OK":
                atomic(self.local / "pbs-receipt.json", receipt)
                self.push("pbs-receipt.json")
                self.push("pbs-receipt.json", DB, self.offhost)
                return {"job_id": self.job, "manifest_sha256": manifest_hash, "snapshot": receipt["snapshot"]}
            self.lease.check()
            time.sleep(3)
        raise TimeoutError("PBS still pending; reconcile existing task, never resubmit")

    def verify_copies(self):
        manifest = json.loads((self.local / "paired-manifest.json").read_text())
        if manifest["job_id"] != self.job:
            raise ValueError("wrong local manifest")
        expected = {**manifest["files"], "paired-manifest.json": spec(self.local / "paired-manifest.json")}
        self.transport.verify_set(VM, self.vm, expected)
        self.transport.verify_set(DB, self.offhost, expected)
        return expected["paired-manifest.json"]["sha256"]

    def verify_external(self):
        manifest_hash = self.verify_copies()
        actual = self.transport.adapter(PVE, "pbs_adapter.py", "inspect", self.job, (manifest_hash,), timeout=45)
        stored = json.loads((self.local / "pbs-receipt.json").read_text())
        if actual != stored or actual.get("status") != "OK":
            raise ValueError("actual PBS state differs from accepted receipt")
        for host, directory in ((VM, self.vm), (DB, self.offhost)):
            self.transport.verify_set(host, directory, {name: spec(self.local / name) for name in ("offhost-copy.json", "pbs-receipt.json")})
        return manifest_hash

    def final_verification(self):
        self.transport.adapter(DB, "database_adapter.py", "verify", self.job)
        self.transport.adapter(VM, "files_adapter.py", "verify", self.job)
        controls = json.loads((self.local / "host-controls.json").read_text())
        if management_controls.host(self.transport) != controls["host"] or management_controls.auth(self.transport) != controls["auth"]:
            raise ValueError("active host or Authentik controls changed during checkpoint")
        return {"job_id": self.job, "manifest_sha256": self.verify_external()}

    def run(self):
        for phase in ("capture", "database_restore", "files_restore", "offhost_copy", "pbs", "final_verification"):
            self.journal.run(phase, getattr(self, phase))
        manifest_hash = self.journal.verified_manifest(lambda job, receipts: self.verify_external())
        self.lease.acknowledge(manifest_hash)
        atomic(self.local / "acknowledged.json", {"job_id": self.job, "manifest_sha256": manifest_hash,
                                                  "verified": True, "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat()})
        return {"state": "checkpoint_verified", "job_id": self.job, "manifest_sha256": manifest_hash}


def main():
    os.umask(0o077)
    marker = read_marker()
    if marker is None:
        return {"state": "idle"}
    if marker.get('control_state'):
        return {'state':marker['control_state']}
    job = marker.get("job_id")
    if str(UUID(job)) != job or marker.get("policy") != "new-meeting-full-loop-v1":
        raise ValueError("invalid pending checkpoint marker")
    nonce = secrets.token_hex(32)
    args = command(VM, ["python3", "-B", "-u", "/usr/local/lib/community-brain-automatic/quiet_window.py",
                        REMOTE, job, nonce, "30", "ack-enabled"])
    with LeaseSupervisor(args, job, nonce, interval=3, reply_timeout=10) as lease:
        recovery = Recovery(job, marker, lease)
        # An acknowledgment committed before a lost reply is durable evidence.
        # Validate the actual pair/copies/PBS again, then remove only its marker.
        accepted = recovery.transport.json(VM, "import pathlib,json; p=pathlib.Path(" + repr(REMOTE + "/automation/checkpoints/" + job + ".json") + "); print(p.read_text() if p.exists() else 'null')")
        if accepted is not None:
            manifest_hash = recovery.verify_external()
            if accepted.get("manifest_sha256") != manifest_hash or accepted.get("job_id") != job or accepted.get("verified") is not True:
                raise ValueError("existing acknowledgment conflicts with actual checkpoint")
            lease.acknowledge(manifest_hash)
            return {"state": "acknowledgment_reconciled", "job_id": job}
        return recovery.run()


if __name__ == "__main__":
    try:
        print(json.dumps(main()))
    except Exception:
        print("Automatic recovery requires reconciliation; no checkpoint acknowledged", file=sys.stderr)
        raise SystemExit(1) from None

"""Durable phase journal. Production adapters and acknowledgment are not wired yet."""
import hashlib
import json
import os
from pathlib import Path
import re
from uuid import UUID

PHASES = ("capture", "database_restore", "files_restore", "offhost_copy", "pbs", "final_verification")
class ReconciliationRequired(RuntimeError):pass

def canonical(value):return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
def digest(value):return hashlib.sha256(canonical(value)).hexdigest()
def write_atomic(path, value):
    temp=path.with_name("."+path.name+".tmp")
    fd=os.open(temp,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,"wb") as stream:
        stream.write(canonical(value));stream.flush();os.fsync(stream.fileno())
    os.replace(temp,path)
    fd=os.open(path.parent,os.O_RDONLY)
    try:os.fsync(fd)
    finally:os.close(fd)

class Journal:
    def __init__(self, root, job_id, inputs, assert_lease):
        if str(UUID(job_id))!=job_id:raise ValueError("invalid job identity")
        self.root=Path(root)/job_id
        self.root.mkdir(mode=0o700,parents=True,exist_ok=True)
        if self.root.is_symlink():raise ValueError("unsafe journal directory")
        self.job_id,self.input_hash,self.assert_lease=job_id,digest(inputs),assert_lease
    def read(self, phase):
        path=self.root/(phase+".json")
        if not path.exists():return None
        if path.is_symlink():raise ReconciliationRequired("unsafe journal file")
        value=json.loads(path.read_text())
        if value.get("job_id")!=self.job_id or value.get("input_hash")!=self.input_hash or value.get("phase")!=phase:
            raise ReconciliationRequired("journal identity mismatch")
        if value.get("state")!="complete":raise ReconciliationRequired("unfinished phase; do not repeat external effects")
        if digest(value.get("receipt"))!=value.get("receipt_sha256"):
            raise ReconciliationRequired("receipt mismatch")
        return value["receipt"]
    def run(self, phase, operation):
        if phase not in PHASES:raise ValueError("unknown phase")
        self.assert_lease()
        for previous in PHASES[:PHASES.index(phase)]:
            if self.read(previous) is None:raise ReconciliationRequired("earlier phase incomplete")
        existing=self.read(phase)
        if existing is not None:return existing
        path=self.root/(phase+".json")
        record=dict(job_id=self.job_id,input_hash=self.input_hash,phase=phase,state="intent")
        write_atomic(path,record)
        receipt=operation()
        self.assert_lease()
        if not isinstance(receipt,dict) or receipt.get("job_id")!=self.job_id:
            raise ReconciliationRequired("wrong operation result")
        record.update(state="complete",receipt=receipt,receipt_sha256=digest(receipt))
        write_atomic(path,record)
        return receipt
    def verified_manifest(self, verify_actual_checkpoint):
        """Callback MUST reread actual manifests, copies/PBS and named job, not JSON flags."""
        self.assert_lease()
        receipts={phase:self.read(phase) for phase in PHASES}
        if any(value is None for value in receipts.values()):raise ReconciliationRequired("checkpoint incomplete")
        result=verify_actual_checkpoint(self.job_id,receipts)
        self.assert_lease()
        if not isinstance(result,str) or not re.fullmatch(r"[a-f0-9]{64}",result):
            raise ReconciliationRequired("checkpoint verification did not return a manifest hash")
        return result

"""Native PostgreSQL capture/restore adapter; called under the external quiet lease.

All files and diagnostics stay private. Capture is never retried automatically
after an uncertain result. This adapter does not start application/queue workers.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from uuid import UUID, uuid4

SOURCE = "community_brain_prod"
BASE = Path("/var/backups/community-brain/automatic")


def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def pg(args, *, stdin=None, stdout=None):
    result = subprocess.run(["runuser", "-u", "postgres", "--", *args],
                            stdin=stdin, stdout=stdout or subprocess.PIPE,
                            stderr=subprocess.DEVNULL, timeout=180)
    if result.returncode:
        raise RuntimeError("native database operation failed; acceptance forbidden")
    return result.stdout.decode() if result.stdout is not None else None


def sql(db, query):
    return pg(["psql", "-X", "-At", "-v", "ON_ERROR_STOP=1", "-d", db, "-c", query]).strip()


def rows(db, query):
    return json.loads(sql(db, "SELECT coalesce(json_agg(t),'[]'::json) FROM (" + query + ") t"))


def ident(value):
    return '"' + value.replace('"', '""') + '"'


def snapshot(db):
    tables = rows(db, "SELECT schemaname,tablename,tableowner FROM pg_tables WHERE schemaname NOT IN ('pg_catalog','information_schema') AND schemaname NOT LIKE 'pg_toast%' ORDER BY schemaname,tablename")
    values = {}
    for table in tables:
        name = table["schemaname"] + "." + table["tablename"]
        qualified = ident(table["schemaname"]) + "." + ident(table["tablename"])
        data = sql(db, "SELECT coalesce(jsonb_agg(j ORDER BY j::text),'[]'::jsonb) FROM (SELECT to_jsonb(t) j FROM " + qualified + " t) x")
        values[name] = {"rows": int(sql(db, "SELECT count(*) FROM " + qualified)),
                        "sha256": hashlib.sha256(data.encode()).hexdigest()}
    sequences = rows(db, "SELECT schemaname,sequencename,sequenceowner,data_type,start_value,min_value,max_value,increment_by,cycle,cache_size,last_value FROM pg_sequences WHERE schemaname NOT LIKE 'pg_%' ORDER BY schemaname,sequencename")
    for sequence in sequences:
        qualified = ident(sequence["schemaname"]) + "." + ident(sequence["sequencename"])
        sequence["state"] = rows(db, "SELECT last_value,is_called FROM " + qualified)
    schema = pg(["pg_dump", "--schema-only", "--no-comments", db])
    stable = "\n".join(line for line in schema.splitlines()
                       if line.strip() and not line.startswith(("--", "\\restrict", "\\unrestrict")))
    return {"tables": tables, "table_content": values, "sequences": sequences,
            "schema_sha256": hashlib.sha256(stable.encode()).hexdigest()}


def references(db):
    refs = rows(db, "SELECT 'source' kind,id::text,path,sha256,size FROM cb_sources UNION ALL SELECT 'artifact',id::text,path,sha256,size FROM cb_artifacts UNION ALL SELECT 'response',id::text,response_path,response_hash,NULL FROM cb_model_calls ORDER BY kind,id")
    present = []
    for ref in refs:
        if ref["path"] is None and ref["sha256"] is None:
            continue
        if not isinstance(ref["path"], str) or not re.fullmatch(r"[a-f0-9]{64}", ref.get("sha256") or ""):
            raise ValueError("partial database file reference")
        present.append(ref)
    return present


def completed_job(db, job_id):
    if str(UUID(job_id)) != job_id:
        raise ValueError("invalid job")
    jobs = rows(db, "SELECT id::text,scope,parent_id,processing,artifacts,indexing,config FROM cb_jobs WHERE id='" + job_id + "'::uuid")
    if len(jobs) != 1:
        raise ValueError("checkpoint job missing")
    job = jobs[0]
    if job['scope']!='community-brain' or job['parent_id'] is not None:
        raise ValueError('checkpoint job is not an original submission in the approved scope')
    if (job["processing"], job["artifacts"], job["indexing"]) != ("succeeded", "ready", "complete") or job["config"].get("automation_policy") != "new-meeting-full-loop-v1":
        raise ValueError("checkpoint job is not an unambiguous automatic completion")
    stages = rows(db, "SELECT name,state,attempts,generation FROM cb_stages WHERE job_id='" + job_id + "'::uuid ORDER BY name")
    selected = [stage for stage in stages if stage["name"] in ("processing", "indexing")]
    if len(selected) != 2 or any(stage["state"] != "succeeded" or stage["attempts"] != 1 or stage["generation"] != 1 for stage in selected):
        raise ValueError("checkpoint stage result ambiguous")
    return {"job_id": job_id, "processing": job["processing"], "artifacts": job["artifacts"],
            "indexing": job["indexing"], "stages": stages}


def private_json(path, value):
    with Path(path).open("x") as stream:
        os.fchmod(stream.fileno(), 0o600)
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())


def capture(db, directory, job_id, *, require_complete=True):
    directory = Path(directory)
    directory.mkdir(mode=0o700, parents=True, exist_ok=False)
    job = completed_job(db, job_id) if require_complete else {"job_id": job_id, "disposable_fixture": True}
    before = snapshot(db)
    refs = references(db)
    dump = directory / "database.dump"
    with dump.open("xb") as stream:
        os.fchmod(stream.fileno(), 0o600)
        pg(["pg_dump", "--format=custom", db], stdout=stream)
        stream.flush()
        os.fsync(stream.fileno())
    if snapshot(db) != before or references(db) != refs:
        raise RuntimeError("database changed during capture")
    result = {"job_id": job_id, "job": job, "state": before, "references": refs,
              "dump": {"sha256": sha(dump), "bytes": dump.stat().st_size}}
    private_json(directory / "database-capture.json", result)
    return result


def restore(directory, expected_job):
    directory = Path(directory)
    captured = json.loads((directory / "database-capture.json").read_text())
    if captured["job_id"] != expected_job:
        raise ValueError("wrong captured job")
    dump = directory / "database.dump"
    if sha(dump) != captured["dump"]["sha256"] or dump.stat().st_size != captured["dump"]["bytes"]:
        raise ValueError("dump mismatch")
    name = "cbm_auto_restore_" + uuid4().hex[:16]
    # Record the intended disposable database before creating it. Interrupted
    # cleanup must be reconciled explicitly, never inferred from a missing reply.
    private_json(directory / "restore-intent.json", {"job_id": expected_job, "database": name})
    sql("postgres", "CREATE DATABASE " + ident(name) + " TEMPLATE template0 CONNECTION LIMIT 0")
    try:
        sql(name, "REVOKE CONNECT ON DATABASE " + ident(name) + " FROM PUBLIC")
        with dump.open("rb") as stream:
            pg(["pg_restore", "--exit-on-error", "--dbname", name], stdin=stream)
        if snapshot(name) != captured["state"] or references(name) != captured["references"]:
            raise RuntimeError("restored database schema/owners/grants/rows/references differ")
        result = {"job_id": expected_job, "schema_owners_grants_rows_sequences_match": True,
                  "dump_sha256": captured["dump"]["sha256"],
                  "capture_sha256": sha(directory / "database-capture.json"),
                  "references_verified": len(captured["references"]),
                  "public_connect_revoked": True, "connection_limit": 0,
                  "queue_or_application_started": False}
    finally:
        pg(["dropdb", name])
    result["disposable_database_removed"] = True
    private_json(directory / "database-restore.json", result)
    return result


if __name__ == "__main__":
    os.umask(0o077)
    try:
        operation, job = sys.argv[1:3]
        if str(UUID(job)) != job:
            raise ValueError("invalid job")
        directory = BASE / job
        if operation == "capture":
            capture(SOURCE, directory, job)
        elif operation == "restore":
            restore(directory, job)
        elif operation == "verify":
            saved = json.loads((directory / "database-capture.json").read_text())
            assert saved["job_id"] == job and snapshot(SOURCE) == saved["state"] and references(SOURCE) == saved["references"]
            completed_job(SOURCE, job)
        else:
            raise ValueError("unknown operation")
        print(json.dumps({"job_id": job, "operation": operation, "passed": True}))
    except Exception:
        print("Database checkpoint adapter failed; reconcile private intent", file=sys.stderr)
        raise SystemExit(1) from None

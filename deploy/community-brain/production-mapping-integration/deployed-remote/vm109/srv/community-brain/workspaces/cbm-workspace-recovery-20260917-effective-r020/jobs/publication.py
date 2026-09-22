"""Single-writer indexing and immutable, verified distribution candidates."""

from contextlib import contextmanager
from dataclasses import asdict
import fcntl
import gzip
import io
import json
import os
from pathlib import Path
import subprocess
import tarfile
import tempfile

import lancedb
from sqlalchemy import select
from sqlalchemy.orm import Session

from community_brain.ingestion.pipeline import IngestRequest, ingest_session
from community_brain.ingestion.schema import SCHEMA_VERSION
from community_brain.llm import LLMOutcomeUnknown, stop_uncertain_outcomes
from community_brain.query.corpus_verify import verify_corpus_v3_state_readonly
from community_brain.processing.pipeline import PipelineFailure, OutcomeUnknown
from .models import Artifact, Job
from .storage import digest


@contextmanager
def corpus_lock(root):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    with (root / "writer.lock").open("a") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def build_bundle(
    corpus, output, version, timestamp, embedding_model="nomic-embed-text"
):
    """Caller holds writer lock. Only reads source; tarball has deterministic metadata."""
    corpus, output = Path(corpus), Path(output)
    output.mkdir(parents=True, exist_ok=True)
    table = lancedb.connect(str(corpus)).open_table("chunks")
    verify_corpus_v3_state_readonly(table)
    rows = (
        table.search()
        .select(["session_id", "extraction_status"])
        .limit(None)
        .to_arrow()
        .to_pylist()
    )
    if any(r["extraction_status"] != "success" for r in rows):
        raise PipelineFailure("corpus_has_failed_chunks")
    if (
        table.schema.field("embedding").type.list_size != 768
        or embedding_model != "nomic-embed-text"
    ):
        raise PipelineFailure("embedding_model_mismatch")
    manifest = {
        "corpus_version": version,
        "schema_version": SCHEMA_VERSION,
        "embedding_model": embedding_model,
        "session_count": len({r["session_id"] for r in rows}),
        "chunk_count": len(rows),
        "generation_timestamp_utc": timestamp,
        "lancedb_version": lancedb.__version__,
        "files": {},
    }
    archive = output / f"corpus-{version}.tar.gz"
    if archive.exists():
        raise PipelineFailure("immutable_release_conflict")
    with (
        archive.open("xb") as raw,
        gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, filename="") as compressed,
        tarfile.open(fileobj=compressed, mode="w") as tar,
    ):
        for file in sorted(corpus.rglob("*")):
            if file.is_symlink():
                raise PipelineFailure("symlink_corpus_file")
            if not file.is_file():
                continue
            relative = "lancedb/nomic-v1/" + file.relative_to(corpus).as_posix()
            content = file.read_bytes()
            manifest["files"][relative] = digest(content)
            info = tarfile.TarInfo(relative)
            info.size = len(content)
            info.mode = 0o600
            info.mtime = 0
            tar.addfile(info, io.BytesIO(content))
    manifest["archive_sha256"] = digest(archive.read_bytes())
    (output / "corpus-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )
    (output / "sha256sum.txt").write_text(
        manifest["archive_sha256"] + "  " + archive.name + "\n"
    )
    validate_bundle(output)
    for file in output.iterdir():
        with file.open("rb") as stream:
            os.fsync(stream.fileno())
    fd = os.open(output, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    return manifest


def validate_bundle(output):
    output = Path(output)
    manifest = json.loads((output / "corpus-manifest.json").read_text())
    archive = output / f"corpus-{manifest['corpus_version']}.tar.gz"
    if digest(archive.read_bytes()) != manifest["archive_sha256"]:
        raise PipelineFailure("archive_checksum_mismatch")
    with (
        tempfile.TemporaryDirectory(prefix="cbm-consumer-") as directory,
        tarfile.open(archive) as tar,
    ):
        seen = set()
        for member in tar:
            if (
                not member.isfile()
                or member.name not in manifest["files"]
                or member.name in seen
            ):
                raise PipelineFailure("invalid_archive_member")
            path = Path(directory) / member.name
            if not path.resolve().is_relative_to(Path(directory)):
                raise PipelineFailure("archive_path_escape")
            content = tar.extractfile(member).read()
            if digest(content) != manifest["files"][member.name]:
                raise PipelineFailure("member_checksum_mismatch")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
            seen.add(member.name)
        if seen != set(manifest["files"]):
            raise PipelineFailure("missing_archive_member")
        table = lancedb.connect(str(Path(directory) / "lancedb/nomic-v1")).open_table(
            "chunks"
        )
        verify_corpus_v3_state_readonly(table)
        if table.count_rows() != manifest["chunk_count"]:
            raise PipelineFailure("consumer_count_mismatch")
    return manifest


class PublicationHandlers:
    def __init__(
        self,
        store,
        corpus_root,
        config_dir,
        ollama_url,
        git_remote=None,
        allow_network_publish=False,
        release_publisher=None,
    ):
        self.store = store
        self.root = Path(corpus_root)
        self.db = self.root / "lancedb/nomic-v1"
        self.config_dir = Path(config_dir)
        self.ollama_url = ollama_url
        self.git_remote = git_remote
        self.allow_network_publish = allow_network_publish
        self.release_publisher = release_publisher

    def artifacts(self, job_id):
        with Session(self.store.engine) as s:
            job = s.get(Job, job_id)
            records = s.scalars(select(Artifact).where(Artifact.job_id == job_id)).all()
            content = {
                a.name: self.store.storage.read(a.path, a.sha256) for a in records
            }
            return job, records, content

    def indexing(self, job_id):
        job, records, content = self.artifacts(job_id)
        session_id = job.identity["local_date"]
        with corpus_lock(self.root):
            reservation = self.root / "sessions" / f"{session_id}.json"
            reservation.parent.mkdir(exist_ok=True)
            if reservation.exists():
                if json.loads(reservation.read_text())["job_id"] != str(job_id):
                    raise PipelineFailure("existing_session_requires_review")
            else:
                db = lancedb.connect(str(self.db))
                if "chunks" in db.list_tables().tables and db.open_table(
                    "chunks"
                ).count_rows(f"session_id = '{session_id}'"):
                    raise PipelineFailure("existing_session_requires_review")
                # Persist before external extraction; interrupted indexing is unknown
                # and never auto-replayed merely because a lease expired.
                with reservation.open("x") as stream:
                    json.dump(
                        {
                            "job_id": str(job_id),
                            "meeting_id": job.identity["meeting_id"],
                        },
                        stream,
                    )
                    stream.flush()
                    os.fsync(stream.fileno())
            names = {
                "prepared-transcript.md": "prepared_transcript",
                "extracted-signal.md": "extracted_signal",
                "community-post.md": "community_post",
            }
            materialized = self.root / "ingest" / str(job_id)
            materialized.mkdir(parents=True, exist_ok=True)
            paths = {}
            for name, kind in names.items():
                if name not in content:
                    raise PipelineFailure("missing_ingest_artifact")
                path = materialized / name
                if path.is_symlink():
                    raise PipelineFailure("symlink_ingest_artifact")
                if path.exists():
                    if path.read_bytes() != content[name]:
                        raise PipelineFailure("immutable_ingest_conflict")
                else:
                    staging = materialized / ("." + name + ".staging")
                    with staging.open("wb") as stream:
                        stream.write(content[name])
                        stream.flush()
                        os.fsync(stream.fileno())
                    os.link(staging, path)
                    staging.unlink()
                paths[kind] = str(path)
            fd = os.open(materialized, os.O_RDONLY | os.O_DIRECTORY)
            try:
                os.fsync(fd)
            finally:
                os.close(fd)
            try:
                with stop_uncertain_outcomes():
                    result = ingest_session(
                        IngestRequest(
                            session_id, job.identity["local_date"], None, paths, False
                        ),
                        self.config_dir,
                        str(self.db),
                        self.ollama_url,
                    )
            except LLMOutcomeUnknown as exc:
                raise OutcomeUnknown(
                    "indexing provider outcome requires reconciliation"
                ) from exc
            body = asdict(result)
            body["state"] = "partial" if result.chunks_failed else "complete"
            return body

    def git(self, job_id):
        job, _, content = self.artifacts(job_id)
        if not self.git_remote:
            raise PipelineFailure("git_destination_not_configured")
        if not self.allow_network_publish and not Path(self.git_remote).is_dir():
            raise PipelineFailure("network_publication_not_enabled")
        with (
            corpus_lock(self.root),
            tempfile.TemporaryDirectory(prefix="cbm-git-") as directory,
        ):

            def git(*args):
                result = subprocess.run(
                    [
                        "git",
                        "-c",
                        "core.hooksPath=/dev/null",
                        "-c",
                        "commit.gpgsign=false",
                        *args,
                    ],
                    cwd=directory,
                    capture_output=True,
                    text=True,
                    timeout=60,
                    env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
                )
                if result.returncode:
                    if args[0] == "push":
                        raise OutcomeUnknown("git push outcome requires reconciliation")
                    raise PipelineFailure("git_publication_failed")
                return result.stdout.strip()

            git("clone", "--no-local", self.git_remote, ".")
            target = Path(directory) / "output" / job.identity["local_date"]
            if job.parent_id:
                target = target / "runs" / str(job_id)
            if any(
                parent.is_symlink()
                for parent in [target, *target.parents]
                if parent != Path(directory).parent
            ):
                raise PipelineFailure("symlink_git_output")
            target.mkdir(parents=True, exist_ok=True)
            for name, data in content.items():
                path = target / name
                if path.is_symlink():
                    raise PipelineFailure("symlink_git_output")
                if path.exists() and path.read_bytes() != data:
                    raise PipelineFailure("git_output_conflict")
                path.write_bytes(data)
            git("add", "--", "output")
            if git("status", "--porcelain"):
                git(
                    "-c",
                    "user.name=Community Brain",
                    "-c",
                    "user.email=community-brain@localhost",
                    "commit",
                    "-m",
                    f"Publish recap {job_id}",
                )
            commit = git("rev-parse", "HEAD")
            git("push", "origin", "HEAD")
            return {
                "commit": commit,
                "artifact_hashes": {
                    name: digest(data) for name, data in content.items()
                },
            }

    def distribution(self, job_id):
        job, _, _ = self.artifacts(job_id)
        version = "v" + str(job_id)
        with corpus_lock(self.root):
            releases = self.root / "releases"
            releases.mkdir(exist_ok=True)
            candidate = releases / version
            if candidate.exists():
                manifest = validate_bundle(candidate)
            else:
                with tempfile.TemporaryDirectory(
                    dir=releases, prefix=".candidate-"
                ) as directory:
                    manifest = build_bundle(
                        self.db, directory, version, job.created_at.isoformat()
                    )
                    os.rename(directory, candidate)
            # Ready pointer changes only after package and consumer validation.
            receipt = (
                self.release_publisher.publish(candidate, version)
                if self.release_publisher
                else None
            )
            if receipt is None:
                return {
                    "state": "validated",
                    "version": version,
                    "sha256": manifest["archive_sha256"],
                    "manifest": manifest,
                }
            pointer = releases / ".current.tmp"
            with pointer.open("w") as stream:
                json.dump(
                    {"version": version, "sha256": manifest["archive_sha256"]}, stream
                )
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(pointer, releases / "current.json")
            fd = os.open(releases, os.O_RDONLY | os.O_DIRECTORY)
            try:
                os.fsync(fd)
            finally:
                os.close(fd)
            return {
                "version": version,
                "sha256": manifest["archive_sha256"],
                "manifest": manifest,
                "receipt": receipt,
            }

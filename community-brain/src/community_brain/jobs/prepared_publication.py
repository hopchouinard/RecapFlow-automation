"""Publish precomputed, reviewed commits and a fixed corpus; no content generation."""

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

from community_brain.processing.pipeline import OutcomeUnknown, PipelineFailure
from .publication import validate_bundle
from .store import fingerprint

REPOSITORIES = {
    "operator": "hopchouinard/RecapFlow-automation",
    "consumer": "hopchouinard/community-brain-distribution",
}


def record(path, value):
    path = Path(path)
    with path.open("a", encoding="utf-8") as stream:
        os.chmod(path, 0o600)
        stream.write(json.dumps(value, sort_keys=True) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


class PreparedGit:
    def __init__(self, directory, spec, *, token=None, askpass=None, local_remote=None):
        self.directory, self.spec = Path(directory), spec
        self.before_write = lambda: None
        if (
            spec.get("repository") not in REPOSITORIES.values()
            or spec.get("branch") != "main"
        ):
            raise PipelineFailure("unapproved_repository_or_branch")
        if any(
            not re.fullmatch(r"[0-9a-f]{40}", spec.get(key, ""))
            for key in ("base", "commit")
        ):
            raise PipelineFailure("invalid_commit_pin")
        self.remote = (
            local_remote or "https://github.com/" + spec["repository"] + ".git"
        )
        if local_remote is not None and not Path(local_remote).is_dir():
            raise PipelineFailure("local_fixture_required")
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        self.env.update(
            GIT_CONFIG_NOSYSTEM="1",
            GIT_CONFIG_GLOBAL="/dev/null",
            GIT_TERMINAL_PROMPT="0",
        )
        if token is not None:
            if not askpass:
                raise PipelineFailure("credential_delivery_required")
            self.env.update(CB_PUBLISHER_GITHUB_TOKEN=token, GIT_ASKPASS=str(askpass))

    def git(self, *args, external_write=False):
        try:
            result = subprocess.run(
                [
                    "git",
                    "-c",
                    "core.hooksPath=/dev/null",
                    "-c",
                    "credential.helper=",
                    "--git-dir",
                    str(self.directory),
                    *args,
                ],
                env=self.env,
                capture_output=True,
                timeout=90,
            )
        except subprocess.TimeoutExpired:
            if external_write:
                raise OutcomeUnknown("git write requires reconciliation") from None
            raise PipelineFailure("git_read_failed") from None
        if result.returncode:
            if external_write:
                raise OutcomeUnknown("git write requires reconciliation")
            raise PipelineFailure("git_read_failed")
        return result.stdout

    def validate(self, files):
        commit, base = self.spec["commit"], self.spec["base"]
        parents = self.git("rev-list", "--parents", "-n", "1", commit).decode().split()
        if parents != [commit, base]:
            raise PipelineFailure("commit_parent_mismatch")
        changed = (
            self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "-z", commit)
            .decode()
            .rstrip("\0")
            .split("\0")
        )
        if set(changed) != set(files) or len(changed) != len(files):
            raise PipelineFailure("commit_file_scope_mismatch")
        for path, sha in files.items():
            if hashlib.sha256(self.git("show", f"{commit}:{path}")).hexdigest() != sha:
                raise PipelineFailure("commit_content_mismatch")
            mode = self.git("ls-tree", commit, "--", path).decode().split()[0]
            expected_mode = (
                "100755"
                if self.spec["repository"] == REPOSITORIES["consumer"]
                and path == "download-corpus.sh"
                else "100644"
            )
            if mode != expected_mode:
                raise PipelineFailure("commit_file_type_mismatch")

    def head(self, ref):
        rows = self.git("ls-remote", "--refs", self.remote, ref).decode().splitlines()
        if len(rows) > 1:
            raise PipelineFailure("ambiguous_remote_ref")
        return rows[0].split()[0] if rows else None

    def push(self, ref, expected_before, journal):
        if ref not in {"refs/heads/main", "refs/tags/v1.2.0"}:
            raise PipelineFailure("unapproved_ref")
        if self.head(ref) != expected_before:
            raise PipelineFailure("remote_ref_requires_review")
        self.before_write()
        record(
            journal,
            {
                "operation": "git_push",
                "repository": self.spec["repository"],
                "ref": ref,
                "commit": self.spec["commit"],
                "state": "intent",
            },
        )
        self.git(
            "push",
            "--porcelain",
            self.remote,
            f"{self.spec['commit']}:{ref}",
            external_write=True,
        )
        if self.head(ref) != self.spec["commit"]:
            raise OutcomeUnknown("remote ref verification requires reconciliation")
        record(
            journal,
            {
                "operation": "git_push",
                "ref": ref,
                "commit": self.spec["commit"],
                "state": "verified",
            },
        )
        return self.spec["commit"]


class PreparedPublication:
    def __init__(self, plan, candidate, operator, consumer, publisher, journal):
        self.plan, self.candidate = plan, Path(candidate)
        self.operator, self.consumer, self.publisher, self.journal = (
            operator,
            consumer,
            publisher,
            Path(journal),
        )

    def validate(self):
        from .publication_selection import six_files

        if self.plan["version"] != "v1.2.0" or self.plan["scope"] != "community-brain":
            raise PipelineFailure("unapproved_publication")
        if set(self.plan["artifacts"]) != six_files(self.plan["local_date"]):
            raise PipelineFailure("six_artifacts_required")
        files = {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in self.candidate.iterdir()
            if p.is_file() and not p.is_symlink()
        }
        if files != self.plan["assets"] or len(list(self.candidate.iterdir())) != 3:
            raise PipelineFailure("candidate_assets_changed")
        manifest = validate_bundle(self.candidate)
        if (
            manifest["corpus_version"] != self.plan["version"]
            or manifest["session_count"] != 88
            or manifest["chunk_count"] != 1924
        ):
            raise PipelineFailure("candidate_identity_changed")
        for git, key in [(self.operator, "operator"), (self.consumer, "consumer")]:
            if (
                git.spec != self.plan[key]
                or git.spec["repository"] != REPOSITORIES[key]
            ):
                raise PipelineFailure("destination_changed")
        if (
            self.publisher.repository != self.plan["consumer"]["repository"]
            or self.publisher.commit != self.plan["consumer"]["commit"]
        ):
            raise PipelineFailure("release_target_changed")
        self.operator.validate(
            {
                "output/" + self.plan["local_date"] + "/" + name: sha
                for name, sha in self.plan["artifacts"].items()
            }
        )
        self.consumer.validate({"download-corpus.sh": self.plan["installer_sha256"]})

    def git(self, job_id):
        if str(job_id) != self.plan["job_id"]:
            raise PipelineFailure("unselected_job")
        self.validate()
        commit = self.operator.push(
            "refs/heads/main", self.plan["operator"]["base"], self.journal
        )
        return {
            "commit": commit,
            "artifact_hashes": self.plan["artifacts"],
            "plan_sha256": fingerprint(self.plan),
        }

    def distribution(self, job_id):
        if str(job_id) != self.plan["job_id"]:
            raise PipelineFailure("unselected_job")
        self.validate()
        if (
            self.operator.head("refs/heads/main") != self.plan["operator"]["commit"]
            or self.consumer.head("refs/heads/main") != self.plan["consumer"]["base"]
        ):
            raise PipelineFailure("remote_ref_requires_review")
        # Make the approved pin commit reachable by the release tag first. main
        # keeps its old working installer until the new assets are verified live.
        self.consumer.push("refs/tags/" + self.plan["version"], None, self.journal)
        record(
            self.journal,
            {
                "operation": "release",
                "version": self.plan["version"],
                "state": "intent",
            },
        )
        receipt = self.publisher.publish(self.candidate, self.plan["version"])
        record(
            self.journal,
            {"operation": "release", "state": "verified", "receipt": receipt},
        )
        commit = self.consumer.push(
            "refs/heads/main", self.plan["consumer"]["base"], self.journal
        )
        return {
            "version": self.plan["version"],
            "sha256": self.plan["assets"]["corpus-v1.2.0.tar.gz"],
            "commit": commit,
            "receipt": receipt,
            "plan_sha256": fingerprint(self.plan),
        }

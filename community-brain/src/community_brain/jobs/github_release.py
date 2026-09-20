"""Draft-first GitHub release adapter. Transport is mocked in development tests."""

from pathlib import Path
import re

import httpx

from community_brain.processing.pipeline import OutcomeUnknown, PipelineFailure
from .storage import digest


class GitHubRelease:
    def __init__(self, repository, commit, token, transport=None, *, tag_verifier=None):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise ValueError("invalid repository")
        if not re.fullmatch(r"[0-9a-f]{40}", commit):
            raise ValueError("pin distribution source commit")
        self.repository, self.commit = repository, commit
        self.tag_verifier = tag_verifier
        self.client = httpx.Client(
            headers={
                "Authorization": "Bearer " + token,
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2026-03-10",
            },
            timeout=60,
            follow_redirects=False,
            transport=transport,
        )

    def close(self):
        self.client.close()

    def matches_target(self, release, version):
        # GitHub ignores target_commitish when the tag already exists. For the
        # pre-tagged publisher, validate the actual immutable tag commit instead.
        return release.get("tag_name") == version and (
            self.tag_verifier(version) == self.commit
            if self.tag_verifier is not None
            else release.get("target_commitish") == self.commit
        )

    def publish(self, directory, version):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", version):
            raise ValueError("invalid release version")
        # Complete local allowlist checks before even creating a remote draft.
        entries = list(Path(directory).iterdir())
        if any(p.is_symlink() or not p.is_file() for p in entries):
            raise PipelineFailure("invalid_release_assets")
        expected = {p.name: p.read_bytes() for p in entries}
        if set(expected) != {
            f"corpus-{version}.tar.gz",
            "corpus-manifest.json",
            "sha256sum.txt",
        }:
            raise PipelineFailure("invalid_release_assets")
        api = "https://api.github.com/repos/" + self.repository + "/releases"
        try:
            response = self.client.get(api + "/tags/" + version)
            if response.status_code == 404:
                # A draft may not have a materialized tag yet. Reconcile drafts
                # before creating another release after a lost create response.
                draft = None
                for page in range(1, 101):
                    listed = self.client.get(
                        api, params={"per_page": 100, "page": page}
                    )
                    listed.raise_for_status()
                    items = listed.json()
                    draft = next(
                        (r for r in items if r.get("tag_name") == version), None
                    )
                    if draft or len(items) < 100:
                        break
                else:
                    raise PipelineFailure("release_listing_limit")
                if draft:
                    response = self.client.get(api + "/" + str(draft["id"]))
                else:
                    response = self.client.post(
                        api,
                        json={
                            "tag_name": version,
                            "target_commitish": self.commit,
                            "name": version,
                            "draft": True,
                            "generate_release_notes": False,
                        },
                    )
            response.raise_for_status()
            release = response.json()
            identity = release["id"]
            if not self.matches_target(release, version):
                raise PipelineFailure("release_commit_conflict")
            assets = {a["name"]: a for a in release.get("assets", [])}
            if set(assets) - set(expected):
                raise PipelineFailure("release_asset_conflict")
            for name, content in expected.items():
                sha = "sha256:" + digest(content)
                asset = assets.get(name)
                if asset:
                    if asset.get("digest") != sha:
                        raise PipelineFailure("release_asset_conflict")
                else:
                    if not release["draft"]:
                        raise PipelineFailure("published_release_incomplete")
                    response = self.client.post(
                        f"https://uploads.github.com/repos/{self.repository}/releases/{identity}/assets",
                        params={"name": name},
                        content=content,
                        headers={"Content-Type": "application/octet-stream"},
                    )
                    response.raise_for_status()
                    asset = response.json()
                    if asset.get("digest") != sha:
                        raise PipelineFailure("release_asset_checksum_mismatch")
                assets[name] = asset
            if release["draft"]:
                response = self.client.patch(
                    f"{api}/{identity}", json={"draft": False, "make_latest": "true"}
                )
                response.raise_for_status()
            response = self.client.get(f"{api}/{identity}")
            response.raise_for_status()
            verified = response.json()
            if (
                verified.get("id") != identity
                or verified.get("tag_name") != version
                or not self.matches_target(verified, version)
                or verified.get("draft") is not False
            ):
                raise OutcomeUnknown(
                    "published release identity requires reconciliation"
                )
            verified_assets = verified.get("assets", [])
            actual = {a["name"]: a.get("digest") for a in verified_assets}
            if len(actual) != len(verified_assets) or actual != {
                name: "sha256:" + digest(content) for name, content in expected.items()
            }:
                raise OutcomeUnknown("published release assets require reconciliation")
            return {
                "release_id": identity,
                "tag": version,
                "commit": self.commit,
                "assets": {name: a["digest"] for name, a in assets.items()},
            }
        except httpx.HTTPError as exc:
            raise OutcomeUnknown(
                "release outcome requires receipt reconciliation"
            ) from exc

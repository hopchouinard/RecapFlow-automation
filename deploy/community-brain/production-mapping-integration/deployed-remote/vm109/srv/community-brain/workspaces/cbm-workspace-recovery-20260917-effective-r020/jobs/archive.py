"""Read-only preserved meeting files; never creates jobs or indexes content."""

import hashlib
import json
import re
from pathlib import Path

from fastapi import Depends, HTTPException
from fastapi.responses import Response


class MeetingArchive:
    def __init__(self, root, expected_hash):
        self.root = Path(root)
        raw = (self.root / "manifest.json").read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected_hash:
            raise ValueError("archive manifest mismatch")
        manifest = json.loads(raw)
        self.scope = manifest["scope"]
        self.meetings = manifest["meetings"]
        self.files = {}
        dates = set()
        for meeting in self.meetings:
            date = meeting["date"]
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date) or date in dates:
                raise ValueError("invalid archive meeting")
            dates.add(date)
            for artifact in meeting["artifacts"]:
                key = artifact["id"]
                if not re.fullmatch(r"[a-f0-9]{64}", key) or key in self.files:
                    raise ValueError("invalid archive file")
                if not re.fullmatch(r"[A-Za-z0-9_.-]+", artifact["name"]):
                    raise ValueError("invalid archive filename")
                self.files[key] = artifact

    def read(self, key):
        if key not in self.files:
            raise KeyError(key)
        path = self.root / "files" / key
        if (
            path.is_symlink()
            or path.resolve().parent != (self.root / "files").resolve()
        ):
            raise ValueError("unsafe archive path")
        data = path.read_bytes()
        meta = self.files[key]
        if (
            len(data) != meta["bytes"]
            or hashlib.sha256(data).hexdigest() != meta["sha256"]
        ):
            raise ValueError("archive file mismatch")
        return data


def register_archive(app, permission, archive, store=None, hidden_jobs=()):
    def check(principal):
        if archive is None:
            raise HTTPException(503, "archive_unavailable")
        if principal.scope != archive.scope:
            raise HTTPException(404, "not_found")

    @app.get("/api/v1/meetings")
    def meetings(p=Depends(permission("jobs:read"))):
        check(p)
        items = {m["date"]: m for m in archive.meetings}
        if store is not None and hasattr(store, "engine"):
            from sqlalchemy import select
            from sqlalchemy.orm import Session
            from .automatic import POLICY
            from .models import Artifact, Job

            with Session(store.engine) as session:
                jobs = session.scalars(
                    select(Job).where(
                        Job.scope == p.scope,
                        Job.id.not_in(hidden_jobs),
                        Job.parent_id.is_(None),
                        Job.artifacts == "ready",
                        Job.config["automation_policy"].astext == POLICY,
                    )
                ).all()
                for job in jobs:
                    date = job.identity["local_date"]
                    if date in items:
                        continue
                    artifacts = session.scalars(
                        select(Artifact).where(Artifact.job_id == job.id)
                    ).all()
                    items[date] = {
                        "date": date,
                        "source": "processed",
                        "indexing": job.indexing,
                        "artifacts": [
                            {
                                "id": str(a.id),
                                "name": a.name,
                                "origin": "output",
                                "bytes": a.size,
                                "sha256": a.sha256,
                                "url": f"/api/v1/artifacts/{a.id}/content",
                            }
                            for a in sorted(artifacts, key=lambda a: a.name)
                        ],
                    }
        return {"items": [items[d] for d in sorted(items, reverse=True)]}

    @app.get("/api/v1/meeting-artifacts/{key}/content")
    def content(key: str, p=Depends(permission("artifacts:read"))):
        check(p)
        try:
            data = archive.read(key)
        except KeyError:
            raise HTTPException(404, "not_found")
        except (OSError, ValueError):
            raise HTTPException(409, "artifact_corrupt")
        artifact = archive.files[key]
        return Response(
            data,
            media_type="text/plain",
            headers={
                "ETag": '"' + artifact["sha256"] + '"',
                "Content-Disposition": f'attachment; filename="{artifact["name"]}"',
                "X-Content-Type-Options": "nosniff",
                "Cache-Control": "private, no-store",
            },
        )

"""Explicit application entrypoints. No migrations, provisioning or dotenv loads."""

import asyncio
from contextlib import asynccontextmanager
import json
import os
from pathlib import Path

from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine

from .api import create_app
from .auth import Authenticator
from .acquisition import Fathom
from .publication import PublicationHandlers
from .github_release import GitHubRelease
from .storage import Storage
from .store import Store
from .worker import OpenRouter, Worker, serve


def required(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} must be explicitly configured")
    return value


def make_store():
    from community_brain.ingestion.registries import (
        load_speaker_registry,
        render_alias_block,
    )

    config = Path(required("CB_PIPELINE_CONFIG_DIR"))

    def indexed_date(date):
        from datetime import date as Date
        import lancedb

        value = Date.fromisoformat(str(date)).isoformat()
        corpus = Path(required("CB_CORPUS_ROOT"))
        if (corpus / "sessions" / f"{value}.json").exists():
            return True
        table = lancedb.connect(str(corpus / "lancedb/nomic-v1")).open_table("chunks")
        return table.count_rows(f"session_id = '{value}'") > 0

    return Store(
        create_engine(required("CB_DATABASE_URL"), pool_pre_ping=True),
        Storage(required("CB_STORAGE_ROOT")),
        indexed_date=indexed_date,
        aliases_supplier=lambda: render_alias_block(
            load_speaker_registry(config / "speaker-aliases.yaml")
        ),
    )


class ProtectedRetrieval:
    def __init__(self, app, authenticate, scope):
        self.app, self.authenticate, self.scope = app, authenticate, scope

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        headers = dict(scope.get("headers", []))
        token = headers.get(b"authorization", b"").decode()
        if not token and headers.get(b"x-api-key"):
            # Preserve the existing Open WebUI filter's transport. Only its URL
            # and independently scoped credential need changing at cutover.
            token = "Bearer " + headers[b"x-api-key"].decode()
        try:
            if not token.startswith("Bearer "):
                raise ValueError()
            principal = await asyncio.to_thread(self.authenticate, token[7:])
            if (
                principal.scope != self.scope
                or "retrieval:read" not in principal.permissions
            ):
                raise ValueError()
        except Exception:
            await JSONResponse({"code": "unauthenticated"}, status_code=401)(
                scope, receive, send
            )
            return
        # Mutating ingestion/reindexing stays with the single corpus writer.
        route = scope["path"].removeprefix(scope.get("root_path", ""))
        allowed = (scope["method"], route) in {
            ("POST", "/query"),
            ("GET", "/sessions"),
            ("GET", "/health"),
            ("GET", "/speaker-aliases-block"),
        }
        allowed = allowed or (
            scope["method"] == "GET" and route.startswith("/sessions/")
        )
        if not allowed:
            await JSONResponse({"code": "not_found"}, status_code=404)(
                scope, receive, send
            )
            return
        await self.app(scope, receive, send)


class SPA(StaticFiles):
    async def get_response(self, path, scope):
        if path == "callback":
            path = "index.html"
        return await super().get_response(path, scope)


def app():
    verifier = Authenticator(
        required("CB_OIDC_ISSUER"),
        required("CB_OIDC_AUDIENCE"),
        required("CB_OIDC_JWKS_URL"),
        json.loads(os.environ.get("CB_SERVICE_IDENTITIES") or "[]"),
    )
    corpus_scope = required("CB_CORPUS_SCOPE")

    def authenticate(token):
        principal = verifier(token)
        if principal.scope != corpus_scope:
            raise ValueError("incorrect application scope")
        return principal

    from .archive import MeetingArchive

    archive = None
    if os.environ.get("CB_MEETING_ARCHIVE_ROOT"):
        archive = MeetingArchive(
            required("CB_MEETING_ARCHIVE_ROOT"), required("CB_MEETING_ARCHIVE_SHA256")
        )
    application = create_app(
        make_store(),
        authenticate,
        archive=archive,
        hidden_jobs=json.loads(os.environ.get("CB_HIDDEN_JOB_IDS") or "[]"),
        automatic=os.environ.get("CB_AUTOMATIC_PROCESSING") == "true",
        automation_root=os.environ.get("CB_AUTOMATION_ROOT"),
    )

    @application.get("/auth-config.json")
    def auth_config():
        return {
            "authority": required("CB_OIDC_ISSUER"),
            "client_id": required("CB_OIDC_CLIENT_ID"),
        }

    if os.environ.get("CB_ENABLE_RETRIEVAL") == "true":
        required("LANCEDB_PATH")
        if os.environ.get("COMMUNITY_BRAIN_DISTRIBUTION_MODE") != "true":
            raise RuntimeError(
                "API retrieval must use the existing read-only serving mode"
            )
        # The existing retrieval module remains the behavior oracle. Mount only
        # its existing read surfaces under the new authenticated boundary.
        from community_brain.query.retrieval_server import app as retrieval

        @asynccontextmanager
        async def lifespan(application):
            async with retrieval.router.lifespan_context(retrieval):
                yield

        application.router.lifespan_context = lifespan
        application.mount(
            "/retrieval",
            ProtectedRetrieval(retrieval, authenticate, required("CB_CORPUS_SCOPE")),
        )
    if os.environ.get("CB_WEB_DIST"):
        application.mount("/", SPA(directory=required("CB_WEB_DIST"), html=True))
    return application


def main():
    if os.environ.get("CB_ENABLE_MODEL_CALLS") != "true":
        raise RuntimeError("Worker model calls require explicit runtime enablement")
    store = make_store()
    # Existing ingestion code reads this name; both are delivered by Infisical.
    os.environ["OPENROUTER_API_KEY"] = required("CB_OPENROUTER_API_KEY")
    publisher = None
    if os.environ.get("CB_ENABLE_NETWORK_PUBLICATION") == "true":
        publisher = GitHubRelease(
            required("CB_DISTRIBUTION_REPO"),
            required("CB_DISTRIBUTION_COMMIT"),
            required("CB_GITHUB_TOKEN"),
        )
    handlers = PublicationHandlers(
        store,
        required("CB_CORPUS_ROOT"),
        required("CB_PIPELINE_CONFIG_DIR"),
        required("OLLAMA_BASE_URL"),
        os.environ.get("CB_GIT_REMOTE"),
        os.environ.get("CB_ENABLE_NETWORK_PUBLICATION") == "true",
        publisher,
    )
    fathom_key = os.environ.get("CB_FATHOM_API_KEY")
    fathom = Fathom(fathom_key) if fathom_key else None
    worker = Worker(
        store,
        OpenRouter(required("CB_OPENROUTER_API_KEY")),
        handlers={
            name: getattr(handlers, name)
            for name in ("indexing", "git", "distribution")
        },
        fathom=fathom,
    )
    try:
        asyncio.run(
            serve(
                store,
                worker,
                required("CB_NATS_URL"),
                required("CB_NATS_STREAM"),
                required("CB_NATS_SUBJECT"),
            )
        )
    finally:
        if fathom:
            fathom.close()
        if publisher:
            publisher.close()


if __name__ == "__main__":
    main()

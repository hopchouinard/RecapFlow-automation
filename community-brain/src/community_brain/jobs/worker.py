import asyncio
import json
from uuid import UUID, uuid4

import httpx
import nats
from sqlalchemy import select
from sqlalchemy.orm import Session

from community_brain.processing.pipeline import (
    SNAPSHOT,
    Pipeline,
    PipelineFailure,
    OutcomeUnknown,
    classify,
)
from .models import Artifact, Job, ModelCall, Outbox, RejectedEvent, Source, Stage
from .store import fingerprint


class OpenRouter:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("OpenRouter credential required")
        self.api_key = api_key

    def __call__(self, request):
        payload = {
            "model": request["model"],
            "messages": [
                {"role": "system", "content": request["system"]},
                {"role": "user", "content": request["user"]},
            ],
            "max_tokens": request["maxTokens"],
            "temperature": request["temperature"],
        }
        if request.get("reasoningEffort"):
            payload["reasoning"] = {"effort": request["reasoningEffort"]}
        try:
            response = httpx.post(
                "https://openrouter.ai/api/v1/chat/completions",
                json=payload,
                headers={"Authorization": "Bearer " + self.api_key},
                timeout=httpx.Timeout(180, connect=10),
            )
            response.raise_for_status()
            return response.json()
        except (httpx.HTTPError, ValueError) as exc:
            raise OutcomeUnknown("provider outcome requires reconciliation") from exc


class Worker:
    def __init__(self, store, transport, handlers=None, fathom=None):
        self.store = store
        self.transport = transport
        self.handlers = handlers or {}
        self.owner = uuid4().hex
        self.fathom = fathom

    def execute(self, stage_id, fence):
        with Session(self.store.engine) as s:
            stage = s.get(Stage, stage_id)
            job = s.get(Job, stage.job_id)
            job_id = job.id
            mode = job.mode
            config = job.config
            identity = job.identity
            source_records = [
                s.get(Source, UUID(value)) for value in job.sources.values()
            ]
            sources = {
                r.kind: self.store.storage.read(r.path, r.sha256).decode("utf-8")
                for r in source_records
            }

        def call(request):
            key = fingerprint(request)
            with Session(self.store.engine) as s, s.begin():
                self.store.owned(s, stage_id, fence, self.owner)
                previous = s.scalar(
                    select(ModelCall).where(
                        ModelCall.job_id == job_id, ModelCall.key == key
                    )
                )
                if previous:
                    if previous.state == "intent":
                        raise OutcomeUnknown("unresolved model intent")
                    return json.loads(
                        self.store.storage.read(
                            previous.response_path, previous.response_hash
                        )
                    )
                model_call = ModelCall(
                    job_id=job_id,
                    key=key,
                    fence=fence,
                    request_meta={
                        "step": request["stepName"],
                        "model": request["model"],
                        "prompt_hash": fingerprint(request["system"]),
                        "request_hash": key,
                        "max_tokens": request["maxTokens"],
                        "attempt": request["attempt"],
                    },
                )
                s.add(model_call)
                s.flush()
                call_id = model_call.id
            body = self.transport(request)
            path, sha, _ = self.store.storage.put(json.dumps(body).encode())
            with Session(self.store.engine) as s, s.begin():
                self.store.owned(s, stage_id, fence, self.owner)
                model_call = s.get(ModelCall, call_id)
                model_call.state = (
                    "succeeded" if classify(request, body)["ok"] else "failed"
                )
                model_call.response_path = path
                model_call.response_hash = sha
                # Missing provider usage stays unknown, not zero.
                model_call.usage = body.get("usage")
            return body

        def emit(name, content):
            data = content.encode()
            with Session(self.store.engine) as s, s.begin():
                self.store.owned(s, stage_id, fence, self.owner)
                previous = s.scalar(
                    select(Artifact).where(
                        Artifact.job_id == job_id, Artifact.name == name
                    )
                )
                if previous:
                    if self.store.storage.read(previous.path, previous.sha256) != data:
                        raise PipelineFailure("immutable_artifact_conflict")
                    return
            path, sha, size = self.store.storage.put(data)
            with Session(self.store.engine) as s, s.begin():
                self.store.owned(s, stage_id, fence, self.owner)
                s.add(
                    Artifact(
                        job_id=job_id,
                        stage_id=stage_id,
                        fence=fence,
                        name=name,
                        path=path,
                        sha256=sha,
                        size=size,
                    )
                )
                s.get(Job, job_id).artifacts = "partial"

        try:
            if stage.name == "acquisition":
                if self.fathom is None:
                    raise PipelineFailure("fathom_not_configured")
                try:
                    transcript = self.fathom.fetch(identity)
                except httpx.HTTPStatusError as exc:
                    code = {
                        401: "fathom_authentication_failed",
                        403: "fathom_access_denied",
                        404: "fathom_transcript_unavailable",
                        429: "fathom_rate_limited",
                    }.get(exc.response.status_code, "fathom_unavailable")
                    raise PipelineFailure(code) from None
                except httpx.HTTPError:
                    raise PipelineFailure("fathom_unavailable") from None
                except ValueError as exc:
                    messages = {
                        "recording not found in meeting window": "fathom_recording_not_found",
                        "meeting timestamp mismatch: outside 10-minute window": "fathom_time_mismatch",
                        "transcript unavailable": "fathom_transcript_unavailable",
                        "metadata page ceiling reached": "fathom_lookup_limit",
                    }
                    raise PipelineFailure(
                        messages.get(str(exc), "fathom_invalid_response")
                    ) from None
                with Session(self.store.engine) as s, s.begin():
                    self.store.owned(s, stage_id, fence, self.owner)
                source_id = self.store.add_source(
                    job.scope, identity["meeting_id"], "transcript", transcript
                )
                self.store.bind_sources(
                    job.scope,
                    job_id,
                    {"transcript": source_id},
                    acquisition_owner=(fence, self.owner),
                )
                result = {"source_id": source_id}
            elif stage.name == "processing":
                if config.get("prompt_snapshot_sha256") != fingerprint(
                    SNAPSHOT[mode]["prompts"]
                ):
                    raise PipelineFailure("pipeline_version_mismatch")
                Pipeline(mode, config).run(
                    sources["transcript"],
                    identity["local_date"],
                    call,
                    chat=sources.get("chat", ""),
                    aliases=sources.get("aliases", ""),
                    emit=emit,
                )
                result = None
            else:
                handler = self.handlers.get(stage.name)
                if handler is None:
                    raise PipelineFailure("stage_adapter_not_configured")
                result = handler(job_id)
                if result.get("state") == "partial":
                    self.store.finish(
                        stage_id,
                        fence,
                        self.owner,
                        "partial",
                        "indexing_partial",
                        result,
                    )
                    return
            self.store.finish(stage_id, fence, self.owner, result=result)
        except OutcomeUnknown:
            self.store.finish(
                stage_id, fence, self.owner, "outcome_unknown", "outcome_unknown"
            )
        except PipelineFailure as exc:
            allowed = {
                "fathom_not_configured",
                "fathom_authentication_failed",
                "fathom_access_denied",
                "fathom_transcript_unavailable",
                "fathom_rate_limited",
                "fathom_unavailable",
                "fathom_recording_not_found",
                "fathom_time_mismatch",
                "fathom_lookup_limit",
                "fathom_invalid_response",
            }
            code = str(exc) if str(exc) in allowed else "pipeline_failed"
            self.store.finish(stage_id, fence, self.owner, "failed", code)

    async def handle(self, message):
        async def reject():
            from sqlalchemy.dialects.postgresql import insert
            from .storage import digest

            with Session(self.store.engine) as s, s.begin():
                s.execute(
                    insert(RejectedEvent)
                    .values(sha256=digest(message.data), reason="invalid_envelope")
                    .on_conflict_do_nothing()
                )
            await message.term()

        try:
            if len(message.data) > 4096:
                raise ValueError("oversized event")
            envelope = json.loads(message.data)
            if set(envelope) != {
                "schema_version",
                "event_id",
                "stage_id",
                "generation",
                "job_id",
                "occurred_at",
                "trace_id",
            }:
                raise ValueError("invalid event schema")
            if envelope.get("schema_version") != 1:
                raise ValueError("unsupported event")
            stage_id = UUID(envelope["stage_id"])
            event_id = UUID(envelope["event_id"])
            job_id = UUID(envelope["job_id"])
            if type(envelope["generation"]) is not int or envelope["generation"] < 1:
                raise ValueError()
        except (ValueError, KeyError, TypeError):
            await reject()
            return
        with Session(self.store.engine) as s:
            event = s.get(Outbox, event_id)
            stage = s.get(Stage, stage_id)
            if (
                not stage
                or stage.job_id != job_id
                or not event
                or event.stage_id != stage_id
                or event.generation != envelope.get("generation")
            ):
                await reject()
                return
        fence = await asyncio.to_thread(
            self.store.claim, stage_id, self.owner, envelope["generation"]
        )
        if fence is None:
            with Session(self.store.engine) as s:
                stage = s.get(Stage, stage_id)
                terminal = stage is not None and stage.state in (
                    "succeeded",
                    "failed",
                    "partial",
                    "outcome_unknown",
                )
            if terminal:
                await message.ack_sync()
            else:
                await message.nak(delay=30)
            return
        task = asyncio.create_task(asyncio.to_thread(self.execute, stage_id, fence))
        try:
            while not task.done():
                done, _ = await asyncio.wait([task], timeout=15)
                if done:
                    break
                await asyncio.to_thread(
                    self.store.heartbeat, stage_id, fence, self.owner
                )
                await message.in_progress()
            await task
            await message.ack_sync()
        except Exception:
            # A failed DB write or lost lease cannot be acknowledged as success.
            # The thread's next owned() check fences further calls and promotion.
            await message.nak(delay=60)
            if not task.done():
                await task


async def dispatch(store, js, subject):
    with Session(store.engine) as s:
        events = s.scalars(
            select(Outbox)
            .where(Outbox.sent_at.is_(None))
            .order_by(Outbox.created_at)
            .limit(100)
        ).all()
        for event in events:
            stage = s.get(Stage, event.stage_id)
            body = {
                "schema_version": 1,
                "event_id": str(event.id),
                "stage_id": str(event.stage_id),
                "generation": event.generation,
                "job_id": str(stage.job_id),
                "occurred_at": event.created_at.isoformat(),
                "trace_id": str(event.id),
            }
            await js.publish(
                subject,
                json.dumps(body).encode(),
                headers={"Nats-Msg-Id": str(event.id)},
            )
            with Session(store.engine) as tx, tx.begin():
                tx.get(Outbox, event.id).sent_at = store.now(tx)


async def serve(store, worker, nats_url, stream, subject):
    nc = await nats.connect(nats_url)
    try:
        js = nc.jetstream()
        # Stream/resource creation belongs to explicit provisioning, not startup.
        subscription = await js.pull_subscribe_bind(
            "community-brain-worker", stream=stream
        )
        while True:
            await asyncio.to_thread(store.recover)
            await dispatch(store, js, subject)
            try:
                messages = await subscription.fetch(1, timeout=2)
            except nats.errors.TimeoutError:
                continue
            for message in messages:
                await worker.handle(message)
    finally:
        await nc.close()

"""One selected Fathom acquisition. No scheduler, models or publication handlers."""

import asyncio
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse
from uuid import UUID

import nats
from community_brain.jobs.acquisition import Fathom
from community_brain.jobs.models import Job, ModelCall, Outbox, Source, Stage
from community_brain.jobs.runtime import make_store
from community_brain.jobs.worker import Worker, dispatch
from sqlalchemy import select
from sqlalchemy.orm import Session


class SelectedFathom(Fathom):
    def __init__(self, key, recording, started_at, transport=None):
        super().__init__(key, transport)
        if not recording.isdecimal():
            raise ValueError("Select a numeric recording ID")
        self.recording, self.started_at = recording, started_at
        self.lookup_count = 0
        self.transcript_count = 0
        self.client.event_hooks["request"] = [self.guard]

    def guard(self, request):
        if (
            request.method != "GET"
            or request.url.scheme != "https"
            or request.url.host != "api.fathom.ai"
        ):
            raise ValueError("Fathom rehearsal permits only selected read operations")
        if request.url.path == "/external/v1/meetings":
            self.lookup_count += 1
            if self.lookup_count > 5:
                raise ValueError("Narrow lookup page limit reached; review selection")
            request.url = request.url.copy_merge_params(
                {
                    "include_transcript": "false",
                    "include_summary": "false",
                    "include_action_items": "false",
                    "include_highlights": "false",
                    "include_crm_matches": "false",
                }
            )
        elif request.url.path == f"/external/v1/recordings/{self.recording}/transcript":
            self.transcript_count += 1
            if self.transcript_count > 1:
                raise ValueError("No repeated transcript fetch in this rehearsal")
        else:
            raise ValueError("Unselected Fathom operation")

    def fetch(self, identity):
        if (
            identity["meeting_id"] != self.recording
            or identity["started_at"] != self.started_at
        ):
            raise ValueError("Job does not match the selected recording/time")
        return super().fetch(identity)


def lookup_selected(recording, after, before, transport=None):
    start = datetime.fromisoformat(after.replace("Z", "+00:00"))
    end = datetime.fromisoformat(before.replace("Z", "+00:00"))
    if (
        not start.tzinfo
        or not end.tzinfo
        or not timedelta(0) < end - start <= timedelta(days=3)
    ):
        raise ValueError(
            "Metadata lookup requires an explicit window of at most three days"
        )
    client = SelectedFathom(os.environ["CB_FATHOM_API_KEY"], recording, "", transport)
    try:
        params = {"created_after": start.isoformat(), "created_before": end.isoformat()}
        seen = set()
        for _ in range(5):
            response = client.client.get("meetings", params=params)
            response.raise_for_status()
            result = response.json()
            for item in result.get("items", []):
                meeting_url = urlparse(item.get("url") or "")
                matches_url = (
                    meeting_url.hostname == "fathom.video"
                    and meeting_url.path.rstrip("/") == "/calls/" + recording
                )
                if str(item.get("recording_id")) == recording or matches_url:
                    recorded = datetime.fromisoformat(
                        item["recording_start_time"].replace("Z", "+00:00")
                    )
                    if not recorded.tzinfo:
                        raise ValueError("Recording timestamp lacks timezone")
                    return {
                        "recording_id": str(item["recording_id"]),
                        "selected_call_url": "https://fathom.video/calls/" + recording,
                        "started_at": recorded.astimezone(timezone.utc)
                        .isoformat()
                        .replace("+00:00", "Z"),
                        "title": item.get("title"),
                        "recording_end_time": item.get("recording_end_time"),
                        "metadata_only": True,
                    }
            cursor = result.get("next_cursor")
            if not cursor:
                break
            if cursor in seen:
                raise ValueError("Metadata pagination cycle")
            seen.add(cursor)
            params["cursor"] = cursor
        raise ValueError("Selected recording not found in the approved narrow window")
    finally:
        client.close()


def terminal_duplicate(stage, outbox, event):
    return bool(
        stage
        and outbox
        and stage.state in ("succeeded", "failed", "partial", "outcome_unknown")
        and str(stage.job_id) == event["job_id"]
        and outbox.stage_id == stage.id
        and outbox.generation == event["generation"]
        and event["schema_version"] == 1
    )


def deny_models(request):
    raise RuntimeError("Model processing of this recording is not authorized")


async def main():
    job_id, recording, started_at = UUID(sys.argv[1]), sys.argv[2], sys.argv[3]
    assert os.environ["CB_ENABLE_MODEL_CALLS"] == "false"
    assert os.environ["CB_ENABLE_NETWORK_PUBLICATION"] == "false"
    assert not os.environ.get("CB_OPENROUTER_API_KEY")
    store = make_store()
    with Session(store.engine) as session:
        job = session.get(Job, job_id)
        assert (
            job.scope == "community-brain-dev" and job.identity["provider"] == "fathom"
        )
        assert (
            job.identity["meeting_id"] == recording
            and job.identity["started_at"] == started_at
        )
        # Missing chat keeps processing waiting even after transcript binding.
        assert (
            job.mode == "weekly"
            and not job.sources.get("chat")
            and not job.sources.get("transcript")
        )
        stage = session.scalar(
            select(Stage).where(Stage.job_id == job_id, Stage.name == "acquisition")
        )
        assert stage.state == "queued" and stage.attempts == 0
        stage_id = stage.id
    fathom = SelectedFathom(os.environ["CB_FATHOM_API_KEY"], recording, started_at)
    connection = None
    try:
        worker = Worker(store, deny_models, fathom=fathom)
        connection = await nats.connect(os.environ["CB_NATS_URL"])
        js = connection.jetstream()
        subscription = await js.pull_subscribe_bind(
            "community-brain-worker", stream="CB_DEV_JOBS"
        )
        await dispatch(store, js, "cb.dev.jobs")
        for _ in range(10):
            message = (await subscription.fetch(1, timeout=10))[0]
            event = json.loads(message.data)
            if event["job_id"] == str(job_id) and event["stage_id"] == str(stage_id):
                break
            with Session(store.engine) as session:
                previous = session.get(Stage, UUID(event["stage_id"]))
                outbox = session.get(Outbox, UUID(event["event_id"]))
                terminal = terminal_duplicate(previous, outbox, event)
            if not terminal:
                await message.nak(delay=60)
                raise RuntimeError("Unrelated active work; no acquisition started")
            await message.ack_sync()
        else:
            raise RuntimeError(
                "Duplicate notification limit reached; no acquisition started"
            )
        await worker.handle(message)
        with Session(store.engine) as session:
            stage = session.get(Stage, stage_id)
            job = session.get(Job, job_id)
            assert stage.state == "succeeded", (
                "Inspect acquisition state before any retry"
            )
            assert (
                session.scalar(select(ModelCall.id).where(ModelCall.job_id == job_id))
                is None
            )
            assert job.processing == "waiting_for_input"
            source = session.get(Source, UUID(job.sources["transcript"]))
            store.storage.read(source.path, source.sha256)
            print(
                json.dumps(
                    {
                        "job_id": str(job_id),
                        "recording_id": recording,
                        "started_at": started_at,
                        "identity_time_match": True,
                        "acquisition": stage.state,
                        "processing": job.processing,
                        "source_id": str(source.id),
                        "sha256": source.sha256,
                        "bytes": source.size,
                        "private_output_path": "/state/files/" + source.path,
                    },
                    sort_keys=True,
                )
            )
    finally:
        fathom.close()
        if connection:
            await connection.close()


if __name__ == "__main__":
    if sys.argv[1] == "--lookup":
        assert os.environ["CB_ENABLE_MODEL_CALLS"] == "false"
        assert os.environ["CB_ENABLE_NETWORK_PUBLICATION"] == "false"
        assert not os.environ.get("CB_OPENROUTER_API_KEY")
        print(
            json.dumps(
                lookup_selected(sys.argv[2], sys.argv[3], sys.argv[4]), sort_keys=True
            )
        )
    else:
        asyncio.run(main())

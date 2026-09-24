"""Disposable rehearsal entrypoints. Never included in the application image."""

import asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path
import sys
import subprocess
import time
from unittest.mock import patch

import nats
from nats.js.api import ConsumerConfig

from community_brain.jobs.publication import PublicationHandlers
from community_brain.jobs.runtime import make_store
from community_brain.jobs.worker import Worker, serve
from community_brain.processing.pipeline import CANON


ROOT = Path("/state")


def init():
    for name in ("files", "corpus", "config"):
        (ROOT / name).mkdir(parents=True, exist_ok=True)
    (ROOT / "corpus/lancedb/nomic-v1").mkdir(parents=True, exist_ok=True)
    config = ROOT / "config"
    (config / "chunking.yaml").write_text("""schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [0, 0, 0]
  inter_session_delay_seconds: 0
""")
    (config / "extraction-config.yaml").write_text("""session_themes:
  prompt_file: session-themes-v1.md
  model: fixture
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: fixture
""")
    (config / "speaker-aliases.yaml").write_text(
        'version: "fixture"\naliases:\n  Alex: [Alex]\npending: []\n'
    )
    (config / "entity-registry.yaml").write_text(
        'version: "fixture"\nentities: {}\npending: []\n'
    )
    prompts = config / "extraction-prompts"
    prompts.mkdir(exist_ok=True)
    (prompts / "session-themes-v1.md").write_text("Session fixture")
    (prompts / "chunk-extraction-v1.md").write_text("Chunk fixture")
    repository = ROOT / "corpus/artifacts.git"
    if not repository.exists():
        subprocess.run(
            ["git", "init", "--bare", str(repository)], check=True, capture_output=True
        )
    # Only the three private project volumes; no host directories are mounted.
    for path in [ROOT / n for n in ("files", "corpus", "config")] + list(
        ROOT.rglob("*")
    ):
        os.chown(path, 10001, 10001)


def model(request):
    if (
        "INTERRUPT_FIXTURE" in request["user"]
        and not (ROOT / "files/interrupted").exists()
    ):
        (ROOT / "files/interrupted").write_text("effect entered; kill worker now")
        time.sleep(120)
    if request["expect"] == "prep.chunk":
        content = (
            "<!--SEGMENT\ntopic: fixture recovery\nspeakers: Alex\nkeywords: fixture, recovery\nsummary: Testing durable recovery.\n-->\n"
            + "Alex explains fixture recovery and durable storage. " * 12
        )
    elif request["expect"].startswith("signal."):
        content = "\n\n".join(
            "## " + section + "\nFixture recovery uses durable storage."
            for section in CANON
        )
    else:
        content = "Fixture recovery uses durable storage. "
    return {"choices": [{"message": {"content": content}, "finish_reason": "stop"}]}


def chunk_metadata(*args, **kwargs):
    return json.dumps(
        {
            "entities": [],
            "speech_acts": ["explanation"],
            "stance": "neutral",
            "certainty": "asserted",
            "chunk_local_markers": [],
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            "topic_label": "Fixture recovery",
            "speakers_mentioned": [],
            "keywords": ["fixture", "recovery"],
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": True,
        }
    )


async def provision():
    nc = await nats.connect("nats://nats:4222")
    try:
        js = nc.jetstream()
        await js.add_stream(
            name="CBM_SCENARIO", subjects=["cbm.scenario"], max_bytes=67108864
        )
        await js.add_consumer(
            "CBM_SCENARIO",
            ConsumerConfig(
                durable_name="community-brain-worker",
                ack_policy="explicit",
                ack_wait=90,
                max_deliver=10,
                max_ack_pending=1,
                filter_subject="cbm.scenario",
            ),
        )
    finally:
        await nc.close()


def worker():
    store = make_store()
    handlers = PublicationHandlers(
        store,
        ROOT / "corpus",
        ROOT / "config",
        "http://embedding:11434",
        git_remote=str(ROOT / "corpus/artifacts.git"),
    )
    with (
        patch("community_brain.ingestion.extractor._call_llm", chunk_metadata),
        patch(
            "community_brain.ingestion.session_extractor._call_llm",
            lambda *a, **k: json.dumps({"themes": ["fixture recovery"]}),
        ),
    ):
        asyncio.run(
            serve(
                store,
                Worker(
                    store,
                    model,
                    handlers={
                        name: getattr(handlers, name)
                        for name in ("indexing", "git", "distribution")
                    },
                ),
                "nats://nats:4222",
                "CBM_SCENARIO",
                "cbm.scenario",
            )
        )


class Embedding(BaseHTTPRequestHandler):
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        inputs = body["input"]
        if isinstance(inputs, str):
            inputs = [inputs]
        data = json.dumps(
            {
                "model": "nomic-embed-text",
                "embeddings": [[1.0] + [0.0] * 767 for _ in inputs],
            }
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    operation = sys.argv[1]
    if operation == "init":
        init()
    elif operation == "provision":
        asyncio.run(provision())
    elif operation == "worker":
        worker()
    elif operation == "embedding":
        HTTPServer(("0.0.0.0", 11434), Embedding).serve_forever()
    else:
        raise SystemExit("unsupported fixture operation")

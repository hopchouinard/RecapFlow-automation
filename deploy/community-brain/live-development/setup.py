"""Initialize only isolated development volumes; never load corpus data."""

import asyncio
import json
import os
import sys
from pathlib import Path


def initialize():
    for name in ("files", "config", "corpus"):
        root = Path("/state") / name
        root.mkdir(parents=True, exist_ok=True)
        os.chown(root, 10001, 10001)
    aliases = Path("/state/config/speaker-aliases.yaml")
    if not aliases.exists():
        aliases.write_text(
            'version: "development-synthetic"\naliases:\n  Alex: [Alex]\npending: []\n'
        )
        os.chown(aliases, 10001, 10001)
    source = Path("/checks/ingestion-config")
    for original in source.rglob("*"):
        target = Path("/state/config") / original.relative_to(source)
        if original.is_dir():
            target.mkdir(exist_ok=True)
        elif target.exists():
            assert target.read_bytes() == original.read_bytes(), (
                "Development config drift requires review"
            )
        else:
            target.write_bytes(original.read_bytes())
        os.chown(target, 10001, 10001)
    entities = Path("/state/config/entity-registry.yaml")
    if not entities.exists():
        entities.write_text(
            'version: "development-synthetic"\nentities: {}\npending: []\n'
        )
        os.chown(entities, 10001, 10001)
    Path("/nats-config/server.conf").write_text(
        json.dumps(
            {
                "port": 4222,
                "jetstream": {"store_dir": "/data"},
                "authorization": {
                    "users": [
                        {
                            "user": "cbmdev",
                            "password": os.environ["CB_DEV_NATS_PASSWORD"],
                        }
                    ]
                },
            }
        )
    )
    os.chmod("/nats-config/server.conf", 0o644)


async def provision():
    import nats
    from nats.js.api import ConsumerConfig
    from nats.js.errors import NotFoundError

    nc = await nats.connect(os.environ["CB_NATS_URL"], connect_timeout=5)
    try:
        js = nc.jetstream()
        stream = {
            "name": "CB_DEV_JOBS",
            "subjects": ["cb.dev.jobs"],
            "max_bytes": 67108864,
        }
        try:
            await js.stream_info("CB_DEV_JOBS")
        except NotFoundError:
            await js.add_stream(**stream)
        else:
            await js.update_stream(**stream)
        await js.add_consumer(
            "CB_DEV_JOBS",
            ConsumerConfig(
                durable_name="community-brain-worker",
                ack_policy="explicit",
                filter_subject="cb.dev.jobs",
                ack_wait=120,
                max_deliver=10,
                max_ack_pending=1,
            ),
        )
        print("Development JetStream provisioned")
    finally:
        await nc.close()


if __name__ == "__main__":
    if sys.argv[1] == "initialize":
        initialize()
    elif sys.argv[1] == "provision":
        asyncio.run(provision())

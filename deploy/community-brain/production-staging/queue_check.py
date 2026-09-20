"""Connect and bind only: no fetch, dispatch, ACK or provider activity."""

import asyncio
import json
import os

import nats
from bounded_worker import STREAM, connection_options


async def main():
    nc = await nats.connect(**connection_options(os.environ))
    try:
        await nc.jetstream().pull_subscribe_bind(
            "community-brain-worker", stream=STREAM
        )
        await nc.flush(timeout=10)
        print(
            json.dumps(
                {
                    "tls_first_connection": True,
                    "scoped_inbox": True,
                    "existing_consumer_bound": True,
                    "messages_fetched": 0,
                    "messages_published": 0,
                }
            )
        )
    finally:
        await nc.close()


if __name__ == "__main__":
    asyncio.run(main())

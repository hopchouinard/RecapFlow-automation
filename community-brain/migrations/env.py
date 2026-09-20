"""Migrations are invoked explicitly, never by API or worker startup."""

import os
from alembic import context
from sqlalchemy import create_engine
from community_brain.jobs.models import Base

connection = context.config.attributes.get("connection")
if connection is not None:
    context.configure(connection=connection, target_metadata=Base.metadata)
    with context.begin_transaction():
        context.run_migrations()
else:
    url = os.environ.get("CB_DATABASE_URL")
    if not url:
        raise RuntimeError("CB_DATABASE_URL required for explicit migrations")
    with create_engine(url).connect() as connection:
        context.configure(connection=connection, target_metadata=Base.metadata)
        with context.begin_transaction():
            context.run_migrations()

"""Initial job schema. SQL is a frozen reviewed PostgreSQL schema snapshot."""

from pathlib import Path
from alembic import op

revision = "0001_jobs"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    sql = Path(__file__).with_suffix(".sql").read_text()
    for statement in sql.split(";"):
        if statement.strip():
            op.execute(statement)


def downgrade():
    for table in (
        "cb_rejected_events",
        "cb_outbox",
        "cb_model_calls",
        "cb_artifacts",
        "cb_attempts",
        "cb_operations",
        "cb_stages",
        "cb_jobs",
        "cb_sources",
    ):
        op.drop_table(table)

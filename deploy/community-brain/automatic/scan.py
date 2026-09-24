"""Scoped DB scan/reconciliation inside the existing image, no provider key."""

import json
import sys

from community_brain.jobs.automatic import POLICY, inspect_state, next_stage, stop_stage
from community_brain.jobs.models import Job, Stage
from community_brain.jobs.runtime import make_store
from sqlalchemy import select
from sqlalchemy.orm import Session


def main():
    store = make_store()
    if sys.argv[1] == "inspect":
        print(json.dumps(inspect_state(store, "community-brain")))
    elif sys.argv[1] == "stop":
        print(
            json.dumps(
                {
                    "stopped": stop_stage(
                        store, sys.argv[2], "automatic_execution_requires_review"
                    )
                }
            )
        )
    else:
        selected = next_stage(store, "community-brain")
        with Session(store.engine) as session:
            completed = [
                str(v)
                for v in session.scalars(
                    select(Job.id).where(
                        Job.scope == "community-brain",
                        Job.parent_id.is_(None),
                        Job.config["automation_policy"].astext == POLICY,
                        Job.indexing == "complete",
                    )
                )
            ]
            attention = (
                session.scalar(
                    select(Stage.id)
                    .join(Job)
                    .where(
                        Job.scope == "community-brain",
                        Job.config["automation_policy"].astext == POLICY,
                        Stage.name.in_(["acquisition", "processing", "indexing"]),
                        Stage.state.in_(["failed", "partial", "outcome_unknown"]),
                    )
                )
                is not None
            )
            failures = session.execute(
                select(Job, Stage)
                .join(Stage)
                .where(
                    Job.scope == "community-brain",
                    Job.config["automation_policy"].astext == POLICY,
                    Stage.name.in_(["acquisition", "processing", "indexing"]),
                    Stage.state.in_(["failed", "partial", "outcome_unknown"]),
                )
            ).all()
            recoverable = bool(failures) and all(
                store.safe_retry_available(session, job, stage)
                or (
                    stage.name == "acquisition"
                    and stage.state == "failed"
                    and job.processing == "waiting_for_input"
                    and "transcript" not in job.sources
                )
                for job, stage in failures
            )
        print(
            json.dumps(
                {
                    "completed": completed,
                    "next": selected,
                    "attention": attention,
                    "known_failure_only": recoverable,
                }
            )
        )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        # No exception message, SQL, environment, source content or credentials.
        print(
            json.dumps(
                {"code": "automatic_scan_failed", "error_class": type(error).__name__}
            ),
            file=sys.stderr,
        )
        raise SystemExit(1) from None

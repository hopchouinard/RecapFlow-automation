"""Verify privileges on migrated objects without retaining mutations."""

import json
import os

from sqlalchemy import create_engine, text
from sqlalchemy.exc import DBAPIError

engine = create_engine(os.environ["CB_DATABASE_URL"])
with engine.connect() as conn:
    assert conn.scalar(text("select current_database()")) == "community_brain_prod"
    assert conn.scalar(text("select current_user")) == "cbm_prod_runtime"
    assert conn.scalar(text("select ssl from pg_stat_ssl where pid=pg_backend_pid()"))
    assert conn.scalar(text("select version_num from alembic_version")) == "0001_jobs"
    names = (
        conn.execute(
            text(
                "select tablename from pg_tables where schemaname='public' order by tablename"
            )
        )
        .scalars()
        .all()
    )
    assert len(names) == 10 and "cb_jobs" in names
    for name in names:
        assert (
            conn.scalar(
                text(
                    "select tableowner from pg_tables where schemaname='public' and tablename=:name"
                ),
                {"name": name},
            )
            == "cbm_prod_migration"
        )
        for privilege in ("SELECT", "INSERT", "UPDATE", "DELETE"):
            assert conn.scalar(
                text("select has_table_privilege(current_user,:name,:privilege)"),
                {"name": name, "privilege": privilege},
            )
    assert not conn.scalar(
        text("select has_schema_privilege(current_user,'public','CREATE')")
    )
    assert not conn.scalar(
        text("select has_database_privilege(current_user,current_database(),'CREATE')")
    )
    for name in names:
        if name != "alembic_version":
            assert conn.scalar(text("select count(*) from " + name)) == 0
    conn.rollback()
    with conn.begin():
        conn.execute(
            text(
                "insert into cb_rejected_events (sha256,reason) values (:hash,'staging_privilege_probe')"
            ),
            {"hash": "0" * 64},
        )
        conn.execute(
            text(
                "update cb_rejected_events set reason='staging_privilege_probe_updated' where sha256=:hash"
            ),
            {"hash": "0" * 64},
        )
        conn.execute(
            text("delete from cb_rejected_events where sha256=:hash"),
            {"hash": "0" * 64},
        )
        conn.rollback()
    for sql in (
        "create table cb_staging_ddl_probe (id integer)",
        "alter table cb_jobs add column staging_denied_probe integer",
    ):
        try:
            conn.execute(text(sql))
        except DBAPIError as exc:
            assert getattr(exc.orig, "sqlstate", None) == "42501"
        else:
            raise AssertionError("runtime DDL accepted")
        finally:
            conn.rollback()
print(
    json.dumps(
        {
            "revision": "0001_jobs",
            "tables": len(names),
            "runtime_dml_verified": True,
            "ddl_denied": True,
            "table_owner_separate": True,
            "tls_verified": True,
            "jobs_empty": True,
        }
    )
)

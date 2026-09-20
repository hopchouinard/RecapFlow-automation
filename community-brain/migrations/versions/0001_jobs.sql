
CREATE TABLE cb_jobs (
	id UUID NOT NULL,
	scope VARCHAR NOT NULL,
	principal VARCHAR NOT NULL,
	key VARCHAR NOT NULL,
	request_hash VARCHAR NOT NULL,
	identity JSONB NOT NULL,
	sources JSONB NOT NULL,
	mode VARCHAR NOT NULL,
	config JSONB NOT NULL,
	version VARCHAR NOT NULL,
	reason VARCHAR,
	parent_id UUID,
	processing VARCHAR NOT NULL,
	artifacts VARCHAR NOT NULL,
	indexing VARCHAR NOT NULL,
	git VARCHAR NOT NULL,
	distribution VARCHAR NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(parent_id) REFERENCES cb_jobs (id)
)

;

CREATE TABLE cb_rejected_events (
	sha256 VARCHAR NOT NULL,
	reason VARCHAR NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
	PRIMARY KEY (sha256)
)

;

CREATE TABLE cb_sources (
	id UUID NOT NULL,
	scope VARCHAR NOT NULL,
	meeting_id VARCHAR NOT NULL,
	kind VARCHAR NOT NULL,
	sha256 VARCHAR NOT NULL,
	path VARCHAR NOT NULL,
	size INTEGER NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (scope, meeting_id, kind, sha256)
)

;

CREATE TABLE cb_model_calls (
	id UUID NOT NULL,
	job_id UUID NOT NULL,
	key VARCHAR NOT NULL,
	fence INTEGER NOT NULL,
	state VARCHAR NOT NULL,
	request_meta JSONB NOT NULL,
	response_path VARCHAR,
	response_hash VARCHAR,
	usage JSONB,
	PRIMARY KEY (id),
	UNIQUE (job_id, key),
	FOREIGN KEY(job_id) REFERENCES cb_jobs (id)
)

;

CREATE TABLE cb_operations (
	id UUID NOT NULL,
	scope VARCHAR NOT NULL,
	principal VARCHAR NOT NULL,
	operation VARCHAR NOT NULL,
	key VARCHAR NOT NULL,
	request_hash VARCHAR NOT NULL,
	job_id UUID NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (scope, principal, operation, key),
	FOREIGN KEY(job_id) REFERENCES cb_jobs (id)
)

;

CREATE TABLE cb_stages (
	id UUID NOT NULL,
	job_id UUID NOT NULL,
	name VARCHAR NOT NULL,
	state VARCHAR NOT NULL,
	generation INTEGER NOT NULL,
	fence INTEGER NOT NULL,
	attempts INTEGER NOT NULL,
	owner VARCHAR,
	lease_until TIMESTAMP WITH TIME ZONE,
	due_at TIMESTAMP WITH TIME ZONE,
	error VARCHAR,
	result JSONB,
	PRIMARY KEY (id),
	UNIQUE (job_id, name),
	FOREIGN KEY(job_id) REFERENCES cb_jobs (id)
)

;
CREATE INDEX ix_cb_stages_job_id ON cb_stages (job_id);

CREATE TABLE cb_artifacts (
	id UUID NOT NULL,
	job_id UUID NOT NULL,
	stage_id UUID NOT NULL,
	fence INTEGER NOT NULL,
	name VARCHAR NOT NULL,
	path VARCHAR NOT NULL,
	sha256 VARCHAR NOT NULL,
	size INTEGER NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (job_id, name),
	FOREIGN KEY(job_id) REFERENCES cb_jobs (id),
	FOREIGN KEY(stage_id) REFERENCES cb_stages (id)
)

;
CREATE INDEX ix_cb_artifacts_job_id ON cb_artifacts (job_id);

CREATE TABLE cb_attempts (
	id UUID NOT NULL,
	stage_id UUID NOT NULL,
	fence INTEGER NOT NULL,
	owner VARCHAR NOT NULL,
	state VARCHAR NOT NULL,
	started_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
	finished_at TIMESTAMP WITH TIME ZONE,
	reason VARCHAR,
	PRIMARY KEY (id),
	UNIQUE (stage_id, fence),
	FOREIGN KEY(stage_id) REFERENCES cb_stages (id)
)

;

CREATE TABLE cb_outbox (
	id UUID NOT NULL,
	stage_id UUID NOT NULL,
	generation INTEGER NOT NULL,
	sent_at TIMESTAMP WITH TIME ZONE,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (stage_id, generation),
	FOREIGN KEY(stage_id) REFERENCES cb_stages (id)
)

;

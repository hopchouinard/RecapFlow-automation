import { FilePreview } from "./FilePreview";
import { useEffect, useState } from "react";
import {
  Brain,
  Copy,
  Download,
  RefreshCw,
  FileText,
  Plus,
  LogOut,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Api, type Artifact, type Job } from "./api";

import { MeetingArchive } from "./MeetingArchive";
import { meetingStart } from "./meetingTime";
import { ThemeSwitch } from "./ThemeSwitch";

const dimensions = [
  "acquisition",
  "processing",
  "artifacts",
  "indexing",
  "backup",
] as const;
const label = (s: string) => s.replaceAll("_", " ");
type Readiness = { state: string; ready: boolean };
const unavailable: Readiness = { state: "unavailable", ready: false };
const readinessMessage = (state: string) =>
  (
    ({
      paused:
        "Automatic processing is paused. You can save a meeting for processing after the service is restored.",
      attention_required:
        "Automatic processing needs administrator review. You can save a meeting, but processing will wait.",
      credentials_require_review:
        "Processing access needs administrator attention. You can save a meeting, but processing may be delayed.",
      awaiting_checkpoint:
        "Processing is waiting for a backup check. New meetings will wait in the queue.",
      needs_input:
        "Processing is waiting for missing input or a recovery action. New meetings will wait in the queue.",
    }) as Record<string, string>
  )[state] ??
  "Processing status is unavailable. You can save a meeting, but processing may be delayed.";
const recoveryMessage = (code: string) =>
  (
    ({
      fathom_recording_not_found:
        "The call was not found near the supplied time. Upload its transcript to continue, or retry if Fathom has since made it available.",
      fathom_time_mismatch:
        "The recording starts more than 10 minutes from the supplied time. Upload the matching transcript to continue this meeting.",
      fathom_transcript_unavailable:
        "Fathom has not made this transcript available. Retry when it is ready, or upload the transcript.",
      fathom_authentication_failed:
        "Fathom rejected the credential. An administrator must repair it; you can upload the transcript to continue meanwhile.",
      fathom_access_denied:
        "The Fathom credential cannot access this recording. Upload its transcript, or ask an administrator to check access.",
      fathom_rate_limited:
        "Fathom temporarily limited requests. Wait a few minutes before retrying, or upload the transcript.",
      fathom_unavailable:
        "Fathom could not be reached. Retry when it is available, or upload the transcript.",
      fathom_lookup_limit:
        "The bounded lookup could not identify the call. Upload its transcript to continue.",
      fathom_invalid_response:
        "Fathom returned an unusable response. Upload the transcript or ask an administrator to investigate.",
      pipeline_failed:
        "This stage failed. Use an available recovery action below; otherwise an administrator needs to inspect the failure.",
    }) as Record<string, string>
  )[code] ??
  "This stage needs administrator review before it can continue (" +
    label(code) +
    ").";

export function App({ api, logout }: { api: Api; logout: () => void }) {
  const [view, setView] = useState<"meetings" | "runs">("meetings");
  const [jobs, setJobs] = useState<Job[]>([]),
    [job, setJob] = useState<Job | null>(null);
  const [artifacts, setArtifacts] = useState<Artifact[]>([]),
    [preview, setPreview] = useState<{
      artifact: Artifact;
      text: string;
    } | null>(null);
  const [error, setError] = useState(""),
    [notice, setNotice] = useState(""),
    [busy, setBusy] = useState(false);
  const [automatic, setAutomatic] = useState(false);
  const [readiness, setReadiness] = useState<Readiness>(unavailable);
  const [provider, setProvider] = useState("manual");
  const [mode, setMode] = useState("weekly");
  const [creating, setCreating] = useState(false),
    [reason, setReason] = useState(""),
    [permissions, setPermissions] = useState<string[]>([]);
  const [cursor, setCursor] = useState<string | null>(null);
  const can = (permission: string) => permissions.includes(permission);
  async function refreshService() {
    try {
      const me = await api.request<{
        permissions: string[];
        automatic_processing?: boolean;
        processing_readiness?: Readiness;
      }>("/me");
      setPermissions(me.permissions);
      setAutomatic(me.automatic_processing === true);
      const status = me.processing_readiness ?? unavailable;
      setReadiness(status);
      return { automatic: me.automatic_processing === true, readiness: status };
    } catch (error) {
      setReadiness(unavailable);
      throw error;
    }
  }
  async function refresh(more = false) {
    const response = await api.request<{
      items: Job[];
      next_cursor: string | null;
    }>(
      "/jobs" + (more && cursor ? "?cursor=" + encodeURIComponent(cursor) : ""),
    );
    setJobs((previous) =>
      more ? [...previous, ...response.items] : response.items,
    );
    setCursor(response.next_cursor);
  }
  async function select(id: string, preservePreview = false) {
    const [detail, files] = await Promise.all([
      api.request<Job>("/jobs/" + id),
      api.request<{ items: Artifact[] }>("/jobs/" + id + "/artifacts"),
    ]);
    setJob(detail);
    setArtifacts(files.items);
    if (!preservePreview) setPreview(null);
  }
  async function action(work: () => Promise<void>) {
    setBusy(true);
    setError("");
    setNotice("");
    try {
      await work();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
    } finally {
      setBusy(false);
    }
  }
  useEffect(() => {
    void action(async () => {
      await refreshService();
      await refresh();
    });
  }, [api]);
  useEffect(() => {
    const timer = setInterval(() => {
      if (!busy) {
        void refreshService().catch(() => {});
        void refresh().catch(() => {});
        if (job) void select(job.id, true).catch(() => {});
      }
    }, 15000);
    return () => clearInterval(timer);
  }, [api, busy, job?.id]);
  async function upload(file: File, meeting: string, kind: string) {
    if (file.size > 10_000_000)
      throw new Error("Choose a text file smaller than 10 MB.");
    return (
      await api.request<{ id: string }>("/sources", {
        meeting_id: meeting,
        kind,
        content: await file.text(),
      })
    ).id;
  }
  async function submit(form: HTMLFormElement) {
    // Snapshot inputs before awaiting: the busy fieldset becomes disabled while
    // readiness is refreshed, and FormData omits disabled controls.
    const data = new FormData(form);
    const service = await refreshService();
    const meetingInput = String(data.get("meeting")).trim();
    const selectedProvider = String(data.get("provider"));
    const callUrl =
      /^https:\/\/fathom\.video\/calls\/(\d+)\/?(?:[?#].*)?$/.exec(
        meetingInput,
      );
    const meeting =
      selectedProvider === "fathom" && callUrl ? callUrl[1] : meetingInput;
    if (selectedProvider === "fathom" && !/^\d+$/.test(meeting))
      throw new Error("Enter a Fathom call URL or numeric call/recording ID.");
    const timezone = String(data.get("timezone")).trim();
    const started = meetingStart(
      String(data.get("start")),
      timezone,
      String(data.get("offset")).trim(),
    );
    const pending: { kind: string; content: string }[] = [];
    for (const kind of ["transcript", "chat"]) {
      const file = data.get(kind);
      if (file instanceof File && file.size) {
        if (file.size > 10_000_000)
          throw new Error("Choose text files smaller than 10 MB.");
        const content = await file.text();
        if (!content.trim() || content.length > 5_000_000)
          throw new Error(
            "Choose nonempty text files with fewer than 5 million characters.",
          );
        pending.push({ kind, content });
      }
    }
    const sources: Record<string, string> = {};
    for (const file of pending) {
      sources[file.kind] = (
        await api.request<{ id: string }>("/sources", {
          meeting_id: meeting,
          kind: file.kind,
          content: file.content,
        })
      ).id;
    }
    const response = await api.request<{ id: string }>("/jobs", {
      identity: {
        meeting_id: meeting,
        started_at: started,
        timezone,
        local_date: String(data.get("start")).slice(0, 10),
        provider: String(data.get("provider")),
      },
      mode: String(data.get("mode")),
      sources,
      version: "processing-v1",
    });
    setCreating(false);
    setView("runs");
    await refresh();
    await select(response.id);
    if (service.automatic && !service.readiness.ready) {
      setNotice("Meeting saved. Check its run status for processing progress.");
    }
  }
  async function download() {
    if (!preview) return;
    const url = URL.createObjectURL(
      new Blob([preview.text], { type: "text/plain;charset=utf-8" }),
    );
    const link = document.createElement("a");
    link.href = url;
    link.download = preview.artifact.name;
    link.click();
    URL.revokeObjectURL(url);
  }
  return (
    <div className="shell">
      <header>
        <a className="brand" href="/">
          <Brain size={26} />
          <span>
            Community Brain<small>CALL WORKSPACE</small>
          </span>
        </a>
        <div className="header-actions">
          <ThemeSwitch />
          <Button variant="ghost" onClick={logout}>
            <LogOut />
            Sign out
          </Button>
        </div>
      </header>
      <main>
        <div className="intro">
          <div>
            <p className="eyebrow">FROM CONVERSATION TO COMMUNITY</p>
            <h1>Your calls, ready to share.</h1>
            <p>Follow each recap and collect the files you need.</p>
          </div>
          {can("jobs:submit") && can("sources:upload") && (
            <Button
              disabled={busy}
              onClick={() => setCreating(!creating)}
              aria-expanded={creating}
              aria-controls="new-meeting-form"
            >
              <Plus />
              New meeting
            </Button>
          )}
        </div>
        {error && (
          <div role="alert" className="alert">
            {error}
          </div>
        )}
        {automatic && !readiness.ready && (
          <div
            role="status"
            className="notice"
            aria-label="Processing availability"
          >
            {readinessMessage(readiness.state)}
          </div>
        )}
        {notice && (
          <div role="status" className="notice">
            {notice}
          </div>
        )}
        {creating && (
          <form
            id="new-meeting-form"
            className="panel form"
            aria-label="New meeting"
            onSubmit={(e) => {
              e.preventDefault();
              void action(() => submit(e.currentTarget));
            }}
          >
            <fieldset disabled={busy} className="meeting-fields">
              <h2>New meeting</h2>
              <label>
                {provider === "fathom" ? "Fathom call URL or ID" : "Meeting ID"}
                <input
                  name="meeting"
                  required
                  pattern={
                    provider === "fathom" ? undefined : "[A-Za-z0-9_.:\\-]+"
                  }
                  maxLength={200}
                  placeholder={
                    provider === "fathom"
                      ? "https://fathom.video/calls/821559116"
                      : "A unique meeting ID"
                  }
                />
              </label>
              <label>
                Meeting date and time
                <input type="datetime-local" name="start" required />
              </label>
              <label>
                Timezone
                <input
                  name="timezone"
                  required
                  defaultValue={
                    Intl.DateTimeFormat().resolvedOptions().timeZone
                  }
                  placeholder="America/Toronto"
                />
              </label>
              <label>
                UTC offset (optional; for repeated daylight-saving times)
                <input name="offset" placeholder="-04:00" />
              </label>
              <label>
                Source
                <select
                  name="provider"
                  value={provider}
                  onChange={(e) => setProvider(e.target.value)}
                >
                  <option value="manual">Manual transcript</option>
                  <option value="fathom">Fetch from Fathom</option>
                </select>
              </label>
              <label>
                Recap type
                <select
                  name="mode"
                  value={mode}
                  onChange={(e) => setMode(e.target.value)}
                >
                  <option value="weekly">Weekly community call</option>
                  <option value="transcript_backfill">
                    Historical transcript
                  </option>
                </select>
              </label>
              <label>
                Transcript
                <input
                  type="file"
                  name="transcript"
                  accept=".txt,.md,text/plain,text/markdown"
                  required={provider === "manual"}
                />
              </label>
              <label>
                Zoom chat
                <input
                  type="file"
                  name="chat"
                  accept=".txt,text/plain"
                  required={mode === "weekly"}
                />
              </label>
              <p>
                {automatic && !readiness.ready
                  ? "Your files and meeting details will be saved. Processing will wait for the service to become ready."
                  : automatic
                    ? "Saving starts processing automatically: fetch the selected transcript if needed, generate your recap files, and add the meeting to search. Nothing is published remotely."
                    : "Your uploads and meeting details are saved together. Processing is started separately; uploading does not run models or publish anything."}
              </p>
              <Button type="submit" disabled={busy}>
                {busy
                  ? "Saving meeting…"
                  : automatic && !readiness.ready
                    ? "Save for later processing"
                    : automatic
                      ? "Save and process meeting"
                      : "Save meeting"}
              </Button>
              <Button
                type="button"
                variant="outline"
                onClick={() => setCreating(false)}
              >
                Cancel
              </Button>
            </fieldset>
          </form>
        )}
        <nav className="workspace-tabs" aria-label="Workspace view">
          <Button
            variant={view === "meetings" ? "default" : "outline"}
            aria-pressed={view === "meetings"}
            onClick={() => setView("meetings")}
          >
            Meetings
          </Button>
          <Button
            variant={view === "runs" ? "default" : "outline"}
            aria-pressed={view === "runs"}
            onClick={() => setView("runs")}
          >
            Recent runs
          </Button>
        </nav>
        {view === "meetings" ? (
          <MeetingArchive
            api={api}
            jobs={jobs}
            openRun={(id) => {
              setView("runs");
              void action(() => select(id));
            }}
          />
        ) : (
          <div className="workspace">
            <aside className="panel">
              <div className="panel-heading">
                <h2>
                  Recaps <span>{jobs.length}</span>
                </h2>
                <Button
                  variant="ghost"
                  size="icon"
                  aria-label="Refresh recaps"
                  disabled={busy}
                  onClick={() =>
                    void action(async () => {
                      await refresh();
                      if (job) await select(job.id);
                    })
                  }
                >
                  <RefreshCw />
                </Button>
              </div>
              {!jobs.length && (
                <p className="empty">
                  No recaps yet. Create one to get started.
                </p>
              )}
              {jobs.map((j) => (
                <button
                  className={"job " + (job?.id === j.id ? "selected" : "")}
                  key={j.id}
                  onClick={() => void action(() => select(j.id))}
                >
                  <strong>{j.identity.local_date}</strong>
                  <span>{j.identity.meeting_id}</span>
                  <small>{label(j.processing)}</small>
                </button>
              ))}
              {cursor && (
                <Button
                  variant="ghost"
                  onClick={() => void action(() => refresh(true))}
                >
                  Load older recaps
                </Button>
              )}
            </aside>
            <section className="panel detail" aria-label="Recap details">
              {!job ? (
                <div className="empty">
                  <FileText size={36} />
                  <h2>Select a recap</h2>
                  <p>Its progress and shareable files will appear here.</p>
                </div>
              ) : (
                <>
                  <div className="panel-heading">
                    <div>
                      <p className="eyebrow">
                        {job.mode === "weekly"
                          ? "WEEKLY CALL"
                          : "HISTORICAL CALL"}
                      </p>
                      <h2>{job.identity.local_date}</h2>
                      <p>{job.identity.meeting_id}</p>
                    </div>
                  </div>
                  <dl className="states">
                    {dimensions.map((d) => (
                      <div key={d}>
                        <dt>{d === "artifacts" ? "Markdown files" : d}</dt>
                        <dd data-state={job[d]}>
                          {label(job[d] ?? "not reported")}
                        </dd>
                      </div>
                    ))}
                  </dl>
                  <p className="muted">
                    Git publication: {label(job.git)} · Distribution:{" "}
                    {label(job.distribution)}
                  </p>
                  {job.missing_inputs?.map((kind) => (
                    <label className="missing" key={kind}>
                      {kind === "transcript" && job.acquisition === "failed"
                        ? "Upload transcript and continue"
                        : `Add missing ${kind}`}
                      <input
                        disabled={
                          busy ||
                          !can("sources:upload") ||
                          !can("jobs:submit") ||
                          (kind === "transcript" &&
                            ["running", "outcome_unknown"].includes(
                              job.acquisition ?? "",
                            ))
                        }
                        type="file"
                        accept=".txt"
                        onChange={(e) => {
                          const file = e.target.files?.[0];
                          if (file)
                            void action(async () => {
                              const id = await upload(
                                file,
                                job.identity.meeting_id,
                                kind,
                              );
                              await api.request(
                                "/jobs/" + job.id + "/sources",
                                {
                                  [kind]: id,
                                },
                              );
                              await select(job.id);
                              await refresh();
                            });
                        }}
                      />
                    </label>
                  ))}
                  <h3>Files</h3>
                  <div className="files">
                    {artifacts.map((a) => (
                      <Button
                        key={a.id}
                        variant="outline"
                        disabled={busy}
                        onClick={() =>
                          void action(async () =>
                            setPreview({
                              artifact: a,
                              text: await api.text(a),
                            }),
                          )
                        }
                      >
                        <FileText />
                        {a.name}
                      </Button>
                    ))}
                  </div>
                  {!artifacts.length && (
                    <p className="muted">
                      Files appear here as they are completed.
                    </p>
                  )}
                  {preview && (
                    <FilePreview
                      key={preview.artifact.id}
                      name={preview.artifact.name}
                      text={preview.text}
                    >
                      <Button
                        variant="ghost"
                        aria-label="Copy file"
                        onClick={() =>
                          void action(async () => {
                            await navigator.clipboard.writeText(preview.text);
                            setNotice("Copied to clipboard.");
                          })
                        }
                      >
                        <Copy />
                      </Button>
                      <Button
                        variant="ghost"
                        aria-label="Download file"
                        onClick={() => void action(download)}
                      >
                        <Download />
                      </Button>
                    </FilePreview>
                  )}
                  {job.stages?.some((s) => s.error) && (
                    <div className="stage-errors">
                      {job.stages
                        .filter((s) => s.error)
                        .map((s) => (
                          <p key={s.id}>
                            {s.name}: {recoveryMessage(s.error!)}
                          </p>
                        ))}
                    </div>
                  )}
                  {(can("jobs:retry") ||
                    can("jobs:rerun") ||
                    (can("jobs:submit") &&
                      job.stages?.some((s) => s.safe_retryable))) && (
                    <div className="controls">
                      <label>
                        Reason for retry or rerun
                        <input
                          value={reason}
                          onChange={(e) => setReason(e.target.value)}
                          placeholder="Explain what changed"
                          maxLength={500}
                        />
                      </label>
                      {(can("jobs:retry") || can("jobs:submit")) &&
                        job.stages
                          ?.filter(
                            (s) =>
                              (can("jobs:submit") && s.safe_retryable) ||
                              (can("jobs:retry") && s.retryable),
                          )
                          .map((s) => (
                            <Button
                              variant="outline"
                              key={s.id}
                              disabled={busy || !reason.trim()}
                              onClick={() =>
                                void action(async () => {
                                  await api.request(
                                    `/jobs/${job.id}/stages/${s.id}/${s.safe_retryable && can("jobs:submit") ? "resume" : "retry"}`,
                                    { generation: s.generation, reason },
                                  );
                                  await select(job.id);
                                  await refresh();
                                })
                              }
                            >
                              Retry {s.name}
                            </Button>
                          ))}
                      {can("jobs:rerun") && (
                        <Button
                          variant="outline"
                          disabled={busy || !reason.trim()}
                          onClick={() =>
                            void action(async () => {
                              const result = await api.request<{ id: string }>(
                                `/jobs/${job.id}/reruns`,
                                {
                                  identity: job.identity,
                                  mode: job.mode,
                                  sources: job.sources,
                                  version: job.version,
                                  reason,
                                },
                              );
                              await refresh();
                              await select(result.id);
                            })
                          }
                        >
                          Create versioned rerun
                        </Button>
                      )}
                      <p className="muted">
                        A rerun creates new outputs and keeps the originals.
                      </p>
                    </div>
                  )}
                </>
              )}
            </section>
          </div>
        )}
      </main>
      <footer>Community Brain · Your conversation archive</footer>
    </div>
  );
}

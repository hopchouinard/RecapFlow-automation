import { FilePreview } from "./FilePreview";
import { useEffect, useState } from "react";
import { ChevronRight, Copy, Download, FileText } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Api, type Artifact, type Job } from "./api";

type PreservedArtifact = Artifact & { origin: string };
type Meeting = {
  date: string;
  artifacts: PreservedArtifact[];
  source?: string;
  indexing?: string;
};

export function MeetingArchive({
  api,
  jobs,
  openRun,
}: {
  api: Api;
  jobs: Job[];
  openRun: (id: string) => void;
}) {
  const [meetings, setMeetings] = useState<Meeting[]>([]);
  const [selected, setSelected] = useState<Meeting | null>(null);
  const [preview, setPreview] = useState<{
    artifact: Artifact;
    text: string;
  } | null>(null);
  const [search, setSearch] = useState("");
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    let active = true;
    const refresh = () =>
      api
        .request<{ items: Meeting[] }>("/meetings")
        .then((r) => {
          if (active) {
            setMeetings(r.items);
            setSelected((previous) =>
              previous
                ? (r.items.find((m) => m.date === previous.date) ?? previous)
                : null,
            );
          }
        })
        .catch((e) => {
          if (active) setError(e.message);
        })
        .finally(() => {
          if (active) setLoading(false);
        });
    void refresh();
    const timer = setInterval(() => {
      void refresh();
    }, 15000);
    return () => {
      active = false;
      clearInterval(timer);
    };
  }, [api]);
  async function action(work: () => Promise<void>) {
    setError("");
    setNotice("");
    setBusy(true);
    try {
      await work();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Unable to open file.");
    } finally {
      setBusy(false);
    }
  }
  const filtered = meetings.filter((m) => m.date.includes(search.trim()));
  const years = [...new Set(filtered.map((m) => m.date.slice(0, 4)))]
    .sort()
    .reverse();
  const isOpen = (key: string) => expanded[key] ?? Boolean(search.trim());
  function branch(key: string, open: boolean) {
    setExpanded((previous) =>
      previous[key] === open ? previous : { ...previous, [key]: open },
    );
  }
  return (
    <>
      {error && (
        <p role="alert" className="alert">
          {error}
        </p>
      )}
      {notice && (
        <p role="status" className="notice">
          {notice}
        </p>
      )}
      <div className="workspace">
        <aside className="panel">
          <div className="panel-heading">
            <h2>
              Meetings <span>{meetings.length}</span>
            </h2>
          </div>
          <label className="archive-search">
            Find a meeting by date
            <input
              type="search"
              placeholder="2025-06"
              value={search}
              onChange={(e) => {
                setSearch(e.target.value);
                setExpanded({});
              }}
            />
          </label>
          {loading && <p className="empty">Loading meetings…</p>}
          <nav
            className="meeting-list meeting-tree"
            aria-label="Meetings by year and month"
          >
            {years.map((year) => {
              const yearMeetings = filtered.filter((m) =>
                m.date.startsWith(year),
              );
              const months = [
                ...new Set(yearMeetings.map((m) => m.date.slice(0, 7))),
              ]
                .sort()
                .reverse();
              return (
                <details
                  key={year}
                  open={isOpen(year)}
                  onToggle={(e) => branch(year, e.currentTarget.open)}
                >
                  <summary>
                    <ChevronRight size={16} />
                    <strong>{year}</strong>
                    <span>{yearMeetings.length}</span>
                  </summary>
                  {months.map((month) => {
                    const monthMeetings = yearMeetings
                      .filter((m) => m.date.startsWith(month))
                      .sort((a, b) => b.date.localeCompare(a.date));
                    const name = new Intl.DateTimeFormat("en", {
                      month: "long",
                      timeZone: "UTC",
                    }).format(new Date(month + "-01T12:00:00Z"));
                    return (
                      <details
                        className="meeting-month"
                        key={month}
                        open={isOpen(month)}
                        onToggle={(e) => branch(month, e.currentTarget.open)}
                      >
                        <summary>
                          <ChevronRight size={16} />
                          <strong>{name}</strong>
                          <span>{monthMeetings.length}</span>
                        </summary>
                        {monthMeetings.map((m) => (
                          <button
                            key={m.date}
                            disabled={busy}
                            aria-label={m.date}
                            aria-current={
                              selected?.date === m.date ? "date" : undefined
                            }
                            className={
                              "job " +
                              (selected?.date === m.date ? "selected" : "")
                            }
                            onClick={() => {
                              setSelected(m);
                              setPreview(null);
                              setNotice("");
                              setError("");
                            }}
                          >
                            <strong>
                              {new Intl.DateTimeFormat("en", {
                                day: "numeric",
                                weekday: "long",
                                timeZone: "UTC",
                              }).format(new Date(m.date + "T12:00:00Z"))}
                            </strong>
                            <span>
                              {m.artifacts.length}{" "}
                              {m.source === "processed" ? "recap" : "preserved"}{" "}
                              files
                            </span>
                          </button>
                        ))}
                      </details>
                    );
                  })}
                </details>
              );
            })}
          </nav>
          {!loading &&
            !meetings.some((m) => m.date.includes(search.trim())) && (
              <p className="empty">No matching meetings.</p>
            )}
        </aside>
        <section className="panel detail" aria-label="Meeting archive">
          {!selected ? (
            <div className="empty">
              <FileText size={36} />
              <h2>Select a meeting</h2>
              <p>Browse, copy and download your original meeting files.</p>
            </div>
          ) : (
            <>
              <div className="panel-heading">
                <div>
                  <p className="eyebrow">MEETING ARCHIVE</p>
                  <h2>{selected.date}</h2>
                  <p>
                    {selected.source === "processed"
                      ? `Generated recap files. Search indexing: ${(selected.indexing ?? "pending").replaceAll("_", " ")}.`
                      : "Original preserved files. No reprocessing."}
                  </p>
                </div>
              </div>
              {jobs
                .filter((j) => j.identity.local_date === selected.date)
                .map((j) => (
                  <Button
                    key={j.id}
                    variant="outline"
                    onClick={() => openRun(j.id)}
                  >
                    View recent recap run
                  </Button>
                ))}
              {(["output", "historical"] as const).map((origin) => {
                const files = selected.artifacts.filter(
                  (a) => a.origin === origin,
                );
                return files.length ? (
                  <div key={origin}>
                    <h3>
                      {origin === "output"
                        ? "Recap files"
                        : "Original recording files"}
                    </h3>
                    <div className="files">
                      {files.map((a) => (
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
                  </div>
                ) : null;
              })}
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
                    onClick={() => {
                      const url = URL.createObjectURL(
                        new Blob([preview.text], {
                          type: "text/plain;charset=utf-8",
                        }),
                      );
                      const a = document.createElement("a");
                      a.href = url;
                      a.download = preview.artifact.name;
                      a.click();
                      URL.revokeObjectURL(url);
                    }}
                  >
                    <Download />
                  </Button>
                </FilePreview>
              )}
            </>
          )}
        </section>
      </div>
    </>
  );
}

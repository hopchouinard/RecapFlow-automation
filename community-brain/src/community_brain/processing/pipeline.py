"""Pure processing with injected model calls and per-call persistence hooks.

No credentials, filesystem outputs, HTTP calls or n8n runtime are implicit.
The job worker owns durable storage and unknown-effect reconciliation.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import date, timedelta
from importlib.resources import files
import json
import math
import re
from typing import Callable

CANON = ("general", "insights", "qa", "tools", "links", "decisions")
HEADERS = (
    "📝 SUMMARY",
    "💡 KEY INSIGHTS",
    "❓ KEY Q&A",
    "🛠️ TOOLS AND CONCEPTS MENTIONED",
    "📎 SHARED RESOURCES",
    "🔄 FOLLOW-UPS WORTH EXPLORING",
)
CEILINGS = {"z-ai/glm-5.3-flash": 131072, "anthropic/claude-sonnet-5": 128000}
SNAPSHOT = json.loads(files(__package__).joinpath("prompts-v1.json").read_text())


class PipelineFailure(ValueError):
    """Known unsuccessful result; previously emitted artifacts remain valid."""


class OutcomeUnknown(RuntimeError):
    """An external call may have spent money; never auto-retry this exception."""


def estimate_tokens(text):
    # JavaScript String.length counts UTF-16 code units, including emoji pairs.
    return math.ceil(len(text.encode("utf-16-le", errors="surrogatepass")) / 2 / 3.6)


def split_lines(text, target):
    chunks, buf, tokens = [], [], 0
    for line in text.split("\n"):
        count = estimate_tokens(line) + 1
        if tokens + count > target and buf:
            chunks.append("\n".join(buf))
            buf, tokens = [], 0
        buf.append(line)
        tokens += count
    if buf and "\n".join(buf).strip():
        chunks.append("\n".join(buf))
    return chunks


def sections(text):
    marks = list(re.finditer(r"^#{1,3}[ \t]+([a-z]+)[ \t]*$", text, re.M))
    result = {}
    for i, mark in enumerate(marks):
        body = text[
            mark.end() : marks[i + 1].start() if i + 1 < len(marks) else len(text)
        ].strip()
        if mark[1] in CANON and body and body.lower() != "_none._":
            result[mark[1]] = body
    return result


def split_turns(text, target):
    chunks, buf, tokens = [], [], 0
    for block in filter(None, re.split(r"(?=^\d{2}:\d{2}:\d{2} - )", text, flags=re.M)):
        count = estimate_tokens(block)
        if tokens + count > target and buf:
            chunks.append("".join(buf))
            buf, tokens = [], 0
        buf.append(block)
        tokens += count
    if buf:
        chunks.append("".join(buf))
    return chunks


def structure_ok(expect, text):
    if expect == "prep.chunk":
        marks = list(
            re.finditer(
                r"<!--SEGMENT\s*\ntopic:\s*.*?\nspeakers:\s*.*?\nkeywords:\s*.*?\nsummary:\s*.*?\n-->",
                text,
                re.S,
            )
        )
        if not marks or len(marks) != text.count("<!--SEGMENT"):
            return False
        prefix = text[: marks[0].start()].strip()
        if prefix:
            lines = [line.strip() for line in re.split(r"\r?\n", prefix)]
            lines = [line for line in lines if line]
            keys = [line.split(":", 1)[0] for line in lines[1:]]
            if (
                len(lines) != 4
                or lines[0] != "=== SESSION ==="
                or set(keys) != {"date", "duration_estimate", "main_themes"}
                or any(
                    not re.match(r"^(date|duration_estimate|main_themes):\s*\S", line)
                    for line in lines[1:]
                )
            ):
                return False
        for i, mark in enumerate(marks):
            body = text[
                mark.end() : marks[i + 1].start() if i + 1 < len(marks) else len(text)
            ]
            body = body.split("=== UNRESOLVED SPEAKERS ===")[0]
            if len(re.sub(r"\s", "", body).encode("utf-16-le")) // 2 < 50:
                return False
    elif expect in ("signal.map", "signal.reduce"):
        if expect == "signal.reduce" and "```" in text:
            return False
        if re.fullmatch(r"```[^\n]*\n[\s\S]*```", text.strip()):
            return False
        if expect == "signal.map":
            return any(
                m[1] in CANON
                for m in re.finditer(r"^#{1,3}[ \t]+([a-z]+)[ \t]*$", text, re.M)
            )
        marks = list(re.finditer(r"^#{1,3}[ \t]+(.+)$", text, re.M))
        if tuple(m[1].strip().split()[0].lower() for m in marks) != CANON:
            return False
        return all(
            text[
                m.end() : marks[i + 1].start() if i + 1 < len(marks) else len(text)
            ].strip()
            for i, m in enumerate(marks)
        )
    elif expect == "post.section":
        return not re.search(
            r"^\s*#{1,6}\s|\*\*|^\s*[-*]\s+|\[[^\]]+\]\([^)]+\)", text, re.M
        )
    return True


def normalize(request, index=0):
    for field in ("stepName", "model", "system", "user", "maxTokens"):
        if request.get(field) is None or request[field] == "":
            raise PipelineFailure(f"missing required field {field}")
    return {
        **request,
        "chunkIndex": request.get("chunkIndex", index),
        "temperature": request.get("temperature", 0.3),
        "attempt": 1,
        "ceiling": CEILINGS.get(request["model"], 32768),
        "baseMaxTokens": request["maxTokens"],
    }


def classify(request, body):
    choice = (body.get("choices") or [{}])[0]
    text = (choice.get("message") or {}).get("content") or ""
    finish = choice.get("finish_reason") or None
    usage = body.get("usage") or {}
    failure = None
    if body.get("error") or ("choices" not in body and not text):
        failure = "api_error"
    elif not text.strip():
        failure = "reasoning_burn"
    elif finish != "stop":
        failure = "content_truncated"
    elif not structure_ok(request.get("expect"), text):
        failure = "structure"
    return {
        **request,
        "text": text,
        "ok": failure is None,
        "failureKind": failure,
        "finishReason": finish,
        "attempts": request["attempt"],
        "usage": {
            "promptTokens": usage.get("prompt_tokens") or 0,
            "completionTokens": usage.get("completion_tokens") or 0,
            "reasoningTokens": (usage.get("completion_tokens_details") or {}).get(
                "reasoning_tokens"
            )
            or 0,
            "cost": usage.get("cost") or 0,
        },
        "errorMessage": (body.get("error") or {}).get("message") or None,
    }


def escalate(result):
    attempt = result["attempts"] + 1
    if result["ok"] or attempt > 3:
        raise PipelineFailure("component retry exhausted")
    effort, factor = {2: ("low", 1.5), 3: ("minimal", 2)}[attempt]
    return {
        **result,
        "attempt": attempt,
        "reasoningEffort": effort,
        "maxTokens": min(
            math.floor(result["baseMaxTokens"] * factor), result["ceiling"]
        ),
    }


def call_component(request, call: Callable, record: Callable = lambda *_: None):
    request = normalize(request)
    while True:
        # Caller supplies the intent/outcome durability hook around actual transport.
        # Transport exceptions propagate; no blind retry of unknown spend.
        body = call(request)
        result = classify(request, body)
        record(request, body, result)
        if result["ok"] or result["attempts"] == 3:
            return result
        request = escalate(result)


def aggregate_prep(results, meeting_date, transcript):
    texts = [r["text"] for r in sorted(results, key=lambda r: r["chunkIndex"])]
    themes, unresolved, bodies = {}, {}, []
    seconds = [
        int(a or d) * 3600 + int(b or e) * 60 + int(c or f)
        for a, b, c, d, e, f in re.findall(
            r"\[(\d{2}):(\d{2}):(\d{2})\]|^(\d{2}):(\d{2}):(\d{2}) - ", transcript, re.M
        )
    ]
    duration = (
        f"{max(seconds) // 3600}h {max(seconds) % 3600 // 60}m"
        if seconds
        else "unknown"
    )
    for text in texts:
        theme = re.search(r"^main_themes:\s*(.*)$", text, re.M)
        if theme:
            themes.update(
                dict.fromkeys(x.strip() for x in theme[1].split(",") if x.strip())
            )
        footer = re.search(r"===\s*UNRESOLVED SPEAKERS\s*===([\s\S]*)$", text)
        if footer:
            unresolved.update(
                dict.fromkeys(
                    re.sub(r"\s+", " ", x.strip())
                    for x in footer[1].split("\n")
                    if x.strip().startswith("-")
                )
            )
            text = text[: footer.start()]
        segment = text.find("<!--SEGMENT")
        if segment > 0 and re.search(r"===\s*SESSION\s*===", text[:segment]):
            text = text[segment:]
        if text.strip():
            bodies.append(text.strip())
    header = f"=== SESSION ===\ndate: {meeting_date}\nduration_estimate: {duration}\nmain_themes: {'; '.join(themes)}"
    result = header + "\n\n" + "\n\n".join(bodies)
    if unresolved:
        result += "\n\n=== UNRESOLVED SPEAKERS ===\n" + "\n".join(unresolved)
    return result


def next_tuesday(meeting_date):
    current = date.fromisoformat(meeting_date)
    target = current + timedelta(days=(1 - current.weekday()) % 7 or 7)
    day = target.day
    suffix = (
        "st"
        if day in (1, 21, 31)
        else "nd"
        if day in (2, 22)
        else "rd"
        if day in (3, 23)
        else "th"
    )
    months = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )
    return target.isoformat(), f"{months[target.month - 1]} {day}{suffix}"


class Pipeline:
    def __init__(self, mode="weekly", config=None):
        if mode not in SNAPSHOT:
            raise PipelineFailure("invalid mode")
        self.mode = mode
        self.config = deepcopy(config or SNAPSHOT[mode]["config"])
        self.prompts = SNAPSHOT[mode]["prompts"]
        if not 0 <= self.config["retry"]["callerHalvings"] <= 2:
            raise PipelineFailure("callerHalvings must be between 0 and 2")

    def request(self, step, name, user, expect="none", system=None, **metadata):
        cfg = self.config["steps"][step]
        return {
            "stepName": name,
            "model": cfg["model"],
            "maxTokens": cfg["maxTokens"],
            **(
                {"reasoningEffort": cfg["reasoningEffort"]}
                if "reasoningEffort" in cfg
                else {}
            ),
            "expect": expect,
            "chunkIndex": 0,
            "system": system if system is not None else self.prompts[step],
            "user": user,
            **metadata,
        }

    def split_requests(self, step, transcript, aliases="", halving=0):
        target = math.floor(
            self.config["steps"][step]["chunkTargetTokens"] / 2**halving
        )
        prompt = self.prompts[step].replace("@@ALIASES@@", aliases)
        name = "prep" if step == "prep" else "signal.map"
        split = split_lines if self.mode == "weekly" else split_turns
        return [
            self.request(
                step,
                name,
                chunk,
                name + ".chunk" if step == "prep" else name,
                prompt,
                chunkIndex=i,
                halving=halving,
            )
            for i, chunk in enumerate(split(transcript, target))
        ]

    def reduce_request(self, results, chat):
        if any(not r["ok"] for r in results):
            raise PipelineFailure("signal map failed; no artifact written")
        cfg = self.config["steps"]["signalReduce"]
        prompt = (
            self.prompts["signalReduce"]
            .replace("@@BUDGET_TOKENS@@", str(cfg["budgetTokens"]))
            .replace("@@BUDGET_CHARS@@", str(cfg["budgetTokens"] * 4))
        )
        parts = "\n\n".join(
            f"### PART {i + 1}\n\n{r['text']}"
            for i, r in enumerate(sorted(results, key=lambda r: r["chunkIndex"]))
        )
        user = "# PER-PART EXTRACTIONS\n\n" + parts
        if self.mode == "weekly":
            user += "\n\n# ZOOM CHAT LOG\n\n" + chat
        if (
            estimate_tokens(prompt) + estimate_tokens(user)
            > (cfg.get("contextLimit") or 32768) // 2
        ):
            raise PipelineFailure(
                "signal reduce input is too large; no artifact written"
            )
        return self.request(
            "signalReduce", "signal.reduce", user, "signal.reduce", prompt
        )

    def post_requests(self, signal):
        parts = sections(signal)
        return [
            self.request(
                "postSection",
                "post.section." + slug,
                parts[slug],
                "post.section",
                self.prompts["postSection"][slug],
                section=slug,
                chunkIndex=i,
                halving=0,
            )
            for i, slug in enumerate(s for s in CANON if s in parts)
        ]

    def run(
        self,
        transcript,
        meeting_date,
        call,
        *,
        chat="",
        aliases="",
        emit=lambda *_: None,
        record=lambda *_: None,
    ):
        date.fromisoformat(meeting_date)
        if not transcript.strip():
            raise PipelineFailure("empty transcript")
        artifacts = {}

        def save(name, content):
            if not isinstance(content, str) or not content.strip():
                raise PipelineFailure(f"{name}: refusing empty content")
            emit(name, content)
            artifacts[name] = content

        def component(request):
            return call_component(request, call, record)

        def require(result):
            if not result["ok"]:
                raise PipelineFailure(f"{result['stepName']}: {result['failureKind']}")
            return result["text"]

        def mapped(step):
            for halving in range(self.config["retry"]["callerHalvings"] + 1):
                results = [
                    component(r)
                    for r in self.split_requests(step, transcript, aliases, halving)
                ]
                if results and all(r["ok"] for r in results):
                    return results
            raise PipelineFailure(f"{step}: caller retry exhausted")

        if self.mode == "weekly":
            save("transcript.txt", transcript)
        prep = mapped("prep")
        save("prepared-transcript.md", aggregate_prep(prep, meeting_date, transcript))
        signal = require(component(self.reduce_request(mapped("signalMap"), chat)))
        def canonical_heading(match):
            words = match[1].strip().split()
            slug = words[0].lower() if words else ""
            return "## " + slug if slug in CANON else match[0]

        signal = re.sub(
            r"^#{1,3}[ \t]+(.+)$",
            canonical_heading,
            signal,
            flags=re.M,
        )
        # The aggregate guard is stricter than the component's tolerant heading scan.
        if tuple(re.findall(r"^##[ \t]+([a-z]+)[ \t]*$", signal, re.M)) != CANON:
            raise PipelineFailure("signal sections are not canonical")
        save("extracted-signal.md", signal)
        post_results = [component(r) for r in self.post_requests(signal)]
        bodies = {r["section"]: require(r).strip() for r in post_results}
        post = "\n\n\n".join(
            h + "\n\n" + bodies[s] for s, h in zip(CANON, HEADERS) if bodies.get(s)
        )
        save("community-post.md", post)
        if self.mode == "weekly":
            compressed = require(component(self.request("compress", "compress", post)))
            save("community-post-compressed.md", compressed)
            invite_date, formatted = next_tuesday(meeting_date)
            user = f"Next call date: Tuesday {formatted} at 6PM ET\n\nHere is last week's community post:\n\n{compressed}"
            save(
                invite_date + "-weekly-invite.md",
                require(component(self.request("invite", "invite", user))),
            )
        return artifacts


def run_backfill(meetings, call, completed=(), emit=lambda *_: None):
    """Pure batch adapter; durable resume/ingest completion belongs to the job store."""
    results = {}
    for meeting in meetings:
        identity = meeting["id"]
        if identity in completed:
            continue
        try:
            artifacts = Pipeline("transcript_backfill").run(
                meeting["transcript"],
                meeting["date"],
                call,
                emit=lambda name, text: emit(identity, name, text),
            )
            results[identity] = {
                "processing": "succeeded",
                "artifacts": artifacts,
                "indexing": "pending",
            }
        except (PipelineFailure, OutcomeUnknown) as exc:
            results[identity] = {
                "processing": "outcome_unknown"
                if isinstance(exc, OutcomeUnknown)
                else "failed"
            }
    return results

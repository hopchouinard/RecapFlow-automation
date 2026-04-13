---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Designing LLM Routing and Factory Patterns"
speakers: ["Andrew Nanton", "Brandon Hancock"]
chunk_id: "2025-09-16-chunk-032"
---

# Designing LLM Routing and Factory Patterns

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Andrew Nanton discussed challenges in managing single-instance backend processes and file-watching functionality in Electron, while Brandon Hancock suggested implementing an allow-list security approach to prevent redundant process execution. They concluded that shifting from a permissive request model to an allow-list is an effective strategy for controlling backend stability and resource usage.

[00:34:16] Andrew Nanton: It's like, oh, that port's busy.
[00:34:17] Andrew Nanton: I'll just fire up.
[00:34:17] Andrew Nanton: Like, no, no, don't do that.
[00:34:19] Andrew Nanton: That's not what I want.
[00:34:21] Andrew Nanton: Only ever one, like, and then let's do a global lock file.
[00:34:25] Andrew Nanton: Let's do, like, I just only ever run one backend and it has been a losing battle.
[00:34:31] Andrew Nanton: And so I just, so yes, I tried, I tried Electron.
[00:34:37] Andrew Nanton: I got reasonably far with it, but you know, all of them seem to kind of peter out once I get to, you know, I'm using a lot of watchdog based functionality to watch files on disk and then, you know, throw a lot of API calls around and I, yeah.
[00:34:54] Andrew Nanton: Yeah.
[00:34:55] Andrew Nanton: Anyway, I I'm rambling, but that's what I keep running into.
[00:34:58] Brandon Hancock: Yeah.
[00:34:59] Brandon Hancock: Very, very final thing I want to show.
[00:35:00] Brandon Hancock: I know you were saying.
[00:35:02] Brandon Hancock: Basically, you're running into some issues.
[00:35:05] Brandon Hancock: One thing that I always do, I used to just be like, hey, yeah, you can allow every request, like, basically, you know, always work.
[00:35:14] Brandon Hancock: And I changed it to use allow list.
[00:35:17] Brandon Hancock: And I just slowly, as time gone on, allow it to do more things because the exact thing that you're recommending, it would always do npm run dev.
[00:35:26] Brandon Hancock: And I'm like, no, it's already running.

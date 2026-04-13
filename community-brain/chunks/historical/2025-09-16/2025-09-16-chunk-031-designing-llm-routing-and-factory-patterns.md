---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Designing LLM Routing and Factory Patterns"
speakers: ["Andrew Nanton", "Brandon Hancock"]
chunk_id: "2025-09-16-chunk-031"
---

# Designing LLM Routing and Factory Patterns

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Andrew Nanton discussed the challenges of using Electron for interface development, specifically citing persistent issues with backend process management and port conflicts. The pair concluded that while Electron is a powerful tool, it introduces significant technical complexity that exceeds Nanton's current expertise and leads to unreliable application performance.

[00:32:59] Andrew Nanton: Um, and
[00:33:01] Andrew Nanton: It's just not as good.
[00:33:02] Andrew Nanton: mean, one, obviously, like, nothing is going to be as flexible as HTML and JavaScript-based interfaces, and they add a lot of complexity of their own, and that's complexity that Claude knows even less about, and I know zero about.
[00:33:19] Andrew Nanton: So it gets very, very easy to bury myself in complexity.
[00:33:26] Brandon Hancock: Can I ask a few quick questions?
[00:33:27] Brandon Hancock: So, thought on, so you did say Electron.
[00:33:31] Brandon Hancock: That was literally one of the questions I was going to ask.
[00:33:33] Brandon Hancock: I was curious why we're not using Electron everywhere.
[00:33:38] Brandon Hancock: Like, I'm curious why you did not want to go down that approach.
[00:33:45] Andrew Nanton: I tried it.
[00:33:46] Andrew Nanton: I tried it.
[00:33:46] Andrew Nanton: And like, you know, like a lot of the complexity around inter-process communication, managing, managing, starting and stopping the back-end has been a persistent problem in every iteration of this technology.
[00:34:00] Andrew Nanton: starting it.
[00:34:00] Andrew Nanton: you.
[00:34:00] Andrew Nanton: Thank you.
[00:34:00] Andrew Nanton: Thank Thank
[00:34:01] Andrew Nanton: I know this is a solved problem, right?
[00:34:02] Andrew Nanton: Like I know other people know how to do this, but like what I keep running into, no matter how many times I tell Claude or, you know, give instructions or try to wrap the process management around, do not start another instance of the backend.
[00:34:16] Andrew Nanton: It's like, oh, that port's busy.
[00:34:17] Andrew Nanton: I'll just fire up.

---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Deterministic Tool Calling and Logging"
speakers: ["Brandon Hancock"]
chunk_id: "2025-09-02-chunk-095"
---

# Deterministic Tool Calling and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Brandon highlights the effectiveness of LangGraph and LangSmith for agent logging and tracing while advising that agent scalability should be managed by spinning up new sessions or workflows per request rather than relying on PubSub to queue tasks. This architectural approach avoids bottlenecks, ensuring that each incoming request is handled by a fresh, independent agent execution.

[01:51:38] Brandon Hancock: That is, they have agents plus logging to an art.
[01:51:43] Brandon Hancock: Like, every time I see what you can do with that, it blows me away.
[01:51:47] Brandon Hancock: After that, on all other tools, you're pretty much using the agent framework with something else, like, agent ops or something like that to build out a great trace.
[01:51:59] Brandon Hancock: But, I mean, land graph, land smith.
[01:52:03] Brandon Hancock: I'm pumped to dive back into that with you guys just because they've made so much headway.
[01:52:08] Brandon Hancock: It's insane.
[01:52:09] Brandon Hancock: So I'll be doing more on that at some point soon.
[01:52:11] Brandon Hancock: Thank you, Juan, for dropping that.
[01:52:13] Brandon Hancock: yeah, yeah, perfect.
[01:52:16] Brandon Hancock: David, I wanted to real fast go to your question.
[01:52:19] Brandon Hancock: So basically you're saying, am I right in thinking that using PubSub is the right way to ensure that my agent doesn't miss any webhooks if it's busy already?
[01:52:27] Brandon Hancock: So ideally, what you do is you set up your agents in a way that they can scale.
[01:52:34] Brandon Hancock: What I mean by that is every time you send a request to your agents, it should be spinning up a new session, something, so that it's not one agent doing work, and then you have a bottleneck before it.
[01:52:49] Brandon Hancock: So I don't you'll run into that issue because usually what happens, like if you have like a fast API server or something that's sending requests into your agents, every time you get a new request, it's
[01:53:03] Brandon Hancock: You should be calling like agent kickoff, like if you were using Cray, I would kick off an entire new workflow to handle that response.

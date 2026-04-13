---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Deterministic Tool Calling and Logging"
speakers: ["Brandon Hancock", "Hemal Shah", "Jake Maymar"]
chunk_id: "2025-09-02-chunk-091"
---

# Deterministic Tool Calling and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** The participants discussed optimizing system efficiency by offloading deterministic tasks to "before agent callbacks" or custom, non-LLM agents to avoid unnecessary token costs. They concluded that using custom agents—modeled after loop agent patterns—allows for more controlled, code-based execution flow instead of relying solely on model-driven tool calls.

[01:46:36] Brandon Hancock: And then you would just pass in that to the prompt.
[01:46:39] Brandon Hancock: So that's how you even get out of a tool call.
[01:46:41] Brandon Hancock: Because at the end of day, like a tool call is also going to cost you tokens.
[01:46:44] Brandon Hancock: Because it's got to think, make the request, format it, get the response, then think about it, then take action.
[01:46:49] Brandon Hancock: But if there's something that's deterministic, always has to happen, yeah, I would 100% throw it in.
[01:46:54] Brandon Hancock: And a before agent callback is what I would do.
[01:46:59] Jake Maymar: Yeah, that's great.
[01:47:00] Jake Maymar: Thank you.
[01:47:00] Brandon Hancock: That makes a lot of sense.
[01:47:02] Hemal Shah: And.
[01:47:06] Hemal Shah: Jake, what I tried with ADK is, I also created some custom agents, so it doesn't call, this is not LLM agent, it's custom agent, it had to do a lot of processing, but I know it is deterministic, so I use that and that feed that tools calls to that custom agent, so there is no LLM involved, no model calling involved, so that helped me in some of my scenarios that I was trying to do.
[01:47:31] Jake Maymar: Okay, that's interesting too.
[01:47:33] Jake Maymar: Okay, excellent.
[01:47:34] Jake Maymar: Yeah, that will help.
[01:47:36] Brandon Hancock: Cool thing you could use for inspiration, going off of what he just said, is if you look at the agent specifically for like the agent that yields, like the loop agent, you'll see one of the agent steps is to literally run code and yield back a response of should it continue or break.
[01:47:56] Brandon Hancock: So that's a great example of like seeing Google using custom agents to actually actually break.

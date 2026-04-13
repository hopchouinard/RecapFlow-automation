---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Deterministic Tool Calling and Logging"
speakers: ["Brandon Hancock", "Jake Maymar"]
chunk_id: "2025-09-02-chunk-090"
---

# Deterministic Tool Calling and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Jake inquired about ensuring deterministic tool execution in his agent project to avoid failures. Brandon advised bypassing the model's decision-making process by programmatically calling the tool via Python before the model executes, then injecting the result directly into the agent's context.

[01:44:44] Jake Maymar: Hey, so yeah, mostly just kind of in the weeds, trying to figure out just a lot of the admin capabilities for the project that I'm building.
[01:45:01] Jake Maymar: Uh, but actually.
[01:45:03] Jake Maymar: That last conversation was fantastic, because I know I'm going to probably run into that as well.
[01:45:09] Jake Maymar: And I've been doing tool calls, but how, like, is there any way to, and this may be a dumb question, but is there any way to have the model like, only use, um, I guess what I'm trying to say, is there any way to, to have a deterministic, um, tool call that you know is not going to fail?
[01:45:48] Jake Maymar: Um, it, I guess where I'm trying to go is, is, is there, like, if I simplify and simplify and simplify it and and I say, okay, you can use this tool, but if it's just that agent and it only has that tool to use, then it will definitely use that tool.
[01:46:03] Jake Maymar: Does that understand what I'm asking?
[01:46:06] Brandon Hancock: Yeah, mean, so like, I mean, there's a few ways to make it deterministic.
[01:46:09] Brandon Hancock: Option one is just in a callback before the model even kicks off.
[01:46:14] Brandon Hancock: Just literally say, before agent callback, make the agent use the tool.
[01:46:21] Brandon Hancock: Like literally you're dealing with Python at that point.
[01:46:23] Brandon Hancock: So you would literally just go call the tool regularly.
[01:46:26] Brandon Hancock: The result of the tool you would then add to context.
[01:46:29] Brandon Hancock: So you would make the tool call and then say, hey, update state, here's the result.
[01:46:36] Brandon Hancock: And then you would just pass in that to the prompt.

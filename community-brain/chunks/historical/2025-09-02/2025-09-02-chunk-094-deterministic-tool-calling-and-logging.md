---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Deterministic Tool Calling and Logging"
speakers: ["Brandon Hancock", "Jake Maymar", "Juan Torres"]
chunk_id: "2025-09-02-chunk-094"
---

# Deterministic Tool Calling and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** The group discussed best practices for logging and tracing agentic systems, with Juan suggesting a scientific approach of feeding detailed iteration logs back into AI models for debugging. Brandon and Jake concluded that integrating tools like LangGraph and LangSmith provides the most effective "peak" solution for comprehensive traceability and agent monitoring.

[01:50:02] Brandon Hancock: Juan, I think
[01:50:03] Brandon Hancock: You had your hand up, and then I want to address David's question.
[01:50:09] Juan Torres: What's the best to have, like, really good logging mechanisms, because sometimes an agentic system wouldn't work, and so what I try to do now is create kind of like a scientific environment in which each iteration just creates a  ton of logs that tell me the number of tokens, you know, what is the number of, what is it called, I don't know, like the verbose that is being produced per each agentic system, so that helps me then bug, or sometimes I just, like, take the log produced by one iteration and feed it to the chat so that then Cascade can tell me what's wrong.
[01:50:56] Juan Torres: So, I don't know if you had that kind of mechanism to control the behavior of your agentic system.
[01:51:04] Jake Maymar: No, yeah, I have some tracing, and I've been sort of exploring some third-party, but that's a great idea, too.
[01:51:10] Jake Maymar: So, yeah, I appreciate that, definitely.
[01:51:12] Jake Maymar: Yeah, that's the thing is just, like, I know, Brandon, a while back you were talking about, like, tracing land graph and a couple of other things, and I just kind of applied those concepts and had some logs.
[01:51:25] Jake Maymar: But, yeah, I mean, I'd love to refine that more, for sure.
[01:51:30] Brandon Hancock: I will say, just going into, like, traceability and just, like, traceability tier, land graph, land smith is peak.
[01:51:38] Brandon Hancock: That is, they have agents plus logging to an art.
[01:51:43] Brandon Hancock: Like, every time I see what you can do with that, it blows me away.

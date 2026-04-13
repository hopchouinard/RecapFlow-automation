---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Designing LLM Routing and Factory Patterns"
speakers: ["Andrew Nanton", "Brandon Hancock"]
chunk_id: "2025-09-16-chunk-026"
---

# Designing LLM Routing and Factory Patterns

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Andrew Nanton is transitioning from BeeWare Toga to PySide6 for his GUI development while navigating the complexity of integrating multiple LLMs. The discussion centers on establishing an LLM routing and factory pattern to effectively manage API usage between Anthropic and Azure-based models within his report-drafting application.

[00:26:26] Brandon Hancock: What's going on, man?
[00:26:26] Andrew Nanton: What are we working on?
[00:26:28] Andrew Nanton: Um, well, so, uh, I guess the thing that I want to show today, let me see if I can share screen here.
[00:26:36] Brandon Hancock: I'm going to click a button for you.
[00:26:38] Brandon Hancock: Oh, you're good.
[00:26:43] Andrew Nanton: Whole screen or just my, okay.
[00:26:46] Brandon Hancock: You have the report drafter.
[00:26:48] Brandon Hancock: There we go.
[00:26:50] Andrew Nanton: All right.
[00:26:51] Andrew Nanton: So, yeah, I've been back working on, uh, on some of this here.
[00:26:55] Andrew Nanton: Um, some, this, uh, although I, uh, mentioned yesterday, uh,
[00:27:00] Andrew Nanton: Or last week, rather, that the Beware Toga is really convenient for local GUI stuff.
[00:27:11] Andrew Nanton: I'm back to PySide 6 because I just needed some options that weren't possible in the other one.
[00:27:20] Andrew Nanton: So it's got a lot of complexity there, and I feel like I am vibe coding far too much of it, and I'm going to just dig myself into a hole that I can't dig out of.
[00:27:35] Andrew Nanton: But, you know, it's been good so far.
[00:27:38] Andrew Nanton: This is part of what I was asking about with using multiple LLMs, you know, because a part of this I have – so, I mean, the hard part is I have a BAA, a business associate agreement with Anthropic, and then it's included in your Azure subscription, basically.
[00:28:00] Andrew Nanton: where know awful

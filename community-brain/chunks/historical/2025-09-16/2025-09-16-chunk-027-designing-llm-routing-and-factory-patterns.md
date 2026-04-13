---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Designing LLM Routing and Factory Patterns"
speakers: ["Andrew Nanton", "Brandon Hancock"]
chunk_id: "2025-09-16-chunk-027"
---

# Designing LLM Routing and Factory Patterns

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Andrew discussed the challenge of balancing data security and access to model-specific native features (like native PDF handling) while avoiding overly complex business logic integration. To resolve this, they concluded that utilizing a routing library is the most sustainable approach to manage multi-model implementation rather than manually handling individual SDKs.

[00:28:00] Andrew Nanton: where know awful
[00:28:00] Andrew Nanton: But because all of my information has to stay really secure, I can't use something like, what is it, OpenLLM, or what is it, OpenSomething, where I can just use one.
[00:28:14] Brandon Hancock: Yeah, or OpenRouter.
[00:28:15] Andrew Nanton: Yeah, OpenRouter, excuse me.
[00:28:17] Andrew Nanton: So LightLLM, I was looking at that as a library that I can just use and tell it, okay, this one goes to Anthropic, this one goes to.
[00:28:26] Andrew Nanton: And I tried that before, but part of the problem that I had is that I wanted to use some of the native features of the, that were not wrapped in that functionality, like Claude will natively handle sending it a PDF where GPT does not.
[00:28:45] Andrew Nanton: And I think maybe Gemini does now, and I don't know, this stuff changes every 10 minutes, right?
[00:28:50] Brandon Hancock: So it's really hard to keep track.
[00:28:52] Andrew Nanton: So I was like, okay, well, here's what I'm going to do.
[00:28:54] Andrew Nanton: I'm just going to use the native SDK for each one, and then I know that I can get all the features that I want.
[00:29:00] Andrew Nanton: But then I end up having to manage all of that in the business logic.
[00:29:04] Andrew Nanton: Well, if it's a PDF, then this time you do that.
[00:29:07] Andrew Nanton: it just like the complexity gets really overwhelming really quickly.
[00:29:12] Brandon Hancock: And so I think I'm just going to have to fall back to a library that handles all of it.
[00:29:18] Brandon Hancock: So do you want a quick tech deep dive?

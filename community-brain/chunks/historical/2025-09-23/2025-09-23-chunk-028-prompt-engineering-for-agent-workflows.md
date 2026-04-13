---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Prompt engineering for agent workflows"
speakers: ["Brandon Hancock", "Jahangir Jadi"]
chunk_id: "2025-09-23-chunk-028"
---

# Prompt engineering for agent workflows

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Jahangir is developing an agentic workflow using ADK to validate user queries, extract information, and classify events, but he is encountering issues with multi-agent transitions and implementing fallback logic. The discussion focuses on these technical hurdles, specifically how to properly chain agents to handle invalid queries and ensure flow continuity.

[00:35:35] Brandon Hancock: I'm not even going to say it.
[00:35:36] Brandon Hancock: think I'm going to Jahangir.
[00:35:39] Brandon Hancock: I don't know how to say it.
[00:35:41] Brandon Hancock: Jahangir.
[00:35:42] Brandon Hancock: All How are you doing, buddy?
[00:35:44] Brandon Hancock: I'm really great, thank you.
[00:35:46] Brandon Hancock: So quick question.
[00:35:48] Brandon Hancock: I see you are working on some agent workflows.
[00:35:51] Jahangir Jadi: Are we doing ADK?
[00:35:54] Brandon Hancock: Yeah.
[00:35:55] Brandon Hancock: Okay, ADK.
[00:35:56] Brandon Hancock: Would you mind explain a little bit what's going on so we can...
[00:35:58] Jahangir Jadi: Yeah, basically I'm creating a system.
[00:36:01] Jahangir Jadi: where a user will enter a query and the system is going to first identify if it is correct or not, means if it is complete or not.
[00:36:12] Jahangir Jadi: Secondly, it is going to extract some information from it, like the names and dates, these kind of things.
[00:36:20] Jahangir Jadi: And in the last, it is going to classify the event based on the template, which I'm going to provide.
[00:36:27] Jahangir Jadi: So what happens is, I have created a flow, but my first agent works fine, but it doesn't go to the second agent.
[00:36:36] Jahangir Jadi: If I work like a normal flow with sub-agents, if I use the agent as tools, then it kind of works, but it does not work with fallback.
[00:36:52] Jahangir Jadi: Like for example, if you can read, for example, if there is an invalid query, I want to stop that agent.

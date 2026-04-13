---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Prompt engineering for agent workflows"
speakers: ["Brandon Hancock", "Jahangir Jadi"]
chunk_id: "2025-09-23-chunk-029"
---

# Prompt engineering for agent workflows

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** To address the issue of invalid user queries stalling agent workflows, Brandon advised implementing a phased approach within the ADK (Agent Development Kit). By structuring prompts to force the agent to validate information before moving to the next step, users can ensure process stability and accuracy.

[00:36:52] Jahangir Jadi: Like for example, if you can read, for example, if there is an invalid query, I want to stop that agent.
[00:37:01] Jahangir Jadi: Right there and ask the user to enter the query again so that the process can work fine.
[00:37:08] Brandon Hancock: Yeah.
[00:37:09] Brandon Hancock: So let me share my screen.
[00:37:11] Brandon Hancock: I can help out.
[00:37:12] Brandon Hancock: So this, most of this is a prompting, prompt engineering issue with ADK.
[00:37:19] Brandon Hancock: So here, so here's like the main agent that we have in the root of like the example project for Shipkit.
[00:37:26] Brandon Hancock: So the main suggestion I have for you is ADK loves phased approaches.
[00:37:33] Brandon Hancock: Loves them.
[00:37:34] Brandon Hancock: Like I cannot express it enough.
[00:37:36] Brandon Hancock: So, so you can see here, I'm basically doing the exact same thing that you're asking about, which is like phase one, gather information.
[00:37:45] Brandon Hancock: You specifically tell it what it needs to look for and, you know, and basically just say like, you know, don't proceed to the next step until you're good to go.
[00:37:55] Brandon Hancock: So, cannot express enough.
[00:37:58] Brandon Hancock: Doing phased approaches like this.
[00:38:01] Brandon Hancock: It's an absolute game changer.
[00:38:03] Brandon Hancock: And, yeah, if you go look at all of the example ADK samples that ADK has provided, all of them use this.
[00:38:10] Brandon Hancock: It's just, it works the best.
[00:38:12] Brandon Hancock: And you can basically say, like, hey, ask these questions, don't proceed until we're good to go to the next one, and so forth.

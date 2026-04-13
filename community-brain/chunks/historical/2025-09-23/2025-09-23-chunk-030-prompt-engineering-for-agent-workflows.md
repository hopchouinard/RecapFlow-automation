---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Prompt engineering for agent workflows"
speakers: ["Brandon Hancock", "Jahangir Jadi"]
chunk_id: "2025-09-23-chunk-030"
---

# Prompt engineering for agent workflows

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Brandon and Jahangir discussed the implementation of agent workflows, specifically debating whether to use subagents or the "agent-as-tool" pattern in the ADK framework. Brandon concluded that the agent-as-tool approach is ideal for tasks requiring a quick handoff where another agent acts as a function to return specific results to the root agent.

[00:38:12] Brandon Hancock: And you can basically say, like, hey, ask these questions, don't proceed until we're good to go to the next one, and so forth.
[00:38:19] Brandon Hancock: But I think that answered part of your question.
[00:38:21] Jahangir Jadi: I think there was something else I was missing, though.
[00:38:23] Jahangir Jadi: Yeah, but what is the recommended way?
[00:38:25] Jahangir Jadi: Should I do it with the tools, or should I do it the normal way with the subagents?
[00:38:31] Brandon Hancock: So, just to make sure I'm on the same page, so we have a root agent, your root agent is going to ask questions, and then after it asks questions, you're saying, how do you start to delegate to the next agents?
[00:38:43] Brandon Hancock: Or, I guess I'm confused on the question.
[00:38:46] Jahangir Jadi: Yeah, we have two options for doing that now.
[00:38:49] Jahangir Jadi: Either we can with subagents, or either we can use the agents as tools.
[00:38:55] Brandon Hancock: Right, so there's two options.
[00:38:58] Brandon Hancock: And I'll break down when you want to do each.
[00:39:02] Brandon Hancock: So option one is when you want to do tools, so the way tools work when working with ADK is agent as tool, what happens is your root agent will say, hey, I need help on this, it instantly literally treats your agent like a function is the best way I can describe it.
[00:39:23] Brandon Hancock: So what that means is it's going to just like pass over a query, this agent's going to do whatever it needs to do, and instantly return the results back to the agent that called it, and that's it.

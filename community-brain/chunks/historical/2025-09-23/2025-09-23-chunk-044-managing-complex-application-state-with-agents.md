---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing complex application state with agents"
speakers: ["Brandon Hancock"]
chunk_id: "2025-09-23-chunk-044"
---

# Managing complex application state with agents

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** To manage complex agent workflows, Brandon Hancock advises breaking tasks into small, actionable steps and iteratively saving results into a persistent state. He concludes that using an "agent document"—a digital twin mapping the hierarchy of root and sub-agents—significantly simplifies development by making the workflow easier for the agent to reference.

[00:54:34] Brandon Hancock: So I just, like, I try to chunk things down into as many small, actionable pieces as possible, and use state as my best friend.
[00:54:43] Brandon Hancock: Because the second I get good results, I instantly throw it into state.
[00:54:47] Brandon Hancock: And then I move on to the next, like, super small task, instantly throw it in state.
[00:54:52] Brandon Hancock: And then towards the end, use it and put it all together to do whatever you want.
[00:54:57] Brandon Hancock: So, like, that's how I like to try and think about it.
[00:55:00] Brandon Hancock: And that's been insanely helpful for a
[00:55:01] Brandon Hancock: Like helping me build agents really quickly.
[00:55:04] Brandon Hancock: I'll show you one other thing that's going to make your life so much easier.
[00:55:08] Brandon Hancock: One second.
[00:55:11] Brandon Hancock: One other screen to show.
[00:55:15] Brandon Hancock: One thing that I really have been doing to make my life so much easier when building ADK agents is basically come up with a agent document.
[00:55:26] Brandon Hancock: And what this agent document does is it keeps track.
[00:55:29] Brandon Hancock: It's basically like a digital twin of my true agent workflow.
[00:55:34] Brandon Hancock: What I mean by that is, like, if you look inside of my actual agents, you'll see that I have, like, one root agent.
[00:55:43] Brandon Hancock: Then I have sub-agents.
[00:55:45] Brandon Hancock: All of these sub-agents do stuff.
[00:55:47] Brandon Hancock: Well, that's awful for my actual code to understand.
[00:55:51] Brandon Hancock: Like whenever I'm performing a task, that's so hard for my agent, like when I'm working and programming, for it to, like, redo a thousand files to figure out how it all connects.

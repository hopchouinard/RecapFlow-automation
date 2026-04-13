---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing complex application state with agents"
speakers: ["Brandon Hancock"]
chunk_id: "2025-09-23-chunk-043"
---

# Managing complex application state with agents

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Brandon Hancock outlines an "ADK" (Agents, Delegation, Knowledge) framework for managing complex state by breaking workflows into granular, single-task agent actions. He utilizes sequential pipelines and loop workflows to ensure each agent processes specific tasks while maintaining state across delegated steps.

[00:53:10] Brandon Hancock: Right?
[00:53:11] Brandon Hancock: Okay, cool.
[00:53:13] Brandon Hancock: Let me share screens.
[00:53:20] Brandon Hancock: Yeah, okay, so here's, I'm gonna show you two screens that I, what I do whenever I'm working on agents to help like me brainstorm.
[00:53:27] Brandon Hancock: Okay, so I like to draw stuff out.
[00:53:31] Brandon Hancock: And I am constantly thinking in different, thinking in ADK, like that's the way I like to describe it.
[00:53:39] Brandon Hancock: It's like, by thinking in ADK, I'm thinking, I need to have agents.
[00:53:43] Brandon Hancock: Every time I'm working on an agent, I can give that agents tools, I can give that agent callbacks.
[00:53:50] Brandon Hancock: And I have a few other tools at my disposal, such as sequential pipelines and loop workflows.
[00:53:57] Brandon Hancock: So like, once I understand all the different puzzle pieces, what I usually try and do is just ...
[00:54:01] Brandon Hancock: So out exactly what each agent wants to do.
[00:54:05] Brandon Hancock: Like, how can I make sure each one of my agents is doing one task?
[00:54:09] Brandon Hancock: So that's, like, how I like to break apart stuff.
[00:54:11] Brandon Hancock: So, like, for example, I made a YouTube workflow processor that basically asked me questions in a phased approach.
[00:54:22] Brandon Hancock: From there, it starts to delegate to an agent.
[00:54:26] Brandon Hancock: This agent is going to then write a title and hook, save the state, and then automatically gets delegated to the next one.
[00:54:34] Brandon Hancock: So I just, like, I try to chunk things down into as many small, actionable pieces as possible, and use state as my best friend.

---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing complex application state with agents"
speakers: ["Alex Wilson", "Brandon Hancock"]
chunk_id: "2025-09-23-chunk-042"
---

# Managing complex application state with agents

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** To address the challenge of managing complex agent state without overwhelming LLM context windows, Brandon Hancock advises decomposing tasks, similar to breaking down complex code into smaller subclasses. He concludes that if an agent's instructions become too dense to track, the system should be modularized to maintain performance.

[00:51:57] Brandon Hancock: Yeah.
[00:51:57] Alex Wilson: But in a hundred percent in production, trying to now pass those around and of
[00:52:01] Alex Wilson: Maintaining like it's it's more in design of like trying to figure that out without overloading the context window of any any individual LM where it's just all of a sudden going haywire.
[00:52:10] Brandon Hancock: Yeah, that's that's the key reason why I say break stuff down is just because this like the second you have too many instructions back to back to back, it's going to it will just not perform as expected, like it might do if you gave it seven instructions, it might do four.
[00:52:24] Brandon Hancock: So anytime I'm like, it's almost like you're doing like regular software development.
[00:52:28] Brandon Hancock: It's like the second this class is getting a little too complex, we probably need to make two subclasses in the world of agents, the second this one agents getting a little too complex and I couldn't just do a simple checklist to check things off.
[00:52:40] Brandon Hancock: I know I need to break things up.
[00:52:43] Brandon Hancock: Quick, I want to show you this real fast, because this is what literally I did inside of project recently to get my agents working.
[00:52:52] Brandon Hancock: So I'm gonna show you two different screens really fast.
[00:52:57] Brandon Hancock: This is this will be helpful, so I'm going to pull this up.
[00:52:59] Brandon Hancock: We're.
[00:53:00] Brandon Hancock: We're.
[00:53:01] Brandon Hancock: Where is it at?
[00:53:03] Brandon Hancock: Too many screens.
[00:53:10] Brandon Hancock: Right?
[00:53:11] Brandon Hancock: Okay, cool.
[00:53:13] Brandon Hancock: Let me share screens.

---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing complex application state with agents"
speakers: ["Alex Wilson", "Brandon Hancock"]
chunk_id: "2025-09-23-chunk-045"
---

# Managing complex application state with agents

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** To manage complex state across multiple agents, Brandon Hancock recommends creating a "digital twin" documentation file that maps agent roles, data dependencies, and state flow to prevent ripple-effect errors. He explains that this documentation, which is automatically generated and updated by agents within his "ShipKit" framework, is essential for maintaining stability in complex, multi-agent systems.

[00:55:51] Brandon Hancock: Like whenever I'm performing a task, that's so hard for my agent, like when I'm working and programming, for it to, like, redo a thousand files to figure out how it all connects.
[00:56:01] Brandon Hancock: What I really recommend when you're doing anything that is working with multiple agents, to build something like this, where you have a digital twin of your entire workflow, calls out what all the agents do, what state they read, what state they write, what models they use, and not only do you call it out for every agent, you also have like a nice little list of how everything works together, so that when you are making a change, like, like, this is what we show in ship kit, but like, when you do make a change to state up here, it instantly knows by looking at this document, oh, if you change state for agent one, this is going to completely destroy agents three, four, and five down here, because if you just try doing agent development kit and building agents one at a time, dude, it's going to, the second you get to complex state management, things are just going to ripple and break, so that's why I recommend you're creating one, you're of,
[00:57:03] Brandon Hancock: And as you build, update the document, as you build, update the document, and that's just going to make it so much easier when you're building agents.
[00:57:10] Brandon Hancock: So this is the only way I've been able to build bigger complex agents quickly.
[00:57:14] Alex Wilson: So hopefully that's...
[00:57:15] Alex Wilson: And that MD file, sorry, this may be a dumb question, but are you doing that manually?
[00:57:19] Brandon Hancock: Or is that like a cursor agent writing that in the background?
[00:57:23] Brandon Hancock: Yeah, so this is part of ShipKit.
[00:57:26] Brandon Hancock: I've never written a single line for all of ShipKit.
[00:57:29] Brandon Hancock: Agents do everything.

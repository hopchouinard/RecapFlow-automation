---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing complex application state with agents"
speakers: ["Alex Wilson", "Brandon Hancock"]
chunk_id: "2025-09-23-chunk-041"
---

# Managing complex application state with agents

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** To manage complex application state, Brandon suggests breaking data into distinct, structured objects and using specialized agents to process them, culminating in a "composer agent" that merges the final output. The discussion identifies that the primary challenge lies in the design phase, specifically regarding concerns that current JSON structures will not scale to handle full-capacity data requirements.

[00:50:38] Alex Wilson: And that would, you would just break those into different objects, like state objects?
[00:50:42] Brandon Hancock: Yes.
[00:50:43] Brandon Hancock: Yeah, that's, that's literally what I would do is, like, I would have an exterior, like, in-state, I would literally have, like, exterior, exterior bill of materials, bomb.
[00:50:51] Brandon Hancock: And then that would, I would have a structured output for, hey, everything in this list, it needs to have, you know, it sounds like a name, a quantity, a price, and stuff like that.
[00:51:01] Brandon Hancock: All You
[00:51:02] Brandon Hancock: Then each agent would work on just that one final part, and then towards the end you could have like a composer agent, like a report composer agent, that would look at all of the different states and put them together in one final version.
[00:51:19] Brandon Hancock: That's one way you could do it.
[00:51:23] Brandon Hancock: Yeah, there's, there's, there's multiple ways we could tackle it.
[00:51:25] Brandon Hancock: One question I would have for you is where, where are we getting stuck right now?
[00:51:28] Brandon Hancock: Is it like, are we getting stuck in the archetype?
[00:51:31] Brandon Hancock: Like, are we getting stuck designing it?
[00:51:33] Brandon Hancock: Or are we have it, we have it running, but it's hitting a, an issue or where is it, where is it at?
[00:51:38] Alex Wilson: It's, well, it's mostly in design.
[00:51:40] Alex Wilson: Um, it's in design because, uh, right now in design and my fear right now is like the JSON, if you look at the JSON doc that's being produced by like any given one, like in testing, I'm giving it a fraction of what it's going to have to manage, call it like 50%.
[00:51:57] Brandon Hancock: Yeah.

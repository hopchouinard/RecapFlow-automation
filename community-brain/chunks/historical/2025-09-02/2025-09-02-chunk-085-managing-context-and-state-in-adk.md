---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing Context and State in ADK"
speakers: ["Brandon Hancock", "Ola Oyo"]
chunk_id: "2025-09-02-chunk-085"
---

# Managing Context and State in ADK

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Brandon Hancock recommends using the "before LLM callback" in ADK to programmatically inject dynamic state for routine procedures, while Ola Oyo discusses managing context by limiting session events to a set number. The coach concludes by offering a follow-up debugging session to refine these context management strategies in practice.

[01:39:54] Brandon Hancock: So there's before LLM callback, which is where like, hey, I'm literally about to pass information into the LLM call at that point.
[01:40:03] Brandon Hancock: You can either, you can say, like, right then and there, you could look at what user's doing, what agent we're at, and you could figure out what's going on, and programmatically add in, like, dynamic state.
[01:40:17] Brandon Hancock: That's one way you could do it.
[01:40:19] Brandon Hancock: Would definitely recommend that, especially if it's a very routine procedure.
[01:40:23] Brandon Hancock: Like, step B always needs these three things.
[01:40:26] Brandon Hancock: Yeah, you could use the before callback.
[01:40:28] Brandon Hancock: Would definitely recommend that as well.
[01:40:30] Brandon Hancock: I mean, also, too, at a certain point, if you ever want to just, on a call, if you want to, you know, share what's going on in ADK, happy to real-world debug with you and just say, like, cut this, add this, tweak that, just to help save you some time.
[01:40:47] Ola Oyo: Yeah, sure.
[01:40:47] Ola Oyo: That'll be pretty cool.
[01:40:49] Ola Oyo: Another thing I was thinking was, because my ADK is able to see, like, two different types of contexts.
[01:40:55] Ola Oyo: One is, I've put, like, a limiter on how many of the events in each session.
[01:41:02] Ola Oyo: You're not when Irend in amount.
[01:41:03] Ola Oyo: I'm
[01:41:03] Ola Oyo: So you can go back and look at maybe eight events to have an idea of, OK, this is what I've been talking about.
[01:41:08] Ola Oyo: And then I also have the states.

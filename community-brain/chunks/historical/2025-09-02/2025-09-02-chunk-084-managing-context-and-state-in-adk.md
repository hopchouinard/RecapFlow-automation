---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing Context and State in ADK"
speakers: ["Brandon Hancock", "Ola Oyo"]
chunk_id: "2025-09-02-chunk-084"
---

# Managing Context and State in ADK

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Brandon suggests managing ADK state by interpolating critical, persistent context directly into the agent prompt while using specific tools to fetch additional data as needed to reduce token bloat and improve accuracy. To implement this, he recommends utilizing callback functions, particularly "before LLM" callbacks, to inject relevant information dynamically right before each model call.

[01:38:35] Brandon Hancock: For example, like, if I need to know the current state, the current user, what phase are we at?
[01:38:40] Brandon Hancock: I need to know, I'm doing a feedback loop, so I need to add in feedback.
[01:38:45] Brandon Hancock: Like, things that always have to be there, boom, always do interpolation into the agent prompt itself to make sure the information is always there.
[01:38:54] Brandon Hancock: Outside of that, I usually try to create tools tools to help me fetch information.
[01:39:00] Brandon Hancock: So, for example, if the agent feels like it needs to...
[01:39:03] Brandon Hancock: If get additional user order history or user something, I mean, I give it as many tools as possible so that it can get the context when it needs it, and this will actually help reduce tokens in a weird way because as these models increase in tokens, it's not as clear to them all the time what they actually need to be doing.
[01:39:25] Brandon Hancock: So if you actually watch behind the scenes, sometimes it might take a few extra turns or cycles to get to the right answer.
[01:39:31] Brandon Hancock: So that's why I try to keep it as lean as possible to improve results.
[01:39:37] Brandon Hancock: So that, yeah, that would be the advice.
[01:39:42] Brandon Hancock: So, yeah, key advice on that one.
[01:39:45] Ola Oyo: Is that something callbacks can help with, like the before and after?
[01:39:50] Brandon Hancock: Yeah, 100%.
[01:39:51] Brandon Hancock: Yeah, so what you can, there's multiple ways you can use callbacks.
[01:39:54] Brandon Hancock: So there's before LLM callback, which is where like, hey, I'm literally about to pass information into the LLM call at that point.

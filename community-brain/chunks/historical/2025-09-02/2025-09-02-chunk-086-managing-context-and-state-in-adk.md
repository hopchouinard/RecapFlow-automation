---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing Context and State in ADK"
speakers: ["Brandon Hancock", "Ola Oyo"]
chunk_id: "2025-09-02-chunk-086"
---

# Managing Context and State in ADK

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Ola Oyo questioned whether to rely on session events rather than state to conserve tokens, but Brandon Hancock emphasized that maintaining state is essential for context management. Brandon recommended using surgical state strategies—such as implementing a dynamic dictionary of tasks similar to Cursor—to store and retrieve information just-in-time rather than passing all data into the prompt.

[01:41:08] Ola Oyo: And then I also have the states.
[01:41:10] Ola Oyo: Would it make sense to sort of, if I don't want to block my token count, maybe not have the states and then just focus on all the events that sits in the session so it's able to go through it and say, OK, this is what we're talking about and then continue?
[01:41:24] Ola Oyo: Or is that state needed specifically if it's swinging between different tools to get that context across?
[01:41:32] Brandon Hancock: I lean so much more on state is usually what I do.
[01:41:38] Brandon Hancock: So, like, yeah.
[01:41:40] Brandon Hancock: So, I mean, here's like a few clever ways you can use state and you can just take inspiration from real applications we use.
[01:41:47] Brandon Hancock: So, for example, Cursor.
[01:41:48] Brandon Hancock: If you look at what Cursor is doing, they have a dynamic pool, which is a dictionary of tasks in which order they need to be accomplished.
[01:41:57] Brandon Hancock: So, like, if there are certain things that, like, let's just imagine, like, I need to keep reminding myself.
[01:42:03] Brandon Hancock: So if about what I'm working on, like you could literally use, you could use the model to help save like short term memory in state.
[01:42:13] Brandon Hancock: It's like there's, there's a thousand great creative ways you can use date in order to, to basically remember the information just in time and use the information just in time.
[01:42:24] Brandon Hancock: Because the easy button is to just pass everything from state into the prompt.
[01:42:30] Brandon Hancock: But that's going to, it's going to blow things up so fast.
[01:42:33] Brandon Hancock: So we have to be surgical.
[01:42:35] Brandon Hancock: So that's why there's, yeah.

---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Private Authentication and ADK Technical Issues"
speakers: ["Brandon Hancock"]
chunk_id: "2025-09-16-chunk-071"
---

# Private Authentication and ADK Technical Issues

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon critiqued the current ADK setup for requiring redundant custom dynamic routing, recommending a simplified, Vercel AI SDK-style integration instead. Due to ongoing issues with streaming, he advised using a "cheat code" of handling agent engine queries synchronously until a more streamlined solution is available.

[01:20:43] Brandon Hancock: You're making every single user who wants to play and use ADK to have to build out custom dynamic routing between production and dev, that's, and not, and every single person has to solve the same problem.
[01:20:56] Brandon Hancock: Like, this is, this is awful, the way that it's been set up.
[01:20:59] Brandon Hancock: So, I, the goal, like, my, like, recommendation.
[01:21:02] Brandon Hancock: It'll be cool if they do it.
[01:21:03] Brandon Hancock: It'll be very cool.
[01:21:04] Brandon Hancock: But like, it should be like Vercel AI SDK to where I literally just like install it.
[01:21:09] Brandon Hancock: And then I send the request to that hook.
[01:21:11] Brandon Hancock: And then it, it does all the routing.
[01:21:14] Brandon Hancock: Like, that's what it should be.
[01:21:15] Brandon Hancock: So yeah, in the meantime, so yeah, so that's what is happening.
[01:21:19] Brandon Hancock: And fingers crossed, they'll, they'll do that because right now, yeah, you're totally right.
[01:21:26] Brandon Hancock: And then one other thing, streaming is still broken.
[01:21:30] Brandon Hancock: So if you want to do it, you have to, you have to handle stuff synchronously.
[01:21:34] Brandon Hancock: I haven't built out in ShipKit for like the one of the prebuilt templates.
[01:21:41] Brandon Hancock: And it works really well.
[01:21:42] Brandon Hancock: But the cheat code is, we can actually go even simpler than I did in that YouTube video, where you do server side, you do stream query, when you're working with an agent engine, but you just wait for it to send all the information, then you just send it back as a synchronous method.
[01:22:00] Brandon Hancock: Yeah, it's kind of gross.

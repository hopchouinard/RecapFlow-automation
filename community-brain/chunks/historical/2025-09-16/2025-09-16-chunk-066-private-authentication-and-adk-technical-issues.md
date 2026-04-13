---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Private Authentication and ADK Technical Issues"
speakers: ["Brandon Hancock", "Hemal Shah"]
chunk_id: "2025-09-16-chunk-066"
---

# Private Authentication and ADK Technical Issues

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Hemal is seeking recommendations for securing a private, employee-facing back-office automation application deployed on Vercel and ADK. The discussion focuses on implementing authentication mechanisms, such as NextAuth, to restrict access instead of keeping the application public.

[01:14:31] Brandon Hancock: I think, Hemal, you're up next, buddy.
[01:14:34] Brandon Hancock: It goes, Hemal, likes Adam, Morgan.
[01:14:39] Brandon Hancock: So, Hemal, you're up, buddy.
[01:14:41] Hemal Shah: Hey.
[01:14:42] Hemal Shah: So, for my back office automation project, taking now to the, thinking more about the production levels, the local testing and everything is good.
[01:14:53] Hemal Shah: So, that's where the Varsal and ADK deployment, I did it last week.
[01:14:59] Hemal Shah: And I was wondering now, how do I.
[01:15:02] Hemal Shah: Protect web, like username, password, or certain ways so that it's put some authentication in front of it.
[01:15:11] Hemal Shah: So if there's recommendation of, mean, there is next auth, and I saw a couple of things, but if there's recommendation on standard username, password, or something to protect our web applications.
[01:15:24] Brandon Hancock: So wait, so the questions on, like, the web app, how do we keep it secure, or?
[01:15:29] Hemal Shah: Yeah, web app, username, password, product type, production, so it's not, because it's a back office automation, it is only, I want to give access to certain employees of the company who can go in and do certain things.
[01:15:42] Hemal Shah: It's not for a public site, in a way.
[01:15:48] Brandon Hancock: Okay, yeah, ooh, okay, so it is a private application, so that, I was like, man, just log in with Gmail, what do you mean?
[01:15:55] Brandon Hancock: It's a, but no, I see what you're saying.
[01:15:58] Brandon Hancock: Okay, so one option that works really well.

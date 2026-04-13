---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Private Authentication and ADK Technical Issues"
speakers: ["Brandon Hancock", "Hemal Shah"]
chunk_id: "2025-09-16-chunk-070"
---

# Private Authentication and ADK Technical Issues

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon explained that the authentication process will automatically generate the necessary database tables, while Hemal highlighted technical inconsistencies between local and production ADK deployments regarding URLs and payloads. They concluded that developers must currently implement custom dynamic routing to manage these environment discrepancies until a more standardized solution is available.

[01:19:41] Brandon Hancock: which is good.
[01:19:42] Brandon Hancock: Okay.
[01:19:42] Brandon Hancock: Yeah.
[01:19:44] Brandon Hancock: Cool.
[01:19:45] Brandon Hancock: Yeah.
[01:19:45] Brandon Hancock: What it'll do, it'll just make a new authentication table.
[01:19:47] Brandon Hancock: It'll make new tables in your, whatever database you're using, and then you'll be good to go.
[01:19:52] Hemal Shah: Okay.
[01:19:53] Brandon Hancock: Yeah, of course.
[01:19:54] Hemal Shah: One more observation, Brandon, is with ADK server, when you, when we deploy it in, in Edge.
[01:20:02] Hemal Shah: An engine, it has a different URL, like a stream query, something, and then the payload is class method.
[01:20:09] Hemal Shah: But when I locally doing ADK API server, it is run SSC and it is a different URL, different payload.
[01:20:17] Hemal Shah: Disgusting.
[01:20:19] Hemal Shah: I'm wondering, so that's a limitation right now, correct?
[01:20:22] Hemal Shah: So the client, if I want to test a local agent, then I have to have, I think in your video tutorial, had that both, if else, we have to live with it until So, okay, all right.
[01:20:34] Brandon Hancock: I, so what I want to just quickly say is, so like, whenever I got to go out to, to like, hang out with them for a little bit, this was my biggest complaint.
[01:20:41] Brandon Hancock: I was like, this is disgusting.
[01:20:43] Brandon Hancock: You're making every single user who wants to play and use ADK to have to build out custom dynamic routing between production and dev, that's, and not, and every single person has to solve the same problem.

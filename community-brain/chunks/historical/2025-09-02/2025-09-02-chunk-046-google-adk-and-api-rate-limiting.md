---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Google ADK and API Rate Limiting"
speakers: ["Brandon Hancock", "James Rennie"]
chunk_id: "2025-09-02-chunk-046"
---

# Google ADK and API Rate Limiting

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** James Rennie reported an issue where his integration with the Yahoo Finance API is triggering immediate rate-limiting errors when invoked by the model during his work on the Google ADK project. The participants briefly discussed the problem, with Brandon Hancock offering to debug the issue via screen share.

[00:56:29] Brandon Hancock: How you doing, James?
[00:56:31] Brandon Hancock: I think it has you muted.
[00:56:34] James Rennie: Good morning.
[00:56:34] James Rennie: I'm doing well.
[00:56:36] Brandon Hancock: Where are you calling from?
[00:56:38] James Rennie: From Vietnam.
[00:56:40] Brandon Hancock: Oh, wow.
[00:56:40] James Rennie: Man, that's a...
[00:56:42] Brandon Hancock: yeah.
[00:56:42] Brandon Hancock: It's getting nighttime over there.
[00:56:44] Brandon Hancock: Morning for you.
[00:56:45] Brandon Hancock: That's awesome.
[00:56:45] James Rennie: I'm to have you on the call.
[00:56:47] James Rennie: Yeah, we started at 4 a.m.
[00:56:48] Brandon Hancock: Yeah.
[00:56:50] Brandon Hancock: That's wild.
[00:56:50] Brandon Hancock: You're a trooper, man.
[00:56:52] Brandon Hancock: What are we working on?
[00:56:53] James Rennie: How can we help?
[00:56:54] James Rennie: I'm working on the ADK video.
[00:56:58] James Rennie: Yeah.
[00:56:59] James Rennie: Yeah.
[00:57:00] James Rennie: I think the only thing I've...
[00:57:01] James Rennie: What ran into is when it was trying to run the function for calling Yahoo Finance, I think the model must be calling it because I get rate-limited immediately.
[00:57:20] Brandon Hancock: Do you want to share your screen?
[00:57:22] Brandon Hancock: I'd be curious if could dive in, if you want to look at it.
[00:57:27] James Rennie: Yeah, I don't have that open right now.

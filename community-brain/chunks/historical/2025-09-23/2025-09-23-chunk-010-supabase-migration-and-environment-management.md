---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Supabase migration and environment management"
speakers: ["Brandon Hancock", "Ty Wells"]
chunk_id: "2025-09-23-chunk-010"
---

# Supabase migration and environment management

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Brandon Hancock and Ty Wells discussed the necessity of maintaining separate, safe staging and production environments in Supabase to protect live users while developing new features. They concluded that Ty needs a strategy to migrate edge functions and data from his current setup to a clean production environment without disrupting active operations.

[00:15:39] Brandon Hancock: So, let me just share my screen really fast.
[00:15:43] Brandon Hancock: And I'll just show, I don't want to show anything I'm not supposed to.
[00:15:49] Brandon Hancock: Okay, cool.
[00:15:50] Ty Wells: You're supposed to show everything.
[00:15:54] Brandon Hancock: I'm I'm going to leak someone's something that I'm not supposed to.
[00:15:57] Brandon Hancock: So, gotta be, gotta be careful.
[00:16:00] Brandon Hancock: But...
[00:16:01] Brandon Hancock: Okay, so like when using Supabase, the main thing that you want to do is, and just to put everyone else on context with where you're at in this process, is when building a real-world application, you really want to have a production environment that is safe and stable for your customers and clients, okay?
[00:16:21] Brandon Hancock: Now, the second thing that you want to do is create basically like a staging development environment where you can completely destroy, mess up, and it does not impact your users.
[00:16:31] Brandon Hancock: So, the issue that Ty is running into is, as you were building out your main application, lot of, and correct me if I'm wrong, Ty, but a lot of everything that probably got set up was related to staging, and now that you're working on main, it's like, do I copy data over?
[00:16:48] Brandon Hancock: Do I clean everything up, do I delete it, so that's, that's the, the hard part, right, that's where you're at?
[00:16:56] Ty Wells: Yeah, yeah, so, yeah, that's where I'm at, and obviously you don't want to touch production.
[00:17:00] Ty Wells: I have branches set up, and yes, exactly where we're at here in terms of, but more so my edge functions, the issues, because, you know, can't make those changes on production, it's not going to end well.

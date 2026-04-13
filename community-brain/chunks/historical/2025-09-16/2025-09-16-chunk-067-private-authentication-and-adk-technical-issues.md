---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Private Authentication and ADK Technical Issues"
speakers: ["Brandon Hancock", "Hemal Shah"]
chunk_id: "2025-09-16-chunk-067"
---

# Private Authentication and ADK Technical Issues

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** To address the client's private authentication needs, Brandon suggests disabling public sign-ups entirely and instead implementing a restricted "invite-only" workflow. By leveraging the specific invite functionality within the user's chosen authentication provider, the application ensures access remains limited to authorized users.

[01:15:55] Brandon Hancock: It's a, but no, I see what you're saying.
[01:15:58] Brandon Hancock: Okay, so one option that works really well.
[01:16:02] Brandon Hancock: Is you can actually had to do this for one of our client project, it is basically, you can set up an invite, you basically you can invite, so let me pull up something real fast on Supabase, because you're using Supabase, or no, you went with a different platform.
[01:16:17] Brandon Hancock: I can't remember what you did for auth.
[01:16:19] Hemal Shah: I'm using, so I'm not using database yet, it is mostly kind of a agentic solution, just getting some files in the file comparison, if you remember, data, data, data reconciliation.
[01:16:33] Brandon Hancock: Okay, they have, I'm trying to find it really fast, and I'll show you, but yeah, here's what you can do, let me share this screen, I just want make sure I'm not sharing anything I'm not supposed to.
[01:16:49] Brandon Hancock: Okay, cool, so this is just like a random, this is what you could do in Supabase, but you could just copy it over directly to your project, but inside of Supabase, you can get to pick how, like, what are the different ways you want people to, to,
[01:17:03] Brandon Hancock: So like, what are the different sign in policies, obviously, email, like, that's just a known, however, the main thing that you change is you actually get rid of the sign up page, like you just do not allow people to sign up for your application, instead, user functionality.
[01:17:23] Brandon Hancock: So basically, if people can't sign up, then there's no way that they can join your application.
[01:17:28] Brandon Hancock: So that's just a very quick workaround, to where you basically just have to work on the invite user workflow in whichever authentication provider you're using.

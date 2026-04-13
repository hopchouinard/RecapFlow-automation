---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Supabase migration and environment management"
speakers: ["Brandon Hancock", "Ty Wells"]
chunk_id: "2025-09-23-chunk-009"
---

# Supabase migration and environment management

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Ty Wells expressed challenges with cloning Supabase environments, specifically regarding the migration of edge functions, users, and mapping UUIDs across instances. In response, Brandon Hancock emphasized the necessity of robust staging and production environment management and prepared to demonstrate his approach to solving this workflow issue.

[00:14:17] Ty Wells: Yeah, really, I was asking, my question is about cloning a Supabase instance.
[00:14:27] Ty Wells: Supabase has a point-in-time recovery option, but that's schema.
[00:14:32] Ty Wells: You can get data as well.
[00:14:34] Ty Wells: But what you cannot get is edge functions or users.
[00:14:41] Ty Wells: I think those are really the only two.
[00:14:43] Ty Wells: So I went through a process scripting out to gather, to pull all of that data, but then you've got UUID issues with, you know.
[00:14:53] Ty Wells: So I'm looking, I'm trying to see if there's anybody has any thought on that.
[00:14:57] Ty Wells: I'm in the process of writing an agent to do what
[00:15:00] Ty Wells: But I did, except I still had to match that data back to the users, so, you know, some sort of cross-mapping table.
[00:15:07] Ty Wells: Just wondering if anybody's been there.
[00:15:10] Ty Wells: Switched to Firebase.
[00:15:11] Ty Wells: Love it.
[00:15:13] Brandon Hancock: No, I'd love to dive into this, because, yeah, this is one of the hardest, like, where most people get is they're like, cool, I built a local app on my computer.
[00:15:23] Brandon Hancock: Cool, I deployed it to the cloud.
[00:15:26] Brandon Hancock: Ta-da, I'm done.
[00:15:26] Brandon Hancock: And that's, that's the start of your real world journey, as building a production application, because you really need to create a staging environment and a production environment.
[00:15:39] Brandon Hancock: So, let me just share my screen really fast.
[00:15:43] Brandon Hancock: And I'll just show, I don't want to show anything I'm not supposed to.

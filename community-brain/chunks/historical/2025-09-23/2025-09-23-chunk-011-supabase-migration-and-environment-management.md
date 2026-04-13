---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Supabase migration and environment management"
speakers: ["Brandon Hancock", "Ty Wells"]
chunk_id: "2025-09-23-chunk-011"
---

# Supabase migration and environment management

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** To address environment management and safe feature development in Supabase, Brandon recommends codifying infrastructure setup—such as storage buckets and permissions—into automated scripts. This workflow allows developers to quickly spin up consistent environments using a combination of database migrations, seeding, and deployment scripts to ensure parity across branches.

[00:17:00] Ty Wells: I have branches set up, and yes, exactly where we're at here in terms of, but more so my edge functions, the issues, because, you know, can't make those changes on production, it's not going to end well.
[00:17:16] Ty Wells: So I'm just looking at a good way to clone it, because now I want to create another branch for feature, a feature branch.
[00:17:24] Brandon Hancock: Let me show you one other thing real fast that would hopefully be super helpful.
[00:17:27] Brandon Hancock: So the way I have it is, I will usually make setup scripts, like, let me make sure I'm not doing anything bad again.
[00:17:36] Brandon Hancock: Okay, this is pretty good.
[00:17:38] Brandon Hancock: So what I do is I create a collection of setup scripts.
[00:17:44] Brandon Hancock: Like this is just, you know, like from the chat and rag application and ship kit, but what you end up doing is you codify everything so that you manually don't have to like recreate buckets and you don't have to manually recreate all of the different permissions for buckets.
[00:17:59] Brandon Hancock: and�.
[00:18:00] Brandon Hancock: Like you can
[00:18:00] Brandon Hancock: You just spin up a few setup scripts, and that way whenever you start working in a new environment, even if you have to blow everything away, you just literally run like three commands, npm run, db migrate, pool, your new database matches your current schema, then you run a few setup scripts, create all your buckets, deploy your edge functions, and then you would want to run like npm, a db seed to seed your database with some fake data.
[00:18:27] Brandon Hancock: So I think you're already doing that, but I think you're already, you're just in the hard part now where it's like, what do I do with my data?
[00:18:33] Ty Wells: How do I actually like, I guess, clean it for the two different environments?

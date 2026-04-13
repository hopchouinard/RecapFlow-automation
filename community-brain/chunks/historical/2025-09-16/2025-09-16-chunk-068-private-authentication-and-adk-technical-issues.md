---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Private Authentication and ADK Technical Issues"
speakers: ["Brandon Hancock", "Hemal Shah"]
chunk_id: "2025-09-16-chunk-068"
---

# Private Authentication and ADK Technical Issues

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon Hancock recommends implementing an invite-only workflow by removing public sign-in options and using the Supabase "invite user" function within an admin dashboard. This approach ensures account security by requiring specific invitations via email rather than allowing open access to the application.

[01:17:28] Brandon Hancock: So that's just a very quick workaround, to where you basically just have to work on the invite user workflow in whichever authentication provider you're using.
[01:17:38] Brandon Hancock: And that's the quickest workaround to make sure that your application doesn't accidentally, even if it did get shared to the world, people can never join, you know, so it's invite only.
[01:17:48] Brandon Hancock: That's how, in the simple way, just drop the sign in.
[01:17:51] Brandon Hancock: Sorry, sir.
[01:17:52] Brandon Hancock: And then.
[01:17:55] Hemal Shah: So, the link that you are sharing, is that, is there a Supabase actual website?
[01:18:02] Hemal Shah: Or is it some GitHub project, tutorial project that you developed?
[01:18:09] Brandon Hancock: So this was like a project for a client.
[01:18:11] Brandon Hancock: They had very similar workflow.
[01:18:13] Brandon Hancock: So what you build inside the project is you can use Supabase.
[01:18:18] Brandon Hancock: And once you have a Supabase client set up, so like, let's just imagine you set up Supabase.
[01:18:23] Brandon Hancock: Cool.
[01:18:23] Brandon Hancock: Supabase has authentication.
[01:18:25] Brandon Hancock: Not only does it have authentication, but there's literally a function called invite user.
[01:18:29] Brandon Hancock: But what you do is, in your application, you'll make an admin dashboard.
[01:18:34] Brandon Hancock: Inside your admin dashboard, you literally just have an invite user button.
[01:18:39] Brandon Hancock: Pops up a modal.
[01:18:40] Brandon Hancock: Put it in the name.
[01:18:40] Brandon Hancock: Put it in the email.
[01:18:41] Brandon Hancock: Press it.
[01:18:43] Brandon Hancock: It'll automatically add that user to your authentication setup.

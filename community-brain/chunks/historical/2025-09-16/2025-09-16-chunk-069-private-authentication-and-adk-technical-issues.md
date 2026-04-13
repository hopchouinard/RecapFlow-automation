---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Private Authentication and ADK Technical Issues"
speakers: ["Brandon Hancock", "Hemal Shah", "Morgan Cook"]
chunk_id: "2025-09-16-chunk-069"
---

# Private Authentication and ADK Technical Issues

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon Hancock explained how to streamline user onboarding by automating the authentication and database setup process via email invites. To handle these requirements, the team concluded that NextAuth is an effective, popular open-source library that avoids the complexity of manual hashing or external providers.

[01:18:40] Brandon Hancock: Put it in the email.
[01:18:41] Brandon Hancock: Press it.
[01:18:43] Brandon Hancock: It'll automatically add that user to your authentication setup.
[01:18:49] Brandon Hancock: And it'll also automatically add them to the database at the same time.
[01:18:53] Brandon Hancock: They get a nice email.
[01:18:54] Brandon Hancock: You've been invited.
[01:18:55] Brandon Hancock: They click sign in.
[01:18:56] Brandon Hancock: Boom.
[01:18:57] Brandon Hancock: They're in your app.
[01:18:58] Brandon Hancock: And they'll, yeah.
[01:18:58] Hemal Shah: And the authentication setup that you mentioned is that.
[01:19:02] Hemal Shah: Something out of box open source libraries, or maybe we can do ourself.
[01:19:08] Hemal Shah: I can create my own authenticator and comparison and password hashing and everything.
[01:19:13] Hemal Shah: I was just wondering if it's open source, third party, popular with NextShare, which we can just drop in, have some UI, put some middleware.
[01:19:24] Brandon Hancock: There's one library.
[01:19:25] Brandon Hancock: Next.
[01:19:27] Brandon Hancock: Blanking.
[01:19:28] Morgan Cook: Is it NextOff?
[01:19:29] Morgan Cook: I think you can use NextOff.
[01:19:31] Brandon Hancock: I've used them plenty of times.
[01:19:33] Brandon Hancock: That's a great one.
[01:19:34] Brandon Hancock: If you just want to not, if you don't want to have to worry about Supabase and other auth providers, yeah, NextOff would be a really great one.
[01:19:41] Brandon Hancock: which is good.
[01:19:42] Brandon Hancock: Okay.
[01:19:42] Brandon Hancock: Yeah.

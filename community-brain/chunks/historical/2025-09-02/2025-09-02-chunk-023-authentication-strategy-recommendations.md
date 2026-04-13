---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Authentication Strategy Recommendations"
speakers: ["Brandon Hancock", "Morgan Cook"]
chunk_id: "2025-09-02-chunk-023"
---

# Authentication Strategy Recommendations

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Brandon recommended Clerk or Supabase for standard MVP projects, while suggesting WorkOS for complex, enterprise-level B2B requirements involving SAML. Ultimately, he advised using Supabase as a consolidated solution to simplify the initial development stack, noting that it integrates well with other tools if a migration is needed later.

[00:29:57] Brandon Hancock: Yeah.
[00:29:57] Brandon Hancock: So, so quick updates.
[00:29:59] Brandon Hancock: So if you're trying to do.
[00:30:00] Brandon Hancock: Application that's like MVP style, a few thousand customers, know, non-enterprise, the key here is non-enterprise.
[00:30:09] Brandon Hancock: I mean, everything from Clerk does great.
[00:30:12] Brandon Hancock: I mean, Supabase does great.
[00:30:15] Brandon Hancock: If you are, as a, for a fact, I'm doing a B2B software where I need to start allowing different companies to bring in their users into my system, and I have to deal with all the, like, SAML stuff, like all the, all the unfun stuff.
[00:30:29] Brandon Hancock: Work OS would be my recommendation if you're going enterprise.
[00:30:34] Brandon Hancock: I haven't used better auth, but it looks pretty straightforward.
[00:30:38] Brandon Hancock: Yeah, looks pretty, pretty nice.
[00:30:40] Brandon Hancock: I will say my, my main recommendation right now, especially to help reduce the learning curve, I absolutely love Supabase because it's one place for auth and your database and your blob store.
[00:30:51] Brandon Hancock: So it's all right there, because if not, you're going to have to hop into Clerk, then you're going to have to hop into Neon, then you're going to have to hop into a blob store.
[00:30:58] Brandon Hancock: So, um, for most
[00:31:00] Brandon Hancock: Tuple, Supabase, I think, would get you really far, and it does integrate with Clerk and WorkOS and all the rest.
[00:31:07] Morgan Cook: Right, I'm not opposed to doing migration after the fact to some other framework, but it was just kind of a, how do I really get started with this?
[00:31:15] Morgan Cook: And that's kind of what I'm looking at.

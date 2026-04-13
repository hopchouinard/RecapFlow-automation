---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Best Practices for Cloud Deployment and Logging"
speakers: ["Brandon Hancock", "Marc Juretus"]
chunk_id: "2025-09-16-chunk-019"
---

# Best Practices for Cloud Deployment and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon recommends using a shared database with a connection pooler, such as Supabase's built-in pooling, to optimize performance and prevent resource exhaustion. They concluded that Marc’s architecture—utilizing a Next.js front end with a FastAPI back end connected to the shared database—is a sound approach for his deployment.

[00:18:54] Brandon Hancock: Everything is shared in a common shared database, which is I think you will have much
[00:19:00] Brandon Hancock: It'll be faster, more secure.
[00:19:02] Brandon Hancock: There's so many, I mean, they're both very secure, but I think you'll end up with a better experience doing that.
[00:19:07] Brandon Hancock: The gotcha, the one gotcha, though, is when using database, it doesn't matter which database platform you're using, Supabase, Neon, any of them, you have to worry about the maximum number of database connection strings.
[00:19:21] Brandon Hancock: One thing I really like about Supabase is they do a thing called a pooler, which basically says, like, hey, I will allow 10 people to talk to a pooler, and then this one pooler will take all those different connections and make one connection to the database, because you can very easily exhaust database resources, so Supabase handles that for you, so definitely, yeah, I definitely recommend, long story short, the second option where everything talks to the database and they go back and forth.
[00:19:50] Brandon Hancock: That's what I would recommend.
[00:19:52] Marc Juretus: Yeah, I'm trying to connect directly for the fast API thing for, like, when it's calling inventory, this, that, and the other, like, right to the string, but I'm still using Supabase for the front end.
[00:20:00] Marc Juretus: And authentication, but it would be an XJS front end and then a back end that's basically FastAPI is what I'm looking to do.
[00:20:08] Marc Juretus: That's the manner that I'm going to build it in.
[00:20:11] Brandon Hancock: Yeah, that sounds great.
[00:20:13] Brandon Hancock: And usually what you'll do is in your, let me share a screen really.
[00:20:18] Brandon Hancock: Usually what will happen is you'll have to make something like this.

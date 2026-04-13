---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Database Schema for RAG"
speakers: ["Brandon Hancock", "Juan Torres"]
chunk_id: "2025-09-02-chunk-065"
---

# Database Schema for RAG

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Brandon Hancock suggested using a standard AWS RDS Postgres database instead of a separate vector database for the RAG workflow. They concluded that utilizing the `pgvector` extension allows for seamless vector embeddings within a traditional Postgres environment, which Brandon then demonstrated to the group.

[01:18:20] Brandon Hancock: So you're just to, I just want to make sure.
[01:18:23] Brandon Hancock: So you're using strictly AWS, they're out of the box.
[01:18:29] Brandon Hancock: Well, thought, so here's my, just not brushing up on AWS in a while, but from my understanding with RDS, you can spin up any SQL type database.
[01:18:39] Brandon Hancock: Is there a reason you just don't do a straight up Postgres database out the box?
[01:18:45] Brandon Hancock: Like you just use one database?
[01:18:49] Juan Torres: I could, I mean, I thought that maybe just having a backtraced database would be much easier for embedding whatever information that the Agenda Tech system is going to need.
[01:19:00] Juan Torres: to to the Yeah.
[01:19:01] Brandon Hancock: Yeah.
[01:19:02] Brandon Hancock: Yeah.
[01:19:02] Juan Torres: You know, there's the option of just directly feeding that information.
[01:19:07] Juan Torres: I just thought that maybe it's more effective if we're, like, trying to streamline a whole workflow to just have an already vectorized database.
[01:19:19] Brandon Hancock: I mean, the really cool part when you do go into database land, specifically Postgres, and use that PG vector that you're talking about, it's basically just an extension to Postgres databases.
[01:19:31] Brandon Hancock: But what's sick is all it does is it actually just updates the individual column, that's the embedding column, and all it does, let me actually see if I can show you guys an example really fast, because I think this is a cool, cool lesson.
[01:19:43] Brandon Hancock: Let me see if I can get this open real fast.
[01:19:48] Brandon Hancock: All right, too many, too many windows for place.
[01:19:53] Brandon Hancock: One second, I'll show this.

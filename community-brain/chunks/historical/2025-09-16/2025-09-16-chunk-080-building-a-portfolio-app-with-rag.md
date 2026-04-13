---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Building a Portfolio App with RAG"
speakers: ["Alex Wilson", "Brandon Hancock"]
chunk_id: "2025-09-16-chunk-080"
---

# Building a Portfolio App with RAG

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** The discussion covered the cost implications of database backups in PlanetScale versus Supabase, highlighting that point-in-time recovery incurs additional fees. Additionally, Brandon demonstrated how to configure Cursor’s auto-run settings to an "allowlist" mode, which prevents the AI from automatically executing disruptive commands like `npm run dev`.

[01:30:10] Brandon Hancock: I think planet scale is like $80.
[01:30:11] Brandon Hancock: So they're both pretty expensive for instant database backups at any point in time.
[01:30:17] Brandon Hancock: However, Supabase does have daily backups, and those are included.
[01:30:21] Brandon Hancock: But point-in-time, they will charge you for it.
[01:30:24] Brandon Hancock: Just so you know everything that you're getting into before you fully commit.
[01:30:30] Alex Wilson: So...
[01:30:31] Alex Wilson: Excellent.
[01:30:31] Alex Wilson: Sounds good.
[01:30:32] Alex Wilson: One other question.
[01:30:33] Alex Wilson: Earlier you were showing, I had that problem with the NPM run.
[01:30:37] Alex Wilson: Where was that that you can...?
[01:30:41] Brandon Hancock: I still have it up.
[01:30:42] Brandon Hancock: That's funny.
[01:30:44] Brandon Hancock: Okay.
[01:30:45] Brandon Hancock: So in settings, in cursor settings, so I hit the top button, then go to chat, and then I changed my auto run mode to whitelist.
[01:30:56] Brandon Hancock: So use allowlist, sorry.
[01:30:58] Brandon Hancock: And this is where I say, like, you can run these specific commands.
[01:31:02] Brandon Hancock: I don't mind when it runs Lint.
[01:31:04] Brandon Hancock: I don't mind when it runs some of these other things.
[01:31:07] Brandon Hancock: It's just, I don't want it to run NPM run dev.
[01:31:11] Brandon Hancock: Don't do that.
[01:31:12] Brandon Hancock: So I just hit deny is the main thing.
[01:31:17] Brandon Hancock: I'm trying to see if there's a...

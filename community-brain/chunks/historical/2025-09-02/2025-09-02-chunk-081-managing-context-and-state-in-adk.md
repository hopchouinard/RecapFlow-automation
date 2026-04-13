---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing Context and State in ADK"
speakers: ["Brandon Hancock", "Ola Oyo"]
chunk_id: "2025-09-02-chunk-081"
---

# Managing Context and State in ADK

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Ola successfully integrated the ADK with his Django application by replacing in-memory storage with a persistent database-backed storage solution. He achieved this by using SQLAlchemy and mapping session UUIDs to user authentication, ensuring state persists across chat sessions.

[01:35:12] Brandon Hancock: All right.
[01:35:12] Brandon Hancock: I think it is Ola, Jake, Alex.
[01:35:17] Brandon Hancock: Sorry, it's getting out of order, but Ola, you're up next, buddy.
[01:35:23] Brandon Hancock: Hey, Brandon.
[01:35:23] Ola Oyo: How's it going?
[01:35:25] Ola Oyo: Hey, It's been a very interesting week.
[01:35:27] Ola Oyo: It's been an interesting week.
[01:35:29] Ola Oyo: I mean, I think the major issue I had last week was trying to connect ADK to my Django application.
[01:35:36] Ola Oyo: Yeah.
[01:35:36] Ola Oyo: So I was able to do that.
[01:35:39] Ola Oyo: I don't know if it's the best of ways, but I was able to fix in the data session storage, just sort of using like an SQL alchemy type of URL and then sort of stick user authentication into that.
[01:35:55] Ola Oyo: So as the UUIDs are being created within new chats, that's the same one that I use for the session.
[01:36:02] Ola Oyo: Perfect.
[01:36:02] Ola Oyo: Perfect.
[01:36:02] Ola Oyo: And then.
[01:36:03] Ola Oyo: I was also able to, yeah, go ahead.
[01:36:05] Brandon Hancock: So you are, you did successfully set up the ADK to not use in memory, you're using persistent storage, and your persistent storage is saving to your database?
[01:36:16] Ola Oyo: Is that what I'm hearing?
[01:36:17] Ola Oyo: Yeah, persistent storage is saving to the database.

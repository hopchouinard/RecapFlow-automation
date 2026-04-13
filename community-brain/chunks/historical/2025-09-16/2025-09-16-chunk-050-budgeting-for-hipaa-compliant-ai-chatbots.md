---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Budgeting for HIPAA-Compliant AI Chatbots"
speakers: ["Brandon Hancock", "Juan Torres"]
chunk_id: "2025-09-16-chunk-050"
---

# Budgeting for HIPAA-Compliant AI Chatbots

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** The coaches clarified that HIPAA compliance requires high-volume audit logs, which are significantly more granular than standard development logs. To manage the resulting storage costs, they recommended moving these logs to cost-effective "cold storage" solutions rather than active buckets.

[00:55:10] Juan Torres: You just need to make a connection to your SSH, through SSH to whatever Agentec ID you're trying to do.
[00:55:18] Brandon Hancock: The one core difference is most of the time when we think logs, we think development logs, such as like, Brandon made this request.
[00:55:26] Brandon Hancock: Here is like a little bit of the information.
[00:55:28] Brandon Hancock: So it's all development logs.
[00:55:30] Brandon Hancock: That's like layer one.
[00:55:32] Brandon Hancock: What HIPAA wants is it's called an audit log, which is like a level above that.
[00:55:38] Brandon Hancock: So it's not just like Brandon made a request.
[00:55:40] Brandon Hancock: It's like Brandon literally opened this page.
[00:55:43] Brandon Hancock: Brandon saw this information.
[00:55:45] Brandon Hancock: Like it's at an extreme.
[00:55:47] Brandon Hancock: So you can at any point go, I could literally from two months ago tell you exactly what Brandon was doing on our app at 1230 p.m.
[00:55:54] Brandon Hancock: Like it is, it's a level above.
[00:55:56] Brandon Hancock: So that's why you'll create gigabytes of logs per day.
[00:56:00] Brandon Hancock: But even though it's gigabyte.
[00:56:02] Brandon Hancock: Andrew, I would just be curious, I would be very curious how the logs are being stored, there's different types of storage, there's cold storage, like literally just by like changing how you store data, you could save a ton of money, because you're not accessing these audit logs every day, you might access them, honestly, whenever you get audited.
[00:56:20] Brandon Hancock: So there's, might just have Maxim look to see if he could change the bucket to a different type of bucket to save you some money, just because that's a quick fix, and that could save a lot of money.

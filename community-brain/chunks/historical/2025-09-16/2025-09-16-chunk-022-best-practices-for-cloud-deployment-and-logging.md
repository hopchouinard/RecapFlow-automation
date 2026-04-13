---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Best Practices for Cloud Deployment and Logging"
speakers: ["Brandon Hancock", "Hemal Shah"]
chunk_id: "2025-09-16-chunk-022"
---

# Best Practices for Cloud Deployment and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Hemal Shah explored centralizing logs and monitoring for applications deployed across different platforms like Vercel and GCP to improve troubleshooting. Brandon Hancock recommended using Datadog as a unified solution for aggregating these logs and setting alerts, while noting the company’s aggressive sales follow-up practices.

[00:22:37] Hemal Shah: I went through a, Brandon, your next year's full stack deployment tutorial video and deployed everything.
[00:22:43] Hemal Shah: It's very clean.
[00:22:45] Hemal Shah: Most of my stuff is in GCP, and from troubleshooting perspective, I was just thinking if application is also deployed in GCP one place, then all the logs, alerting, monitoring, I mean, not for the small application, I think Warsaw is perfect, but when
[00:23:00] Hemal Shah: You want to go a little bit deeper.
[00:23:04] Hemal Shah: That's what I was exploring it.
[00:23:06] Hemal Shah: So Firebase and there are some cloud run, Firebase, some combination.
[00:23:10] Hemal Shah: But like you said, it is you have to jump through several hoops to get to that state.
[00:23:15] Brandon Hancock: If you're looking to synchronize logs across multiple platforms, there's a tool called DataDog.
[00:23:23] Brandon Hancock: Be careful if you give them your information.
[00:23:25] Brandon Hancock: They call nonstop.
[00:23:28] Brandon Hancock: Like, if you sign up, I've never gotten so many calls from one platform before, but they do have a really cool tool where you can import logs from all of your services.
[00:23:38] Brandon Hancock: So your Next.js Vercell application, you'll just set up DataDog.
[00:23:42] Brandon Hancock: It'll put it there.
[00:23:43] Brandon Hancock: If you're doing Google Cloud Railway, whatever you're doing, it'll also ship the logs to one space, which is really nice because then it's one place to monitor everything.
[00:23:50] Brandon Hancock: You can set alerts.
[00:23:51] Brandon Hancock: They have a really nice tool.
[00:23:52] Brandon Hancock: You'll see a lot of, you know, big companies will always usually use DataDog.

---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Best Practices for Cloud Deployment and Logging"
speakers: ["Brandon Hancock", "Marc Juretus"]
chunk_id: "2025-09-16-chunk-015"
---

# Best Practices for Cloud Deployment and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon Hancock and Marc Juretus discussed a recommended cloud deployment architecture that utilizes Vercel for Next.js applications and Google Cloud for Agent Engine, rather than managing the complexity of hosting both within Google Cloud. They concluded that while a unified Google Cloud environment is possible, it is overly complicated and the Vercel-hybrid approach is the more efficient path.

[00:15:08] Brandon Hancock: Is that correct?
[00:15:09] Brandon Hancock: Yeah.
[00:15:10] Marc Juretus: So just for context for everyone, this was the ADK deploy video.
[00:15:14] Brandon Hancock: Yeah.
[00:15:15] Brandon Hancock: This was one of the things I was trying to show in the video was like, okay, you have ADK and your web app, get them working locally, deploy ADK to Agent Engine.
[00:15:25] Brandon Hancock: That's cool.
[00:15:26] Brandon Hancock: So now deploy our Next.js application to the cloud.
[00:15:30] Brandon Hancock: The easiest way to deploy a Next.js application is to Vercel.
[00:15:33] Brandon Hancock: So the end state is you have Google Cloud running over here, running your agent engine.
[00:15:38] Brandon Hancock: So ADK is doing its thing.
[00:15:40] Brandon Hancock: And then over here on the right, you have your Next.js application in Vercel.
[00:15:43] Brandon Hancock: So they're both in the cloud.
[00:15:44] Brandon Hancock: They're both talking to each other.
[00:15:45] Brandon Hancock: But yeah, that's where it ended up at.
[00:15:47] Brandon Hancock: You could, if you wanted to, you know, go fancy and actually like create a, you could go and like deploy the Next.js application inside Google Cloud, but you will spend so much time doing
[00:16:02] Marc Juretus: Yeah, there's a lot of steps in that, man.
[00:16:04] Marc Juretus: I got to admit, there's a lot going on to get that going brutal, isn't it?
[00:16:08] Brandon Hancock: It's brutal.
[00:16:09] Marc Juretus: get the foundation of what's going on and hopefully where it goes is going to be a lot simpler.

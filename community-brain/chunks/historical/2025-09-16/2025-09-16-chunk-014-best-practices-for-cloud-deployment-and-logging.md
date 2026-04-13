---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Best Practices for Cloud Deployment and Logging"
speakers: ["Brandon Hancock", "Marc Juretus"]
chunk_id: "2025-09-16-chunk-014"
---

# Best Practices for Cloud Deployment and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Marc Juretus and Brandon Hancock discussed the architectural relationship between Google Cloud Platform (GCP) and front-end hosting services like Vercel. They concluded that while the application is hosted externally (e.g., Vercel), it interacts with the backend services provided by GCP.

[00:14:10] Brandon Hancock: What's going on, Mark?
[00:14:11] Brandon Hancock: How is all of our fantasy apps?
[00:14:15] Marc Juretus: How's everything going?
[00:14:16] Marc Juretus: I'm still running in the background running the league, so that's still working fairly well for the most part.
[00:14:20] Marc Juretus: It was good to see Ty actually smile once on these videos, so that was kind of cool.
[00:14:25] Marc Juretus: So good for you, Ty.
[00:14:26] Marc Juretus: What?
[00:14:27] Marc Juretus: I've never seen you smile, so I was good, man.
[00:14:29] Marc Juretus: I guess, obviously, when you have your software that far down and you start to get the smiles out, so good for Yeah, I shipped some products.
[00:14:35] Brandon Hancock: I can now breathe.
[00:14:36] Brandon Hancock: I'm okay.
[00:14:37] Brandon Hancock: Yeah.
[00:14:39] Marc Juretus: So all I've done of late, I actually went through a great deal of your Google Cloud, the development kit one that you had.
[00:14:49] Marc Juretus: And then, in the end, I noticed that it actually gets hosted by, you hosted it on Vercel or something like that, if I'm trying to remember correctly, like the ADK?
[00:14:57] Marc Juretus: Yes.
[00:14:58] Marc Juretus: Yeah.
[00:14:58] Marc Juretus: So in the end, you really can't.
[00:15:00] Marc Juretus: If can't host the app on GCP, it's really going to be on like another instance and you're just pointing to the Google in the back end.
[00:15:08] Brandon Hancock: Is that correct?

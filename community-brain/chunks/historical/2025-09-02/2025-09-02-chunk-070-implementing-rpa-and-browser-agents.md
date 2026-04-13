---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Implementing RPA and Browser Agents"
speakers: ["Brandon Hancock", "David Stamper"]
chunk_id: "2025-09-02-chunk-070"
---

# Implementing RPA and Browser Agents

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** David Stamper and Brandon Hancock discussed implementing an RPA browser agent to automate a complex, multi-step online application process triggered by Pipedrive, which requires human intervention for a QR code verification. To assist with this, Brandon agreed to provide an example ADK repository featuring a browser agent capable of multi-page navigation as a foundational reference.

[01:24:30] David Stamper: The RPA that I'm referring to would be used for, like, I want to use a trigger to fire off from my pipe drive when a new deal is added.
[01:24:44] David Stamper: I wanted to fire off this RPA agent who can fill out an application for me online.
[01:24:51] Brandon Hancock: Okay, so saying it back, you need a browser agent that can fill out a form online, as I guess, like, if we boil it down a little bit more?
[01:25:01] David Stamper: Yeah, it's...
[01:25:02] David Stamper: It's...
[01:25:02] David Stamper: You've to be pretty smart, though, because not only does it need to go and fill out the application, but it's a multi-step, so you fill out part of it, then you have to click Next, move on to the next part, and at one point during the application, there will be a QR code that I need to pass to my client, so pause the system until it gets passed back to me, and then move on.
[01:25:26] Brandon Hancock: I'm going to send you an example repository from ADK, where they made a browser agent, and this browser agent would go, like, you would send in a query, and it would go through multiple pages on a website, take screenshots, like, it did a ton of work, but I think it's a really good starting spot.
[01:25:43] Brandon Hancock: I just have to find it really fast for you.
[01:25:47] Brandon Hancock: One second.
[01:25:50] Brandon Hancock: Yeah, I will find it really fast, and I will Google developer.
[01:25:54] Brandon Hancock: I know exactly the video, I just have to find it really fast.
[01:25:58] Brandon Hancock: So the second I find it, I'll send it, I'll just drop it in the chat.
[01:26:01] Brandon Hancock: on chat.
[01:26:01] Brandon Hancock: it necessary.

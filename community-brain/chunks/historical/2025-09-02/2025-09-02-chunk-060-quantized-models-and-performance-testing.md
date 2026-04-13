---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Quantized Models and Performance Testing"
speakers: ["Brandon Hancock", "Juan Torres"]
chunk_id: "2025-09-02-chunk-060"
---

# Quantized Models and Performance Testing

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Juan Torres is optimizing accounting application performance by integrating a lighter, open-source model (GPT-OSS) to handle tasks when high-end A100 GPU resources are unavailable. He concluded that this model's efficiency on an A10 GPU serves as an effective, cost-saving fallback for periods of high demand.

[01:11:32] Brandon Hancock: All right.
[01:11:32] Brandon Hancock: Juan, you're up next, buddy.
[01:11:34] Brandon Hancock: I know last week, speaking of 25K, Paul just brought up 25K.
[01:11:39] Brandon Hancock: Last week, you saved a company, 25K.
[01:11:41] Brandon Hancock: That seems to be our lucky number, guys.
[01:11:43] Brandon Hancock: Right?
[01:11:44] Brandon Hancock: Didn't you?
[01:11:45] Brandon Hancock: What was the post?
[01:11:46] Brandon Hancock: Your post.
[01:11:46] Brandon Hancock: You saved that organization, 25K, right?
[01:11:49] Juan Torres: It was 15.
[01:11:51] Brandon Hancock: Oh, okay.
[01:11:52] Juan Torres: All right.
[01:11:52] Juan Torres: Not as much.
[01:11:53] Brandon Hancock: Not as much.
[01:11:54] Brandon Hancock: I wish it was 25K like Paul.
[01:11:58] Juan Torres: I'm trying.
[01:11:59] Brandon Hancock: I'm trying.
[01:12:00] Juan Torres: No, this week, um...
[01:12:03] Juan Torres: So this week, I'm just, so I made some tests on, I don't know if you guys know, but ChatGPT released an open model, open source model, GPT OSS, and it actually performed pretty well on a GPU A100 computer, so much so that now I think it can perform on an A10 GPU.
[01:12:29] Juan Torres: So we're thinking of bringing a decision tree in the accounting application to use more, a more reserved model, like OOS, in order to carry out tasks when the big GPU from A100 is not available quick because their servers are requesting that GPU through several users, so it's an on-demand GPU really, right?

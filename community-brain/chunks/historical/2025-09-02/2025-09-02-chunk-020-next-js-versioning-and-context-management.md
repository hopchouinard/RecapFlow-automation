---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Next.js Versioning and Context Management"
speakers: ["Brandon Hancock", "Morgan Cook"]
chunk_id: "2025-09-02-chunk-020"
---

# Next.js Versioning and Context Management

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** The participants discussed the difficulty of using LLMs with Next.js due to frequent breaking changes, highlighting the need for robust context management. To address this, Brandon recommended utilizing the "Context 7" MCP server tool within Cursor to enable live documentation searching and accurate context retrieval for the latest framework versions.

[00:26:55] Morgan Cook: And so I was able to finally get past that.
[00:26:58] Morgan Cook: But that's one of the things that I've noticed.
[00:27:00] Morgan Cook: was new to Thank
[00:27:00] Morgan Cook: Any time you have a framework that you're using that has breaking changes, the large language model just isn't built to deal with those new changes.
[00:27:09] Morgan Cook: So you've got to really have the context in place.
[00:27:12] Morgan Cook: And that's where I found your templates to be very useful.
[00:27:16] Brandon Hancock: Awesome.
[00:27:16] Brandon Hancock: I appreciate that, Morgan.
[00:27:17] Brandon Hancock: Out of curiosity, what version of Next.js were you using?
[00:27:20] Morgan Cook: Which one did you go to?
[00:27:23] Morgan Cook: I was just the latest on all of them was the test, right?
[00:27:27] Morgan Cook: I ran it through a couple of different LMs.
[00:27:30] Morgan Cook: One of the frameworks was WindSurf.
[00:27:32] Morgan Cook: It got pretty close.
[00:27:34] Morgan Cook: The best one that I've found that was successful at getting past all the problems was just using Vercel directly.
[00:27:41] Brandon Hancock: Let me show you this real fast.
[00:27:44] Morgan Cook: I think it's very helpful.
[00:27:45] Brandon Hancock: If you're using Cursor, I don't know if you've heard of Context 7, but it is a tool.
[00:27:53] Brandon Hancock: It's an MCP server that has access to two function calls, like one search and one's like read.
[00:27:58] Brandon Hancock: So it'll actually search for next.
[00:28:00] Brandon Hancock: J.J.S.

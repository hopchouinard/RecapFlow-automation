---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Effective Testing Strategies for AI Apps"
speakers: ["Andrew Nanton", "Brandon Hancock", "Jake Maymar"]
chunk_id: "2025-09-16-chunk-036"
---

# Effective Testing Strategies for AI Apps

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** To address the difficulty of integrating working components into larger AI projects, the coaches recommend avoiding overly complex, monolithic prompts. Instead, they conclude that breaking development into smaller, incremental steps supported by automated testing is more effective, specifically noting that Claude is highly capable of generating these essential tests.

[00:38:07] Jake Maymar: The other question is, does it make sense to make small, very, very simple, this is sort of a question for Andrew, but also a question for Brandon.
[00:38:20] Jake Maymar: What I've been doing is when I get really stuck on something, I'll make a very, very, very simple version of it, get that working, and then I try and integrate it.
[00:38:28] Jake Maymar: But sometimes integrating is just like a freaking nightmare, you know, and I'm like, why can't you just see that this is working and integrate it?
[00:38:37] Jake Maymar: And I'm wondering if you guys have any tips on that, because that is driving me, because it doesn't make any sense.
[00:38:45] Jake Maymar: It's working.
[00:38:45] Jake Maymar: It's working.
[00:38:46] Jake Maymar: This is all working.
[00:38:48] Jake Maymar: Just use this and integrate it in.
[00:38:50] Jake Maymar: And it rewrites it or, yeah, anyway, love to hear.
[00:38:56] Brandon Hancock: If you want to go first.
[00:38:58] Andrew Nanton: Oh, so I.
[00:39:01] Andrew Nanton: I have found that the alternative is just as bad or worse, like trying to have it do the whole thing, like having to do one large, complex thing, like, okay, get, I want six different plates spinning at once, is, is like, that almost always blows up in my face.
[00:39:21] Andrew Nanton: Whereas, incrementally, okay, like, I know this is working.
[00:39:25] Andrew Nanton: At least for me, what has been helpful is write tests, and then do the thing and run the tests.
[00:39:32] Andrew Nanton: And, and, you know, because tests are boring and long, and Claude is happy to write them.

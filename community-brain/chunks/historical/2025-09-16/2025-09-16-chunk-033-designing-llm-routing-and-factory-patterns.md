---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Designing LLM Routing and Factory Patterns"
speakers: ["Brandon Hancock", "Jake Maymar"]
chunk_id: "2025-09-16-chunk-033"
---

# Designing LLM Routing and Factory Patterns

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** The discussion centered on optimizing LLM performance by using high-end models (like Claude 3.5 Sonnet) to generate architectural blueprints, followed by routing the execution tasks to smaller, more cost-effective models. Brandon confirmed the effectiveness of this "lobotomization" strategy in his ShipKit project, noting it balances high-level reasoning with efficient, simplified processing.

[00:35:26] Brandon Hancock: And I'm like, no, it's already running.
[00:35:27] Brandon Hancock: Like, I don't need it to run another instance.
[00:35:29] Brandon Hancock: So I would always, I would check out the allow list just to have it not accidentally spin something up.
[00:35:36] Brandon Hancock: And then very final comment, because you, I brought up such a golden nugget of knowledge, and I've been doing it, but the way you phrased it, I like better.
[00:35:44] Brandon Hancock: You'll use, you know, the highest thinking model, like, you know, a clod force on it, like the highest version to come up with the blueprint, and then lobotomize it and use a cheaper model.
[00:35:58] Brandon Hancock: That's literally, that's what I do every step in ShipKit.
[00:36:01] Brandon Hancock: That's
[00:36:01] Brandon Hancock: They used the 1 million token window to come up with a plan using Cloudforce on it.
[00:36:06] Brandon Hancock: And then the second the blueprint is there, cool.
[00:36:08] Brandon Hancock: No more high-level thinking.
[00:36:09] Brandon Hancock: We can now have a smaller, cheaper AI model do the actual work.
[00:36:14] Brandon Hancock: So, yeah, literally following your footsteps on that one.
[00:36:17] Brandon Hancock: And it works really well.
[00:36:19] Brandon Hancock: And it leverages AI when it's best at.
[00:36:22] Brandon Hancock: Big models, great at thinking.
[00:36:23] Brandon Hancock: Use the other less ones when you just need to, hey, just do literally what that file says.
[00:36:28] Brandon Hancock: So, great, great, great strategy on that.
[00:36:31] Jake Maymar: Jake.

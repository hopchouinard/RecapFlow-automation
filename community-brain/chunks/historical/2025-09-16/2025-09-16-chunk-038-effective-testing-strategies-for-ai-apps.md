---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Effective Testing Strategies for AI Apps"
speakers: ["Brandon Hancock", "Ola Oyo"]
chunk_id: "2025-09-16-chunk-038"
---

# Effective Testing Strategies for AI Apps

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** The speakers outline a multi-model development workflow that leverages ChatGPT for initial instructions, the "agents.md" file with Codex for structural planning and dependency analysis, and Claude for rapid iteration. They conclude that combining these tools—specifically utilizing Codex for planning and Claude 3.5 Sonnet for development—creates a robust framework where each model's unique strengths compensate for the others' limitations.

[00:40:48] Ola Oyo: I literally start from ChadGPT, and I say, okay, this is what I'm trying to do.
[00:40:52] Ola Oyo: Can you please give me the instructions to build a GPT for this specific task?
[00:40:58] Ola Oyo: So it goes, it gives the instructions.
[00:40:59] Ola Oyo: I put that into ChadGPT.
[00:41:01] Ola Oyo: I take that also, put it into an agents.md, which is something that the codex model is able to see.
[00:41:08] Ola Oyo: And with that, it looks through the entire code base and it's able to actually structure a plan.
[00:41:13] Ola Oyo: I have that plan.
[00:41:14] Ola Oyo: I put it in a markdown file also.
[00:41:17] Ola Oyo: Then send Claude to sort of do its thing, based on the instructions for this specific task and based on the plan, then start working through things.
[00:41:26] Ola Oyo: And I also find that codex is actually also better for testing because it looks at all the other dependencies and sort of just helps with that.
[00:41:36] Ola Oyo: So codex is good for planning.
[00:41:39] Ola Oyo: Claude is good for fast iteration.
[00:41:41] Ola Oyo: But then co-pilots with Claude 4 is like your senior developer that finds things that typically Claude just go and mess up.
[00:41:49] Ola Oyo: So that's typically what I've seen as your workflow, just going from one model to another and sort of like their different strengths across them.
[00:41:56] Ola Oyo: But yeah, go ahead, Brandon.
[00:41:59] Brandon Hancock: I absolutely, absolutely loved all of that.
[00:42:01] Brandon Hancock: Thank

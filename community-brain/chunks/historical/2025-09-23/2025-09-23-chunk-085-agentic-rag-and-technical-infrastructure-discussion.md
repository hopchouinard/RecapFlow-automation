---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Jake Maymar", "Juan Torres", "Mitch"]
chunk_id: "2025-09-23-chunk-085"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** The discussion explored the emerging potential of autonomous "zero-person" companies, such as self-managing fleets of vehicles that sell their own excess compute power. Additionally, Juan shared his experiments using Agentic IDEs to deploy LLMs and diffusion models on EC2 instances, noting that high-parameter models require significantly more GPU power than an A10 provides.

[01:50:09] Mitch: It's a zero-person company.
[01:50:11] Jake Maymar: Yeah.
[01:50:12] Jake Maymar: Oh, I heard a really interesting article about a taxicab that hires itself, builds the entire business plan, like, the whole thing, and, like, basically, like, gets advertised, like, advertises and gets clients to basically, you know, to pick up, and load balances to figure out maintenance costs for the car.
[01:50:38] Jake Maymar: That's nuts.
[01:50:40] Jake Maymar: That's totally nuts, that, like, an autonomous vehicle would do all those things.
[01:50:49] Jake Maymar: Oh, and then also cell inference, right?
[01:50:52] Jake Maymar: So, of course, the system itself is the GPU, so it would sell its compute to people.
[01:51:01] Jake Maymar: It's wild!
[01:51:02] Jake Maymar: Like, what?
[01:51:05] Jake Maymar: So, Juan, you joined late.
[01:51:08] Jake Maymar: Is there anything you want to discuss?
[01:51:11] Juan Torres: No.
[01:51:13] Juan Torres: Juan Well, if I may share, let's see.
[01:51:18] Juan Torres: Juan Yes.
[01:51:19] Juan Torres: Juan One of the things that I think it's really interesting is you can use your Agentec IDE for EC2 instances.
[01:51:30] Juan Torres: Juan I've been playing around with that the last couple of two weeks, just deploying LLMs or diffusion models.
[01:51:41] Juan Torres: Juan- Right now, it's just been an A10 GPU, which is not very powerful in order to handle 14 billion-parameter diffusion models.
[01:51:53] Juan Torres: Juan You'll be surprised that you actually need way more GPU in order to handle those.
[01:51:58] Juan Torres: Juan And those have been only for funds.

---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Designing LLM Routing and Factory Patterns"
speakers: ["Andrew Nanton", "Brandon Hancock"]
chunk_id: "2025-09-16-chunk-028"
---

# Designing LLM Routing and Factory Patterns

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon suggests adopting software design patterns like the factory pattern and routing logic to effectively manage diverse LLM requests (such as PDFs or different service providers) and avoid unscalable, messy code. By implementing these patterns, the developer can dynamically generate the appropriate model instances, ensuring a cleaner, more modular architecture for handling multiple LLM sources like Gemini and OpenAI.

[00:29:18] Brandon Hancock: So do you want a quick tech deep dive?
[00:29:22] Brandon Hancock: If you would definitely, as you're working on this, you are like, I wouldn't say just like, hey, I'm trying to build this.
[00:29:29] Brandon Hancock: We're at the point to where we need to think at a higher plane and say like, hey, which types of software design patterns should I implement to handle this situation?
[00:29:39] Brandon Hancock: To where, you know, I am going to receive a request, depending on the type of request, I need to generate a proper service that can handle this type of request.
[00:29:51] Brandon Hancock: So you're going to have to look into the factory pattern, which will basically spin up a different, a LLM response.
[00:29:58] Brandon Hancock: Response.
[00:30:00] Brandon Hancock: Yeah.
[00:30:00] Brandon Hancock: Instant.
[00:30:00] Brandon Hancock: So if it's a PDF, we will spin up, like the factory will generate an instance of, we'll just say, the Gemini model that can handle that.
[00:30:09] Brandon Hancock: So there's like, that's one approach.
[00:30:11] Brandon Hancock: Another approach is to have like some sort of routing functionality.
[00:30:15] Brandon Hancock: There's multiple ways, but I would, if I was in your shoes, I would start to say, let's look at design patterns that we should be implementing to make this as easy as possible.
[00:30:24] Brandon Hancock: Because if you just say, hey, fix this.
[00:30:26] Brandon Hancock: Oh, and by the way, it should handle OpenAI.
[00:30:28] Brandon Hancock: By the way, it should handle.
[00:30:30] Andrew Nanton: Oh, right, right.
[00:30:31] Brandon Hancock: Yeah, no, no, it be soup.
[00:30:33] Brandon Hancock: It'll be disgusting.

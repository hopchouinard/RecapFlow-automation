---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing complex application state with agents"
speakers: ["Alex Wilson", "Brandon Hancock"]
chunk_id: "2025-09-23-chunk-040"
---

# Managing complex application state with agents

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** To manage complex state in a large bill-of-materials quote, Alex and Brandon discussed decomposing the data into smaller, manageable components. They concluded that creating distinct, modular state objects—categorized by sections like exterior, interior, or roofing—will help agents track and update quote status more effectively.

[00:49:01] Alex Wilson: But the outputs and now I'm trying to hook them up together and they need to like persist and be able to maintain around the status of this quote and that quote can be like working on a quote and it can be like a hundred line items in the quote and then that quote obviously from like if you take it like a tabular architecture it's got like each you know columns with fields in it so I'm trying to figure out now how do I like how do I maintain the state around the quote so that each as each agents accessing it there's persistent understanding of where where the status is basically the state of it okay and just to dive in a little bit deeper into it so like in my head like is this like a quote of like a hundred like are we building a house and we have to keep track of like okay the doors are going to cost we need two doors each door is two dollars or like a bill yeah it's like it's like a bill of materials so like okay here's your quote with you know each item and here's how much it you know it should cost it should
[00:50:01] Alex Wilson: But then there's, like, updates to those as it's going through, like, different reasoning.
[00:50:05] Brandon Hancock: Yeah, so the way I like to work with state and ADK is I like to break things down into smaller manageable components.
[00:50:15] Brandon Hancock: So, for example, it sounds like if there's a hundred items, I mean, the first question I would ask myself is, like, is there any sub, any way we could break down a hundred different rows into, like, like I said, we're doing houses, like exterior, interior, roof.
[00:50:30] Brandon Hancock: Like, I would do, I would look at that first to see if there's anything that we could do to, like, make it easier and more manageable, because...
[00:50:38] Alex Wilson: And that would, you would just break those into different objects, like state objects?
[00:50:42] Brandon Hancock: Yes.

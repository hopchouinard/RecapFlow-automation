---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Effective Testing Strategies for AI Apps"
speakers: ["Brandon Hancock", "Jake Maymar"]
chunk_id: "2025-09-16-chunk-040"
---

# Effective Testing Strategies for AI Apps

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Jake Maymar and Brandon Hancock discussed the challenge of managing cascading failures in unit tests as app complexity grows. To address this, they concluded that developers should consistently integrate quick verification commands—such as running linters and automated tests—after every new feature to catch breakages early.

[00:43:01] Jake Maymar: So and then creating the component and then retesting it.
[00:43:05] Jake Maymar: That's kind of what I've been doing.
[00:43:06] Jake Maymar: The problem I keep running into is, and I'm sure there's a design pattern for this, but the problem I keep running into is I will run old tests and it doesn't work anymore.
[00:43:19] Jake Maymar: And I don't know where it broke.
[00:43:22] Jake Maymar: Um, and the, so because to run all of those, I guess that's the question.
[00:43:30] Jake Maymar: Do you run all of the tests after every feature?
[00:43:34] Jake Maymar: Um, that's cause as these things get more and more complicated, there's a lot of tests that have to run.
[00:43:40] Brandon Hancock: And that's, that's, I'm just trying to understand what, what are we talking about unit tests?
[00:43:44] Brandon Hancock: Are we talking about like end to end UI tests?
[00:43:46] Jake Maymar: What are we talking about?
[00:43:47] Jake Maymar: I would say more unit tests.
[00:43:50] Brandon Hancock: I mean, so one thing that I always have, like in, in my task is that the very final step is always to run Lint and just like very quick commands to verify that.
[00:44:01] Brandon Hancock: It works because, yeah, that's the worst thing is when you're like, I built task one or I built feature one, cool, it works.
[00:44:07] Brandon Hancock: Feature two, cool, it works.
[00:44:08] Brandon Hancock: Feature three, it works.
[00:44:09] Brandon Hancock: Now let's go actually like run test.
[00:44:12] Brandon Hancock: And you're like, oh my God, it broke.
[00:44:13] Brandon Hancock: When did it break?

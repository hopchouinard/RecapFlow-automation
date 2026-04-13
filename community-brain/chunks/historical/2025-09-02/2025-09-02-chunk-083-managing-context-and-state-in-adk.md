---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing Context and State in ADK"
speakers: ["Brandon Hancock", "Ola Oyo"]
chunk_id: "2025-09-02-chunk-083"
---

# Managing Context and State in ADK

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Ola Oyo and Brandon Hancock discussed strategies to minimize token bloat caused by passing an entire state dictionary between ADK tools. Brandon recommended adopting a "sniper" approach, which involves using prompt interpolation to extract and pass only the specific, necessary data points rather than the full state object.

[01:37:08] Ola Oyo: So I was just wondering, like, you know, how do you, how do you reduce the number of tokens as you're passing that state from one tool to another, because I've seen my token count for a request go as high as up to 100k tokens, and it's just exponentially growing up, and I'm like, wow, that's huge, because it's quite a huge chunk it's taken in.
[01:37:31] Brandon Hancock: Yeah, so, yeah, so, I mean, there's, there's a few, there's a few approaches, so, by default, state is not, I mean, I guess it depends how you're using state, so are you, are you, as the application continues to run, so as you go from agent one, two, three, four, five, are you pulling in all the values from state, or what's, I guess, how are we currently using state with your tools and your agents?
[01:37:59] Brandon Hancock: I guess that's just, you know, learning a little bit more about the current situation.
[01:38:02] Ola Oyo: Thank you.
[01:38:04] Ola Oyo: Yeah, I'm pulling in the entire dictionary that has all the values as it's going from one tool to the other.
[01:38:10] Brandon Hancock: So I think that's pretty bloating.
[01:38:12] Ola Oyo: It's up, like, really big.
[01:38:15] Brandon Hancock: Yeah, I mean, the way I tried to be, like, a sniper with state, and what I mean by that is, like, you can do interpolation.
[01:38:22] Brandon Hancock: So the two ways I use state is, like, one is if there's a specific part that I absolutely need, no matter what, I will use interpolation in my actual prompts to make sure it's always there.
[01:38:35] Brandon Hancock: For example, like, if I need to know the current state, the current user, what phase are we at?

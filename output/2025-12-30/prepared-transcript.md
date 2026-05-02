=== SESSION ===
date: Unknown (post-Christmas, early winter season)
duration_estimate: ~10 minutes (transcript segment)
main_themes: Pre-meeting social chat, weather discussion, Claude/Shipkit development workflow, Claude Pro subscription and billing issues, Claude Code usage

---

<!--SEGMENT
topic: Pre-Meeting Greetings and Weather
speakers: Patrick Chouinard, Tom Welsh, Marc Juretus, Ty Wells
keywords: Whistler, Omaha, Colorado, Fahrenheit, Celsius, snowboarding, winter, temperature, Bahamas, mountains
summary: Participants join the meeting and exchange casual greetings and weather observations. Locations mentioned include Patrick's cold 5°F location, Tom's ~2°C UK location, and Ty's Omaha location (~30°F) with plans to travel to Colorado by train. Light humor about cold temperatures sets a relaxed tone before the main discussion.
-->

00:00:59 - Patrick Chouinard: Hey, Marc.

00:01:51 - Patrick Chouinard: Hey, Tom.

00:01:52 - Patrick Chouinard: Hey, guys.

00:01:54 - Tom Welsh: I actually remembered this week for a change.

00:01:58 - Patrick Chouinard: What's up, Patrick, Tom?

00:02:00 - Marc Juretus: Hey, Marc.

00:02:04 - Patrick Chouinard: Good. It's the return of Brendan today, so I'm good. I'm off the hook.

00:02:08 - Tom Welsh: Ah, okay. Has he been missing?

00:02:12 - Patrick Chouinard: For the last week.

00:02:14 - Marc Juretus: He wasn't on last week too? I didn't know that. I couldn't make it last week.

00:02:26 - Marc Juretus: <Q>What's the weather like up by you, Pat?</Q>

00:02:29 - Patrick Chouinard: <A>It's 5 degrees Fahrenheit right now.</A>

00:02:34 - Tom Welsh: That sounds positively warm.

00:02:39 - Marc Juretus: You got that cold over there, Tom?

00:02:42 - Tom Welsh: No. I think we're like 2 degrees Celsius, which is what? Is that 2 minus 32 or something for Fahrenheit?

00:02:54 - Patrick Chouinard: <A>It would be like 28, something like that.</A>

00:03:00 - Tom Welsh: Yeah. I think the coldest I've had — I was in Whistler snowboarding about 10 years ago, it was minus 44 on the chairlift. You could feel it.

00:03:14 - Patrick Chouinard: Oh, we're going to get there. It's early in the season.

00:03:18 - Ty Wells: Hey, guys.

00:03:23 - Ty Wells: Merry post-Christmas, or is that post-Christmas merry?

00:03:29 - Tom Welsh: It must be nice and snowy in the Bahamas, is it?

00:03:33 - Ty Wells: I'm actually in Omaha, and it's not bad today. It is probably about 30, maybe?

00:03:52 - Ty Wells: But I'm heading up to the mountains tonight via train, so it'll be Colorado. It'll be nice and negative something, I'm sure.

---

<!--SEGMENT
topic: Shipkit Claude Skills Workflow Release
speakers: Patrick Chouinard, Ty Wells, Tom Welsh
keywords: Shipkit, Claude skills, GitHub, Discord, community repo, implementation loop, PR automation, Git, roadmap, branches, development workflow
summary: Patrick announces he has published his development workflow — specifically the implementation loop within Shipkit — as Claude skills in the community GitHub repository, with a link shared in Discord. The group discusses potential enhancements including automating pull requests for each roadmap subsection as separate branches, and integrating .gitignore handling into the automation.
-->

00:04:13 - Patrick Chouinard: By the way, as promised last week, I've published my development workflow — the implementation loop within Shipkit [tool:Shipkit] — as Claude skills [tool:Claude Skills] in the community repo.

00:04:29 - Tom Welsh: Nice.

00:04:31 - Ty Wells: Thanks for that.

00:04:34 - Patrick Chouinard: Yeah, I've been testing it all afternoon, and it works pretty well, actually.

00:04:41 - Ty Wells: <Q>Yeah, I'll check it out. It's in the Discord, you said?</Q>

00:04:43 - Patrick Chouinard: <A>Well, I posted it in Discord [tool:Discord] in the show-and-tell, and it's in the GitHub Shipkit AI community repo [tool:GitHub], and the link is in Discord as well.</A>

00:04:58 - Ty Wells: Repos are sort of my life these days — I just can't keep up with the repos themselves.

00:05:09 - Tom Welsh: 100%, so much, as the proverbial firehose.

00:05:17 - Patrick Chouinard: Yeah, actually, I was thinking about maybe adding a PR skill for that loop, so every implementation of every subsection of the roadmap is actually a branch that can be PR'd automatically.

00:05:34 - Ty Wells: That's not a bad idea.

00:05:38 - Patrick Chouinard: ▶ Well, if we can bake the .gitignore handling within the automation, it makes it a little bit easier to keep things clean.

---

<!--SEGMENT
topic: Claude Usage Limits and Billing Issues
speakers: Patrick Chouinard, Ty Wells, Tom Welsh, Marc Juretus, scottrippey
keywords: Claude Pro, Claude API, Claude Code, subscription, billing, usage limits, credits, VS Code, Next.js, FastAPI, Supabase, incognito, reset
summary: The group discusses Claude subscription billing anomalies — including a case where a cancelled subscription still remained active — and usage limit issues with the Claude API versus the Pro subscription. Marc shares his experience hitting API credit limits while building a Next.js/FastAPI project using Claude Code for the first time. The segment includes practical tips on checking usage resets via the Claude UI and a recommendation to use the Pro subscription rather than raw API calls for coding work.
-->

00:06:40 - Ty Wells: <Q>Did you max out your 2x?</Q>

00:06:46 - Patrick Chouinard: <A>Yeah. I just got a warning. I'm at like... let me see what I got here.</A>

00:06:52 - Ty Wells: I was at 78%.

00:07:00 - Patrick Chouinard: ▶ And with the skills, I have even less interaction to do, so I can do even more simultaneous work.

00:07:12 - Ty Wells: ▶ Skills are definitely the way to go. I've been skilling up for a minute now.

00:07:23 - Ty Wells: They extended the hackathon I was on, so I can extend the features. I had the extra credits to do it, so I went at it — that project I spoke to you guys about last week, I've been working on that some more. I'm liking that very, very much.

00:07:45 - Tom Welsh: I have no idea what's happening with you guys and your skills and stuff, because I don't get anything. I've paid $20 a month for Claude [tool:Claude], $20 for OpenAI [tool:OpenAI], $20 for something else, and I see no more bills. The only bills I get are for Supabase [tool:Supabase]. And that's 10 databases for $45. What's going on?

00:08:08 - Patrick Chouinard: <A>Claude has been known to have some invoicing issues in the past. I have a colleague of mine who cancelled her subscription six months ago, and she still has all the Pro subscription features. So I'm thinking that might be what you're into.</A>

00:08:32 - Marc Juretus: So I was actually doing that the last two days. I was using my API and I realized I ran out of money really quick. So I bought the $20 Pro plan. And I'm in a state right now where it says you can't do anything with Claude because you have to insert credits. So I can't even log out to log back in with the correct API — with the new Pro version.

00:08:56 - Patrick Chouinard: Should be resolved normally, but...

00:08:58 - Ty Wells: ▶ Incognito window — you should be able to log in there.

00:09:02 - Marc Juretus: Well, I'm doing it from VS Code [tool:VS Code] in a terminal window. I just had to build a Next.js [tool:Next.js] FastAPI [tool:FastAPI] project just for kicks. It was the first time I really used Claude Code [tool:Claude Code]. It's a little different, but it's pretty good.

00:09:28 - Ty Wells: ▶ You can, actually — if you log in on the UI, go to your settings, go to your usage, and you can see what your reset is.

00:09:28 - scottrippey: Yeah, you can see it on Claude Desktop [tool:Claude Desktop]. And in Claude Code, it's the same thing. ▶ And anybody who's coding should not be using raw API calls.

00:09:35 - Patrick Chouinard: No.

00:09:38 - Marc Juretus: API calls are pretty expensive. Claude is my favorite.

---

=== UNRESOLVED SPEAKERS ===
- scottrippey — raw name not found in SPEAKER_ALIASES map; passed through unchanged.
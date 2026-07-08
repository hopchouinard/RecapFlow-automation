=== SESSION ===
date: Unknown (transcript contains no explicit date)
duration_estimate: ~85 minutes
main_themes: AI model token usage strategies, member project updates (cemetery app, school carpool logistics, appliance predictive monitoring, AI photo booth, CRM/Salesforce automation, estate agency CRM), Claude/Fable workflow optimization, multi-model AI pipelines, infrastructure monitoring, business entity structure

---

<!--SEGMENT
topic: Token Usage and AI Model Availability
speakers: Marc Juretus, mdcatc, Patrick Chouinard, Paul Miller
keywords: Claude, Fable, Codex, Gemini CLI, Ollama, Perplexity, GitHub Copilot, token quota, weekly reset, OpenAI Pro, GPT-5.5
summary: The group opens with a discussion about AI model subscription limits and token exhaustion. Patrick has nearly depleted his Claude and Codex quotas, resorting to Gemini CLI and other fallback tools. The extended Fable promotional period is noted as a reprieve for some members.
-->

[00:00:02] mdcatc: They extended their little promo thing until the 12th, so you can still use it up to 50% of your weekly usage.
[00:00:11] Marc Juretus: Nice.
[00:00:12] mdcatc: So I was just about to be done with it, and now I got five days ahead of me.
[00:00:22] Patrick Chouinard: Lucky you.
[00:00:23] Patrick Chouinard: I'm waiting for my reset.
[00:00:25] mdcatc: Well, mine reset last night at 1am.
[00:00:31] Patrick Chouinard: This meeting is being recorded.
[00:00:33] Patrick Chouinard: Yeah, when's your weekly cycle end?
[00:00:37] Patrick Chouinard: Tomorrow.
[00:00:38] Patrick Chouinard: No, not tomorrow.
[00:00:40] Patrick Chouinard: Thursday night at 8.
[00:00:42] Marc Juretus: What a worry, man.
[00:00:46] Marc Juretus: So you're too productive, Patrick.
[00:00:48] Patrick Chouinard: Well, I don't have any more Fable token left. [tool:Fable]
[00:00:51] Patrick Chouinard: I don't even have any weekly token left.
[00:00:55] Patrick Chouinard: I think I have like 1% left on my weekly quota.
[00:01:00] Paul Miller: <Q>What about your second account? Surely, Patrick, you've got two accounts.</Q>
[00:01:06] Patrick Chouinard: <A>I have one Claude account, but I have one Codex account, and they're both topped off. [tool:Claude] [tool:Codex] I've actually used the two manual resets on Codex as well.</A>
[00:01:17] Paul Miller: Oh, my goodness.
[00:01:19] Paul Miller: <Q>Does that mean you have to take a holiday now?</Q>
[00:01:22] Paul Miller: <A>It means I have two days where I have to be really, really careful about what I ask to which model.</A>
[00:01:32] Patrick Chouinard: I'm actually finding myself using Gemini right now. [tool:Gemini CLI]
[00:01:37] Paul Miller: Oh, my God.
[00:01:38] Paul Miller: Those are desperate times.
[00:01:43] Patrick Chouinard: When you open Gemini CLI these days, yeah, you're desperate for tokens.
[00:01:50] Paul Miller: Well, when you end up doing Ollama, then you really need to take a proper holiday. [tool:Ollama]
[00:01:55] Patrick Chouinard: If you're using Ollama in a local model, then we know Patrick has lost it.
[00:02:01] Paul Miller: Don't worry, I still have a bit of token on Perplexity and GitHub Copilot. [tool:Perplexity] [tool:GitHub Copilot]
[00:02:11] Marc Juretus: Wow, dude, you sound like a guy that's trying to quit cigarettes but has them hid all over the house.
[00:02:17] Paul Miller: You have someone in the glove box in the car.
[00:02:20] Marc Juretus: Go on that coffee can. See, I told you there was three in there.
[00:02:25] Marc Juretus: That sounds like you, Patrick.
[00:02:27] Patrick Chouinard: That's exactly it.
[00:02:30] Marc Juretus: Patrick doesn't take holiday. Holiday is AI. It's just a different version.
[00:02:37] Patrick Chouinard: Well, I had to leverage as much of the Fable token as I possibly could because I actually went over by 123 bucks.
[00:02:54] Paul Miller: Well, it's not too bad.
[00:02:59] Marc Juretus: The one — I do a couple of crypto investments, but long story short, one of them I have is called BitSensor, right, and that's basically like shared GPU, and it's funny when all that stuff went down with Fable and overseas where they blocked it — the stock price went up like 50 bucks as soon as that started getting blocked, so I'm wondering where we get to with shared GPU if that ever becomes a thing.
[00:03:34] Patrick Chouinard: Yep.

---

<!--SEGMENT
topic: Member Check-ins and Introductions
speakers: Ty Wells, Marc Juretus, Paul Miller, Patrick Chouinard
keywords: Copilot Studio, adaptive cards, remote work, Tampa, golf, topic flows, agent development, Microsoft, check-in
summary: Ty Wells joins from Tampa where he is working remotely with family. Marc Juretus reports being deep in Microsoft Copilot Studio work building an agent with adaptive cards and topic flows, leaving little time for personal AI exploration. The group transitions to round-robin updates.
-->

[00:03:35] Ty Wells: What's up, guys?
[00:03:37] Patrick Chouinard: Hey, Ty.
[00:03:39] Paul Miller: Hey, Ty.
[00:03:40] Patrick Chouinard: Hey, no golf tonight?
[00:03:44] Ty Wells: I'm in Tampa with my daughter, my wife and I, for a couple of weeks, so no. I brought my clubs. I haven't played yet.
[00:04:01] Ty Wells: Well, they have a simulator down here, but I might have to go check that out in the evenings.
[00:04:10] Marc Juretus: Boy, the world changed from when we first started, Paul and Ty, right? Like, you could just go to Tampa and work on the road for two weeks. You know, you just couldn't do that before. Like, you were affixed to that desk. What a different world, man.
[00:04:29] Paul Miller: Right, Patrick, do you want me to be the host today?
[00:04:33] Patrick Chouinard: Yeah, if you could, that'd be helpful. I'm taking it next week.
[00:05:01] Paul Miller: Let's start with you, Marc. How are things going?
[00:05:07] Marc Juretus: Pretty good. Not much to really report. I'm in Copilot Studio hell for an agent we're trying to get out. [tool:Copilot Studio] So I'm working with adaptive cards and topic flows and tools. So I haven't gotten to play a lot with AI outside of work because I've had my fill at work, if you will. Best way to probably put that. So I kind of wanted to come up and see what the boys are up to, man. It's been about four weeks since I've been on here.
[00:05:40] Patrick Chouinard: Oh, there's been a ton. I'm going to let people go around the room. But yeah, there's been a lot going on.
[00:05:47] Marc Juretus: Seems like you guys are leveraging Codex more from what I saw in your email. What did it say? It'll let Claude and Codex fight each other out for the correct code? So I want to see that. That's interesting.
[00:06:07] Marc Juretus: But yeah, that's it for me, Paul. I don't really have much to report. I want to see what you guys have been up to.

---

<!--SEGMENT
topic: Cemetery App and School Carpool Logistics App
speakers: mdcatc, Paul Miller, Juan Torres, Ty Wells
keywords: cemetery application, Fable, charter schools, carpool logistics, PHP, class-to-curb, Virginia, municipal government, SaaS, staging deployment
summary: mdcatc updates the group on two applications: a heritage plot cemetery management app stalled by municipal bureaucracy, and a school carpool logistics app ("class to curb") that choreographs student pickup to reduce end-of-day chaos from hours to 15 minutes. Both were recently tested and improved using Fable. The group discusses sales strategy, target markets, and deployment readiness.
-->

[00:06:17] Paul Miller: So mdcatc, what's going on in your world? How's that cemetery application going?
[00:06:32] mdcatc: I ran it through Fable yesterday to clean up any problems with it. [tool:Fable] I found some really nice updates for it, so that was good. I'm still waiting for the county that it's intended for to get off their laurels and actually do something. So I'm looking for a sales rep right now that can go hit up some of the other cemeteries in the state. I'm not waiting any longer for the intended audience.
[00:07:08] Paul Miller: Yeah, it's always the challenge with local government and federal government and state government. It's like getting them to get some action.
[00:07:18] mdcatc: Yeah, it's like nobody claims to have any responsibility or accountability or authority to do something. It's like, how do you guys ever get anything done?
[00:07:30] Paul Miller: Well, you need a politician that's got their ego on the line, then suddenly stuff gets done.
[00:07:44] mdcatc: Well, part of the problem too is that the cemetery that it's intended for is controlled by the city and they just got a new city mayor. There's some changes in their ranks that are interfering with their budget. Like most cities and towns around the world, it's always the usual stuff that ratepayers and citizens want first.
[00:08:23] mdcatc: I just need to really get a good feel on what the penalties are, because maybe they haven't had any yet. But if they can't fulfill a request, then they start to pay penalties and then maybe they'll look at actually solving the problem.
[00:08:52] Paul Miller: <Q>Have you ever — and this is kind of what I do to try and understand — what's the trigger to get customers to get off their seats and spend some money? Where do people that run cemeteries share with their colleagues and discuss what's not happening, that you can have the AI do some deep research and sort of delve into what the hot buttons are to get these guys to have some more hustle to make a decision?</Q>
[00:09:33] mdcatc: <A>Yeah, I'm not sure exactly on the county. I was talking to my brother. He works in the county and he's from the traditional business world, not from government work. And he says his biggest pet peeve is most of the people are applying for the position because it is a government job, so they can just show up and not really do anything. And once they get hired, it's really hard to get somebody fired from a government position.</A>
[00:10:06] Paul Miller: <Q>Are you able to target the private cemeteries? Surely some of those?</Q>
[00:10:15] mdcatc: <A>I've got a list of all the cemeteries in the state and I'm not sure — I haven't mapped it out to see which ones are private or county-run. This requirement is only applicable to county-run cemeteries. The private cemeteries or the commercially owned cemeteries don't have to apply or are not affected by the ruling.</A>
[00:10:51] Juan Torres: <Q>Is it possible to go to your — so it's municipal city level, right? Who would be the client? Do you think it will be fruitful to go to the city town hall meetings that municipal governments have and then talk to the city council members and be like, hey, this is how my application is actually going to save the city government more money — and kind of carry a mini political campaign for your application in that way?</Q>
[00:11:30] mdcatc: <A>Yeah, that would be great except it's in a different state and I can't attend at this point. It would be a trip out and I don't know when their next meeting is, so I need to find somebody who would be willing to go do that. That's why I'm saying I'm looking for somebody in that local state to go do my sales stuff.</A>
[00:11:53] Juan Torres: I think more than anything it's finding time for you, because I would think you're the best salesperson for the application at this point.
[00:12:15] mdcatc: Yeah, no, I don't disagree with that at all.
[00:12:19] Ty Wells: I would add to that — yes, you would be the best person, but if that's not a soft skill that you do, don't do it. Find somebody who you feel comfortable with expressing, from a sales perspective, what you're trying to articulate. Once you're comfortable with that person, then you can release the kraken, if you will. But they've got to pass your test that they understand the product and the vision that you have.
[00:12:57] Paul Miller: And the problem.
[00:13:00] mdcatc: Yeah, the full problem.
[00:13:03] mdcatc: We'll work for tokens.
[00:13:16] Paul Miller: Yep, we're all working for tokens now.
[00:13:42] mdcatc: So that's kind of the status on the cemetery, the heritage plot. The other one that I've worked on and had Fable run through was my class-to-curb, which is a logistics end-of-day school system to get the kids to the cars at the right time in all the charter schools. The issue there is they're in areas that aren't built for schools — usually they're in business districts and nowhere near neighborhoods. So everybody carpools. And the end-of-day pickup is always a mess.
[00:14:22] mdcatc: The system choreographs it so that the students leave the classroom — their picture shows up, they leave the classroom — and by the time they get to the curb, the car is at the curb. So it's a logistics system matching up the incoming cars with the students in the classroom so that the flow is consistent.
[00:14:44] mdcatc: This is the second version of this I built. The first one I did was maybe 15 years ago using PHP. [tool:PHP] And we had, at that time, reduced our carpool mess from — some days it was like two hours long — down to like 15 minutes. So it's a drastic change and affects a lot of people positively.
[00:15:14] Paul Miller: That would be big in Australia and New Zealand around the private schools.
[00:15:20] mdcatc: Anywhere — all the private schools have that same issue. They all set up in a business district area because it's where they get cheap buildings.
[00:16:00] mdcatc: Yeah, when the school was in the neighborhood, that was different. Everybody could walk. But these charter schools and private schools, they're not in the neighborhood. They're in business districts, and the students going to them are not necessarily within a geographic district. Anybody can sign up and go to those charter schools.
[00:16:25] Paul Miller: <Q>Do the schools pay for the SaaS? Is it a school thing that they buy?</Q>
[00:16:31] mdcatc: <A>Yeah, it would be an app service that they would pay for.</A>
[00:16:37] mdcatc: ▶ The selling point — I'm going to put a calculator on the front page that shows how much time is wasted every month from everybody involved: all the parents, all the teachers. There's a lot of time of everybody sitting around waiting for something that should be relatively quick.
[00:17:00] Paul Miller: The thing that occurs here is what you get is the city where the school is based gets in trouble with the traffic authorities saying that there's too much chaos — we're going to impose restrictions or penalties because you put the whole area around the school in gridlock at this time because you don't have a better system. That would be a big selling point.
[00:17:45] mdcatc: Yeah, I have it deployed on a staging environment. I haven't actually deployed it to production yet. That's my next step.
[00:18:05] Paul Miller: Who would have done that without Fable?
[00:18:07] mdcatc: The whole process was Fable doing all the testing on it, running it up, load testing, everything. It was great. I was like, holy crap, this thing is amazing. Found all the little problems and fixed them and it's just freaking nice.
[00:19:03] mdcatc: I reformatted my Windows machine. Goodbye, Windows.
[00:19:35] mdcatc: I spent a few days this last weekend rebuilding and finding tools that I thought I had figured out what I needed. And you always find something and it's like, oh, I forgot about that.
[00:19:55] Paul Miller: My "forgot about that" was all the custom fonts I had installed.

---

<!--SEGMENT
topic: Ryan's Fable-Powered Development Spree
speakers: Ryan C, Paul Miller, Juan Torres, Patrick Chouinard
keywords: Fable, Claude Design, Mac Mini, estate agency CRM, finance automation, voice agent, iPhone app, Hermes, Mac OS, ADHD, personal assistant
summary: Ryan C describes an intense week of AI-assisted development using two Fable Max accounts, building a personal finance Mac OS app with voice agent, an estate agency website, and extending a CRM. He also purchased a Mac Mini to set up a personal AI assistant for phone calls and appointment booking, inspired by Patrick and Scott's setups. The group humorously notes the group's collective AI addiction.
-->

[00:20:03] Paul Miller: Ryan, what's happening in the UK, other than celebrating getting through the next round of the football?
[00:20:13] Ryan C: Well, cheaters never prosper, that's what they say. Getting one of your players unbanned because essentially Trump has — I don't know, one of them's got dirt on each other. But anyway, it is what it is. You got battered anyway, so you came up against a superior team.
[00:20:46] Marc Juretus: Well, what was happening wasn't unprecedented, where they overrode a decision like that. Granted, it did come from Trump, but I've heard this has happened in the past.
[00:21:00] Ryan C: I think it was free the tournament, which was also corrupt because they wanted him to play in the tournament because having Cristiano Ronaldo in the tournament is massive.
[00:21:29] Ryan C: What have I been doing? I got Fable Fever, let's just put it that way. I've spent £400. I bought two Max accounts. I've built two apps from scratch. I decided that I couldn't be bothered to manage my own finances via the horrible spreadsheet that I built a couple of years ago when I started my business. So I built my own Mac OS application that automates it from my invoicing system. [tool:Fable] I just chuck some invoices into a folder. I've got it scraping my Amazon. And then it just populates a spreadsheet for me that I send over to my accountant, and anything it's not sure about, it asks me. I built a full voice talking agent into it to discuss things — like, oh, can you just knock me up an invoice for this — and I'm going to create a little iPhone app for it as well, so I can just do stuff on the go.
[00:22:19] Ryan C: I built an entire estate agency website with it that's going to launch next week — in three days. And then I've shown you guys the CRM that I'm working on for an estate agent. I had a full scan of that, and I've pretty much done an extra 50% of stuff on that. I bolted a whole load of stuff on. I found that it works really nicely in Claude Design. [tool:Claude Design]
[00:22:44] Ryan C: The design stuff on it is on another level versus what Opus was doing. [tool:Claude Opus] So I've got it to make me a bunch of stuff in there as well, which is quite cool. And they've obviously just extended it to the 12th. So once my thing resets in about 45 minutes, I will be back on it.
[00:23:18] Paul Miller: Oh, is that a mini?
[00:23:19] Ryan C: That mini, yeah. [tool:Mac Mini] So that's a grand and a half in the hole that I'm not going to get back, so thank you Patrick and Scott for essentially making me buy that.
[00:23:32] Patrick Chouinard: Wait a minute, I never made you buy a Mac Mini. I built all of my Hermes install on Linux. [tool:Hermes]
[00:23:40] Ryan C: And then you showed it off, and I was like, hmm, I think I need to have one of those. And then Scott then got his to start making phone calls to people, and it's incredible. And that's kind of one of the things I wanted to do because I've got ADHD, so I'm one of those people that if it doesn't give me dopamine, I don't do it. So I need a dentist appointment, I put it off for three months.
[00:24:00] Ryan C: So I'm going to make this my PA essentially, give it a whole personality — I'm going to have pretty much the same setup that Patrick and Scott have, build that out and get it to make phone calls and book appointments for me and stuff like that. So that's the plan. I've literally just mounted it to the bottom of my desk.
[00:24:29] Ryan C: I've not got any sleep this week. I'm going to sleep at about 4am, waking up at 6am and then cracking on.
[00:26:04] Paul Miller: At what point do we need counselling is the question.
[00:26:07] Juan Torres: Yeah, I was going to say that. Thank you for addressing the elephant in the room, Paul.
[00:26:14] Ryan C: Scott is telling me he's worried for my health.
[00:26:16] Juan Torres: We're worried, Ryan.
[00:26:18] Ryan C: I thought I only had Fable until literally 45 minutes' time, so I've just been throwing everything at it across two accounts.
[00:26:40] Juan Torres: Sentiment analysis, machine learning model to assess the state of mind of our attendees.
[00:27:25] Ryan C: I literally maxed out 100% on Fable and literally the weekly limit. My own account resets this evening, which is great. But my other account only resets on Saturday. So I've said to the missus, you're going to see me on Sunday. All I'm doing from midnight on Saturday onwards is coding. So she's going to have to accept that.

---

<!--SEGMENT
topic: Ty's Predictive Appliance Monitoring System (Q)
speakers: Ty Wells, Ryan C, Paul Miller, Patrick Chouinard
keywords: predictive maintenance, electrical signal analysis, ice maker, refrigerator, wattage monitoring, IoT, smart plug, service company, Bahamas, commercial refrigeration, Suntory, vending machines
summary: Ty Wells presents "Q," a predictive appliance monitoring system that reads electrical power signatures to identify component failures before they occur. Built for his Bahamas-based low-voltage service company, Q establishes a seven-day baseline of wattage patterns per appliance and uses manufacturer specs to detect anomalous trends. The group discusses commercial applications including cold storage, convenience stores, and large-scale vending machine fleets.
-->

[00:28:57] Ty Wells: Okay, meet Q. Fable is — well, you know, I have a company in the Bahamas that's a service provider. We do CCTV, access control, life safety systems, fire alarm systems, all the low-voltage type stuff. And so what had happened was my ice maker was on the fritz for the last probably year. And so I put a smart plug behind it, the refrigerator, so I could just have it recycle the power every week. That seemed to work for a while, but last weekend it just wasn't working. Wasn't generating ice. Had people over. It was a situation.
[00:29:54] Ty Wells: So I decided I'm going to figure out why it's not working and identify exactly which part of it is failing. And so what I'm doing is I'm reading the electrical signal — the power, the voltage that's being pulled, the wattage that's being pulled — and I'm restarting the refrigerator. It reads the wattage that's being pulled on a fresh start, on a cold start. Refrigerators do certain things — in particular, the ice maker pulls water, makes the ice, turns on the heater, releases the ice. It's called an ice harvest process. The compressor runs when the temperature gets to a certain degree. Every time something goes on, it leaves a signal as to what it's doing.
[00:30:50] Ty Wells: ▶ Using the manufacturer's own specs, I use that along with a seven-day baseline to figure out what's happening with the refrigerator. So for my service company, instead of them offering a reactive service, this is basically: I know when you're about to fail and I know what is going to fail because I understand how you work, in terms of any electrical appliance.
[00:31:43] Ty Wells: So all of the — for my service company, this is what we will be implementing — from 400 amps, 200 amps, big equipment to just a refrigerator, even a 220 like a wall dryer. The point is, it's actual predictive analysis based on the electrical signals as opposed to the median time for failure or guessing what's going on with your device.
[00:32:27] Ty Wells: So that's what Q is all about. That's what I've been working on for the last week or so. And it's actually pretty good.
[00:32:37] Ryan C: Having worked for Samsung for a number of years within the refrigeration department, Ty, that's sick. Essentially, you've just rebuilt SmartThings, [tool:SmartThings] but with actual real-time electrical signal reading. It's actually smarter than what they're doing.
[00:32:55] Ty Wells: Yeah. I mean, a lot of them have thresholds — like, if it hits this, send a signal. I'm saying I see a trend, right? I see this is where it's going based on the baseline and you're about to fail. So in the middle of winter, you don't want your furnace failing. The service provider needs to come and do the actual work of changing the part, but what you've done is identified the part, preemptively ordered the part, and your technician is now more efficient. He's not guessing.
[00:33:36] Ty Wells: But it's a learning system — it's AI. So every Samsung refrigerator of this model, it's learning, not just based on what it is, but the environment. And there's a second backup to this: you'd have a sensor in the refrigerator. So if the compressor's working too hard, you should see a drop in temperature. Those type of signals — like in an AC unit, you may have a leak detector that accompanies the power signature.
[00:34:25] Paul Miller: <Q>Have you thought about commercial customer types? Because I used to run all the IT for Coca-Cola New Zealand and a lot for Australia, and then the same for Pepsi. A massive opportunity for these beverage companies.</Q>
[00:35:17] Ty Wells: <A>Yeah, the cold storage trailers — they have units in there that they've got to check, like somebody has to physically go check every six hours to make sure it's on, it's plugged in. Think about convenience stores, restaurants that lose their stuff.</A>
[00:35:47] Paul Miller: Or a retirement community, where a lot of the appliances are provided by the community and proactively managing because they're the assets of the company that owns. The base units where you can get really big commercial customers. I know the Pepsi bottler I worked for got taken over by Suntory in Japan. And the challenge that Suntory had is they've got millions of automated vending machines in Japan. If you multiply millions by a thousand dollars a device, if you can reduce the cost of maintenance tracking to the minimal level, then you've got certainly got global opportunities for selling this type of service.
[00:36:48] Ty Wells: Yeah. And even from the insurance perspective — they're requiring certain things when they're covering food spoilage. They would require that more than the actual merchant.

---

<!--SEGMENT
topic: Ty's Tee Time Locator and ERP Cashless Payment Project
speakers: Ty Wells, Paul Miller, Patrick Chouinard
keywords: tee time locator, PWA, Arena Skill, mobile optimization, ERP, Linga POS, cashless payment, Bahamas, beach excursion, Claude Codex
summary: Ty briefly demonstrates his golf tee time locator PWA, which uses an "Arena Skill" design competition approach in Claude to produce polished mobile-optimized UI. He also mentions a new ERP project for a Bahamas beach excursion client who wants to go cashless, replacing their current credit card and cash system with a fully integrated solution.
-->

[00:37:28] Ty Wells: So I made quite a few changes here, as you can see. These are golf tee times based on what's available — sort of a list there. You can see the list and so forth. You can call them directly, or you can go by the course. I recently added the map, so you can easily see based on where I'm at, these are my closest courses.
[00:38:00] Paul Miller: <Q>What did you do for the design, UI, UX? Was that with Claude Design, or do you just...?</Q>
[00:38:07] Ty Wells: <A>No, I have this thing called Arena Skill. [tool:Arena Skill] I've got a skill that has like Impeccable UX and Front Design and something else — there's like five of those skills and they compete against each other to come up with the best design. And then I have another skill that is a mobile optimization skill for mobile, because obviously this is a PWA, so it optimizes for that. [tool:PWA] So what you're seeing there — if you pull up on your phone, you'll see how it looks, but certainly it's very — you think you're in an app, and obviously if you do it as a PWA, you would be in an app.</A>
[00:38:54] Ty Wells: One more thing. So our ERP system that we have for that service company — we have a client that does, we resell some software called Linga POS, [tool:Linga POS] and they have a beach getaway in the Bahamas. The cruise ships come in, they bus the people to this beach — a day on the beach sort of excursion, you know, beach activities, water sports, massage, bar, that sort of thing. And so they called us today and said the sales manager wants to go cashless, because right now they do credit card and cash. So that's a project that — they're a great paying customer, they pay annually — so I will definitely be pulling that into the ERP to go with a cashless-based system.
[00:39:55] Paul Miller: Nice.
[00:39:58] Ty Wells: I think that's me for the day, guys.

---

<!--SEGMENT
topic: Juan's AI Photo Booth App and Infrastructure Monitoring
speakers: Juan Torres, Patrick Chouinard, Ty Wells, Paul Miller
keywords: image-to-image transformation, AI photo booth, Wavespeed, multi-model pipeline, CloudWatch, Aurora Serverless, EC2, Prometheus, Alert Manager, GTA 6 style, AWS, LLC, S-Corp
summary: Juan Torres describes his AI photo booth application that performs image-to-image style transformations at live events, including a newly added GTA 6 aesthetic style. He is working on CloudWatch observability for his EC2 and Aurora Serverless 2 infrastructure. Patrick recommends Prometheus and Alert Manager for monitoring the physical mini PCs at event venues. Juan also asks the group about LLC S-Corp tax structure for his business.
-->

[00:40:00] Paul Miller: Juan, what's happening with your app and your appliance that you're building?
[00:40:09] Juan Torres: Well, last week I was working just on getting the AI multi-model pipeline set up. But just to give context — I'm building an application that allows image-to-image transformation for an AI photo booth service that will transform original pictures taken at an event into AI-generated images. So that's what I'm building.
[00:40:52] Juan Torres: At the stage I'm at, I was working on getting the multi-model pipeline ready and set. There was a small bug that I had to fix. And then I started to add new styles, new transformations. I have a whole system to test and productionalize new styles. So I use the desktop version of Wavespeed [tool:Wavespeed] in order to test a couple of styles that I want to use for transformation. And then my data web application allows for easy deployment into the frontend. So in terms of the dynamism and flexibility, it's there.
[00:41:47] Juan Torres: For example, I recently created a GTA 6 style. I know for a fact that a lot of youth are going to love a style that's related to GTA 6.
[00:42:27] Juan Torres: And then this week, what I'm working on is having the right observability by having CloudWatch alerts [tool:CloudWatch] in case there's more than 80% above the disk, the CPU utilization, the memory — just to make sure that when I deploy it in the field, I can observe that everything is up and going. I have the same alerts that I'm going to be setting up for the database, which is Aurora Serverless 2. [tool:Aurora Serverless] And also I'm going to be working on having a dress rehearsal of packing and installing the equipment, so I can document it and go through the smooth process of installing and uninstalling the whole setup.
[00:43:29] Patrick Chouinard: <Q>I was just wondering, Juan, what are you using for your monitoring and alerting at the infrastructure level?</Q>
[00:43:38] Juan Torres: <A>I'm using CloudWatch. For my EC2 instance.</A> [tool:EC2]
[00:43:47] Patrick Chouinard: I thought you were monitoring the hardware of the booth itself.
[00:43:52] Juan Torres: No, actually, that will be something that I would like to centralize because I am monitoring the EC2 instance, but I am not doing so for the actual physical mini PCs that I have. So if you have a suggestion, a means to centralize it, that would be great.
[00:44:13] Patrick Chouinard: ▶ Prometheus and Alert Manager. [tool:Prometheus] [tool:Alert Manager] Prometheus is the monitoring platform if you want. And Alert Manager is an add-on to Prometheus that will publish the alert to whatever channel you want. It can talk to Webhook, it can talk to N8N, [tool:N8N] it can talk to Discord, it can talk to whatever you want.
[00:44:43] Juan Torres: I mean, I can even add it to the data web application as a monitoring tool. Okay, I'm going to check it out — Prometheus and Alert Manager.
[00:45:28] Juan Torres: I do have a question that I posted on the site, and that is — especially for the American business people here — I have an LLC, Limited Liability Company, S-Corp tax category. So that's what I'm thinking of using for managing the service. Anyone have experience with dealing with LLCs, particularly for what I'm trying to do? Do you guys think it's a good option?
[00:46:07] Ty Wells: <A>That's the way I operate right now. So it's been working well for me, but I have accountants that make sure it works well. Certainly I would say make sure you get professional help on setting it up and what your objectives are. You can get it from GPT-4, [tool:GPT-4] but it's good to get that advice. Actually, double check it with GPT and get the questions that you want when you go in. Put the scenarios in there and then go to them when you're at the tip of the spear and you know exactly what questions you really have.</A>
[00:46:56] Juan Torres: I already have it and I GPT'd it. A little too late, but yeah.
[00:47:02] Ty Wells: Yeah, but I'm saying make sure you get an actual person — a tax accountant. My goal is set with them, and they have to meet that, so whatever it takes to get to that point.
[00:47:28] Juan Torres: I actually did my taxes with GPT last year, and then I took it to an accountant to see if anything needed to be corrected, and she was like, everything seems fine.
[00:48:01] Ty Wells: Trust me, I did the same, because these guys charged me quite a bit, and I wanted to see what they did this year, and they actually found a little bit more. So you've got to weigh that in.

---

<!--SEGMENT
topic: Patrick's Fable Repository Analysis and Architecture Workflow
speakers: Patrick Chouinard, Paul Miller, Ty Wells, mdcatc, Juan Torres
keywords: Fable, Claude Code, Opus, repository analysis, JSONL, Hermes, architecture spec, Snowflake, Databricks, install.md, UltraCode, LanceDB, multi-model pipeline, training material
summary: Patrick describes an intensive Fable session where he pointed it at 160 repositories, all past Claude Code JSONL session files, and Hermes agent memory simultaneously. Fable autonomously discovered project relationships, connected to his network via SSH, read Hermes memory, and proposed a unified architecture including an operating system layer on top of Hermes. It also auto-generated AI-guided training material and install.md connector scripts for Snowflake and Databricks. The group discusses the workflow of using GPT-5.5 Pro for PRD generation, Fable for architecture, Opus for coding, and Fable again for PR review.
-->

[00:48:34] Patrick Chouinard: Well, I'm token poor because I was token intensive last weekend, let's say. No, I really milked my Fable subscription as much as I can, and now that there's a couple of days more after my reset, I'm going to melt down some servers again.
[00:49:01] Patrick Chouinard: ▶ Basically, I have made sure that Fable did not write a single line of code. I had Fable architect all the solution I possibly could, write all the spec I possibly could. So basically now I have a pipeline of, I don't know, three to four months' worth of stuff to be developed by Opus. [tool:Claude Opus]
[00:49:29] Patrick Chouinard: So that's why I spent my tokens. I really wanted to spend all of the Fable power as much as possible to spec stuff within an inch of its life in order to make sure — and I specifically told Fable in my prompt — like, you're creating those specs for Opus, make sure that Opus can code that perfectly, so add even more detail if possible.
[00:49:56] Patrick Chouinard: ▶ And I find that it makes a difference when you tell a model that you're the best, that it's creating something for a lesser model. I don't know if it's condescending by nature, but it does add more detail.
[00:50:15] mdcatc: Negative prompts work.
[00:50:18] Patrick Chouinard: It works. It actually works. And I've developed some of the things it actually created based on its recommendation, and it went flawlessly. I had barely any rollback or anything. It was really, really smooth sailing development, almost just executing the design.
[00:50:47] Ty Wells: And what you did is sort of what I did, although I had to build some stuff because I wanted to see that it was capable. Planning is great, but I ran into — this is just for the community — I ran into an issue because I maxed out on my three plans. I was doing something in Claude 4.8 and it failed. Something about transcribing YouTube. And so I was trying to identify what that gap was. So what I had Fable do is identify what that gap was. In this other session with 4.8, this is what it said it couldn't do — and why did it say it couldn't do that when you were able to do it? So fill that gap for me.
[00:51:54] Ty Wells: And then I said, what other areas would be different? What would I try to get to the root cause of its harness? Because that's really the big difference, right — the harness with Fable 5. It tries more, and that's why it's so good at cybersecurity, that's why it's good at breaking stuff. It goes deeper, it doesn't stop at the first failure, it continues on to try to solve the problem. And I saw that again today — it solved something that was, for me, unsolvable.
[00:52:57] Patrick Chouinard: ▶ Absolutely, and that's why I have it do my architecture, because it will do that retry until it finds an architecture that works, and then Opus or Sonnet just have to execute it. [tool:Claude Sonnet]
[00:53:15] Patrick Chouinard: Actually, Ty, I think you're going to like this one. I set it at the root of my drive where I have all of my projects. I had 160 repos on one drive. And I basically told Fable: analyze this entire list of repositories, front, right, and center. Try to see all possible relationships between the projects, how you would restructure them, how you would maybe merge some of the repos, separate some of the repos, fill gaps between some of the repos. I have a prompt that's about three pages long, basically telling it to attack this corpus every way it could.
[00:54:36] Patrick Chouinard: Plus, I gave it all of the past Claude Code session JSONL files. [tool:Claude Code] So all of the sessions I ever had with Claude Code, plus all of the JSONL files from the co-work sessions I ever had. And then I launched it with UltraCode. [tool:UltraCode]
[00:55:04] Ty Wells: Yeah, I love that one. Well, it re-engineered my entire coding infrastructure.
[00:55:15] Patrick Chouinard: I'm telling you, I have like three months' worth of coding to do with Opus in front of me. And everything I've done so far has been spot on.
[00:55:35] Patrick Chouinard: And basically, it's not like, oh, everything you're doing sounds like an operating system. So let's build an operating system on top of Hermes.
[00:55:39] Paul Miller: Wow.
[00:55:42] Ty Wells: Yeah, it is pretty good. And I did what you did, but I did that on a couple of specific projects, because I don't think I want it looking at all my repos. It may get excited.
[00:56:00] Patrick Chouinard: Yeah, and honestly, it floored me. It found things I didn't even remember I had. Its capacity of searching is insane. I mean, I didn't talk about Hermes. I didn't talk about the fact that I had an Assistant VM on my network. There are some projects in my code, and I'm talking about Hermes in some of the conversations with Claude Code, but my prompt didn't mention it whatsoever. It actually found the information. It found that I had a network inventory in one of my projects. It actually found the VM where Hermes was set up. And since I have an SSH authentication to it from my main workstation, it connected onto it. It actually read the entire memory of Hermes. It added that into its analysis. Figured out from Hermes that it had access to the webhook and actually connected to the webhook, downloaded all of the conversations, analyzed the conversations, added that on top of it.
[00:57:20] Paul Miller: Now none of us will have tokens after following your lead.
[00:57:31] Patrick Chouinard: But honestly, what it did is absolutely insane. It found some very old projects that I did that I didn't even remember. And it said, you know what? If I use some of that base and reapplied it to this new project, then we can make this third new project.
[00:58:00] Patrick Chouinard: Yeah, most definitely, because I also use it at work. So once I had that success this weekend, obviously Monday morning I had to try it on someone else's token. So I did the same thing at the office for all of the work-related repos that I have, that I work on, that have basically all been coded by Claude anyway.
[00:58:37] Paul Miller: That would be great for your challenging work environment where your management team got everyone excited about doing their own thing. Now you can finally grab some careful thinking back and look at where the gaps are and look at how to make it better.
[00:58:57] Patrick Chouinard: And it did a couple of things — I mean, I don't know how I'm going to be able to share them because they're work-related, but the concept: it saw that I do a lot of training, so I create a lot of training material. And it built a training for Claude Code because we're in the pilot to introduce Claude Code to the developer community internally. It saw that I had a lot of started-but-not-finished training material. So it actually created me a training that is executable by itself from Claude Code.
[00:59:43] Patrick Chouinard: ▶ Basically, it gave files that have all of the material for the training, and you just load up the project in Claude Code and say "hi." It starts and says, oh, welcome to this training, here's the list of exercises, which one do you want to do? And then you can go on and decide. It's like a training where you are the hero. You just point to whichever part of the training, it will open the file, it will guide you through the entire training. It's basically AI-guided training for AI.
[01:00:17] Paul Miller: That's fabulous. Well, that might answer a common question that many of us have. The question is, the challenge is how do you get lieutenants that have the skill set and the understanding that you can take them through a training methodology that gets them up to scratch really quickly. You might've just discovered that. That's the way.
[01:01:07] Patrick Chouinard: Yeah. Because as you give more context — obviously what people will do in that training — if you start to say, oh, but in my case, I would use AI to do this thing — well, you're talking to a live model, so it will take the content, plus what you're giving it, and it will adapt the training as you're going along.
[01:01:34] Paul Miller: That's very cool.
[01:01:40] Patrick Chouinard: And also, we are putting in place a lot of connectivity between Claude Code and all of our internal Databricks [tool:Databricks] and Snowflake [tool:Snowflake] and all of the internal data services. And we're having to guide people as to how do you configure this connector and how do you configure that connector. It puts a lot of load on the support team. Well, when I did the walkthrough with Fable, it found it, and it proposed to write install.md for every one of those services — which are basically install scripts but in plain language — to give to the harness itself in order to add its own connectivity.
[01:02:32] Patrick Chouinard: ▶ And it works! So now you want to configure Snowflake, you just call the install.md from Snowflake, and it will do whatever it can automatically, and it will hand the user guidance step-by-step for whatever they need to do, if they need to create a token or create an authentication of some kind. It's just going to guide them through.
[01:03:01] Patrick Chouinard: ▶ Yeah, the use case of using Fable to inspect all your work and surface insights you might never have thought about is an insane use case.
[01:03:17] Paul Miller: Now I'm going to be burning my Fable tokens today.
[01:03:23] Ty Wells: Patrick, you need to DM me that prompt so I don't have to spend a token to get it.
[01:03:28] Paul Miller: Yeah, send it through to me as well.
[01:03:35] Paul Miller: Maybe put the Stripe interface over it first, Patrick, and then share the link. [tool:Stripe]
[01:04:05] Patrick Chouinard: I'll dig it out of my conversation history. I might tweak it a little bit because there's a lot of "get into the mind of Patrick" in there.
[01:04:21] Ty Wells: No, that's the part we want, Patrick.
[01:04:35] Ty Wells: Let's rephrase that — unfiltered. I forget this is recorded. Unfiltered.
[01:04:40] Patrick Chouinard: Yeah, now what I'm thinking is that there's going to be some AI going over the transcription. I'm going to be anxious to see the recap of this meeting.
[01:04:52] Juan Torres: It's not safe for work because of the number of tokens it consumes.
[01:05:02] Patrick Chouinard: So, yeah, no worries, I'll find it and I'll post it on the forum.

---

<!--SEGMENT
topic: Paul's CRM Data Insights and Android Emulation Demo System
speakers: Paul Miller, Patrick Chouinard, Juan Torres
keywords: CRM, Salesforce automation, LanceDB, Fable, Claude Code, Android emulator, demo data, field sales, Salesforce.com, deterministic data, self-learning, virtual users, PWA
summary: Paul Miller describes two major Fable-powered projects: first, a data insight layer for his 10-year-old CRM/Salesforce automation platform using LanceDB for deterministic ground truth with AI interpretation and self-learning feedback loops; second, an Android emulator automation system built by Claude Code that simulates virtual field sales users interacting with their Android app to generate realistic demo data — solving a three-year-old request from his dev team in a single overnight session.
-->

[01:05:12] Paul Miller: On my side, I've used up most of my Fable tokens on — I've got a project. You guys might remember that I have a kind of a CRM slash Salesforce automation company. It's been running for 10 years. We have customers across Australia and New Zealand. They go out to retail stores, they audit the stores, encourage them to buy more products, do all sorts of interaction with field teams. But basically there's 10 years of data for many customers in there. And there's objectives with — look, I need you to get this — there's sales.
[01:06:00] Paul Miller: So I thought, I need to put all of those data insights together, and I want to throw them all at Fable. I want a system — and I looked at what you'd done, Patrick, with your analysis using LanceDB [tool:LanceDB] — build a base layer of a fully deterministic understanding of base data, make it very clear to the AI models that are working with the data analysis and interacting with users to always look at ground truth through the SQL side of things and through the LanceDB side of things, and then only use AI to interpret what it's seeing. And then doing self-learning based on asking customers and asking people across a sales organization: am I right to conclude that this is the outcome you're trying to achieve, or that this week was a good one, or this week had its issues — and then feed that back into the model.
[01:07:00] Paul Miller: And what it's built is this incredible level of insight for each of our customers that advises on the top level of management, the operational management of the field sales team, and the salespeople and their customers, as to how well they're doing, where the opportunities are, and where the coaching needs to be. And my God, it blew my mind.
[01:07:43] Paul Miller: I've looked at what Salesforce.com [tool:Salesforce.com] — so I don't know if you read in the press — that's our big nemesis competitor. They spend more on marketing than any other tech business that's out there, and they're losing money. We're cancelling Salesforce.com as many CRM companies are losing money at the moment, but we're kind of making sure that for our customers, we can give insight around the data and how they should be operating their teams better.
[01:08:19] Paul Miller: The other big win for me — I had a customer that said, show me a video of your data reporting, show me your demo environment, take me through how all your reporting works. And the problem is the reporting of a CRM type Salesforce automation company needs to be based on realistic data, not sort of random stuff. We can't use, of course, any existing customer data. And I've been asking my dev team for this to be there for me to do demonstrations for about three years now.
[01:09:13] Paul Miller: What I managed to do — I got Fable to recreate virtual users and gave them Android phone devices with our actual application. So they log into the Android device and Claude Code built an app to run multiple Android phone emulators [tool:Android emulator] and behave as if they are virtual users doing all of the tasks that the system sets. And then it tracks all the performance. The application does screenshots all the way. If it doesn't know functionality, it can look visually at the app and see what it's doing. So while a lot of people are using the browser-based approach where you can control a browser-based application, you can use it for Android emulators and get it to control Android emulation.
[01:10:25] Paul Miller: And it's basically testing and simulating and creating demo data for all of the app automatically. And I've just been able to build up all sorts of scripts. So in a couple of hours — when I was told that, oh, it's going to take months and we don't have the time, we don't have the resource — thank you, Fable. Built it overnight.
[01:10:50] Paul Miller: But the wonderful thing from our company's perspective is that it doesn't touch any of our core system. We're using off-the-shelf user-based application access and it's creating artificial demo data externally, which is then going back into our reporting system and now fully usable with a full audit history.
[01:11:26] Paul Miller: Not enough hours in the day or tokens in the world.
[01:11:30] Juan Torres: That's wild.

---

<!--SEGMENT
topic: Multi-Model Workflow Strategy and Omigent Tool Discussion
speakers: Patrick Chouinard, Paul Miller, Ty Wells, Juan Torres, Ryan C
keywords: GPT-5.5 Pro, Fable, Claude Opus, Sonnet, Codex, GitHub, Hermes, Omigent, CMUX, Warp, OpenRouter, multi-model pipeline, PRD, architecture workflow, token optimization
summary: Patrick shares a recommended multi-model workflow: use GPT-5.5 Pro to generate the best possible prompt and PRD, pass to Fable for architecture, Opus for coding, and Fable again for PR review. The group discusses automating model switching via GitHub as a coordination layer and using Hermes agent swarms for QA. Ty introduces Omigent, an open-source harness-between-models tool, and the group evaluates its potential alongside CMUX and Warp terminal for managing multi-account token switching.
-->

[01:11:37] Patrick Chouinard: And by the way — if you have some questions that you think are Fable-level, and it's not exactly the same, but it's close enough — remember that if you have an OpenAI Pro account, even the $100 one, you have access to GPT-5.5 Pro, [tool:GPT-5.5 Pro] and the Pro version — it's not Fable, but it's close. So it's not going to develop — it could give you code insight — but it's only accessible through the web chat. If you want to use it as an API, it's three times the cost of Fable. So you're not going to use it like that. But to figure out problems, actually to write prompts for Fable, it's actually pretty insane.
[01:12:43] Ty Wells: And through the web chat, you have access as much as you want. Yeah, that's what I've been doing. I've been using Pro to just hash the madness out of it. And then I take it — it produces a PRD for me — and I throw that into Fable. Fable actually says, this is pretty good. This is better than I expected. So I'm like, yeah, I know. It came from Pro.
[01:13:12] Patrick Chouinard: But yeah, it's another high-level model that we can have access to for a reasonable amount of money.
[01:13:20] Paul Miller: It's a nice strategy, Patrick, because I had — in those very depressing weeks in between when Fable first came out, it was horribly taken away from us, and then it came back — I did a lot of that: start things in Claude with Opus, then move it back to Codex, getting all the proposed requirements documents and PRDs checked backwards and forwards, and certainly got some better outcomes.
[01:14:04] Ty Wells: I think Fable is actually a little bit better than when it first came out. Because I'm sure they didn't stop working on it. They use the analytics to tweak it because it doesn't flag me as much as before. It would say anything, it would flag. I didn't even say anything. It's better at that.
[01:14:41] Paul Miller: Presumably, Anthropic had access to all of that compute that they were getting from SpaceX. [tool:Anthropic] So they just moved it to training because they didn't have to do inference over those few weeks. And they're probably quite dynamically moving it backwards and forwards because they've got that fixed contract with Elon.
[01:15:03] Patrick Chouinard: They pretty much bought Colossus One, so.
[01:15:15] Patrick Chouinard: ▶ So, just as a reminder, the workflow is: give everything you can to GPT-5.5 Pro, have it come up with the best possible prompt for Fable to do the architecture, give that to Fable to do the architecture, give it to Opus to do the coding, then Fable to do the PR review, and you should be — this is how I extracted as much possible value from each model.
[01:16:43] Ty Wells: You know, I'm on that train. I just don't like the back and forth too much because I've got to get a prompt. I mean, it's a little bit of work. I'm working on that because I just wanted to take what I have in the UI and push it into Fable. Actually, now that we're talking about this — I'm working on my CMUX. [tool:CMUX] I don't know if you guys are using CMUX. Patrick, I think you are.
[01:17:11] Patrick Chouinard: I'm back into Warp. [tool:Warp]
[01:17:16] Ty Wells: Are you? So yeah, I'm taking — there are some things that weren't working on CMUX. They're probably working on Warp. So I can probably save my time on that. But one thing is switching subscriptions. Have you done anything with that in CMUX?
[01:17:34] Patrick Chouinard: Not within the same provider.
[01:17:37] Ty Wells: I've switched provider a lot, but — okay. I'm going to give that one to Fable. Hey, I need to switch between my three accounts to optimize usage — switch when one's about to die. When I'm running low on one, switch to the other one, downgrade the model — because obviously I've got extra usage on — because if I'm in the middle of something, I want it to finish, but I want it to automatically switch, go to GPT-5.5 Pro, pull my PRD there, bring it into Fable, build a plan, switch to Opus, build the product, switch back to Fable, check the product, and then ship the product — sort of the pipeline.
[01:18:27] Paul Miller: <Q>Couldn't you do a CMUX skill that goes to OpenAI, does that prompting in OpenAI, pulls it across the other CMUX terminal?</Q>
[01:18:39] Ty Wells: <A>Yeah, that's what I started today. I forked CMUX so I can go ahead and make the changes, because it had problems with Google OAuth, it wouldn't work in the browser — I fixed that. I had problems with the microphone — I fixed that as well. So I'm just trying to work with all the issues that I work around, at least get them resolved with Fable and GPT-5.5.</A>
[01:19:09] Patrick Chouinard: On my end, I manage the flip between different providers through GitHub, actually. [tool:GitHub] I use them as if they were independent people. So basically, I build some — let's say I build the architecture from my architect — it will push the code, the specs, and then I will download it onto a second profile using Codex, for example, and we'll do either the code or the validation. Basically, I use them as individual people and I leverage what tools you already have to have a multi-team of developers.
[01:19:46] Ty Wells: That's interesting because yeah, what you can do — what I'm thinking is you just queue them up and you see something in there that says I'm ready to go in GitHub, pull it down in Fable, right? GPT puts it there, pull it down, Fable processes it. When it says it's done, the other one's polling it — go ahead and implement in Claude 4.8 or even Sonnet 5, I don't know — and then Fable back again when it's done.
[01:20:17] Patrick Chouinard: Exactly. And my QA is done by a swarm of Hermes agents. Because it's not the coding part — it's really: use the thing I just built and report whatever you find.
[01:20:34] Juan Torres: <Q>Wasn't there like an OpenRouter tool that coordinated the work between all of the models?</Q> [tool:OpenRouter]
[01:20:41] Patrick Chouinard: <A>No, the tool from OpenRouter is more of a "let's build Fable out of multiple models working together." It's not really individual models working separately. It amplifies the one model with the help of the others into an internal framework, and it spits out the improved answer. But it's not like you can do part of the work with one, then give it to the other one to do another part of the work. It's really a fusion model that gives out a better answer, but it's one question in, one answer out still.</A>
[01:21:31] Ty Wells: But you need a harness on top of the harnesses.
[01:21:35] Ty Wells: Did you look at Omigent? I think that's the name of it. O-M-I-G-E-N-T. [tool:Omigent]
[01:22:02] Ty Wells: It's like a harness between models. Take a look at it. Yeah, omnigent.ai. [link:omnigent.ai] Found the GitHub, I'll copy that in the chat.
[01:22:36] Ty Wells: Yeah, I looked at it. This was promising, but obviously it was an SOS call — Shiny Object Syndrome, for those that don't know. But I did spend a few hours working with it. It wasn't too bad, actually. I just didn't get back to it.
[01:22:56] Patrick Chouinard: But no, I haven't seen that one. So I think I'm going to have to investigate.
[01:23:03] Ty Wells: Well, it gives me something to do while I wait for my limit to reset. You queue it up for Fable to start looking at it.
[01:23:19] Juan Torres: You will have to go outside to the real world.
[01:23:22] Ty Wells: Can you explain the concept of what you just said?
[01:23:24] Ty Wells: It's a chat-based interface where it's basically using the models that you want to use at the time. You can sort of switch between models. I think it's in 127. It's like a harness between models.
[01:24:31] Ty Wells: Like I said, I actually brought it up and running for a couple of hours. I used it, but it was having some memory issues, so it crashed often. That's what I remember. It was crashing, but obviously that's solvable with Fable. I was running it locally. But then there were some issues with it, but I did like the concept.
[01:24:58] Ty Wells: This was a whole week ago, so — you know, this is ancient time. That's so long ago. I don't even have it running on my CMUX. So obviously can't be that important.
[01:25:08] Juan Torres: It was a desperate measure.
[01:25:11] Ty Wells: Well, no, somebody brought it to my attention. So I said I would look at it for them. And I did for a minute.
[01:25:22] Ty Wells: Okay, guys, I'm going to cut out and touch some grass. See you guys next week.
[01:25:28] Patrick Chouinard: Cool.
[01:25:29] Juan Torres: Thank you very much, everyone.
[01:25:31] Paul Miller: See you guys.

---

=== UNRESOLVED SPEAKERS ===

- **mdcatc** — raw name passed through unchanged; not resolved to a canonical full name via alias map. Referred to as "Morgan" once by Paul Miller at [00:19:16], suggesting the canonical name may be **Morgan** (last name unknown). Listed here as unresolved pending alias map confirmation.
- **Ryan C** — partial name; last name not provided in transcript. Passed through unchanged.
- **Juan Torres** — passed through unchanged; not confirmed in alias map context (alias map data was not populated in the SPEAKER_ALIASES block).

> Note: The `SPEAKER_ALIASES` context block resolved to the literal string `{{ $('HTTP Request: Get Speaker Aliases').item.json.data }}`, indicating the alias map was not injected at runtime. All speaker names have been passed through as-is from the source transcript. If a canonical alias map is available, re-processing is recommended.
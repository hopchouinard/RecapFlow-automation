## general

This was an informal coaching/community call that took place without the usual host (Brandon), who had rescheduled to the following day. Paul Miller stepped in to host. The group included Ty Wells, Jake Maymar, Rod Morrison, and Morgan Cook. The session was largely unstructured, covering a range of AI tooling topics including AI-powered trading experiments, Claude's memory and Skills features, Google AI Studio updates, browser-based AI agents, and vibe coding workflows.

A significant portion of the conversation focused on practical pain points: Jake raised a persistent problem with AI models failing to maintain consistent multi-level bullet/numbering structures in legal contracts, which led to a productive group problem-solving discussion. Ty shared progress on a security scanning app for repos, and Paul discussed using Google AI Studio to rapidly prototype a proof-of-concept email order analyzer for a client. The group also touched on the tradeoffs between Claude Code, Cursor, and Lovable for different stages of development.

The call ended with confirmation that the regular session with Brandon would happen the following day at the same time.

## insights

- **Paul Miller:** Using JSON or XML as an intermediate format when generating structured documents (like contracts) preserves hierarchy reliably, then convert to Markdown or DOCX as a final step — avoids the multi-level bullet inconsistency problem.
- **Rod Morrison:** Shared Python code demonstrating five-level deep nested list generation, providing a working solution to Jake's contract formatting problem.
- **Ty Wells:** Advocated a "five-minute rule" — if you can't solve a problem in five minutes, ask for help rather than spiraling down rabbit holes with conflicting AI outputs.
- **Paul Miller:** Google AI Studio's "Build" mode now lets you pre-select API integrations (Google Maps, Gemini, video analysis, etc.) that get loaded as best-practice scaffolding into vibe-coded apps — significantly accelerating proof-of-concept development.
- **Paul Miller:** Linking Google Stitch (UI/UX design tool) with AI Studio provides a Lovable-like design-to-code pipeline within the Google ecosystem.
- **Ty Wells:** AI models consistently struggle with logo/image handling — they attempt to convert PNGs to SVG and fail; the workaround is to remove the image background first and avoid letting the model recreate the image.
- **Paul Miller:** Rapid proof-of-concept demos built with vibe tools are an effective sales strategy — get client commitment in writing before building the full production version.
- **Ty Wells:** Claude Skills provides deterministic, step-by-step consistency in outputs but cannot access external data or perform tool calling — MCPs remain necessary for those use cases but carry data exposure risks as a "black box."
- **Morgan Cook:** Using SVG as source format for logos may help since it is text-based and the model can read rather than interpret it visually.
- **Jake Maymar:** When referencing multiple open-source projects in Claude Code, leakage between projects occurs — adding reference-only projects to `.gitignore` may resolve this.

## qa

**Q (Jake Maymar):** Has anyone been using the new memory feature in Claude — specifically Claude Desktop or Claude Code?
**A (Paul Miller):** Memory seems to appear in Projects but not in the base Claude interface. It's unclear whether project memory is scoped per project or shared globally, though per-project scoping would be most useful. Hard to tell yet if it's making a difference.

**Q (Paul Miller):** Has anyone tried the Claude Code browser function?
**A (Ty Wells):** Looked at it briefly — the main limitation is no preview capability, so you can't see your UI as you build. Gave it only a couple of minutes before moving on.

**Q (Paul Miller):** What's the verdict on AI browsers — OpenAI's vs. Perplexity vs. others?
**A (Jake Maymar/Ty Wells):** Perplexity (referred to as "Comet") is the current favorite. The OpenAI browser had issues with content restrictions — it blocked certain sites in ways a normal browser wouldn't, which was a dealbreaker.

**Q (Jake Maymar):** Has anyone successfully used AI to generate legal contracts with proper multi-level numbering/bullets?
**A (Paul Miller):** Use JSON or XML as the intermediate staging format — it enforces structural rules. Then convert to Markdown and finally to DOCX. This approach worked for a similar problem with restaurant menu scanning.

**Q (Paul Miller):** Are people using Claude Code exclusively now, or still combining with Cursor?
**A (Ty Wells):** Mostly Claude Code now. Still uses Lovable for quick UI/UX prototyping, then moves into Claude Code. Built a Telegram bridge to continue Claude Coding from mobile.

**Q (Paul Miller):** Are you pushing ShipKit rules and libraries into Claude Code projects?
**A (Ty Wells):** Not yet on new projects — existing projects were started in Cursor. Has adopted Brandon's AI document templates (with minor personal tweaks) for project planning.

## tools

- **Alpha Arena** — AI model trading competition platform; models given $10k to trade crypto, mentioned as "crypto gambling"
- **Claude Memory (Claude Desktop)** — New memory feature in Claude; discussed whether it scopes per project or globally
- **Claude Code** — Primary coding agent used by most participants; discussed for vibe coding, refs, and CLI-based workflows
- **Claude Skills** — New Claude feature for deterministic, step-by-step task execution; Ty Wells actively integrating it
- **Cursor** — IDE/coding agent; discussed as comparison point to Claude Code, noted as better at handling `@refs`
- **Lovable** — Vibe coding tool; still used by Ty Wells for rapid UI/UX prototyping before switching to Claude Code
- **Google AI Studio (Build mode)** — Vibe coding platform with pre-loadable API integrations; Paul Miller demoing and using heavily
- **Google Stitch** — Google's UI/UX AI design tool; recently linked to AI Studio for design-to-code workflow
- **Gemini CLI** — Google's CLI coding agent; Rod Morrison noted it spirals/loops and burns tokens before requiring API key
- **Gemini 2.5 Pro** — Google's flagship model; mentioned in context of Gemini CLI spiraling behavior
- **Deep Seek** — Chinese AI model; leading in the Alpha Arena trading competition
- **ChatGPT** — Used by Rod Morrison to fix logo background issue; redirected him to a background-removal site
- **Perplexity (Comet browser)** — Jake Maymar's preferred AI browser for certain tasks
- **Strawberry Browser** — AI browser Ty Wells had been on a waitlist for since Feb/March; recently received access and tested
- **ShipKit** — Brandon's starter kit; Rod Morrison purchased it and uses it with Claude Code
- **MongoDB** — Paul Miller used it as a JSON document store for restaurant menu scanning project
- **Discord** — Community platform; discussed as too noisy/interruptive for async help-seeking
- **Skool** — Community platform where Brandon posted the meeting reschedule notice
- **Telegram** — Ty Wells built a bridge to Claude Code for mobile coding sessions
- **Google Maps / Places API** — Available as a pre-loadable integration in Google AI Studio Build mode
- **Nano Banana (Imagen)** — Google's image generation model; referenced as a reason to use Google AI Studio

## links

- **Alpha Arena** — Link shared by Jake Maymar in chat; AI model trading competition site (URL not captured in transcript)
- **Rod Morrison's Google AI Studio demo** — Link shared in chat showing a data ingestion/cleansing/GCS pipeline presentation built in AI Studio
- **Rod Morrison's Python code** — Shared in chat; Python solution for generating five-level deep nested list/contract structure

## decisions

- **Jake Maymar** will try using JSON as an intermediate format for contract generation, then convert to Markdown, based on Paul Miller's suggestion.
- **Jake Maymar** will investigate adding reference-only open-source projects to `.gitignore` in Claude Code to prevent leakage between projects.
- **Ty Wells** will send Jake Maymar a sample contract/document to experiment with for the multi-level formatting problem.
- **Ty Wells** will share a link to his security repo scanning app with the community once it is finished (expected within a couple of days).
- **Ty Wells** will share details of his Claude Skills integration project with the group next week when it is complete.
- **Group** will reconvene at the same time the following day for the regular session with Brandon.
## Meeting Purpose

[Discussing AI development tools, workflows, and problem-solving strategies.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=367.0)

## Key Takeaways

  - [**Google AI Studio is a powerful PoC tool.** Its new "additional functionality" cards (e.g., Maps, Video) enable rapid PoC creation, like building a structured order generator from free-text emails in 15 minutes.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=1114.0)
  - [**Use JSON as an intermediate format for complex structures.** This solves LLM failures with nested lists (e.g., legal contracts) by enforcing a rigid, machine-readable schema before converting to a human-readable format like Markdown or DOCX.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2358.0)
  - [**Adopt a "five-minute rule" to avoid rabbit holes.** If a problem isn't solved in five minutes, ask for help in the Skool community to accelerate progress and prevent wasted time.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=3138.0)
  - [**Claude Code is the preferred dev environment.** It's more stable than Cursor, especially for mobile CLI use via a Telegram bridge, and integrates well with ShipKit.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2865.0)

## Topics

### AI Tooling & Browser Landscape

  - [**Claude:**](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=789.0)
      - [**Memory:** A new feature with unclear scope (global vs. project-specific).](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=789.0)
      - [**Code Browser:** A CLI-like environment lacking a UI preview, limiting its utility for front-end work.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=881.0)
  - [**AI Browsers:**](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=988.0)
      - [**Perplexity:** The current group favorite for general research.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=988.0)
      - [**Strawberry Browser:** A new tool that completes tasks but is slow.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=933.0)
      - [**OpenAI Browser:** Perceived as a flop, with restrictive policies that limit access to certain websites.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=988.0)

### Google AI Studio: A PoC Powerhouse

  - [**New "Additional Functionality" Cards:** Allow preloading APIs (Maps, Video, Places) into a Vibe session, enabling rapid PoC creation.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=1174.0)
      - [**Example:** Paul built a system to generate structured JSON orders from free-text emails in 15 minutes.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=1335.0)
  - [**Integration with Stitch:** Google's UI/UX AI tool can now feed its designs directly into AI Studio to guide code generation.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=1814.0)
  - [**Accessing Credits:** Rod secured $2k in Google Cloud credits via the Google Startup School.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=1596.0)

### Solving LLM Formatting Failures

  - [**Problem:** LLMs consistently fail to generate correctly nested lists in formats like Markdown or DOCX, which is critical for structured documents like legal contracts.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2072.0)
  - [**Solution:** Use JSON as an intermediate format.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2358.0)
      - [**Rationale:** JSON's rigid, machine-readable structure forces the LLM to follow the hierarchy correctly.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2358.0)
      - [**Workflow:** Prompt for JSON → Convert JSON to Markdown/DOCX.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2358.0)
  - [**Validation:** Rod provided Python code in the chat that successfully generated a 5-level nested list, confirming the approach.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2718.0)

### Development Workflow & Community Support

  - [**Claude Code vs. Cursor:**](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2865.0)
      - [**Preference:** Claude Code is preferred for its stability, especially for mobile CLI use via a Telegram bridge.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2865.0)
      - [**Reference Projects:** To prevent Claude Code from "leaking" into unintended files, place reference projects in `.gitignore`.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=3016.0)
  - [**Community Support:**](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=3115.0)
      - [**"Five-Minute Rule":** Ask for help in Skool after five minutes of being stuck to avoid wasting time.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=3138.0)
      - [**Discord:** Considered too interruptive and difficult to follow for deep problem-solving.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=3199.0)

## Next Steps

  - [**Jake:** Test the JSON-to-Markdown workflow for legal contracts.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2478.0)
  - [**Ty:** Share the security app with the community upon completion.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=2777.0)
  - [**All:** Attend tomorrow's rescheduled meeting.](https://fathom.video/share/Ckyed68UfjsQcsTPmZrJ1eniCRPRi3xa?tab=summary&timestamp=3405.0)


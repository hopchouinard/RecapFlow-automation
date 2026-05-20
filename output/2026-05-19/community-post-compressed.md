📝 SUMMARY

This week's coaching call focused on career transitions into AI engineering for domain experts, with guidance for statisticians and DevOps professionals on leveraging existing expertise. Participants showcased projects including a golf swing analysis wearable, cybersecurity MCP tool for vulnerability detection, and serverless AI photo booth architecture. The session covered adversarial AI workflows, prompt injection security risks, and strategies for managing non-technical collaborators.

💡 KEY INSIGHTS

Domain expertise is your strongest asset when transitioning to AI engineering. The ability to validate AI-generated output in your specific field is rarer and more valuable than generic software engineering skills.

Build first projects in areas you understand deeply. A statistician should build an A/B testing tool rather than generic SaaS, ensuring you can verify the AI's work.

Adversarial code review requires model separation. Use Claude for architecture and initial coding, then switch to GPT or Codex for review in a separate conversation to avoid bias and context pollution.

Agentic DevOps is an underserved niche. While everyone focuses on agentic coding, few address infrastructure automation—yet Claude Code and Codex handle Terraform, Ansible, and AWS CLI tasks exceptionally well.

Prompt injection poses real security risks in shared natural language artifacts. Malicious instructions can hide in Base64-encoded strings within skills or prompts, with no commercial antivirus currently available for this threat vector.

For non-technical teams, GitHub Organizations with fork-based workflows provide isolation. Contributors work in their own forks where mistakes cannot break the main project, while still allowing merges through standard pull requests.

❓ KEY Q&A

Q: I have 20 years as a statistician. AI engineering roles look like software engineering jobs. How do I transition?

A: Your ability to evaluate AI output in your domain is the critical skill. Build projects in statistics or data science that you can validate, learn basic architectural concepts through practice, and use tools like Superpower to guide you through the full SDLC. You become a manager of virtual agents rather than a manual coder.

Q: How do I get two AI systems to review each other's work without sharing context?

A: Open both in the same repository. Give Codex the Git diff or commit list and ask for a savage adversarial review. Save that report as a file, then provide that file to Claude with the context that "Codex found these issues." The code serves as the shared source while conversation histories remain separate.

Q: My non-technical team does not use GitHub. How do I manage version control safely?

A: Create a GitHub organization and have team members fork the repository. Place an instruction file at the root explaining how to update their fork. Their changes stay isolated, preventing breakage of the main project. Alternatively, Codex's web interface can automate branch creation and pull requests with you as the code owner.

Q: Is there a security risk in copying skills from external sources?

A: Yes. Prompt injection attacks can embed malicious instructions in natural language artifacts using Base64 encoding or subtle text patterns that humans miss but AI systems execute. Treat shared skills with the same caution as executable code until a verification ecosystem emerges.

🛠️ TOOLS AND CONCEPTS MENTIONED

AI Coding Harnesses: Claude Code serves as the primary development environment, with Codex used for adversarial review due to its generous $20 monthly limits and precise plan-following capabilities. The Superpower plugin guides users through the complete software development lifecycle.

Infrastructure and DevOps: Terraform, AWS CloudFront, EC2, and S3 form the backbone of serverless architectures, with the Google Cloud Platform CLI noted for infrastructure automation. Claude Code handles infrastructure-as-code tasks effectively, though human validation of security and best practices remains essential.

Security Tools: ShipSafe is a cybersecurity MCP tool that checks code for vulnerabilities at generation time. Stripe webhook integrations are the most common failure point in payment processing implementations.

Project Showcases: SwingTrack combines gyroscopic wristbands and camera-enabled caps for golf swing analysis. ConchPass provides vendor vetting for cruise passengers. An AI Photo Booth uses AWS CloudFront for media egress decoupled from compute.

Automation and Integration: Google Apps Script powers foundation workflows, while Looker Studio provides dashboard layers over spreadsheet data. N8N and Zapier offer agentic orchestration capabilities.

Hardware: Mentra Glass offers YC-backed smart glasses with an open SDK, suggested as a potential camera source for wearable AI projects.

📎 SHARED RESOURCES

ShipSafe cybersecurity MCP tool: https://shipsafe.franklabs.io/

SwingTrack golf analysis app: https://swingtrack-nu.vercel.app/

ConchPass vendor vetting platform: https://conchpass.com/

Anthropic's official Claude Code training: https://anthropic.skilljar.com/claude-code-in-action

Google Workspace CLI for AI harnesses: https://github.com/googleworkspace/cli

Mentra Glass open SDK smart glasses: https://www.ycombinator.com/companies/mentra

Wavespeed multi-model API platform: https://wavespeed.ai/dashboard

Google Looker Studio (free): https://lookerstudio.google.com/

Text-to-image model leaderboard: https://arena.ai/leaderboard/text-to-image/pareto

Theo on markdown-to-HTML tooling: https://www.youtube.com/watch?v=S9EGx6ik-18&t=1924s

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick will develop an adversarial code review skill demonstration using the "cake method"—showing the finished result first, then table-walking the construction process—for an upcoming training session.

Ty is meeting with hardware design partners to advance the physical SwingTrack device and exploring Mentra open SDK smart glasses as a camera source. Community members interested in ShipSafe can email Ty for free access to the cybersecurity school community.

Juan is investigating porting the AI Photo Booth to a native iPhone app following interest from the group.

Mitch will present an AI-assisted Amazon data analysis workflow to his team using the GitHub org and fork strategy discussed for safe collaboration with non-technical contributors.

Brandon Hancock will host next week's call and plans to share updated workflows and lessons learned.
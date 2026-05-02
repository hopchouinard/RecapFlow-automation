The 5 query types — sample questions tailored to your corpus                                                                                                                                            

For each: I give you the question, what success looks like in the answer, and what raw /query data should support it.                                                                                   

1. Evolution over time                                                                                                                                                                             
Question: "How has the group's perspective on AI coding tools evolved from early 2025 to today?"

Success: Answer references both the Feb 2025 conversations (DeepSeek R1 vs O3 Mini debate, Cursor/Windsurf as IDEs) AND the April 2026 conversations (Claude Code, Anthropic-Microsoft partnership,       
current toolchain). Inference layer articulates the trajectory ("they moved from X to Y"), not just two disconnected snapshots.

Failure mode: Answer pulls only from one phase, or fakes a synthesis that the chunks don't support.

2. Relationships between ideas                                                                                                                                                                            

  Question: "What's the connection between content creation strategy and AI consultancy sales funnels?"
  Success: Answer surfaces Brandon's recurring thesis across multiple Feb sessions — that LinkedIn/YouTube content IS the sales funnel for early-stage AI consultancies, with the discovery call as the only conversion step. Should reference at least 2 distinct sessions weaving these together.

  Failure mode: Answer treats the topics independently or invents a connection not in the chunks.

3. Contradictions / disagreements                                                                                                                                                                    
  Question: "Were there differing opinions about how to price AI services to clients?"

  Success: Answer surfaces the Alexandra/Brandon discussion on revenue share vs license fees, possibly Mike's input on pricing for ICP, etc. Should show ≥2 chunks with different stance on the same topic.

  Failure mode: Answer asserts everyone agreed (false), or invents disagreement (worse).

  Note: With only 8 sessions, this is the weakest query type — disagreements are usually intra-session, not cross-session. May need to lower expectations here.

4. Outcomes or impacts
  Question: "What did Adam (Gold Flamingo Solutions) commit to in early February, and what came of it?"

  Success: Answer references 2025-02-05's decisions (post LinkedIn content this week, abandon Udemy course, target law firms) AND any follow-up in 2025-02-09 / 02-12 (did he report back? did the funnel get traction?). Should pull chunks with non-null decisions followed by chunks with references_prior: true or matching topic_label.

  Failure mode: Answer only quotes the original commitment with no follow-up arc.

5. Missing / unresolved questions

  Question: "What questions came up across these calls that didn't get fully answered?"

  Success: Answer lists genuinely unresolved questions, drawing from chunks with has_unresolved_question=true (your corpus has many: 11 in 2025-02-05, 8 in 2025-02-09, etc.). Should NOT include questions that DID get answered.
  Failure mode: Answer fabricates "open questions" that were actually resolved on the call.

---

I'm continuing the Community Brain project. Plan A, Plan B, and Hybrid Retrieval v2 are all complete and deployed (retrieval server 0.2.0 live on the VM, validated 2026-04-28; addendum in Plan A spec §10). Findings 6 and 7 from the original Phase 6 catalog are empirically resolved: entity-grounded retrieval went from 0/10 → 6/10 hits, metadata-tagged retrieval from 1/10 → 6/10 hits. The work for this session: design Retrieval v3.
Read in this order before brainstorming:
1. docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md (handoff document; the "v3 design (when warranted)" subsection summarizes Finding 8 and the three concrete fix paths)
2. docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md — find the "v2 hybrid retrieval validation (2026-04-28 — against live VM)" subsection in §10. That addendum captures F6/F7 empirical outcomes, Finding 8's full description, and the v3 candidate fix paths it surfaced.             
3. docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md §12 "Future work (v3 candidates)" — secondary candidates beyond Finding 8 (LLM intent classifier, cross- encoder reranker, weighted-sum fusion, synthesized BM25 field, cue rules in YAML,response).
4. community-brain/CLAUDE.md "Known v2 backlog" + "Trade-offs we've deliberately kept" sections — context for what v3 must NOT break. 
 
Leading v3 candidate is Finding 8: the answering LLM under-utilizes Stage C metadata flags (e.g. has_unresolved_question=True) because the trust contract in docs/inference-guidelines.md correctly tells it to re-derive from text. Pre-v2 this was invisible (retrieval was the bottleneck); v2 fixed retrieval and surfaced this as the next
constraint. Three concrete fix paths captured in the spec addendum:
(a) Tighten inference-guidelines.md so strong flags are authoritative even when textual cues are subtle
(b) Format chunks with metadata flags inline in the LLM prompt (filter-side change to community_brain_filter.py)
(c) Add a metadata_summary field to /query responses giving authoritative per-flag counts 

Out of scope for this v3 (likely; confirm during brainstorming): ingestion-side Stage C improvements (entities-field underpopulation,
speakers_mentioned never set — both in community-brain/CLAUDE.md "Known v2 backlog"). These are real but separate concerns; tackle
as a parallel ingestion-side initiative if you want, but don't bundle them into v3 retrieval work without explicit scoping.

Use superpowers:brainstorming to explore the design space (which of the candidates to bundle into v3, what the right scope is, whether 
the trust partition itself needs revision, whether ingestion-side work should ride along). Don't pre-decide. Then write a spec via
superpowers:writing-plans → an implementation plan. Ship via superpowers:subagent-driven-development.

Constraints:
- Don't break the existing /query request/response contract. Open WebUI filter and n8n workflows must continue to work. Same clean-break stance as v2 — no `mode` parameter, no parallel endpoint, no backwards-compat shims for a single-operator deployment.
- Preserve the trust partition (ground_truth / derived_metadata / provenance) at the structural level. v3 may revise HOW derived_metadata is presented to the answering LLM (Finding 8 fix path (b) does exactly this), but the partitioning is non-negotiable.
- Plan C backfill (~57 sessions) is held until v3 ships, so design with the knowledge that the corpus will grow ~7× shortly after
  deploy. RRF score calibration assumptions may need re-checking at that scale.
- Solo operator, no real users. Same operational reality as v2. Track B (Plan C full backfill) is held until v3 lands and you've decided what the final extraction_prompt_version is. Don't kick off the backfill mid-design. 

A few things baked in deliberately:

- Doesn't pre-decide v3's scope. Finding 8 is the lead candidate, but brainstorming should pressure-test whether (a/b/c) is actually three separate options or one composite, and whether ingestion-side work should ride along or stay separate.
- Calls out the Plan C constraint. v3 needs to be designed knowing the corpus will grow ~7× shortly after deploy — RRF Δ calibration assumptions may need re-checking at that scale. Worth surfacing during the design phase, not after.
- Explicit "trust partition is structural; presentation can change." Fix path (b) (inline flags in the LLM prompt) does exactly that — revises presentation while preserving the structural contract.

That's the seam future-you should be aware of. 
- Reaffirms "no backwards-compat shims" stance. Solo operator; same ship-clean discipline that v2 used. Saves a re-litigation conversation.

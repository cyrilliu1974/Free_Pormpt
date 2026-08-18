# Defense Memorandum Generator for Litigation

## 簡介

The Defense Memorandum Generator for Litigation is a free AI prompt that produces comprehensive defense strategy memorandums for trial attorneys handling civil and criminal cases. This defense memorandum prompt for ChatGPT walks you through systematic phases that deconstruct the plaintiff's theory, identify jurisdictional defects, map affirmative defenses to available evidence, and deliver actionable recommendations across nine litigation phases - from knockout immunity doctrines and statute of limitations bars to liability-limiting comparative fault theories and settlement leverage analysis. It runs on ChatGPT, Claude, Gemini, and Grok, adapting its depth to case complexity: simple single-claim matters receive focused analysis of the strongest defenses, while multi-party federal litigation or catastrophic exposure cases receive full exploration of procedural defects, statutory gaps, discovery priorities, motion practice roadmaps, and sample pleading language. Reach for this prompt when you need to build a defense strategy memorandum that ties legal standards to case facts, rates defense viability, and prioritizes action items for case strategy meetings. ● Analyzes Tier 1 knockout defenses (immunity, statute of limitations, jurisdictional defects, standing) with viability ratings and strategic risk assessments. ● Maps Tier 2 and Tier 3 defenses (comparative fault, failure to mitigate, laches, estoppel) to evidentiary requirements and discovery targets. ● Produces sample affirmative defense paragraphs for answers, motion practice roadmaps for early dispositive relief, and evidence-to-defense mapping tables. ● Delivers a nine-phase executive summary with the three strongest defenses, immediate action items, resource requirements, and go-forward strategy for client meetings. ## Prompt

```
## Role

You are an experienced trial attorney specializing in affirmative defenses across civil and criminal cases. You identify procedural defects, statutory gaps, and creative defense strategies that shift litigation outcomes.

## Task

Generate a comprehensive memorandum analyzing potential affirmative defenses tailored to the case facts, jurisdiction, and claims provided. Work through systematic phases that deconstruct the plaintiff's theory, identify jurisdictional nuances, map defenses to evidence, and deliver actionable strategic recommendations.

## Context

Provide the following case information:

**{{case-facts}}**  
(Include: causes of action; jurisdiction (federal/state, circuit/state); summary of alleged events; client's version; procedural history; relevant dates (incident, filing); involved parties; contractual relationships; available evidence and witnesses)

**{{client-goals}}**  
(Describe: desired outcome; risk tolerance; settlement vs. trial preference; resource constraints; timeline urgency)

## Methodology

Work through phases appropriate to case complexity:

### Phase 1: Case Assessment
Analyze the plaintiff's liability theory, identify vulnerabilities, and map defensive categories. Deliver a 2-3 paragraph strategic assessment.

### Phase 2: Tier 1 Knockout Defenses
Examine complete bars to liability: statute of limitations, immunity doctrines, jurisdictional defects, standing, failure to state a claim. For each viable defense provide:
- Legal standard
- Required factual predicates
- Viability rating (HIGH/MEDIUM/LOW)
- Strategic advantages and risks

### Phase 3: Tier 2 Liability-Limiting Defenses
Analyze exposure-reducing defenses: comparative fault, assumption of risk, failure to mitigate, superseding cause, damages limitations. Structure each with evidentiary requirements and tactical considerations.

### Phase 4: Tier 3 Procedural & Alternative Theories
Evaluate leverage-creating defenses: laches, estoppel, waiver, res judicata, procedural defects. Focus on settlement leverage and procedural advantages.

### Phase 5: Evidence & Discovery Strategy
Map defenses to proof. Identify:
- Evidence gaps by defense
- Discovery priorities
- Document/deposition targets
- Expert witness needs

### Phase 6: Pleading Strategy
Draft sample affirmative defense paragraphs for the answer, including catchall preservation language and alternative theory considerations.

### Phase 7: Motion Practice Roadmap
Identify defenses supporting early dispositive relief (12(b)(6), summary judgment). Recommend motion timing and judicial efficiency arguments.

### Phase 8: Settlement Leverage Analysis
Assess which defenses most impact plaintiff's risk calculus. Outline negotiation pressure points and timing considerations.

### Phase 9: Executive Summary
Synthesize analysis into client-ready recommendations:
- Three strongest defenses with rationale
- Immediate action items
- Resource requirements
- Go-forward strategy

**Adapt phase depth to case complexity:** Simple single-claim cases warrant compressed analysis (phases 1-2-5-9); multi-party federal litigation or catastrophic exposure cases justify full exploration of all nine phases.

## Output

Deliver a structured litigation memorandum with:
- Clear headings for each phase
- Legal standards integrated naturally (no citation lists)
- Viability ratings and risk assessments
- Evidence-to-defense mapping tables where helpful
- Sample pleading language for top defenses
- Prioritized action plan

Format for immediate use in case strategy meetings and pleading preparation.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-facts}}、{{client-goals}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Defense Memorandum Generator for Litigation is a free AI prompt that produces comprehensive defense strate…

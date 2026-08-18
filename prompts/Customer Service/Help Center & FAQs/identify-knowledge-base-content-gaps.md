# Knowledge Base Gap Analysis Prompt

## 簡介

The Knowledge Base Gap Analysis Prompt is a free AI prompt that maps support ticket patterns against existing help center articles to identify documentation gaps for customer success and support teams. This knowledge base gap analysis prompt for ChatGPT performs a three-pass forensic review: it finds topics with high ticket volume but zero documentation (direct gaps), flags existing articles that still generate support requests (thin coverage), and extrapolates logically connected topics users will need (adjacent gaps). The prompt runs on ChatGPT, Claude, Gemini, and Grok, and delivers a structured report with up to 25 prioritized recommendations, each tagged by gap type and estimated ticket deflection impact. Support managers use it to shift resources from reactive ticket handling to proactive content creation, while technical writers gain a data-driven content calendar that targets real user pain points instead of assumptions. Reach for this prompt when your team wants to reduce repeat tickets, prioritize help center updates, or justify content investments with evidence tied to actual support volume. ● Maps ticket categories against article titles to reveal which missing topics cost the most support hours. ● Flags existing articles that still generate high ticket volume, signaling insufficient depth or unclear instructions. ● Extrapolates adjacent topics users will need next, preventing downstream support requests before they arrive. ● Ranks every gap by estimated deflection potential and caps output at 25 recommendations to force strategic focus. ## Prompt

```
## Role

You are a knowledge base gap analyst specializing in ticket deflection. You cross-reference support ticket patterns against documentation coverage to identify which missing or insufficient articles would save the most support hours.

## Task

Perform a three-pass gap analysis:

1. **Direct Gaps** – Compare ticket categories against existing article titles to find topics with high ticket volume but zero documentation
2. **Thin Coverage** – Identify existing articles whose topics still generate significant ticket volume, indicating insufficient depth or clarity
3. **Adjacent Gaps** – Extrapolate logically connected topics that would prevent downstream issues, based on patterns in high-volume tickets

Rank all gaps by estimated ticket deflection potential and group into High/Medium/Low priority tiers. Cap the final output at 25 recommendations maximum.

## Context

**Existing KB articles:**
{{kb-article-titles}}

**Top support ticket categories or FAQs:**
{{ticket-categories}}

**Product/service:**
{{product-description}}

## Requirements

- **Volume over variety** – Prioritize topics generating the most tickets
- **Exclude edge cases** – Omit issues affecting fewer than 1% of users
- **Exclude non-documentable issues** – Omit problems requiring physical intervention, hardware repair, or human-only resolution
- **Avoid duplication** – Do not recommend articles that duplicate existing content under different titles
- **Estimate impact** – Each recommendation must include a tactical rationale explaining ticket deflection potential
- **Maintain focus** – Cap at 25 recommendations to force prioritization

## Output

Deliver a structured report:

**PASS 1: DIRECT GAPS**  
[Narrative explanation of methodology and findings]

**PASS 2: THIN COVERAGE**  
[Narrative explanation of methodology and findings]

**PASS 3: ADJACENT GAPS**  
[Narrative explanation of methodology and findings]

**PRIORITIZED RECOMMENDATIONS**

**HIGH PRIORITY:**  
1. [Proposed Article Title] – Gap Type: [Direct/Thin/Adjacent] | Rationale: [One-sentence explanation of ticket deflection potential]  
2. [Continue...]

**MEDIUM PRIORITY:**  
[Continue same format...]

**LOW PRIORITY:**  
[Continue same format...]

Each recommendation must include: Proposed Article Title, Gap Type classification, Priority tier, and tactical rationale. Group all recommendations by priority tier.
```

## 用法 / Usage
- 必填變數 / Variables: {{kb-article-titles}}、{{product-description}}、{{ticket-categories}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Knowledge Base Gap Analysis Prompt is a free AI prompt that maps support ticket patterns against existing …

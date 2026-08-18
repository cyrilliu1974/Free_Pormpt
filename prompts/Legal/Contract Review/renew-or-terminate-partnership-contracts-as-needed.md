# Partnership Contract Renewal & Termination Evaluator

## 簡介

The Partnership Contract Renewal & Termination Evaluator is a free AI prompt that produces detailed contract assessment reports for businesses reviewing vendor and partner agreements. This partnership contract evaluation prompt for ChatGPT works by analyzing each agreement against your custom evaluation criteria and performance metrics, then generating an executive summary, individual contract assessments with revenue contribution analysis, strategic alignment scoring, and prioritized recommendations with financial impact projections. It runs on ChatGPT, Claude, Gemini, and Grok, accepting two inputs: the partnership contracts you need to review and the evaluation criteria specific to your business objectives. Legal teams, procurement managers, and business operations professionals use it to structure quarterly contract reviews, prepare board-level partnership reports, and support negotiation decisions with quantitative rationale. ● Structures reviews around performance against KPIs, revenue contribution, and alignment with company objectives rather than subjective impressions ● Produces executive summaries, per-contract assessments with clear renew/terminate/renegotiate verdicts, and risk-weighted action plans ● Outputs formatted reports with headings and bullet points designed for stakeholder presentation and quick reference ● Supports data-driven negotiation and budget allocation by quantifying the expected financial impact of each recommendation ## Prompt

```
## Role
You are an expert contract analyst evaluating partnership agreements.

## Task
Assess current contracts and provide recommendations for renewal or termination in a comprehensive report format.

## Context
Review each contract focusing on key performance indicators and alignment with company objectives. Analyze partnership effectiveness based on metrics and strategic fit. Develop clear, data-supported rationales for each recommendation.

**Contracts to evaluate:**
{{partnership-contracts}}

**Evaluation criteria:**
{{evaluation-criteria}}

## Output
Prepare a detailed report that includes:

### Executive Summary
- Overview of contracts reviewed
- High-level recommendations

### Individual Contract Analysis
For each partnership:
- Partner name and contract term
- Performance against key metrics
- Revenue contribution
- Strategic alignment assessment
- Recommendation (renew/terminate/renegotiate)
- Supporting rationale with data
- Impact on company goals and bottom line

### Recommendations Summary
- Prioritized action items
- Risk assessment
- Expected financial impact

Use clear headings, subheadings, and bullet points for readability and quick reference.
```

## 用法 / Usage
- 必填變數 / Variables: {{evaluation-criteria}}、{{partnership-contracts}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Partnership Contract Renewal & Termination Evaluator is a free AI prompt that produces detailed contract a…

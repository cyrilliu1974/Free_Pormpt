# Grant Proposal Review Criteria Prompt

## 簡介

The Grant Proposal Review Criteria Prompt is a free AI prompt that systematically evaluates grant applications against funding objectives and eligibility requirements for reviewers and grant-making organizations. This grant review prompt for ChatGPT guides the model to act as an expert grant proposal reviewer, analyzing submissions through a structured assessment framework and delivering results in customizable markdown tables. You define the grant type (research, nonprofit, small business, innovation), the business type being evaluated, and the exact column structure for your assessment matrix - the AI then reviews proposals for strengths, weaknesses, alignment with funding goals, and compliance with eligibility factors. It runs on ChatGPT, Claude, and Gemini, producing evidence-based evaluations that mirror professional grant review panels. Reach for this prompt when you need consistent, transparent scoring frameworks across multiple applications or want to ensure every proposal receives the same rigorous criteria-based analysis. ● Produces markdown table assessments with flexible column counts and custom evaluation criteria headers ● Evaluates alignment between proposals and funding objectives, eligibility requirements, and grant-specific criteria ● Reviews both strengths and weaknesses with evidence-based analysis rather than subjective impressions ● Adapts to any grant type (federal, foundation, corporate, research, community) and any business or organization type ## Prompt

```
## Role
You are an expert grant proposal reviewer conducting systematic evaluation of grant applications.

## Task
Analyze the submitted grant proposal against established criteria and deliver a structured assessment in table format. Review the grant requirements and eligibility factors, then evaluate the proposal's strengths, weaknesses, and alignment with funding objectives.

## Context
Grant type: {{grant-type}}
Business type: {{business-type}}

## Output
Provide your assessment as a markdown table with {{column-count}} columns using these headers: {{column-names}}

Ensure the evaluation is comprehensive, evidence-based, and addresses all key criteria relevant to the grant type and applicant business.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-type}}、{{column-count}}、{{column-names}}、{{grant-type}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Grant Proposal Review Criteria Prompt is a free AI prompt that systematically evaluates grant applications…

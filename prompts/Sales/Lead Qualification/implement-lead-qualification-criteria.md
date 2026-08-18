# Lead Qualification Criteria Framework Builder

## 簡介

The Lead Qualification Criteria Framework Builder is a free AI prompt that creates custom, weighted lead scoring systems for sales and marketing teams. This lead qualification prompt for ChatGPT produces a structured markdown table listing 6-10 industry-specific criteria - such as target profile fit, budget alignment, timeline feasibility, decision-making authority, pain-point alignment, and buyer readiness - complete with clear descriptions and numerical weights that sum to 100%. You supply five variables (industry, target customer profile, budget range, project timeline, and business goals), and the prompt returns a ready-to-use scoring framework that reflects both qualification signals and disqualification red flags. It runs on ChatGPT, Claude, Gemini, and Grok, delivering consistent results across text-generation models. Reach for this prompt when you need to standardize lead evaluation, train a sales team on prioritization, or build a scoring model for your CRM. ● Outputs a markdown table with criteria name, description, and numerical weight for easy import into CRM or sales playbooks. ● Covers qualification dimensions - fit, need, authority, timeline - and disqualification signals in a single framework. ● Adjusts criteria weighting to reflect your specific budget range, customer profile, and business goals. ● Saves hours of manual framework design by synthesizing best practices into a context-aware scoring model. ## Prompt

```
## Role
You are an expert lead qualification specialist.

## Task
Develop a comprehensive set of weighted criteria for qualifying sales leads, tailored to the provided industry and customer context.

## Context
Industry: {{industry}}
Target customer profile: {{target-customer-profile}}
Budget range: {{budget-range}}
Project timeline: {{timeline}}
Business goals: {{business-goals}}

Analyze these inputs to understand what makes a lead viable. Consider factors such as fit with the target profile, budget alignment, timeline feasibility, decision-making authority, pain points addressed by your solution, and readiness to buy.

## Output
Provide a markdown table with three columns:

| Criteria | Description | Weight |
|----------|-------------|--------|

- **Criteria**: 6-10 distinct qualification factors that evaluate lead quality
- **Description**: Clear explanation of what each criterion measures and why it matters
- **Weight**: Numerical importance (percentage or 1-10 scale; all weights should sum to 100% or a consistent total)

Ensure criteria are specific to the industry, aligned with the customer profile, and reflect the budget and timeline constraints. Cover both qualification (fit, need, authority) and disqualification signals.
```

## 用法 / Usage
- 必填變數 / Variables: {{budget-range}}、{{business-goals}}、{{industry}}、{{target-customer-profile}}、{{timeline}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Lead Qualification Criteria Framework Builder is a free AI prompt that creates custom, weighted lead scori…

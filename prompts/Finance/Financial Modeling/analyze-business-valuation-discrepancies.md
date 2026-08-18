# Business Valuation Analysis Prompt

## 簡介

The Business Valuation Analysis Prompt is a free AI prompt that applies multiple valuation methodologies to produce defensible business value ranges for owners facing acquisitions, investor negotiations, or strategic decisions. This business valuation prompt for ChatGPT works by triangulating value through at least three established methodologies: earnings multiples, discounted cash flow, and asset-based approaches. It processes your financial metrics and valuation purpose to generate side-by-side calculations, highlight methodology-specific pros and cons, and produce a consolidated valuation range with low, mid, and high estimates accompanied by confidence levels. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across text-generation platforms. Real use cases include preparing for acquisition offers, responding to investor term sheets, evaluating partnership buyouts, and grounding internal strategic planning in market reality. Reach for this prompt when you need to reconcile conflicting third-party estimates, justify a valuation to stakeholders, or make time-sensitive decisions without access to expensive advisory services. ● Applies three or more valuation methodologies with step-by-step calculations and resulting ranges for each method. ● Identifies key value drivers and quantifies how factors like revenue growth, margin improvement, or customer concentration could shift the estimate. ● Highlights risk factors with estimated impact, including limited financial history, market volatility, and industry-specific challenges. ● Delivers a consolidated valuation range with confidence levels and a recommended negotiation range tailored to your stated purpose. ## Prompt

```
## Role
You are an experienced valuation analyst who applies multiple methodologies to derive practical business valuations. You triangulate value using industry comparables, financial fundamentals, and market conditions to produce defensible ranges for negotiations and strategic decisions.

## Task
Provide a comprehensive business valuation using at least three established methodologies (earnings multiples, discounted cash flow, asset-based approaches). For each method, show calculations, explain applicability to the business stage and industry, and highlight assumptions and limitations. Present a consolidated valuation range with confidence levels and identify the key drivers and risks that could materially shift the estimate.

## Context
The business owner needs a reliable valuation for {{valuation-purpose}} and faces conflicting estimates or time-sensitive decisions. Standard models may not fit their reality due to limited financial history, volatile conditions, or industry-specific factors. The valuation must be grounded in their actual financials and current market conditions.

## Input
{{financial-metrics}}

## Output
Structure your analysis using these sections:

**Financial Summary**
- Bullet points of key metrics provided

**Valuation Method 1: [Method Name]**
- Calculation with specific steps
- Resulting valuation range
- Pros and cons for this business context

**Valuation Method 2: [Method Name]**
- Calculation with specific steps
- Resulting valuation range
- Pros and cons for this business context

**Valuation Method 3: [Method Name]**
- Calculation with specific steps
- Resulting valuation range
- Pros and cons for this business context

**Consolidated Valuation Range**
- Low, mid, and high estimates with confidence levels
- Recommended range for negotiations

**Key Value Drivers**
- Factors that could increase valuation (with estimated impact)

**Risk Factors**
- Factors that could decrease valuation (with estimated impact)

**Strategic Recommendations**
- Actionable next steps for the stated purpose

Use tables to compare methods side-by-side. Bold important figures. Provide specific dollar amounts and percentages. State all material assumptions explicitly.
```

## 用法 / Usage
- 必填變數 / Variables: {{financial-metrics}}、{{valuation-purpose}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Business Valuation Analysis Prompt is a free AI prompt that applies multiple valuation methodologies to pr…

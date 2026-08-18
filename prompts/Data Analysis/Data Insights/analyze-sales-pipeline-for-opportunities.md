# Sales Pipeline Opportunity Analysis Prompt

## 簡介

The Sales Pipeline Opportunity Analysis Prompt is a free AI prompt that evaluates your sales data and market context to identify high-value growth opportunities and optimization areas. This sales pipeline analysis prompt for ChatGPT takes your company information, market position, and current sales metrics, then produces a prioritized summary table showing specific opportunities, expected revenue impact, and probability of closing. Below the table, it delivers detailed explanations for each opportunity including rationale based on market trends and customer behavior, recommended implementation strategies, risk mitigation approaches, and timeline considerations. It runs on ChatGPT, Claude, Gemini, and Grok, making it versatile for teams using different text-generation models. Real use cases include quarterly pipeline reviews, territory planning, and identifying which deals or segments warrant additional resources. This prompt is built for sales leaders, revenue operations teams, and business analysts who need structured, data-informed recommendations rather than raw spreadsheet exports. ● Produces a three-column summary table ranking opportunities by expected value (revenue × probability) and feasibility ● Estimates potential revenue impact and closing probability for each identified opportunity ● Considers market trends, customer behavior, and industry benchmarks in the analysis logic ● Includes detailed implementation strategies, risk mitigation steps, and timeline guidance for every recommendation ## Prompt

```
## Role
You are a sales analyst evaluating a company's pipeline to identify growth opportunities and optimization areas.

## Task
Analyze the provided sales and business context to produce a prioritized list of opportunities. For each opportunity, estimate potential revenue impact and likelihood of success. Consider current market trends, customer behavior, and industry benchmarks in your analysis.

## Context
**Company & Market:**
{{company-and-market}}
(Include: company name, industry, target market segments)

**Sales Performance:**
{{sales-data-and-kpis}}
(Provide: current sales metrics overview, key performance indicators, notable trends)

## Output
Deliver your analysis as:

1. **Summary table** with three columns:
   - OPPORTUNITY (clear, specific description)
   - EXPECTED REVENUE (quantified estimate or range)
   - PROBABILITY OF CLOSING (percentage or High/Medium/Low)

2. **Detailed explanations** below the table for each opportunity covering:
   - Rationale and supporting data
   - Recommended implementation strategies
   - Risks, challenges, and mitigation approaches
   - Timeline considerations

Prioritize opportunities by expected value (revenue × probability) and implementation feasibility.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-and-market}}、{{sales-data-and-kpis}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales Pipeline Opportunity Analysis Prompt is a free AI prompt that evaluates your sales data and market c…

# Sales Funnel Analysis Prompt for ChatGPT

## 簡介

The Sales Funnel Analysis Prompt for ChatGPT is a free AI prompt that diagnoses conversion bottlenecks and delivers actionable optimization strategies for businesses seeking to improve funnel performance. This sales funnel analysis prompt for ChatGPT takes your business context - funnel stages, audience characteristics, product offering, and conversion challenges - and returns a structured markdown table evaluating each stage's current conversion rate alongside 3-5 tailored optimization tactics. It runs on ChatGPT, Claude, and Gemini, producing a stage-by-stage diagnostic followed by a prioritized summary of the highest-leverage improvements. Marketing teams use it to surface hidden friction points, e-commerce businesses rely on it to audit checkout abandonment, and SaaS operators apply it to onboarding and retention stages. Reach for this prompt when you need a systematic, data-informed view of where prospects drop off and how to fix it. ● Evaluates each funnel stage - from awareness through retention - with estimated conversion rates and bottleneck identification. ● Proposes 3-5 detailed, actionable optimization tactics per stage, tailored to your business type and conversion challenge. ● Outputs a markdown table for easy sharing with stakeholders, followed by a summary of the top 2-3 highest-impact improvements. ● Adapts to any business model: e-commerce, SaaS, lead-gen, B2B pipelines, subscription services, or multi-step checkout flows. ## Prompt

```
## Role
You are an expert sales funnel analyst specializing in conversion rate optimization.

## Task
Analyze the sales funnel for the business described below, identify bottlenecks at each stage, evaluate current conversion rates, and propose specific optimization strategies to improve overall funnel performance and increase revenue.

## Context
**Business & Funnel Details:**
{{business-and-funnel-context}}

Include: business type, current funnel stages (e.g., Awareness → Interest → Consideration → Purchase → Retention), target audience characteristics, main product/service offering, and the biggest conversion challenge currently faced.

## Output
Deliver your analysis as a markdown table with three columns:

| FUNNEL STAGE | CURRENT CONVERSION RATE | OPTIMIZATION STRATEGIES |
|--------------|-------------------------|-------------------------|

Each row should correspond to one funnel stage. For each stage:
- Assess the likely current conversion rate based on the context provided
- Propose 3-5 detailed, actionable optimization strategies tailored to the specific business and challenge
- Prioritize high-impact tactics that address the identified bottlenecks

After the table, provide a brief summary highlighting the 2-3 highest-leverage improvements.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-and-funnel-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Sales Funnel Analysis Prompt for ChatGPT is a free AI prompt that diagnoses conversion bottlenecks and del…

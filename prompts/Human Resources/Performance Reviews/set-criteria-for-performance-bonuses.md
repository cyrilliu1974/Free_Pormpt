# Sales Performance Bonus Criteria Generator

## 簡介

The Sales Performance Bonus Criteria Generator is a free AI prompt that builds tiered bonus plans for sales teams based on your metrics, targets, and business context. This sales bonus structure prompt for ChatGPT analyzes your key sales metrics - revenue, quota attainment, new accounts, or custom KPIs - and designs a 3-5 tier reward plan that motivates continuous improvement and recognizes top performers. It outputs a markdown table mapping performance levels to bonus amounts or percentages, tier-by-tier explanations of why each threshold drives the right behaviors, and conditions such as minimum tenure, conduct standards, and payment timing. Sales managers, compensation specialists, and HR teams use it to replace subjective bonus decisions with transparent, data-aligned incentive structures that sales reps can immediately understand. The prompt runs on ChatGPT, Claude, Gemini, and Grok. ● Outputs a multi-tier bonus table mapping metrics to dollar amounts or percentages ● Provides rationale for each tier to ensure thresholds align with business goals and drive desired behaviors ● Includes eligibility conditions, pro-rating rules, and payment timing for compliance and clarity ● Adapts to any sales context - SaaS, B2B, retail, enterprise - and any metric mix ## Prompt

```
## Role
You are a senior sales compensation specialist designing a performance bonus structure that motivates sales teams and aligns rewards with business outcomes.

## Task
Create a tiered bonus plan based on the provided sales context. Analyze the metrics and goals to set appropriate thresholds, design tiers that encourage continuous improvement and reward exceptional performance, then present the structure in a clear table format.

## Context
{{sales-context}}

Include relevant details: key sales metrics (revenue, quota attainment, new accounts, etc.), performance goals and targets, industry, team size, and any existing bonus structure to build from or replace.

## Output
Deliver:

1. **Bonus Structure Table** in markdown format:

| Sales Metrics | Bonus Amounts |
|--------------|---------------|
| [tier description] | [amount/percentage] |

Include 3-5 performance tiers that span from minimum threshold to top performer levels.

2. **Tier Explanations**: Brief rationale for each tier's thresholds and why they motivate the desired behaviors.

3. **Conditions & Qualifications**: Any additional requirements (minimum tenure, conduct standards, payment timing, pro-rating rules) necessary to earn bonuses.

Ensure the structure is immediately understandable to sales team members and fair across different performance levels.
```

## 用法 / Usage
- 必填變數 / Variables: {{sales-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales Performance Bonus Criteria Generator is a free AI prompt that builds tiered bonus plans for sales te…

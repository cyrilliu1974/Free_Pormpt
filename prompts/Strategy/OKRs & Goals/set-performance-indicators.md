# Performance Indicator Framework Generator

## 簡介

The Performance Indicator Framework Generator is a free AI prompt that builds a complete set of Key Performance Indicators tailored to your business type, goals, and strategic objectives. This performance indicator prompt for ChatGPT analyzes your business context and produces a structured table of KPIs - each validated against SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound) - along with realistic targets, recommended measurement frequency, and detailed rationale. It balances leading indicators (predictive metrics) with lagging indicators (outcome measures) and grounds target-setting in industry benchmarks. Runs on ChatGPT, Claude, Gemini, and Grok. Use it when launching performance-tracking systems, refining strategy alignment, or establishing dashboards for executive teams, department heads, or startup founders. ● Delivers a markdown table mapping each KPI to its target and measurement cadence ● Explains why each metric matters, how it supports stated goals, and whether it is leading or lagging ● Aligns indicators with strategic objectives and industry standards to enable actionable decision-making ● Balances insight value against tracking overhead, recommending practical measurement frequencies ## Prompt

```
## Role
You are a business analyst specializing in Key Performance Indicator (KPI) development.

## Task
Develop a comprehensive set of KPIs tailored to the specified business context. For each KPI:
- Ensure it is SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- Balance leading indicators (predictive) with lagging indicators (outcome-based)
- Set realistic targets based on industry standards
- Define appropriate measurement frequency
- Align with strategic objectives to enable actionable decision-making

## Context
{{business-context}}

## Analysis Approach
1. Identify the core performance areas relevant to the business type and goals
2. Select KPIs that directly support strategic objectives
3. Establish targets reflecting industry benchmarks and company maturity
4. Recommend measurement cadences that balance insight value with tracking overhead

## Output
Present your KPIs in a markdown table:

| KPI | Target | Measurement Frequency |
|-----|--------|----------------------|

Below the table, provide a brief explanation for each KPI covering:
- Why it matters for this business
- How it connects to the stated goals
- Whether it is a leading or lagging indicator
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Reasoning_Strategy_Advisor
- 適用 / Use when: The Performance Indicator Framework Generator is a free AI prompt that builds a complete set of Key Performanc…

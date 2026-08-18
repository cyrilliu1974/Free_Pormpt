# Marketing Automation Metrics Analysis Prompt

## 簡介

The Marketing Automation Metrics Analysis Prompt is a free AI prompt that evaluates marketing automation campaign performance by analyzing key metrics and delivering actionable recommendations for marketing analysts and teams. This marketing automation metrics prompt for ChatGPT takes your campaign name, goals, audience, industry, and timeframe as inputs and produces a structured markdown table comparing four critical KPIs - open rate, click-through rate, conversion rate, and ROI - against their target values. For each metric, it identifies whether goals were met, highlights trends or anomalies in the data, and provides specific, concrete recommendations for optimization or scaling success. It runs on ChatGPT, Claude, Gemini, and Grok, making it flexible for any text-based AI workflow. This prompt is designed for marketing analysts, automation specialists, and campaign managers who need to quickly assess performance, identify what's working, and pinpoint exactly where to improve. Use it after any email campaign, nurture sequence, or automated funnel to turn raw data into strategic next steps. ● Compares open rate, click-through rate, conversion rate, and ROI against campaign goals in a single structured view ● Identifies trends, anomalies, and performance gaps with actionable insights for each metric ● Delivers concrete recommendations for improving underperforming areas and scaling successful tactics ● Outputs findings in markdown table format for easy reporting and stakeholder sharing ## Prompt

```
## Role
You are an expert marketing analyst evaluating marketing automation performance.

## Task
Analyze key metrics—open rates, click-through rates, conversion rates, and ROI—and provide actionable insights. Compare actual performance against goals, identify trends, anomalies, and optimization opportunities.

## Context
**Campaign:** {{campaign-name}}
**Goals & audience:** {{campaign-goals-and-audience}}
**Industry & timeframe:** {{industry-and-timeframe}}

## Output
Deliver your analysis as a markdown table with four columns:

| Metric | Goal | Actual | Insights |
|--------|------|--------|----------|

For each metric row, provide:
- **Metric**: The KPI name (Open Rate, Click-Through Rate, Conversion Rate, ROI)
- **Goal**: The target value
- **Actual**: The observed result
- **Insights**: Concise analysis noting whether the metric met/missed the goal, any trends or anomalies, and one concrete recommendation for improvement or leveraging success

Ensure insights are specific, actionable, and highlight both wins and areas needing optimization.
```

## 用法 / Usage
- 必填變數 / Variables: {{campaign-goals-and-audience}}、{{campaign-name}}、{{industry-and-timeframe}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Marketing Automation Metrics Analysis Prompt is a free AI prompt that evaluates marketing automation campa…

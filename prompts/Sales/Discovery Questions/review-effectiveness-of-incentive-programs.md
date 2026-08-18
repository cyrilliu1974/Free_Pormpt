# Sales Incentive Program Effectiveness Review Prompt

## 簡介

The Sales Incentive Program Effectiveness Review Prompt is a free AI prompt that evaluates sales incentive programs and delivers structured performance analysis for sales analysts and revenue leaders. This sales incentive analysis prompt for ChatGPT works by assessing each program - commission tiers, bonuses, SPIFs, recognition awards, travel incentives - against performance metrics you define, such as revenue lift, deal velocity, quota attainment, participation rate, and ROI. The prompt produces a markdown table with program names, incentive types, performance summaries, effectiveness ratings (Highly Effective, Effective, Needs Improvement, Ineffective), and data-backed explanations. Sales leaders use it to identify which incentives drive results and which drain budget without moving the needle. It runs on ChatGPT, Claude, and Gemini. Reach for this prompt when you need to justify incentive spend, optimize comp plans, or present incentive performance to executives in a clear, repeatable format. ● Evaluates multiple incentive programs side by side with consistent performance criteria ● Assigns effectiveness ratings grounded in KPIs like revenue lift, deal velocity, and ROI ● Outputs a clean markdown table formatted for executive reports and strategy sessions ● Supports custom column counts to surface dimensions like cost per acquisition or year-over-year trends ## Prompt

```
## Role
You are an expert sales analyst evaluating sales incentive programs.

## Task
Analyze the effectiveness of current sales incentive programs and present findings in a structured table format.

## Context
Company: {{company-name}}

Programs to evaluate: {{programs-and-incentives}}
(List each program name and its incentive type—e.g., commission tiers, bonuses, SPIFs, recognition awards, travel incentives)

Performance metrics: {{performance-metrics}}
(Specify the KPIs used to assess each program—e.g., revenue lift, deal velocity, quota attainment, participation rate, ROI)

## Method
1. Assess each program against the provided performance metrics
2. Determine an effectiveness rating (e.g., Highly Effective, Effective, Needs Improvement, Ineffective) based on metric performance
3. Justify each rating with data-driven reasoning

## Output
Deliver your analysis as a markdown table with these columns:
- **Program Name**
- **Incentive Type**
- **Performance Metrics** (summarize key results)
- **Effectiveness Rating**
- **Explanation** (brief rationale for the rating, citing specific metrics)

Ensure the table has {{number-of-columns}} columns total. If more columns are needed beyond the five listed, add relevant dimensions such as Cost per Acquisition, Participation Rate, or Year-over-Year Change.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-name}}、{{number-of-columns}}、{{performance-metrics}}、{{programs-and-incentives}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Project_Discovery_Scoping_Protocol
- 適用 / Use when: The Sales Incentive Program Effectiveness Review Prompt is a free AI prompt that evaluates sales incentive pro…

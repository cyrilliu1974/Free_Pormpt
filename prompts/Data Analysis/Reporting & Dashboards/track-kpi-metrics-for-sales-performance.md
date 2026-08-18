# Sales KPI Tracking Table Generator

## 簡介

The Sales KPI Tracking Table Generator is a free AI prompt that creates customized KPI monitoring systems for sales teams and managers. This sales KPI tracking prompt for ChatGPT produces a markdown table with four columns - KPI Name, Description, Target, and Actual Performance - populated with metrics tailored to your team's structure, goals, and sales context. It works on ChatGPT, Claude, and Gemini by analyzing the sales-team-context you provide, then selecting the most impactful indicators (conversion rates, pipeline velocity, average deal size, quota attainment, etc.) and pairing each with a clear description and realistic target. Sales managers use it to build dashboards, align team objectives, and prepare performance reviews; revenue operations teams deploy it to standardize reporting across regions or product lines. Reach for this prompt when you need a consistent, ready-to-populate framework that turns scattered sales data into a single tracking table. ● Generates a four-column markdown table (KPI Name, Description, Target, Actual Performance) ready to fill with live data. ● Selects metrics based on your sales-team-context - team size, product type, sales cycle, or vertical - so the table reflects real priorities. ● Includes clear, actionable descriptions and realistic targets for each KPI, making it simple to spot gaps and drive improvement. ● Works across text-generation models (ChatGPT, Claude, Gemini) and exports easily into spreadsheets, dashboards, or reports. ## Prompt

```
## Role
You are an expert sales performance analyst building a KPI tracking system for a sales team.

## Task
Create a comprehensive KPI tracking table that monitors sales performance metrics. For each KPI:
- Provide a clear, actionable description
- Set realistic targets aligned with sales strategy
- Include space for actual performance data
- Ensure metrics deliver actionable insights for improvement

## Context
{{sales-team-context}}

## Output
Deliver a markdown table with exactly these columns: **KPI Name** | **Description** | **Target** | **Actual Performance**

Populate the table with the KPIs most relevant to the team context provided. If specific KPIs were mentioned, include those; otherwise select the most impactful metrics for the team structure and goals described.
```

## 用法 / Usage
- 必填變數 / Variables: {{sales-team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales KPI Tracking Table Generator is a free AI prompt that creates customized KPI monitoring systems for …

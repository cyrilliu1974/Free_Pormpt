# Operational Efficiency Metrics Report Generator

## 簡介

The Operational Efficiency Metrics Report Generator is a free AI prompt that creates actionable performance analysis reports for business departments of any size or type. This operational efficiency prompt for ChatGPT analyzes your department's current data, selects 5-8 relevant key performance indicators, and outputs a clean markdown table with four columns: the metric name, current performance baseline, specific measurable target, and 2-4 prioritized action steps to close the gap. You provide the department name and any available performance data or goals, and the prompt structures a complete efficiency roadmap. It runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for quarterly reviews, board presentations, process improvement initiatives, and strategic planning sessions. Business analysts, operations managers, department heads, and consultants use this prompt when they need to turn raw performance data into a clear improvement plan that stakeholders can act on immediately. ● Automatically selects the most relevant KPIs for the department type or uses your specified metrics ● Quantifies current performance from your data or estimates realistic ranges when information is incomplete ● Sets targets aligned with industry benchmarks and the department's actual capacity ● Delivers 2-4 prioritized, actionable initiatives per metric to guide implementation ## Prompt

```
## Role
You are an expert business analyst creating a comprehensive operational efficiency report.

## Task
Analyze the department's current performance, identify relevant metrics, set appropriate targets, and develop actionable improvement steps. Present findings in a clear, actionable format that provides a roadmap for enhancing operational efficiency.

## Context
Department: {{department}}

Performance data and goals: {{current-data-and-targets}}

## Output
Present your analysis as a markdown table with these columns: Metric | Current Performance | Target | Action Steps

- Each row covers one key performance metric relevant to the department
- Current Performance: quantified baseline from available data, or estimated range if data is incomplete
- Target: specific, measurable goal aligned with industry benchmarks and department capacity
- Action Steps: 2-4 concrete, prioritized initiatives to close the gap

Include 5-8 metrics that matter most for this department's operational efficiency. If specific metrics were requested, prioritize those; otherwise select the most impactful indicators for the department type.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-data-and-targets}}、{{department}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Operational Efficiency Metrics Report Generator is a free AI prompt that creates actionable performance an…

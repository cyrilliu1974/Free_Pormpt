# Automated Analytics Report Generator for Education

## 簡介

The Automated Analytics Report Generator for Education is a free AI prompt that builds a comprehensive KPI tracking framework for schools, colleges, and universities seeking to monitor institutional performance and student outcomes. This education analytics prompt for ChatGPT creates a markdown table of 8–12 tailored metrics covering areas like student retention, enrollment trends, learning outcomes, faculty effectiveness, and financial health. You specify your institution type, focus areas, reporting frequency, target audience (administrators, boards, accreditation bodies), and data systems (PowerSchool, Infinite Campus, SQL databases, Excel). The prompt then delivers metric names, clear definitions explaining what each KPI measures and why it matters, the exact data source or system field to pull from, and the optimal visualization type - line charts for trends, bar charts for comparisons, heatmaps for patterns, or gauges for thresholds. It runs on ChatGPT, Claude, and Gemini. Education leaders use it to standardize dashboards, prepare board reports, satisfy accreditation requirements, and identify early-warning signals in student performance. ● Maps each KPI to its precise data source, whether a student information system table, custom database query, or spreadsheet field ● Recommends the chart type that best reveals trends, outliers, or performance gaps for each metric ● Tailors the metric set to your institution's unique priorities - student success, operational efficiency, financial sustainability, or compliance ● Produces a reusable table format that stakeholders can adopt as a reporting standard across departments ## Prompt

```
## Role
You are an expert data analyst specializing in educational analytics and institutional performance measurement.

## Task
Generate an automated analytics report framework that tracks key performance indicators for an educational institution. For each metric, provide a clear definition, specify the data source, and recommend an appropriate visualization type.

## Context
**Institution & Focus**: {{institution-and-focus}}
(Include the institution name or type, and the key performance areas to track—e.g., student retention, learning outcomes, enrollment trends, faculty effectiveness, financial health.)

**Reporting Parameters**: {{reporting-parameters}}
(Specify the reporting frequency—daily, weekly, monthly, quarterly, annual—and the primary audience for this report, such as administrators, board members, department heads, or accreditation bodies.)

**Data Infrastructure**: {{data-system}}
(Name the data management system or platform in use, e.g., PowerSchool, Infinite Campus, custom SQL database, Excel workbooks.)

## Output
Deliver your response as a markdown table with exactly four columns:

| Metric | Definition | Data Source | Visualization |
|--------|------------|-------------|---------------|

Include 8–12 metrics tailored to the focus areas provided. Each row should contain:
- **Metric**: The KPI name
- **Definition**: A concise explanation of what it measures and why it matters
- **Data Source**: The specific table, report, or system field
- **Visualization**: The chart type best suited to display trends or comparisons (e.g., line chart, bar chart, heatmap, gauge)

Ensure the metrics provide actionable insights for improving educational outcomes and institutional performance.
```

## 用法 / Usage
- 必填變數 / Variables: {{data-system}}、{{institution-and-focus}}、{{reporting-parameters}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Automated Analytics Report Generator for Education is a free AI prompt that builds a comprehensive KPI tra…

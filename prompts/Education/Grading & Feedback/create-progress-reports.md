# Student Progress Report Generator for ChatGPT

## 簡介

The Student Progress Report Generator is a free AI prompt that transforms raw student performance data into comprehensive, actionable reports for educators and administrators. This student progress report prompt for ChatGPT organizes academic data into clear tables tracking individual student achievement across courses and metrics, then analyzes patterns to surface trends, identify improvement opportunities, and deliver evidence-based recommendations. It produces reports structured with an executive summary, formatted performance tables, trend analysis, improvement areas, and prioritized action items. The prompt runs on ChatGPT, Claude, Gemini, and Grok, adapting to your institution's grading period, data source, chosen performance metrics, and target audience - whether parents, faculty, or school leadership. Educators and administrators reach for this prompt when they need to convert spreadsheet data into professional reports that inform decision-making and communicate student progress effectively. ● Organizes student data into markdown tables with clear columns for name, course, grade, and custom performance metrics ● Identifies achievement patterns across cohorts, courses, or time periods to highlight what's working and what needs attention ● Generates prioritized, evidence-based recommendations tied directly to observed gaps and trends ● Formats output with executive summaries, section headings, and bullet points that communicate findings to diverse audiences ## Prompt

```
## Role

You are an expert educational data analyst creating comprehensive student progress reports.

## Task

Produce a structured performance report that tracks student achievement, identifies trends, and delivers actionable recommendations.

## Context

- **Institution & period**: {{institution-and-period}}
- **Data source**: {{data-source}}
- **Performance metrics**: {{performance-metrics}}
- **Audience**: {{audience}}

## Process

1. Organize raw data into a table with columns: Student Name, Course, Grade, and relevant performance metrics
2. Populate the table with data for each student
3. Analyze for trends, patterns, and improvement opportunities
4. Generate evidence-based insights and recommendations
5. Ensure all data is accurately represented

## Output

Structure your report with:

- **Executive Summary**: key findings in 3–5 bullet points
- **Student Performance Table**: organized data with clear column headers
- **Trend Analysis**: patterns observed across cohorts, courses, or metrics
- **Areas for Improvement**: specific gaps or underperforming segments
- **Recommendations**: prioritized action items with rationale

Use markdown tables for data, bullet points for insights, and clear section headings throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{audience}}、{{data-source}}、{{institution-and-period}}、{{performance-metrics}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Student Progress Report Generator is a free AI prompt that transforms raw student performance data into co…

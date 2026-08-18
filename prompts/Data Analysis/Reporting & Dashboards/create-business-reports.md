# Business Metrics Report Generator

## 簡介

The Business Metrics Report Generator is a free AI prompt that creates structured performance reports for business analysts, department heads, and strategic planners. This business metrics report prompt for ChatGPT works by guiding the AI to identify relevant KPIs for your specified department and report type, organize current performance data against targets, and generate actionable recommendations in a clean markdown table format. It runs on ChatGPT, Claude, Gemini, and Grok, producing reports with three core components: a concise introduction that frames the analysis, a metrics table showing current performance versus targets with specific action items, and a summary of key findings with prioritized recommendations. Use it for monthly departmental reviews, quarterly business analysis, executive briefings, or any situation where you need to translate raw metrics into strategic insights quickly. ● Produces markdown tables with four columns: Metrics, Current Performance, Targets, and Action Items for immediate use in presentations and documents ● Adapts to any department (sales, marketing, operations, finance) and report type (weekly, monthly, quarterly, annual) ● Includes executive summary sections that highlight critical gaps and recommended priorities ● Generates realistic targets based on industry standards and actionable items tailored to performance gaps ## Prompt

```
## Role
You are an expert business analyst who creates comprehensive performance reports that inform strategic decision-making.

## Task
Generate a detailed metrics report in a structured table format. 

1. Identify the most relevant metrics for the specified department and report type
2. Gather or estimate current performance data for each metric
3. Set appropriate targets based on industry standards and organizational goals
4. Develop actionable items to improve performance where gaps exist

## Context
**Department:** {{department}}
**Key metrics to track:** {{key-metrics}}
**Report type:** {{report-type}}

## Output
Provide:
- A brief introduction (2-3 sentences) summarizing the report's purpose and scope
- A markdown table with columns: Metrics | Current Performance | Targets | Action Items
- A summary of key findings highlighting the most critical insights and recommended priorities

Ensure the report is clear, concise, and actionable for strategic planning.
```

## 用法 / Usage
- 必填變數 / Variables: {{department}}、{{key-metrics}}、{{report-type}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Business Metrics Report Generator is a free AI prompt that creates structured performance reports for busi…

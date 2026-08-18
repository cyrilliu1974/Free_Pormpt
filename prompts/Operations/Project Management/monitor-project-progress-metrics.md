# Project Progress Metrics Tracker Report Generator

## 簡介

The Project Progress Metrics Tracker Report Generator is a free AI prompt that creates comprehensive KPI tracking reports for project managers and team leads. This project progress tracking prompt for ChatGPT organizes your key performance indicators into clean markdown tables, then analyzes the data to surface trends, flag challenges, and generate prioritized recommendations. You provide the project name, reporting frequency (weekly, monthly, sprint-based), the KPIs you're monitoring, and your preferred table structure - the prompt produces a two-part deliverable: a formatted progress table and a bullet-point analysis covering metric performance, positive and negative trends, critical issues, and next steps. It runs on ChatGPT, Claude, and Gemini, turning raw project data into decision-ready reports. Project managers use it to standardize status reporting, engineering leads rely on it for sprint reviews, and consultants deploy it to track client deliverables with consistent structure. ● Organizes any set of KPIs into a custom markdown table structure you define ● Analyzes metric performance to identify both positive momentum and emerging risks ● Flags critical challenges that require immediate attention or escalation ● Delivers prioritized, actionable recommendations grounded in the progress data ● Maintains consistent reporting format across weekly, bi-weekly, monthly, or sprint cycles ## Prompt

```
## Role
You are an expert project manager tracking key performance indicators and preparing structured progress reports.

## Task
Create a comprehensive progress report that tracks project metrics, identifies trends and challenges, and provides actionable recommendations. Present the data in a clear table format followed by analysis.

## Context
**Project:** {{project-name}}
**Reporting Frequency:** {{reporting-frequency}}
**Key Performance Indicators:** {{kpis}}
**Table Structure:** {{table-structure}}

## Process
1. Organize the KPIs into the specified table structure
2. Analyze the data to identify trends, challenges, and successes
3. Assess each metric's current status and implications
4. Develop actionable recommendations based on the progress data

## Output
Deliver your report in two parts:

1. **Progress Table:** A markdown table displaying all KPIs according to the specified structure
2. **Analysis:** Bullet-point list containing:
   - Key observations about metric performance
   - Identified trends (positive and negative)
   - Critical challenges requiring attention
   - Actionable recommendations with priorities
```

## 用法 / Usage
- 必填變數 / Variables: {{kpis}}、{{project-name}}、{{reporting-frequency}}、{{table-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Project Progress Metrics Tracker Report Generator is a free AI prompt that creates comprehensive KPI track…

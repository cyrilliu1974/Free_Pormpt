# KPI Dashboard Specification Generator

## 簡介

The KPI Dashboard Specification Generator is a free AI prompt that creates comprehensive dashboard specifications for tracking key performance indicators across any department or business function. This KPI dashboard prompt for ChatGPT guides you through designing a complete dashboard structure - from defining calculation methods and target thresholds for each metric to specifying chart types, column layouts, and drill-down capabilities. You provide your department goals, desired column count, and KPI list; the prompt returns a full specification document covering dashboard purpose, KPI definitions with targets, layout design with visual hierarchy, visualization recommendations with rationale, interactive filtering options, and actionable insights tied to each metric state. It runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for business intelligence teams, data analysts, and department heads building or redesigning performance dashboards. ● Defines each KPI with precise calculation methods, target values, and threshold ranges for red/yellow/green states ● Specifies column structure, component placement, and visual hierarchy to ensure intuitive information flow ● Recommends the optimal chart or graph type for each metric with clear rationale based on data characteristics ● Includes interactive drill-down paths, filtering options, and user interaction patterns for deeper data exploration ## Prompt

```
## Role
You are an expert data analyst and business intelligence specialist creating KPI dashboards.

## Task
Generate a comprehensive, visually appealing KPI dashboard specification that effectively tracks and analyzes key performance indicators for {{department-goals}}.

## Context
The dashboard should:
- Present data in a clear, intuitive layout with {{column-count}} columns
- Track these specific KPIs: {{kpi-list}}
- Enable actionable insights and performance comparison over time
- Include appropriate data visualizations (charts, graphs, tables)
- Incorporate drill-down capabilities and interactive elements for data exploration

## Output
Provide a structured dashboard specification with:

### Dashboard Overview
- Purpose and target audience
- Key objectives alignment

### KPI Definitions
- Each KPI with calculation method, target values, and thresholds

### Layout Design
- Column structure and component placement
- Visual hierarchy and information flow

### Visualization Recommendations
- Chart/graph type for each KPI with rationale
- Color coding and visual conventions

### Interactive Features
- Drill-down paths and filtering options
- User interaction patterns

### Insights & Actions
- Key insights each section should surface
- Recommended actions based on KPI states
```

## 用法 / Usage
- 必填變數 / Variables: {{column-count}}、{{department-goals}}、{{kpi-list}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The KPI Dashboard Specification Generator is a free AI prompt that creates comprehensive dashboard specificati…

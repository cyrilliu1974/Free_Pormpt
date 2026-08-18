# CRM Dashboard Customization Prompt for Data Insights

## 簡介

The CRM Dashboard Customization Prompt for Data Insights is a free AI prompt that creates detailed configuration plans to optimize CRM dashboards for business intelligence and decision-making. This CRM dashboard prompt for ChatGPT guides you through every aspect of dashboard design: metric prioritization, visualization selection, layout hierarchy, color schemes, interactive filters, automated alerts, and usability validation. It works on ChatGPT, Claude, and Gemini, taking your business context and target dashboard structure as inputs and delivering a step-by-step customization plan formatted as a markdown table that maps directly to your specified columns. Real-world use cases include sales pipeline visualization, customer service performance tracking, marketing campaign monitoring, and executive reporting dashboards. Reach for this prompt when you need to transform a generic CRM interface into a focused analytics tool that surfaces the metrics your team actually needs, or when onboarding users who require clear visual guidance on dashboard configuration. ● Recommends appropriate chart types for each metric with clear rationale - time series for trends, gauges for KPIs, funnels for conversion stages, heatmaps for activity patterns ● Designs intuitive multi-column layouts that balance visual hierarchy with logical information flow across main views and drill-down panels ● Specifies interactive features including dynamic filters, drill-through links, hover tooltips, and threshold-based alerts that enable deeper data exploration ● Provides design guidelines covering performance-based color schemes, spacing, font sizing, and data refresh schedules that keep dashboards accurate and actionable ## Prompt

```
## Role
You are a CRM expert specializing in dashboard customization and business intelligence visualization.

## Task
Create a comprehensive dashboard customization plan that helps the user configure their CRM to surface actionable insights. The plan should guide them through selecting relevant widgets, choosing effective visualizations, designing an intuitive layout, and implementing interactive features.

## Context
Business context: {{business-context}}
(Include business type, key metrics to track, team size, and primary goals for the dashboard)

Target dashboard structure: {{dashboard-structure}}
(Specify number of columns and their names/purposes)

## Output
Provide a step-by-step customization plan covering:

- **Metric selection & prioritization**: Which of the specified metrics belong on the main dashboard vs. drill-down views, and why
- **Visualization recommendations**: Appropriate chart types for each metric (time series, bar, gauge, funnel, heatmap, etc.) with rationale
- **Layout & hierarchy**: How to arrange widgets across the specified columns for logical flow and visual balance
- **Design guidelines**: Color schemes that aid interpretation (e.g., red/yellow/green for performance thresholds), font sizes, spacing
- **Interactivity**: Filters, drill-through links, tooltips, and click actions that enable deeper analysis
- **Automation**: Recommended data refresh schedules and alerts for threshold breaches
- **Usability testing**: How to validate the dashboard meets user needs

Present the plan as a markdown table using the column structure specified in {{dashboard-structure}}. Each row should represent one dashboard component or configuration step, with details distributed across the columns as appropriate.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{dashboard-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The CRM Dashboard Customization Prompt for Data Insights is a free AI prompt that creates detailed configurati…

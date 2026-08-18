# Real-Time Sales Dashboard Builder Prompt

## 簡介

The Real-Time Sales Dashboard Builder Prompt is a free AI prompt that creates structured, actionable sales dashboard designs for operations teams tracking performance metrics. This sales dashboard prompt for ChatGPT guides the AI to act as a data visualization specialist, producing a complete dashboard framework that includes a markdown KPI table (with current values, targets, variances, and status indicators), visual design recommendations (color-coding schemes, thresholds, icon systems), and technical specifications (refresh rates, data sources, alert triggers). It works on ChatGPT, Claude, and Gemini, turning your team context and chosen KPIs into a working dashboard prototype with realistic example data. Sales managers use it to standardize reporting, operations analysts rely on it to design stakeholder dashboards, and revenue teams adopt it to align on metric definitions and visual conventions. Reach for this prompt when you need a dashboard structure quickly, want consistent visual language across reports, or are onboarding a team to new KPI tracking systems. ● Outputs a markdown table layout with KPI name, current value, target, absolute and percentage variance, and status indicators ● Includes visual design rules (red/yellow/green thresholds, emoji or icon systems) and formatting conventions for positive and negative performance ● Specifies technical requirements such as recommended data refresh rates, data source dependencies, and alert thresholds for critical metrics ● Suggests enhancement features like trend indicators (week-over-week, month-over-month), drill-down paths, and export options for stakeholder sharing ## Prompt

```
## Role
You are an expert data visualization specialist designing real-time sales dashboards.

## Task
Create an effective dashboard that tracks key performance indicators for a sales operations team. Design a structured table layout that clearly presents each KPI with its current value, target value, and variance.

## Context
Sales operations team: {{team-context}}

Key performance indicators to track: {{kpis}}

## Output
Deliver a complete dashboard design that includes:

1. **KPI Table Structure** - A markdown table with columns for: KPI name, current value, target value, variance (absolute and percentage), and status indicator

2. **Visual Design Recommendations**
   - Color coding scheme for performance levels (red/yellow/green thresholds)
   - Icon or emoji indicators for at-a-glance status assessment
   - Formatting conventions for positive/negative variances

3. **Technical Specifications**
   - Recommended data refresh rate for each KPI
   - Data source requirements
   - Alert thresholds for critical metrics

4. **Enhancement Features**
   - Trend indicators (week-over-week, month-over-month)
   - Drill-down recommendations for deeper analysis
   - Export and sharing capabilities

Present the dashboard as a working markdown table with realistic example data that demonstrates the layout and visual conventions. Include a legend explaining your color coding and status indicators.
```

## 用法 / Usage
- 必填變數 / Variables: {{kpis}}、{{team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Real-Time Sales Dashboard Builder Prompt is a free AI prompt that creates structured, actionable sales das…

# Real-Time Educational Analytics Framework Builder

## 簡介

The Real-Time Educational Analytics Framework Builder is a free AI prompt that generates comprehensive analytics strategies for educational institutions seeking to monitor and improve student performance, engagement, and learning outcomes. This educational analytics prompt for ChatGPT guides data analysts through the creation of a structured framework that connects data collection, metric selection, and visualization design. It runs on ChatGPT, Claude, and Gemini, taking into account your institution type, existing data infrastructure, priority focus areas, and target stakeholders to produce 6-8 cohesive analytics strategies presented in a clear markdown table. Use cases include building dashboards for university administrators, designing real-time monitoring systems for K-12 districts, and creating data pipelines that align technical capabilities with decision-making needs. Educational data analysts, business intelligence teams, and institutional research professionals reach for this prompt when they need to translate scattered data assets into a unified analytics strategy tailored to their institution's unique context and stakeholder requirements. ● Maps data sources directly to measurable outcomes like student performance, engagement, and retention ● Generates visualization strategies appropriate for different stakeholder audiences (faculty, administrators, academic leadership) ● Accounts for existing technical infrastructure to ensure recommendations are implementable, not aspirational ● Produces 6-8 integrated strategies that form a complete view of institutional effectiveness rather than isolated metrics ## Prompt

```
## Role
You are an expert data analyst specializing in educational analytics.

## Task
Develop a comprehensive real-time analytics framework for an educational institution. The framework should cover data collection, analysis, and visualization to deliver actionable insights that improve student performance, engagement, and learning outcomes.

## Context
Institution: {{institution-type}}
Current infrastructure: {{current-data-infrastructure}}
Primary focus: {{focus-areas}}
Target stakeholders: {{target-audience}}

Design strategies that align with the institution's existing capabilities while addressing their specific educational priorities and stakeholder needs.

## Output
Deliver your framework as a markdown table with three columns:

| DATA SOURCES | KEY METRICS | VISUALIZATION TECHNIQUES |
|--------------|-------------|-------------------------|

Each row should represent one cohesive analytics strategy targeting a specific dimension of student performance, engagement, or learning outcomes. Include 6-8 strategies that together form a holistic view of institutional effectiveness. Ensure recommendations are practical given the described infrastructure and directly support the stakeholders' decision-making needs.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-data-infrastructure}}、{{focus-areas}}、{{institution-type}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Real-Time Educational Analytics Framework Builder is a free AI prompt that generates comprehensive analyti…

# Sales Workflow Automation Analysis & Design Prompt

## 簡介

The Sales Workflow Automation Analysis & Design Prompt is a free AI prompt that helps sales operations professionals identify automation opportunities and build implementation-ready workflow plans. This sales workflow automation prompt for ChatGPT, Claude, and Gemini acts as an expert sales operations analyst that examines your existing processes, pinpoints high-impact automation candidates, and delivers a detailed comparison table showing how to transform manual tasks into efficient automated workflows. You provide your sales context, efficiency targets, and available automation platform, and the AI evaluates each opportunity for time savings, ROI, team productivity gains, customer experience impact, and implementation complexity. Sales leaders, operations managers, and revenue operations teams use it to prioritize automation projects and accelerate digital transformation. ● Generates 8-12 ranked automation opportunities in a three-column markdown table format ● Compares current manual workflows against proposed automated solutions with specific triggers and tools ● Evaluates each opportunity for time savings, productivity impact, and implementation complexity ● Includes change management considerations and customer experience effects for every recommendation ## Prompt

```
## Role
You are an expert sales operations analyst specializing in workflow automation and process optimization.

## Task
Analyze the current sales workflow, identify high-value automation opportunities, and design a comprehensive implementation plan that streamlines operations and increases efficiency.

## Context
Current sales environment:
{{sales-operations-context}}

Target efficiency improvement: {{efficiency-target}}

Automation tools available: {{automation-platform}}

For each automation opportunity, evaluate:
- Time savings and ROI potential
- Impact on sales team productivity
- Effect on customer experience and satisfaction
- Integration requirements and implementation complexity
- Change management considerations

## Output
Deliver your analysis as a markdown table with three columns:

| TASK | CURRENT PROCESS | AUTOMATED WORKFLOW |
|------|-----------------|--------------------|

Each row should:
- **TASK**: Name the sales activity or process step
- **CURRENT PROCESS**: Describe the existing manual workflow, including pain points and inefficiencies
- **AUTOMATED WORKFLOW**: Propose the automated solution, specifying triggers, actions, tools used, and expected benefits

Include 8-12 automation opportunities ranked by implementation priority and business impact.
```

## 用法 / Usage
- 必填變數 / Variables: {{automation-platform}}、{{efficiency-target}}、{{sales-operations-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Sales Workflow Automation Analysis & Design Prompt is a free AI prompt that helps sales operations profess…

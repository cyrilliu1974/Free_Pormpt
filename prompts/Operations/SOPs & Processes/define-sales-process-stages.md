# Sales Process Stage Definition Prompt

## 簡介

The Sales Process Stage Definition Prompt is a free AI prompt that builds complete sales workflow documentation tailored to your product, customers, and process. It outputs a markdown table mapping every stage of your sales cycle with descriptions, key activities, success metrics, typical durations, critical checkpoints, and the criteria that move prospects to the next stage. This sales process prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok. You provide three variables (your sales process type, target customer profile, and product or service), and the AI returns a 7-column table with status indicators and granular workflow detail. Sales leaders use it to standardize pipelines, onboard reps faster, and align teams around measurable milestones. Operations teams use it to document and refine handoffs between marketing, sales, and customer success. Reach for this prompt when you need to formalize an ad-hoc sales motion, communicate your process to stakeholders, or audit stage-by-stage conversion rates. ● Produces a 7-column table covering stage name, description, key activities, success metrics, duration, checkpoints, and next-stage triggers. ● Includes visual status emojis (in progress, complete) for at-a-glance workflow tracking. ● Accepts three variables so the output reflects your specific sales motion, customer segment, and offering. ● Outputs clean markdown tables that paste directly into Notion, Confluence, Google Docs, or CRM documentation. ## Prompt

```
## Role
You are a sales process engineer specializing in defining, optimizing, and visualizing sales workflows for maximum effectiveness.

## Task
Create a comprehensive sales process table with 7 columns:
- Stage
- Description
- Key Activities
- Success Metrics
- Duration
- Checkpoints
- Next Stage Trigger

For each stage, provide clear descriptions, key activities, success metrics, typical duration, critical checkpoints, and progression triggers.

Use status emojis:
- ⏳ = In Progress
- ✅ = Complete

## Context
**Sales process:** {{sales-process}}

**Target customers:** {{target-customers}}

**Product/service:** {{product-service}}

## Output
Deliver as a markdown table:

| Stage | Description | Key Activities | Success Metrics | Duration | Checkpoints | Next Stage Trigger |
|-------|-------------|----------------|-----------------|----------|-------------|--------------------|
| [Stage Name] [Status] | [Description] | - [Activity 1]<br>- [Activity 2]<br>- [Activity 3]<br>- [Activity 4] | - [Metric 1]<br>- [Metric 2]<br>- [Metric 3] | [Duration] | - [Checkpoint 1]<br>- [Checkpoint 2]<br>- [Checkpoint 3] | [Trigger] |
```

## 用法 / Usage
- 必填變數 / Variables: {{product-service}}、{{sales-process}}、{{target-customers}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Sales Process Stage Definition Prompt is a free AI prompt that builds complete sales workflow documentatio…

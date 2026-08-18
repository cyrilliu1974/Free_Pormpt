# CRM Automation Workflow Design Prompt for ChatGPT

## 簡介

The CRM Automation Workflow Design Prompt is a free AI prompt that creates structured automation plans for businesses looking to optimize their customer relationship management systems. This CRM automation prompt for ChatGPT walks you through designing comprehensive workflows across three core areas: lead management, customer communication, and sales processes. You provide your business context, CRM platform details, target audience characteristics, and key performance indicators, and the prompt generates a detailed automation plan delivered as a structured markdown table. Each workflow includes specific triggers, automated actions, timing sequences, task assignments, and predicted KPI impact. It runs on ChatGPT, Claude, and Gemini, making it ideal for operations managers, sales leaders, and CRM administrators mapping out automation strategies that integrate with platforms like Salesforce, HubSpot, Zoho, or Pipedrive. Reach for this prompt when you need to translate business objectives into executable CRM workflows, reduce manual follow-up tasks, or align your automation strategy with measurable conversion and velocity goals. ● Produces 9-15 prioritized workflows organized by lead management, customer communication, and sales process stages ● Specifies triggers, automated actions, email sequences, follow-up cadences, and task ownership for each workflow ● Aligns every automation to stated KPIs like conversion rate, response time, deal velocity, or customer retention ● Outputs a structured markdown table format that serves as an implementation roadmap for your CRM platform ## Prompt

```
## Role
You are a CRM automation specialist designing workflows that streamline lead management, customer communication, and sales processes.

## Task
Create a comprehensive CRM automation plan organized into three sections: lead management, customer communication, and sales processes. For each section, specify:
- Automated workflows and triggers
- Email templates and messaging sequences
- Follow-up cadences and timing
- Task assignments and ownership
- Success metrics aligned with the stated KPIs

Ensure all workflows integrate smoothly with the specified CRM platform and match the business's sales cycle stages.

## Context
**Business and CRM environment:**
{{business-and-crm-context}}
(Include: business type, current CRM system, sales process stages)

**Target audience:**
{{target-audience}}
(Describe customer demographics, pain points, buying behavior)

**Key performance indicators:**
{{kpi}}
(List the metrics this automation plan should improve: conversion rate, response time, deal velocity, etc.)

## Output
Deliver your automation plan as a markdown table with columns for:
- **Section** (Lead Management / Customer Communication / Sales Processes)
- **Workflow Name**
- **Trigger**
- **Actions** (emails, tasks, notifications)
- **Timing**
- **KPI Impact**

Provide 3–5 workflows per section, prioritizing high-impact automations that address the stated KPIs.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-and-crm-context}}、{{kpi}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The CRM Automation Workflow Design Prompt is a free AI prompt that creates structured automation plans for bus…

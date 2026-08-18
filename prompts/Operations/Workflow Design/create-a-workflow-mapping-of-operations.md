# Workflow Mapping for Operations Optimization

## 簡介

The Workflow Mapping for Operations Optimization is a free AI prompt that creates detailed workflow maps with actionable improvement recommendations for business operations teams. This workflow mapping prompt for ChatGPT helps business process analysts and operations managers systematically analyze current processes, assign clear ownership, identify appropriate tools, and establish measurable KPIs. Running on ChatGPT, Claude, or Gemini, it produces a markdown table that lays out each process step alongside responsible parties, required tools, and efficiency metrics, followed by 3-5 prioritized recommendations with expected impact. Use it when launching process improvement initiatives, onboarding new operations staff, documenting workflows for audits, or diagnosing bottlenecks in existing systems. ● Produces a four-column workflow table showing process steps, responsible parties, tools, and metrics in a single structured view. ● Analyzes operational context and current challenges to surface bottlenecks and inefficiencies. ● Delivers prioritized improvement recommendations ranked by expected impact and feasibility. ● Adapts to any industry or operational context by accepting company-specific details and baseline productivity levels. ## Prompt

```
## Role
You are an expert business process analyst specializing in workflow optimization and efficiency improvements.

## Task
Create a comprehensive workflow mapping that optimizes productivity and efficiency. Analyze current operations, identify key process steps with responsible parties, recommend appropriate tools, and establish measurable metrics.

## Context
**Company & Industry:** {{company-and-industry}}

**Operational Context:** {{operational-context}}
(Include: current challenges, baseline productivity level, and specific efficiency improvements sought)

## Process
1. Analyze the current operational processes
2. Identify key process steps and assign responsible parties
3. Recommend appropriate tools for each step
4. Define metrics to measure efficiency
5. Provide actionable recommendations for process improvements

## Output
Deliver your workflow mapping as a markdown table with these columns:
- **Process Steps** – sequential actions in the workflow
- **Responsible Parties** – roles or teams accountable for each step
- **Tools** – software, systems, or resources needed
- **Metrics** – KPIs to track efficiency and success

Follow the table with 3-5 prioritized recommendations for immediate process improvements, each with expected impact.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-and-industry}}、{{operational-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Workflow Mapping for Operations Optimization is a free AI prompt that creates detailed workflow maps with …

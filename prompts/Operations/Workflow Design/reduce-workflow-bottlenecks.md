# Workflow Bottleneck Analysis Prompt

## 簡介

The Workflow Bottleneck Analysis Prompt is a free AI prompt that systematically diagnoses process inefficiencies and delivers practical improvement recommendations for operations managers and workflow analysts. This workflow bottleneck prompt for ChatGPT examines each stage of your business process to pinpoint chokepoints, delays, and resource allocation issues. It runs on ChatGPT, Claude, Gemini, and Grok, producing a structured markdown table that maps specific bottlenecks to their productivity impact and pairs each with a concrete solution - including what changes, who implements it, and expected improvements. Use it when evaluating manufacturing lines, service delivery workflows, software development pipelines, or administrative processes where efficiency gains matter. ● Produces a table with 4–8 rows covering the most critical bottlenecks, their impact on time, cost, or quality, and actionable solutions ● Considers resource allocation, process redesign, automation opportunities, and skill gaps in every recommendation ● Ensures solutions are feasible, cost-effective, and aligned with industry best practices ● Adapts to any workflow context - manufacturing, service operations, software development, or administrative processes ## Prompt

```
## Role
You are a workflow optimization analyst specializing in diagnosing process inefficiencies and designing practical improvements.

## Task
Analyze the provided workflow to identify bottlenecks, assess their impact on productivity, and recommend actionable solutions. Examine each workflow stage systematically, considering resource allocation, process redesign, automation opportunities, and skill gaps. Ensure recommendations are feasible, cost-effective, and aligned with industry best practices.

## Context
**Workflow & Environment:**
{{workflow-context}}
(Include: the workflow process itself, industry, company size, current efficiency baseline, and budget constraints)

## Output
Present your analysis as a markdown table with three columns:

| Bottleneck | Impact | Solution |
|------------|--------|----------|
| [Specific chokepoint or delay] | [Effect on productivity, time, cost, or quality] | [Practical remediation with implementation approach] |

Provide 4–8 rows covering the most significant bottlenecks. Each solution should specify what changes, who implements it, and expected improvement.
```

## 用法 / Usage
- 必填變數 / Variables: {{workflow-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Workflow Bottleneck Analysis Prompt is a free AI prompt that systematically diagnoses process inefficienci…

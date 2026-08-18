# Bottleneck Analysis Prompt for Workflow Optimization

## 簡介

The Bottleneck Analysis Prompt for Workflow Optimization is a free AI prompt that systematically identifies delays and inefficiencies in business processes for operations managers, process analysts, and team leads. This bottleneck analysis prompt for ChatGPT works by examining your workflow context - including process steps, industry, team size, current metrics, and resource constraints - then delivers a prioritized markdown table with three columns: Bottleneck, Impact, and Solution. It runs on ChatGPT, Claude, Gemini, and Grok, analyzing each delay point for its effect on overall productivity and recommending practical fixes ordered by severity and feasibility. Use it when you need to diagnose why projects stall, where handoffs break down, or which constraints drain the most time. ● Identifies every bottleneck causing delays or reduced throughput in multi-step processes ● Assesses impact severity on productivity metrics so you address high-cost issues first ● Provides practical, implementable solutions tailored to your team size and resource constraints ● Outputs a markdown table sorted by priority, making it easy to share with stakeholders and track remediation ## Prompt

```
## Role
You are an expert process improvement analyst conducting a bottleneck analysis to identify workflow delays and optimize productivity.

## Task
Analyze the provided workflow to:

1. Identify all bottlenecks causing delays or inefficiency
2. Assess each bottleneck's impact on overall productivity
3. Develop practical, actionable solutions
4. Prioritize bottlenecks by impact severity and solution feasibility
5. Deliver clear recommendations for process improvement

## Context
{{workflow-context}}

*Include: the workflow process steps, industry, team size, current productivity metrics, and any resource constraints.*

## Output
Present your analysis as a markdown table with three columns:

| Bottleneck | Impact | Solution |
|------------|--------|----------|

Each row must provide concise, comprehensive information that enables effective decision-making and implementation. Order rows by priority (highest impact first).
```

## 用法 / Usage
- 必填變數 / Variables: {{workflow-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Bottleneck Analysis Prompt for Workflow Optimization is a free AI prompt that systematically identifies de…

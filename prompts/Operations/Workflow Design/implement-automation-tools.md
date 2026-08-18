# Business Process Automation Implementation Planner

## 簡介

The Business Process Automation Implementation Planner is a free AI prompt that creates structured automation strategies and implementation roadmaps for businesses looking to streamline their operations. This business process automation prompt for ChatGPT analyzes your existing workflows, identifies bottlenecks and automation opportunities, recommends appropriate tools within your budget, and documents a complete implementation plan using dependency grammar principles to show which tasks must be completed before others can begin. It works with ChatGPT, Claude, Gemini, and Grok to produce detailed roadmaps that cover process analysis, tool selection, sequenced implementation steps, resource allocation, timeline estimates, and success metrics. Teams use it when planning workflow automation projects, evaluating automation tools, or documenting implementation strategies that need to account for task dependencies and parallel execution paths. ● Maps current processes to identify inefficiencies, bottlenecks, and automation readiness ● Ranks automation opportunities by impact and recommends specific tools matched to budget and team size ● Creates sequenced implementation roadmaps showing which tasks depend on others and which can run in parallel ● Defines success metrics, KPIs, efficiency benchmarks, and ROI projections for measuring automation impact ## Prompt

```
## Role
You are an expert business process automation specialist implementing automation tools to streamline operations.

## Task
Document a complete automation implementation process using dependency grammar framework. Analyze the current process, identify automation opportunities, select appropriate tools, and outline implementation steps with clear task dependencies.

## Context
{{business-context}}

Include: the specific business process to automate, industry, current efficiency baseline (metrics, pain points, or bottlenecks), available budget, and team size.

## Output
Structure your documentation using dependency grammar principles:

### Process Analysis
- Current state mapping
- Bottlenecks and inefficiencies
- Automation readiness assessment

### Automation Strategy
- Identified automation opportunities (ranked by impact)
- Recommended tools and platforms
- Expected efficiency improvements

### Implementation Roadmap
- Sequenced steps with explicit dependencies ("Task B depends on Task A completion")
- Resource allocation
- Timeline estimates
- Risk mitigation

### Success Metrics
- KPIs to track
- Efficiency benchmarks
- ROI projections

Emphasize task dependencies throughout, showing which activities must precede others and which can run in parallel.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Business Process Automation Implementation Planner is a free AI prompt that creates structured automation …

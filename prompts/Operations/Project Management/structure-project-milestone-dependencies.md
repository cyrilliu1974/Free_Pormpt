# Project Milestone Dependency Structure Prompt

## 簡介

The Project Milestone Dependency Structure Prompt is a free AI prompt that transforms high-level project goals into structured milestone frameworks with full dependency analysis and critical path identification for project managers and team leads. This project management prompt for ChatGPT decomposes objectives into logical phases with clear deliverables, maps task interdependencies using forward and backward pass analysis, calculates the critical path to determine minimum project duration, and establishes monitoring protocols that prioritize bottleneck risks. It runs on ChatGPT, Claude, Gemini, and Grok, taking three variables - project goal, timeline and resource constraints, and primary risks - and returning a milestone breakdown, dependency matrix, critical path sequence with float calculations, and a monitoring framework that focuses resource allocation on timeline-critical elements. Use it when launching multi-phase initiatives, coordinating cross-functional teams, or planning under tight deadlines where sequencing and resource conflicts can derail delivery. ● Breaks ambitious goals into phase-by-phase milestones with success criteria and deliverables. ● Maps task relationships in a dependency matrix showing sequencing requirements and constraints. ● Calculates the critical path - the longest chain of dependent activities - and identifies float in non-critical tasks. ● Produces a monitoring framework with prioritized focus areas for resource allocation and risk mitigation. ## Prompt

```
## Role
You are an expert project management strategist specializing in critical path analysis, milestone decomposition, and dependency mapping for complex initiatives.

## Task
Transform the provided project goal into a structured milestone framework with comprehensive dependency analysis and critical path identification. Break down the objective into manageable components, map interdependencies, and establish monitoring protocols that focus on timeline-critical elements.

## Context
**Project Goal:** {{project-goal}}

**Timeline & Constraints:** {{timeline-resources-stakeholders}}
(Include deadline, available resources/team size, key stakeholders and decision-makers)

**Risk Profile:** {{primary-risks}}

## Analysis Method
1. Decompose the goal into logical milestone phases with clear deliverables and success criteria
2. Identify task dependencies using forward and backward pass analysis
3. Map relationships between all project elements in a dependency matrix
4. Calculate the critical path—the longest sequence of dependent activities determining minimum project duration
5. Establish monitoring protocols prioritizing critical path items and potential bottlenecks

## Output
Provide your analysis under these headings:

**Milestone Breakdown**
- Phase-by-phase structure with deliverables and success criteria

**Dependency Matrix**
- Present as a table mapping task relationships and sequencing requirements

**Critical Path Analysis**
- Identify the critical path sequence
- Highlight duration drivers and float/slack in non-critical tasks

**Monitoring Framework**
- Actionable recommendations in bullet points
- Focus areas for resource allocation and risk mitigation
```

## 用法 / Usage
- 必填變數 / Variables: {{primary-risks}}、{{project-goal}}、{{timeline-resources-stakeholders}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Project Milestone Dependency Structure Prompt is a free AI prompt that transforms high-level project goals…

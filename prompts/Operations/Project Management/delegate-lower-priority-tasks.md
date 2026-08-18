# Task Delegation Plan Builder for Project Managers

## 簡介

The Task Delegation Plan Builder for Project Managers is a free AI prompt that creates optimized work assignments by matching tasks to the right team members based on their capabilities and current workload. This task delegation prompt for ChatGPT analyzes your team roster, evaluates task requirements and complexity, and produces a complete delegation plan formatted as a markdown table with assigned owners and deadlines. It runs on ChatGPT, Claude, and Gemini, balancing workloads to prevent bottlenecks while ensuring all assignments ladder up to your project deadline. The prompt includes a rationale section that explains key assignment decisions, helping managers communicate why specific team members were chosen for particular tasks. Project managers use it when launching new initiatives, redistributing work during team changes, or rebalancing assignments when priorities shift. ● Assesses task complexity, dependencies, and skill requirements before making assignments ● Matches each task to team members based on experience, capabilities, and current workload ● Sets realistic deadlines that prevent bottlenecks and ensure timely project completion ● Provides assignment rationale to help managers explain delegation decisions to their teams ## Prompt

```
## Role
You are an expert team manager specializing in task delegation and resource optimization.

## Task
Create a task delegation plan that assigns work to team members based on their skills, experience, and current availability. Match each task to the most suitable person and set realistic deadlines that ensure timely project completion.

## Context
{{team-roster}}

{{task-list}}

{{project-deadline}}

## Process
1. Assess each task's requirements, complexity, and dependencies
2. Match tasks to team members based on skills, experience, and current workload
3. Balance assignments to prevent bottlenecks and optimize productivity
4. Set achievable deadlines that ladder up to the project deadline

## Output
Provide your delegation plan as a markdown table with three columns:

| Task | Assignee | Deadline |
|------|----------|----------|

Include a brief rationale beneath the table explaining key assignment decisions.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-deadline}}、{{task-list}}、{{team-roster}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Task Delegation Plan Builder for Project Managers is a free AI prompt that creates optimized work assignme…

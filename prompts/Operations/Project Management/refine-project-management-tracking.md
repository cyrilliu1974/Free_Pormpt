# Project Task Duration Tracking Table Generator

## 簡介

The Project Task Duration Tracking Table Generator is a free AI prompt that creates detailed time-tracking frameworks for project managers who need to analyze task performance and refine estimation accuracy. This project management tracking prompt for ChatGPT produces a comprehensive table breaking down each task into granular sub-tasks, comparing estimated time against actual time spent, documenting blockers and resource constraints, and analyzing discrepancies to reveal patterns. It runs on ChatGPT, Claude, Gemini, and Grok, delivering a structured tracking format plus actionable insights and concrete recommendations for improving future estimates. Use it when planning sprints, conducting retrospectives, or building historical data to benchmark team velocity and capacity. ● Breaks down each project task into sub-tasks with separate estimated and actual time columns for granular visibility ● Documents blockers, dependencies, and resource constraints alongside each task to contextualize delays and overruns ● Analyzes discrepancy patterns across all tasks to identify root causes like underestimated complexity or resource bottlenecks ● Generates 3-5 actionable recommendations for improving estimation accuracy on future projects based on historical performance data ## Prompt

```
## Role
You are an expert project manager skilled at estimating task durations, tracking project progress, and analyzing time discrepancies to improve future planning.

## Task
Create a comprehensive task duration tracking table that compares estimated vs. actual times, documents blockers and resource constraints, and provides actionable insights for refining future estimates.

## Context
Project: {{project-name}}
Deadline: {{project-deadline}}
Team size: {{team-size}}
Number of tasks to track: {{task-count}}

Break down each task into granular sub-tasks for accurate tracking. Factor in blockers, dependencies, and resource constraints when analyzing discrepancies between estimated and actual times.

## Output
Provide your response in this format:

### Task Duration Tracking Table

| Task | Sub-Tasks | Estimated Time | Actual Time | Blockers/Dependencies | Resources | Discrepancy Analysis |
|------|-----------|----------------|-------------|----------------------|-----------|----------------------|
| [Task name] | - [Subtask]<br>- [Subtask]<br>- [Subtask] | [Hours/days] | [Hours/days] | - [Blocker/dependency]<br>- [Blocker/dependency] | - [Resource]<br>- [Resource] | [Root cause analysis] |

(Repeat row for each task)

### Insights from Discrepancy Analysis
[Summarize patterns, recurring issues, and key learnings from comparing estimated vs. actual times across all tasks]

### Recommendations for Refining Estimates
[Provide 3-5 concrete, actionable recommendations for improving future task duration estimates based on the discrepancy patterns identified]
```

## 用法 / Usage
- 必填變數 / Variables: {{project-deadline}}、{{project-name}}、{{task-count}}、{{team-size}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Structured_Analytical_Decomposition
- 適用 / Use when: The Project Task Duration Tracking Table Generator is a free AI prompt that creates detailed time-tracking fra…

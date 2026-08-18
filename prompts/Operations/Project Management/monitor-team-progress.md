# Team Progress Monitoring Report Generator

## 簡介

The Team Progress Monitoring Report Generator is a free AI prompt that produces comprehensive project health reports for project managers tracking team performance and delivery timelines. This project management prompt for ChatGPT analyzes task completion status, team member workload distribution, timeline adherence, and identifies bottlenecks or blockers across your active work. It runs on ChatGPT, Claude, Gemini, and Grok, accepting three variables: your project name, team name, and the PM tool you use (Jira, Asana, Monday, Trello, or any other platform). The output is a clean markdown table with Task, Assignee, Due Date, and Status columns, followed by a summary of critical risks. Use it during sprint reviews, stakeholder updates, or weekly check-ins when you need visibility into what's on track, at risk, delayed, blocked, or complete. ● Outputs a markdown table showing all active tasks with assignee, due date, and clear status indicators ● Identifies bottlenecks, delays, and blockers to keep projects on schedule ● Includes a summary section flagging critical issues for leadership review ● Works with any project management tool by accepting the tool name as context ## Prompt

```
## Role
You are an expert project manager monitoring team progress and project health.

## Task
Analyze the current project status, identify potential bottlenecks or delays, and produce a comprehensive progress report that enhances transparency and facilitates decision-making.

## Context
**Project:** {{project-name}}
**Team:** {{team-name}}
**Tool in use:** {{pm-tool}}

Focus on:
- Task completion status
- Team member performance and workload
- Timeline adherence
- Risk identification (bottlenecks, delays, blockers)

## Output
Provide the progress report as a markdown table with exactly 4 columns:

| Task | Assignee | Due Date | Status |
|------|----------|----------|--------|

Include all active tasks. For the Status column, use clear indicators (e.g., On Track, At Risk, Delayed, Blocked, Complete). After the table, add a brief summary highlighting any critical issues or risks requiring attention.
```

## 用法 / Usage
- 必填變數 / Variables: {{pm-tool}}、{{project-name}}、{{team-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Strategic_Resource&Sprint_Prioritization
- 適用 / Use when: The Team Progress Monitoring Report Generator is a free AI prompt that produces comprehensive project health r…

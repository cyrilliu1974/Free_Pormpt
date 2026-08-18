# MoSCoW Task Prioritization Prompt for Projects

## 簡介

The MoSCoW Task Prioritization Prompt for Projects is a free AI prompt that categorizes project tasks into four priority tiers to help project managers and teams focus resources on what matters most. This MoSCoW prioritization prompt for ChatGPT takes your task list, project name, deadline, goals, and available resources, then distributes every task into MUST-HAVES (critical to success), SHOULD-HAVES (important but not vital), COULD-HAVES (desirable but not necessary), and WON'T-HAVES (out of scope). The output is a clean markdown table with justifications for non-obvious decisions, making it straightforward to communicate priorities across teams. It runs on ChatGPT, Claude, Gemini, and Grok, giving you flexibility to use whichever text model fits your workflow. Reach for this prompt whenever you need to triage a backlog, align stakeholders on scope, or transparently allocate limited time and budget against competing demands. ● Categorizes every task in your list into four tiers based on impact, deadline, resources, and goals. ● Outputs a markdown table that is easy to share in Slack, Notion, Jira, or any documentation tool. ● Provides brief justifications for borderline decisions so teams understand why tasks landed where they did. ● Adapts to any project type by accepting custom goals, deadlines, and resource constraints as variables. ## Prompt

```
## Role
You are a project management expert specializing in MoSCoW prioritization.

## Task
Categorize the tasks from {{task-list}} into four priority tiers using the MoSCoW method: MUST-HAVES (critical to success), SHOULD-HAVES (important but not vital), COULD-HAVES (desirable but not necessary), and WON'T-HAVES (out of scope for this iteration).

## Context
Project: {{project-name}}
Deadline: {{deadline}}
Goals: {{project-goals}}
Resources: {{available-resources}}

Analyze each task's impact on project success, considering the deadline, available resources, and stated goals. Provide brief justification for any non-obvious categorizations.

## Output
Present your prioritization as a markdown table with four columns (MUST-HAVES, SHOULD-HAVES, COULD-HAVES, WON'T-HAVES). List tasks under the appropriate column, ensuring all tasks are accounted for and properly distributed.
```

## 用法 / Usage
- 必填變數 / Variables: {{available-resources}}、{{deadline}}、{{project-goals}}、{{project-name}}、{{task-list}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The MoSCoW Task Prioritization Prompt for Projects is a free AI prompt that categorizes project tasks into fou…

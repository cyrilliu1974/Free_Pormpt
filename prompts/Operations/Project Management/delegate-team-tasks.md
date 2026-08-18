# Task Delegation Plan Generator for Project Teams

## 簡介

The Task Delegation Plan Generator for Project Teams is a free AI prompt that creates optimized task assignments by matching project requirements with team member capabilities and availability. This task delegation prompt for ChatGPT analyzes your project timeline, team roster (including roles, skills, and workload status), and task list to produce a complete delegation plan in markdown table format. It runs on ChatGPT, Claude, Gemini, and Grok, systematically evaluating each team member's expertise and capacity before assigning responsibilities with realistic deadlines. Real-world use cases include sprint planning, campaign launches, product releases, and cross-functional initiatives where balancing workload and expertise directly impacts delivery speed and quality. Project managers, team leads, and scrum masters reach for this prompt when they need to distribute work fairly across teams while respecting skill gaps and bandwidth constraints. ● Produces a markdown table mapping each task to the best-fit assignee with a deadline ● Considers skills, experience level, and current workload to prevent bottlenecks and burnout ● Includes a rationale section explaining critical assignments and load-balancing decisions ● Accepts flexible inputs for project timelines, team rosters, and task lists of any size ## Prompt

```
## Role
You are an expert project manager creating an optimized task delegation plan.

## Task
Analyze the project context and team capacity, then assign each task to the most suitable team member with realistic deadlines. Consider skills, experience, and current workload when matching responsibilities.

## Context
**Project & Timeline:**
{{project-and-timeline}}

**Team Members:**
{{team-roster}}
(For each member, include: name, role, key skills, and current workload status)

**Tasks to Delegate:**
{{task-list}}

## Output
Provide your delegation plan as a markdown table:

| Task | Assignee | Deadline |
|------|----------|----------|
| ... | ... | ... |

After the table, briefly explain any critical assignments or workload balancing decisions.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-and-timeline}}、{{task-list}}、{{team-roster}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Task Delegation Plan Generator for Project Teams is a free AI prompt that creates optimized task assignmen…

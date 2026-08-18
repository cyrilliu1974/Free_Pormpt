# Daily Task Prioritization Prompt for ChatGPT

## 簡介

The Daily Task Prioritization Prompt for ChatGPT is a free AI prompt that analyzes your to-do list and identifies the three highest-impact tasks achievable within your available hours. Instead of a vague productivity pep-talk, it delivers a concrete, prioritized checklist that connects each task to your stated daily goal and explains exactly why it matters. This task prioritization prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, applying dependency sequencing and time-realism filters so you focus on what will actually move the needle. Teams and solo professionals use it to cut through overloaded task lists, product managers rely on it to align sprint work with roadmap milestones, and busy executives turn to it when they need clarity on where the next four hours should go. ● Accepts your full to-do list, daily goal, and available working hours as input and returns exactly three ranked tasks. ● Explains the impact rationale for each task so you understand why it made the cut and how it supports your goal. ● Filters out low-value activities and applies task-dependency logic to prevent wasted effort. ● Designed for daily use - paste a fresh to-do list each morning and get a new prioritized plan in seconds. ## Prompt

```
## Role
You are a productivity expert specializing in task prioritization and time management.

## Task
Analyze the user's to-do list and identify the 3 most impactful tasks achievable within their available time. Provide a prioritized action plan for maximum results in one day.

## Context
Apply these prioritization criteria:
- Highest potential impact on results and long-term goals
- Realistic completion within the specified timeframe
- Task dependencies and sequencing
- Avoidance of low-value activities

**User Information:**
- To-do list: {{todo-list}}
- Main goal for the day: {{daily-goal}}
- Available working hours: {{available-time}}

## Output
Provide a prioritized checklist with exactly 3 tasks:

1. [High Priority] Task name: Brief explanation of why this task delivers maximum impact
2. [Medium Priority] Task name: Brief explanation of importance and contribution to the goal
3. [Low Priority] Task name: Brief explanation of value and why it ranks third

For each task, clearly connect the selection to the user's stated daily goal and explain the rationale.
```

## 用法 / Usage
- 必填變數 / Variables: {{available-time}}、{{daily-goal}}、{{todo-list}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Daily Task Prioritization Prompt for ChatGPT is a free AI prompt that analyzes your to-do list and identif…

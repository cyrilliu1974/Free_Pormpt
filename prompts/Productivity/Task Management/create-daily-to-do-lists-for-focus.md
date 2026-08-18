# Daily To-Do List Prioritization Prompt

## 簡介

The Daily To-Do List Prioritization Prompt is a free AI prompt that transforms your task list into a structured, priority-ordered action plan for busy professionals and knowledge workers. This task management prompt for ChatGPT analyzes your raw list of tasks, evaluates each item for significance and time-sensitivity, then outputs a markdown table with three columns: Task, Priority (High/Medium/Low), and Deadline. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across every major text-generation model. Real use cases include daily planning for remote teams, sprint planning for project managers, and focus-session prep for anyone managing competing deadlines. The prompt accepts a {{tasks-and-constraints}} variable where you describe your tasks, how you define importance versus urgency, your available time, and environmental factors like meetings or energy peaks. Reach for this prompt when you have a scattered list of to-dos and need an objective, systematic way to decide what comes first. ● Orders tasks in descending priority so the most critical work appears first ● Assigns High, Medium, or Low priority labels based on both urgency and importance ● Sets realistic deadlines for each task to keep you accountable ● Accepts context about meetings, dependencies, and energy levels for smarter scheduling ## Prompt

```
## Role
You are a productivity expert creating an efficient, prioritized daily to-do list.

## Task
Analyze the provided tasks and organize them into a clear, actionable priority table. For each task:

1. Evaluate significance and time-sensitivity
2. Assign a priority level (High/Medium/Low) based on importance and urgency
3. Set a realistic deadline
4. Order tasks by priority, most critical first

## Context
{{tasks-and-constraints}}

*Include: your list of tasks, how you define importance vs. urgency, available time today, and any work environment factors that affect scheduling (meetings, energy levels, dependencies, etc.)*

## Output
Deliver a markdown table with three columns:

| Task | Priority | Deadline |
|------|----------|----------|

List tasks in descending priority order.
```

## 用法 / Usage
- 必填變數 / Variables: {{tasks-and-constraints}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Daily To-Do List Prioritization Prompt is a free AI prompt that transforms your task list into a structure…

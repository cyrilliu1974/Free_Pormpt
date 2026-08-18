# Eisenhower Matrix Task Prioritization Prompt

## 簡介

The Eisenhower Matrix Task Prioritization Prompt is a free AI prompt that categorizes and organizes tasks by urgency and importance for professionals managing competing priorities. This Eisenhower Matrix prompt for ChatGPT analyzes your task list and sorts each item into one of four quadrants: Do First (urgent and important), Schedule (important but not urgent), Delegate (urgent but not important), or Don't Do (neither urgent nor important). The prompt evaluates each task's impact, time-sensitivity, and strategic alignment, then delivers a markdown table with all tasks organized by priority along with clear justifications for each placement. Whether you're a manager juggling project deadlines, a founder deciding where to focus, or a knowledge worker drowning in requests, this prompt transforms an overwhelming to-do list into an actionable plan. It runs on ChatGPT, Claude, Gemini, and Grok. ● Categorizes tasks into four Eisenhower Matrix quadrants based on urgency and importance ● Provides written justification for each task's placement to validate prioritization decisions ● Outputs a clean markdown table format that's easy to share with teams or reference throughout the day ● Helps distinguish between tasks that require immediate action versus those that can be scheduled, delegated, or eliminated ## Prompt

```
## Role
You are an expert task manager applying the Eisenhower Matrix to prioritize tasks based on urgency and importance.

## Task
Analyze the provided tasks and categorize each one into the appropriate Eisenhower Matrix quadrant. For each task, consider its impact, time-sensitivity, and alignment with stated priorities. Provide a brief justification explaining why each task belongs in its assigned category.

## Context
{{task-list}}

## Output
Present your analysis as a markdown table with four columns:

| Do First (urgent + important) | Schedule (important, not urgent) | Delegate (urgent, not important) | Don't Do (neither) |
|-------------------------------|----------------------------------|----------------------------------|--------------------|

Below the table, include a **Justification** section that briefly explains the placement rationale for each task.
```

## 用法 / Usage
- 必填變數 / Variables: {{task-list}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Eisenhower Matrix Task Prioritization Prompt is a free AI prompt that categorizes and organizes tasks by u…

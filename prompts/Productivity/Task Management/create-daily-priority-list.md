# Eisenhower Matrix Daily Priority List Generator

## 簡介

The Eisenhower Matrix Daily Priority List Generator is a free AI prompt that organizes any set of tasks into a structured, four-quadrant framework based on urgency and importance. This task management prompt for ChatGPT takes your raw list of tasks and a date, then categorizes each item into Quadrant 1 (Urgent & Important: do first), Quadrant 2 (Not Urgent but Important: schedule), Quadrant 3 (Urgent but Not Important: delegate), or Quadrant 4 (Not Urgent & Not Important: minimize). The AI acts as a productivity expert, delivering a markdown-formatted checklist with brief execution guidance for each quadrant. It runs on ChatGPT, Claude, Gemini, and Grok, making it easy to paste your daily task dump and receive a strategic action plan in seconds. Use it every morning to decide what deserves your focus, what to defer, and what to drop entirely. ● Automatically sorts tasks into the four Eisenhower Matrix quadrants with checkboxes and actionable labels. ● Provides contextual guidance for each quadrant explaining whether to do, schedule, delegate, or eliminate tasks. ● Outputs clean markdown formatting that integrates seamlessly into note-taking apps, project managers, or daily journals. ● Accepts any number of tasks and a date, making it flexible for daily planning, weekly reviews, or ad-hoc triage sessions. ## Prompt

```
## Role
You are a productivity expert organizing tasks using the Eisenhower Matrix to maximize effectiveness and time management.

## Task
Create a prioritized to-do list that categorizes the provided tasks into the four Eisenhower Matrix quadrants. For each quadrant, explain its priority level and provide actionable guidance on how to approach those tasks.

## Context
Date: {{date}}

Tasks to organize:
{{tasks}}

## Output
Format the to-do list as markdown with the following structure:

### Quadrant 1: Urgent & Important
- Brief explanation: Do these first—critical tasks requiring immediate attention
- [ ] Task items with checkboxes

### Quadrant 2: Not Urgent but Important
- Brief explanation: Schedule these—strategic tasks that drive long-term success
- [ ] Task items with checkboxes

### Quadrant 3: Urgent but Not Important
- Brief explanation: Delegate if possible—tasks that demand attention but don't advance key goals
- [ ] Task items with checkboxes

### Quadrant 4: Not Urgent & Not Important
- Brief explanation: Minimize or eliminate—low-value activities to avoid
- [ ] Task items with checkboxes

Include brief guidance after each quadrant on execution strategy.
```

## 用法 / Usage
- 必填變數 / Variables: {{date}}、{{tasks}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Eisenhower Matrix Daily Priority List Generator is a free AI prompt that organizes any set of tasks into a…

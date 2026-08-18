# Task Deadline Prioritization by Importance Prompt

## 簡介

The Task Deadline Prioritization by Importance Prompt is a free AI prompt that evaluates your tasks against custom importance and urgency criteria, then generates a structured schedule with specific deadlines. This task deadline prompt for ChatGPT helps you move from an unorganized task list to a clear, prioritized schedule. You provide your tasks with context, define what "importance" means for your work (business impact, strategic value, etc.), and define what "urgency" means (client deadlines, dependencies, time-sensitivity). The AI evaluates each item, assigns realistic deadlines, balances workload to avoid bottlenecks, and returns a markdown table showing task name, importance level, and specific deadline - along with a brief explanation of the prioritization method applied. It runs on ChatGPT, Claude, Gemini, and Grok, making it versatile for any text-generation workflow. Ideal for project managers juggling multiple deliverables, team leads coordinating sprints, or individual contributors who need to translate a chaotic to-do list into a time-bound action plan. ● Accepts fully customizable definitions of importance and urgency so the framework fits your domain - sales pipelines, software sprints, academic research, or personal projects. ● Outputs a clean markdown table (Task | Importance | Deadline) that you can paste into project management tools, wikis, or planning documents. ● Includes a 2-3 sentence rationale explaining the prioritization logic, so stakeholders understand why deadlines were assigned. ● Balances workload distribution to prevent scheduling conflicts and bottlenecks across your available time frame. ## Prompt

```
## Role
You are a task management expert specializing in prioritization frameworks and deadline setting.

## Task
Analyze the provided tasks and organize them into a structured prioritization system with assigned deadlines. Evaluate each task based on its importance and urgency, then create a clear schedule that optimizes productivity and time management.

## Context
**Tasks and constraints:**
{{tasks-and-context}}

**Prioritization criteria:**
- Importance: {{importance-definition}}
- Urgency: {{urgency-definition}}

## Process
1. Evaluate each task against the importance and urgency criteria
2. Assign deadlines that reflect both factors and fit within the available time frame
3. Balance the workload to prevent bottlenecks

## Output
Provide a brief explanation (2-3 sentences) of the prioritization method you applied, then present a markdown table with three columns:

| Task | Importance | Deadline |
|------|------------|----------|

Ensure deadlines are specific and realistic.
```

## 用法 / Usage
- 必填變數 / Variables: {{importance-definition}}、{{tasks-and-context}}、{{urgency-definition}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Task Deadline Prioritization by Importance Prompt is a free AI prompt that evaluates your tasks against cu…

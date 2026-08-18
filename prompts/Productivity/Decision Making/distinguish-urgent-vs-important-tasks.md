# Eisenhower Matrix Task Prioritization Prompt

## 簡介

The Eisenhower Matrix Task Prioritization Prompt is a free AI prompt that categorizes your tasks into four quadrants based on urgency and importance, then delivers actionable management strategies for each category. This Eisenhower Matrix prompt for ChatGPT analyzes your task inventory and organizes it into a four-quadrant markdown table: Urgent & Important tasks that need immediate attention, Important but Not Urgent work that drives long-term goals, Urgent but Not Important items to delegate, and Neither Urgent nor Important activities to eliminate. It runs on ChatGPT, Claude, Gemini, and Grok, producing a complete prioritization framework that includes quadrant-by-quadrant handling recommendations, time allocation strategies, and 3-4 productivity suggestions tailored to your specific workload distribution. Teams use it for sprint planning, managers apply it to delegate effectively, and individuals rely on it to break free from reactive work patterns. ● Categorizes every task into one of four Eisenhower Matrix quadrants with reasoning for each placement ● Provides specific management guidance for each quadrant, including whether to do, schedule, delegate, or eliminate ● Analyzes your overall task distribution and identifies patterns that create urgency-driven work ● Delivers 3-4 concrete productivity recommendations based on where your tasks actually fall in the matrix ## Prompt

```
## Role
You are a task management expert specializing in the Eisenhower Matrix prioritization framework.

## Task
Categorize and organize the user's tasks using the Eisenhower Matrix, then provide actionable management strategies for each quadrant.

## Context
The Eisenhower Matrix divides tasks into four quadrants based on urgency and importance:
- **Urgent & Important** (Do First): Critical tasks requiring immediate attention
- **Important, Not Urgent** (Schedule): Strategic work that drives long-term goals
- **Urgent, Not Important** (Delegate): Tasks demanding attention but not aligned with core objectives
- **Neither Urgent nor Important** (Eliminate): Low-value activities to minimize or remove

## Input
{{task-inventory}}

## Output
1. **Matrix Table**: Organize all tasks into a four-column markdown table with headers for each quadrant. Place each task in the appropriate column based on its urgency and importance relative to the stated goals and deadlines.

2. **Quadrant Management Guide**: For each quadrant, explain:
   - Why these tasks belong in this category
   - Recommended handling approach (immediate action, scheduling, delegation, elimination)
   - Time allocation strategy

3. **Productivity Recommendations**: Analyze the distribution of tasks across quadrants and provide 3-4 specific suggestions to optimize workload, reduce urgency-driven work, and align daily activities with stated goals.
```

## 用法 / Usage
- 必填變數 / Variables: {{task-inventory}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Eisenhower Matrix Task Prioritization Prompt is a free AI prompt that categorizes your tasks into four qua…

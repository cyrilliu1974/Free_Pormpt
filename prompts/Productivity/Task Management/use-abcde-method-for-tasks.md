# ABCDE Task Prioritization Method Prompt

## 簡介

The ABCDE Task Prioritization Method Prompt is a free AI prompt that categorizes tasks into five priority levels based on urgency, consequences, and delegation potential for anyone managing competing responsibilities. This task management prompt for ChatGPT analyzes your workload and sorts every item into A (must-do with serious consequences), B (important with mild consequences), C (nice-to-have with no consequences), D (delegate), or E (eliminate). You provide your task list along with context about deadlines, resources, and delegation options, and the AI returns a structured markdown table with justifications for each categorization. It runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for project managers, entrepreneurs, and teams that need transparent rationale behind priority decisions. Reach for this prompt when you have a long task list and need a rational framework to decide what deserves attention, what can wait, and what should never have been on your list in the first place. ● Categorizes tasks into five evidence-based priority levels (A through E) with reasoning for each placement ● Accounts for deadlines, resources, delegation options, and consequence severity in a single analysis ● Outputs a markdown table that clearly separates what you must do, should do, could do, should delegate, or should drop ● Provides justifications so you can explain priority decisions to stakeholders or revisit them as conditions change ## Prompt

```
## Role
You are a productivity expert specializing in task prioritization using the ABCDE method.

## Task
Analyze the provided tasks and categorize them into five priority levels:
- **A**: Must-do tasks with serious consequences if not completed
- **B**: Important tasks with mild consequences if not completed
- **C**: Nice-to-have tasks with no real consequences
- **D**: Tasks that can be delegated to others
- **E**: Tasks that can be eliminated entirely

For each task, provide a brief justification explaining its categorization based on the priorities, deadlines, available resources, and delegation options provided.

## Context
{{task-and-context}}

Include:
- The full list of tasks to categorize
- Your current priorities and goals
- Relevant deadlines
- Available resources (time, budget, tools, team)
- Delegation options (who can take on which types of work)

## Output
Present your analysis as a markdown table with five columns (A, B, C, D, E). Each cell should contain:
- The task name
- A concise justification for its categorization

Format:
```
| A (Must Do) | B (Should Do) | C (Nice to Have) | D (Delegate) | E (Eliminate) |
|-------------|---------------|------------------|--------------|---------------|
| Task + why | Task + why | Task + why | Task + why | Task + why |
```
```

## 用法 / Usage
- 必填變數 / Variables: {{task-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The ABCDE Task Prioritization Method Prompt is a free AI prompt that categorizes tasks into five priority leve…

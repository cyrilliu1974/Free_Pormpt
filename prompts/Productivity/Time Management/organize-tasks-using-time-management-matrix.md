# Eisenhower Matrix Task Organizer for Time Management

## 簡介

The Eisenhower Matrix Task Organizer for Time Management is a free AI prompt that categorizes your tasks into a proven priority framework and delivers specific action strategies for professionals managing complex workloads. This time management prompt for ChatGPT analyzes each task against two dimensions - urgency (time sensitivity) and importance (impact on goals) - then sorts them into the classic four-quadrant Eisenhower Matrix: Urgent & Important (do first), Not Urgent but Important (schedule), Urgent but Not Important (delegate or minimize), and Not Urgent & Not Important (eliminate or defer). The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing a markdown table with all tasks distributed across quadrants, plus bulleted recommendations covering scheduling tactics, delegation opportunities, and elimination candidates. Real use cases include sprint planning for product teams, daily workload triage for executives, and student assignment prioritization. Reach for this prompt when you need to transform a chaotic task list into a clear action plan that separates what truly matters from what only feels urgent. ● Sorts tasks into four quadrants using urgency and importance as evaluation criteria ● Explains the rationale behind non-obvious task placements so you understand the logic ● Recommends concrete scheduling, delegation, and elimination strategies for each category ● Outputs a clean markdown table followed by a bulleted action list you can implement immediately ## Prompt

```
## Role
You are an expert time management consultant specializing in priority matrix frameworks.

## Task
Categorize the provided tasks into an Eisenhower Matrix (four-quadrant priority framework) and deliver actionable task management recommendations.

## Context
User context and constraints:
{{context}}

Tasks to organize:
{{tasks}}

## Process
1. Analyze each task against urgency (time sensitivity) and importance (impact on goals)
2. Assign each task to the appropriate quadrant:
   - **Urgent & Important**: Do first
   - **Not Urgent but Important**: Schedule
   - **Urgent but Not Important**: Delegate or minimize
   - **Not Urgent & Not Important**: Eliminate or defer
3. Explain placement rationale for any non-obvious categorizations
4. Recommend specific strategies: scheduling tactics, delegation opportunities, elimination candidates

## Output
Deliver a markdown table with four columns (one per quadrant), tasks distributed accordingly, followed by your management recommendations in bulleted list format.
```

## 用法 / Usage
- 必填變數 / Variables: {{context}}、{{tasks}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Eisenhower Matrix Task Organizer for Time Management is a free AI prompt that categorizes your tasks into …

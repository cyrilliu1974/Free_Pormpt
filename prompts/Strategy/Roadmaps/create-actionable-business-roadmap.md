# 12-Week Business Roadmap Generator

## 簡介

The 12-Week Business Roadmap Generator is a free AI prompt that reverse-engineers any 3-month business goal into two alternative strategic roadmaps with quantifiable weekly KPIs and calendar-ready actions. This business roadmap prompt for ChatGPT takes a single goal and context statement, then produces two complete 12-week plans - each with a different strategic approach. Every week within the roadmap includes specific, measurable actions that can be scheduled directly into a calendar, complete with time estimates and quantifiable targets. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and includes validation logic that rejects vague goals, ensuring every output contains actionable, measurable steps. Founders, product managers, and solo entrepreneurs use it to turn high-level objectives into day-by-day execution plans that track progress through clear KPIs. ● Produces two complete roadmaps with different strategic approaches, giving you flexibility in execution. ● Breaks each month into weekly goals with quantifiable actions, time estimates, and measurable targets. ● Rejects vague inputs and prompts you to refine goals into specific, action-oriented statements. ● Outputs calendar-ready tasks that can be scheduled immediately into project management or calendar tools. ## Prompt

```
## Role
You are an expert business strategist building a 12-week actionable roadmap to achieve a 3-month business goal.

## Task
Reverse-engineer the user's goal into two alternative 3-month roadmaps with quantifiable weekly KPIs and calendar-ready actions.

**If the goal is vague or unmeasurable, respond only with:** "Retry with a quantifiable and action-oriented goal. You can do this!"

## Context
**Goal and business context:**  
{{goal-and-context}}

## Output
For each roadmap, structure as follows:

# Month X: [BIG GOAL OF MONTH X]
● Summarize the month's goal and KPIs

## Week X: [BIG GOAL OF WEEK X]
● List specific, quantifiable weekly actions the user can schedule (include time estimates, quantities, or measurable targets)

Repeat for all 12 weeks across 3 months. Provide two complete roadmaps with different strategic approaches.
```

## 用法 / Usage
- 必填變數 / Variables: {{goal-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The 12-Week Business Roadmap Generator is a free AI prompt that reverse-engineers any 3-month business goal in…

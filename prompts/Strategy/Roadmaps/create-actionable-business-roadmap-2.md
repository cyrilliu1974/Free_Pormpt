# 12-Week Business Roadmap Generator

## 簡介

The 12-Week Business Roadmap Generator is a free AI prompt that reverse-engineers 3-month business goals into structured, actionable execution plans for entrepreneurs and strategists. This business roadmap prompt for ChatGPT takes any quarterly objective and breaks it down into three monthly themes, each divided into four weekly milestones with specific, quantifiable actions. It validates that your goal is measurable and action-oriented before building the plan, then delivers calendar-ready tasks with clear KPIs for every week. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across major text AI platforms. Use it when you need to transform ambitious quarterly targets into daily and weekly tasks that can be scheduled, tracked, and executed without ambiguity. ● Validates goal clarity upfront and prompts you to refine vague objectives into quantifiable targets ● Organizes 12 weeks into three monthly themes, each with four weekly milestones and specific actions ● Produces calendar-friendly tasks you can immediately schedule in your project management or calendar tool ● Ensures every action and KPI is measurable, enabling consistent progress tracking and adjustment ## Prompt

```
## Role
You are an expert business strategist specializing in goal decomposition and execution planning.

## Task
Reverse-engineer the provided 3-month goal into a detailed, actionable 12-week roadmap. Break the goal into monthly themes and weekly milestones, each with specific, quantifiable actions.

## Context
**3-month goal and context:**
{{goal-and-context}}

## Requirements
- First, validate the goal is action-oriented and quantifiable. If not, respond with: "Retry with a quantifiable and action-oriented goal. You can do this!" and stop.
- Each week must include specific, measurable, achievable actions that build toward the overall objective.
- All KPIs and actions must be quantifiable.
- Weekly actions should be calendar-friendly (suitable for scheduling).

## Output
Provide a 12-week roadmap using this structure:

# Month 1: [Monthly Goal]
Summarize the month's objective and key KPIs

## Week 1: [Weekly Goal]
List specific, quantified actions to achieve this week's goal (calendar-ready format)

## Week 2: [Weekly Goal]
List specific, quantified actions to achieve this week's goal (calendar-ready format)

## Week 3: [Weekly Goal]
List specific, quantified actions to achieve this week's goal (calendar-ready format)

## Week 4: [Weekly Goal]
List specific, quantified actions to achieve this week's goal (calendar-ready format)

*Repeat the Month + 4 Weeks structure for Month 2 and Month 3*
```

## 用法 / Usage
- 必填變數 / Variables: {{goal-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The 12-Week Business Roadmap Generator is a free AI prompt that reverse-engineers 3-month business goals into …

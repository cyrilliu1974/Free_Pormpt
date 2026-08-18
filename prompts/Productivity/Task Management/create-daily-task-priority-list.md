# Daily Task Priority List Prompt for Goal Alignment

## 簡介

The Daily Task Priority List Prompt for Goal Alignment is a free AI prompt that builds a focused, prioritized daily plan based on your personal goals, available time, and energy patterns. This task management prompt for ChatGPT analyzes your stated goals, values, and current priorities to produce a markdown table of 5-8 ranked tasks, each with a priority level (High/Medium/Low) and realistic time estimate. It sequences work to match your energy peaks - scheduling high-impact activities when you're most alert - and ensures the total workload fits your available hours. Use it when you need to turn a scattered to-do list into a strategic daily plan that advances what matters most. The prompt runs on ChatGPT, Claude, Gemini, and Grok, requiring three inputs: your goals and values, your available time and energy windows, and your current priorities. ● Filters tasks by alignment with personal goals and core values ● Ranks by both impact and urgency, not just deadline pressure ● Estimates realistic time per task to prevent over-commitment ● Sequences activities to match natural energy rhythms throughout the day ## Prompt

```
## Role
You are an expert productivity coach specializing in goal-aligned task planning.

## Task
Create a prioritized daily task list that maximizes impact within the user's available time and energy patterns.

## Context
Analyze the information below to understand what matters most to the user:

**Goals & Values:**
{{goals-and-values}}

**Available Time & Energy:**
{{time-and-energy}}

**Current Priorities:**
{{current-priorities}}

## Process
1. Identify tasks that directly advance the stated goals and align with values
2. Prioritize by impact and urgency (High/Medium/Low)
3. Estimate realistic time requirements for each task
4. Sequence tasks to match energy patterns (high-energy work during peak periods)
5. Ensure the total time fits within available hours

## Output
Provide the task list as a markdown table with three columns:

| Priority Level | Task | Estimated Time |
|----------------|------|----------------|

Include 5-8 tasks that together form a focused, achievable daily plan.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-priorities}}、{{goals-and-values}}、{{time-and-energy}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Daily Task Priority List Prompt for Goal Alignment is a free AI prompt that builds a focused, prioritized …

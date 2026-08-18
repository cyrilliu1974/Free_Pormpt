# Pomodoro Technique Schedule Builder for ChatGPT

## 簡介

The Pomodoro Technique Schedule Builder is a free AI prompt that creates a complete time-blocked schedule using the Pomodoro method for anyone managing tasks and deadlines. This Pomodoro technique prompt for ChatGPT analyzes your list of tasks and work context, then builds a structured schedule that assigns each task a specific number of 25-minute Pomodoros, calculates break durations (5 minutes between sessions, 15-30 minutes after every fourth), and totals the time required. It delivers both a markdown table showing task breakdown and an implementation guide with execution tips, focus strategies, and context-specific advice. The prompt runs on ChatGPT, Claude, and Gemini, making it accessible across the major text-model platforms. Reach for this prompt when you need to transform an overwhelming task list into a disciplined, time-boxed plan that prevents burnout and maintains concentration throughout your workday. ● Calculates exact Pomodoro counts per task based on complexity and scope ● Automatically assigns 5-minute breaks between sessions and longer 15-30 minute breaks after every fourth Pomodoro ● Outputs a markdown table showing task, Pomodoro count, break duration, and total time ● Includes implementation guidance tailored to your specific work environment and productivity goals ## Prompt

```
## Role
You are a productivity expert specializing in time-blocking and focus techniques.

## Task
Create a structured Pomodoro Technique schedule that breaks down the user's tasks into focused 25-minute work sessions (Pomodoros) with appropriate breaks. Analyze the tasks provided, determine how many Pomodoros each requires, assign break durations (5 minutes after each Pomodoro, 15-30 minutes after every fourth), and calculate total time needed.

## Context
User's situation:
{{work-context}}

Tasks to schedule:
{{tasks}}

## Output
Provide your response in two parts:

1. **Pomodoro Schedule Table** (markdown format) with columns:
   - Task
   - Pomodoro Count
   - Break Duration
   - Total Time

2. **Implementation Guide** (3-4 concise points) explaining:
   - How to execute each Pomodoro session
   - When to take breaks and why the timing matters
   - Tips for maintaining focus given the user's specific work context
   - How this schedule aligns with their stated productivity goals
```

## 用法 / Usage
- 必填變數 / Variables: {{tasks}}、{{work-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Pomodoro Technique Schedule Builder is a free AI prompt that creates a complete time-blocked schedule usin…

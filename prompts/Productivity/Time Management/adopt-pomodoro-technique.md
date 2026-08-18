# Pomodoro Technique Schedule Builder for ChatGPT

## 簡介

The Pomodoro Technique Schedule Builder is a free AI prompt that creates customized time-management plans breaking work into focused intervals with strategic rest periods for students, remote workers, and anyone seeking structured productivity. This Pomodoro technique prompt for ChatGPT analyzes your session preferences - work interval length, break duration, desired cycles - and your specific tasks and environment to build a structured schedule. It explains the core Pomodoro method, then organizes your workload into manageable chunks presented as a markdown table showing each task, its Pomodoro interval, break duration, and cycle count. The prompt works across ChatGPT, Claude, and Gemini, delivering context-aware tips for maintaining strict focus during work periods and fully disconnecting during breaks. Reach for this prompt when you need to transform an overwhelming task list into a disciplined, time-boxed plan that prevents burnout while maintaining high concentration. ● Breaks down tasks into Pomodoro-sized work intervals tailored to your concentration span ● Sequences work periods and breaks in a clear markdown table format ● Provides environment-specific tips for maintaining focus and ensuring complete mental rest ● Adapts the classic Pomodoro system to your unique workflow, task load, and workspace conditions ## Prompt

```
## Role
You are a Pomodoro Technique expert designing a structured, productivity-focused time management plan.

## Task
Create a personalized Pomodoro schedule that breaks down the user's work into focused intervals with strategic breaks. Organize the plan to maximize concentration during work periods and ensure complete mental rest during breaks.

## Context
The user needs help applying the Pomodoro Technique to their specific work situation:
- **Session parameters:** {{session-config}} (work interval length, break duration, number of cycles desired)
- **Tasks and environment:** {{work-context}} (main tasks to accomplish, work environment characteristics)

Briefly explain the Pomodoro Technique, then guide the user through:
- Breaking down their tasks into manageable Pomodoro-sized chunks
- Sequencing work intervals and breaks effectively
- Maintaining strict focus during work periods
- Fully disconnecting during rest periods
- Adjusting the system to their environment

## Output
Present the plan as a markdown table with columns:
- **Task** (what to work on)
- **Pomodoro Interval** (work duration)
- **Break Duration** (rest period)
- **Cycles** (repetitions)

Below the table, provide 3-5 targeted tips for success based on their specific work context and environment.
```

## 用法 / Usage
- 必填變數 / Variables: {{session-config}}、{{work-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Pomodoro Technique Schedule Builder is a free AI prompt that creates customized time-management plans brea…

# Learning Schedule Generator for Structured Study Plans

## 簡介

The Learning Schedule Generator for Structured Study Plans is a free AI prompt that creates personalized, week-by-week study schedules for any subject based on your timeframe, skill level, learning style, and available hours. This learning schedule prompt for ChatGPT accepts five variables - subject, timeframe, skill level, learning style, and study hours per week - and outputs a comprehensive markdown table mapping each week to specific learning activities, curated resources, and time allocations. The prompt balances active and passive learning techniques, schedules regular review sessions and self-assessment checkpoints, and distributes study time evenly while building in flexibility for individual pacing. It runs on ChatGPT, Claude, Gemini, and Grok. Use it when planning a course of self-study, preparing for an exam, or teaching a student who needs a structured roadmap. ● Breaks complex subjects into progressive topics and subtopics that build logically on each other. ● Assigns diverse learning activities - readings, exercises, projects, reviews - matched to the learner's preferred style. ● Recommends specific resources for each week and allocates time based on topic complexity and importance. ● Includes review sessions and self-assessment checkpoints at appropriate intervals to reinforce retention. ## Prompt

```
## Role
You are an expert educational planner designing personalized learning schedules.

## Task
Create a comprehensive learning plan for {{subject}} optimized for {{timeframe}}. Break the subject into progressive topics and subtopics, assign appropriate learning activities with specific resources, and allocate time based on complexity and importance. Balance active and passive learning techniques, include regular review sessions and self-assessment checkpoints, and build in flexibility for varying learning paces.

## Context
Current skill level: {{skill-level}}
Preferred learning style: {{learning-style}}
Available study hours per week: {{study-hours-per-week}}

## Output
Provide a brief introduction (2-3 paragraphs) explaining the overall structure, learning approach, and how the schedule accommodates the specified constraints.

Then present the schedule as a markdown table:

| Week | Learning Activities | Resources | Time Allocation |
|------|---------------------|-----------|------------------|

Ensure the plan distributes study time evenly across the timeframe and includes review sessions at appropriate intervals.
```

## 用法 / Usage
- 必填變數 / Variables: {{learning-style}}、{{skill-level}}、{{study-hours-per-week}}、{{subject}}、{{timeframe}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Learning Schedule Generator for Structured Study Plans is a free AI prompt that creates personalized, week…

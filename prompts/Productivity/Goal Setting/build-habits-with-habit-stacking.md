# Habit Stacking Routine Builder for Productivity

## 簡介

The Habit Stacking Routine Builder for Productivity is a free AI prompt that designs a custom habit formation plan anchored to your existing daily routine and preferred productivity method. This habit stacking prompt for ChatGPT analyzes your chosen productivity framework - whether GTD, Pomodoro, Time Blocking, or another system - and identifies key behaviors that compound on each other throughout your day. It assigns natural trigger points already present in your routine (like "after I pour my morning coffee" or "when I close my laptop at 5 PM") and pairs each habit with a meaningful reward that reinforces completion. The prompt works across ChatGPT, Claude, Gemini, and Grok, delivering both an implementation guide and a structured table mapping habits to triggers and rewards. Use it when you want to build multiple new habits without relying on willpower alone, or when previous attempts at behavior change have failed because new routines felt disconnected from your day. ● Anchors new habits to existing daily behaviors, eliminating the need to remember arbitrary schedules ● Matches rewards to individual motivations for immediate positive reinforcement after each habit ● Aligns habit selection with your productivity method's core principles for coherent routines ● Outputs an actionable markdown table and implementation guide you can start using today ## Prompt

```
## Role
You are a productivity expert designing a personalized habit stacking routine.

## Task
Create a comprehensive habit stacking plan that:
- Identifies key habits aligned with the specified productivity method
- Assigns clear triggers that fit naturally into the user's existing daily routine
- Suggests meaningful rewards that reinforce habit completion
- Delivers an actionable implementation guide

## Context
**Productivity method:** {{productivity-method}}
**Daily routine and goals:** {{daily-routine-and-goals}}
**Number of habits to design:** {{number-of-habits}}

Analyze the productivity method's core principles, then design habits that compound on each other using natural trigger points already present in the user's day. Select rewards that match their motivations and are immediately available after habit completion.

## Output
Provide:
1. A brief explanation (3-4 sentences) of how to implement this habit stacking routine
2. A markdown table with three columns: **Habit** | **Trigger** | **Reward**

Each row should describe one complete habit stack with a specific behavioral trigger and an intrinsic or extrinsic reward the user finds motivating.
```

## 用法 / Usage
- 必填變數 / Variables: {{daily-routine-and-goals}}、{{number-of-habits}}、{{productivity-method}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Habit Stacking Routine Builder for Productivity is a free AI prompt that designs a custom habit formation …

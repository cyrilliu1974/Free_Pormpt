# RescueTime Productivity Analysis & Planning Prompt

## 簡介

The RescueTime Productivity Analysis & Planning Prompt is a free AI prompt that guides users through data-driven productivity optimization using RescueTime's time-tracking insights. This productivity prompt for ChatGPT walks you through five structured phases: installing and configuring RescueTime for your work environment, collecting and interpreting your productivity metrics, setting evidence-based goals, implementing tailored strategies, and establishing ongoing review cycles. It translates RescueTime data - productive time percentages, distraction patterns, and focus time trends - into concrete action steps aligned with your specific work style and existing productivity tools. Whether you're setting up time tracking for the first time or looking to extract more value from your RescueTime dashboard, the prompt delivers numbered instructions with clear headings that explain what to look for at each stage. It runs on ChatGPT, Claude, Gemini, and Grok. ● Provides concrete instructions for RescueTime setup, metric interpretation, and goal alignment based on your current work context ● Explains how to identify top distractions, productive time patterns, and focus windows from your dashboard data ● Delivers a structured five-phase plan covering setup, analysis, goal setting, strategy implementation, and regular review cycles ● Integrates recommendations with your existing productivity tools and emphasizes weekly check-ins and monthly adjustments ## Prompt

```
## Role
You are a productivity expert optimizing personal workflow through data-driven insights.

## Task
Guide the user through installing and configuring RescueTime, analyzing their productivity data, and creating a personalized productivity plan. Provide clear instructions for each phase: setup, data analysis, goal setting, and strategy implementation.

## Context
**Current situation:**
{{productivity-context}}

**Desired outcomes:**
{{productivity-goals}}

## Approach
- Offer specific insights on interpreting RescueTime metrics (productive time %, top distractions, focus time patterns)
- Translate data into actionable improvements tailored to the user's work style
- Emphasize regular review cycles (weekly check-ins, monthly plan adjustments) based on ongoing data
- Integrate recommendations with the user's existing productivity tools where relevant

## Output
Deliver your guidance as a numbered list with clear headings for each major step:
1. **Setup & Configuration**
2. **Data Collection & Initial Analysis**
3. **Goal Setting**
4. **Strategy Implementation**
5. **Review & Adjustment Process**

For each step, provide concrete instructions and explain what the user should look for in their data.
```

## 用法 / Usage
- 必填變數 / Variables: {{productivity-context}}、{{productivity-goals}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The RescueTime Productivity Analysis & Planning Prompt is a free AI prompt that guides users through data-driv…

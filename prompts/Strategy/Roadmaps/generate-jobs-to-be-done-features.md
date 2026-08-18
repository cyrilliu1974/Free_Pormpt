# Jobs-To-Be-Done Feature Generator

## 簡介

The Jobs-To-Be-Done Feature Generator is a free AI prompt that uncovers user motivations and translates them into feature ideas by focusing on the progress users want to make in specific circumstances. This jobs-to-be-done prompt for ChatGPT applies Clayton Christensen's framework to identify the core job your app is hired to do, map the functional, emotional, and social dimensions of user needs, and generate feature recommendations tied to real pain points. It structures output into four sections: a jobs analysis that defines the core job, triggering circumstances, and desired outcomes; a progress map showing the user journey; a pain-point assessment highlighting friction; and feature recommendations that explicitly connect each idea to the job it solves, the circumstances where it helps, and the progress it enables. Product managers use it to move beyond demographic assumptions and surface-level requests when planning roadmaps. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to validate feature ideas against actual user jobs or translate qualitative research into a prioritized backlog. ● Maps functional, emotional, and social jobs users hire your app to accomplish ● Identifies friction points blocking users from making progress toward desired outcomes ● Connects every feature recommendation to a specific job, circumstance, and outcome ● Structures analysis into four clear sections: jobs analysis, progress mapping, pain assessment, and feature ideas ## Prompt

```
## Role
You are an expert product strategist specializing in the Jobs-to-be-Done framework. You help companies uncover user motivations and translate them into breakthrough features by focusing on the progress users want to make, not demographics or surface requests.

## Task
Generate innovative feature ideas that directly address real user jobs and pain points using Clayton Christensen's Jobs-to-be-Done methodology. Remember: customers don't buy products—they hire them to make progress in specific circumstances.

## Context
Analyze the following app:

{{app-context}}

Consider the core job the app is hired to do and the circumstances that trigger this need; functional jobs (what users accomplish), emotional jobs (how they want to feel), and social jobs (how they want to be perceived); current friction points blocking users from making progress; and the desired outcomes that define success for users.

## Output
Structure your response with these sections:

**Jobs-to-be-Done Analysis**
Identify the core job, triggering circumstances, and desired outcomes.

**User Progress Mapping**
Map the journey users take toward their desired progress.

**Pain Point Assessment**
Highlight current friction and struggles blocking progress.

**Feature Recommendations**
Present feature ideas as bullet points, each explicitly connected to:
- The specific user job it addresses
- The circumstances where it helps
- The progress it enables

Ensure every feature recommendation ties directly to user jobs, not assumptions.
```

## 用法 / Usage
- 必填變數 / Variables: {{app-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Jobs-To-Be-Done Feature Generator is a free AI prompt that uncovers user motivations and translates them i…

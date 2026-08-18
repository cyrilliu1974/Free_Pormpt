# Employee Upskilling Plan Generator

## 簡介

The Employee Upskilling Plan Generator is a free AI prompt that creates tailored professional development strategies for employees seeking career advancement or transitions. This upskilling plan prompt for ChatGPT analyzes the gap between an employee's current position and target capabilities, identifies priority skills, matches them to effective learning resources, and sequences them into a realistic timeline table. It produces a markdown-formatted plan that includes skill priorities, specific learning resources (courses, platforms, internal programs), and a phased timeline that respects workload constraints and learning capacity. Use it when planning career development for direct reports, designing training programs, or building personal growth roadmaps that balance ambition with practical constraints. The prompt runs on ChatGPT, Claude, and Gemini. ● Identifies skill gaps between current roles and career targets, prioritizing what to learn first. ● Matches each skill to specific learning resources, considering budget, time, and platform access. ● Outputs a clean markdown table showing skills, resources, and timelines in one view. ● Includes implementation guidance and progress checkpoints to keep plans achievable alongside daily work. ## Prompt

```
## Role
You are an expert career development specialist designing upskilling plans that balance ambition with practical constraints.

## Task
Create a comprehensive professional development strategy for an employee seeking to advance or transition in their career. Analyze the gap between their current position and target capabilities, identify priority skills, match them to effective learning resources, and sequence them into a realistic timeline.

## Context
{{employee-profile}}

Include: current role, desired field or skill direction, time frame available for upskilling, accessible learning resources (internal programs, online platforms, budget constraints), and any relevant workload or capacity considerations.

## Output
Provide a brief introduction (2-3 sentences) contextualizing the plan for this employee's situation.

Then present the upskilling plan as a markdown table:

| Skill | Learning Resource | Timeline |
|-------|-------------------|----------|

Follow with a concluding paragraph addressing implementation strategy, motivation tips, or progress checkpoints to ensure the plan remains achievable alongside current responsibilities.
```

## 用法 / Usage
- 必填變數 / Variables: {{employee-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Employee Upskilling Plan Generator is a free AI prompt that creates tailored professional development stra…

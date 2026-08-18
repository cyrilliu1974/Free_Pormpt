# Adult Learning Roadmap Builder Prompt

## 簡介

The Adult Learning Roadmap Builder Prompt is a free AI prompt that creates progressive, personalized skill-development plans for adult learners in any field. This adult learning roadmap prompt for ChatGPT takes a learner's background, current skill level, available time, and learning style, then outputs a multi-stage plan as a clean markdown table. Each stage includes specific learning objectives, concrete resources (courses, books, projects, tools), and measurable milestones to track progress. It runs on ChatGPT, Claude, Gemini, and Grok, and is designed for educational consultants, career coaches, and L&D professionals who need realistic plans that respect adult learners' busy schedules and varied commitments. ● Structures learning in sequential stages from foundation to advanced competency, tailored to the learner's current level and field. ● Defines measurable objectives and practical resources for each stage, ensuring learners know exactly what to study and how to validate progress. ● Balances ambition with realism, accounting for time constraints and preferred learning styles of working adults. ● Outputs a clean markdown table (Stage | Learning Objectives | Resources | Milestones) that is easy to share, track, and adjust. ## Prompt

```
## Role
You are an educational consultant specializing in adult learning pathways and skill development.

## Task
Design a structured learning roadmap that guides an adult learner through progressive stages of skill acquisition in their chosen field. The roadmap must account for the learner's current level, available time, and how they learn best.

## Context
{{learner-and-field-context}}
(Include: the learner's background/persona, field of study, current skill level, desired timeframe, and preferred learning style)

## Requirements
- Structure the roadmap in clear, sequential stages from foundation to advanced competency
- Define specific, measurable learning objectives for each stage
- Recommend concrete resources (courses, books, projects, tools) appropriate to the field
- Establish milestones that allow the learner to track and validate progress
- Ensure the plan is realistic for adult learners balancing other commitments
- Align with current industry standards and best practices in the field

## Output
Present the roadmap as a markdown table with 4 columns:

| Stage | Learning Objectives | Resources | Milestones |
|-------|-------------------|-----------|------------|
| ... | ... | ... | ... |
```

## 用法 / Usage
- 必填變數 / Variables: {{learner-and-field-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Adult Learning Roadmap Builder Prompt is a free AI prompt that creates progressive, personalized skill-dev…

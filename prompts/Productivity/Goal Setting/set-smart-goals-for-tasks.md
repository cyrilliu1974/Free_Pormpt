# SMART Goal Setting Prompt for Task Management

## 簡介

The SMART Goal Setting Prompt for Task Management is a free AI prompt that converts any list of tasks into prioritized SMART goals aligned with your objectives and constraints. Built for productivity experts and project managers, this SMART goal prompt for ChatGPT analyzes task complexity, urgency, and alignment before generating specific, measurable, achievable, relevant, and time-bound goal statements. It runs on ChatGPT, Claude, Gemini, and Grok, producing a clean markdown table with each goal, its deadline, and a High/Medium/Low priority rating. The prompt evaluates available resources, dependencies, and overall project timeframes to ensure every goal is realistic and actionable. Use it when you need to organize scattered tasks, align work with strategic objectives, or build a prioritized roadmap that balances impact and urgency. ● Analyzes each task against main objectives, available resources, and constraints to ensure achievability ● Generates SMART goal statements that are specific, measurable, and time-bound, not abstract intentions ● Assigns priority levels based on impact and urgency, making it easy to focus on what matters most ● Outputs a markdown table format ready to paste into project management tools, documentation, or planning sessions ## Prompt

```
## Role
You are a productivity expert specializing in goal-setting and task management.

## Task
Transform the provided tasks into SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound) that optimize productivity and enable effective prioritization.

## Context
Analyze each task considering:
- Complexity and scope
- Importance relative to main objectives
- Urgency and dependencies
- Available resources and constraints

Ensure each goal is:
- **Specific**: Clear and well-defined
- **Measurable**: Quantifiable success criteria
- **Achievable**: Realistic given the resources and constraints
- **Relevant**: Aligned with the main objectives
- **Time-bound**: Has a concrete deadline

Assign priority levels (High/Medium/Low) based on impact and urgency.

## Input
**Tasks**: {{tasks}}

**Overall timeframe**: {{timeframe}}

**Main objectives**: {{main-objectives}}

**Available resources**: {{available-resources}}

**Constraints**: {{constraints}}

## Output
Present your analysis as a markdown table with three columns:

| Goal | Timeframe | Priority |
|------|-----------|----------|
| [SMART goal statement] | [Specific deadline] | [High/Medium/Low] |
```

## 用法 / Usage
- 必填變數 / Variables: {{available-resources}}、{{constraints}}、{{main-objectives}}、{{tasks}}、{{timeframe}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SMART Goal Setting Prompt for Task Management is a free AI prompt that converts any list of tasks into pri…

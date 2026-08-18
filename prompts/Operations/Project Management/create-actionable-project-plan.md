# Project Plan Action Steps Builder

## 簡介

The Project Plan Action Steps Builder is a free AI prompt that transforms high-level project goals into granular, trackable action plans for project managers and team leads. This project management prompt for ChatGPT creates a four-column markdown table that organizes any project into four major goals, each with bulleted action steps, assigned deadlines, and progress indicators. It works across ChatGPT, Claude, Gemini, and Grok by accepting a project name variable and applying expert project management methodology to break abstract objectives into concrete, measurable tasks. Teams use it to launch new products, coordinate cross-functional initiatives, plan marketing campaigns, and structure software development cycles with clear accountability at every stage. Reach for this prompt when you need to move from vision to execution - when stakeholders have agreed on outcomes but the path forward remains unclear. ● Converts four high-level project goals into granular, measurable action steps presented in a clean markdown table format. ● Assigns realistic deadlines for each goal based on scope and complexity, helping teams sequence work and manage dependencies. ● Embeds progress tracking mechanisms - percentage complete or status indicators - so stakeholders can monitor momentum at a glance. ● Outputs a structured, shareable document that serves as both a roadmap and a communication tool for distributed teams. ## Prompt

```
## Role
You are an expert project manager who breaks down projects into actionable steps, milestones, and progress tracking mechanisms.

## Task
Create a comprehensive project plan table that transforms high-level goals into granular, measurable action steps with realistic deadlines and progress indicators.

## Context
Project: {{project-name}}

## Requirements
1. Break down each high-level goal into specific, measurable action steps
2. Assign realistic deadlines based on project scope and complexity
3. Include progress tracking mechanisms (percentage complete or completion status)
4. Cover all key aspects of the project across 4 major goals

## Output
Return a markdown table with 4 columns: Goal | Action Steps | Deadline | Progress

Include 4 rows, one for each high-level goal. Format action steps as bulleted lists within table cells. Example structure:

| Goal | Action Steps | Deadline | Progress |
|------|--------------|----------|----------|
| [Goal 1] | • [Action step 1]<br>• [Action step 2]<br>• [Action step 3] | [Date] | [%] |
| [Goal 2] | • [Action step 1]<br>• [Action step 2]<br>• [Action step 3] | [Date] | [%] |
| [Goal 3] | • [Action step 1]<br>• [Action step 2]<br>• [Action step 3] | [Date] | [%] |
| [Goal 4] | • [Action step 1]<br>• [Action step 2]<br>• [Action step 3] | [Date] | [%] |
```

## 用法 / Usage
- 必填變數 / Variables: {{project-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Project Plan Action Steps Builder is a free AI prompt that transforms high-level project goals into granul…

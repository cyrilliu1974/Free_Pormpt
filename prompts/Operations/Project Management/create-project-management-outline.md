# Project Breakdown and Task Hierarchy Generator

## 簡介

The Project Breakdown and Task Hierarchy Generator is a free AI prompt that decomposes complex projects into structured, actionable hierarchies for project managers and teams. This project management prompt for ChatGPT takes a single project description and outputs a clear four-level hierarchy: Project → Phases → Tasks → Subtasks. Each element is concretely defined and actionable, using a consistent indented outline format that teams can immediately adopt for planning. It works on ChatGPT, Claude, Gemini, and Grok, adapting the structure to fit software launches, construction timelines, marketing campaigns, research initiatives, or any multi-phase undertaking. The prompt ensures logical sequencing, full coverage of project scope, and a visual structure that makes dependencies and workstreams easy to communicate. Reach for this prompt when you need to turn a concept or brief into a ready-to-execute project plan that all stakeholders can understand and act on. ● Produces a four-tier hierarchy - project, phases, tasks, subtasks - formatted as an indented outline ready to paste into documentation or project-management tools. ● Adapts the number of phases and tasks to match the scope and type of project, whether agile sprints, event planning, or long-term strategic initiatives. ● Ensures every task and subtask is actionable and clearly defined, reducing ambiguity and improving team accountability. ● Uses standardized bullet symbols for each level, making the structure visually scannable and easy to navigate in team meetings or handoff documents. ## Prompt

```
## Role
You are a strategic planning expert who decomposes complex projects into hierarchical, actionable task structures.

## Task
Create a comprehensive project breakdown for the provided project description. Organize it into a clear hierarchy: Project → Phases → Tasks → Subtasks.

## Context
Project description:
{{project-description}}

## Output
Format the breakdown as a hierarchical outline using this structure:

• Project: [Project Name]
   ○ Phase 1: [Phase Name]
      § Task 1: [Task Description]
         - Subtask 1a: [Subtask Description]
         - Subtask 1b: [Subtask Description]
      § Task 2: [Task Description]
         - Subtask 2a: [Subtask Description]
         - Subtask 2b: [Subtask Description]
   ○ Phase 2: [Phase Name]
      § Task 1: [Task Description]
         - Subtask 1a: [Subtask Description]
         - Subtask 1b: [Subtask Description]
      § Task 2: [Task Description]
         - Subtask 2a: [Subtask Description]
         - Subtask 2b: [Subtask Description]
   ○ Phase 3: [Phase Name]
      § Task 1: [Task Description]
         - Subtask 1a: [Subtask Description]
         - Subtask 1b: [Subtask Description]
      § Task 2: [Task Description]
         - Subtask 2a: [Subtask Description]
         - Subtask 2b: [Subtask Description]

Requirements:
- Cover all major aspects of the project comprehensively
- Make each phase, task, and subtask clearly defined and actionable
- Ensure the hierarchy is logical and easy to follow
- Adapt the structure to fit the specific project type
- Use only the indented bullet point format shown above
```

## 用法 / Usage
- 必填變數 / Variables: {{project-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Project Breakdown and Task Hierarchy Generator is a free AI prompt that decomposes complex projects into s…

# Kanban Board Generator for Project Task Management

## 簡介

The Kanban Board Generator for Project Task Management is a free AI prompt that creates customized Kanban boards in markdown table format and provides tailored workflow optimization advice for project teams. This Kanban board prompt for ChatGPT takes your project context and task list, distributes tasks intelligently across four workflow columns (Backlog, In Progress, Testing, Completed), and delivers specific management instructions including WIP limits, prioritization rules, and bottleneck-resolution strategies. It runs on ChatGPT, Claude, Gemini, and Grok, producing both a ready-to-use board table and practical guidance calibrated to your team size and project needs. Teams use it to visualize sprint work, onboard new members to existing workflows, or redesign task management systems that have grown chaotic. Reach for this prompt when you need to transform a flat task list into a structured visual workflow or when your team requires clear criteria for moving work through stages. ● Applies intelligent prioritization logic (urgency, dependencies, quick wins) when organizing your Backlog column ● Recommends team-size-appropriate work-in-progress limits to prevent multitasking overhead and bottlenecks ● Defines specific criteria and triggers for when tasks should move between workflow stages ● Includes daily and weekly board maintenance routines plus metrics for tracking workflow health over time ## Prompt

```
## Role
You are a project management expert specializing in Kanban workflow optimization.

## Task
Create a customized Kanban board in table format with four columns: Backlog, In Progress, Testing, and Completed. Populate the board with the user's tasks, then provide actionable guidance on managing the board to maximize team productivity.

## Context
{{project-context}}

{{task-list}}

## Output
Deliver your response in two parts:

1. **Kanban Board Table**  
   Present a markdown table with columns for Backlog | In Progress | Testing | Completed. Distribute the provided tasks across columns based on their current state and priority. Apply intelligent prioritization (urgent/important, dependencies, quick wins) when placing items in the Backlog.

2. **Board Management Instructions**  
   Provide clear, specific guidance on:
   - How to prioritize and sequence tasks in the Backlog
   - Recommended work-in-progress (WIP) limits for In Progress and Testing columns based on team size
   - Criteria and triggers for moving tasks between columns
   - Daily/weekly routines for board maintenance and review
   - Strategies to identify and resolve bottlenecks
   - Metrics to track for continuous workflow improvement

Tailor all advice to the project context provided. Keep instructions practical and immediately actionable.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}}、{{task-list}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Kanban Board Generator for Project Task Management is a free AI prompt that creates customized Kanban boar…

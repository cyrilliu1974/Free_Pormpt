# Project Schedule & Gantt Chart Generator

## 簡介

The Project Schedule & Gantt Chart Generator is a free AI prompt that creates structured project timelines with task dependencies, duration estimates, and milestone tracking for project managers and team leaders. This project scheduling prompt for ChatGPT walks through a five-step methodology: identifying major tasks and subtasks, mapping dependencies and constraints, estimating durations, assigning start and end dates, and highlighting milestones. It outputs a formatted task table with columns for task name, dates, duration, and dependencies, plus a dedicated milestones section. Use it when planning software releases, construction projects, product launches, or any multi-phase initiative that requires clear timeline visualization. The prompt runs on ChatGPT, Claude, Gemini, and Grok. ● Breaks down complex projects into tasks, subtasks, and logical sequences ● Calculates task dependencies and constraints to prevent scheduling conflicts ● Produces a formatted task table and milestone list ready for stakeholder review ● Accepts custom project name, timeline, and resource variables for any domain ## Prompt

```
## Role
You are an expert project manager creating a comprehensive project schedule and Gantt chart.

## Task
Develop a detailed project schedule that outlines tasks, dependencies, and milestones. Work systematically:

1. Identify all major tasks and subtasks required for project completion
2. Determine the logical sequence of tasks, including dependencies and constraints
3. Estimate the duration of each task and assign start and end dates
4. Highlight key milestones representing significant achievements or deliverables
5. Organize into a clear Gantt chart structure

## Context
**Project:** {{project-name}}
**Timeline:** {{start-date}} to {{end-date}}
**Stakeholders & Resources:** {{stakeholders-and-resources}}

## Output
Present your schedule as:

**Tasks Table:**
| Task Name | Start Date | End Date | Duration | Dependencies |
|-----------|------------|----------|----------|-------------|
| ...       | ...        | ...      | ...      | ...         |

**Milestones Section:**
List key project milestones with target dates and deliverables.
```

## 用法 / Usage
- 必填變數 / Variables: {{end-date}}、{{project-name}}、{{stakeholders-and-resources}}、{{start-date}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Project Schedule & Gantt Chart Generator is a free AI prompt that creates structured project timelines wit…

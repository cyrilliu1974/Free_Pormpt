# Kanban Implementation Plan Generator for Teams

## 簡介

The Kanban Implementation Plan Generator for Teams is a free AI prompt that creates customized Kanban workflow systems for teams seeking to optimize their processes and improve productivity. This Kanban methodology prompt for ChatGPT walks through all core principles - visualizing work, limiting work-in-progress, managing flow, making policies explicit, implementing feedback loops, and collaborative improvement - and applies them to your specific team context. It produces a structured implementation plan delivered as a markdown table with "To Do," "In Progress," and "Done" columns populated with 4-6 actionable tasks per stage. The prompt covers board structure design, task card formats, WIP limits for each workflow stage, daily stand-up protocols, tracking metrics like cycle time and throughput, and retrospective formats. Teams use it when transitioning to Kanban, optimizing existing workflows, or addressing specific bottlenecks in their processes. It runs on ChatGPT, Claude, Gemini, and Grok. ● Maps your current workflow to a proper Kanban board structure with appropriate columns and WIP limits for each stage ● Defines operational practices including daily stand-up formats, card management protocols, and blocker handling procedures ● Establishes metrics tracking for cycle time, lead time, and throughput to measure workflow efficiency ● Provides continuous improvement cadence with retrospective formats aligned to your team's desired outcomes ## Prompt

```
## Role
You are a Kanban methodology expert designing a workflow optimization system.

## Task
Create a comprehensive Kanban implementation plan that includes:

1. **Core Principles Application**: Explain how Kanban's foundational principles (visualize work, limit WIP, manage flow, make policies explicit, implement feedback loops, improve collaboratively) apply to the specific workflow described.

2. **Board Setup Instructions**:
   - Design the Kanban board structure with appropriate columns
   - Define task card format and required information
   - Establish work-in-progress (WIP) limits for each stage
   - Map the current workflow to board columns

3. **Operational Guidelines**:
   - Daily stand-up meeting structure and focus points
   - Board management practices (card movement, updates, blockers)
   - Metrics to track (cycle time, lead time, throughput)
   - Continuous improvement cadence and retrospective format

4. **Tailored Recommendations**: Address the specific pain points and align strategies with the desired outcomes for this team context.

## Context
{{team-context}}

## Output
Deliver your implementation plan as a markdown table with three columns: "To Do", "In Progress", and "Done". Populate each column with 4-6 specific, actionable tasks and strategies that demonstrate how this Kanban system should be structured and operated for this team.
```

## 用法 / Usage
- 必填變數 / Variables: {{team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Kanban Implementation Plan Generator for Teams is a free AI prompt that creates customized Kanban workflow…

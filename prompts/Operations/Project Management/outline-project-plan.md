# Grant Proposal Project Plan Builder

## 簡介

The Grant Proposal Project Plan Builder is a free AI prompt that creates comprehensive, phase-by-phase project plans for grant proposals, helping project managers organize milestones, deliverables, resources, and timelines in a single view. This grant proposal project plan prompt for ChatGPT transforms high-level grant objectives into an actionable roadmap presented as a markdown table with four columns: Milestone, Deliverable, Resource, and Timeline. You provide the grant proposal details, available resources and constraints, and the project timeline with key stakeholders, and the prompt generates a structured plan that accounts for dependencies and realistic scheduling. It runs on ChatGPT, Claude, Gemini, and Grok, making it flexible for any text-based AI workflow. Teams writing federal research grants, nonprofit program proposals, or corporate foundation applications use it to visualize project scope, assign personnel and equipment, and communicate plans to stakeholders and reviewers. Reach for this prompt when you need to translate a grant narrative into a concrete plan that funders can evaluate for feasibility and alignment with objectives. ● Organizes the entire project into logical phases with dependencies and timelines clearly mapped. ● Identifies personnel, equipment, and funding requirements at each milestone to support budget justification. ● Produces a markdown table format that integrates directly into proposal documents or project management tools. ● Ensures alignment between grant objectives and proposed activities by linking every deliverable to a milestone and timeline. ## Prompt

```
## Role
You are an expert project manager specializing in grant proposal planning.

## Task
Create a comprehensive project plan that breaks down the proposal into actionable phases. Identify key milestones, specify deliverables for each milestone, list required resources (personnel, equipment, funding), and establish realistic timelines accounting for dependencies and constraints.

## Context
**Grant proposal details:**
{{grant-proposal-details}}

**Available resources and constraints:**
{{resources-and-constraints}}

**Project timeline and key stakeholders:**
{{timeline-and-stakeholders}}

## Output
Present your project plan as a markdown table with 4 columns:

| Milestone | Deliverable | Resource | Timeline |
|-----------|-------------|----------|----------|

Ensure the plan is comprehensive, achievable, and aligned with the grant proposal's objectives. Structure milestones in logical phases that clearly show project progression.
```

## 用法 / Usage
- 必填變數 / Variables: {{grant-proposal-details}}、{{resources-and-constraints}}、{{timeline-and-stakeholders}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Grant Proposal Project Plan Builder is a free AI prompt that creates comprehensive, phase-by-phase project…

# Online Team Collaboration Workflow Design Prompt

## 簡介

The Online Team Collaboration Workflow Design Prompt is a free AI prompt that builds a comprehensive workflow improvement plan for teams using digital collaboration platforms. This team collaboration prompt for ChatGPT applies dependency grammar - a linguistic framework that structures messages around core actions and their dependent elements - to reduce ambiguity, surface blockers early, and streamline communication. You provide the platform (Slack, Teams, Asana, etc.) and your team's specific challenges; the prompt returns six detailed improvement areas: communication pattern analysis, dependency grammar application, protocol design, task templates, prioritization guidelines, and a feedback system. It runs on ChatGPT, Claude, Gemini, and Grok, making it adaptable to your preferred text model. Real use cases include onboarding remote teams to structured communication, reducing handoff confusion in cross-functional projects, and establishing clarity standards for distributed workflows. Reach for this prompt when your team struggles with vague task assignments, unclear dependencies, or communication bottlenecks on collaboration platforms. ● Analyzes current communication patterns to identify inefficiencies, bottlenecks, and clarity gaps specific to your platform and team context. ● Structures messages and tasks using dependency grammar so core actions, ownership, timing, and conditions are explicit and unambiguous. ● Delivers ready-to-use task templates for requests, updates, and handoffs that teams can adopt immediately. ● Provides prioritization and workflow guidelines to sequence tasks, manage dependencies, and prevent blockers before they impact delivery. ## Prompt

```
## Role
You are an expert collaboration specialist focused on improving team productivity through structured communication and workflow design.

## Task
Develop a comprehensive plan to optimize team collaboration using dependency grammar principles—a framework that structures messages and tasks by identifying core actions and their dependent elements. Deliver six main improvement areas, each with detailed implementation steps.

## Context
Platform: {{platform}}
Team & challenges: {{team-context}}

Dependency grammar structures communication by anchoring each message or task to a core verb or action, then explicitly mapping what depends on it (who, what, when, conditions). This reduces ambiguity and surfaces blockers early.

## Output
Provide your response as a numbered list (1–6) corresponding to:

1. **Current communication pattern analysis** – identify inefficiencies, bottlenecks, and clarity gaps specific to the team context.
2. **Dependency grammar application** – how to structure messages and task descriptions so core actions and their dependencies are explicit.
3. **Communication protocol** – rules and conventions the team should adopt to maintain clarity and effectiveness.
4. **Task templates** – ready-to-use formats for common collaborative activities (e.g., requests, updates, handoffs) built on dependency grammar.
5. **Prioritization and workflow guidelines** – how to sequence tasks and manage dependencies to prevent blockers.
6. **Feedback and refinement system** – mechanisms to gather input and iteratively improve the collaboration process.

For each numbered point, include bullet-pointed subpoints detailing concrete implementation steps tailored to the platform and team context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{platform}}、{{team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Online Team Collaboration Workflow Design Prompt is a free AI prompt that builds a comprehensive workflow …

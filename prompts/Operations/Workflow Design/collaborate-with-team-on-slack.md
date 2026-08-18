# Slack Team Collaboration Strategy Prompt

## 簡介

The Slack Team Collaboration Strategy Prompt is a free AI prompt that develops communication frameworks and channel architectures for project teams using Slack. This Slack communication prompt for ChatGPT analyzes your project context - team size, objectives, and current challenges - then designs a complete strategy including channel recommendations, message structure guidelines based on dependency grammar, and reusable templates for status updates, blockers, and decision requests. It runs on ChatGPT, Claude, and Gemini, producing actionable communication frameworks that help distributed teams structure messages so key actions and decisions come first, with supporting details logically branching from core statements. Use it when launching a new project, reorganizing team workflows, or addressing communication bottlenecks that slow down collaboration. ● Analyzes project context to identify communication patterns, information flow requirements, and decision-making bottlenecks ● Recommends purpose-specific Slack channels mapped to audiences and project aspects ● Provides dependency grammar message templates that lead with actions and requests, improving clarity and response time ● Includes implementation plans with onboarding steps and success metrics for adoption ## Prompt

```
## Role
You are an expert Slack communication strategist optimizing team collaboration and productivity.

## Task
Develop a comprehensive Slack communication strategy that promotes clarity, efficiency, and team cohesion using dependency grammar principles—structuring messages so each element logically depends on core actions or decisions.

## Context
Project: {{project-name}}

Project details:
{{project-context}}
(Include team size, duration, main objectives, and current communication challenges)

## Analysis & Strategy
Address the following:

1. **Communication Needs Analysis**: Assess how the project context shapes messaging patterns, information flow, and decision-making requirements.

2. **Channel Architecture**: Recommend specific Slack channels for different project aspects (e.g., #project-updates, #technical-discussion, #blockers). Map each to its purpose and appropriate audience.

3. **Dependency Grammar Guidelines**: Establish message structure rules where supporting details branch from core statements. Show how to lead with the key action, decision, or request, then attach context and dependencies.

4. **Message Templates**: Create reusable templates for common scenarios—status updates, blocking issues, decision requests, handoffs—each demonstrating dependency grammar structure.

5. **Implementation Plan**: Outline rollout steps, team onboarding to the new patterns, and success metrics.

## Output
Deliver as a numbered list with bullet-point subsections for detailed strategies, templates, and guidelines. Make every recommendation actionable and specific to the project context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}}、{{project-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Slack Team Collaboration Strategy Prompt is a free AI prompt that develops communication frameworks and ch…

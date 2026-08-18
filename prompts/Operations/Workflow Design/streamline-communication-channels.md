# Communication Channel Optimization Prompt

## 簡介

The Communication Channel Optimization Prompt is a free AI prompt that audits internal communication systems and produces tailored workflow improvements for teams and organizations. This communication channel optimization prompt for ChatGPT works by assessing your current tools and practices - email, Slack, meetings, project boards - then mapping friction points to root causes like adoption gaps, tool sprawl, or unclear processes. It outputs a structured markdown table comparing existing channels, their pain points, and optimized solutions, followed by an implementation priority ranking. Use it when onboarding grows chaotic, cross-department collaboration stalls, or information silos slow down decision-making. The prompt runs on ChatGPT, Claude, Gemini, and Grok. ● Evaluates each channel (email, chat, meetings, docs) against its intended purpose and actual usage ● Maps pain points to root causes - tool limitations, low adoption, unclear guidelines, or misaligned processes ● Recommends concrete actions: tool swaps, new usage policies, structural changes, or role-specific adjustments ● Tailors solutions to different departments and workflow patterns for realistic implementation ## Prompt

```
## Role
You are an expert communication strategist specializing in organizational workflow optimization.

## Task
Analyze the current communication infrastructure, identify inefficiencies and friction points, then propose actionable solutions to enhance productivity and information flow across departments and roles.

## Context
Company and environment:
{{company-and-industry}}

Current communication setup and challenges:
{{communication-landscape}}

## Approach
1. Assess each existing channel's effectiveness for its intended purpose
2. Map pain points to their root causes (tool limitations, adoption gaps, process issues)
3. Recommend specific optimizations: tool changes, usage guidelines, or structural adjustments
4. Tailor solutions to different departmental workflows and role requirements

## Output
Deliver your analysis as a markdown table with three columns:

| Current Channels | Pain Points | Optimized Solutions |
|-----------------|-------------|---------------------|
| ...             | ...         | ...                 |

Follow the table with a brief implementation priority ranking and any cross-cutting recommendations.
```

## 用法 / Usage
- 必填變數 / Variables: {{communication-landscape}}、{{company-and-industry}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Communication Channel Optimization Prompt is a free AI prompt that audits internal communication systems a…

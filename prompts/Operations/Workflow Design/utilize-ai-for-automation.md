# AI Automation Implementation Guide Prompt

## 簡介

The AI Automation Implementation Guide Prompt is a free AI prompt that produces detailed, hierarchical instruction manuals for deploying AI-driven automation in specific business contexts. This business automation prompt for ChatGPT works by accepting a description of your business process, current systems, industry regulations, and team capabilities, then generating a numbered implementation roadmap covering opportunity identification, tool selection, system integration, employee training, and performance monitoring. Each major step includes actionable sub-steps structured using dependency grammar - meaning every instruction builds logically on the previous one - along with practical examples, regulatory compliance notes, and common pitfalls. It runs on ChatGPT, Claude, and Gemini to help operations managers, IT directors, and process improvement teams translate automation goals into executable plans. Reach for this prompt when you need a complete framework that addresses technical integration, change management, and ongoing optimization in one document. ● Produces five-stage implementation roadmaps: opportunity analysis, tool selection, integration design, change management, and performance tracking ● Structures every step with numbered sub-steps (1, 1.1, 1.1.1) so tasks follow a logical sequence and dependencies are clear ● Includes ROI quantification guidance, vendor assessment criteria, API mapping, skill-gap analysis, and KPI definition tailored to your industry ● Addresses scalability, cost-effectiveness, regulatory compliance, and risk mitigation within each section of the guide ## Prompt

```
## Role
You are an expert business process automation specialist creating implementation guides for AI-driven automation.

## Task
Develop a detailed, step-by-step instruction manual for implementing AI-driven automation in a specific business context. Structure the guide using dependency grammar, where each main step includes relevant sub-steps that elaborate on the process.

## Context
Business context: {{business-context}}

The business context should describe:
- The specific business process to be automated
- Current automation level and existing systems
- Industry and any relevant regulatory requirements
- Team's technical expertise and capacity
- Available AI tools or platforms being considered

## Output
Create a numbered guide covering:

1. **Identification of automation opportunities** - Analyze the current process, pinpoint bottlenecks, quantify potential ROI, and prioritize automation candidates

2. **Selection of appropriate AI tools** - Evaluate tools against requirements, assess vendor stability and support, consider integration capabilities, and validate with proof-of-concept

3. **Integration with existing systems** - Map data flows, design API connections, plan migration paths, and establish testing protocols

4. **Employee training and change management** - Assess skill gaps, develop training programs, create documentation, and build feedback loops

5. **Performance monitoring and optimization** - Define KPIs, implement monitoring dashboards, establish review cycles, and plan iterative improvements

For each main step, provide:
- Actionable sub-steps using dependency grammar structure
- Practical examples relevant to the business context
- Best practices addressing scalability, cost-effectiveness, and regulatory compliance
- Common pitfalls and mitigation strategies

Format as a numbered list with hierarchical sub-steps (1, 1.1, 1.1.1).
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Skill_Orchestration&Assembly · Skill_Selection_Gate_And_Binding
- 適用 / Use when: The AI Automation Implementation Guide Prompt is a free AI prompt that produces detailed, hierarchical instruc…

# Customer Issue Decision Tree Builder

## 簡介

The Customer Issue Decision Tree Builder is a free AI prompt that creates structured diagnostic flows for support teams and self-service help centers. It transforms a customer issue into a text-based decision tree with binary branches and a conversational narrative script agents can follow during live calls, minimizing resolution time while ensuring no customer hits a dead end without escalation context. This customer issue decision tree prompt for ChatGPT, Claude, Gemini, and Grok asks for a symptom description, known resolution paths, and escalation rules, then outputs two formats: an indented flowchart showing yes/no branching logic and a plain-language script designed to be read aloud. Each node uses only observable information - no technical jargon - and every branch terminates in either a complete fix or a handoff to the right team with accumulated diagnostic context. The prompt enforces a maximum depth of five questions, flags trees that exceed fifteen endpoints for decomposition, and eliminates redundant paths. Reach for this prompt when you need to standardize triage workflows, train new agents, or publish interactive troubleshooters in a knowledge base. ● Binary questions based on what customers can see or test themselves, no specialized tools required ● Dual output: visual flowchart for documentation and conversational script for phone support ● Built-in validation that flags overly complex trees needing subdivision before deployment ● Escape routes at every decision point so customers never loop or hit a wall without human handoff ## Prompt

```
## Role
You are a Process Design Specialist with expertise building diagnostic decision trees for enterprise customer support operations. Your goal is to create clear, customer-centric decision trees that minimize resolution time and friction.

## Context
Every unnecessary step costs money and erodes trust. The tree must serve both self-service users and support agents under pressure. Use plain language customers actually speak—no internal jargon. Assume intermediate technical proficiency unless otherwise specified.

## Task
Create a decision tree for the given customer issue that guides from symptom to resolution in minimum steps.

**Structure each node as:**
- Binary yes/no or simple multiple-choice question
- Based only on information the customer can observe without specialized knowledge
- Include "none of these apply" escape routes to live support with accumulated context

**Each branch must terminate in either:**
- Complete resolution with actionable steps, or
- Specific escalation path with context for the receiving team

**Constraints:**
- Maximum 5 levels deep; flag if more questions are needed (requires subdivision)
- No dead ends or circular loops
- Eliminate redundant branches where different paths lead to identical outcomes
- Flag if tree generates more than 15 terminal nodes (requires decomposition)

{{customer-issue}}

{{resolution-paths}}

{{escalation-context}}

## Output
Deliver two versions:

1. **Text-based flowchart** using indentation and arrows (→) to show branching logic
2. **Narrative version** written conversationally for agents to read aloud during calls

Include any flags for trees needing subdivision or decomposition.
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-issue}}、{{escalation-context}}、{{resolution-paths}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Issue Decision Tree Builder is a free AI prompt that creates structured diagnostic flows for supp…

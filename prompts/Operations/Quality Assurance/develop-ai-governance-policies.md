# AI Governance Policy Framework Generator

## 簡介

The AI Governance Policy Framework Generator is a free AI prompt that creates actionable governance policies aligned with the NIST AI Risk Management Framework for organizations deploying AI systems. This AI governance policy prompt for ChatGPT, Claude, Gemini, and Grok walks you through building complete policy documents covering system capabilities, approved and prohibited use cases, user qualifications, data handling requirements, performance monitoring criteria, incident reporting procedures, and enforcement mechanisms. It works by assessing your AI system's capabilities and deployment context, mapping risks to NIST AI RMF components, and drafting specific guidelines that prevent misuse while enabling legitimate applications. Teams use it to establish clear boundaries for AI tools in healthcare, finance, customer service, and other high-stakes environments where undefined policies create compliance and safety risks. Reach for this prompt when you need to formalize AI use rules that balance innovation with risk mitigation and translate technical assessments into executive-readable policy. ● Assesses AI system capabilities and deployment environments to identify specific risks, required safeguards, and performance boundaries. ● Produces eight structured policy sections with concrete examples, measurable thresholds, and actionable guidelines for immediate implementation. ● Translates technical risk findings into plain language accessible to both technical teams and non-technical executives. ● Defines graduated enforcement mechanisms and clear incident reporting procedures tied to real-world decision points. ## Prompt

```
## Role
You are an AI governance specialist with expertise in the NIST AI Risk Management Framework, translating technical risk assessment into actionable policy that balances innovation with compliance and safety.

## Task
Create a comprehensive AI use policy grounded in the NIST AI RMF. The policy must define approved applications, prohibited uses, user responsibilities, performance boundaries, and enforcement mechanisms in plain language accessible to both technical teams and executives.

## Context
{{system-and-deployment-context}}

The policy operates in an environment where unclear governance has led to regulatory violations and safety incidents. Each section must be specific enough to guide real-world decisions while enabling legitimate use.

## Process
1. Assess the AI system's capabilities, intended use cases, and deployment environment to identify risks and required safeguards
2. Map findings to NIST AI RMF components
3. Draft policy sections that prevent misuse without blocking valid applications

## Output
Structure the policy with these sections, each containing specific examples, measurable criteria, and actionable guidelines:

**System Capabilities and Limitations**  
Describe what the system can and cannot reliably do, with performance boundaries.

**Approved Use Cases**  
List permitted applications with concrete examples tied to business needs.

**Prohibited Applications**  
Specify forbidden uses with rationale (regulatory, ethical, technical).

**User Qualification and Training**  
Define who may use the system and what preparation they require.

**Data Handling and Privacy Requirements**  
Detail data governance, retention, and privacy safeguards.

**Performance Monitoring and Acceptable Boundaries**  
Establish KPIs, thresholds, and review cadences.

**Incident Reporting Procedures**  
Provide clear escalation paths and reporting triggers.

**Enforcement Mechanisms**  
Outline graduated consequences for policy violations.

Use plain language while maintaining technical accuracy and legal precision. Make each guideline immediately implementable.
```

## 用法 / Usage
- 必填變數 / Variables: {{system-and-deployment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The AI Governance Policy Framework Generator is a free AI prompt that creates actionable governance policies a…

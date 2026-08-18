# Compliance Reporting Gap Analysis Prompt

## 簡介

The Compliance Reporting Gap Analysis Prompt is a free AI prompt that evaluates organizational controls against COSO framework principles to identify documentation gaps, control weaknesses, and regulatory vulnerabilities for compliance professionals and internal auditors. This compliance reporting gap analysis prompt for ChatGPT, Claude, Gemini, and Grok systematically examines all five COSO components - control environment, risk assessment, control activities, information and communication, and monitoring - against your current compliance reports and audit findings. It identifies timeline deficiencies, reporting inconsistencies, control procedure weaknesses, and information flow problems that could trigger regulatory violations. Use it when preparing for external audits, responding to regulatory scrutiny, or strengthening internal control frameworks after audit findings. Reach for this prompt when you need a structured, framework-based assessment of compliance weaknesses across multiple organizational departments and control areas. ● Evaluates control environment, risk assessment procedures, control activities, information flow, and monitoring mechanisms against COSO framework standards. ● Identifies documentation gaps, timeline deficiencies, and reporting inconsistencies across departments that could expose the organization to regulatory violations. ● Produces a prioritized action plan table with gap category, risk level, corrective action, timeline, and responsible party assignments. ● Analyzes how compliance information flows across organizational units and whether monitoring mechanisms effectively capture control performance. ## Prompt

```
## Role
You are a compliance auditor and internal controls specialist with deep expertise in COSO Internal Control-Integrated Framework principles. Your focus is identifying control weaknesses, documentation gaps, and systemic vulnerabilities that expose organizations to regulatory violations and audit failures.

## Task
Conduct a comprehensive compliance reporting gap analysis. Evaluate all five COSO components—control environment, risk assessment, control activities, information and communication, and monitoring—against current compliance reports and audit findings. Identify documentation gaps, timeline deficiencies, control procedure weaknesses, and reporting inconsistencies that could trigger regulatory violations. Analyze compliance information flow across departments and assess whether monitoring mechanisms capture control effectiveness. Map missing or incomplete reporting areas against regulatory transparency and accountability standards.

## Context
{{compliance-context}}

Include: industry and key regulatory requirements; current compliance reporting frequency and regulators; organization size, departments, and reporting structure; recent internal or external audit findings; primary compliance concerns or known weak areas.

## Output
Structure your analysis using COSO framework headings:

### Control Environment
- [Identified gaps as bullet points]

### Risk Assessment
- [Identified gaps as bullet points]

### Control Activities
- [Identified gaps as bullet points]

### Information and Communication
- [Identified gaps as bullet points]

### Monitoring Activities
- [Identified gaps as bullet points]

### Prioritized Action Plan
Present a table with columns: Gap Category | Risk Level | Corrective Action | Timeline | Responsible Party

Order recommendations by risk severity and implementation urgency.
```

## 用法 / Usage
- 必填變數 / Variables: {{compliance-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Compliance Reporting Gap Analysis Prompt is a free AI prompt that evaluates organizational controls agains…

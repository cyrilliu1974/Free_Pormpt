# Internal Control Assessment Using COSO Framework

## 簡介

The Internal Control Assessment Using COSO Framework is a free AI prompt that evaluates control design and operating effectiveness across an organization's Control Environment, Risk Assessment, Control Activities, Information & Communication, and Monitoring Activities. This internal control assessment prompt for ChatGPT, Claude, Gemini, and Grok guides auditors and compliance professionals through a structured COSO analysis, pinpointing control gaps, redundancies, and root causes while quantifying regulatory, financial, operational, and reputational impact. It delivers an executive summary, detailed findings by component, a prioritized action plan ranked by risk severity and implementation complexity, and a phased implementation roadmap with success metrics. Reach for this prompt when preparing for an internal audit, responding to audit findings, or strengthening compliance systems in regulated industries. ● Systematically evaluates all five COSO components, assessing design adequacy and operating effectiveness. ● Identifies control gaps, redundancies, and root causes, then quantifies potential impact across regulatory, financial, operational, and reputational dimensions. ● Prioritizes recommendations in a table format showing risk level, timeline, and resource requirements. ● Provides a phased implementation roadmap with dependencies and measurable success criteria. ## Prompt

```
## Role
You are an internal audit specialist with expertise in the COSO Internal Control–Integrated Framework. You assess control design and operating effectiveness, identify gaps, and deliver actionable recommendations that strengthen compliance while maintaining operational efficiency.

## Task
Conduct a comprehensive internal control assessment across all five COSO components:

1. **Control Environment** – Assess governance structure, tone at the top, and ethical culture
2. **Risk Assessment** – Evaluate how the organization identifies, analyzes, and responds to risks
3. **Control Activities** – Examine policies, procedures, and controls that mitigate identified risks
4. **Information & Communication** – Analyze data flows, reporting channels, and communication effectiveness
5. **Monitoring Activities** – Review ongoing evaluations and corrective action processes

For each component:
- Assess design adequacy and operating effectiveness
- Identify control gaps, redundancies, and root causes
- Evaluate risk coverage against regulatory requirements and industry best practices
- Quantify potential impact of weaknesses (regulatory, financial, operational, reputational)
- Provide improvement strategies with implementation timelines

Prioritize recommendations by risk severity, implementation complexity, and resource requirements.

## Context
{{organization-context}}

{{audit-findings}}

## Output
Structure your analysis as follows:

### Executive Summary
High-level overview of control maturity, critical findings, and top 3 priority actions.

### Detailed Findings by COSO Component
For each of the five components:
- **Current State Assessment**
- **Control Gaps Identified** (bulleted list)
- **Root Cause Analysis**
- **Impact Quantification**

### Prioritized Action Plan
Present as a table:

| Recommendation | Risk Level | Timeline | Resource Requirements |
|----------------|------------|----------|----------------------|
| [specific action] | Critical/High/Medium/Low | [timeframe] | [people, budget, tools] |

### Implementation Roadmap
Phased approach (Quick Wins → Short-term → Long-term) with dependencies and success metrics.
```

## 用法 / Usage
- 必填變數 / Variables: {{audit-findings}}、{{organization-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Internal Control Assessment Using COSO Framework is a free AI prompt that evaluates control design and ope…

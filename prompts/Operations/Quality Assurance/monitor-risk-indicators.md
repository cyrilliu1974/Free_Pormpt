# Risk Indicator Monitoring Framework Generator

## 簡介

The Risk Indicator Monitoring Framework Generator is a free AI prompt that creates comprehensive risk assessment plans for businesses seeking to identify, prioritize, and mitigate operational threats. This risk management prompt for ChatGPT analyzes both internal factors (operational, financial, human resources, technology) and external factors (market conditions, regulatory changes, competitive pressures, economic shifts) to deliver a prioritized markdown table. Each entry maps a specific risk indicator to its potential impact and an actionable mitigation strategy, ordered by likelihood and severity. The prompt runs on ChatGPT, Claude, and Gemini, making it ideal for quality assurance teams, risk managers, and business leaders who need a systematic approach to threat assessment. Real-world use cases include operational continuity planning, compliance risk mapping, and strategic risk reviews. Reach for this prompt when you need to move beyond ad-hoc risk tracking and build a documented, prioritized framework that stakeholders can act on. ● Identifies specific risk indicators across internal operations and external market conditions ● Evaluates concrete financial, operational, and reputational consequences with severity ratings ● Proposes feasible, cost-effective mitigation strategies with implementation guidance ● Prioritizes risks automatically by likelihood and severity for clear decision-making ## Prompt

```
## Role
You are a risk management expert creating a comprehensive risk management plan.

## Task
Develop a structured risk assessment that identifies key risk indicators, evaluates their potential impact, and proposes actionable mitigation strategies. Prioritize risks by likelihood and severity, ensuring strategies are feasible and cost-effective.

## Context
Business context: {{business-context}}

Consider both internal factors (operational, financial, human resources, technology) and external factors (market conditions, regulatory changes, competitive pressures, economic shifts) relevant to this business.

## Output
Deliver your analysis as a markdown table with three columns:

| Risk Indicator | Potential Impact | Mitigation Strategy |
|---------------|------------------|---------------------|

Each row must contain:
- **Risk Indicator**: Specific risk with clear description
- **Potential Impact**: Concrete consequences (financial, operational, reputational) with severity assessment
- **Mitigation Strategy**: Actionable steps with implementation guidance

Order rows from highest to lowest priority based on likelihood × severity.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Risk Indicator Monitoring Framework Generator is a free AI prompt that creates comprehensive risk assessme…

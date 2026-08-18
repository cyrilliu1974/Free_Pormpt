# Financial Risk Analysis Report Generator

## 簡介

The Financial Risk Analysis Report Generator is a free AI prompt that produces actionable risk assessments for businesses, analysts, and finance teams evaluating exposure and planning mitigation. This financial risk analysis prompt for ChatGPT, Claude, Gemini, and Grok takes a description of your financial situation and returns a five-section report: risk identification with category labels (market, credit, liquidity, operational), a scored assessment table ranking likelihood and impact, prioritized mitigation strategies for high-risk items, a numbered monitoring plan, and an executive summary. Use it when preparing board presentations, quarterly reviews, investment decisions, or compliance documentation that demands clarity and structure. ● Identifies and categorizes financial risks tailored to the specific context you provide, with no generic placeholders. ● Builds a risk assessment table scoring each threat on likelihood and impact, calculating an overall risk score for prioritization. ● Delivers short-term and long-term mitigation strategies ranked by urgency, plus a step-by-step monitoring process. ● Outputs an executive summary that distills critical findings into a concise, decision-ready paragraph. ## Prompt

```
## Role
You are a financial risk analyst creating a structured, actionable risk analysis.

## Task
Develop a comprehensive financial risk analysis that identifies threats, assesses their severity, and provides mitigation strategies to support decision-making.

## Context
Analyze the financial situation described below:

{{financial-context}}

Write in clear, direct prose. Avoid unnecessary adjectives, adverbs, and jargon. Target readability at a Gunning Fog index of 8. Tailor all risks and recommendations to the specific context provided—do not add generic placeholders.

## Output
Structure your analysis in five sections:

**1. Risk Identification**
- List potential financial risks
- Categorize each (market risk, credit risk, liquidity risk, operational risk, etc.)

**2. Risk Assessment**
Present risks in a table:

| Risk | Likelihood (1-5) | Impact (1-5) | Risk Score (Likelihood × Impact) |
|------|------------------|--------------|----------------------------------|

**3. Risk Mitigation Strategies**
- Bullet points for each high-risk item
- Include both short-term and long-term approaches
- Prioritize by risk score

**4. Monitoring and Review**
Provide a step-by-step ongoing risk management plan. Number each step with an emoji.

**5. Executive Summary**
Write a concise paragraph (3-5 sentences) summarizing the most critical findings and recommended actions.
```

## 用法 / Usage
- 必填變數 / Variables: {{financial-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Financial Risk Analysis Report Generator is a free AI prompt that produces actionable risk assessments for…

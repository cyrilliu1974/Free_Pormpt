# Business Risk Assessment Framework Generator

## 簡介

The Business Risk Assessment Framework Generator is a free AI prompt that conducts comprehensive risk identification and mitigation planning for any business context. This business risk assessment prompt for ChatGPT produces a two-part deliverable: a markdown table categorizing risks by type (financial, operational, strategic, compliance) with likelihood and impact ratings (Low/Medium/High), followed by actionable mitigation strategies tailored to your specific business environment. It analyzes industry exposures, regulatory requirements, market dynamics, and operational dependencies, then prioritizes threats by severity and probability. The prompt runs on ChatGPT, Claude, Gemini, and Grok, adapting its analysis to the business context you provide - whether you're a startup navigating early-stage vulnerabilities, an enterprise managing complex compliance landscapes, or a mid-market company balancing growth and stability. ● Categorizes risks systematically across four key domains: financial, operational, strategic, and compliance. ● Rates each identified risk by likelihood and business impact to support data-driven prioritization. ● Generates context-specific mitigation strategies that reflect your industry, size, location, and risk tolerance. ● Outputs a markdown table and bullet-point action plan ready for board presentations, audit documentation, or internal planning sessions. ## Prompt

```
## Role
You are a risk management expert conducting a comprehensive business risk assessment.

## Task
Identify potential risks across financial, operational, strategic, and compliance categories. Assess each risk's likelihood and business impact, then prioritize and develop practical mitigation strategies tailored to the specific business context.

## Context
Business context: {{business-context}}

Analyze the business environment, operations, and vulnerabilities specific to this context. Consider industry-specific exposures, regulatory requirements, market dynamics, and operational dependencies. Prioritize risks by severity and probability.

## Output
Deliver your assessment in two parts:

1. **Risk Assessment Table** (markdown format with 3 columns):
   - Risk Category
   - Likelihood (Low/Medium/High)
   - Impact (Low/Medium/High)

2. **Risk Management Strategies** (bullet-point list under each identified risk):
   - Practical, actionable mitigation or management strategies
   - Tailored to the business context provided

Ensure the assessment is thorough, actionable, and specific to the business type, industry, size, location, and risk tolerance described.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Business Risk Assessment Framework Generator is a free AI prompt that conducts comprehensive risk identifi…

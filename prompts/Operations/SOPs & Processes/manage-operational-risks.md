# Operational Risk Management Plan Builder

## 簡介

The Operational Risk Management Plan Builder is a free AI prompt that creates comprehensive operational risk assessments with mitigation strategies for businesses across any industry. This operational risk management prompt for ChatGPT guides the AI through a systematic analysis of your business operations, identifying 8-12 material risks across financial, operational, strategic, compliance, reputational, and technology categories. It evaluates each risk's likelihood (from rare to almost certain) and impact (from negligible to severe), then proposes concrete, actionable mitigation strategies tailored to your specific business context. The prompt works on ChatGPT, Claude, Gemini, and Grok, delivering results in a clear markdown table format that prioritizes risks by their combined likelihood-impact scores. Use cases include regulatory compliance preparation, operational audits, business continuity planning, investor due diligence, and strategic planning sessions. This prompt is ideal for risk managers, consultants, operations directors, compliance officers, and business owners who need to systematically identify and address operational vulnerabilities. ● Analyzes internal factors (processes, systems, personnel, controls) and external factors (market, regulatory, supply chain, competition) to surface hidden vulnerabilities ● Assigns structured likelihood and impact ratings with rationale, enabling objective prioritization of where to focus resources ● Generates specific, implementable mitigation strategies rather than generic risk management advice ● Outputs results in a sortable markdown table format that stakeholders can review, discuss, and act upon immediately ## Prompt

```
## Role
You are an expert risk management consultant creating comprehensive operational risk assessments.

## Task
Develop a risk management plan that identifies operational risks, assesses their likelihood and impact, and proposes mitigation strategies tailored to the business context.

## Context
Business context: {{business-context}}

Analyze operations across internal factors (processes, systems, personnel, controls) and external factors (market, regulatory, supply chain, competition). Consider industry-specific vulnerabilities and compliance requirements.

## Process
1. Identify operational risks across key categories: financial, operational, strategic, compliance, reputational, and technology risks
2. Assess each risk's likelihood (rare/possible/likely/almost certain) and impact (negligible/minor/moderate/major/severe)
3. Develop actionable mitigation strategies specific to the business type and risk profile
4. Prioritize risks by combining likelihood and impact scores

## Output
Present findings as a markdown table with these columns:
- **Risk Category** – the type and specific risk identified
- **Likelihood** – probability of occurrence with brief rationale
- **Impact** – potential consequence severity and scope
- **Mitigation Strategies** – specific, actionable controls and responses

Include 8-12 material risks. Order by priority (highest combined likelihood-impact first). Make strategies concrete and implementable.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Operational Risk Management Plan Builder is a free AI prompt that creates comprehensive operational risk a…

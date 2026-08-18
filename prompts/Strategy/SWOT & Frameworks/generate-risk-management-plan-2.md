# Risk Management Plan Generator for Business

## 簡介

The Risk Management Plan Generator for Business is a free AI prompt that creates tailored risk management frameworks for organizations seeking to identify and address potential threats. This risk management prompt for ChatGPT guides the AI to act as an expert consultant, categorizing risks into five domains - operational, financial, strategic, compliance, and reputational - then assessing their likelihood and impact using a 3×3 matrix. The output includes an executive summary, a prioritized risk assessment table, detailed mitigation strategies with action plans and timelines, and ongoing monitoring processes. Teams use it when launching new initiatives, conducting annual reviews, preparing for audits, or responding to emerging market conditions. It runs on ChatGPT, Claude, and Gemini. ● Categorizes risks into operational, financial, strategic, compliance, and reputational buckets with specific examples ● Produces a risk assessment matrix scoring likelihood and impact on a 1–9 scale for the top three threats ● Delivers mitigation strategies with responsible parties, timelines, and concrete action steps ● Establishes monitoring cadence, key risk indicators, and escalation procedures for ongoing risk governance ## Prompt

```
## Role
You are an expert risk management consultant who identifies, assesses, and mitigates business risks across industries. Develop a comprehensive risk management plan tailored to the provided business context.

## Task
Create a structured risk management plan that:
- Identifies and categorizes potential internal and external risks
- Assesses likelihood and impact of key risks
- Provides specific, actionable mitigation strategies
- Establishes monitoring and reporting processes

## Context
Business context: {{business-context}}

## Output
Deliver the plan in the following format:

### Executive Summary
Provide a high-level overview of key findings and recommendations.

### Risk Identification
Categorize potential risks into:
- **Operational Risks**: Process failures, system outages, supply chain disruptions
- **Financial Risks**: Cash flow issues, market volatility, credit exposure
- **Strategic Risks**: Competitive threats, market shifts, M&A challenges
- **Compliance Risks**: Regulatory violations, legal liabilities, policy breaches
- **Reputational Risks**: Brand damage, customer trust erosion, negative publicity

### Risk Assessment Matrix
For the top three risks, create a table:

| Risk Name | Likelihood | Impact | Risk Score |
|-----------|------------|--------|------------|
| [Risk 1]  | Low/Medium/High | Low/Medium/High | [1-9 scale] |
| [Risk 2]  | Low/Medium/High | Low/Medium/High | [1-9 scale] |
| [Risk 3]  | Low/Medium/High | Low/Medium/High | [1-9 scale] |

### Risk Mitigation Strategies
For each top risk, provide:

**[Risk Name]**
- **Mitigation Strategy**: High-level approach to reduce or manage the risk
- **Action Plan**: Specific steps with clear deliverables
- **Responsible Party**: Role or department accountable for execution
- **Timeline**: Implementation milestones and completion date

### Risk Monitoring and Reporting
Describe the ongoing process for:
- Regular risk reviews (frequency and participants)
- Key risk indicators (KRIs) to track
- Escalation procedures for emerging threats
- Reporting cadence and stakeholder communication

### Appendix
Include supporting documentation, data sources, or additional risk details as needed.

---

**Guidelines**:
- Use clear, jargon-free language accessible to all stakeholders
- Base recommendations on the specific business context provided
- Prioritize actionable, implementable strategies over theoretical frameworks
- Calculate risk scores using a 3×3 matrix (Low=1, Medium=2, High=3; multiply likelihood × impact)
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Strategic_Resource&Sprint_Prioritization
- 適用 / Use when: The Risk Management Plan Generator for Business is a free AI prompt that creates tailored risk management fram…

# Risk Audit Report Generator for Business Compliance

## 簡介

The Risk Audit Report Generator for Business Compliance is a free AI prompt that conducts structured risk audits and produces actionable risk management plans for businesses operating under specific regulatory frameworks. This risk audit prompt for ChatGPT analyzes your business operations, industry trends, and regulatory environment to identify 8-12 distinct vulnerabilities across custom risk categories. For each identified risk, it assesses likelihood (low/medium/high) and potential impact (low/medium/high), then recommends tailored mitigation strategies with explanatory context. The output is a markdown table sorted by priority, placing the most critical risks first. It runs on ChatGPT, Claude, and Gemini, and adapts to any industry by accepting three variables: business context, regulatory environment, and the specific risk categories you want evaluated. Reach for this prompt when you need a systematic risk assessment that goes beyond generic checklists - whether you're preparing for compliance reviews, onboarding new operations, or responding to emerging threats in your sector. ● Produces a structured markdown table with Risk Category, Likelihood, Impact, Mitigation Strategy, and Explanation columns for clarity and ease of implementation. ● Prioritizes risks by combined likelihood and impact, ensuring leadership focuses on the most critical vulnerabilities first. ● Adapts to any regulatory environment and custom risk categories, from financial compliance and data privacy to operational safety and reputational threats. ● Delivers 8-12 distinct, actionable risk findings in a single audit report, ready for stakeholder review or integration into broader compliance documentation. ## Prompt

```
## Role
You are an expert risk management consultant conducting a comprehensive risk audit.

## Task
Identify potential vulnerabilities and develop a robust risk management plan tailored to the specified business context. Analyze business operations, industry trends, and the regulatory environment. For each risk identified:
- Categorize the risk type
- Assess likelihood (low/medium/high)
- Assess potential impact (low/medium/high)
- Devise effective mitigation strategies
- Provide a brief explanation

## Context
Business context: {{business-context}}

Regulatory environment: {{regulatory-environment}}

Risk categories to evaluate: {{risk-categories}}

## Output
Present findings as a markdown table with these columns: Risk Category | Likelihood | Impact | Mitigation Strategy | Explanation

Include 8-12 distinct risks across the specified categories. Prioritize risks by combined likelihood and impact, placing the most critical at the top.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{regulatory-environment}}、{{risk-categories}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Risk Audit Report Generator for Business Compliance is a free AI prompt that conducts structured risk audi…

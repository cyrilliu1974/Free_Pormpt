# Security Assessment Report Prompt for ChatGPT

## 簡介

The Security Assessment Report Prompt for ChatGPT is a free AI prompt that helps security analysts and risk managers conduct systematic security assessments for any business or industry. This security assessment prompt for ChatGPT walks you through evaluating existing risk management processes, identifying security threats and vulnerabilities across specific assessment areas, rating their likelihood and impact, and developing targeted mitigation strategies. The output is a clear markdown table that organizes findings into Assessment Areas, Potential Risks, Likelihood ratings, Impact ratings, and Mitigation Strategies. It runs on ChatGPT, Claude, and Gemini, and requires three variables: your business name, industry, and the specific assessment areas you want to evaluate (such as network security, physical access, data protection, or compliance). Real use cases include quarterly security reviews, pre-audit preparations, vendor risk assessments, and incident response planning. Reach for this prompt when you need to document security posture, communicate risk to stakeholders, or build a prioritized remediation roadmap. ● Evaluates risk management processes systematically across custom assessment areas ● Identifies and categorizes security threats with likelihood and impact ratings ● Generates mitigation strategies tailored to each identified vulnerability ● Delivers findings in a markdown table format ready for reports and stakeholder review ## Prompt

```
## Role
You are an expert security analyst conducting a comprehensive security assessment.

## Task
Evaluate risk management processes and identify potential vulnerabilities. For each assessment area, analyze current processes, identify security threats and vulnerabilities, assess likelihood and impact, and develop mitigation strategies.

## Context
Business: {{business-name}}
Industry: {{industry}}
Assessment areas: {{assessment-areas}}

Ensure findings build logically on one another, with each risk assessment informing subsequent analysis.

## Output
Present your findings as a markdown table with these columns:
- Assessment Areas
- Potential Risks
- Likelihood (Low/Medium/High)
- Impact (Low/Medium/High)
- Mitigation Strategies

Each row should connect logically to create a coherent security assessment that enhances the organization's risk management and security posture.
```

## 用法 / Usage
- 必填變數 / Variables: {{assessment-areas}}、{{business-name}}、{{industry}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Security Assessment Report Prompt for ChatGPT is a free AI prompt that helps security analysts and risk ma…

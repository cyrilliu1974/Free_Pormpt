# Employee Offboarding Security Risk Analysis Prompt

## 簡介

The Employee Offboarding Security Risk Analysis Prompt is a free AI prompt that generates comprehensive data protection measures for organizations managing employee departures. This employee offboarding prompt for ChatGPT guides AI models including ChatGPT, Claude, Gemini, and Grok to analyze security touchpoints during employee transitions and deliver prioritized action plans. It accounts for your organization profile and compliance context, then produces a numbered list of precautions with specific implementation steps and timelines. Teams use it to address immediate risks like access revocation and device recovery on departure day, plus ongoing monitoring for unauthorized access attempts and intellectual property concerns. ● Prioritizes actions by risk severity and time sensitivity, from departure-day tasks to long-term monitoring ● Covers technical controls (access management, data audit trails) and human factors that threaten data integrity ● Produces legally sound recommendations adaptable to different industries and organizational structures ● Includes specific implementation steps for each security precaution, not generic checklists ## Prompt

```
## Role

You are an expert cybersecurity consultant and data protection specialist with deep experience in enterprise security protocols and employee lifecycle management.

## Task

Provide comprehensive, actionable data security precautions that organizations must implement when employees leave the company. Analyze critical security touchpoints during employee offboarding, prioritize actions based on risk severity and time sensitivity, and provide specific implementation steps for each precaution.

## Context

Employee departures represent one of the highest-risk periods for data breaches, intellectual property theft, and security vulnerabilities. The departure process requires immediate, systematic action across multiple security domains including access management, device recovery, data audit trails, and legal compliance.

Consider both technical security measures and human factors that could compromise data integrity. Address immediate actions required on the departure date as well as ongoing monitoring requirements.

**Organization profile:**  
{{organization-profile}}

**Security and compliance context:**  
{{security-compliance-context}}

## Output

Deliver your response as a numbered list with clear headings, specific action items, and implementation timelines for each security precaution. Ensure recommendations are practical, legally sound, and implementable across different organizational sizes and industries.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-profile}}、{{security-compliance-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Employee Offboarding Security Risk Analysis Prompt is a free AI prompt that generates comprehensive data p…

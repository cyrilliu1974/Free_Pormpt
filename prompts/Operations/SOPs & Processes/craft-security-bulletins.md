# Security Bulletin Writer Prompt for Cybersecurity Teams

## 簡介

The Security Bulletin Writer Prompt for Cybersecurity Teams is a free AI prompt that creates comprehensive security alerts explaining threats, impacts, and protective measures for diverse organizational audiences. This security bulletin prompt for ChatGPT, Claude, Gemini, and Grok transforms a security issue description into a structured alert containing severity assessments, plain-language threat explanations, prioritized mitigation steps, technical details like CVE identifiers, and resource links. It balances accessibility for business stakeholders with the technical depth IT professionals need, adjusting tone and complexity based on your specified target audience and urgency level. Cybersecurity teams use it to standardize incident communications, compliance officers use it to document vulnerability responses, and IT managers use it to coordinate rapid remediation efforts. Reach for this prompt whenever you need to quickly draft a clear, actionable security bulletin that both executives and engineers can act on. ● Produces five-section bulletins covering summary, threat description, recommended actions, technical details, and resources ● Adapts language complexity and technical depth based on specified audience and organization type ● Includes severity assessment, exploitation scenarios, prioritized mitigation steps, and implementation timelines ● Incorporates space for CVE identifiers, affected versions, IOCs, patch links, and internal contact information ## Prompt

```
## Role
You are an expert cybersecurity analyst creating a security bulletin that communicates threats and protective measures clearly to diverse audiences.

## Task
Produce a comprehensive security bulletin that alerts stakeholders to a security issue and guides them through mitigation. The bulletin must balance accessibility for non-technical readers with sufficient technical depth for IT professionals.

## Context
**Organization type:** {{organization-type}}
**Target audience:** {{target-audience}}
**Security issue:** {{security-issue}}
**Urgency level:** {{urgency-level}}

## Output Requirements
Structure the bulletin with these sections:

**Summary**
- Severity and urgency assessment
- Brief description of the threat or vulnerability in plain language
- Who is affected

**Threat Description**
- Clear explanation of what the vulnerability or threat is
- How it could be exploited
- Potential impact on systems, data, or operations

**Recommended Actions**
- Specific, prioritized mitigation steps
- Prevention measures
- Timeline for implementation based on urgency

**Technical Details**
- CVE identifiers, affected versions, or IOCs where applicable
- System requirements or configurations at risk
- Detection methods

**Resources**
- Links to patches, updates, or vendor advisories
- Internal contacts for assistance
- Further reading or guidance

Use clear headings, bullet points, and concise language. Tailor technical depth to the specified audience while ensuring all stakeholders understand the severity and required actions.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-type}}、{{security-issue}}、{{target-audience}}、{{urgency-level}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Security Bulletin Writer Prompt for Cybersecurity Teams is a free AI prompt that creates comprehensive sec…

# Employee Offboarding Checklist Generator

## 簡介

The Employee Offboarding Checklist Generator is a free AI prompt that creates phase-by-phase departure checklists for HR teams managing legal compliance, security protocols, and knowledge transfer. This employee offboarding prompt for ChatGPT builds a chronological checklist spanning resignation notice through post-departure follow-up, with each item specifying the responsible party, completion deadline, and verification method. It addresses asset recovery, access revocation, documentation requirements, knowledge handover, and compliance obligations tailored to your company size, industry, and regulatory environment (SOX, HIPAA, GDPR, financial services). The output is checkbox-ready and formatted for immediate use in HRIS systems or as standalone workflow documentation. Runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to standardize offboarding across employee types, close security gaps, mitigate legal risk, or solve problems like missed asset returns, delayed access revocation, or knowledge loss. ● Organizes tasks chronologically across pre-departure preparation, final week activities, departure day procedures, and post-departure follow-up. ● Assigns clear ownership, specific timelines ("Day 1," "3 days before departure," "Within 24 hours of exit"), and completion criteria for every checklist item. ● Includes callouts for role-specific variations and compliance-driven requirements to address different employee types and regulatory standards. ● Balances administrative tasks (asset recovery, access revocation, documentation) with relationship preservation and employer brand protection. ## Prompt

```
## Role
You are an HR operations specialist designing offboarding systems that balance legal compliance, security, and positive employee experience.

## Task
Create a comprehensive offboarding checklist structured chronologically from resignation notice through post-departure follow-up. Each item must specify the responsible party, completion deadline, and verification method.

## Context
Effective offboarding mitigates legal risk, closes security gaps, preserves institutional knowledge, and protects employer brand. The checklist must address:

- Pre-departure preparation (resignation to final week)
- Final week activities
- Departure day procedures
- Post-departure follow-up
- Documentation requirements and asset recovery
- Access revocation and knowledge transfer
- Compliance obligations and relationship preservation
- Variations for different employee types and roles

**Company profile:** {{company-context}}
(Include company size, industry, typical employee roles, and any specific compliance requirements such as SOX, HIPAA, GDPR, financial services regulations, or healthcare standards.)

**Current challenges:** {{offboarding-challenges}}
(Describe specific problems with your current offboarding process—missed asset returns, delayed access revocation, compliance gaps, knowledge loss, negative exit experiences, or administrative bottlenecks.)

## Output
Deliver a structured checklist with:

- Clear section headers for each phase
- Checkbox-ready line items
- Responsible party assignment for each task
- Specific timelines (e.g., "Day 1," "3 days before departure," "Within 24 hours of exit")
- Verification/completion criteria
- Callouts for role-specific or compliance-driven items

Format for maximum usability—ready to implement or adapt into your HRIS or workflow system.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-context}}、{{offboarding-challenges}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Employee Offboarding Checklist Generator is a free AI prompt that creates phase-by-phase departure checkli…

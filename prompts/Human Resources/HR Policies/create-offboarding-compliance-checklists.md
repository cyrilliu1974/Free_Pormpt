# Offboarding Compliance Checklist Generator

## 簡介

The Offboarding Compliance Checklist Generator is a free AI prompt that creates structured employee exit checklists for HR teams and compliance officers managing regulatory obligations and security protocols. This offboarding compliance prompt for ChatGPT produces four separate checklists - administrative processes, legal compliance requirements, IT security protocols, and knowledge transfer procedures - each organized across pre-departure, departure day, and post-departure phases. It runs on ChatGPT, Claude, Gemini, and Grok, generating actionable items with assigned responsible parties, specific timelines, verification methods, escalation paths, and common failure points. Use it when designing exit workflows for organizations that must meet ISO 30414:2018 Human Capital Reporting Standards or navigate industry-specific regulations, from standard employee transitions to complex executive departures. ● Produces checklists with clear timelines, responsible parties, verification steps, and escalation procedures for administrative, legal, IT, and knowledge transfer tasks. ● Integrates ISO 30414:2018 standards and addresses interdependencies between departments, jurisdiction-specific regulations, and approval workflows. ● Scales from routine employee exits to high-stakes executive departures, accounting for final pay, benefits, records retention, device return, data protection, and documentation handover. ● Identifies common failure points - incomplete access revocation, missing legal clearances, inadequate knowledge transfer - and provides avoidance strategies to prevent data breaches and legal liabilities. ## Prompt

```
## Role
You are an HR compliance specialist with expertise in offboarding process design, ISO 30414:2018 Human Capital Reporting Standards, and enterprise risk mitigation.

## Task
Create four comprehensive offboarding process checklists:

1. **Administrative Processes** – final pay, benefits, records retention
2. **Legal Compliance Requirements** – regulatory obligations, clearances, documentation
3. **IT Security Protocols** – access revocation, device return, data protection
4. **Knowledge Transfer Procedures** – documentation, handover, continuity planning

Each checklist must include:
- Specific timelines across pre-departure, departure day, and post-departure phases
- Responsible parties for each action
- Verification steps and quality control checkpoints
- Escalation procedures for blockers
- Common failure points and avoidance strategies

Design the checklists to scale from standard employee transitions to complex executive departures.

## Context
{{company-and-compliance-context}}

Organizations lose millions when offboarding fails due to incomplete access revocation, missing knowledge documentation, inadequate legal clearances, or non-compliance with industry regulations. The checklists must integrate ISO 30414:2018 standards while addressing interdependencies between departments and jurisdiction-specific requirements.

## Output
Deliver four separate checklists with clear phase-based structure:

- **Pre-departure preparation** (1-4 weeks before last day)
- **Departure day execution** (final day actions)
- **Post-departure verification** (days/weeks after exit)

Format each item as: **action** → responsible party → timeline → verification method.

Include documentation requirements, approval workflows, and quality control gates. Tailor guidance to the company size, industry, compliance landscape, and existing protocols provided in the context.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-and-compliance-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Offboarding Compliance Checklist Generator is a free AI prompt that creates structured employee exit check…

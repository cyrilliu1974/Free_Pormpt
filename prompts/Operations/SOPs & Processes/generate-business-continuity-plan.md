# Business Continuity Plan Generator for ChatGPT

## 簡介

The Business Continuity Plan Generator is a free AI prompt that creates detailed business continuity plans for organizations preparing for operational disruptions, crises, and disaster scenarios. This business continuity plan prompt for ChatGPT walks you through building a multi-section plan that includes executive summaries, risk assessments for natural disasters and cyberattacks, prevention strategies, incident response protocols, team assignments, communication workflows, IT disaster recovery procedures, and testing schedules. It runs on ChatGPT, Claude, Gemini, and Grok, requiring only a brief business overview to tailor the output. Real-world applications include preparing startups for infrastructure outages, designing pandemic response protocols for mid-sized companies, and documenting recovery time objectives for regulated industries that require compliance documentation. Reach for this prompt when you need a structured, actionable continuity plan that addresses detection, containment, and recovery across every critical function in your operation. ● Identifies and prioritizes potential disruptions by likelihood and business impact across operational, financial, and reputational dimensions ● Defines recovery time objectives and recovery point objectives for each critical business function, with step-by-step restoration procedures ● Assigns continuity team roles, contact chains, and escalation thresholds to ensure clear decision authority during crises ● Structures internal and external communication plans covering employee notifications, customer updates, supplier coordination, and regulatory reporting ## Prompt

```
## Role
You are a business continuity expert with deep knowledge in risk management, disaster recovery, and crisis response.

## Task
Create a comprehensive business continuity plan that prepares for and responds to potential disruptions. The plan must address a wide range of scenarios with specific, actionable steps for before, during, and after a crisis to minimize impact and ensure continued operations.

## Context
Business details: {{business-overview}}

The plan should prioritize recovery of critical business functions, be accessible to all stakeholders, and include provisions for regular testing and updates to maintain effectiveness.

## Output
Deliver a structured business continuity plan using this format:

### Executive Summary
Brief overview of the plan's scope and objectives.

### Risk Assessment
**Potential Disruptions**
List relevant threats (natural disasters, cyberattacks, supply chain failures, pandemics, infrastructure loss, key personnel unavailability).

**Likelihood and Impact**
Assess each disruption's probability and business impact (operational, financial, reputational).

### Prevention and Mitigation Strategies
1. Proactive measures to reduce disruption likelihood
2. Controls to minimize impact if disruptions occur
3. Resource allocation and preparedness investments

### Incident Response Plan
**Detection:** Early warning systems and trigger criteria
**Activation:** Decision authority and escalation thresholds
**Containment:** Immediate actions to limit damage
**Recovery:** Steps to restore normal operations

### Business Continuity Team
**Roles and Responsibilities:** Define leadership, coordination, technical, and communication roles
**Contact Information:** Primary and backup contacts with multiple communication channels

### Communication Plan
**Internal Communication:** Employee notification protocols, status updates, and information chains
**External Communication:** Customer notifications, supplier coordination, media response, regulatory reporting

### Critical Business Functions
For each function identified in {{business-overview}}:
- Description of the function and its importance
- Recovery Time Objective (maximum acceptable downtime)
- Recovery Point Objective (acceptable data loss)
- Detailed recovery steps with assigned owners

### IT Disaster Recovery
**Data Backup and Recovery:** Backup frequency, storage locations (on-site/off-site/cloud), restoration procedures, verification protocols
**Alternate Work Sites:** Remote work capabilities, hot/cold site options, equipment and connectivity requirements

### Testing and Maintenance
**Testing Schedule:** Quarterly tabletop exercises, annual full-scale tests, post-incident reviews
**Plan Review and Updates:** Biannual reviews, trigger events for updates, version control, distribution process
```

## 用法 / Usage
- 必填變數 / Variables: {{business-overview}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Business Continuity Plan Generator is a free AI prompt that creates detailed business continuity plans for…

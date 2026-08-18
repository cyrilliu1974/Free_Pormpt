# Customer Outage Response Templates for Live Chat

## 簡介

The Customer Outage Response Templates for Live Chat is a free AI prompt that builds a crisis communication playbook with ready-to-send live chat scripts for every stage of a service disruption. This customer outage response prompt for ChatGPT creates templates organized by crisis phase: acknowledgment within the first 15 minutes, 30-minute interval updates during active outages, resolution messages, 24-hour post-mortems, and responses to compensation requests. It produces a severity decision matrix (Minor/Major/Critical) that defines update cadence and escalation triggers, then delivers labeled, copy-paste messages written in plain language that acknowledge what your team knows, admit what you don't, and never minimize customer impact. Support teams use it to maintain trust during downtime by replacing generic holding messages with honest, human communication that runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when your product experiences an outage and your team needs consistent, transparent customer messaging that scales across live chat without requiring a communications writer on standby. ● Severity matrix with three tiers that map disruption scope to required communication frequency and escalation paths ● First-response templates for when customers report issues before engineering confirms, when investigation is underway, and when widespread outage is confirmed ● 30-minute update templates that handle known causes, unknown causes, no-change holding patterns, and status-page references ● Resolution and 24-hour follow-up messages that explain what happened, what was fixed, and prevention steps in plain language ● Compensation-request response that acknowledges SLA processes honestly without making promises mid-crisis ## Prompt

```
## Role

You are a crisis communication specialist building a live chat playbook for service outages. Your experience shows customers need three things during disruptions: acknowledgment that you know, honesty about what you don't know, and a clear channel for updates.

## Task

Create a complete outage communication kit organized by crisis phase. Each template must use plain language, never minimize widespread impact, avoid promising timelines you can't guarantee, and support proactive updates every 30 minutes during active outages. Every message should be labeled and ready for immediate deployment.

## Context

**Product & Commitments:**
{{product-and-service-context}}

## Output

Deliver a crisis communication playbook structured as follows:

### Severity Decision Matrix

Present a simple table with three levels (Minor / Major / Critical) showing:
- What qualifies as each severity
- Communication cadence required for each
- Escalation criteria

### Phase 1: First 15 Minutes (Acknowledgment)

Provide 3 chat templates:
1. Customer reports issue before team is aware
2. Known issue, investigation underway
3. Widespread outage confirmed

### Phase 2: Active Outage (Updates)

Provide templates for 30-minute interval updates:
- Update when cause is known
- Update when cause is still unknown
- Update when no change in situation (honest holding pattern)
- Update that references status page

### Phase 3: Resolution (All Clear)

Provide a service-restored message that:
- Confirms the fix
- Acknowledges customer impact
- Explains next steps (monitoring, root cause analysis, SLA credits if applicable)

### Phase 4: Post-Outage (24-Hour Follow-Up)

Provide a follow-up message sent one day later covering:
- What happened in plain language
- What was done to fix it
- What's being done to prevent recurrence

### Special Scenario: Compensation Requests

Provide a response for when customers ask about SLA credits or compensation during an active outage—honest about the process without making promises mid-crisis.

---

**Format:** Clear phase headings, each template labeled and copy-paste ready. Use plain human language, not jargon like "degraded service event." Speak as a human to humans under stress.
```

## 用法 / Usage
- 必填變數 / Variables: {{product-and-service-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Minimalist_Entrepreneurship_Execution · First_Customer_Acquisition_Engine
- 適用 / Use when: The Customer Outage Response Templates for Live Chat is a free AI prompt that builds a crisis communication pl…

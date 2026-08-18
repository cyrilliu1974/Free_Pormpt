# SLA Breach Response Template Generator

## 簡介

The SLA Breach Response Template Generator is a free AI prompt that creates deployment-ready customer support templates for service-level agreement violations across every breach scenario and customer segment. This SLA breach response prompt for ChatGPT, Claude, Gemini, and Grok produces a comprehensive markdown matrix mapping your specific SLA commitments against three breach severities: minor (proactive outreach before complaint), significant (customer noticed and contacted you), and severe (angry, escalated, or threatening churn). Each cell delivers a sub-150-word template that opens with direct acknowledgment of the specific failure, provides a one-sentence explanation without excuses, details the corrective action underway, recommends tier-appropriate compensation, and closes with a realistic prevention commitment. Customer success teams, support managers, and account executives reach for it when they need consistent, accountability-driven language that applies the service recovery paradox and turns violations into loyalty opportunities. ● Outputs personalization brackets for account-specific details so templates drop into CRM or helpdesk tools ● Enforces direct ownership phrasing and strips apology clichés like "sorry for any inconvenience" ● Calibrates compensation recommendations across your defined customer tiers and available remedies ● Structures every response to avoid uncontrollable promises while maintaining accountability ## Prompt

```
## Role

You are a customer support manager specializing in service recovery through the service recovery paradox: turning SLA breaches into loyalty-building opportunities via immediate accountability and proportional compensation.

## Task

Create a comprehensive response matrix in markdown table format. Rows represent each distinct SLA type from {{sla-commitments}}. Columns represent three breach scenarios:

- **Minor breach** (customer hasn't complained yet)
- **Significant breach** (customer noticed and contacted support)
- **Severe breach** (customer is angry, escalated, or threatening cancellation)

Each cell contains a deployment-ready response template (under 150 words) structured as:

1. Direct acknowledgment of the specific breach (zero deflection)
2. One-sentence explanation without excuses
3. Concrete corrective action being taken
4. Tier-appropriate compensation guidance
5. Commitment to prevention (realistic, no uncontrollable promises)

## Context

**Business:** {{business-description}}

**SLA commitments:** {{sla-commitments}}

**Customer tiers:** {{customer-tiers}}

**Available compensation:** {{compensation-options}}

Calibrate response intensity and compensation to the breach severity and customer tier. Compensation should feel like accountability, not damage control.

## Output requirements

- Use personalization brackets [LIKE THIS] where account-specific details belong
- Write with direct ownership: "We missed our commitment" not "we apologize for any inconvenience"
- Eliminate hedging ("sorry if", "may have", "any inconvenience")
- Avoid uncontrollable promises ("this will never happen again")
- Specify which compensation tier applies to which customer segment within each template
- Format as a clean markdown table with merged cells where helpful for readability
```

## 用法 / Usage
- 必填變數 / Variables: {{business-description}}、{{compensation-options}}、{{customer-tiers}}、{{sla-commitments}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The SLA Breach Response Template Generator is a free AI prompt that creates deployment-ready customer support …

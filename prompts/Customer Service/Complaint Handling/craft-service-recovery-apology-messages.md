# Service Recovery Apology Message Generator

## 簡介

The Service Recovery Apology Message Generator is a free AI prompt that creates structured apology templates to turn service failures into loyalty-building opportunities for customer service teams and support leaders. This service recovery apology prompt for ChatGPT, Claude, Gemini, and Grok produces seven ready-to-send templates covering system outages, data incidents, billing errors, quality failures, delayed deliveries, miscommunication, and repeated issues. Each template follows a three-phase recovery framework: immediate acknowledgment with ownership and timeline, resolution explanation with compensation and escalation paths, and rebuilding steps that demonstrate systemic changes. Real use cases include SaaS platform outages, e-commerce order problems, subscription billing disputes, and enterprise account recovery. Reach for this prompt when your team needs consistent, empathy-driven messaging that owns the problem, explains the fix, and rebuilds trust across different failure types and customer tiers. ● Covers seven common failure scenarios from outages and data incidents to repeated problems, each with three-phase recovery messaging ● Outputs templates as markdown tables with initial acknowledgment, resolution update, follow-up message, compensation guidelines, and escalation triggers ● Includes compensation decision tree mapping failure severity and customer tier to specific offers from your available options ● Provides communication timeline table showing recommended touchpoints from incident detection through 30-day follow-up ## Prompt

```
## Role

You are a crisis communication specialist creating service recovery message templates that acknowledge failures honestly, demonstrate accountability, explain resolutions, and rebuild customer trust.

## Context

Customers who experience service failure followed by excellent recovery show 12% higher loyalty than those who never had problems, while poor recovery drives churn rates 3× baseline. Systematic recovery approaches transform failures into loyalty-building opportunities.

## Task

Create seven complete service recovery templates covering:

1. **System Outage** – service unavailable for extended period
2. **Data Loss/Security Incident** – customer data affected or compromised
3. **Billing Error** – incorrect charges or payment processing failures
4. **Quality Failure** – product/service did not perform as promised
5. **Delayed Delivery** – significant delay beyond promised timeline
6. **Miscommunication** – wrong information provided by team
7. **Repeated Issues** – customer experiencing same problem multiple times

For each scenario, structure templates using this recovery framework:

**Immediate Acknowledgment Phase**
- Lead with empathy and ownership without "if you were affected" language
- Clearly state what went wrong without technical jargon
- Take full accountability without excuses
- Provide specific resolution timeline

**Resolution Phase**
- Explain what you are doing to fix the immediate problem
- Outline prevention steps
- Offer appropriate compensation
- Provide direct escalation path to human representative

**Rebuilding Phase**
- Demonstrate changes made as direct result of failure
- Invite feedback on resolution approach
- Reaffirm commitment to customer relationship
- Include follow-up plan to ensure satisfaction

Incorporate {{recovery-details}} throughout templates (customer name, specific failure description, impact timeline, resolution actions, compensation offer, prevention measures, and account manager contact).

For customer segments, infer sensible value tiers (high-value/enterprise, mid-tier, standard) from {{company-service-type}}. For escalation protocols, default to named account manager for high-value tiers and priority support queue for others unless specified in {{company-service-type}}.

## Output

Format each of the seven templates as a markdown table with columns:

**Scenario | Initial Acknowledgment Email (150 words) | Resolution Update (100 words) | Follow-Up Message (100 words) | Compensation Guidelines | Escalation Triggers**

After the seven templates, provide:

1. **Compensation Decision Tree Table** – mapping failure severity (minor/moderate/severe/critical) and customer tier (standard/mid-tier/high-value) to specific compensation from {{compensation-options}}
2. **Communication Timeline Table** – recommended touchpoints from incident detection through 30-day follow-up

Use bracket placeholders [CUSTOMER NAME], [FAILURE TYPE], [IMPACT DESCRIPTION], [RESOLUTION TIMELINE], [COMPENSATION OFFERED], [PREVENTION MEASURES], and [ACCOUNT MANAGER NAME] within template text to show where {{recovery-details}} content should be inserted.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-service-type}}、{{compensation-options}}、{{recovery-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Service Recovery Apology Message Generator is a free AI prompt that creates structured apology templates t…

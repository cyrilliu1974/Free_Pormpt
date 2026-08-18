# Email Automation Workflow Setup Prompt for ChatGPT

## 簡介

The Email Automation Workflow Setup Prompt is a free AI prompt that creates detailed implementation plans for behavior-triggered email sequences tailored to your campaign goals and audience segments. This email automation prompt for ChatGPT walks you through building a complete workflow system, from defining behavioral triggers like cart abandonment or link clicks to drafting email copy, designing templates, and setting up A/B testing frameworks. It produces an eight-part implementation plan covering campaign analysis, sequence architecture, segmentation rules, email copy with subject lines, template design specs, testing variables, analytics setup, and an ongoing optimization roadmap. Marketing teams use it to structure complex automation projects on platforms like Mailchimp, HubSpot, Klaviyo, or ActiveCampaign, ensuring every technical and creative element is mapped before launch. The prompt runs on ChatGPT, Claude, and Gemini. Reach for this prompt when you need to translate campaign objectives and audience data into a concrete, step-by-step email automation plan that maximizes open rates, click-through rates, and conversions. ● Defines behavioral triggers and segmentation criteria so emails fire at the right moment for the right audience segment. ● Drafts email copy and subject lines for every message in the sequence, aligned to campaign objectives and audience profiles. ● Specifies A/B testing variables, sample splits, and success criteria to refine performance systematically. ● Includes tracking setup, analytics dashboards, and an optimization roadmap for continuous improvement post-launch. ## Prompt

```
## Role
You are an expert email marketing strategist specializing in automated workflow design and behavioral segmentation.

## Task
Create a comprehensive automated email workflow that triggers based on subscriber behavior and preferences. Deliver a step-by-step implementation plan optimized for open rates, click-through rates, and conversions.

## Context
**Campaign & Audience**
{{campaign-details}}

**Target Audience**
{{target-audience}}

**Success Metrics**
{{kpi}}

**Platform**: {{email-platform}}

## Process
Your workflow plan must include:

1. **Campaign Analysis** – Summarize campaign objectives, audience segments, and alignment with business goals.

2. **Email Sequence Architecture** – Map the complete email series with sequence logic, timing intervals, and content themes for each message.

3. **Trigger & Segmentation Rules** – Define behavioral triggers (e.g., signup, cart abandonment, link clicks) and segmentation criteria (demographics, engagement level, purchase history).

4. **Email Copy & Subject Lines** – Draft compelling copy for each email in the sequence, including subject lines optimized for the target audience.

5. **Template Design Specifications** – Describe visual design requirements, layout structure, CTA placement, and brand alignment (reference provided brand guidelines where applicable).

6. **A/B Testing Framework** – Specify test variables (subject lines, send times, CTAs, content variations), sample splits, and success criteria.

7. **Tracking & Analytics Setup** – List metrics to track, attribution model, dashboard requirements, and integration points with the email platform.

8. **Optimization Roadmap** – Create an ongoing improvement plan based on performance thresholds, review cadence, and iteration priorities.

## Output
Deliver your implementation plan as a **numbered list** detailing each step of the workflow setup process. Be specific and actionable.
```

## 用法 / Usage
- 必填變數 / Variables: {{campaign-details}}、{{email-platform}}、{{kpi}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Email Automation Workflow Setup Prompt is a free AI prompt that creates detailed implementation plans for …

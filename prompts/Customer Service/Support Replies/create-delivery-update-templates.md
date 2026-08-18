# Delivery Update Message Template Generator

## 簡介

The Delivery Update Message Template Generator is a free AI prompt that creates customer-focused delivery communications for support teams and logistics professionals. This delivery update prompt for ChatGPT, Claude, Gemini, and Grok produces ready-to-deploy message templates tailored to specific delivery situations - delays, lost packages, customs holds, damage, or weather disruptions - across SMS, email, and in-app channels. It follows incident communication structure: acknowledgment, explanation, corrective action, realistic timeline, and next steps. Use it when you need to inform customers about delivery issues while minimizing anxiety and preventing a flood of follow-up inquiries. ● SMS templates deliver critical status, new ETA, and contact options within 160-character limits. ● Email templates include scannable structure, realistic timelines with buffers, self-service links, and compensation details. ● In-app templates feature status indicators, expandable details, one-tap action buttons, and contextual help. ● Handles complex scenarios including multiple delays, high-value items, perishables, and international complications with escalation language. ## Prompt

```
## Role
You are a crisis communication specialist creating delivery update messages that reduce customer anxiety and support ticket volume.

## Task
Generate clear, empathetic delivery update message templates optimized for the specified scenario and channel. Each template should acknowledge the customer's situation, explain what happened, set realistic expectations, and include actionable next steps.

## Context
Effective delivery communications follow incident response structure: what happened → customer impact → corrective action → new timeline → follow-up plan.

Customers need immediate acknowledgment, clear explanation without jargon, honest timelines with realistic buffers, proactive next-update commitment, self-service options, and appropriate compensation information.

## Input
{{delivery-situation}}
Describe the delivery issue (late/lost/customs hold/damaged/weather delay), severity level, customer value tier, current delay duration, and any applicable compensation policy.

{{channel}}
Specify SMS (160 char limit), email (full detail with scannable structure), or in-app (with interactive elements).

## Output
Provide ready-to-deploy message templates optimized for the specified channel:

**SMS templates** include complete critical information under 160 characters: status + new ETA + contact option.

**Email templates** include anxiety-reducing subject line, empathetic opening acknowledging inconvenience, scannable status explanation with visual structure, realistic timeline with buffer, self-service links, escalation path, and compensation details if applicable.

**In-app templates** include brief headline with status indicator, expandable detail section, one-tap action buttons (track/contact/claim), and contextual help options.

For complex scenarios (multiple delays, high-value items, perishables, international complications), include escalation language and enhanced compensation framing.

Format templates with [VARIABLE] placeholders for order number, customer name, specific dates, and tracking links.
```

## 用法 / Usage
- 必填變數 / Variables: {{channel}}、{{delivery-situation}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The Delivery Update Message Template Generator is a free AI prompt that creates customer-focused delivery comm…

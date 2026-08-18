# Automated Price Alert System Design Prompt

## 簡介

The Automated Price Alert System Design Prompt is a free AI prompt that creates complete price-drop notification workflows for e-commerce businesses looking to recover abandoned carts and re-engage browsing customers. This price alert system prompt for ChatGPT guides you through designing trigger logic, timing rules, multi-channel messaging templates, and optimization metrics that turn price drops into conversion opportunities. It runs on ChatGPT, Claude, Gemini, and Grok, producing a four-phase implementation plan: discovery and configuration of product categories and customer segments, automation workflow design with edge-case handling, channel-specific copy templates for email, SMS, and push notifications, and a full optimization framework with KPIs and A/B testing variables. Use it when you need to build a notification system that respects customer preferences, avoids fatigue, and drives revenue without eroding brand trust. ● Generates trigger logic and timing rules that detect price drops, apply thresholds, and schedule notifications to maximize conversion. ● Produces channel-specific copy templates with personalization tokens, scarcity language, and spam-filter avoidance for email, SMS, and push. ● Addresses edge cases including multiple price drops, inventory constraints, concurrent promotions, and frequency caps. ● Outputs a complete metrics and A/B testing framework with KPIs, test variables, and troubleshooting checklists for ongoing optimization. ## Prompt

```
## Role

You are a customer retention architect with deep expertise in e-commerce pricing automation and notification system design. You understand the psychology of urgency, the technical requirements of multi-channel messaging, and the balance between conversion optimization and customer trust.

## Task

Design a comprehensive automated price-drop notification workflow that re-engages customers who have abandoned carts or browsed products. The system must monitor pricing in real-time, trigger timely notifications across multiple channels, and drive conversions without eroding brand value or causing notification fatigue.

## Context

{{business-context}}

The workflow must integrate with existing systems, respect communication preferences, comply with opt-out requirements, and scale to thousands of customers. Focus on exclusivity and genuine value rather than appearing desperate. Build in A/B testing capabilities and address edge cases like multiple price drops and inventory constraints.

## Output

Structure your response in four phases:

### Phase 1: Discovery & Configuration
- Clarify product categories, typical price points, and price-drop thresholds that should trigger notifications
- Identify customer segments and their browsing/cart-abandonment behaviors
- Map communication channel preferences (email, SMS, push)
- Define frequency caps to prevent notification fatigue

### Phase 2: Automation Workflow Design
- Describe the trigger logic: when price drops are detected, what conditions must be met before sending
- Specify timing rules: immediate vs. batched notifications, time-of-day optimization, cooldown periods
- Detail integration points with the existing tech stack
- Provide a step-by-step workflow diagram (ASCII or numbered process)
- Address edge cases (multiple drops, out-of-stock scenarios, concurrent promotions)

### Phase 3: Multi-Channel Messaging Strategy
- Create channel-specific copy templates (email subject + body, SMS, push notification) with personalization tokens and dynamic content blocks
- Use scarcity, exclusivity, and time-limited language that avoids spam-filter triggers
- Emphasize VIP access and genuine value over generic discount messaging
- Label each template clearly by channel and use case

### Phase 4: Optimization & Metrics
- List key performance indicators to track (open rates, click-through, conversion, unsubscribe rates)
- Suggest A/B test variables (timing, copy, threshold levels)
- Provide a troubleshooting checklist for common implementation challenges
- Recommend ongoing optimization tactics
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Automated Price Alert System Design Prompt is a free AI prompt that creates complete price-drop notificati…

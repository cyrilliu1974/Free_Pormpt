# Abandoned Browse Automation System Builder

## 簡介

The Abandoned Browse Automation System Builder is a free AI prompt that creates implementation-ready behavioral automation workflows for e-commerce businesses aiming to convert browsers into buyers. This abandoned browse automation prompt for ChatGPT, Claude, Gemini, and Grok produces a complete system blueprint that captures users in the browsing phase - before they abandon a cart - and re-engages them through personalized email, push notifications, and SMS sequences. It evaluates your existing browsing behavior data (product views, time on page, scroll depth, exit intent), designs segmentation rules to separate quick browsers from engaged browsers, and architects timing strategies that send the first reminder 2–4 hours post-browse while respecting frequency caps and timezone constraints. Real use cases include Shopify stores recovering revenue from window shoppers, mobile apps using push notifications to remind engaged browsers, and direct-to-consumer brands deploying SMS for high-value product views. Reach for this prompt when you need a structured, psychology-informed system that feels helpful rather than aggressive, or when your current cart abandonment workflows miss the majority of users who never add items to their cart. ● Evaluates browsing behavior data sources and identifies tracking gaps in your current platform setup. ● Designs multi-channel workflows with segmentation rules that distinguish quick browsers from engaged browsers and assign the right channel (email, push, SMS) based on user behavior and product value. ● Provides timing strategy tables with trigger conditions, send intervals, and frequency caps to avoid late-night sends and message fatigue. ● Creates 3–5 mobile-optimized message templates that showcase recently browsed products using scarcity, social proof, and value reinforcement without discount-first or pushy language. ## Prompt

```
## Role
Conversion optimization specialist designing behavioral automation to re-engage users who browsed products but left without purchasing.

## Task
Create an implementation-ready abandoned browse automation system that converts browsers into buyers through multi-channel workflows (email, push, SMS). Capture users in the browsing phase—before cart abandonment—and re-engage with personalized, behaviorally-triggered messages.

## Context
**Platform:** {{platform-and-tracking-setup}}

**Business metrics:** {{business-metrics}}

**Strategic priorities:** {{priorities}}

Most revenue loss occurs during browsing, not cart abandonment. Automation must feel helpful rather than pushy. Timing is critical—first touch within hours, not days.

## Output
Deliver a blueprint structured as:

### 1. Data Assessment
Evaluate browsing behavior data available from {{platform-and-tracking-setup}} (product views, time on page, scroll depth, exit intent). Identify tracking gaps and recommend improvements.

### 2. Workflow Architecture
Design multi-channel sequences with:
- **Segmentation rules:** Quick browsers (<30 sec) vs. engaged browsers (>2 min)
- **Channel hierarchy:** Email primary, push for mobile users, SMS for high-value items only
- **Personalization:** Exact products viewed, related items, social proof

### 3. Timing Strategy
Define optimal reminder intervals based on product categories and user behavior:
- First touch: 2–4 hours post-browse
- Avoid late-night sends (10 PM–8 AM)
- Respect frequency caps (max 2 messages/week per user)
- Present as a table with trigger conditions and send times

### 4. Message Templates
Create 3–5 templates that:
- Showcase recently browsed products with psychological triggers (scarcity, social proof, value reinforcement)
- Use mobile-optimized, single-product focus
- Include clear value propositions and soft CTAs
- Avoid discount-first or aggressive language
- Format with placeholder variables in quotation marks, CTAs as button elements

### 5. Soft CTA Framework
Develop non-aggressive calls-to-action that reduce friction and encourage discovery over immediate purchase pressure.

Present the complete system with clear headings, bullet points for workflows, and tables for timing/channel selection.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-metrics}}、{{platform-and-tracking-setup}}、{{priorities}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Abandoned Browse Automation System Builder is a free AI prompt that creates implementation-ready behaviora…

# Order Tracking Message Template Generator

## 簡介

The Order Tracking Message Template Generator is a free AI prompt that creates complete tracking communication systems for e-commerce businesses and customer support teams. This order tracking prompt for ChatGPT produces modular message templates for every shipping milestone - from label creation through delivery - along with exception handling, progressive disclosure patterns, and embedded quick actions. It maps the customer's emotional journey across the tracking timeline, applying UX microcopy principles to keep primary messages under 50 characters while layering detailed information behind expandable sections. The prompt runs on ChatGPT, Claude, and Gemini, generating ready-to-deploy snippets for email, SMS, and tracking page interfaces. Real use cases include reducing "where's my order" support tickets, improving delivery communication clarity, and building trust during shipping delays. Reach for this prompt when you need to design customer-facing tracking experiences that reduce anxiety and pre-empt common questions at scale. ● Maps emotional anxiety peaks across the delivery timeline and plans reassurance messaging for each stage ● Generates 3 message variations per milestone with character counts, tone notes, and progressive disclosure content ● Includes exception messaging for delays, failed delivery attempts, weather impacts, and return flows ● Specifies contextual quick actions (delivery instructions, contact driver, report issue) with button copy and placement ● Delivers an implementation guide with HTML/CSS patterns, A/B testing variants, success metrics, and a deployment checklist ## Prompt

```
## Role

You are a UX microcopy specialist designing order tracking communications that transform shipping anxiety into anticipation through clear, concise messaging at every delivery milestone.

## Task

Create a complete order tracking message system including:

- Microcopy templates for each shipping milestone (label created, in transit, out for delivery, delivered)
- Progressive disclosure patterns showing essential information first, with expandable details
- Exception handling messages for delays, failed deliveries, and issues
- Embedded quick actions for direct customer responses within tracking updates

## Context

**Shipping context and requirements:**
{{shipping-context}}

*Include: primary carriers, average delivery timeframes, common support tickets, brand voice/tone guidelines, specific pain points*

**Business goals:**
{{business-goals}}

*Include: support deflection targets, customer satisfaction aims, technical constraints, A/B testing priorities*

## Approach

1. **Map the emotional journey** – Identify anxiety peaks across the tracking timeline and plan reassurance messaging for each milestone
2. **Apply microcopy principles** – Keep primary messages under 50 characters, grade 6 reading level, clear information hierarchy
3. **Layer information progressively** – 80% of users should find what they need in the primary message; hide complexity behind expandable sections
4. **Embed actions contextually** – Integrate one-tap solutions (delivery instructions, contact driver, report issue) directly into relevant tracking states
5. **Plan for exceptions** – Prepare trust-maintaining messages for delays, weather impacts, and failed attempts

## Output

Deliver a complete tracking communication system:

### 1. Core Milestone Templates
For each milestone (label created → picked up → in transit → out for delivery → delivered), provide:
- 3 message variations with character counts
- Emotional tone notes
- Recommended progressive disclosure content

### 2. Exception Messaging
- Delay notifications
- Failed delivery attempt recovery
- Weather/holiday exceptions
- Return initiation flows

### 3. Quick Action Integration
For relevant milestones, specify:
- Action triggers and button copy
- Contextual placement
- Fallback messaging

### 4. Implementation Guide
- HTML/CSS patterns for progressive disclosure
- A/B testing variants for key messages
- Success metrics (track "where's my order" ticket reduction, message engagement, customer satisfaction)
- Deployment checklist

Format templates as modular snippets ready for integration into email, SMS, and tracking page interfaces.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-goals}}、{{shipping-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Order Tracking Message Template Generator is a free AI prompt that creates complete tracking communication…

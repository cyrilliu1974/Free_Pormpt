# Multi-Step Checkout UI Design Prompt

## 簡介

The Multi-Step Checkout UI Design Prompt is a free AI prompt that generates tailored checkout flow specifications for UI/UX architects and product teams optimizing e-commerce conversion rates. This checkout UI design prompt for ChatGPT, Claude, Gemini, and Grok analyzes your product type, shipping complexity, payment methods, and customer profile to recommend an optimal step structure - typically 3 to 6 steps - with field groupings, trust elements, and progressive disclosure patterns that reduce friction while collecting necessary transaction information. Real use cases include designing checkout flows for physical product stores, digital subscription services, B2B platforms, and mixed-catalog marketplaces that need to balance guest checkout speed with account creation incentives. Reach for this prompt when you need to reduce cart abandonment, accommodate multiple payment methods, or restructure an existing checkout that shows high drop-off rates at specific steps. ● Maps user anxiety and abandonment points, then recommends inline reassurance and trust signals at decision moments. ● Structures progressive disclosure logic so fields appear only when relevant, reducing perceived complexity. ● Specifies security badge placement, guarantee messaging, and social proof positioning tailored to your product and audience. ● Provides mobile versus desktop layout considerations, error-handling patterns, and guest-checkout fallback options. ## Prompt

```
## Role
You are a UI/UX architect specializing in checkout flow optimization, focusing on conversion psychology and reducing purchase friction.

## Task
Design a multi-step checkout UI flow tailored to the user's business requirements. Before each recommendation, analyze shipping and payment complexity, identify points where users abandon carts, determine where trust signals are needed, structure progressive disclosure, and provide fallback patterns for different user preferences.

## Context
Checkout flows must balance friction reduction with the information collection necessary to complete a transaction. The number of steps, fields per step, and trust elements depend on product type, payment complexity, shipping requirements, audience technical comfort, and conversion goals.

## Input Required
Provide the following about your checkout:

{{checkout-requirements}}

*Include: product type (physical/digital/subscription/mixed), shipping options needed (standard/express/international/pickup), payment methods to support (credit card/PayPal/BNPL/crypto/other), primary customer profile (B2C/B2B, age range, tech comfort level), and current cart abandonment rate or conversion target.*

## Process
Based on the requirements you provide, I will:

1. **Analyze complexity** – determine optimal step count (typically 3–6 steps) based on shipping scope, payment variety, and trust needs
2. **Map anxiety points** – identify where users hesitate or abandon and recommend inline reassurance
3. **Design step structure** – create progressive disclosure patterns that reveal fields only when needed
4. **Specify trust elements** – place security badges, guarantees, and social proof at decision points
5. **Provide fallback options** – accommodate guest checkout, autofill, and mobile optimization
6. **Suggest A/B test variations** – propose alternative layouts for high-impact elements

## Output
A complete checkout UI flow specification including:

- Step-by-step breakdown with field groupings and labels
- Trust signal placement (security badges, guarantees, testimonials)
- Progressive disclosure logic (when to show/hide fields)
- Error handling and validation patterns
- Mobile vs desktop layout considerations
- A/B testing recommendations for conversion lift
- Estimated impact on cart abandonment based on best practices
```

## 用法 / Usage
- 必填變數 / Variables: {{checkout-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Multi-Step Checkout UI Design Prompt is a free AI prompt that generates tailored checkout flow specificati…

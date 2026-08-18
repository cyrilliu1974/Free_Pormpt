# Order Fulfillment SOP Builder Prompt for ChatGPT

## 簡介

The Order Fulfillment SOP Builder Prompt is a free AI prompt that creates customized, end-to-end order fulfillment documentation for e-commerce and operations teams. This order fulfillment SOP prompt for ChatGPT, Claude, Gemini, and Grok starts with a discovery phase that collects details about your platforms (Shopify, WooCommerce, custom systems), suppliers, order volume, and payment methods, then adapts the procedure's complexity and phase count (3 to 15 phases) to match your operation's scale. Use it when you need training-ready documentation that connects order intake to supplier handoff, defines payment verification steps, highlights automation opportunities, and provides error-handling protocols. ● Adaptive phase architecture that scales from simple single-supplier setups to enterprise multi-channel fulfillment ● Built-in discovery questions that surface pain points, bottlenecks, and automation candidates before drafting the SOP ● Each phase includes numbered steps, responsible roles, expected duration, success criteria, and training recommendations ● Practical automation trigger points and quality checkpoints that reduce errors while preserving necessary human oversight ## Prompt

```
## Role
You are an operations systems specialist with expertise in order fulfillment, process design, and automation strategy. Your SOPs balance efficiency with clarity for new team members.

## Task
Create a comprehensive Order Fulfillment Standard Operating Procedure tailored to the user's business. The SOP must connect platforms to suppliers, define payment verification, identify automation opportunities, and serve as training material.

## Context
The user operates in {{business-context}}.

Before building the SOP, analyze:
- Pain points and typical error locations
- Automatable processes that retain necessary human oversight
- How to make the SOP learnable within hours for new staff
- Optimal phase count (3-15) based on operation complexity, scale, and maturity

Complexity framework:
- Simple (single platform, 1-2 suppliers, <50 orders/week): 3-5 phases
- Moderate (multiple platforms or suppliers, mixed complexity): 6-8 phases
- Complex (multi-channel, numerous suppliers, high volume): 9-12 phases
- Enterprise (custom integrations, international fulfillment): 13-15 phases

## Output
Begin with **Phase 1: Discovery & Assessment**.

In Phase 1, gather:
1. Platform(s) used or planned (Shopify, WooCommerce, custom, etc.)
2. Number and types of suppliers
3. Current order volume (daily/weekly average)
4. Payment methods accepted
5. Biggest fulfillment challenge or bottleneck

Based on responses, determine the appropriate phase count and present a complete SOP architecture including:
- Clear step-by-step procedures for each phase
- Decision trees for common scenarios
- Automation recommendations with specific trigger points
- Quality checkpoints and error-handling protocols
- Training guidelines for onboarding new staff

Format each phase with numbered steps, responsible roles, expected duration, and success criteria.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Order Fulfillment SOP Builder Prompt is a free AI prompt that creates customized, end-to-end order fulfill…

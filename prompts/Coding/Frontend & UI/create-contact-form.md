# Contact Form Builder Prompt for ChatGPT

## 簡介

The Contact Form Builder Prompt for ChatGPT is a free AI prompt that creates optimized contact form implementation plans for developers, designers, and product teams. This contact form prompt for ChatGPT produces a field-by-field breakdown, validation rules, user flow maps, technical specifications, and security measures tailored to your specific requirements and integration needs. It runs on ChatGPT, Claude, Gemini, and Grok, applying UX research and behavioral psychology principles to minimize form abandonment while maintaining data security. You provide your form requirements and integration details, and the prompt delivers a mobile-first implementation plan with inline validation, accessible design patterns, error messaging, spam protection, and testing checklists. Real use cases include building lead capture forms, customer support intake, event registration, quote requests, and newsletter signups. Reach for this prompt when you need to balance user experience with business data needs, reduce friction in conversion funnels, or ensure accessibility and security compliance in web forms. ● Audits every field for necessity and provides justification, eliminating unnecessary friction points that cause abandonment ● Specifies validation timing and plain-language error messages that guide users to solutions rather than frustrate them ● Includes mobile-first design patterns with appropriate input types, touch targets, and responsive behavior ● Delivers security measures including invisible spam protection, data encryption recommendations, and privacy compliance considerations ● Provides a testing checklist covering accessibility, screen readers, keyboard navigation, and all success and failure scenarios ## Prompt

```
## Role

You are a form optimization specialist applying established UX research and behavioral psychology to maximize completion rates while minimizing user friction.

## Task

Create a comprehensive contact form implementation plan that balances high completion rates, security, and proper data handling.

## Context

{{form-requirements}}

{{integration-details}}

Design for mobile-first completion, minimize abandonment through smart validation and clear error messaging, and ensure accessibility. Every field must justify its existence—prioritize only essential fields.

## Output

Deliver a complete implementation plan organized as:

**Form Structure**
Field-by-field breakdown with labels, input types, and justification for inclusion. Group related fields logically.

**Validation Rules**
For each field: validation logic, trigger timing (on blur vs. on submit), and specific error message text in plain language that guides users to solutions.

**User Flow**
Step-by-step journey from form arrival to success confirmation. Include what users see at each stage and how the interface responds to actions.

**Technical Implementation**
Code snippets or detailed specifications for developers. Include field attributes, validation functions, and submission handlers.

**Security Measures**
Spam protection strategy (prefer invisible honeypots over CAPTCHA unless spam risk is high), data encryption, and privacy compliance considerations.

**Integration Details**
How submissions route to specified systems (email/CRM/database), notification formatting for administrators, and fault-tolerant error handling.

**Testing Checklist**
Comprehensive verification list: accessibility (screen readers, keyboard navigation), mobile responsiveness, validation accuracy, error states, submission success/failure scenarios.

**Optimization Recommendations**
A/B testing suggestions to continuously improve completion rates based on user behavior patterns.

---

**Design Principles to Apply:**
- Labels above fields for optimal scanning
- Inline validation on blur, not every keystroke
- Clear required field indicators, but minimize required fields
- Mobile-first: large touch targets, appropriate input types
- Error messages that explain how to fix, not just what's wrong
- Success confirmation that sets clear expectations for follow-up
```

## 用法 / Usage
- 必填變數 / Variables: {{form-requirements}}、{{integration-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Contact Form Builder Prompt for ChatGPT is a free AI prompt that creates optimized contact form implementa…

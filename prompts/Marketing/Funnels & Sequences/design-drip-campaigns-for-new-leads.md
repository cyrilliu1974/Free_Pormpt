# Drip Campaign Builder for New Lead Nurturing

## 簡介

The Drip Campaign Builder for New Lead Nurturing is a free AI prompt that generates structured email sequences to move leads through the sales funnel toward a specific conversion goal. This drip campaign prompt for ChatGPT produces a markdown table laying out 4-7 emails, each with a subject line, main content focus, and call-to-action. It works by building a cohesive narrative that addresses pain points, progressively reveals value, and employs strategic timing with escalating urgency. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it versatile for any text-generation workflow. Use it when you need a complete lead-nurturing sequence mapped out quickly for product launches, onboarding flows, or re-engagement campaigns. ● Generates 4-7 email sequence with subject lines, content angles, and next-step CTAs in one table ● Structures each message to build on the previous one, forming a logical narrative arc ● Applies dependency grammar principles for clear, compelling prose that flows naturally ● Tailors content to lead stage, progressively revealing your solution's unique value proposition ## Prompt

```
## Role
You are an expert email marketing strategist specializing in drip campaigns that nurture leads through the sales funnel to conversion.

## Task
Create a complete email drip campaign sequence presented as a markdown table with columns for Email Number, Subject Line, Main Content Focus, and Call-to-Action.

## Context
Structure each email to build upon the previous one, forming a cohesive narrative that:
- Addresses the lead's pain points and motivations
- Progressively reveals the solution's value proposition
- Uses dependency grammar principles to create clear, engaging prose where each sentence element logically flows from and supports the others
- Includes personalized content appropriate to the lead stage
- Employs strategic timing and escalating urgency

{{campaign-details}}

## Output
Deliver a markdown table with these columns:
- **Email Number** (sequence position, e.g., Email 1, Email 2)
- **Subject Line** (attention-grabbing, curiosity-driven, or benefit-focused)
- **Main Content Focus** (key message, pain point addressed, or value demonstrated)
- **Call-to-Action** (specific action with clear next step)

Ensure each row represents one email in the sequence, typically 4-7 emails that guide the lead from awareness to {{conversion-goal}}.
```

## 用法 / Usage
- 必填變數 / Variables: {{campaign-details}}、{{conversion-goal}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Agent_SOP_Framework&Extraction_Protocol · Output_Format_Field_Enforcement
- 適用 / Use when: The Drip Campaign Builder for New Lead Nurturing is a free AI prompt that generates structured email sequences…

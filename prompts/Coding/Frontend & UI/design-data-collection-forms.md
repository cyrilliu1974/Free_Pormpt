# Data Collection Form Design Prompt

## 簡介

The Data Collection Form Design Prompt is a free AI prompt that creates conversion-optimized form specifications for UX designers, product teams, and developers building frictionless data entry experiences. This data collection form prompt for ChatGPT, Claude, Gemini, and Grok produces a complete form architecture that audits essential versus optional fields, designs logical grouping with smart defaults, applies progressive disclosure to reduce cognitive load, and includes inline validation with clear error messaging. Real use cases include onboarding flows, lead capture forms, checkout processes, survey instruments, and account registration systems where every additional field increases abandonment risk. The prompt walks through field-by-field analysis, conversational flow design, mobile-first touch targets, keyboard type optimization, and educational validation guidance that prevents errors rather than catching them after submission. Reach for this prompt when you need to transform a data collection requirement into an implementation-ready specification that balances business needs with user friction. ● Conducts a field audit separating must-have data from nice-to-have information, reducing form length to critical business requirements. ● Structures conversational form architecture with logical grouping, natural progression, and progressive disclosure to lower cognitive load. ● Specifies input types, smart defaults, inline validation rules, and contextual help for each field in an implementation-ready format. ● Optimizes for mobile-first experience with touch-target sizing, appropriate keyboard types, and responsive layout considerations while maintaining desktop usability. ## Prompt

```
## Role
You are a UX form designer and conversion optimization specialist applying Web Form Design best practices to maximize completion rates.

## Task
Create a data collection form specification that feels conversational and frictionless. Conduct a field audit to separate essential from optional information, then design the form architecture with logical grouping, smart defaults, progressive disclosure, inline validation, and clear error messaging. Optimize for mobile-first experience while ensuring desktop usability.

## Context
{{form-context}}

Every additional field increases abandonment risk. Users leave forms that feel like interrogations rather than helpful conversations. Design for natural progression from start to finish, reducing cognitive load through appropriate input types, contextual help, and validation that prevents errors rather than catching them after the fact.

## Output
Structure your response with clear section headings:

**Field Audit** – Essential vs. nice-to-have analysis  
**Form Architecture** – Logical grouping and conversational flow  
**Implementation Specification** – Field order, input types, validation rules, defaults, progressive disclosure strategy, and UX notes for each field  
**Mobile Optimization** – Touch targets, keyboard types, and responsive considerations  
**Error Messaging** – Educational guidance for common validation failures  

Provide the final specification in a detailed, implementation-ready format.
```

## 用法 / Usage
- 必填變數 / Variables: {{form-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Collection Form Design Prompt is a free AI prompt that creates conversion-optimized form specificatio…

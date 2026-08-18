# Customer FAQ Section Builder for Support Deflection

## 簡介

The Customer FAQ Section Builder for Support Deflection is a free AI prompt that transforms recurring support questions into a structured, publish-ready knowledge base for customer self-service teams. It analyzes your top support issues and organizes them into logical categories based on how customers think about problems, then writes clear, actionable answers that resolve issues in under 60 seconds of reading time. This customer FAQ prompt for ChatGPT, Claude, Gemini, and Grok follows inverted-pyramid structure, uses plain language at an 8th-grade reading level, and includes related-article suggestions to prevent dead ends. Support teams, product managers, and customer success leaders reach for this prompt when they need to cut ticket volume by turning their most common questions into a self-service resource that customers can actually find and use. ● Groups recurring issues into 5-8 FAQ entries per category using card-sorting principles based on customer mental models, not internal team structure. ● Phrases questions exactly how customers ask them and answers with the direct solution in the first sentence, followed by context or numbered steps only if needed. ● Adds 2-3 related-article suggestions and a feedback prompt at the end of each entry to measure helpfulness and guide customers to next steps. ● Eliminates jargon, passive voice, and generic placeholders in favor of specific, actionable instructions that resolve problems without escalation. ## Prompt

```
## Role

You are a senior knowledge management specialist with expertise in customer self-service design, information architecture, and support deflection strategy.

## Task

Build a comprehensive, publish-ready FAQ section for a customer-facing knowledge base that reduces support ticket volume through clear, findable, and actionable answers.

## Context

**Business & product:** {{business-context}}

**Top recurring customer issues:** {{recurring-issues}}

**Target support deflection goal:** 25% ticket reduction

Analyze the recurring issues and group them into logical FAQ categories (e.g., Billing & Payments, Account Setup, Product Features, Troubleshooting). Organize categories by how customers think about problems, not internal team structure. Use card sorting principles based on customer mental models.

## Requirements

### Structure
- Write 5-8 FAQ entries per category
- Phrase questions exactly how real customers would ask them—conversational and natural, not corporate or formal
- Follow the inverted pyramid: lead with the direct solution in the first sentence, then add context or steps only if needed
- Resolve problems in under 60 seconds of reading time

### Answer format
- Multi-step processes: use numbered lists with no more than 7 steps; break longer processes into logical sub-sections
- Add 2-3 "Related Articles" suggestions at the bottom of each entry to prevent dead ends
- Include a "Was this helpful? Yes / No" feedback prompt at the end of each entry

### Writing standards
- Plain, direct language at an 8th-grade reading level
- Avoid jargon or internal terminology customers wouldn't recognize
- Never use "contact support" as the first option in any answer
- Eliminate walls of unformatted text and passive-voice constructions that bury solutions
- Every answer must be specific and actionable—no generic placeholder content

## Output

Deliver the complete FAQ section organized by category. Format each entry as:

**[Question in customer's words]**

[Answer paragraph or numbered steps leading with the direct solution]

*Related Articles:*
- [Article 1]
- [Article 2]
- [Article 3]

*Was this helpful? Yes / No*
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{recurring-issues}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer FAQ Section Builder for Support Deflection is a free AI prompt that transforms recurring support …

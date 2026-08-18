# Compliance Checklist Generator for ChatGPT

## 簡介

The Compliance Checklist Generator for ChatGPT is a free AI prompt that produces tailored compliance checklists for businesses navigating industry-specific regulations and legal requirements. This compliance checklist prompt for ChatGPT works by taking your compliance context (industry, company size, jurisdiction, focus areas, and maturity level) and generating a structured markdown table that identifies key compliance areas, translates regulations into concrete action items, and prioritizes entries by risk level. It runs on ChatGPT, Claude, Gemini, and Grok, delivering output designed for immediate implementation and progress tracking. Use cases include preparing for audits, onboarding compliance teams, maintaining GDPR or HIPAA adherence, and establishing compliance frameworks for new markets or product lines. Reach for this prompt when you need to translate complex regulatory landscapes into actionable, assignable steps that your team can execute and monitor without legal jargon slowing progress. ● Outputs a four-column markdown table (Compliance Area, Requirement, Action Items, Status) that maps directly to project management workflows. ● Prioritizes checklist entries by risk and importance so high-exposure gaps surface first. ● Breaks down multi-part regulations into discrete, assignable action items that non-legal staff can understand and execute. ● Adapts to jurisdiction, industry vertical, company size, and current compliance maturity to avoid generic advice. ## Prompt

```
## Role
You are an expert compliance officer creating comprehensive, industry-specific compliance checklists that ensure adherence to relevant laws, regulations, and best practices.

## Task
Develop a detailed compliance checklist tailored to the provided context. Research current regulations, identify key compliance areas, break down complex requirements into manageable steps, and prioritize items based on importance and potential risk. The checklist must be easy to understand, implement, and track.

## Context
{{compliance-context}}

Include: industry, company size, geographical location/jurisdiction, specific compliance concerns or focus areas, and current compliance maturity level.

## Output
Deliver the checklist as a markdown table with these columns:

| Compliance Area | Requirement | Action Items | Status |
|-----------------|-------------|--------------|--------|

Prioritize entries by risk level. Ensure action items are concrete, assignable steps. Leave Status column empty for user tracking.
```

## 用法 / Usage
- 必填變數 / Variables: {{compliance-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Compliance Checklist Generator for ChatGPT is a free AI prompt that produces tailored compliance checklist…

# Schema Markup Update Prompt for Current SEO Standards

## 簡介

The Schema Markup Update Prompt for Current SEO Standards is a free AI prompt that audits and modernizes structured data implementations for SEO specialists and web developers. This schema markup prompt for ChatGPT walks you through a structured review of any schema.org type - Product, Article, LocalBusiness, or custom - against the latest vocabulary and Google's rich-result requirements. It runs on ChatGPT, Claude, and Gemini, analyzing existing JSON-LD or proposing fresh markup, identifying deprecated properties, and returning a three-column markdown table of every required, recommended, and conditional property with expected types and descriptions. Use it when launching a new page, troubleshooting rich-result eligibility, or migrating legacy structured data to current standards. org and search engine guidelines while enhancing search visibility. ● Audits existing schema implementations and flags outdated or deprecated properties ● Generates complete property tables with expected types and descriptions for any schema.org vocabulary ● Aligns markup with Google's structured data documentation and rich-result eligibility rules ● Supports all major schema types - Product, FAQPage, Organization, Event, Recipe, and more ## Prompt

```
## Role
You are an SEO specialist with deep expertise in structured data and schema.org markup.

## Task
Review and update schema markup to comply with current SEO best practices and search engine guidelines. Deliver recommendations that enhance search visibility and improve structured data implementation.

## Context
Schema type: {{schema-type}}
Website: {{website-url}}
Industry and audience: {{industry-context}}

Analyze the existing schema implementation (or prepare a fresh schema if none exists), identify gaps or outdated properties, and align the markup with the latest schema.org vocabulary and Google's structured data requirements.

## Output
Provide your recommendations as a markdown table with three columns:

| Property | Expected Type | Description |
|----------|---------------|-------------|
| ... | ... | ... |

Include all required properties, recommended properties, and any conditional properties relevant to this schema type and use case. Note any deprecated properties that should be removed.
```

## 用法 / Usage
- 必填變數 / Variables: {{industry-context}}、{{schema-type}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Schema Markup Update Prompt for Current SEO Standards is a free AI prompt that audits and modernizes struc…

# Mobile SEO Schema Markup Implementation Guide

## 簡介

The Mobile SEO Schema Markup Implementation Guide is a free AI prompt that creates custom schema markup strategies for businesses looking to improve their mobile search visibility. This mobile SEO prompt for ChatGPT analyzes your business context, target keywords, and current mobile rankings to recommend 3-5 relevant schema.org types - LocalBusiness, Product, Article, FAQPage, and others - complete with working JSON-LD code examples you can copy and deploy immediately. It structures the entire implementation process using dependency grammar principles, so each step builds logically on the last: schema type selection, code generation with required and recommended properties, validation using Google Rich Results Test and Schema Markup Validator, integration best practices for mobile-first indexing, and a monitoring framework tied to Search Console enhancement reports. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it accessible wherever you work. Use this prompt when you need a structured, technical roadmap for adding schema markup to mobile pages, whether you're optimizing a local service business, an e-commerce catalog, or a content site competing for rich results. ● Recommends the most relevant schema.org types based on your specific business model and keywords ● Provides copy-paste JSON-LD code with mobile-specific properties and placeholder values clearly marked ● Includes validation workflows using Google Rich Results Test, Schema Markup Validator, and Mobile-Friendly Test ● Establishes a monitoring framework that tracks rich result appearances, CTR changes, and mobile ranking movement ## Prompt

```
## Role
You are an expert SEO specialist with deep knowledge of schema markup implementation and mobile search optimization.

## Task
Create a comprehensive, step-by-step guide for implementing schema markup to improve mobile SEO performance. Structure your response using dependency grammar principles, ensuring each step logically builds on the previous one.

## Context
Business context: {{business-context}}
Target keywords: {{target-keywords}}
Current mobile search ranking: {{current-ranking}}

The guide should be actionable for the specified business type and audience, focusing on mobile-first indexing requirements.

## Output
Deliver a numbered implementation guide that includes:

1. **Schema type identification** – Analyze the business type and recommend the 3-5 most relevant schema.org types (e.g., LocalBusiness, Product, Article, FAQPage) with justification for each

2. **Implementation roadmap** – Provide working code examples in JSON-LD format for each recommended schema type, including:
   - Complete markup structure
   - Required and recommended properties
   - Mobile-specific considerations

3. **Validation process** – Detail how to test implementation using:
   - Google Rich Results Test
   - Schema Markup Validator
   - Mobile-Friendly Test
   - Common error patterns and fixes

4. **Integration best practices** – Cover:
   - Placement within HTML structure
   - Dynamic vs. static implementation
   - Page-type priority (homepage, product pages, blog posts)
   - Mobile performance impact

5. **Monitoring framework** – Establish metrics to track:
   - Rich result appearances
   - Click-through rate changes
   - Mobile ranking movement for target keywords
   - Search Console enhancement reports

Use dependency grammar to structure each section: lead with the core action, then branch into supporting details and conditions. Make all code examples copy-paste ready, with placeholder values clearly marked for customization.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{current-ranking}}、{{target-keywords}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile SEO Schema Markup Implementation Guide is a free AI prompt that creates custom schema markup strate…

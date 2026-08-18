# Review Schema Implementation Guide for SEO

## 簡介

The Review Schema Implementation Guide for SEO is a free AI prompt that creates step-by-step structured data markup plans to enhance search visibility for businesses displaying customer reviews. This review schema prompt for ChatGPT analyzes your website URL, business type, product or service, and current schema status to generate valid JSON-LD code with all required properties - reviewRating, author, datePublished, and reviewBody - plus recommended fields like aggregate ratings and nested itemReviewed objects. It delivers HTML integration instructions, property formatting guidelines, and validation steps using Google Rich Results Test and Schema Markup Validator. E-commerce sites, local businesses, service providers, and SaaS companies use it to display rich snippets in search results and increase click-through rates through verified review displays. The prompt runs on ChatGPT, Claude, Gemini, and Grok, adapting its output to match schema.org specifications and Google's current structured data requirements. ● Identifies the correct Review Schema type (Product, LocalBusiness, Organization) based on your specific business model and context ● Generates fully compliant JSON-LD markup with both required and recommended properties following current schema.org standards ● Provides clear HTML integration instructions showing exactly where to place script tags in your page structure ● Includes validation workflows using Google Rich Results Test and guidance on avoiding common implementation errors ## Prompt

```
## Role
You are an SEO specialist implementing Review Schema markup to improve organic search visibility.

## Task
Create a complete Review Schema implementation guide with JSON-LD code tailored to the website context. Include the code structure, required and recommended properties, integration instructions, and validation steps.

## Context
**Website:** {{website-url}}
**Business type:** {{business-type}}
**Product/service being reviewed:** {{product-or-service}}
**Current schema status:** {{current-schema-status}}

## Output
Provide a step-by-step implementation guide structured as:

1. **Schema Selection** – Identify the appropriate Review Schema type (Product, LocalBusiness, Organization, etc.) based on the business type
2. **JSON-LD Code** – Generate complete, valid JSON-LD markup including:
   - Required properties (reviewRating, author, datePublished, reviewBody)
   - Recommended properties (publisher, itemReviewed with full nested object)
   - Aggregate rating markup if applicable
3. **HTML Integration** – Explain where and how to place the `<script type="application/ld+json">` tag in the page structure
4. **Property Guidelines** – Specify data sources for each property and formatting requirements
5. **Validation** – Instructions for testing with Google Rich Results Test and Schema Markup Validator
6. **Best Practices** – Cover review authenticity, markup placement, multiple reviews handling, and common implementation errors to avoid

Format all code snippets in markdown code blocks. Ensure the schema follows current schema.org specifications and Google's structured data guidelines.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-type}}、{{current-schema-status}}、{{product-or-service}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Review Schema Implementation Guide for SEO is a free AI prompt that creates step-by-step structured data m…

# Breadcrumb Schema Implementation Guide Generator

## 簡介

The Breadcrumb Schema Implementation Guide Generator is a free AI prompt that produces detailed technical instructions for adding structured breadcrumb markup to improve search engine visibility and site navigation. This breadcrumb schema prompt for ChatGPT helps you create implementation plans tailored to your CMS, technical skill level, and existing site hierarchy. It maps your current URL structure to Schema.org BreadcrumbList properties, generates code examples specific to WordPress, Shopify, custom builds, or other platforms, and includes validation steps using Google's Rich Results Test and Search Console. SEO specialists, web developers, and site owners use it to ensure breadcrumb trails appear correctly in search results and enhance crawlability. The prompt runs on ChatGPT, Claude, and Gemini. Reach for this prompt when you need to implement or audit Breadcrumb Schema markup and want a clear checklist that accounts for your specific CMS and technical background. ● Maps your existing site hierarchy to BreadcrumbList Schema properties with clear parent-child relationships ● Generates code examples tailored to your CMS (WordPress, Shopify, custom HTML, or other platforms) ● Includes validation workflows using structured data testing tools and Search Console checks ● Identifies common implementation errors (missing position values, incorrect URL paths, orphaned pages) and how to fix them ## Prompt

```
## Role
You are an SEO specialist creating a step-by-step implementation guide for Breadcrumb Schema markup.

## Task
Produce a comprehensive guide that enhances search engine visibility through properly structured Breadcrumb Schema. Cover implementation, validation, and testing. Use dependency grammar principles—attach modifiers directly to their head terms—to keep instructions concise and clear.

## Context
Website: {{website-url}}
Primary keywords: {{primary-keywords}}
Current site structure: {{site-structure}}
CMS: {{cms}}
Technical expertise: {{technical-level}}

## Output
Deliver the guide as a numbered list with clear headings for each major implementation step. Ensure all markup adheres to current search engine guidelines and best practices. Include:

- How to map the existing site hierarchy to Breadcrumb Schema properties
- Code examples tailored to the specified CMS
- Dependency grammar techniques for writing concise schema labels
- Validation methods (structured data testing tools, search console checks)
- Common pitfalls and how to avoid them
- How the markup integrates with the primary keywords and site structure
```

## 用法 / Usage
- 必填變數 / Variables: {{cms}}、{{primary-keywords}}、{{site-structure}}、{{technical-level}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Breadcrumb Schema Implementation Guide Generator is a free AI prompt that produces detailed technical inst…

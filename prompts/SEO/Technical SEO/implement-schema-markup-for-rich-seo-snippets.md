# Schema Markup Implementation Plan for Rich Snippets

## 簡介

The Schema Markup Implementation Plan for Rich Snippets is a free AI prompt that builds a prioritized structured-data strategy complete with valid JSON-LD code for any website. This schema markup prompt for ChatGPT analyzes your site structure, maps the most impactful schema.org types - Organization, Article, Product, LocalBusiness, FAQ, HowTo, BreadcrumbList, and more - to specific pages, and outputs ready-to-paste code blocks tailored to your technical skill level. It runs on ChatGPT, Claude, Gemini, and Grok, producing a markdown table that pairs each schema type with the relevant page and complete markup, followed by deployment priority, testing steps via Google Rich Results Test and Search Console, and maintenance guidance. Agencies, in-house SEO teams, and developers use it to accelerate structured-data rollouts, improve search visibility, and unlock star ratings, carousels, FAQ panels, and other rich result features without trial-and-error. ● Identifies high-value pages and matches them to the most relevant schema.org types for maximum rich-snippet impact ● Generates clean, valid JSON-LD markup ready to paste into the head section of each page ● Provides deployment priority, testing workflows, and maintenance recommendations customized to your technical skill level ● Covers Organization, Article, Product, LocalBusiness, FAQ, HowTo, BreadcrumbList, and other schema types that unlock enhanced search features ## Prompt

```
## Role
You are an SEO specialist building a Schema Markup implementation plan to generate rich snippets and improve search visibility.

## Task
Analyze the website structure and content, then create a complete Schema Markup strategy that identifies the most impactful schema types, maps them to specific pages, and provides ready-to-implement JSON-LD markup code.

## Context
Website and goals:
{{website-and-goals}}

Primary content types:
{{content-types}}

Technical expertise level:
{{technical-level}}

## Process
1. Review the website structure and identify high-value pages for schema implementation
2. Match the most relevant schema.org types to each content type (Organization, Article, Product, LocalBusiness, FAQ, HowTo, BreadcrumbList, etc.)
3. Prioritize schemas that deliver the richest snippets for the stated SEO goals
4. Generate clean, valid JSON-LD markup for each schema type
5. Tailor implementation instructions to the user's technical expertise

## Output
Present your strategy as a markdown table with three columns:

| Schema Type | Relevant Page | Markup Code |
|-------------|---------------|-------------|

- **Schema Type**: The schema.org type name and what it enables
- **Relevant Page**: Which page(s) or content sections to apply it to
- **Markup Code**: Complete JSON-LD snippet ready to paste into the `<head>` section

After the table, provide:
- Implementation priority order (what to deploy first)
- Testing steps (Google Rich Results Test, Search Console)
- Maintenance recommendations
- Any warnings specific to the technical level provided
```

## 用法 / Usage
- 必填變數 / Variables: {{content-types}}、{{technical-level}}、{{website-and-goals}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Schema Markup Implementation Plan for Rich Snippets is a free AI prompt that builds a prioritized structur…

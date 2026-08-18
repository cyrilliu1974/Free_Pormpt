# Canonical Tag Implementation Plan for SEO

## 簡介

The Canonical Tag Implementation Plan for SEO is a free AI prompt that creates a complete technical strategy for identifying duplicate content and deploying canonical tags across any CMS. This canonical tag prompt for ChatGPT walks you through auditing your site for duplicate URLs, defining selection criteria for preferred versions, implementing tags within your specific content management system, and verifying correct placement. It covers blog posts, product pages, category pages, cross-domain scenarios, and crawl budget considerations. You provide your website URL, CMS platform, known duplicate content issues, technical skill level, and available resources; the AI returns a numbered, logically sequenced implementation plan tailored to your team's capabilities. Use it when launching a new site, migrating domains, or resolving indexation problems caused by parameter variations, pagination, or HTTP/HTTPS duplicates. ● Systematically identifies duplicate content across all page types and URL variations ● Provides clear criteria for choosing the canonical version of each URL cluster ● Details CMS-specific implementation steps, from self-referencing tags to cross-domain rel=canonical ● Includes verification methods, testing protocols, and ongoing monitoring recommendations ## Prompt

```
## Role
You are an expert SEO specialist creating a canonical tag implementation plan for website optimization.

## Task
Develop a comprehensive, actionable strategy to implement canonical tags that prevents duplicate content issues and enhances SEO performance. Structure your plan with clear logical progression, covering:

- Identification of duplicate content across the site
- Selection criteria for preferred (canonical) URLs
- Technical implementation of canonical tags within the CMS
- Verification and testing of proper tag placement
- Considerations for different content types (blog posts, product pages, category pages, etc.)
- Cross-domain canonicalization where applicable
- Impact on crawl budget and indexation

## Context
Website: {{website-url}}
CMS: {{cms}}
Primary duplicate content issues: {{duplicate-content-issues}}
Technical expertise: {{technical-level}}
Available resources: {{resources}}

## Output
Present your implementation plan as a structured, numbered list with clear headings for each main section. Make the strategy actionable and appropriate for the stated technical expertise level.
```

## 用法 / Usage
- 必填變數 / Variables: {{cms}}、{{duplicate-content-issues}}、{{resources}}、{{technical-level}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Canonical Tag Implementation Plan for SEO is a free AI prompt that creates a complete technical strategy f…

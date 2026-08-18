# XML Sitemap Audit and Error Fix Prompt

## 簡介

The XML Sitemap Audit and Error Fix Prompt is a free AI prompt from God of Permit that conducts technical SEO audits focused on identifying and resolving XML sitemap errors for websites. When you provide your website URL, sitemap location, CMS platform, and recent site changes, this XML sitemap prompt for ChatGPT analyzes your sitemap structure for common errors that prevent optimal search engine crawling - including invalid syntax, blocked URLs, redirect chains, incorrect priority values, oversized sitemaps, and missing declarations. It runs on ChatGPT, Claude, and Gemini to deliver a prioritized action plan with CMS-specific implementation steps tailored to platforms like WordPress, Shopify, or custom builds. SEO specialists and website owners reach for this prompt when troubleshooting indexing problems, after major site migrations, or when maintaining technical SEO hygiene across large content inventories. ● Analyzes sitemap structure, format validation, size limits, and robots.txt declarations to identify crawl barriers ● Identifies specific errors including 404s, redirects, non-canonical URLs, missing timestamps, and incorrect sitemap index architecture ● Delivers CMS-specific implementation instructions for your platform, explaining what to change and why it matters for search engine crawlers ● Provides a validation checklist and ongoing maintenance practices to prevent future sitemap errors and maintain optimal indexing ## Prompt

```
## Role
You are an expert SEO specialist conducting a comprehensive technical SEO audit focused on XML sitemap optimization.

## Task
Analyze the XML sitemap for {{website-url}}, identify errors and issues that prevent optimal search engine crawling, and deliver a step-by-step action plan to fix them. The sitemap is located at {{sitemap-url}} and the site runs on {{cms}}.

## Context
Recent website changes: {{recent-changes}}

Target search engine: Google (primary focus, with cross-engine compatibility).

Common XML sitemap errors to investigate include:
- Invalid XML syntax or formatting
- URLs blocked by robots.txt
- Non-canonical URLs in sitemap
- 404 or redirected URLs
- URLs with incorrect priority or changefreq values
- Missing lastmod timestamps
- Sitemap size exceeding 50MB or 50,000 URL limits
- Images, videos, or alternate language pages not properly declared
- Incorrect sitemap index structure
- Sitemap not declared in robots.txt or submitted to Search Console

## Output
Deliver your audit and action plan as a numbered list with clear section headings:

1. **Current Sitemap Analysis** - assessment of structure, size, and format
2. **Identified Errors** - specific issues found, with severity ratings
3. **Prioritized Fix Recommendations** - actionable solutions for each error
4. **CMS-Specific Implementation Steps** - how to execute fixes in {{cms}}
5. **Validation & Submission Checklist** - steps to verify corrections and resubmit
6. **Ongoing Maintenance Best Practices** - how to prevent future sitemap issues

For each fix, explain what to change, why it matters for search engine crawlers, and the expected SEO impact.
```

## 用法 / Usage
- 必填變數 / Variables: {{cms}}、{{recent-changes}}、{{sitemap-url}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The XML Sitemap Audit and Error Fix Prompt is a free AI prompt from God of Permit that conducts technical SEO …

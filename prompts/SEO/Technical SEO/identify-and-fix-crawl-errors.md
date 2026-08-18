# Crawl Error Audit and Fix Prompt for SEO

## 簡介

The Crawl Error Audit and Fix Prompt for SEO is a free AI prompt that systematically diagnoses technical crawl issues blocking search engines from indexing your site and delivers prioritized solutions tailored to your platform and expertise level. This crawl error prompt for ChatGPT analyzes your website for common and technical-specific errors - 404s, server errors, redirect chains, robots.txt blocks, noindex tags, canonical conflicts, and sitemap problems - then outputs a structured markdown table mapping each error type to its description and immediate fix. It adapts recommendations to your CMS platform (WordPress, Shopify, custom builds) and technical skill level, ensuring solutions are practical whether you're a developer or a site owner. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across all major text AI models. Reach for this prompt when site traffic drops unexpectedly, Google Search Console flags indexing issues, or you need a comprehensive technical SEO health check before a migration or redesign. ● Detects both common crawl errors (404s, 5xx server errors, redirect loops, timeout issues) and advanced technical problems (robots.txt misconfigurations, incorrect noindex usage, canonical tag errors, sitemap validation failures) ● Prioritizes fixes by SEO impact and user experience consequences, so you address the most damaging issues first ● Tailors solution complexity to your technical level, from point-and-click CMS fixes to developer-level server configuration changes ● Aligns all recommendations with current search engine guidelines from Google, Bing, and other major platforms ## Prompt

```
## Role
You are an expert SEO specialist conducting a technical crawl error audit.

## Task
Identify crawl errors affecting {{website-url}} and provide actionable solutions to resolve them. Prioritize errors by their impact on search engine performance and user experience.

## Context
- Primary search engine: {{search-engine}}
- Website platform: {{platform-cms}}
- User technical expertise: {{technical-level}}

Analyze the website's crawl status systematically:
1. Identify common errors (404s, server errors, redirect chains, timeout issues)
2. Detect specific technical issues (robots.txt blocks, noindex tags, canonical problems, sitemap errors)
3. Assess impact on crawlability and indexation
4. Align all recommendations with current SEO best practices and search engine guidelines

## Output
Present findings as a markdown table with three columns:

| Error Type | Description | Solution |
|------------|-------------|----------|

Each row must provide clear, concise, and immediately actionable information tailored to the specified technical expertise level.
```

## 用法 / Usage
- 必填變數 / Variables: {{platform-cms}}、{{search-engine}}、{{technical-level}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Crawl Error Audit and Fix Prompt for SEO is a free AI prompt that systematically diagnoses technical crawl…

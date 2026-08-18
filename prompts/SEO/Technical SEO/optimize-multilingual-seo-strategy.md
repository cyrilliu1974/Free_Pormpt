# Multilingual SEO Hreflang Implementation Guide

## 簡介

The Multilingual SEO Hreflang Implementation Guide is a free AI prompt that creates actionable technical documentation for international website optimization and proper language targeting. This hreflang implementation prompt for ChatGPT walks you through seven concrete steps: identifying target languages based on market research, creating culturally localized content, implementing hreflang tags using HTML, HTTP headers, or XML sitemaps, structuring language-specific URLs (subdirectories, subdomains, or ccTLDs), building user-friendly language switchers, updating XML sitemaps, and setting up monitoring through Google Search Console. It includes code examples for each hreflang method, warns against common pitfalls like missing return links or incorrect ISO language codes, and adapts recommendations to your existing URL structure. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing clear guides that balance technical accuracy with readability for developers, marketing teams, and SEO specialists. Reach for this prompt when launching a website in new markets, fixing indexation issues caused by duplicate multilingual content, or auditing an existing international site for technical SEO problems. ● Produces language selection criteria based on analytics, market size, and business priorities rather than guesswork ● Delivers three hreflang implementation methods (HTML head, HTTP header, XML sitemap) with working code examples ● Identifies seven common pitfalls including incorrect bidirectional linking, missing region codes, and auto-redirect traps ● Adapts URL structure recommendations (subdirectory vs. subdomain vs. ccTLD) to your current site architecture and SEO goals ## Prompt

```
## Role
You are an expert SEO consultant specializing in multilingual website optimization.

## Task
Create a comprehensive, step-by-step guide for implementing hreflang tags and targeting the right languages for a multilingual website. The guide should be actionable, formatted for quick reference, and avoid overly technical jargon.

## Context
The user needs to optimize their website for multiple languages with proper technical SEO implementation.

{{website-details}}

## Output
Deliver a guide with the following structure:

**Multilingual Website Optimization Guide**

**Objective:** State the main goal of creating multilingual versions of the website.

**Step 1: Identify Target Languages**
- Instructions for researching and selecting target languages
- Best practices (market research, user analytics, business priorities)
- List the selected languages from the user's context

**Step 2: Create Language-Specific Content**
- Instructions for professional translation vs. machine translation
- Best practices (cultural localization, native review, maintaining brand voice)

**Step 3: Implement Hreflang Tags**
- Instructions for adding hreflang annotations
- Code examples showing HTML head implementation, HTTP header method, and XML sitemap method
- Best practices (bidirectional linking, x-default for language selector pages, ISO language codes)

**Step 4: Create Language-Specific URLs**
- Instructions for choosing URL structure (subdirectories, subdomains, or ccTLDs)
- Examples based on the user's current URL structure
- Best practices (consistency, SEO implications of each approach)

**Step 5: Set Up Language Switcher**
- Instructions for implementing user-friendly language selection
- Best practices (visible placement, automatic detection considerations, manual override)

**Step 6: Update XML Sitemap**
- Instructions for including all language versions
- Best practices (separate sitemaps per language vs. unified, proper hreflang in sitemap)

**Step 7: Monitor and Test**
- Instructions for validation and ongoing monitoring
- Best practices (Google Search Console International Targeting report, hreflang testing tools, indexation tracking)

**Common Pitfalls to Avoid:**
1. Incorrect or missing return links in hreflang implementation
2. Using language codes without region codes when needed (es vs. es-ES vs. es-MX)
3. Mixing URL structure approaches inconsistently
4. Auto-redirecting users based on IP/browser without manual override option
5. Duplicate content without proper hreflang signals
6. Forgetting to update hreflang when adding/removing language versions

Conclude with a brief summary emphasizing that proper multilingual SEO is an ongoing process requiring regular audits and updates as the site evolves.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Multilingual SEO Hreflang Implementation Guide is a free AI prompt that creates actionable technical docum…

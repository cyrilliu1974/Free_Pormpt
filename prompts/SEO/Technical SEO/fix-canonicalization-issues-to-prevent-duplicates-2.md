# Canonicalization Audit Prompt for SEO

## 簡介

The Canonicalization Audit Prompt for SEO is a free AI prompt that conducts technical SEO audits to identify and resolve duplicate content issues for website owners and SEO professionals. This canonicalization prompt for ChatGPT analyzes seven critical areas where duplicate content arises: URL structure variations (trailing slashes, www vs non-www, HTTP vs HTTPS, case sensitivity), canonical tag accuracy, 301 redirect coverage, URL parameter handling for sorting and pagination, internal linking consistency, hreflang tags for multilingual sites, and XML sitemap alignment with canonical URLs. It runs on ChatGPT, Claude, and Gemini, producing a structured markdown table that pairs each identified issue with actionable implementation steps, prioritized by SEO impact. Use it when auditing a website's technical foundation, diagnosing ranking dilution from duplicates, or preparing migration checklists. ● Detects URL structure inconsistencies that split ranking signals across duplicate pages ● Validates canonical tag implementation and identifies missing or conflicting directives ● Audits 301 redirect chains and coverage gaps that allow duplicate indexing ● Reviews URL parameter handling for filters, sorts, and session IDs that spawn duplicate content ● Checks hreflang tag configuration for multi-regional sites to prevent cross-language duplication ● Ensures XML sitemap entries match canonical URLs to maintain clear indexing hierarchy ## Prompt

```
## Role
You are an expert SEO analyst conducting a technical SEO audit focused on canonicalization and duplicate content.

## Task
Identify canonicalization issues on the website and provide actionable solutions. Analyze:

1. URL structure variations that create duplicate content (trailing slashes, www vs non-www, HTTP vs HTTPS, case sensitivity)
2. Canonical tag implementation and accuracy
3. 301 redirect configuration and coverage
4. URL parameter handling (sorting, filtering, tracking, pagination)
5. Internal linking consistency and canonical preference signals
6. Hreflang tag setup for multilingual/multi-regional content (if applicable)
7. XML sitemap entries and their alignment with canonical URLs

## Context
Website: {{website-url}}
CMS: {{cms}}
Primary language: {{primary-language}}
Target audience: {{target-audience}}

## Output
Provide findings in a markdown table with two columns:

| Issue | Solution |
|-------|----------|
| [Describe the specific canonicalization problem identified] | [Provide clear implementation steps to resolve it] |

Include only issues found during analysis. For each issue, specify affected URLs or patterns and prioritize solutions by impact.
```

## 用法 / Usage
- 必填變數 / Variables: {{cms}}、{{primary-language}}、{{target-audience}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Canonicalization Audit Prompt for SEO is a free AI prompt that conducts technical SEO audits to identify a…

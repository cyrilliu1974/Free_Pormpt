# Broken Link Audit Prompt for Technical SEO

## 簡介

The Broken Link Audit Prompt for Technical SEO is a free AI prompt that identifies broken links across a website and delivers specific repair recommendations for SEO specialists and site managers. This technical SEO prompt for ChatGPT works by scanning a target website URL for broken links, analyzing their HTTP status codes, documenting where each broken link appears, and proposing tailored solutions such as 301 redirects, content restoration, link updates, or removal. It outputs a prioritized markdown table sorted by SEO impact, making it easy for development and content teams to implement fixes immediately. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and is ideal for routine technical audits, site migrations, content refreshes, or diagnosing sudden ranking drops caused by link integrity issues. ● Scans a website for broken links and captures HTTP status codes, source pages, and link URLs in a single audit ● Prioritizes fixes by SEO impact, distinguishing high-authority internal links from low-value external references ● Delivers specific, actionable solutions for each broken link, such as redirects, content restoration, or safe removal ● Outputs findings in a markdown table format that developers and content editors can use immediately ## Prompt

```
## Role
You are an expert SEO specialist conducting a comprehensive technical SEO audit focused on broken links that impact search engine rankings.

## Task
Identify and document broken links across {{website-url}}, then provide actionable solutions for each.

## Process
1. Scan the website for broken links using standard SEO crawling methodology
2. Analyze each broken link to determine its HTTP status code and the page where it appears
3. Develop specific, actionable solutions for each broken link (redirect, update, remove, restore content, etc.)
4. Prioritize fixes based on SEO impact (internal vs. external, page authority, traffic potential)

## Output
Present findings as a markdown table with these columns:

| Link URL | Status Code | Source Page | Proposed Solution |
|----------|-------------|-------------|-------------------|

Include {{max-links}} broken links in order of priority. Ensure the table is properly formatted with clear, concise solutions that can be immediately implemented by a development or content team.
```

## 用法 / Usage
- 必填變數 / Variables: {{max-links}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Broken Link Audit Prompt for Technical SEO is a free AI prompt that identifies broken links across a websi…

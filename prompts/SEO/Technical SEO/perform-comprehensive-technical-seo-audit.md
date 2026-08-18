# Technical SEO Audit Prompt for Website Analysis

## 簡介

The Technical SEO Audit Prompt for Website Analysis is a free AI prompt that systematically evaluates your website's technical search engine optimization health and delivers prioritized, actionable recommendations for SEO analysts, webmasters, and digital marketers. This technical SEO audit prompt for ChatGPT examines eight critical dimensions: site structure and crawlability, on-page content optimization, mobile responsiveness and Core Web Vitals, page speed and performance, indexability and robots directives, backlink profile health, schema markup and structured data, and security and HTTPS implementation. The prompt produces a markdown table ranking issues by severity (Critical, High, Medium, Low) with specific remediation steps, plus an executive summary spotlighting the top three priorities. It runs on ChatGPT, Claude, Gemini, and Grok, making it compatible with all major text-generation models. Use it when launching a new site, diagnosing ranking drops, preparing for algorithm updates, or establishing an SEO baseline. ● Analyzes site structure, crawlability, mobile responsiveness, Core Web Vitals, page speed, indexability, backlink health, schema markup, and HTTPS security in a single audit workflow. ● Outputs a severity-ranked table with each issue clearly described alongside actionable recommendations, so you know exactly what to fix first. ● Includes an executive summary that distills findings into the top three priorities and their estimated impact on search performance. ● Accepts website URL and business context (target audience, business type, competitors, KPIs) to tailor the audit to your specific goals and competitive landscape. ## Prompt

```
## Role
You are an expert SEO analyst conducting a comprehensive technical SEO audit.

## Task
Identify and prioritize technical issues hindering search engine performance for the website. Analyze the site systematically across all critical technical SEO dimensions:

- Site structure and crawlability
- On-page content optimization
- Mobile responsiveness and Core Web Vitals
- Page speed and performance
- Indexability and robots directives
- Backlink profile health
- Schema markup and structured data
- Security and HTTPS implementation

## Context
**Website:** {{website-url}}

**Business context:** {{business-context}}
(Include target audience, business type, primary competitors, and key performance indicators you're tracking)

## Output
Present your findings as a markdown table with three columns:

| Issue | Severity | Recommendations |
|-------|----------|----------------|

List issues in priority order, with the most critical at the top. For each issue:

- **Issue:** Clearly describe the technical problem found
- **Severity:** Rate as Critical, High, Medium, or Low based on impact on search performance
- **Recommendations:** Provide specific, actionable steps to resolve the issue

After the table, include a brief executive summary highlighting the top 3 priorities and estimated impact of addressing them.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical SEO Audit Prompt for Website Analysis is a free AI prompt that systematically evaluates your web…

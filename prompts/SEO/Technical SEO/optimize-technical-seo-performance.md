# Technical SEO Audit and Competitor Benchmark

## 簡介

The Technical SEO Audit and Competitor Benchmark is a free AI prompt that builds a data-driven framework to assess your website's technical health against competitor sites and prioritize fixes. This technical SEO prompt for ChatGPT walks you through systematic data collection using Google PageSpeed Insights, Mobile-Friendly Test, Screaming Frog SEO Spider, and tools like Ahrefs or SEMrush. It produces a comparative analysis table scoring your site and 2-3 competitors across seven core metrics (page load speed, mobile friendliness, crawl errors, XML sitemaps, HTTPS, structured data, canonical tags), then delivers a ranked action plan with implementation steps, timeframes, and success metrics for each fix. Use it when launching a redesign, preparing for a site migration, diagnosing search visibility drops, or building a quarterly SEO roadmap. It runs on ChatGPT, Claude, and Gemini. ● Compares your site against competitors on page speed, mobile score, crawl errors, HTTPS, structured data, XML sitemaps, and canonicals ● Outputs a side-by-side table and a ranked action plan with specific technical steps, tools, and expected impact for each recommendation ● Includes monitoring cadence (weekly Search Console tracking, monthly metric retests) to measure progress over time ● Covers both automated tool collection (PageSpeed Insights, Screaming Frog) and manual audits (robots.txt, canonicalization, structured data validation) ## Prompt

```
## Role

You are an expert technical SEO consultant specializing in website optimization and competitive benchmarking.

## Task

Develop a comprehensive technical SEO assessment framework comparing {{website-url}} against {{competitor-urls}} (provide 2-3 competitor URLs). Identify performance gaps, strengths, and prioritized improvement opportunities.

## Methodology

**Data Collection:**
- Use Google PageSpeed Insights, Mobile-Friendly Test, and Search Console for core web vitals and mobile usability
- Crawl all sites with Screaming Frog SEO Spider to identify technical issues
- Review Ahrefs or SEMrush for backlink profile health
- Manually audit robots.txt, XML sitemaps, HTTPS configuration, canonicalization, and structured data

**Key Metrics to Evaluate:**
- Page load speed (target: <3 seconds)
- Mobile friendliness score (target: 100/100)
- Crawl errors (target: 0)
- XML sitemap presence and quality
- HTTPS security (valid SSL)
- Structured data implementation (0 errors)
- Canonical tag coverage (100%)

## Output

### Comparative Analysis Table

| Metric | {{website-url}} | Competitor 1 | Competitor 2 | Competitor 3 |
|--------|-----------------|--------------|--------------|-------------|
| Page Speed | | | | |
| Mobile Score | | | | |
| Crawl Errors | | | | |
| XML Sitemap | | | | |
| HTTPS | | | | |
| Structured Data | | | | |
| Canonicals | | | | |

### Prioritized Action Plan

Rank technical SEO improvements by impact and effort:

1. **[Highest priority issue]** - Expected impact, implementation steps
2. **[Second priority issue]** - Expected impact, implementation steps
3. **[Third priority issue]** - Expected impact, implementation steps

For each recommendation, provide:
- Specific technical steps to implement
- Tools needed
- Expected timeframe
- Success metrics

**Monitoring:**
Track progress weekly in Google Search Console and retest all metrics monthly to measure improvement against competitors.
```

## 用法 / Usage
- 必填變數 / Variables: {{competitor-urls}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical SEO Audit and Competitor Benchmark is a free AI prompt that builds a data-driven framework to as…

# Website SEO Audit Prompt for Local Search Performance

## 簡介

The Website SEO Audit Prompt for Local Search Performance is a free AI prompt that performs technical SEO audits focused on broken links, crawlability, and local search optimization for business websites. This website SEO audit prompt for ChatGPT, Claude, and Gemini analyzes a URL to identify broken links, technical issues, and missing local SEO elements. It produces a structured report containing a broken-links table with HTTP status codes and suggested fixes, prioritized technical recommendations (page speed, mobile usability, metadata gaps), and a local SEO checklist covering Google Business Profile setup, NAP consistency, schema markup, and citation strategy. Typical use cases include pre-launch site reviews, monthly performance monitoring, and diagnosing sudden ranking drops in local search results. This prompt is built for marketing teams, SEO consultants, and small business owners who need a repeatable audit framework that connects technical fixes to local visibility gains. ● Produces a broken-links table with page URLs, HTTP status codes, and specific fix actions (redirect, update, remove). ● Evaluates local SEO essentials: Google Business Profile completion, NAP consistency, local schema markup, and review strategy. ● Delivers 3–4 prioritized technical recommendations beyond links, such as mobile usability, crawl errors, and metadata gaps. ● Includes a four-step implementation roadmap from high-impact fixes to recurring audit scheduling. ## Prompt

```
## Role

You are an SEO consultant specializing in technical website audits and local search optimization.

## Task

Perform a comprehensive SEO audit of the provided website, identifying broken links and technical issues that negatively impact local search rankings. Deliver a structured report with actionable fixes prioritized for local search performance.

## Context

**Website URL:** {{website-url}}  
**Website niche:** {{niche}}  
**Target location:** {{target-location}}

## Output

Structure your audit report as follows:

### Website Overview
Summarize the site's purpose, niche positioning, and local market context.

### Broken Links Report
Present findings in a table:

| Page URL | Broken Link | Status Code | Suggested Fix |
|----------|-------------|-------------|---------------|
| [First identified page] | [URL returning error] | [HTTP code] | [Specific action: redirect, update, remove] |
| [Second identified page] | [URL returning error] | [HTTP code] | [Specific action] |
| [Third identified page] | [URL returning error] | [HTTP code] | [Specific action] |

Include 3–5 critical broken links with the highest impact on user experience and crawlability.

### Additional SEO Recommendations
Provide 3–4 prioritized technical improvements beyond broken links (e.g., page speed, mobile usability, crawl errors, metadata gaps).

### Local SEO Checklist
Evaluate and mark completion status:

- [ ] Google Business Profile optimized (categories, hours, photos, posts)
- [ ] NAP consistency across site and citations
- [ ] Customer review strategy active
- [ ] Local schema markup implemented (LocalBusiness, address, hours)
- [ ] Location-specific content published
- [ ] Local citations and backlinks established

### Next Steps
Outline a 4-step implementation roadmap:
1. Fix broken links by impact priority
2. Deploy technical SEO improvements
3. Complete local SEO checklist items
4. Schedule recurring audits (monthly or quarterly)
```

## 用法 / Usage
- 必填變數 / Variables: {{niche}}、{{target-location}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Website SEO Audit Prompt for Local Search Performance is a free AI prompt that performs technical SEO audi…

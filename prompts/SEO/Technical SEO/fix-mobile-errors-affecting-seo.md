# Mobile SEO Error Audit and Fix Prompt

## 簡介

The Mobile SEO Error Audit and Fix Prompt is a free AI prompt that identifies and resolves mobile optimization errors affecting search rankings and user experience for SEO analysts and webmasters. This mobile SEO audit prompt for ChatGPT walks through a three-phase process: auditing technical infrastructure, content rendering, and mobile UX patterns; prioritizing issues by their impact on crawlability, indexing, and Core Web Vitals; then delivering step-by-step technical fixes with validation methods. You provide your website URL, top competitors, audience demographics, current mobile traffic percentage, and page speed score, and the prompt returns an executive summary with a mobile SEO health score, ranked priority issues with remediation instructions, quick wins for immediate impact, and long-term strategic recommendations. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when mobile traffic is underperforming, after a Google algorithm update, or before a site migration to catch indexing or rendering problems that hurt mobile rankings. ● Identifies critical mobile errors across technical infrastructure, content rendering, and Core Web Vitals that impact rankings ● Ranks issues by SEO impact and user friction, focusing remediation effort where it matters most ● Provides step-by-step technical fixes with validation methods so you can verify improvements ● Includes quick wins for immediate impact and long-term recommendations for sustained mobile performance ## Prompt

```
## Role

You are an expert SEO analyst specializing in mobile optimization and technical site audits.

## Task

Conduct a comprehensive mobile SEO audit for the provided website, identify critical errors affecting search rankings and user experience, then deliver prioritized, actionable recommendations aligned with current mobile SEO best practices.

## Context

**Website and Competitive Landscape:**
{{website-and-competition}}
(Include: website URL, top 3 competitors, primary target audience demographics/needs, current mobile traffic percentage, current mobile page speed score)

## Process

1. **Audit Phase**: Analyze mobile-specific issues across technical infrastructure, content rendering, and UX patterns
2. **Prioritization**: Rank issues by SEO impact (crawlability, indexing, Core Web Vitals) and user friction
3. **Remediation**: Provide specific technical fixes, content optimizations, and UX enhancements for each issue

## Output

Deliver your analysis in the following structure:

### Executive Summary
- Overall mobile SEO health score
- Top 3 critical issues requiring immediate attention

### Priority Issues (ranked by impact)

For each issue:
- **Issue**: Clear description and where it occurs
- **Impact**: Effect on rankings, traffic, and user experience
- **Fix**: Step-by-step technical remediation
- **Validation**: How to verify the fix worked

### Quick Wins
- Low-effort, high-impact optimizations

### Long-term Recommendations
- Strategic improvements for sustained mobile performance

Use clear headings, subheadings, and bullet points throughout. Include relevant metrics and benchmarks where applicable.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-and-competition}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile SEO Error Audit and Fix Prompt is a free AI prompt that identifies and resolves mobile optimization…

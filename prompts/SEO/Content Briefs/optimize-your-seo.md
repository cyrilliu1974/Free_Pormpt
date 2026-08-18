# SEO Article Audit and Optimization Checklist

## 簡介

The SEO Article Audit and Optimization Checklist is a free AI prompt that evaluates blog articles against 20-30 high-impact SEO factors and generates a detailed audit with specific recommendations for improving search engine rankings. This SEO audit prompt for ChatGPT analyzes your article's source code and produces a structured report with a 1-10 SEO score, a checklist of passing criteria (what's done right), and failing criteria with concrete fixes. It evaluates technical factors like meta tags, heading structure, keyword density, load times, and schema markup - focusing only on practices that meaningfully affect Google rankings for the specific article being reviewed. The output uses markdown formatting with checkmarks and X-marks for easy scanning. Content creators, digital marketers, and SEO professionals use it to audit blog posts before publication or to diagnose ranking issues on existing content. It runs reliably on ChatGPT, Claude, and Gemini. ● Scores articles 1-10 and justifies the rating with evidence from the audit ● Evaluates 20-30 concrete SEO factors with measurable details like character counts and keyword density ● Separates passing criteria from failures, each with specific fix recommendations ● Filters out low-impact SEO practices to focus only on changes that move rankings ## Prompt

```
## Role

You are an SEO specialist who audits blog articles and provides actionable recommendations to improve search engine rankings.

## Task

Analyze the provided blog article source code and deliver a comprehensive SEO audit in checklist format.

## Input

{{article-source-code}}

## Analysis Criteria

- Evaluate 20-30 specific, high-impact SEO factors widely recognized by the SEO community
- Focus on practices that meaningfully affect Google rankings
- Be concrete and concible; include numbers where applicable (character counts, keyword density, load times)
- Exclude practices with negligible ranking impact for this specific article

## Output

Structure your audit as follows:

### SEO Score
[Score from 1-10 with brief justification]

### What's Done Right
✅ [Criterion with specific detail]
✅ [Criterion with specific detail]
✅ [Criterion with specific detail]
[Continue for all passing criteria]

### What's Done Wrong
❌ [Criterion with specific fix recommendation]
❌ [Criterion with specific fix recommendation]
❌ [Criterion with specific fix recommendation]
[Continue for all failing criteria]

Use markdown formatting throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{article-source-code}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SEO Article Audit and Optimization Checklist is a free AI prompt that evaluates blog articles against 20-3…

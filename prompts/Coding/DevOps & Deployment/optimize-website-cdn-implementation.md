# CDN Implementation Guide for Website Performance

## 簡介

The CDN Implementation Guide for Website Performance is a free AI prompt that produces a tailored Content Delivery Network deployment plan with technical configuration steps, provider comparisons, and realistic performance forecasts for website owners and network engineers. This CDN implementation prompt for ChatGPT analyzes your existing website performance metrics - page load times, bounce rates, and geographic slow zones - then recommends three suitable CDN providers (CloudFlare, Fastly, AWS CloudFront, Akamai, or alternatives) with feature comparisons. It delivers 5-7 actionable implementation steps covering DNS configuration, origin server setup, cache rules, TTL settings, SSL/TLS certificates, and validation procedures, plus a post-implementation checklist and quantified predictions for load-time and bounce-rate improvements. The prompt runs on ChatGPT, Claude, and Gemini, outputting structured technical guidance grounded in current CDN best practices. Reach for this prompt when you need to reduce global loading times, configure your first CDN, or justify a CDN migration with data-backed projections. ● Receives specific website URL and current performance baseline (load time, bounce rate, slow regions) to tailor every recommendation ● Compares three CDN providers matched to the site's technical requirements and traffic patterns ● Outputs 5-7 step-by-step configuration instructions for DNS, caching, SSL, origin servers, and testing ● Includes a post-launch verification checklist covering cache hit rates, SSL functionality, geographic distribution, and monitoring setup ● Provides percentage-based predictions for load-time reduction and bounce-rate improvement anchored to the input metrics ## Prompt

```
## Role
You are an expert network engineer specializing in CDN implementations for websites of all sizes.

## Task
Provide a comprehensive CDN implementation guide tailored to the specified website, including current performance analysis, provider recommendations, implementation steps, and realistic performance improvement projections.

## Context
Website to optimize: {{website-url}}

Current performance baseline: {{performance-metrics}}
(Include average page load time, bounce rate, and geographical regions with slowest load times)

## Output
Deliver your analysis and recommendations in this structure:

**Website URL:** [state the URL]

**Current Performance Metrics:**
- Average page load time
- Bounce rate percentage
- Geographical regions with slowest load times

**CDN Provider Recommendations:**
Provide 3 suitable CDN providers with their key features relevant to this website's needs (consider CloudFlare, Fastly, AWS CloudFront, Akamai, or others based on site requirements).

**Implementation Steps:**
Provide 5-7 detailed, actionable steps covering:
- DNS configuration
- Origin server setup
- Cache rules and TTL settings
- SSL/TLS certificate configuration
- Testing and validation procedures

**Post-Implementation Checklist:**
Include 5+ verification items covering cache hit rates, SSL functionality, geographic distribution testing, and monitoring setup.

**Expected Performance Improvements:**
- Predicted average page load time reduction (percentage)
- Predicted bounce rate reduction (percentage)
- Regions expected to see most significant improvements

Base all recommendations on current best practices for CDN deployment and provide realistic projections grounded in the stated performance metrics.
```

## 用法 / Usage
- 必填變數 / Variables: {{performance-metrics}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The CDN Implementation Guide for Website Performance is a free AI prompt that produces a tailored Content Deli…

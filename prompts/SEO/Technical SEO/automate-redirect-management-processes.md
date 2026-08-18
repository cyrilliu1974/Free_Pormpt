# SEO Redirect Management System Builder

## 簡介

The SEO Redirect Management System Builder is a free AI prompt that creates comprehensive redirect management frameworks for SEO specialists working on technical optimization and programmatic SEO. This redirect management prompt for ChatGPT helps you build a complete system with structured redirect tables (covering redirect type, source URL, target URL, and status), implementation guidelines for 301 vs 302 redirects, monitoring procedures to track performance and indexation, and monthly maintenance workflows. It runs on ChatGPT, Claude, and Gemini, taking your website URL and SEO context as inputs to deliver customized redirect strategies that preserve search rankings, manage crawl budget, and transfer link equity. The prompt addresses common technical SEO challenges like redirect chains, broken targets, server configuration, and the impact on page load times and user navigation flows. Reach for this prompt when launching site migrations, restructuring URL architecture, consolidating duplicate content, or managing redirects for large-scale programmatic SEO campaigns where manual tracking becomes impractical. ● Generates markdown redirect tables with clear columns for type, source URL, target URL, status, and tracking fields ● Provides step-by-step server setup, testing, and deployment instructions tailored to your website ● Delivers monitoring checklists covering crawl budget, indexation changes, server response codes, and redirect performance metrics ● Includes monthly maintenance protocols with audit criteria, update triggers, and procedures for retiring outdated redirects ## Prompt

```
## Role
You are an SEO specialist building a redirect management system to improve search rankings and support programmatic SEO at scale.

## Task
Create a comprehensive redirect management process that includes:

- A structured redirect table with columns for Redirect Type, Source URL, Target URL, Status, and any additional tracking fields
- Implementation guidelines covering when to use 301 vs 302 redirects, redirect chains to avoid, and server configuration
- Monitoring procedures to track redirect performance, indexation changes, and crawl errors
- Maintenance workflow for auditing outdated redirects, updating broken targets, and retiring unnecessary redirects

## Context
Website: {{website-url}}
SEO objectives and current performance: {{seo-context}}

Consider impact on:
- Search engine crawl budget and ranking preservation
- Page load times and server response codes
- User experience and navigation flows
- Link equity transfer and indexation

## Output
Deliver:

1. A markdown table template with the redirect structure
2. Step-by-step implementation instructions (server setup, testing, deployment)
3. Monitoring checklist with key metrics and tools
4. Monthly maintenance protocol with audit criteria and update triggers

Format all tables in clean markdown with clear column headers.
```

## 用法 / Usage
- 必填變數 / Variables: {{seo-context}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The SEO Redirect Management System Builder is a free AI prompt that creates comprehensive redirect management …

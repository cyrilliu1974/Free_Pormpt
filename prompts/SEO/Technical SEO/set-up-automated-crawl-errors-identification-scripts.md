# Automated Crawl Error Detection Script Setup

## 簡介

The Automated Crawl Error Detection Script Setup is a free AI prompt that builds complete configuration instructions for monitoring website crawl errors automatically. This crawl error monitoring prompt for ChatGPT walks you through the entire automation process: initial tool configuration, script setup, scheduling parameters, alert thresholds, and structured error reporting at your chosen frequency. It adapts the technical complexity to match your expertise level (beginner, intermediate, or advanced) and works with any SEO tool you specify - whether Screaming Frog, Sitebulb, Google Search Console API, or custom solutions. The output includes both setup documentation and a markdown table template that categorizes errors by type, URL, and priority, helping you triage 404s, server errors, redirect chains, and timeout issues efficiently. SEO analysts and webmasters use it to eliminate manual crawl audits and catch technical issues before they damage search visibility. ● Configures automated detection for all major crawl error types including 404 errors, 5xx server errors, redirect loops, and timeout failures ● Adapts setup complexity and technical terminology based on user expertise level, from beginner-friendly walkthroughs to advanced API integration ● Generates markdown error report templates with priority classification logic for efficient triage and remediation workflows ● Includes scheduling configuration, alert threshold recommendations, and credential management for continuous monitoring ## Prompt

```
## Role
You are an expert SEO analyst specializing in automated crawl error detection and monitoring systems.

## Task
Create a comprehensive system to identify and monitor crawl errors for {{website-url}} using {{seo-tool}}. Provide step-by-step setup instructions for automated error tracking, covering all necessary configurations, parameters, and scheduling. Then explain how to structure and generate actionable error reports at {{reporting-frequency}} intervals.

## Context
The user's technical expertise level is {{technical-expertise-level}}. Tailor the complexity of your setup instructions accordingly—use appropriate terminology and provide more or less explanation based on their proficiency (beginner/intermediate/advanced).

## Output
Structure your response in two parts:

1. **Setup Instructions**: Step-by-step process for configuring automated crawl error tracking, including:
   - Initial tool configuration
   - Script/automation setup
   - Required parameters and credentials
   - Scheduling and frequency settings
   - Alert thresholds

2. **Error Report Template**: Present the monitoring output as a markdown table with three columns:

| Error Type | URL | Priority |
|------------|-----|----------|
| [Type of crawl error] | [Affected URL] | [High/Medium/Low] |

Include sample rows demonstrating common crawl errors (404s, server errors, redirect chains, timeout issues) and explain the priority classification logic.
```

## 用法 / Usage
- 必填變數 / Variables: {{reporting-frequency}}、{{seo-tool}}、{{technical-expertise-level}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Automated Crawl Error Detection Script Setup is a free AI prompt that builds complete configuration instru…

# HTTPS Implementation Guide for SEO and Security

## 簡介

The HTTPS Implementation Guide for SEO and Security is a free AI prompt that produces a customized migration roadmap for web developers, SEO specialists, and site administrators moving their websites from HTTP to HTTPS. This HTTPS migration prompt for ChatGPT walks through every phase of the transition: selecting and installing SSL/TLS certificates, configuring server and CMS settings, updating internal links and media resources, implementing 301 redirects, and preserving search rankings throughout the process. It adapts technical depth to your stated expertise level and accounts for your specific hosting provider, CMS platform, and security concerns. Use it when you need to secure data transmission, meet Google's HTTPS preference for ranking, or comply with browser security warnings on non-HTTPS sites. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and outputs a numbered action plan with lettered sub-steps for each phase. ● Produces a pre-migration audit checklist and SSL certificate acquisition steps specific to your hosting environment ● Includes server and CMS configuration instructions, 301 redirect patterns, and internal link update strategies ● Covers search engine notification procedures, verification testing, and post-migration monitoring for ranking preservation ● Addresses common pitfalls like mixed content warnings, broken resources, and crawl budget impact during the transition ## Prompt

```
## Role
You are an expert web security specialist with deep knowledge of HTTPS implementation, SSL/TLS protocols, and technical SEO best practices.

## Task
Provide a comprehensive, step-by-step guide for implementing HTTPS site-wide. Cover SSL certificate acquisition and installation, content migration, redirect configuration, resource updates, and SEO preservation strategies. Address common challenges and verification procedures.

## Context
Website: {{website-url}}
Hosting provider: {{hosting-provider}}
CMS: {{cms}}
Technical expertise level: {{technical-expertise}}
Primary concerns: {{primary-concerns}}

The implementation must enhance security while maintaining or improving search engine rankings. Account for the user's technical background when explaining procedures and troubleshooting steps.

## Output
Deliver the guide as a numbered list with lettered sub-points (a, b, c) for detailed steps within each main section. Include:

1. Pre-migration preparation and audit
2. SSL certificate selection, acquisition, and installation procedures
3. Server and CMS configuration for HTTPS
4. Content and resource migration (internal links, media, scripts, stylesheets)
5. Redirect implementation (301 redirects from HTTP to HTTPS)
6. Search engine and external service updates
7. Testing and verification procedures
8. Post-migration monitoring and troubleshooting
9. Common pitfalls and how to avoid them

Tailor technical depth and terminology to the stated expertise level. Highlight solutions specific to the hosting provider and CMS when applicable.
```

## 用法 / Usage
- 必填變數 / Variables: {{cms}}、{{hosting-provider}}、{{primary-concerns}}、{{technical-expertise}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The HTTPS Implementation Guide for SEO and Security is a free AI prompt that produces a customized migration r…

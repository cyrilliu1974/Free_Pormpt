# HTTPS Migration Checklist Generator for Websites

## 簡介

The HTTPS Migration Checklist Generator for Websites is a free AI prompt that creates a complete, actionable migration plan for website administrators transitioning from HTTP to HTTPS. This HTTPS migration prompt for ChatGPT produces a ten-step checklist covering SSL certificate procurement, server configuration, internal link updates, 301 redirects, security header setup, search engine notification, and ongoing monitoring. You provide a website URL, and the prompt returns a structured checklist with clear action items for procurement, installation, testing, and post-migration tasks like updating sitemaps, configuring HSTS headers, and checking for mixed content warnings. It runs on ChatGPT, Claude, Gemini, and Grok. Use it when planning a site-wide security upgrade, preparing for compliance requirements, or improving search ranking signals through secure protocols. ● Covers all critical steps from certificate authority procurement through final monitoring and certificate renewal planning ● Includes additional considerations for analytics tracking code, third-party integrations, canonical URLs, and social media metadata updates ● Provides checkbox format for easy progress tracking and team coordination during migration ● Addresses technical details like server binding, 301 redirect implementation, security headers, and mixed content resolution ## Prompt

```
## Role
You are an expert website administrator specializing in SSL certificate configuration and secure HTTPS migration.

## Task
Generate a comprehensive, sequential checklist for migrating {{website-url}} from HTTP to HTTPS.

## Output
Provide a complete migration checklist structured as follows:

**Website:** {{website-url}}

**HTTPS Migration Checklist:**

⬜ Step 1: [Procurement - obtaining SSL certificate from certificate authority or provider]

⬜ Step 2: [Installation - installing SSL certificate on web server]

⬜ Step 3: [Server configuration - enabling HTTPS and binding certificate]

⬜ Step 4: [Internal links - updating all internal URLs from HTTP to HTTPS]

⬜ Step 5: [External resources - updating embedded content, APIs, and CDN links]

⬜ Step 6: [Redirects - implementing 301 redirects from HTTP to HTTPS]

⬜ Step 7: [Testing - verifying SSL certificate installation and HTTPS functionality]

⬜ Step 8: [Security headers - configuring HSTS and other security headers]

⬜ Step 9: [Search engines - updating sitemaps and notifying search consoles]

⬜ Step 10: [Monitoring - checking for mixed content warnings and certificate expiration]

**Additional Considerations:**

- Update analytics and tracking code configurations
- Verify third-party integrations support HTTPS
- Plan certificate renewal process before expiration
- Monitor performance and troubleshoot any issues
- Update social media sharing metadata and canonical URLs

Each step should include clear, actionable details appropriate for the specific website infrastructure.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The HTTPS Migration Checklist Generator for Websites is a free AI prompt that creates a complete, actionable m…

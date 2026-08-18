# SEO 404 Error Monitoring and Redirect Workflow

## 簡介

The SEO 404 Error Monitoring and Redirect Workflow is a free AI prompt that builds a complete system for tracking broken links and automating redirect implementation for website owners and SEO professionals. This technical SEO prompt for ChatGPT creates a structured workflow that sets up automated crawlers to scan your site at custom intervals, logs every 404 error in your tracking system, analyzes each broken URL to determine the best redirect destination, and implements 301 redirects to preserve link equity. It runs on ChatGPT, Claude, and Gemini, delivering a flow-chart-style process that includes monthly reporting and quarterly manual audits. Use it when you need to prevent traffic loss from broken links, maintain search engine rankings after site migrations, or establish ongoing 404 monitoring as part of your technical SEO practice. ● Configures automated crawlers to detect 404 errors at your chosen scan frequency and log findings in your preferred tracking system ● Analyzes each broken URL to identify whether the page moved, was deleted, or became outdated, then determines the most relevant redirect destination ● Generates monthly reports showing new 404 errors, implemented 301 redirects, and success rates for ongoing performance tracking ● Includes quarterly manual spot-check procedures to verify that redirects remain functional and relevant over time ## Prompt

```
## Role
You are a web development engineer specializing in SEO, information architecture, and technical SEO auditing.

## Task
Develop a comprehensive workflow for monitoring {{website-url}} for 404 errors on an ongoing basis and implementing 301 redirects to maintain SEO equity. Present the workflow as a clear, easy-to-follow flow chart.

## Workflow Structure

**1. Set up automated website crawler to scan {{website-url}} for 404 errors**
   - Configure crawler to run at {{scan-frequency}}
   - Log all detected 404 errors with full URLs in {{tracking-system}}

**2. For each new 404 error logged:**
   - Analyze URL to determine appropriate redirect
     - If page moved, identify new URL
     - If page deleted, identify most relevant alternative URL
     - If page outdated, identify up-to-date replacement content
   - Implement 301 redirect from 404 URL to chosen destination
     - Add redirect rule to server configuration
     - Test redirect with HTTP status checker tool
     - Confirm redirect is functioning with HTTP 301 status
   - Update {{tracking-system}} log
     - Mark 404 URL as redirected
     - Note redirect destination URL

**3. Generate monthly report from {{tracking-system}}**
   - List all new 404 errors detected
   - Show 301 redirects implemented
   - Calculate percentage of 404 errors successfully redirected

**4. Schedule quarterly manual spot-checks**
   - Randomly check sample of redirected URLs
   - Ensure redirects still relevant and functional

## Key Principles
- Configure scan frequency to balance timely detection with server load
- Prioritize user experience and site navigation when choosing redirect destinations
- Implement redirects promptly to minimize SEO and UX impact
- Maintain accurate tracking for all errors and their resolution status
```

## 用法 / Usage
- 必填變數 / Variables: {{scan-frequency}}、{{tracking-system}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The SEO 404 Error Monitoring and Redirect Workflow is a free AI prompt that builds a complete system for track…

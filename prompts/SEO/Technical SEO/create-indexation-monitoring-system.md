# Indexation Monitoring System for Google Search Console

## 簡介

The Indexation Monitoring System for Google Search Console is a free AI prompt that designs a complete technical SEO monitoring framework for website managers and SEO professionals. This indexation monitoring prompt for ChatGPT builds a full specification for tracking which pages search engines index, combining data from Google Search Console, log file analyzers, and crawling tools like Screaming Frog into a single dashboard. It defines metrics for indexed versus crawled pages, index coverage status, and crawl budget efficiency, then structures dashboard components including trend graphs, status breakdowns by page type, and prioritized issue tables. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing alert rules for indexation drops, weekly digests, and actionable recommendations tied to technical SEO barriers, sitemap problems, and internal linking gaps. Use it when you need a repeatable system to catch de-indexation events before they harm organic traffic. ● Consolidates Google Search Console coverage data, server logs, and crawler reports into one monitoring framework ● Defines dashboard views for indexation trends, page-type breakdowns, and top non-indexed URLs with issue codes ● Generates alert thresholds and notification rules for indexation rate drops and sudden spikes in excluded pages ● Delivers prioritized insights in Issue → Recommendation → Impact format, covering technical barriers, crawl budget waste, and sitemap optimization ## Prompt

```
## Role
You are an SEO and web analytics expert specializing in website indexation monitoring and reporting.

## Task
Design a comprehensive indexation monitoring and reporting system for {{website-url}}. Integrate data from Google Search Console and other relevant tools into a centralized dashboard that provides clear, actionable insights.

## Output
Deliver a complete monitoring system specification structured as:

**Website URL:** {{website-url}}

**Data sources:**
- Google Search Console
- Log file analysis tools
- Site crawlers (Screaming Frog, Sitebulb, or similar)

**Indexation metrics:**
1. Total indexed vs. crawled pages
2. Index coverage status (valid, excluded, errors)
3. Crawl budget utilization and efficiency

**Dashboard components:**
1. Overall indexation status:
   ✅ Indexed pages: [count and percentage]
   ❌ Non-indexed pages: [count and percentage]
2. Indexation trend over time (line graph showing 90-day history)
3. Indexation status by page type/category (pie chart)
4. Top non-indexed pages with issues (table: URL | Issue Type | Recommendation)
5. Crawl stats: requests per day, fetch errors, robots.txt blocked URLs

**Alerts and notifications:**
- Email alert when indexation rate drops below 85%
- Weekly email digest of indexation status and trends
- Immediate alert for sudden spikes in excluded or error pages (>10% change)

**Insights and recommendations:**
Provide 3-5 prioritized insights based on the data, each following this format:
- **Issue identified** → **Specific recommendation** → **Expected impact**

Focus on: technical SEO barriers, content quality signals, crawl budget waste, sitemap optimization, and internal linking improvements.

**Next steps:**
1. Implement the monitoring system using available tools
2. Establish baseline metrics and set performance targets
3. Schedule weekly dashboard reviews and monthly deep-dive audits
4. Create a remediation workflow for newly discovered indexation issues
5. Document all changes and track their impact on indexation rates
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Indexation Monitoring System for Google Search Console is a free AI prompt that designs a complete technic…

# Website Caching Optimization Protocol Prompt

## 簡介

The Website Caching Optimization Protocol Prompt is a free AI prompt that produces a comprehensive technical roadmap for diagnosing, testing, and implementing optimal caching policies on any website. This website caching prompt for ChatGPT walks you through six structured phases: establishing baseline performance metrics with tools like PageSpeed Insights and WebPageTest, auditing existing cache headers and server configurations, optimizing Cache-Control and ETag directives, deploying multi-level caching (browser, server, CDN, database), load-testing different scenarios, and setting up continuous monitoring with real user metrics. It runs on ChatGPT, Claude, Gemini, and Grok, delivering a procedural document ready for technical teams to follow. Use it when you need to reduce Time to First Byte, improve Core Web Vitals, or troubleshoot slow-loading assets on a live site. ● Covers baseline measurement, header audits, Cache-Control tuning, reverse proxy setup, CDN integration, and load testing in a single workflow. ● Names specific technologies - Varnish, Nginx, Redis, Memcached, Apache Bench, JMeter - and explains when and how to deploy each. ● Includes test scenarios for empty-cache first visits, primed-cache returns, and forced refreshes to validate real-world behavior. ● Emphasizes iterative monitoring with cache hit/miss analysis and real user monitoring tools for continuous improvement. ## Prompt

```
## Role

You are an expert website performance engineer specializing in optimizing caching policies to improve site speed and content delivery efficiency.

## Task

Provide a comprehensive, step-by-step protocol for testing and fine-tuning caching configurations on {{website-url}}. Focus on actionable steps to diagnose performance bottlenecks, experiment with different caching strategies, measure their impact, and implement the optimal policy.

## Output

Deliver the protocol as a clear, procedural document for technical audiences. Include specific tools, technologies, and techniques for each step. Emphasize measuring performance impact and iterating based on results.

Structure your response with these sections:

**Step 1: Establish Baseline Metrics**
- Use tools like Google PageSpeed Insights, GTmetrix, or WebPageTest to measure current performance
- Record key metrics: Time to First Byte (TTFB), First Contentful Paint (FCP), Largest Contentful Paint (LCP), Total Blocking Time (TBT), Cumulative Layout Shift (CLS)
- Identify the slowest loading pages and assets as optimization targets

**Step 2: Audit Existing Caching Setup**
- Inspect HTTP headers to determine current caching policy:
  - Cache-Control directives (max-age, no-cache, must-revalidate)
  - ETag and Last-Modified headers for validation
- Review server configuration files (.htaccess, nginx.conf) for caching rules
- Check for proper use of expires headers and cache-busting techniques

**Step 3: Optimize Caching Headers**
- Set appropriate Cache-Control headers for static assets:
  - Long max-age values (1 year) for versioned assets like CSS, JS, images
  - Shorter max-age for frequently updated content
- Ensure ETag and Last-Modified headers are present for efficient validation
- Leverage browser caching by setting optimal expires headers

**Step 4: Implement Caching at Various Levels**
- Enable server-side caching:
  - Configure reverse proxy caching (Varnish, Nginx)
  - Utilize application-level caching frameworks (Redis, Memcached)
- Implement database query result caching to reduce server load
- Explore edge caching with a Content Delivery Network (CDN) for global distribution

**Step 5: Test Caching Policies**
- Simulate different user scenarios and measure performance impact:
  - First-time visitor (empty cache)
  - Returning visitor (primed cache)
  - Visitor with forced cache refresh
- Use tools like Apache Bench or JMeter for load testing
- Verify proper caching behavior by inspecting HTTP headers and server logs

**Step 6: Monitor and Iterate**
- Continuously monitor site performance using real user monitoring (RUM) tools
- Analyze cache hit/miss ratios and identify areas for improvement
- Experiment with different caching durations and configurations
- Regularly review and update caching policies based on performance data and changing requirements

Conclude with a summary emphasizing the importance of documenting findings and configurations for future reference and maintainability.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Website Caching Optimization Protocol Prompt is a free AI prompt that produces a comprehensive technical r…

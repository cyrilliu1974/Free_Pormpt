# XML Sitemap Creation Guide for Large Websites

## 簡介

The XML Sitemap Creation Guide for Large Websites is a free AI prompt that walks SEO specialists and webmasters through the complete process of generating, validating, and deploying XML sitemaps for sites of any scale. This XML sitemap prompt for ChatGPT, Claude, and Gemini produces tool-specific instructions tailored to your sitemap generator, website URL, content types, and update schedule. It covers preparation and configuration, content discovery rules, crawl execution, priority and changefreq optimization, multi-sitemap handling for sites exceeding 50,000 URLs, validation, robots.txt integration, and submission to Google Search Console and Bing Webmaster Tools. Real-world use cases include enterprise e-commerce sites with thousands of product pages, news publishers with high-frequency content updates, and multi-language platforms requiring hreflang sitemap support. Reach for this prompt when you need structured, actionable guidance that adapts to your specific sitemap tool and ensures technical SEO best practices are followed at every step. ● Configures crawl depth, URL patterns, and exclusion rules to capture all important content types while filtering out admin pages and duplicates ● Sets priority and changefreq values per page type, splits sitemaps when exceeding 50,000 URLs or 50MB, and generates sitemap index files ● Provides validation checks, deployment instructions, robots.txt syntax, and submission workflows for Google Search Console and Bing Webmaster Tools ● Includes scheduling for automatic regeneration and monitoring to keep sitemaps synchronized with site changes and content updates ## Prompt

```
## Role
You are an expert SEO specialist with deep knowledge of XML sitemap generation and technical SEO implementation.

## Task
Guide the user through creating a comprehensive XML sitemap for their website using their chosen sitemap generator tool. Provide clear, actionable steps that ensure all important pages are indexed and SEO best practices are followed.

## Context
Website: {{website-url}}
Sitemap generator tool: {{sitemap-tool}}
Primary content types: {{content-types}}
Desired update frequency: {{update-frequency}}

## Instructions
1. **Preparation & Tool Setup**
   - Access {{sitemap-tool}} and configure basic settings
   - Enter {{website-url}} as the root domain
   - Set crawl depth appropriate for site size

2. **Content Discovery Configuration**
   - Configure the tool to identify {{content-types}}
   - Set URL patterns and exclusion rules (admin pages, thank-you pages, duplicate content)
   - Enable detection of images, videos, and alternative language versions if applicable

3. **Crawl Execution & Quality Check**
   - Initiate the sitemap generation crawl
   - Monitor for errors, broken links, and redirect chains
   - Verify that all priority page types are discovered

4. **Sitemap Optimization**
   - Set appropriate priority values (0.0-1.0) based on page importance
   - Configure changefreq tags to {{update-frequency}} or per content type
   - Split into multiple sitemaps if page count exceeds 50,000 URLs or 50MB
   - Create a sitemap index file if using multiple sitemaps

5. **Validation & Deployment**
   - Validate XML syntax using the tool's built-in validator or external checker
   - Upload sitemap(s) to website root directory or appropriate location
   - Add sitemap location to robots.txt: `Sitemap: https://{{website-url}}/sitemap.xml`

6. **Search Engine Submission**
   - Submit sitemap via Google Search Console
   - Submit via Bing Webmaster Tools
   - Monitor indexing status and coverage reports

7. **Ongoing Maintenance**
   - Schedule automatic regeneration at {{update-frequency}}
   - Set up monitoring for sitemap errors or accessibility issues
   - Review and update as site structure or content strategy evolves

## Output
Deliver each step with specific actions tailored to {{sitemap-tool}}, highlighting any configuration options unique to that tool.
```

## 用法 / Usage
- 必填變數 / Variables: {{content-types}}、{{sitemap-tool}}、{{update-frequency}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The XML Sitemap Creation Guide for Large Websites is a free AI prompt that walks SEO specialists and webmaster…

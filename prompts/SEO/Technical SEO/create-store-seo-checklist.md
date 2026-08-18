# E-Commerce SEO Audit Checklist Generator

## 簡介

The E-Commerce SEO Audit Checklist Generator is a free AI prompt that creates customized, platform-specific SEO audit checklists for online store owners and digital marketers. This e-commerce SEO prompt for ChatGPT, Claude, Gemini, and Grok transforms generic optimization advice into measurable action items tailored to your specific platform (Shopify, WooCommerce, BigCommerce, Magento, or custom builds). By analyzing your business context - platform type, SEO goals, current traffic, and technical capabilities - it generates a multi-phase checklist covering technical foundations, on-page elements, e-commerce-specific optimizations, and measurement systems. Store owners use it to systematically improve product rankings, fix technical issues, and track progress with concrete success criteria. The prompt adapts phase complexity from 3 simple steps for basic stores to 15 detailed phases for enterprise overhauls. Reach for this prompt when you need to turn SEO theory into a concrete action plan that respects your platform's constraints and your team's technical skill level. ● Adapts audit complexity dynamically based on platform, technical access, and business maturity ● Includes implementation tracking tables with priority scoring, status fields, and impact documentation ● Covers technical SEO (speed, crawlability, mobile), on-page optimization, product schema, and category page best practices ● Provides specific tool recommendations, success metrics, and monthly review workflows for non-technical users ## Prompt

```
## Role

You are an expert SEO strategist with deep e-commerce platform experience. You understand how search algorithms interact with different platforms and translate technical SEO concepts into actionable steps for store owners.

## Task

Create a comprehensive, platform-specific SEO audit checklist that transforms generic optimization advice into measurable, trackable actions. The checklist must adapt to the user's e-commerce platform, technical capabilities, and business goals.

## Context

**User Information Required:**

{{business-context}}

*Provide: (1) E-commerce platform (Shopify, WooCommerce, BigCommerce, Magento, custom, or other); (2) Primary SEO goal (product search rankings, category page rankings, local presence, technical fixes, or complete overhaul); (3) Current monthly organic traffic estimate; (4) Technical capability (developer access available, or no-code solutions only)*

**Adaptive Phase Logic:**

Determine the optimal number of audit phases (3–15) based on:

- Platform complexity and constraints
- User's technical skill level
- Current SEO maturity
- Scope of desired outcomes

*Guidelines:* Simple stores: 3–5 phases | Growing businesses: 6–8 phases | Enterprise operations: 9–12 phases | Complete overhauls: 13–15 phases

## Output

Deliver a structured SEO audit checklist organized into dynamic phases. Each phase must include:

### Technical Foundation Audit

**Site Speed & Performance**
- Page load time under 3 seconds (test with PageSpeed Insights)
- Images optimized and lazy-loaded
- Minimize JavaScript/CSS blocking
- Enable browser caching
- CDN implementation for global reach

**Crawlability & Indexation**
- XML sitemap submitted to Google Search Console
- Robots.txt properly configured
- Zero crawl errors in Search Console
- Canonical tags on all pages
- Pagination handled correctly

**Mobile Optimization**
- Mobile-responsive design verified
- Touch elements properly spaced (min 48px)
- Text readable without zooming
- Mobile page speed optimized

**Site Architecture**
- Clean URL structure: domain.com/category/product
- Breadcrumb navigation implemented
- Strategic internal linking
- 404 pages redirect or provide value
- HTTPS across entire site

### On-Page SEO Elements

**Keyword Mapping**
- Primary keyword identified for each page
- Search intent matched (informational vs transactional)
- Keyword difficulty assessed
- Competitor gap analysis completed

**Title Tags & Meta Descriptions**
- Unique title tags for every page (under 60 characters)
- Primary keyword near beginning of title
- Compelling meta descriptions under 160 characters
- Include emotional triggers or unique selling points

**Content Optimization**
- H1 tag contains primary keyword
- H2–H3 tags create logical hierarchy
- First 100 words include target keyword naturally
- Content answers user intent comprehensively
- Related keywords integrated organically

**Image SEO**
- Descriptive file names (product-name-color.jpg)
- Alt text describes image and includes keyword
- Images compressed without quality loss
- Next-gen formats used (WebP)

### E-commerce Specific SEO

**Product Page Optimization**
- Unique product descriptions (no manufacturer copy)
- Customer reviews visible with schema markup
- Product specifications in structured format
- Related products linked strategically
- Out-of-stock handling preserves SEO value

**Category/Collection Pages**
- Descriptive category content (300+ words)
- Faceted navigation avoids duplicate content
- Sort/filter options don't generate new URLs
- Category page titles optimized for target keywords
- Internal linking between related categories

**Schema Markup Implementation**
- Product schema (price, availability, reviews)
- Breadcrumb schema
- Organization schema
- FAQ schema where applicable
- Local business schema (if physical presence)

### Measurement & Tracking System

**Implementation Tracking Template:**

| Task Category | Specific Task | Priority (1–5) | Status | Date Completed | Impact Notes | Next Review |
|--------------|---------------|----------------|---------|----------------|--------------|-------------|
| Technical SEO | Page Speed < 3s | 5 | In Progress | — | — | Monthly |
| On-Page | Title Tag Optimization | 4 | Complete | MM/DD/YY | +15% CTR | Quarterly |

**Key Metrics to Monitor:**
- Organic traffic growth (weekly)
- Keyword ranking improvements (bi-weekly)
- Page load times (monthly)
- Crawl errors (weekly)
- Conversion rate from organic traffic (monthly)

**Tools Setup Checklist:**
- Google Search Console verified
- Google Analytics 4 configured
- Platform-specific SEO app installed
- Rank tracking tool selected and active
- Technical monitoring alerts enabled

**Monthly Review Process:**
1. Export Search Console performance data
2. Identify top performing pages and queries
3. Find quick-win optimization opportunities
4. Update checklist task priorities
5. Document wins and learnings

Format all checklist items as actionable tasks with clear success criteria. Prioritize based on platform constraints, technical capability, and expected impact on the stated SEO goal. Make the checklist foolproof for non-technical users by including specific tools, metrics, and next steps.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The E-Commerce SEO Audit Checklist Generator is a free AI prompt that creates customized, platform-specific SE…

# Video Schema Markup Implementation Guide

## 簡介

The Video Schema Markup Implementation Guide is a free AI prompt that analyzes video content and produces structured data implementation plans for websites seeking better search visibility. This video schema markup prompt for ChatGPT walks through the technical process of adding JSON-LD or Microdata to web pages, covering required schema.org properties like name, description, thumbnailUrl, uploadDate, duration, and contentUrl alongside recommended optional fields. It delivers two outputs: detailed implementation instructions including HTML placement and validation steps using Google's Rich Results Test, plus a markdown table inventorying all videos with titles, descriptions, and URLs ready for markup. Works on ChatGPT, Claude, and Gemini. Use this prompt when you need to make video content eligible for rich snippets in search results, improve click-through rates by surfacing video metadata to search engines, or streamline the technical SEO process for sites with embedded or hosted video libraries. ● Produces step-by-step JSON-LD and Microdata formatting instructions specific to your website and video library ● Creates a three-column markdown table organizing video titles, descriptions, and URLs for efficient markup deployment ● Includes validation guidance using Google's Rich Results Test to confirm correct implementation ● Covers both required and optional schema.org VideoObject properties to maximize search engine understanding ## Prompt

```
## Role
You are an SEO specialist implementing Video Schema Markup to improve video discoverability and search engine visibility.

## Task
Analyze the provided video content and create a comprehensive Video Schema Markup implementation plan. Deliver step-by-step instructions for adding structured data to the website, followed by a structured inventory of videos ready for markup.

## Context
Website: {{website-url}}

Video content and context: {{video-content-description}}

Target audience: {{target-audience}}

## Output
Provide your response in two parts:

1. **Implementation Instructions**: Step-by-step guidance for adding Video Schema Markup to the website pages, including:
   - How to structure the JSON-LD or Microdata
   - Required schema.org properties (name, description, thumbnailUrl, uploadDate, duration, contentUrl)
   - Recommended optional properties
   - Where to place the markup in the HTML
   - Validation steps using Google's Rich Results Test

2. **Video Inventory Table**: A markdown table with three columns:

| Video Title | Video Description | Video URL |
|-------------|-------------------|-----------|
```

## 用法 / Usage
- 必填變數 / Variables: {{target-audience}}、{{video-content-description}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Video Schema Markup Implementation Guide is a free AI prompt that analyzes video content and produces stru…

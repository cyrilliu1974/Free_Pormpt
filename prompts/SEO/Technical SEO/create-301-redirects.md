# 301 Redirect Mapping Generator for Website Migrations

## 簡介

The 301 Redirect Mapping Generator is a free AI prompt that creates structured redirect tables for web developers and SEO specialists managing website migrations or restructuring. This 301 redirect prompt for ChatGPT takes your website structure changes and target SEO keywords, then produces a complete mapping table with old URLs matched to their optimal new destinations. The prompt analyzes content relevance, preserves keyword targeting, identifies potential redirect chains or orphaned pages, and delivers implementation-ready tables with full URLs. It runs on ChatGPT, Claude, and Gemini, making it compatible with most modern AI workflows. Use it when migrating domains, consolidating site sections, changing URL structures, or launching redesigns where maintaining search rankings is critical. ● Analyzes website structure changes and maps old URLs to new destinations based on content relevance and SEO keyword alignment ● Flags redirect issues like broken chains, orphaned content, and keyword cannibalization before implementation ● Outputs markdown tables with full URLs formatted for immediate technical deployment ● Includes implementation recommendations covering redirect validation, testing procedures, and post-migration monitoring ## Prompt

```
## Role
You are an expert web developer specializing in SEO and URL management.

## Task
Create a comprehensive 301 redirect mapping table from old URLs to new URLs. Analyze the website structure changes, ensure logical URL mapping that preserves SEO value, and provide implementation recommendations.

## Context
{{website-structure-changes}}

Primary SEO keywords to preserve: {{seo-keywords}}

## Process
1. Identify all URLs requiring redirection based on the structural changes described
2. Map each old URL to its most appropriate new destination, maintaining content relevance and keyword targeting
3. Ensure redirects preserve link equity and user intent
4. Flag any potential issues (broken redirect chains, orphaned content, keyword cannibalization)

## Output
Provide:
- Brief summary of the redirect strategy and any important considerations
- Markdown table with two columns: **Old URL** and **New URL**
- Implementation recommendations (redirect type confirmation, testing approach, monitoring suggestions)

Format the table with actual full URLs ready for technical implementation.
```

## 用法 / Usage
- 必填變數 / Variables: {{seo-keywords}}、{{website-structure-changes}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The 301 Redirect Mapping Generator is a free AI prompt that creates structured redirect tables for web develop…

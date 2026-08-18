# Keyword Intent Classification for User Queries

## 簡介

The Keyword Intent Classification for User Queries is a free AI prompt that analyzes search behavior to categorize keywords by intent for SEO strategists and content marketers. This keyword intent prompt for ChatGPT examines user queries within your industry context, extracting primary keywords, estimating monthly search volumes, and assigning each to one of four standard SEO intent categories: informational (seeking knowledge), navigational (finding a specific site), commercial (researching options), or transactional (ready to convert). The prompt generates a structured markdown table and delivers 2-3 strategic content recommendations based on the intent distribution you uncover. It runs on ChatGPT, Claude, Gemini, and Grok, adapting to your target audience and competitive landscape. Reach for this prompt when you need to audit existing traffic patterns, prioritize content creation by user intent, or align landing pages with the search behaviors driving your organic visibility. ● Classifies each keyword by intent type (informational, navigational, commercial, transactional) using standard SEO taxonomy. ● Estimates monthly search volume within industry norms to help prioritize keyword targets. ● Outputs a markdown table format that integrates directly into briefs, audits, and strategy decks. ● Delivers tailored content optimization recommendations based on the intent mix in your query set. ## Prompt

```
## Role
You are an expert SEO analyst specializing in keyword intent classification.

## Task
Analyze the provided user queries to extract keywords, estimate their search volume, and classify their search intent according to standard SEO categories: informational, navigational, commercial investigation, or transactional.

## Context
Target audience: {{target-audience}}
Industry: {{industry}}
Website and competitive landscape: {{website-and-competitors}}

User queries to analyze:
{{user-queries}}

## Analysis Framework
For each query:
1. Identify the primary keyword or keyword phrase
2. Estimate monthly search volume based on typical patterns in the industry
3. Classify intent:
   - **Informational**: seeking knowledge or answers
   - **Navigational**: looking for a specific site or page
   - **Commercial**: researching options before purchase
   - **Transactional**: ready to take action or convert

## Output
Present your analysis as a markdown table:

| KEYWORD | SEARCH VOLUME | INTENT |
|---------|---------------|--------|
| [keyword] | [estimated monthly volume] | [intent category] |

After the table, provide 2-3 strategic recommendations for content optimization based on the intent distribution.
```

## 用法 / Usage
- 必填變數 / Variables: {{industry}}、{{target-audience}}、{{user-queries}}、{{website-and-competitors}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Keyword Intent Classification for User Queries is a free AI prompt that analyzes search behavior to catego…

# SEO User Intent Analyzer for Keyword Research

## 簡介

The SEO User Intent Analyzer for Keyword Research is a free AI prompt that classifies search intent and evaluates strategic value for website optimization. This keyword research prompt for ChatGPT generates 10-15 related search queries for any target keyword, then categorizes each by user intent (informational, navigational, commercial, transactional), scores its relevance to your business on a 1-10 scale, and recommends concrete actions such as creating content, optimizing pages, or targeting paid search. It runs on ChatGPT, Claude, Gemini, and Grok, delivering a structured markdown table plus a strategic summary of the top three opportunities and content gaps. SEO professionals, content marketers, and website owners use this prompt to move beyond surface-level keyword lists and understand what users really want when they search. By mapping intent to business context, you can prioritize the queries that drive conversions and avoid wasting effort on low-value terms. ● Generates 10-15 related search queries for any keyword, surfacing variations users actually type ● Classifies each query by intent type (informational, navigational, commercial, transactional) to align content with funnel stage ● Scores relevance on a 1-10 scale based on your specific business context and website goals ● Recommends specific next steps for each query: create content, optimize existing pages, ignore, monitor competitors, or bid in paid search ● Outputs a markdown table for easy sorting and a summary highlighting the top three opportunities and strategy gaps ## Prompt

```
## Role
You are an expert SEO analyst specializing in search intent analysis and keyword strategy optimization.

## Task
Analyze search queries related to a specific keyword and assess their strategic value for website SEO. For each related query, determine user intent, score its relevance, and recommend concrete actions.

## Context
Keyword: {{keyword}}
Website: {{website-url}}
Business context: {{business-context}}

## Process
1. Brainstorm 10-15 related search queries that users might enter when researching {{keyword}}
2. Classify the user intent for each query (informational, navigational, commercial, transactional)
3. Score relevance to the website on a 1-10 scale based on alignment with the business context
4. Recommend specific actions: create content, optimize existing pages, ignore, monitor competitors, or target for paid search

## Output
Present your analysis as a markdown table:

| Search Query | User Intent | Relevance Score (1-10) | Recommended Action |
|--------------|-------------|------------------------|--------------------|

After the table, provide a brief summary highlighting the top 3 opportunities and any gaps in current content strategy.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{keyword}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SEO User Intent Analyzer for Keyword Research is a free AI prompt that classifies search intent and evalua…

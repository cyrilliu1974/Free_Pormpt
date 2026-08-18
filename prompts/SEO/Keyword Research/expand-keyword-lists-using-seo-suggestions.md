# Keyword Expansion Prompt for SEO Research

## 簡介

The Keyword Expansion Prompt for SEO Research is a free AI prompt that generates related keyword suggestions with estimated search volumes for SEO professionals and content marketers. This keyword research prompt for ChatGPT analyzes your original keywords and business context to produce 10-20 high-value variations per seed keyword, organized in a structured markdown table. It considers search intent variations (informational, commercial, transactional), long-tail opportunities, semantic relationships, and competitive difficulty to surface keywords that match your target audience and market. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering actionable keyword lists that help you identify content gaps and ranking opportunities without requiring separate keyword research tools. Reach for this prompt when you need to quickly expand a seed keyword list, discover long-tail variations, or validate content ideas with volume estimates before investing in paid keyword tools. ● Analyzes search intent variations to uncover informational, commercial, and transactional keyword opportunities ● Estimates search volumes based on keyword characteristics and market size without requiring third-party API access ● Considers ranking difficulty and competition level to surface realistic opportunities ● Outputs results in a three-column markdown table mapping original keywords to suggestions with volume data ## Prompt

```
## Role
You are an expert SEO keyword researcher specializing in keyword expansion and search volume analysis.

## Task
Expand the provided keyword list by generating related keyword suggestions that match search intent, relevance, and competitive opportunity. Analyze and estimate search volumes for each suggested keyword.

## Context
**Business context:** {{business-context}}
(Include: target website/business, industry, target audience, and geographic focus)

**Original keywords:** {{original-keywords}}

## Process
1. Review the original keyword list and business context
2. Generate related keywords considering:
   - Search intent variations (informational, commercial, transactional)
   - Long-tail opportunities
   - Semantic relationships and topical relevance
   - Competition level and ranking difficulty
3. Estimate search volumes based on keyword characteristics and market size

## Output
Provide your results as a markdown table with three columns:

| Original Keyword | Suggested Keyword | Search Volume |
|-----------------|-------------------|---------------|
| ...             | ...               | ...           |

Include 10-20 high-value keyword suggestions per original keyword where applicable.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{original-keywords}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Keyword Expansion Prompt for SEO Research is a free AI prompt that generates related keyword suggestions w…

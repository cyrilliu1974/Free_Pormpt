# Factual Error Correction Prompt for Content Editing

## 簡介

The Factual Error Correction Prompt for Content Editing is a free AI prompt that identifies and corrects factual inaccuracies in written content while preserving the original voice, intent, and audience alignment. This factual error correction prompt for ChatGPT works by systematically analyzing the provided text, flagging every inaccuracy, researching verified information from reliable sources, and delivering a polished rewrite structured using dependency grammar principles for clarity. It runs on ChatGPT, Claude, and Gemini, making it ideal for blog posts, articles, reports, marketing copy, educational materials, and any content where accuracy is non-negotiable. Use it when you need to salvage well-written content marred by outdated statistics, misattributed quotes, or incorrect claims without starting from scratch. ● Lists every factual inaccuracy found with brief explanations so you understand what went wrong ● Researches and applies correct information from reliable sources with transparent verification notes ● Rewrites sentences using dependency grammar to improve clarity while keeping the original tone, style, and audience fit intact ● Provides before-and-after versions with a summary of all changes and sources consulted for full editorial transparency ## Prompt

```
## Role
You are an expert content editor specializing in fact-checking and rewriting.

## Task
Correct factual errors in the provided content while preserving its original intent, tone, and style. Structure your rewrite using dependency grammar principles for maximum clarity and coherence.

## Context
**Content topic:** {{content-topic}}
**Target audience:** {{target-audience}}
**Writing style to maintain:** {{writing-style}}

## Process
Work through these steps systematically:

1. **Identify Errors** – List all factual inaccuracies found in the content
2. **Research** – Verify correct information from reliable sources
3. **Rewrite** – Apply dependency grammar framework to reconstruct sentences with accurate facts
4. **Review** – Confirm all errors are resolved and original intent is preserved

## Output
Deliver your response with these clear section headings:

### Original Content
[Display the content as provided]

### Identified Errors
[Numbered list of factual inaccuracies with brief explanations]

### Corrected Version
[Complete rewrite with accurate information, maintaining tone and style]

### Verification Notes
[Summary of changes made and sources consulted]
```

## 用法 / Usage
- 必填變數 / Variables: {{content-topic}}、{{target-audience}}、{{writing-style}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Factual Error Correction Prompt for Content Editing is a free AI prompt that identifies and corrects factu…

# Competitor Technical SEO Audit Prompt

## 簡介

The Competitor Technical SEO Audit Prompt is a free AI prompt that systematically evaluates a rival's website and surfaces exploitable weaknesses across all major ranking factors for SEO professionals and marketers. This competitor analysis prompt for ChatGPT examines technical implementation (crawlability, indexability, site speed, mobile usability, structured data), on-page optimization (title tags, meta descriptions, header structure, keyword targeting), content strategy, internal linking architecture, backlink profiles, user experience signals, and local SEO elements. You provide the competitor URL and your market context (industry, audience, geography), and it returns a three-column markdown table mapping each SEO factor to the competitor's current approach and specific opportunities for you to exploit or match. It runs reliably on ChatGPT, Claude, and Gemini. Reach for this prompt when you need to reverse-engineer a competitor's SEO strategy, prepare a client benchmark report, or identify quick-win gaps in a rival's technical foundation. ● Evaluates 10+ SEO dimensions including site speed, mobile-friendliness, structured data, keyword deployment, and backlink quality ● Outputs a markdown table with clear competitor strengths, weaknesses, and your specific opportunities to outrank them ● Accepts any competitor URL and market context, adapting analysis to your industry and geographic focus ● Surfaces technical vulnerabilities (broken canonicals, slow load times, thin content) and strategic gaps you can immediately target ## Prompt

```
## Role
You are an expert SEO analyst conducting a comprehensive technical SEO audit.

## Task
Analyze the competitor's website and identify their strengths and weaknesses across all major SEO factors. Examine technical implementation, content strategy, on-page optimization, backlink profile, site architecture, mobile usability, page speed, and other ranking signals. Evaluate what the competitor is doing well and where they are vulnerable.

## Context
Competitor website: {{competitor-url}}

Market context: {{market-context}}
(Include your industry, target audience, and geographic focus)

## Output
Present your findings as a markdown table with three columns:

| SEO Factor | Competitor's Approach | Opportunities for Improvement |
|------------|----------------------|-------------------------------|

Cover at minimum: technical SEO (crawlability, indexability, site speed, mobile-friendliness, structured data), on-page SEO (title tags, meta descriptions, header structure, keyword usage), content quality and strategy, internal linking, backlink profile, user experience signals, and local SEO factors if relevant.

Each row must provide clear, actionable insights that reveal specific weaknesses to exploit or strengths to match.
```

## 用法 / Usage
- 必填變數 / Variables: {{competitor-url}}、{{market-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Competitor Technical SEO Audit Prompt is a free AI prompt that systematically evaluates a rival's website …

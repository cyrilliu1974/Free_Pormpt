# Customer Feedback Executive Summary Prompt

## 簡介

The Customer Feedback Executive Summary Prompt is a free AI prompt that transforms raw customer feedback into a boardroom-ready executive brief for business leaders and customer experience teams. This customer feedback prompt for ChatGPT, Claude, Gemini, and Grok analyzes customer comments across channels and produces a structured summary under 600 words that highlights recurring themes, sentiment patterns, frequency data, and actionable recommendations. You provide the raw feedback, industry context, time period, and optional comparison data; the prompt returns a decision-ready brief with four sections: At a Glance takeaways, Key Themes analysis, Bright Spots highlighting what customers appreciate, and Recommended Actions tied directly to identified issues. It is designed for executives who need to absorb critical customer intelligence in under five minutes without wading through unstructured data. Reach for this prompt when you need to translate scattered feedback from surveys, support tickets, reviews, or social media into strategic insights that drive leadership decisions. ● Identifies the top 3–5 recurring themes with context on prevalence and trend direction when comparison data is available. ● Surfaces sentiment shifts and frequency patterns without fabricating unsupported statistics. ● Delivers 2–3 numbered, concrete action recommendations tied to customer pain points and opportunities. ● Formats output as a scannable executive brief with At a Glance bullets, thematic analysis, bright spots, and next steps. ## Prompt

```
## Role

You are an expert customer experience strategist translating raw feedback into boardroom-ready insights for executive leadership.

## Task

Distill customer feedback into a concise executive brief (<600 words) that busy leaders can absorb in under five minutes. Identify recurring themes, sentiment shifts, frequency patterns, and actionable insights. Write in a confident, direct tone without hedging language. Do not fabricate statistics unsupported by the data. If the dataset is too small for firm conclusions, acknowledge this in one sentence and proceed.

## Context

**Customer feedback data:**
{{customer-feedback}}

**Industry/business type:**
{{industry}}

**Time period:**
{{time-period}}

**Comparison data:**
{{comparison-data}}

## Output

Structure the brief with these sections:

**At a Glance**
3–4 specific, data-grounded bullet points capturing the most critical takeaways.

**Key Themes**
Cover the top 3–5 themes. For each, explain what customers are saying, how widespread the issue is, and whether it's improving or worsening (if comparison data exists).

**Bright Spots**
Highlight 1–2 things customers genuinely appreciate to show what's working.

**Recommended Actions**
Provide 2–3 concrete, numbered suggestions tied directly to identified themes.

Keep total length under 600 words. No methodology explanations or excessive caveats.
```

## 用法 / Usage
- 必填變數 / Variables: {{comparison-data}}、{{customer-feedback}}、{{industry}}、{{time-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Feedback Executive Summary Prompt is a free AI prompt that transforms raw customer feedback into …

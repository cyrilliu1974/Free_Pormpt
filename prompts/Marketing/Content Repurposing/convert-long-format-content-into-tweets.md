# Long-Form Content to Tweet Repurposing Prompt

## 簡介

The Long-Form Content to Tweet Repurposing Prompt is a free AI prompt that transforms articles, essays, and blog posts into tweet-ready content for entrepreneurs and creators building an audience on X (Twitter). This content repurposing prompt for ChatGPT analyzes your long-form writing and generates five distinct tweet variations, each under 280 characters. It extracts the most thought-provoking ideas with viral potential, varying the approach so some summarize the entire piece while others spotlight a single insight. The prompt runs on ChatGPT, Claude, Gemini, and Grok, preserving your original voice and meaning while adapting structure for maximum readability on social platforms. Use it when you need to amplify blog posts, newsletters, or thought leadership pieces across Twitter without manually distilling each concept. ● Produces five tweet variations per run, each with a different angle or focus drawn from your original content ● Enforces the 280-character limit and uses blank lines between idea blocks for readability ● Avoids hashtags and emojis, relying instead on punchy sentences and simple language ● Tailors tone and messaging to your target audience and personal positioning ## Prompt

```
## Role
You are a professional audience-building coach specializing in repurposing long-form content into high-performing tweets for entrepreneurs.

## Task
Generate 5 tweet ideas adapted from the provided long-form content. Each tweet must:

- Extract the most compelling, thought-provoking ideas with viral potential
- Vary the approach: some summarize the whole piece, others highlight one specific insight
- Stay within 280 characters (strict)
- Preserve the original meaning and voice; add words only when necessary
- Avoid hashtags and emojis entirely
- Use blank lines for readability: maximum 2 sentences per paragraph
- Favor short, punchy sentences and simple, direct language

## Context
**Target audience:** {{target-audience}}

**Your positioning:** {{personal-positioning}}

**Long-form content to repurpose:**
{{content}}

## Output
Return 5 tweet options separated by `---` (no numbered list). Format each tweet with blank lines between idea blocks.

**Example structure:**

You will be surprised how many people want:

● to share their experience on a user interview
● roast your landing page
● try your product in exchange for a testimonial

It's a win-win for everyone.

You get insights. People get attention.

You just need to ask them.

---

[next tweet]
```

## 用法 / Usage
- 必填變數 / Variables: {{content}}、{{personal-positioning}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Long-Form Content to Tweet Repurposing Prompt is a free AI prompt that transforms articles, essays, and bl…

# News Brief Generator for Complex Topics

## 簡介

The News Brief Generator for Complex Topics is a free AI prompt that transforms dense, complicated subjects into concise, accessible news summaries tailored to specific audiences. This news brief prompt for ChatGPT guides the model to produce journalist-quality briefs of 100-150 words, complete with punchy headlines (under 15 words), a lead sentence answering the 5 Ws, three bulleted key points, and a "Why This Matters" section that connects the story to reader concerns. It uses dependency grammar principles to structure sentences around core verbs and noun phrases, ensuring relationships between ideas are immediately clear. The prompt works across ChatGPT, Claude, Gemini, and Grok, making it ideal for communications teams, content marketers, internal newsletters, and anyone who needs to report on technical or policy developments without overwhelming readers. ● Outputs headline, lead, three key points, relevance statement, and related resources in a consistent format ● Applies dependency grammar techniques to maximize clarity and readability ● Adapts tone and detail level to match the specified target audience ● Includes placeholders for reputable sources, encouraging fact-checked, credible briefs ## Prompt

```
## Role
You are an expert journalist who creates concise, accessible news briefs on complex topics.

## Task
Write a 100-150 word news brief that distills complex information into a clear, engaging summary for the specified audience.

## Context
**Topic:** {{topic}}
**Target audience:** {{target-audience}}

Structure your brief using dependency grammar principles—organize sentences around核心 verbs and noun phrases that make relationships between ideas immediately clear.

## Output
Deliver the brief in this format:

**Headline:** [Under 15 words capturing the essence]

**Lead:** [One sentence answering Who, What, When, Where, Why]

**Key Points:**
- [Critical aspect 1 with detail]
- [Critical aspect 2 with detail]
- [Critical aspect 3 with detail]

**Why This Matters:** [1-2 sentences on relevance and impact for your target audience]

**Related Resources:**
- [Reputable source for further reading]
- [Additional context resource]

Avoid jargon unless essential to the audience. Prioritize clarity and relevance.
```

## 用法 / Usage
- 必填變數 / Variables: {{target-audience}}、{{topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The News Brief Generator for Complex Topics is a free AI prompt that transforms dense, complicated subjects in…

# LinkedIn Ad Copy Generator Prompt

## 簡介

The LinkedIn Ad Copy Generator Prompt is a free AI prompt that creates professionally formatted ad variations for LinkedIn campaigns targeting B2B and professional audiences. This LinkedIn ad copy prompt for ChatGPT produces three complete ad variations in a single run, each containing a headline (150 characters or fewer), body text (600 characters or fewer), and a call-to-action that respects LinkedIn's format restrictions. It applies dependency grammar principles to build clear, logical copy where each sentence element reinforces the next, ensuring your message communicates value quickly and drives clicks. Runs on ChatGPT, Claude, Gemini, and Grok. Use it when you need multiple ad tests for A/B campaigns, want to maintain a consistent brand voice across variations, or need to launch LinkedIn Sponsored Content quickly without sacrificing persuasive structure. ● Produces three complete ad sets with headlines, body copy, and CTAs in one request ● Applies dependency grammar to ensure clarity and logical flow in every line ● Respects LinkedIn's character limits and professional platform conventions ● Customizes tone and messaging using your product details, audience, USP, and brand voice ## Prompt

```
## Role
You are an expert LinkedIn advertising copywriter.

## Task
Generate three high-performing LinkedIn ad variations that promote the product or service, attract the target audience, and drive clicks. Each ad must include a headline (≤150 characters), body text (≤600 characters), and call-to-action.

## Context
**Product/Service**: {{product-service}}

**Target Audience**: {{target-audience}}

**Unique Selling Proposition**: {{usp}}

**Brand Voice**: {{brand-voice}}

**Call-to-Action**: {{cta}}

Use dependency grammar principles to create clear, impactful copy where each element builds logically on the previous. Write headlines that stop the scroll, body text that communicates value quickly, and CTAs that create urgency. Follow LinkedIn's ad format restrictions and professional platform conventions.

## Output
Provide your response as a markdown table:

| Headline | Body Text | Call-to-Action |
|----------|-----------|----------------|
| ...      | ...       | ...            |
| ...      | ...       | ...            |
| ...      | ...       | ...            |
```

## 用法 / Usage
- 必填變數 / Variables: {{brand-voice}}、{{cta}}、{{product-service}}、{{target-audience}}、{{usp}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The LinkedIn Ad Copy Generator Prompt is a free AI prompt that creates professionally formatted ad variations …

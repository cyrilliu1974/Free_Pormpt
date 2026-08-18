# Brand Consistency Audit Prompt for Multi-Platform Content

## 簡介

The Brand Consistency Audit Prompt for Multi-Platform Content is a free AI prompt that evaluates your content samples across channels to identify alignment gaps and strengthen brand cohesion for marketers, content teams, and brand managers. This brand consistency prompt for ChatGPT examines tone, voice, stylistic choices, and messaging against your brand guidelines, then outputs a structured markdown table rating each content element as Strong, Moderate, Weak, or Inconsistent. It highlights discrepancies in vocabulary, sentence structure, formatting, and emphasis on key brand points, while respecting platform-specific adaptations. The prompt concludes with a summary paragraph that prioritizes the most critical gaps and recommends concrete actions to unify your brand presence. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible for teams working in any text-generation environment. Use this prompt when launching a rebrand, onboarding new writers, preparing for a content audit, or ensuring consistency across social media, email, web, and advertising copy. ● Compares real content samples against your brand guidelines and target audience expectations ● Delivers a consistency rating and observations for each piece of content in a scannable table format ● Identifies where platform adaptation has diluted brand identity or messaging clarity ● Provides a prioritized action summary so teams know exactly what to fix first ## Prompt

```
## Role
You are an expert content strategist specializing in brand consistency audits.

## Task
Analyze the provided content across multiple platforms to ensure unified brand voice, tone, style, and messaging. Identify areas of strong alignment and discrepancies that weaken brand cohesion.

## Context
**Content to review:** {{content-samples}}

**Brand voice & messaging:** {{brand-guidelines}}

**Target audience:** {{target-audience}}

**Distribution platforms:** {{platforms}}

## Analysis Approach
Examine each content piece for:
- Tone and voice consistency with brand guidelines
- Stylistic alignment (vocabulary, sentence structure, formatting)
- Message coherence and emphasis on key brand points
- Platform-appropriate adaptation without diluting brand identity

## Output
Deliver your assessment as a markdown table with these columns:

| Content Element | Consistency Rating | Observations | Recommendations |
|-----------------|-------------------|--------------|------------------|

**Consistency Rating scale:** Strong / Moderate / Weak / Inconsistent

Include a summary paragraph after the table highlighting the most critical gaps and prioritized actions to strengthen brand consistency.
```

## 用法 / Usage
- 必填變數 / Variables: {{brand-guidelines}}、{{content-samples}}、{{platforms}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Brand Consistency Audit Prompt for Multi-Platform Content is a free AI prompt that evaluates your content …

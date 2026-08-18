# Style Guide Compliance Checker and Content Rewriter

## 簡介

The Style Guide Compliance Checker and Content Rewriter is a free AI prompt that rewrites existing content to match your company's brand voice and style standards while maintaining the original intent. This style guide compliance prompt for ChatGPT works by taking three inputs: your style guide parameters (tone, voice, terminology, formatting rules), the content that needs revision, and strategic business context (audience, industry, messaging goals). It runs on ChatGPT, Claude, Gemini, and Grok to produce a fully rewritten version alongside a detailed alignment summary that documents every change made to tone, terminology, formatting, messaging, and brand consistency. Use it to standardize blog posts, marketing copy, internal documentation, or any written material that must reflect your brand guidelines. This prompt is built for content strategists, brand managers, editors, and marketing teams who need to enforce style consistency across diverse contributors or retrofit existing content to updated guidelines. ● Preserves the original message and intent while applying tone, voice, and terminology standards from your style guide ● Produces a full rewritten version with clear headings that match your original structure ● Delivers a detailed alignment summary that explains tone adjustments, terminology updates, formatting corrections, and messaging refinements ● Works across content types including marketing copy, blog posts, documentation, emails, and internal communications ## Prompt

```
## Role
You are an expert content strategist specializing in brand voice consistency and style guide application.

## Task
Rewrite the provided content to align with the company's style guide while preserving the original message and intent. Ensure consistent branding, messaging, tone, voice, terminology, and formatting throughout.

## Context
**Style Guide & Brand Parameters:**
{{style-guide}}
(Include: tone, voice, terminology preferences, formatting rules, prohibited words, capitalization standards, and any visual/structural guidelines)

**Content to Rewrite:**
{{original-content}}
(Paste the full text that needs to be aligned with the style guide)

**Strategic Context:**
{{business-context}}
(Include: target audience, industry, content type/channel, key messaging points, and any specific brand positioning requirements)

## Output
Provide your rewritten content using this structure:

### Rewritten Content
[Full rewritten version organized with clear headings matching the original structure]

### Style Guide Alignment Summary
- **Tone & Voice Changes:** [Specific adjustments made]
- **Terminology Updates:** [Terms replaced or standardized]
- **Formatting Corrections:** [Structural or visual changes]
- **Messaging Refinements:** [How key points were strengthened or clarified]
- **Brand Consistency Improvements:** [Other alignment actions taken]
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{original-content}}、{{style-guide}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Style Guide Compliance Checker and Content Rewriter is a free AI prompt that rewrites existing content to …

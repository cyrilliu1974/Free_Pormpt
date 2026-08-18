# Content Style Guide Builder Prompt

## 簡介

The Content Style Guide Builder Prompt is a free AI prompt that creates detailed, actionable style guides for organizations seeking consistent brand voice and content quality across all channels. This content style guide prompt for ChatGPT produces a three-column markdown table covering Voice and Tone, Grammar and Punctuation, and Formatting Guidelines. It analyzes your brand personality, target audience, and primary content channels to deliver specific, practical rules that content creators can apply immediately. The prompt works on ChatGPT, Claude, Gemini, and Grok, translating abstract brand attributes into concrete editorial decisions. Use it to define how your organization should sound in different contexts, establish grammar conventions like serial comma usage and numeral rules, and set formatting standards for headers, lists, emphasis, and visual hierarchy. This prompt is for content strategists, marketing teams, and organizations that need to align multiple writers, maintain brand consistency, or onboard new content creators with clear editorial standards. ● Produces a structured markdown table with specific rules in three key categories: voice/tone, grammar/punctuation, and formatting ● Analyzes brand personality and translates abstract attributes into concrete writing decisions that eliminate ambiguity ● Includes context-specific guidance for different content types and situations, not just one-size-fits-all rules ● Generates guidelines precise enough that multiple writers will make identical editorial choices when applying them ## Prompt

```
## Role
You are an expert content strategist specializing in building Content Style Guides that ensure consistency and quality across all organizational content.

## Task
Create a comprehensive Content Style Guide structured as a markdown table with three columns: **Voice and Tone**, **Grammar and Punctuation**, and **Formatting Guidelines**. Provide detailed, actionable guidance in each category that content creators can immediately apply.

## Context
Company: {{company-name}}
Target audience: {{target-audience}}
Primary content channels: {{content-channels}}
Brand personality: {{brand-personality}}

Analyze how the brand personality should translate into voice and tone across different contexts. Consider audience expectations and channel-specific requirements. Define grammar standards, punctuation conventions, and formatting rules that reinforce brand consistency.

## Output
Deliver the Style Guide as a markdown table with three columns. Each cell should contain specific, clear guidelines:

- **Voice and Tone**: How the brand sounds (formal/casual, expert/friendly, etc.), with examples for different content types and situations
- **Grammar and Punctuation**: Specific rules on capitalization, serial commas, contractions, numerals, abbreviations, and common style decisions
- **Formatting Guidelines**: Headers, lists, emphasis (bold/italics), link styles, whitespace, paragraph length, and visual hierarchy standards

Make every guideline concrete enough that two writers would make the same choice when applying it.
```

## 用法 / Usage
- 必填變數 / Variables: {{brand-personality}}、{{company-name}}、{{content-channels}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Content Style Guide Builder Prompt is a free AI prompt that creates detailed, actionable style guides for …

# SEO Image Alt Text Optimizer for Accessibility

## 簡介

The SEO Image Alt Text Optimizer for Accessibility is a free AI prompt that generates descriptive, keyword-optimized ALT text for website images while meeting accessibility standards for screen readers. This image alt text prompt for ChatGPT analyzes visual content, identifies key elements relevant to your page topic, and naturally incorporates your target keywords into concise descriptions of 125 characters or fewer. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing a markdown table that pairs each image filename with optimized ALT text that serves both search engines and visually impaired users. Use it when auditing existing site images, launching new visual content, or building accessibility compliance into your workflow. ● Analyzes image content and identifies key visual elements relevant to page context and user intent ● Incorporates target keywords naturally only where they accurately describe the actual image ● Enforces the 125-character best practice for ALT text length while maximizing descriptive value ● Outputs a clean markdown table format pairing filenames with optimized ALT text ready for implementation ## Prompt

```
## Role
You are an expert SEO image optimizer specializing in accessibility and search visibility.

## Task
Create descriptive, keyword-rich ALT text for images that improves searchability and meets accessibility standards.

## Context
Website niche: {{website-niche}}
Target keywords: {{target-keywords}}
Primary audience: {{primary-audience}}

For each image:
1. Analyze the visual content and identify key elements
2. Consider relevance to the page topic and user intent
3. Incorporate target keywords naturally where they fit the actual image content
4. Write concise ALT text (typically 125 characters or fewer) that accurately describes what the image shows
5. Ensure the description is useful for screen readers and search engines alike

## Output
Provide a markdown table with two columns:

| Image Name | ALT Text |
|------------|----------|
| [filename] | [optimized description] |
```

## 用法 / Usage
- 必填變數 / Variables: {{primary-audience}}、{{target-keywords}}、{{website-niche}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SEO Image Alt Text Optimizer for Accessibility is a free AI prompt that generates descriptive, keyword-opt…

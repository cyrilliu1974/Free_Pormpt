# SEO Blog Post Generator for ChatGPT

## 簡介

The SEO Blog Post Generator for ChatGPT is a free AI prompt that produces complete, search-optimized blog articles with natural language and strategic keyword integration for content creators and marketers. This SEO blog post prompt for ChatGPT takes your topic, target audience, and primary keyword and generates a full-length article with H1/H2/H3 structure, meta description under 155 characters, table of contents, FAQ section, and conclusion with actionable next steps. It runs on ChatGPT, Claude, Gemini, and Grok, placing your keyword naturally 4-6 times across title, headings, and body while maintaining conversational tone. The prompt returns structured JSON output showing word count, keyword frequency, and exact placement locations. Use it when you need blog content that ranks in search results without sounding robotic or stuffed with keywords. ● Structures posts with proven title formulas, scannable sections, and conversational FAQ headings that address reader questions directly. ● Integrates your primary keyword 4-6 times across strategic locations while keeping prose natural and avoiding keyword stuffing. ● Outputs valid JSON with the complete markdown-formatted post, meta description, word count, and a map of where keywords appear. ● Emphasizes short paragraphs, bullet points, varied sentence rhythm, and authentic voice over corporate jargon or AI-sounding phrases. ## Prompt

```
## Role

You are an expert content strategist who combines data-driven SEO technique with engaging storytelling. You understand search intent psychology, natural keyword integration, and how to craft blog posts that rank well while building genuine reader trust.

## Task

Write a complete, SEO-optimized blog post that sounds authentically human and delivers practical value to the target audience.

## Context

{{blog-topic}}

{{target-audience}}

Primary SEO keyword: {{primary-keyword}}

## Output Requirements

### Structure
- **Title (H1)**: Use a proven formula with magnet words (Ultimate, Complete, Essential, Proven, Secret) that promises a clear benefit
- **Meta description**: Compelling summary under 155 characters that drives clicks
- **Table of contents**: Scannable list of main sections
- **Body sections**: 3-6 H2 sections with H3 subsections as needed
- **FAQ section**: 4-6 conversational statement headings (not "Question:"/"Answer:" format)
- **Conclusion**: Concrete next steps, not generic summary

### SEO Integration
- Place {{primary-keyword}} naturally 4-6 times throughout (title, introduction, headings, body)
- Implement proper H1/H2/H3 hierarchy
- Match search intent precisely—deliver what the title promises

### Voice & Readability
- Write conversationally with contractions, varied sentence rhythm, and authentic personality
- Use extensive bullet points for scannability
- Keep paragraphs short (2-4 sentences)
- Avoid corporate jargon, AI-sounding phrases, and keyword stuffing
- Make it feel like expert advice shared naturally, not robotic content

### Format

Return valid JSON with no additional commentary:

```json
{
 "meta_description": "[under 155 characters]",
 "blog_post": "[full markdown-formatted post]",
 "word_count": [number],
 "keyword_mentions": [number],
 "keyword_locations": ["title", "intro", "H2 section 3", etc.]
}
```
```

## 用法 / Usage
- 必填變數 / Variables: {{blog-topic}}、{{primary-keyword}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The SEO Blog Post Generator for ChatGPT is a free AI prompt that produces complete, search-optimized blog arti…

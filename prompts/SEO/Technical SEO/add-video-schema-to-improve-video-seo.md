# Video Schema Markup Implementation Guide for SEO

## 簡介

The Video Schema Markup Implementation Guide for SEO is a free AI prompt that creates customized, step-by-step instructions for adding structured data to video content on any website. This video schema prompt for ChatGPT analyzes your current video setup, recommends the appropriate Schema.org types (VideoObject, Clip, or BroadcastEvent), and delivers annotated JSON-LD code examples with verification steps. It adjusts technical depth to match your SEO experience level and explains both implementation mechanics and the ranking signals each property influences. Real use cases include e-commerce sites adding product demo markup, publishers optimizing video articles for rich results, and content creators improving YouTube embed visibility. The prompt runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to make video content eligible for Google's video carousels, enhanced snippets, and Search Console video reports but want guidance tailored to your specific CMS and technical comfort level. ● Analyzes your existing video content structure and identifies gaps in current markup implementation ● Recommends the correct Schema.org video types based on your content format and publishing context ● Provides JSON-LD code with inline annotations explaining each property's SEO function and search eligibility requirements ● Includes verification steps using Google Rich Results Test and Search Console with troubleshooting guidance ● Explains ranking signals and discoverability improvements tied to each structured data element ## Prompt

```
## Role
You are an expert SEO specialist focused on technical video optimization and structured data implementation.

## Task
Create a step-by-step guide to implement Schema Markup for video content, tailored to the user's technical level and current SEO baseline. Analyze the existing video structure, recommend appropriate Schema types (VideoObject, Clip, or BroadcastEvent), provide implementation code, and explain verification methods.

## Context
{{website-and-video-context}}

## Output
Deliver a numbered guide with clear section headings:

1. **Current State Analysis** - assess the video content structure and existing markup
2. **Schema Selection** - identify which Schema.org video types fit the content
3. **Implementation Steps** - provide code examples with inline annotations explaining each property
4. **Verification & Testing** - list tools (Rich Results Test, Search Console) and what to check
5. **SEO Impact** - explain how each markup element improves discoverability, click-through rate, and ranking signals

Adjust technical depth and jargon to match the stated expertise level. For each step, explain *why* it matters for search visibility, not just *how* to do it.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-and-video-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Video Schema Markup Implementation Guide for SEO is a free AI prompt that creates customized, step-by-step…

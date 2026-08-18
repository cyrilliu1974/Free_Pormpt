# Schema Markup Implementation Guide for Local SEO

## 簡介

The Schema Markup Implementation Guide for Local SEO is a free AI prompt that generates a technical implementation roadmap for adding structured data to local business websites. This schema markup prompt for ChatGPT produces a dependency-sequenced guide covering the three core Schema types for local search: LocalBusiness, PostalAddress, and GeoCoordinates. For each type, the prompt explains the SEO impact before delivering properly formatted JSON-LD code snippets, HTML placement instructions, and validation steps using Google's Rich Results Test. It runs on ChatGPT, Claude, and Gemini, and is built for SEO specialists, web developers, and local business owners who need to structure metadata for map pack eligibility and rich snippet display. Reach for this prompt when you need to implement or audit local business structured data with clear rationale for each element and its contribution to ranking factors. ● Produces complete JSON-LD snippets for LocalBusiness, PostalAddress, and GeoCoordinates Schema types with proper syntax ● Explains the local search ranking impact and rich snippet eligibility of each Schema element before implementation ● Includes HTML placement instructions and Google Rich Results Test validation steps ● Uses dependency sequencing to teach foundational concepts, then implementation, validation, and optimization impact ## Prompt

```
## Role
You are an expert SEO specialist focused on technical local search optimization.

## Task
Create a step-by-step implementation guide for adding Schema Markup to improve local search visibility for {{business-details}}. Structure your explanation using clear dependencies: explain why each Schema type matters before showing how to implement it.

## Context
Schema Markup directly influences how search engines understand and display local business information in search results, affecting rankings, rich snippet eligibility, and click-through rates. Focus on the three core Schema types for local SEO: LocalBusiness (establishes entity type and core attributes), PostalAddress (provides location data for map packs and local queries), and GeoCoordinates (enables precise geographic targeting).

## Output
Deliver a numbered step-by-step guide that:

1. Explains the SEO impact and purpose of each Schema type before implementation
2. Provides complete, properly formatted JSON-LD code snippets for LocalBusiness, PostalAddress, and GeoCoordinates
3. Shows where to place the markup in the website HTML
4. Includes validation steps using Google's Rich Results Test
5. Describes how each element contributes to local search ranking factors, user experience improvements, and enhanced click-through rates in local packs

Format all code snippets with clear labels and syntax highlighting indicators. Use dependency sequencing: foundational concepts → implementation → validation → optimization impact.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Schema Markup Implementation Guide for Local SEO is a free AI prompt that generates a technical implementa…

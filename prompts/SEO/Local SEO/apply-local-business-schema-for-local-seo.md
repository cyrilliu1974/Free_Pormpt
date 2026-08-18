# Local Business Schema Implementation Guide Generator

## 簡介

The Local Business Schema Implementation Guide Generator is a free AI prompt that creates detailed, actionable guides for adding structured data markup to local business websites. This local business schema prompt for ChatGPT produces a comprehensive implementation guide that includes JSON-LD code examples customized to your specific business details, validation testing procedures, and optimization best practices. Simply provide your business information - name, address, phone, hours, and service type - and the prompt generates a step-by-step guide explaining why Local Business Schema matters, which properties to include (address structure, geo-coordinates, opening hours, business type), how to implement the markup correctly, and common errors that cause validation failures. It runs on ChatGPT, Claude, Gemini, and Grok. Use this prompt when you need to improve local search visibility, help search engines understand your business information, or enable rich snippets in local search results. ● Creates custom JSON-LD schema code using your specific business name, address, phone, coordinates, and operating hours ● Explains testing with Google Rich Results Test and Schema Markup Validator to ensure correct implementation ● Identifies common pitfalls like NAP inconsistencies, duplicate markup, and validation errors that harm rankings ● Provides structured output with clear headings, annotated code blocks, and actionable best practices for immediate deployment ## Prompt

```
## Role

You are an expert SEO specialist focused on local search optimization.

## Task

Provide a comprehensive implementation guide for Local Business Schema markup that will enhance visibility in local search results. Explain the importance, structure, and best practices of Local Business Schema, and include specific JSON-LD code examples, testing procedures, and common pitfalls to avoid.

## Context

Local Business Schema markup is structured data that helps search engines understand key business information and display it prominently in local search results. This guide should be practical and actionable for immediate implementation.

**Business Details:**
{{business-details}}

## Output

Structure your guide with:

- **Introduction**: Why Local Business Schema matters for local SEO
- **Schema Structure**: Core properties and optional enhancements
- **Implementation**: Step-by-step JSON-LD code example using the business details provided
- **Properties to Include**: Name, type, address (structured), phone, URL, opening hours, geo-coordinates, and relevant extensions
- **Testing & Validation**: Tools and methods to verify correct implementation (Google Rich Results Test, Schema Markup Validator)
- **Best Practices**: Accuracy requirements, consistency with NAP citations, avoiding duplicate markup
- **Common Pitfalls**: Errors that cause validation failures or penalties

Use clear headings, subheadings, and bullet points throughout. Present code examples in properly formatted blocks with explanatory annotations.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Local Business Schema Implementation Guide Generator is a free AI prompt that creates detailed, actionable…

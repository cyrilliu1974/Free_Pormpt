# Structured Data Implementation Tutorial Generator

## 簡介

The Structured Data Implementation Tutorial Generator is a free AI prompt that creates technical documentation for implementing Schema.org markup on websites. This structured data tutorial prompt for ChatGPT produces complete markdown guides that walk developers through marking up articles, products, reviews, and other content types with working code examples in JSON-LD, Microdata, or RDFa formats. It runs on ChatGPT, Claude, Gemini, and Grok, generating tutorials that cover Schema.org type selection, required properties, validation workflows, and technical SEO best practices. The output includes an introduction to structured data benefits, dedicated sections for each content type with production-ready code, testing instructions using Google's Rich Results Test, and a best-practices checklist. Reach for this prompt when you need to document structured data implementation for a specific website or train team members on Schema.org markup techniques. ● Generates markdown tutorials covering Schema.org type selection, key properties, and complete working code examples for articles, products, reviews, or custom content types ● Includes validation steps using Google's Rich Results Test and Schema Markup Validator to ensure markup meets search engine requirements ● Provides best-practice sections on choosing the most specific Schema type, maintaining accuracy, and staying current with Schema.org updates ● Outputs production-ready JSON-LD, Microdata, or RDFa code blocks formatted for immediate implementation on live websites ## Prompt

```
## Role

You are an expert web developer specializing in structured data, Schema.org markup, and technical SEO.

## Task

Create a comprehensive tutorial on implementing Schema.org structured data for {{content-types}}. The tutorial should provide clear, step-by-step instructions with working code examples that demonstrate proper markup techniques.

## Context

Website: {{website-url}}

Structured data helps search engines understand content more accurately, improving visibility in search results and enabling rich snippets. The tutorial will guide readers through practical implementation, testing, and validation.

## Output

Format the tutorial in markdown with the following structure:

### Introduction
- Overview of structured data and its SEO/UX benefits
- Role of Schema.org in standardizing markup

### Implementation Sections

For each content type in {{content-types}}, provide:

1. **Key elements** to mark up (e.g., for articles: headline, author, datePublished, image; for products: name, price, availability, aggregateRating; for reviews: reviewer, rating, reviewBody)
2. **Appropriate Schema.org types** (Article/NewsArticle/BlogPosting, Product/Offer, Review/Rating, etc.)
3. **Complete code example** using JSON-LD, Microdata, or RDFa as appropriate
4. **Testing and validation** steps using Google's Rich Results Test or Schema Markup Validator

### Best Practices
- Maintain consistency and accuracy across all markup
- Use the most specific Schema.org type available
- Include all required properties and recommended optional properties
- Test markup before deployment
- Resources for staying current with Schema.org updates

### Conclusion
- Summary of implementation steps
- Encouragement to adopt structured data
- Links to official Schema.org documentation and community resources

Use clear headings, numbered lists, bullet points, and properly formatted code blocks. Ensure all examples are production-ready and follow current Schema.org specifications.
```

## 用法 / Usage
- 必填變數 / Variables: {{content-types}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Structured Data Implementation Tutorial Generator is a free AI prompt that creates technical documentation…

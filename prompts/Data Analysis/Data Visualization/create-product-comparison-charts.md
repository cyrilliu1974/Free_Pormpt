# Product Comparison Chart Generator

## 簡介

The Product Comparison Chart Generator is a free AI prompt that builds side-by-side markdown tables comparing features, pricing, and benefits across products in any category. This product comparison prompt for ChatGPT guides the model to research leading options in your specified category, identify the most decision-relevant attributes, and organize everything into a scannable table with custom columns. It works on ChatGPT, Claude, Gemini, and Grok, producing markdown tables that help buyers evaluate alternatives quickly. Teams building buying guides, e-commerce content, or internal vendor assessments use it to standardize how they present competitive information. You control the product category, target audience, comparison focus, number of columns, and column names, so the output matches your editorial or business needs. Reach for this prompt when you need to transform scattered product research into a clean, apples-to-apples table that readers can scan in seconds. ● Accepts flexible inputs for product category, audience, comparison focus, column count, and column names ● Outputs well-structured markdown tables that render cleanly in documentation, CMS platforms, and reports ● Ensures consistency in language, formatting, and depth across every row in the table ● Includes instructions for verifying accuracy and adding context valuable to potential buyers ## Prompt

```
## Role
You are an expert product analyst creating comprehensive comparison charts that help buyers make informed decisions.

## Task
Develop a clear, informative product comparison chart in markdown table format for {{product-category}}. The chart should highlight key features, benefits, and pricing across the specified products.

## Context
Target audience: {{target-audience}}
Comparison focus: {{comparison-focus}}

## Process
1. Research and gather detailed information about leading products in the category
2. Identify the most important features, benefits, and pricing points for comparison
3. Organize information into a structured table with {{number-of-columns}} columns: {{column-names}}
4. Use clear, concise language to describe each product aspect
5. Ensure consistency in formatting and presentation across all products
6. Verify all information for accuracy and completeness
7. Include additional relevant information valuable for potential buyers

## Output
Present your comparison as a markdown table that is well-organized, easy to read, and visually scannable. Ensure the table structure uses the specified columns and presents information in a way that facilitates quick comparison across products.
```

## 用法 / Usage
- 必填變數 / Variables: {{column-names}}、{{comparison-focus}}、{{number-of-columns}}、{{product-category}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Product Comparison Chart Generator is a free AI prompt that builds side-by-side markdown tables comparing …

# Recipe Schema Markup Generator for SEO

## 簡介

The Recipe Schema Markup Generator for SEO is a free AI prompt that creates properly structured JSON-LD Recipe Schema for food bloggers and recipe sites looking to improve search visibility. This recipe schema prompt for ChatGPT analyzes your recipe content and produces compliant JSON-LD markup that meets schema.org Recipe specifications and Google's rich results requirements. It identifies ingredients, cooking instructions, prep time, nutritional information, and other key elements, then structures them with clear hierarchical relationships - tying ingredients to specific steps and showing how prep time contributes to total time. The prompt runs on ChatGPT, Claude, and Gemini, and outputs code-formatted markup with inline comments explaining each section. Recipe bloggers use it to enable rich snippets in Google search, improve click-through rates, and make recipes more discoverable to home cooks searching for specific dishes or cooking techniques. ● Outputs complete JSON-LD syntax with all required Recipe Schema properties ● Maps ingredients to instruction steps and calculates total time from prep and cook durations ● Includes inline comments documenting each schema section for easy customization ● Ensures compliance with current schema.org standards and Google's rich result guidelines ## Prompt

```
## Role
You are an SEO specialist and schema markup developer implementing Recipe Schema for a recipe blog.

## Task
Create comprehensive, properly structured Recipe Schema markup in JSON-LD format that complies with schema.org standards and Google's rich results guidelines. Analyze the recipe content to identify ingredients, instructions, cooking time, nutritional information, and other key elements, then craft markup that accurately represents the recipe's hierarchical structure and element relationships.

## Context
Recipe blog: {{blog-name}}
Recipe details: {{recipe-details}}
Target audience: {{target-audience}}

The schema markup must enhance search engine visibility and enable rich results in Google search. Structure the markup to clearly show dependencies and relationships between recipe components (e.g., ingredients tied to specific instruction steps, prep time contributing to total time).

## Output
Deliver the schema markup as:
- JSON-LD syntax in a code block
- Inline comments explaining each major section
- Full compliance with current schema.org Recipe specifications
- Hierarchical structure reflecting logical dependencies between elements
```

## 用法 / Usage
- 必填變數 / Variables: {{blog-name}}、{{recipe-details}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Recipe Schema Markup Generator for SEO is a free AI prompt that creates properly structured JSON-LD Recipe…

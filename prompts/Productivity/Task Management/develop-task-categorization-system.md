# Task Categorization System Builder

## 簡介

The Task Categorization System Builder is a free AI prompt that creates custom task management frameworks for businesses seeking to organize their daily operations. This task categorization prompt for ChatGPT guides the AI to act as a categorization specialist, analyzing your business type and operational needs to generate a complete system of main task categories. Each category includes a descriptive name, clear scope definition, and representative example tasks common to your industry. The system is designed to be mutually exclusive and collectively exhaustive, covering all major task areas without creating unnecessary complexity. It works on ChatGPT, Claude, Gemini, and Grok, adapting to different business contexts - from startups needing lean workflows to enterprises managing complex operations. This prompt is ideal for business owners, operations managers, and productivity consultants who need to impose structure on chaotic task lists or standardize workflows across teams. ● Generates customized category structures based on your business type, desired number of categories, and operational priorities ● Provides concrete example tasks for each category so teams immediately understand where activities belong ● Creates mutually exclusive categories that eliminate overlap and confusion in task assignment ● Adapts to any business context by analyzing specific operational needs in the input variable ## Prompt

```
## Role
You are a categorization specialist who designs task management systems for businesses.

## Task
Create a structured system for categorizing common business tasks into main categories optimized for the user's specific business type.

## Context
Business context: {{business-type-and-needs}}
(Include: business type, desired number of main categories, any specific operational priorities)

## Output
Provide the categorization system in this format:

**[Business Type]**

Number of Main Categories: [Number]

**Category 1:**
Name: [Category Name]
Description: [Brief description of what task types this encompasses]
Example Tasks:
- [Common task 1]
- [Common task 2]
- [Common task 3]

**Category 2:**
Name: [Category Name]
Description: [Brief description]
Example Tasks:
- [Common task 1]
- [Common task 2]
- [Common task 3]

[Continue for all categories]

**Requirements:**
- Each category must have a clear, descriptive name
- Example tasks should be common, representative activities for that business type
- Keep the system comprehensive yet concise—cover major task areas without creating category overload
- Ensure categories are mutually exclusive and collectively exhaustive for the business type
```

## 用法 / Usage
- 必填變數 / Variables: {{business-type-and-needs}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Task Categorization System Builder is a free AI prompt that creates custom task management frameworks for …

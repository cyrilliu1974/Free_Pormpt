# FAQ Document Generator for Products and Services

## 簡介

The FAQ Document Generator for Products and Services is a free AI prompt that creates complete, organized FAQ documentation for any product or service. This FAQ prompt for ChatGPT produces structured help documentation that includes an introduction, table of contents, topical question sections, troubleshooting guides, and resource links. It runs on ChatGPT, Claude, Gemini, and Grok, transforming your product description, target audience, and key features into a navigable FAQ document with clear answers, step-by-step problem-solving instructions, and practical examples. Technical writers, customer support teams, and product managers use it to build help center content that anticipates user questions and provides actionable solutions without technical jargon. ● Organizes FAQs into 3-5 topical sections with table of contents for easy user navigation ● Generates question-answer pairs grouped by categories like Getting Started, Features, Account Management, and Billing ● Includes 5-8 common troubleshooting scenarios with step-by-step solutions and fallback instructions ● Provides Additional Resources section with support contact information and related documentation links ## Prompt

```
## Role
You are a technical writer creating a comprehensive FAQ document that helps users understand and troubleshoot a product or service.

## Task
Develop a complete FAQ document with clear organization, practical answers, and troubleshooting guidance. Address the questions users commonly ask, anticipate their needs, and provide step-by-step solutions to typical problems.

## Context
Product/Service: {{product-service-description}}

Target Audience: {{target-audience}}

Key Features: {{key-features}}

## Output
Structure the FAQ document with these components:

### Introduction
- Brief overview of the product/service
- Purpose of this FAQ
- How to navigate and use this document effectively

### Table of Contents
Organize into 3-5 main topical sections with subsections for easy navigation

### Main FAQ Sections
Group questions by topic (e.g., Getting Started, Features & Functionality, Account Management, Billing). Within each section:
- Use clear question-and-answer format
- Provide detailed, jargon-free answers
- Include practical examples where helpful
- Cover 2-4 questions per subsection

### Troubleshooting
Address 5-8 common problems with:
- Clear problem statement
- Step-by-step solutions
- What to do if the solution doesn't work

### Additional Resources
- Links to related documentation, videos, or tutorials
- Contact information for support (email, chat, phone as applicable)
- Community forums or knowledge base links if available

Use markdown formatting with appropriate headings (##, ###) and lists for readability. Keep language clear and accessible to {{target-audience}}.
```

## 用法 / Usage
- 必填變數 / Variables: {{key-features}}、{{product-service-description}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The FAQ Document Generator for Products and Services is a free AI prompt that creates complete, organized FAQ …

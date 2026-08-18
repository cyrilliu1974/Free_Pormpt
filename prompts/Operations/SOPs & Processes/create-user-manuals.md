# User Manual Generator Prompt for Products and Services

## 簡介

The User Manual Generator Prompt for Products and Services is a free AI prompt that produces complete, structured user manuals for any product or service. This user manual prompt for ChatGPT works by taking your product or service name and generating a full documentation package: a product overview, target audience section, prerequisites list, numbered step-by-step procedures with image descriptions, troubleshooting guide, FAQ section, and additional resources. It runs on ChatGPT, Claude, Gemini, and Grok, and outputs plain-language documentation designed for users with varying technical expertise. Product teams, support managers, SaaS companies, and technical writers use it to create onboarding guides, how-to documentation, and customer-facing manuals that reduce support tickets and accelerate user adoption. Reach for this prompt when you need to document a complex workflow, launch a new feature, or turn tribal knowledge into repeatable instructions without hiring a technical writer. ● Breaks every procedure into discrete, numbered steps with descriptive headings for clarity ● Anticipates common user pain points and addresses them proactively in troubleshooting and FAQ sections ● Prompts for image descriptions wherever a diagram or screenshot would aid comprehension ● Outputs a complete manual structure: overview, prerequisites, step-by-step guide, troubleshooting, FAQ, and resources ## Prompt

```
## Role

You write clear, thorough user manuals and how-to guides for complex products and services. Your output is structured, practical, and accessible to users with varying levels of technical expertise.

## Context

Product or service: {{product-or-service}}

## Task

Produce a complete user manual for the product or service above. Follow the structure and requirements below exactly.

**Requirements:**
- Use plain, jargon-free language; define any technical terms on first use
- Break every process into discrete, numbered steps
- Anticipate common user questions and pain points; address them proactively
- Include visual prompts (image descriptions) where a diagram or screenshot would help
- Keep the manual well-structured and easy to navigate

## Output

Deliver a complete user manual with the following sections:

**Product or Service Overview** — Brief description of what it is, what it does, and key benefits.

**Target Audience** — Who this manual is for and what skill level is assumed.

**Prerequisites** — What users need before starting (hardware, software, accounts, permissions, prior knowledge).

**Step-by-Step Guide** — Core procedures broken into numbered steps with descriptive headings. Include image descriptions where visual aids would clarify (e.g., "Screenshot: the Settings menu with the 'Advanced' tab highlighted").

**Troubleshooting** — 3–5 common issues with their symptoms and solutions.

**FAQ** — 3–5 frequently asked questions with concise answers.

**Additional Resources** — Links to support channels, related documentation, or community forums.
```

## 用法 / Usage
- 必填變數 / Variables: {{product-or-service}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The User Manual Generator Prompt for Products and Services is a free AI prompt that produces complete, structu…

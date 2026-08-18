# Investment Terminology Explainer Prompt

## 簡介

The Investment Terminology Explainer Prompt is a free AI prompt that translates complex Wall Street jargon into plain English for everyday investors and learners. It delivers three-part explanations for any investment term: a jargon-free definition, a real-world scenario showing how the concept applies in actual investing, and an everyday analogy that connects finance to familiar experiences. This investment terminology prompt for ChatGPT, Claude, Gemini, and Grok is built for learners with zero finance background, making it ideal for self-study, onboarding new investors, or preparing educational content. Reach for it when you need technically accurate explanations that remain fully accessible, whether you are clarifying a single concept or building a custom glossary of terms. ● Accepts a learner profile variable to tailor explanations to the user's background and goals. ● Structures each term with a definition, practical example, and analogy for progressive understanding. ● Outputs single-term explanations as flowing paragraphs or multi-term responses as scannable glossaries. ● Ensures technical accuracy while eliminating jargon, making finance education accessible to absolute beginners. ## Prompt

```
## Role
You are a financial educator specializing in investment literacy. Your expertise lies in translating Wall Street terminology into plain English that everyday investors can immediately understand and apply.

## Task
The user will provide one or more investment terms they want to understand. For each term, deliver a three-part explanation:

1. **Definition** – A jargon-free explanation that captures the core concept
2. **Real-world example** – A practical scenario showing how the term applies in actual investing
3. **Everyday analogy** – A comparison to familiar experiences that cements understanding

Build each explanation progressively so someone with zero investment background can follow along.

## Context
{{learner-profile}}

## Output
**For a single term:** provide the three-part explanation in flowing paragraphs.

**For multiple terms:** format as a glossary with each term as a bullet point or numbered entry. Clearly label or separate the definition, example, and analogy within each entry for easy scanning.

Ensure all explanations are technically accurate while remaining fully accessible.
```

## 用法 / Usage
- 必填變數 / Variables: {{learner-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Investment Terminology Explainer Prompt is a free AI prompt that translates complex Wall Street jargon int…

# Code Breakdown Explainer Prompt for ChatGPT

## 簡介

The Code Breakdown Explainer Prompt is a free AI prompt that transforms complex code into clear, logical explanations tailored to any experience level. Whether you're debugging unfamiliar legacy code, onboarding a junior developer, or teaching yourself a new programming pattern, this code explanation prompt for ChatGPT helps you understand what each line does, why it appears in that order, and how the pieces interconnect to produce the final result. This prompt runs on ChatGPT, Claude, and Gemini. It analyzes your code block and reader experience level, then produces a structured breakdown: a plain-language overview, numbered step-by-step explanations with inline definitions, a flow diagram showing data movement, a list of key programming concepts in use, and a summary that ties everything together. The approach mirrors Donald Knuth's literate programming philosophy - building understanding incrementally, one logical step at a time. Reach for this prompt when you inherit code you didn't write, need to document a function for your team, or want to deepen your grasp of a tricky algorithm. ● Explains every line in sequence, showing what it does, why it happens in that order, and how it depends on previous steps. ● Adapts explanation depth to the reader's experience - beginners get foundational context, advanced users get architectural trade-offs. ● Includes an ASCII flow diagram or written data-flow description so you can visualize how information moves through the code. ● Identifies key programming concepts (recursion, state management, closures) and defines jargon inline with real-world analogies. ## Prompt

```
## Role
You are a code explanation specialist who breaks down complex code into clear, logical steps that build upon each other.

## Task
Analyze the provided code and produce a complete, line-by-line explanation that makes the logic transparent.

**Before you begin**, identify: (1) the code's overall purpose, (2) its logical flow, (3) each component's role, (4) how pieces interconnect, (5) the cumulative effect.

## Context
**Code to explain:**
{{code-block}}

**Reader experience level:**
{{experience-level}}

## Output
Structure your explanation using these sections:

### Overview
State in plain language what the code accomplishes and why it exists.

### Step-by-Step Breakdown
Explain each line or logical section:
- **What** it does in simple terms
- **Why** it happens in that specific order
- **How** it builds toward the final result
- **Dependencies** on previous steps

Number each explanation. Never skip lines. When jargon is unavoidable, define it inline. Use analogies (cooking recipes, assembly instructions) to bridge understanding gaps.

### Flow Diagram
Provide an ASCII diagram or written description showing how data moves through the code.

### Key Concepts
Bullet list of important programming concepts used (loops, recursion, state management, etc.).

### Summary
Describe how all pieces work together to achieve the result. If errors or inefficiencies exist, note them constructively.

---

**Adapt explanation depth to the stated experience level.** Beginners need more foundational context; advanced users benefit from focus on architecture and trade-offs.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-block}}、{{experience-level}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Code Breakdown Explainer Prompt is a free AI prompt that transforms complex code into clear, logical expla…

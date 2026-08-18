# Manuscript Editor and Revision Prompt

## 簡介

The Manuscript Editor and Revision Prompt is a free AI prompt that guides systematic editing of manuscripts using dependency grammar principles for clarity, flow, and structural coherence. This manuscript revision prompt for ChatGPT applies an eight-stage editorial process - from initial assessment and syntax analysis to flow optimization and proofreading - producing actionable recommendations with before/after examples and specific rationale for each change. Writers, academic researchers, and professional editors use it to refine dissertations, journal articles, book chapters, and reports on ChatGPT, Claude, or Gemini by providing manuscript context, style guide requirements, and editorial focus areas. The prompt outputs structured feedback organized by revision stage, identifying structural weaknesses, ambiguous constructions, and inconsistencies while delivering concrete rewrites that improve sentence architecture and logical progression. ● Analyzes sentence structure using dependency grammar to identify ambiguity, complexity, and weaknesses ● Delivers actionable revisions organized by editorial stage - syntax, clarity, flow, style, technical precision, and proofreading ● Provides before/after examples and rationale for major structural changes to support learning and decision-making ● Adapts to manuscript type, audience, style guide, and specific editorial concerns through three customizable variables ## Prompt

```
## Role
You are an expert manuscript editor specializing in clarity, flow, and structural coherence. You apply dependency grammar principles to analyze and improve sentence architecture.

## Task
Revise the provided manuscript through a systematic editing process. Deliver actionable recommendations organized by revision stage, with specific rewrites and explanations for major changes.

## Context
Manuscript details:
- Type, audience, and field: {{manuscript-context}}
- Style guide and formatting requirements: {{style-guide}}
- Specific areas of concern or focus: {{editorial-focus}}

## Process
1. **Initial Assessment** – Read through to understand the core argument, structure, and intended message.
2. **Syntax Analysis** – Apply dependency grammar to identify structural weaknesses, ambiguous constructions, and overly complex sentences.
3. **Clarity Enhancement** – Revise unclear passages with attention to word choice, sentence structure, and logical connections.
4. **Flow Optimization** – Strengthen transitions within and between paragraphs; ensure ideas build logically.
5. **Style & Coherence Refinement** – Adjust tone, voice, and register to suit the audience; unify stylistic elements throughout.
6. **Technical Precision** – Verify consistency in terminology, citation format, heading hierarchy, and adherence to the specified style guide.
7. **Proofreading** – Correct grammar, spelling, punctuation, and typographical errors.
8. **Summary of Revisions** – Provide an overview of major changes with brief rationale for each.

## Output
Structure your response with clear headings for each process step. Under each heading, use bullet points to detail:
- Specific issues identified
- Proposed revisions or rewrites
- Reasoning behind recommendations

Include before/after examples for significant structural changes.
```

## 用法 / Usage
- 必填變數 / Variables: {{editorial-focus}}、{{manuscript-context}}、{{style-guide}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Manuscript Editor and Revision Prompt is a free AI prompt that guides systematic editing of manuscripts us…

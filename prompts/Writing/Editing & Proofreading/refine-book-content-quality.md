# Book Content Quality Review Prompt

## 簡介

The Book Content Quality Review Prompt is a free AI prompt that generates detailed editorial evaluations for authors, editors, and publishing professionals refining manuscript quality. This book editing prompt for ChatGPT walks through a four-dimensional review framework - clarity, coherence, consistency, and engagement - to assess how well manuscript sections align with a book's overarching theme, target audience, and narrative voice. You provide the content excerpt and a brief book overview (audience, theme, purpose), and the AI returns a structured evaluation report highlighting ambiguous passages, logical flow gaps, tonal inconsistencies, and opportunities to strengthen reader engagement, complete with actionable revision recommendations and concrete rephrasing examples. It runs on ChatGPT, Claude, Gemini, and Grok. Use it when you need a systematic editorial review during manuscript development, before sending a draft to beta readers, or when preparing content for a developmental or line editor. ● Evaluates clarity, coherence, consistency, and engagement across four distinct analytical dimensions ● Identifies specific problematic sections with explanations and concrete rephrasing examples ● Assesses alignment with target audience expectations, overarching theme, and intended message ● Highlights strengths to preserve, including effective language, storytelling techniques, and impactful passages ## Prompt

```
## Role
You are an expert proofreading specialist with deep expertise in narrative coherence, stylistic consistency, and content clarity.

## Task
Evaluate and refine the specified book content to ensure it effectively communicates its intended message, resonates with the target audience, and maintains cohesive, engaging narrative flow. Focus on enhancing integration with the book's overarching theme while ensuring consistency in voice, tone, and style.

## Context
**Book content to review:** {{content-to-review}}

**Book overview:** {{book-overview}}
(Include: target audience, overarching theme, intended message or purpose)

## Output
Provide a comprehensive evaluation report structured as follows:

### General Assessment
Evaluate the content's alignment with the book's overall theme, target audience expectations, and narrative flow. Note initial impressions of strengths and improvement areas.

### Detailed Analysis
Analyze across four dimensions:

- **Clarity:** Identify ambiguous or unnecessarily complex ideas that need clearer, more concise expression
- **Coherence:** Examine logical flow between sentences and paragraphs; flag where narrative progression could be smoother
- **Consistency:** Verify voice, tone, and style align with the book's overall narrative; note any jarring discrepancies
- **Engagement:** Assess reader interest capture and retention; identify opportunities for stronger hooks, vivid descriptions, relatable examples, or compelling questions

### Specific Revisions Needed
For each issue identified, provide:
- The problematic section or pattern
- Clear explanation of why it needs adjustment
- Actionable recommendation with concrete rephrasing examples where applicable

### Strengths to Preserve
Highlight effective elements that should be maintained or emphasized: strong language use, successful storytelling techniques, impactful passages, and features that enhance reader connection.
```

## 用法 / Usage
- 必填變數 / Variables: {{book-overview}}、{{content-to-review}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Book Content Quality Review Prompt is a free AI prompt that generates detailed editorial evaluations for a…

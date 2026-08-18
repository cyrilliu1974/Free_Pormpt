# Draft Editing and Revision Prompt

## 簡介

The Draft Editing and Revision Prompt is a free AI prompt that applies dependency grammar analysis to systematically edit and improve written drafts for any audience or purpose. This draft editing prompt for ChatGPT works by evaluating your text through ten editorial lenses, from overall structure and logical flow to sentence-level syntax and word choice precision. It runs on ChatGPT, Claude, and Gemini, producing an executive summary, sentence-by-sentence edits with before-and-after examples, style recommendations, and a revised draft or key excerpts. Writers use it to polish blog posts, academic papers, business reports, marketing copy, and any document where clarity and coherence matter. Reach for this prompt when you need a second editorial eye that applies linguistic rigor, not just surface-level grammar checks, to identify structural weaknesses, vague phrasing, inconsistent tone, and gaps in argumentation. ● Analyzes head-dependent relationships in sentences to diagnose unclear or awkward constructions ● Provides before-and-after examples so you see exactly what changed and why ● Evaluates ten dimensions from structure and flow to tone consistency and content gaps ● Outputs an executive summary, detailed edits, and a revised draft ready for publication ## Prompt

```
## Role
You are an expert editor and writing consultant specializing in dependency grammar analysis.

## Task
Revise and edit the provided draft to improve clarity, coherence, and overall effectiveness. Apply dependency grammar principles to analyze and strengthen sentence structure, word choice, and logical flow.

## Context
**Draft type:** {{draft-type}}
**Target audience:** {{target-audience}}
**Writing purpose:** {{writing-purpose}}
**Tone:** {{desired-tone}}
**Specific concerns:** {{specific-concerns}}

## Analysis Framework
Evaluate the draft systematically:

1. **Structure & Organization** – Assess overall architecture and section arrangement
2. **Coherence & Flow** – Evaluate logical progression and idea development
3. **Sentence Architecture** – Apply dependency grammar to examine head-dependent relationships and syntactic dependencies
4. **Grammar & Syntax** – Identify and correct errors
5. **Clarity** – Simplify complex constructions; elaborate vague concepts
6. **Precision** – Improve word choice for accuracy and impact
7. **Consistency** – Ensure uniform tone and style
8. **Transitions** – Strengthen connections between paragraphs and sections
9. **Argumentation** – Verify main points are clearly presented and well-supported
10. **Content Gaps** – Recommend additional material or examples where needed

## Output
Provide your analysis in a structured format with clear headings:

- **Executive Summary** – Overview of key findings
- **Structural Analysis** – Organization and flow assessment
- **Sentence-Level Edits** – Specific dependency grammar improvements with before/after examples
- **Style & Tone** – Consistency and voice recommendations
- **Content Recommendations** – Suggestions for additions or revisions
- **Revised Draft** (or key excerpts) – Implementation of major changes
```

## 用法 / Usage
- 必填變數 / Variables: {{desired-tone}}、{{draft-type}}、{{specific-concerns}}、{{target-audience}}、{{writing-purpose}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Draft Editing and Revision Prompt is a free AI prompt that applies dependency grammar analysis to systemat…

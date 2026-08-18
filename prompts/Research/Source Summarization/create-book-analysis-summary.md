# Book Analysis Summary Generator

## 簡介

The Book Analysis Summary Generator is a free AI prompt that produces structured, chapter-by-chapter reference guides for literary works. This book analysis prompt for ChatGPT asks the AI to act as an expert literary analyst and create a three-column table covering every chapter's summary, key plot points, character developments, and thematic elements. It runs on ChatGPT, Claude, Gemini, and Grok, transforming any book title into a concise, scannable markdown table that captures the core narrative arc without excessive detail. Students preparing for exams, educators designing curricula, book club facilitators, and avid readers tracking complex narratives use this prompt to distill novels, memoirs, and non-fiction works into quick-reference guides. ● Produces a markdown table with chapter number, 2-3 sentence synopsis, and 2-4 key-point bullets per chapter ● Highlights character arcs, thematic evolution, and narrative shifts without minor subplot clutter ● Delivers accurate summaries faithful to the source material in a scannable reference format ● Works for fiction, non-fiction, memoirs, and academic texts across all genres ## Prompt

```
## Role
You are an expert literary analyst creating a structured reference guide for a book.

## Task
Produce a chapter-by-chapter analysis table with three columns: Chapter | Summary | Key Points.

**For each chapter:**
- **Chapter**: List the chapter number
- **Summary**: Write a 2-3 sentence synopsis covering main events, major plot points, and significant character moments
- **Key Points**: Provide 2-4 bullet points highlighting:
  - Important character developments
  - Major themes introduced or expanded
  - Significant narrative shifts or foreshadowing

## Context
Read through {{book-title}} carefully, identifying essential plot points, character arcs, and recurring themes. Focus on core narrative elements; omit minor subplots and excessive detail. The goal is a comprehensive yet concise reference that captures the book's fundamental story and thematic structure.

## Output
Deliver the analysis as a clean markdown table without XML tags or extra formatting. Ensure accuracy to the source material and maintain readability for quick reference.
```

## 用法 / Usage
- 必填變數 / Variables: {{book-title}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Book Analysis Summary Generator is a free AI prompt that produces structured, chapter-by-chapter reference…

# Grant Document Checklist Generator

## 簡介

The Grant Document Checklist Generator is a free AI prompt that creates organized, comprehensive checklists of all required documents and information for grant applications. This grant document checklist prompt for ChatGPT analyzes your grant type, funding focus, and application requirements to produce a structured markdown table listing 8-15 essential documents. Each entry specifies the document's purpose in the application and the 3-5 most critical elements it must contain. The prompt runs on ChatGPT, Claude, Gemini, and Grok, prioritizing standard requirements like needs statements, budgets, timelines, organizational background, and evaluation plans while adding specialized documents relevant to your specific grant context. Grant writers use it to ensure nothing is overlooked when preparing federal, foundation, corporate, or research grant proposals. ● Creates a three-column reference table showing document name, purpose, and key content points for each required item ● Adapts to different grant types including government, foundation, corporate, and research funding applications ● Identifies both standard requirements and specialized documents relevant to your grant's focus area ● Ensures comprehensive preparation by specifying the 3-5 critical elements each document must address ## Prompt

```
## Role
You are an expert grant writer specializing in proposal organization and document preparation.

## Task
Compile a comprehensive checklist of all required documents and information for a grant application. Identify the standard documents needed for the grant type, then organize them into a structured reference table that clarifies each document's purpose and critical content requirements.

## Context
{{grant-details}}

Include:
- Grant type and focus area
- Project description and objectives
- Organization type and profile
- Funding amount requested
- Application deadline

## Output
Deliver your response as a markdown table with three columns:

| Document Name | Purpose | Key Points |
|---------------|---------|------------|

List 8-15 documents appropriate to the grant type. For each document, specify its function in the application and the 3-5 most critical elements it must contain. Prioritize standard requirements (needs statement, budget, timeline, organizational background, evaluation plan) and add specialized documents relevant to the specific grant context.
```

## 用法 / Usage
- 必填變數 / Variables: {{grant-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Grant Document Checklist Generator is a free AI prompt that creates organized, comprehensive checklists of…

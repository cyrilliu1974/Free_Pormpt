# Technical Glossary Curator Prompt for Documentation

## 簡介

The Technical Glossary Curator Prompt for Documentation is a free AI prompt that builds industry-specific glossaries with precise definitions, usage context, and navigation aids for technical writers and documentation teams. This technical glossary prompt for ChatGPT, Claude, Gemini, and Grok produces markdown-formatted tables containing term definitions pitched to your audience's expertise level - basic, intermediate, or advanced - complete with pronunciation guides, usage examples, and cross-references to related entries. Technical writers use it to document software APIs, hardware specifications, medical devices, engineering systems, and compliance frameworks, organizing terms alphabetically or by category to match reader workflows. The prompt ensures terminology reflects current industry standards by drawing from authoritative sources. Reach for this prompt when you need to transform scattered technical vocabulary into navigable reference material, whether onboarding new engineers, supporting customer education, or standardizing internal documentation. ● Tailors definition complexity to basic, intermediate, or advanced audience expertise levels. ● Outputs markdown tables with Term, Definition, Context/Usage, and Related Terms columns. ● Adds pronunciation guides for ambiguous or jargon-heavy terms to reduce miscommunication. ● Cross-references related entries to help readers navigate interconnected concepts. ## Prompt

```
## Role
You are an expert technical writer specializing in curating comprehensive, accurate technical glossaries.

## Task
Create a structured technical glossary with clear, concise definitions tailored to the target audience's expertise level. Research industry-specific terminology from authoritative sources and organize entries to maximize clarity and navigation.

## Context
{{glossary-scope}}

## Requirements
- Organize entries {{organization-method}}
- Pitch definitions at {{detail-level}} level (basic/intermediate/advanced)
- Include relevant context and usage examples where they clarify meaning
- Add cross-references to related terms within the glossary
- Provide pronunciation guides for complex or ambiguous terms
- Ensure terminology reflects current industry standards

## Output
Deliver the glossary as a markdown table with these columns:

| Term | Definition | Context/Usage | Related Terms |
|------|------------|---------------|---------------|
| ... | ... | ... | ... |
```

## 用法 / Usage
- 必填變數 / Variables: {{detail-level}}、{{glossary-scope}}、{{organization-method}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical Glossary Curator Prompt for Documentation is a free AI prompt that builds industry-specific glos…

# Technical Glossary Generator for Complex Topics

## 簡介

The Technical Glossary Generator for Complex Topics is a free AI prompt that builds structured, accessible glossaries for specialized subjects and technical content. This technical glossary prompt for ChatGPT guides the model to produce two-tier glossaries covering both key concepts and advanced terminology, each with related terms, subterms, and example sentences. It applies dependency grammar principles - establishing core ideas first, then layering dependent details - so definitions build logically rather than overwhelming readers. The prompt works on ChatGPT, Claude, and Gemini, and is designed for course creators, technical writers, documentation teams, and educators who need to demystify specialized vocabulary for audiences without prior domain knowledge. ● Outputs 5 terms total: 3 key concepts and 2 advanced terms, each with related vocabulary and context ● Structures every explanation using dependency grammar so foundational concepts anchor more specific details ● Includes example sentences for advanced subterms to demonstrate real-world usage ● Maintains consistent depth and accessibility throughout, written for non-specialist readers ## Prompt

```
## Role

You are an expert technical writer who explains complex topics clearly and structures definitions using dependency grammar principles.

## Task

Create a comprehensive glossary of terms for {{complex-topic}}. Explain jargon and key concepts in accessible language, structuring each explanation so that foundational ideas establish the context for more specific details.

## Requirements

- Write for readers without prior specialized knowledge of the subject
- Use dependency grammar to structure explanations: establish core concepts first, then build dependent details from that foundation
- Include concrete examples and related terms to deepen understanding
- Maintain consistent depth within each section

## Output

Structure the glossary in two sections:

**Key Concepts** (3 terms)  
For each term:
- Provide a clear, accessible explanation using dependency grammar structure
- List 2 related terms with brief definitions

**Advanced Terminology** (2 terms)  
For each term:
- Provide an in-depth explanation using dependency grammar structure  
- List 2 subterms with detailed definitions
- Include one example sentence demonstrating each subterm in context

Format as:

# Glossary of Terms for [Topic Name]

## Key Concepts

1. **[Term]**: [Explanation]
   - *[Related term]*: [Brief definition]
   - *[Related term]*: [Brief definition]

## Advanced Terminology

4. **[Advanced term]**: [In-depth explanation]
   - *[Subterm]*: [Detailed definition]  
     Example: [Sentence]
   - *[Subterm]*: [Detailed definition]  
     Example: [Sentence]
```

## 用法 / Usage
- 必填變數 / Variables: {{complex-topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical Glossary Generator for Complex Topics is a free AI prompt that builds structured, accessible glo…

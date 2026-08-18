# Contract Redline Analysis Prompt

## 簡介

The Contract Redline Analysis Prompt is a free AI prompt that compares original and revised contract versions and produces a complete redline document with standard legal markup for attorneys, paralegals, and legal teams. It performs systematic section-by-section comparisons, marks every deletion with strikethrough and every addition with underline, preserves the original contract structure and numbering, and extracts a summary of material changes affecting rights, obligations, or key terms. This contract redline prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, turning side-by-side contract versions into a single negotiation-ready document that clearly visualizes all edits. Use it when preparing for contract negotiations, conducting due diligence reviews, or needing to present changes to clients or opposing counsel in a professional format that meets legal documentation standards. ● Identifies and marks all deletions, additions, modifications, moved sections, and renumbered clauses with standard legal markup conventions. ● Produces a cover page, summary of material changes, full redline document, and optional explanatory notes in a single structured output. ● Maintains original contract organization, section numbering, and professional formatting throughout the comparison. ● Flags substantive modifications that affect rights, obligations, payment terms, or key definitions for quick negotiation review. ## Prompt

```
## Role
You are a legal document specialist conducting a detailed contract redline comparison using standard legal markup conventions.

## Task
Compare two contract versions and produce a comprehensive redline document that visually displays all changes in a professional, negotiation-ready format.

## Context
You are preparing materials for {{negotiation-context}}. The redline must be accurate, complete, and formatted to professional legal standards to facilitate clear negotiation and prevent confusion.

## Method
1. **Systematic Comparison**: Review both versions section by section, clause by clause, and sentence by sentence
2. **Identify All Changes**: Detect deleted text, added text, modified language, moved sections, and renumbered clauses
3. **Apply Standard Markup**: Use strikethrough (~~deleted text~~) for deletions and underline (<u>added text</u>) for additions
4. **Preserve Structure**: Maintain the original contract organization, numbering, and formatting
5. **Summarize Material Changes**: Extract and list substantive modifications that affect rights, obligations, or key terms
6. **Add Context Where Needed**: Note significant changes that require explanation or attention

## Input
**Original Contract:**
{{original-contract}}

**Revised Contract:**
{{revised-contract}}

**Contract Type:** {{contract-type}}

## Output
Structure your redline document with these sections:

### 1. Cover Page
- Document title and contract type
- Version comparison details (dates, parties, or version identifiers)

### 2. Summary of Material Changes
- Bullet-point list of substantive modifications
- Focus on changes affecting rights, obligations, payments, terms, or key definitions

### 3. Full Redline Document
- Complete contract text with all changes marked
- ~~Strikethrough~~ for deletions
- <u>Underline</u> for additions
- Preserve original section numbering and structure
- Mark every change with no exceptions

### 4. Notes/Comments (if applicable)
- Explanatory notes for complex changes
- Flags for areas requiring special attention

Format the output as a clean, print-ready legal document with professional styling throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{contract-type}}、{{negotiation-context}}、{{original-contract}}、{{revised-contract}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Contract Redline Analysis Prompt is a free AI prompt that compares original and revised contract versions …

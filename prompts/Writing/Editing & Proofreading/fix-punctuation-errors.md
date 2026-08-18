# Punctuation Error Correction Prompt for ChatGPT

## 簡介

The Punctuation Error Correction Prompt for ChatGPT is a free AI prompt that systematically identifies and fixes punctuation mistakes while explaining the grammatical reasoning behind each change. This punctuation correction prompt for ChatGPT asks the model to act as an expert proofreader who applies dependency grammar principles to ensure commas, periods, semicolons, colons, quotation marks, and apostrophes accurately reflect the relationships between words and phrases. It works on any document type, adapts to your target audience and writing style, and outputs side-by-side original and corrected sentences with clear explanations. Use it to polish articles, business documents, academic papers, dialogue-heavy fiction, or any text where punctuation precision matters. ● Identifies misplaced or missing commas, periods, semicolons, colons, quotation marks, and apostrophes across complex sentence structures ● Applies dependency grammar principles to clarify how punctuation marks signal syntactic relationships between sentence elements ● Outputs a three-part format for each correction: original sentence, corrected version, and a brief explanation of significant changes ● Handles specialized punctuation challenges including list formatting, serial comma usage, dialogue attribution, and nested clauses ## Prompt

```
## Role
You are an expert proofreader and editor specializing in punctuation correction and clarity enhancement using dependency grammar principles.

## Task
Correct all punctuation errors in the provided document, ensuring punctuation accurately reflects the grammatical relationships between words and phrases. Focus on:

- Misplaced or missing commas, periods, semicolons, colons, quotation marks, and apostrophes
- Complex sentence structures and their punctuation requirements
- List formatting and serial punctuation
- Dialogue punctuation and attribution
- Dependency grammar relationships between sentence elements

## Context
**Document type:** {{document-type}}
**Target audience:** {{target-audience}}
**Writing style:** {{writing-style}}

Work systematically through the document, examining each sentence for punctuation accuracy and applying dependency grammar principles to clarify syntactic relationships.

## Output
Provide corrections in a clear, annotated format:

**Original:** [sentence with errors]
**Corrected:** [sentence with fixes]
**Explanation:** [brief rationale for major changes]

Repeat this structure for each section requiring correction. Focus explanations on significant changes that improve clarity or correct grammar, helping the writer understand the reasoning behind modifications.
```

## 用法 / Usage
- 必填變數 / Variables: {{document-type}}、{{target-audience}}、{{writing-style}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Punctuation Error Correction Prompt for ChatGPT is a free AI prompt that systematically identifies and fix…

# Legal Document Plain Language Translation Prompt

## 簡介

The Legal Document Plain Language Translation Prompt is a free AI prompt that converts complex legal jargon into accessible everyday language for any audience while preserving the original legal meaning and intent. This legal document simplification prompt for ChatGPT guides AI models (ChatGPT, Claude, Gemini, Grok) to analyze legal text, identify complex terminology and convoluted sentence structures, then produce a clear plain-language version presented in a two-column markdown table for easy side-by-side comparison. The prompt ensures the simplified version maintains all legal implications and accuracy, making it ideal for client communications, employee handbooks, consumer agreements, or any scenario where legal precision must meet readability. It systematically replaces legalese with everyday vocabulary appropriate for your target audience and simplification level. Reach for this prompt when you need to make contracts, terms of service, compliance documents, or legal notices understandable to non-lawyers without sacrificing legal accuracy. ● Analyzes and identifies complex legal terminology, jargon, and compound sentence structures systematically. ● Translates legalese into everyday language calibrated to your specified audience and simplification level. ● Outputs a two-column markdown table showing original legal text alongside its plain-language translation for transparent comparison. ● Verifies that simplified versions preserve all legal implications, meaning, and intent of the original document. ## Prompt

```
## Role
You are an expert legal translator and plain language specialist.

## Task
Translate complex legal text into clear, understandable language while preserving the original meaning and intent. Present the results in a side-by-side comparison format.

## Context
**Target audience:** {{target-audience}}
**Simplification level:** {{simplification-level}}
**Additional context:** {{context}}

## Process
1. Analyze the original legal text to identify complex terms, jargon, and convoluted sentence structures
2. Replace legal terminology with everyday language appropriate for the target audience
3. Break down long, compound sentences into shorter, clearer statements
4. Verify that the plain language version preserves all legal meaning and implications
5. Review for accuracy and consistency between both versions

## Legal Text
{{legal-text}}

## Output
Present your translation as a markdown table with two columns:
- **Left column:** Original legal text (preserve exact wording and structure)
- **Right column:** Plain language translation

Break lengthy passages into logical segments for easier comparison.
```

## 用法 / Usage
- 必填變數 / Variables: {{context}}、{{legal-text}}、{{simplification-level}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Legal Document Plain Language Translation Prompt is a free AI prompt that converts complex legal jargon in…

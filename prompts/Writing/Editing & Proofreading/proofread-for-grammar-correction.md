# Grammar Correction and Proofreading Prompt

## 簡介

The Grammar Correction and Proofreading Prompt is a free AI prompt that applies systematic three-pass editing to any written content for writers, editors, and professionals who need polished text. This grammar correction prompt for ChatGPT walks through your document in structured layers: first identifying and fixing grammatical errors, then restructuring sentences for clarity using dependency grammar principles to ensure proper syntactic relationships, and finally analyzing logical flow to improve coherence and transitions. You provide editing parameters (audience, tone, specific focus areas) and the text to edit, and the AI returns a detailed report with the original text, a list of grammatical corrections applied, explanations of clarity improvements made at the sentence level, and coherence enhancements that strengthen the logical progression of ideas. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need more than a quick spell-check: when preparing business documents, academic writing, marketing copy, or any content where grammatical precision and logical flow matter. ● Corrects grammatical errors with detailed explanations of what was wrong and why ● Restructures sentences using dependency grammar to clarify syntactic relationships and improve readability ● Analyzes logical flow and adds transitions to strengthen coherence across paragraphs ● Preserves the original text for easy side-by-side comparison of changes ## Prompt

```
## Role
You are an expert proofreader and editor specializing in dependency grammar analysis.

## Task
Refine the provided text through three passes:
1. Identify and correct grammatical errors
2. Restructure sentences for clarity, ensuring proper syntactic relationships between words and phrases
3. Analyze and improve the logical flow of ideas for coherence

## Context
{{editing-parameters}}

{{text-to-edit}}

## Output
Provide your revisions in four sections:

### Original Text
[Quote the full original]

### Grammatical Corrections
[List errors found and corrections applied]

### Clarity Improvements
[Explain sentence restructuring and syntactic changes]

### Coherence Enhancements
[Describe logical flow improvements and transitions added]
```

## 用法 / Usage
- 必填變數 / Variables: {{editing-parameters}}、{{text-to-edit}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Grammar Correction and Proofreading Prompt is a free AI prompt that applies systematic three-pass editing …

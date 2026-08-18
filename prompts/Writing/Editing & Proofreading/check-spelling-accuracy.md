# Spelling Accuracy Checker for Documents

## 簡介

The Spelling Accuracy Checker for Documents is a free AI prompt that identifies and corrects spelling errors in professional documents across any industry or field. This spelling accuracy prompt for ChatGPT works by analyzing each word in context, examining grammatical role, potential homonyms, commonly misspelled words, technical terminology, and proper nouns. You provide document details (type, industry, target audience, and style guide preferences like AP, Chicago, or APA) along with the text to proofread, and the prompt returns a clean markdown table showing the location of each error, the misspelled word, and the suggested correction. Use cases include academic papers, business reports, marketing copy, technical documentation, and any professional writing where spelling precision matters. The prompt runs on ChatGPT, Claude, and Gemini. This prompt is ideal for writers, editors, content managers, students, and business professionals who need context-aware spelling review that respects industry conventions and style guides. ● Analyzes spelling in context, catching homonym errors (their/there/they're) and technical terms that basic spell-checkers miss ● Respects style guide preferences (AP, Chicago, APA) and industry-specific terminology for accurate corrections ● Returns findings in a structured markdown table with location, error, and correction for easy review ● Handles proper nouns, technical jargon, and field-specific vocabulary across industries ## Prompt

```
## Role
You are an expert proofreader specializing in spelling accuracy.

## Task
Meticulously examine the provided text and identify all spelling errors. Analyze each word in context, considering its grammatical role, potential homonyms, commonly misspelled words, technical terminology, and proper nouns.

## Context
{{document-details}}

Provide details about the document type, industry/field, target audience, and any style guide preferences (e.g., AP, Chicago, APA) that should inform spelling conventions.

## Output
Deliver your findings as a markdown table with three columns:

| Location | Spelling Error | Suggested Correction |
|----------|----------------|---------------------|
| [section/paragraph/line] | [incorrect word] | [correct spelling] |

If no spelling errors are found, state: "No spelling errors detected."

---

**Text to proofread:**

{{text}}
```

## 用法 / Usage
- 必填變數 / Variables: {{document-details}}、{{text}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Expertise · Differentiated_Claim_Drafting_Engine
- 適用 / Use when: The Spelling Accuracy Checker for Documents is a free AI prompt that identifies and corrects spelling errors i…

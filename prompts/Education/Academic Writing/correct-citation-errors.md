# Citation Error Correction Prompt for Academic Writing

## 簡介

The Citation Error Correction Prompt for Academic Writing is a free AI prompt that identifies and fixes citation formatting errors, missing elements, and style inconsistencies for researchers, students, and academic writers. This citation error correction prompt for ChatGPT works by analyzing each reference against the specified style guide - whether APA, MLA, Chicago, Harvard, or others - and flags formatting mistakes, incorrect punctuation, missing DOIs or author names, element sequencing problems, and inconsistencies across multiple citations. It preserves all original information while correcting the structure, and highlights any suspicious details or gaps that cannot be inferred. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and outputs a side-by-side comparison showing the original citation, the corrected version with changes marked in bold, and a detailed explanation of each rule applied. Use it when preparing manuscripts for journal submission, cleaning up dissertation bibliographies, or ensuring consistency across collaborative research documents. ● Detects missing elements such as author names, publication dates, titles, publishers, page numbers, and DOIs in each reference. ● Corrects punctuation, capitalization, italics, spacing, and element ordering to match APA, MLA, Chicago, and other citation styles. ● Ensures consistency across multiple citations so all references follow the same formatting rules. ● Flags suspicious or incomplete information that requires manual verification or additional research. ## Prompt

```
## Role
You are a citation accuracy specialist who corrects errors, inconsistencies, and formatting issues in academic references across all major citation styles.

## Task
Analyze and correct the provided citations according to the specified style guide. Identify errors in missing elements, formatting, ordering, and consistency. Preserve all original information while fixing format issues.

## Context
**Citation style:** {{citation-style}}
**Citations to correct:** {{citations}}
**Field and document type:** {{academic-context}}

## Process
1. Confirm the citation style (APA, MLA, Chicago, etc.) or identify it from the examples
2. Analyze each citation for:
   - Missing elements (author, date, title, publisher, DOI, etc.)
   - Formatting errors (punctuation, capitalization, italics, spacing)
   - Incorrect element sequence
   - Inconsistencies across multiple citations
3. Flag any information that appears incorrect or suspicious beyond formatting
4. Highlight missing information that cannot be inferred from context

## Output
For each citation, provide:

**Original Citation:**  
[Original text]

**Corrected Citation:**  
[Corrected version with **changes in bold**]

**Changes Made:**  
- [Specific correction 1 with rule applied]  
- [Specific correction 2 with rule applied]  
- [Flag any missing or suspicious information]

If multiple citations are provided, include a summary table at the end listing all corrections made.
```

## 用法 / Usage
- 必填變數 / Variables: {{academic-context}}、{{citation-style}}、{{citations}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Citation Error Correction Prompt for Academic Writing is a free AI prompt that identifies and fixes citati…

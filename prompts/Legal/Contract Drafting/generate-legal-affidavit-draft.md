# Legal Affidavit Draft Generator for ChatGPT

## 簡介

The Legal Affidavit Draft Generator is a free AI prompt that produces structured, jurisdictionally compliant affidavit documents for legal professionals, paralegals, and individuals preparing sworn statements. This affidavit prompt for ChatGPT walks through every formal element required in a legally sound affidavit: it opens with a solemn affirmation, organizes facts into numbered paragraphs, details the affiant's personal knowledge and involvement, references supporting evidence, and closes with a complete jurat block ready for notarization. The prompt runs on ChatGPT, Claude, and Gemini, accepting the statement or event at issue and affiant details as inputs, then returns a draft document that meets the structural and terminological standards expected in legal proceedings. Law firms use it to accelerate affidavit preparation for motions, estate matters, and evidentiary filings; individuals use it to draft affidavits for immigration, family court, or sworn declarations without starting from scratch. ● Produces a complete affidavit structure including introduction, numbered body paragraphs, affirmation clause, and jurat signature block ● Incorporates appropriate legal terminology and sworn-statement language that meets jurisdictional standards ● Guides the affiant to organize facts, personal knowledge, and supporting evidence in a clear, sequential format ● Returns a document ready for legal review, signature, and notarization without manual reformatting ## Prompt

```
## Role
You are a legal document specialist drafting a formal affidavit that meets jurisdictional standards.

## Task
Draft a comprehensive affidavit based on the statement or event and affiant information provided. Structure the document with numbered paragraphs covering facts, the affiant's knowledge and involvement, supporting evidence, and additional relevant information. Conclude with a solemn affirmation and proper sworn statement formatting.

## Context
An affidavit is a written statement of facts made under oath. Use appropriate legal terminology throughout. Include only verified information directly relevant to the matter at hand.

## Input
**Statement or event:**
{{statement-or-event}}

**Affiant details:**
{{affiant-details}}

## Output
Structure the affidavit as follows:

**Introduction:** "I, [name], [occupation], of [address], solemnly affirm and declare as follows:"

**Body (numbered paragraphs):**
1. Statement of facts
2. Affiant's knowledge and involvement in the matter
3. Supporting evidence
4. Additional relevant information

**Affirmation:** "I make this affidavit in support of [purpose]. I solemnly affirm that the contents of this affidavit are true and correct to the best of my knowledge, information, and belief."

**Jurat:**
```
SWORN before me at [location] this [date].

[affiant signature]
[affiant name]

[notary public signature]
[notary public name]
Notary Public in and for [jurisdiction]
My Commission Expires: [expiration date]
```

Provide the complete affidavit ready for review and execution.
```

## 用法 / Usage
- 必填變數 / Variables: {{affiant-details}}、{{statement-or-event}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Legal Affidavit Draft Generator is a free AI prompt that produces structured, jurisdictionally compliant a…

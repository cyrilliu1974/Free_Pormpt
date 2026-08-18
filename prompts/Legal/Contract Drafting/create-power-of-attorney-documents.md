# Power of Attorney Document Generator

## 簡介

The Power of Attorney Document Generator is a free AI prompt that drafts legally structured power of attorney documents for individuals and legal professionals needing formal delegation-of-authority paperwork. This power of attorney prompt for ChatGPT produces complete documents that identify the principal and attorney-in-fact, enumerate specific granted powers, establish duration and commencement dates, detail any limitations or restrictions, and include execution signature blocks plus notary acknowledgment sections formatted for legal enforceability. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and walks the model through each required element - party identification, jurisdiction, powers scope, duration terms, and notarization details - so the output follows formal legal structure and terminology appropriate to the governing state law. Use it when you need a starting draft for general, financial, healthcare, or limited powers of attorney that you can review with counsel and customize for specific circumstances. ● Identifies principal and attorney-in-fact with full legal names and governing jurisdiction. ● Enumerates each granted power in clear, specific terms and lists any restrictions or limitations. ● Establishes commencement and end dates, or until-revoked language, plus early-revocation conditions. ● Includes formal signature block and notary acknowledgment section with state, county, and commission fields. ## Prompt

```
## Role

You are an expert legal consultant specializing in drafting precise and comprehensive power of attorney documents. Provide clear, legally sound guidance using appropriate legal terminology and structure for maximum clarity and enforceability.

## Task

Draft a legally sound power of attorney document that clearly identifies the parties, specifies granted powers, establishes duration and limitations, and includes proper execution and notarization sections.

## Context

{{party-and-jurisdiction-details}}

Include: principal's full legal name, attorney-in-fact's full legal name, and governing law state.

{{powers-and-scope}}

Include: specific powers granted to the attorney-in-fact and any limitations or restrictions on those powers.

{{duration-and-dates}}

Include: commencement date, end date (or "until revoked" if indefinite), and any conditions for earlier revocation.

{{notarization-details}}

Include: execution date, notary state, notary county, notary date, notary name, and notary commission details.

## Output

Structure the document as follows:

**POWER OF ATTORNEY**

**Introduction**: State the principal and appointed attorney-in-fact, specify governing law jurisdiction.

**POWERS GRANTED**: List each power and authority granted in clear, specific terms.

**Duration**: Specify commencement and end dates; mention conditions for earlier revocation.

**LIMITATIONS**: State any restrictions on the powers granted.

**IN WITNESS WHEREOF**: Include signature line, principal's name, and execution date.

**NOTARY ACKNOWLEDGEMENT**: Include state, county, appearance date, notary statement certifying principal's identity and voluntary execution under penalty of perjury, with space for notary signature, name, and commission details.

Use formal legal language throughout. Ensure all required elements for enforceability in the specified jurisdiction are present.
```

## 用法 / Usage
- 必填變數 / Variables: {{duration-and-dates}}、{{notarization-details}}、{{party-and-jurisdiction-details}}、{{powers-and-scope}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Power of Attorney Document Generator is a free AI prompt that drafts legally structured power of attorney …

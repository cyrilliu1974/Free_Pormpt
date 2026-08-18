# Legal Research Memo Generator for ChatGPT

## 簡介

The Legal Research Memo Generator is a free AI prompt that produces formal legal research memos identifying applicable laws, case precedents, and analytical conclusions for attorneys, paralegals, and legal researchers. This legal research memo prompt for ChatGPT guides the AI through a structured professional format: executive summary, relevant statutes and regulations, case precedent analysis with holdings and reasoning, application of authorities to the issue at hand, and research-supported conclusions. It runs on ChatGPT, Claude, and Gemini, requiring only the legal issue or question as input. Legal professionals use it to quickly draft preliminary research memos, explore unfamiliar areas of law, or structure complex multi-jurisdictional research into client-ready documentation. Reach for this prompt when you need to transform a legal question into a properly formatted research memo grounded in identified authorities rather than speculation. ● Produces memos with six formal sections: header, executive summary, relevant laws, case precedents, analysis, and conclusion ● Ensures all statements reference identified statutes, regulations, or court decisions by name and citation ● Explains how authorities connect to the legal issue, distinguishing binding precedent from persuasive authority ● Uses precise legal terminology appropriate for client advisories, internal research files, and court filings ## Prompt

```
## Role
You are an expert legal researcher and analyst producing a comprehensive legal research memo.

## Task
Research the legal topic or question provided, then deliver a professional legal research memo that identifies and summarizes all relevant laws, case precedents, and legal principles. Analyze how the authorities relate to the issue and provide a clear conclusion based on your findings.

## Context
Legal topic or question to research:
{{legal-issue}}

## Output
Format your response as a formal legal research memo with these sections:

**MEMO HEADER**
- To: [Recipient]
- From: [Your Name], Legal Researcher
- Date: [Current Date]
- Re: Legal Research Memo – [Topic]

**EXECUTIVE SUMMARY**
Summarize the key findings in 2–3 paragraphs.

**RELEVANT LAWS**
Identify and summarize all applicable statutes, regulations, and legal principles.

**RELEVANT CASE PRECEDENTS**
Summarize important court decisions that bear on the issue, including jurisdiction, holding, and reasoning.

**ANALYSIS**
Explain how the laws and precedents apply to the legal issue. Show connections, distinctions, and the weight of authority.

**CONCLUSION**
Provide a clear, research-supported answer to the legal question.

---

**Requirements:**
- Ground all statements in identified legal sources; avoid unsupported speculation.
- Use precise legal terminology appropriate for professional legal documents.
- Cite authorities by name (case name, statute number, or regulation citation) in each section.
```

## 用法 / Usage
- 必填變數 / Variables: {{legal-issue}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Legal Research Memo Generator is a free AI prompt that produces formal legal research memos identifying ap…

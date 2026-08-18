# Discovery Deficiency Chart Generator for Litigation

## 簡介

The Discovery Deficiency Chart Generator for Litigation is a free AI prompt that creates comprehensive documentation of deficiencies in opposing counsel's discovery responses for commercial litigation attorneys. This discovery deficiency chart prompt for ChatGPT analyzes case details and produces a structured markdown table identifying improper objections, incomplete answers, missing documents, inadequate privilege logs, and failures to supplement under Federal Rules of Civil Procedure. The output includes case citations, prioritization by evidentiary value and urgency, and court-appropriate language suitable for meet-and-confer letters or motions to compel. It runs on ChatGPT, Claude, Gemini, and Grok, accepting case-details as input and returning a professional litigation document with case caption header, deficiency summary by category, sequential numbering, and specific relief sought for each item. Litigation attorneys preparing for discovery disputes, motion practice, or meet-and-confer conferences will find this prompt useful for organizing and documenting discovery failures systematically. ● Documents all deficiency types including boilerplate objections, evasive answers, document production failures, and inadequate privilege logs under FRCP 26(b)(5) ● Cites applicable Federal Rules of Civil Procedure (26(b)(1), 26(e), 33, 34, 37) and relevant case law standards for the jurisdiction ● Prioritizes deficiencies by likelihood of yielding case-dispositive evidence, patterns of evasion, and deadline urgency ● Formats output as a structured table with columns for request number, original request, response received, specific deficiency, legal basis, relief sought, and meet-and-confer notes ## Prompt

```
## Role
You are an experienced commercial litigation attorney specializing in e-discovery and motion practice under the Federal Rules of Civil Procedure.

## Task
Create a comprehensive Discovery Deficiency Chart that documents every inadequacy in opposing counsel's discovery responses. The chart will serve as the foundation for meet-and-confer discussions and potential motions to compel.

## Context
{{case-details}}

The chart must accomplish three objectives: create a complete record of deficiencies, support targeted meet-and-confer efforts, and provide the court with specific grounds for relief if motion practice becomes necessary.

## Analysis Requirements
Identify and categorize all deficiency types:
- Improper or boilerplate objections lacking specificity
- Incomplete or evasive answers
- Failure to produce responsive documents
- Inadequate privilege logs (missing required elements under FRCP 26(b)(5))
- Failure to supplement responses per FRCP 26(e)

Cite applicable authority including FRCP 26(b)(1), 26(e), 33, 34, and 37, plus relevant case law standards for the jurisdiction.

Prioritize deficiencies by:
- Likelihood of yielding case-dispositive evidence
- Patterns suggesting systematic evasion
- Urgency (deadlines, upcoming depositions)
- Whether informal resolution or motion practice is appropriate

## Output
Deliver a structured markdown table with these columns:

| Request No. | Original Request | Response Received | Specific Deficiency | Legal Basis (FRCP/Case Law) | Relief Sought | Meet & Confer Notes |

**Required components:**
- Professional header with case caption and "Discovery Deficiency Chart" title
- Summary section showing total deficiencies by category and priority tier
- Sequential numbering for each deficiency
- Precise, court-appropriate language that is specific but not inflammatory
- Footer with preparer information and date prepared

Format the entire output as a litigation document suitable for court exhibit or attachment to a motion to compel.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Discovery Deficiency Chart Generator for Litigation is a free AI prompt that creates comprehensive documen…

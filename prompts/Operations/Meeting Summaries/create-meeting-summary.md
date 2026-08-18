# Meeting Summary Generator Prompt for ChatGPT

## 簡介

The Meeting Summary Generator Prompt for ChatGPT is a free AI prompt that transforms raw meeting notes into actionable, one-page summaries for teams and professionals. This meeting summary prompt for ChatGPT works by extracting key discussion points, documenting decisions with their rationale, listing action items with owners and deadlines, and flagging unresolved issues that need follow-up. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured outputs that include a meeting overview, discussion highlights, concrete decisions, assigned tasks, and a brief recap of next steps. Teams use it to keep remote members informed, create records for compliance or planning, and ensure everyone understands outcomes without reading lengthy transcripts. Reach for this prompt when you need to turn informal discussion notes into professional summaries that drive accountability and continuity across projects. ● Structures summaries into six labeled sections: overview, discussion points, decisions, action items, unresolved issues, and a closing recap ● Focuses on outcomes and accountability by assigning owners and deadlines to every task ● Keeps summaries to one page or less, making them scannable for busy team members ● Adapts to any meeting type, from sprint planning and board sessions to client calls and strategy reviews ## Prompt

```
## Role
You are an expert meeting summarizer who distills discussion notes into actionable summaries.

## Task
Create a concise, structured summary of the meeting notes provided. The summary must enable someone who did not attend to understand the discussion, outcomes, and next steps at a glance.

## Context
Your audience needs clarity on what was decided and what requires action. Focus on outcomes over process. Keep the summary to one page or less.

## Output
Structure your summary as follows:

**Meeting Overview**
Briefly state the meeting's purpose and objectives.

**Key Discussion Points**
Summarize each main topic, highlighting important arguments, insights, or data presented.

**Decisions Made**
For each topic, state the decision reached and the rationale or key factors behind it.

**Action Items**
List specific tasks agreed upon, with assigned owners and deadlines or timeframes for completion.

**Unresolved Issues**
Note any topics requiring further discussion or follow-up.

**Summary**
Conclude with a brief recap of overall outcomes and emphasize the immediate next steps.

---

{{meeting-notes}}
```

## 用法 / Usage
- 必填變數 / Variables: {{meeting-notes}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Meeting Summary Generator Prompt for ChatGPT is a free AI prompt that transforms raw meeting notes into ac…

# Meeting Notes Generator From Transcript

## 簡介

The Meeting Notes Generator From Transcript is a free AI prompt that converts raw meeting transcripts into clear, scannable notes with decisions, action items, and follow-ups for teams and project managers. This meeting notes prompt for ChatGPT processes full transcripts and organizes them into structured sections: a summary of objectives and outcomes, key discussion points with relevant details, documented decisions with owners and deadlines, action items with assignees and due dates, and unresolved issues flagged for follow-up. It runs on ChatGPT, Claude, Gemini, and Grok, turning lengthy meeting recordings or live transcriptions into reference documents that keep teams aligned. Use it after customer calls, sprint planning sessions, stakeholder reviews, or any discussion where accountability and clarity matter. ● Extracts main objectives, outcomes, and key discussion points with supporting details ● Documents every decision with assigned owners and deadlines for accountability ● Lists action items with clear assignees and due dates in a scannable format ● Flags unresolved issues and assigns follow-up responsibility to prevent dropped threads ## Prompt

```
## Role
You are an expert in business communication and meeting management specializing in transforming meeting transcripts into clear, actionable notes.

## Task
Distill the provided meeting transcript into structured meeting notes that capture key discussions, decisions, action items, and unresolved issues. The notes must be easy to scan and serve as a reliable reference for participants and stakeholders.

## Input
{{meeting-transcript}}

## Process
1. Read the full transcript to understand context and flow
2. Extract the meeting's main objectives and outcomes
3. Identify key discussion points with relevant details (opinions, data, examples)
4. Document decisions with assigned owners and deadlines
5. List action items with assignees and due dates
6. Flag unresolved issues requiring follow-up and who will address them
7. Note any contextual observations that aid understanding
8. Include next meeting date/time if mentioned

## Output
Structure the meeting notes with these sections:

**Summary**
Brief overview of objectives and outcomes

**Key Discussion Points**
- Concise descriptions of main topics discussed
- Relevant details, data, or perspectives shared

**Decisions Made**
- Each decision with assigned owner and deadline/timeline

**Action Items**
- Task description
- Assigned to: [person/team]
- Due date: [if applicable]

**Unresolved Issues**
- Questions or topics requiring further discussion
- Assigned owner for follow-up

**Additional Notes** (optional)
Context or observations that don't fit other categories

**Next Steps**
Date and time of next meeting or follow-up

Use bullet points and clear formatting for easy scanning.
```

## 用法 / Usage
- 必填變數 / Variables: {{meeting-transcript}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Meeting Notes Generator From Transcript is a free AI prompt that converts raw meeting transcripts into cle…

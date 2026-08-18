# Meeting Minutes Template for ChatGPT

## 簡介

The Meeting Minutes Template for ChatGPT is a free AI prompt that transforms raw meeting notes into professional, structured documentation for teams and organizations. This meeting minutes prompt for ChatGPT takes your meeting notes and automatically organizes them into a clear five-column markdown table covering attendees, agenda items, discussion points, decisions made, and action items with assigned owners and deadlines. It runs on ChatGPT, Claude, Gemini, and Grok, handling meetings of any length or complexity. Teams use it to create consistent records after standups, sprint planning sessions, client calls, board meetings, and cross-functional reviews, ensuring accountability and follow-through. The prompt is built for project managers, executive assistants, team leads, and anyone responsible for documenting meetings who needs a fast, reliable way to capture what was discussed and what happens next. ● Outputs a five-column markdown table that separates attendees, agenda, discussion, decisions, and actions for easy scanning and reference ● Automatically extracts action items and pairs them with responsible owners and due dates to track accountability ● Captures the rationale behind decisions so teams understand the context weeks or months later ● Works with messy, informal meeting notes and produces consistent, polished documentation every time ## Prompt

```
## Role
You are an expert meeting facilitator creating comprehensive meeting minutes.

## Task
Produce a structured record of the meeting that captures attendees, agenda items, key discussion points, decisions made, and action items with assigned owners and deadlines.

## Context
**Meeting:** {{meeting-name}}
**Date:** {{meeting-date}}
**Duration:** {{meeting-duration}}
**Attendees:** {{attendee-list}}

## Input
{{meeting-notes}}

## Output
Deliver the minutes as a markdown table with 5 columns:

| Attendees | Agenda Items | Discussion Points | Decisions | Action Items |
|-----------|--------------|-------------------|-----------|-------------|

**Format requirements:**
- Each row corresponds to one agenda item
- Use bullet points within cells for multiple entries
- Action items must specify owner and deadline
- Discussion Points should capture the essence of conversations and rationale behind decisions
- Ensure accuracy and completeness across all sections
```

## 用法 / Usage
- 必填變數 / Variables: {{attendee-list}}、{{meeting-date}}、{{meeting-duration}}、{{meeting-name}}、{{meeting-notes}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Meeting Minutes Template for ChatGPT is a free AI prompt that transforms raw meeting notes into profession…

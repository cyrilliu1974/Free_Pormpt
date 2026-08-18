# Meeting Summary Email Generator

## 簡介

The Meeting Summary Email Generator is a free AI prompt that transforms meeting notes into structured, professional emails for attendees and stakeholders. This meeting summary email prompt for ChatGPT guides the AI to synthesize discussions, decisions, and action items into a scannable format that serves as an official record. It runs on ChatGPT, Claude, Gemini, and Grok, producing emails with clear subject lines, meeting overviews, decision logs, and deadline-tracked action items. Use it after team meetings, client calls, or project reviews to ensure everyone - including those who couldn't attend - stays aligned on what was discussed and what happens next. Reach for this prompt when you need to turn raw meeting notes into a formal communication that doubles as documentation. ● Breaks down discussions into bullet points and numbered lists for quick scanning ● Assigns action items to specific owners with deadlines to drive accountability ● Documents decisions alongside the topics that prompted them for traceability ● Maintains a professional yet approachable tone suitable for cross-functional teams ## Prompt

```
## Role
You are a corporate communications specialist drafting a post-meeting summary email.

## Task
Synthesize meeting notes into a structured, professional email that summarizes the meeting for attendees and stakeholders who need to stay informed. The email serves as an official record of what was discussed, decided, and assigned.

## Context
Meeting: {{meeting-topic}}
Date: {{meeting-date}}
Participants: {{participants}}

## Output
Structure the email with these components:

**Subject Line:** "Summary of {{meeting-topic}} Meeting – {{meeting-date}}"

**Opening:** Brief greeting and one-sentence purpose statement.

**Meeting Overview:** State the meeting's objective and list key participants (note significant absences if relevant).

**Main Discussions:** Break down core topics using bullet points or numbered lists for clarity.

**Decisions Reached:** Clearly enumerate decisions made, linking each to its originating discussion.

**Action Items:** List tasks with assigned owners and deadlines in this format:
{{action-items}}

**Follow-Up:** Note any materials to be circulated (slides, documents) and scheduled check-in dates:
{{follow-up-details}}

**Closing:** Invite questions or comments, thank participants for their contributions, and sign off with your name and title.

Maintain a professional yet approachable tone. Use formatting (bullets, bold headers, white space) to ensure easy scanning and navigation.
```

## 用法 / Usage
- 必填變數 / Variables: {{action-items}}、{{follow-up-details}}、{{meeting-date}}、{{meeting-topic}}、{{participants}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Meeting Summary Email Generator is a free AI prompt that transforms meeting notes into structured, profess…

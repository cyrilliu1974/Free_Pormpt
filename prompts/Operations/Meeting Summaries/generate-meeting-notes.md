# Meeting Notes to Action Items Prompt

## 簡介

The Meeting Notes to Action Items Prompt is a free AI prompt that converts unstructured meeting transcripts into organized follow-up documentation for project managers, team leads, and meeting facilitators. This meeting notes prompt for ChatGPT, Claude, Gemini, and Grok analyzes your raw meeting content and extracts actionable tasks with assigned owners, deadlines, and context. It produces a structured document containing a discussion summary, a list of decisions made with their implications, and a prioritized action-item roster organized by urgency. Real-world use cases include sprint retrospectives, client calls, executive briefings, and cross-functional planning sessions where accountability and follow-through matter. Reach for this prompt whenever you need to distribute clear post-meeting documentation quickly, ensure nothing falls through the cracks, or turn long transcripts into trackable deliverables. ● Extracts task assignments, responsible parties, and completion dates from unstructured notes ● Summarizes discussion topics and decisions to provide context for stakeholders ● Prioritizes action items by deadline and criticality for immediate follow-up ● Verifies each item is actionable, specifically assigned, and time-bound before output ## Prompt

```
## Role
You are an expert project manager and meeting facilitator specializing in actionable follow-up documentation.

## Task
Analyze the provided meeting notes and extract a structured list of action items with clear ownership and deadlines. Summarize key discussion points and decisions to provide context for the action items.

## Process
1. Read the meeting notes in full to understand discussion topics, decisions, and task assignments
2. Summarize the main discussion points briefly to establish context
3. Document each decision made and its relevance to project objectives
4. Extract and list all assigned tasks with:
   - Clear, specific task description
   - Responsible individual or team name
   - Completion deadline
   - Any critical details or considerations
5. Organize action items by priority (earliest deadlines or highest criticality first)
6. Verify each item is actionable: clearly defined, specifically assigned, and time-bound

## Input
{{meeting-notes}}

## Output
Provide a structured document containing:

**Discussion Summary**: Brief overview of main topics and context

**Decisions Made**: List of key decisions and their implications

**Action Items**: Organized list where each item includes:
- Task description
- Assigned to: [name/team]
- Deadline: [date]
- Notes: [relevant details]

Format for clarity and immediate distribution to stakeholders.
```

## 用法 / Usage
- 必填變數 / Variables: {{meeting-notes}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Meeting Notes to Action Items Prompt is a free AI prompt that converts unstructured meeting transcripts in…

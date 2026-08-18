# Analyze Meeting Notes

## 簡介

The Analyze Meeting Notes is a free AI prompt that extracts actionable outcomes from meeting transcripts for executives, project managers, and teams who need clarity on what was decided and who owns next steps. This meeting notes prompt for ChatGPT processes raw transcripts and separates concrete decisions from discussion noise, surfaces action items with clear ownership and deadlines, and flags unresolved questions that require follow-up. It runs on ChatGPT, Claude, Gemini, and Grok, turning dense conversation logs into three-section summaries that eliminate ambiguity and ensure accountability. Use it after stakeholder meetings, sprint reviews, or strategic planning sessions where commitments must be tracked and follow-through is critical. Reach for this prompt when you inherit a verbose transcript and need to answer: what was finalized, who is responsible for what, and what still needs resolution. ● Distinguishes concrete decisions from topics that were merely discussed to prevent confusion about what was actually agreed upon. ● Identifies specific action items with named owners and deadlines to drive accountability and forward momentum. ● Surfaces open questions requiring resolution so nothing critical falls through the cracks. ● Formats output into three clean sections that stakeholders can scan in seconds. ## Prompt

```
## Role
You are an expert at extracting actionable outcomes from meeting transcripts. Your focus is distinguishing decisions from discussion, ensuring clear ownership, and surfacing unresolved issues that require follow-up.

## Context
Stakeholders need immediate clarity on what was decided, who owns what, and what remains unresolved. Raw transcripts bury critical insights in dense discussion. Your job is to cut through the noise and extract only what matters for forward momentum.

## Task
Analyze the meeting transcript and extract information into exactly three sections:

- **Key Decisions**: Actual commitments or resolutions that were agreed upon (not topics discussed)
- **Next Steps**: Specific action items with clearly identified owners and deadlines
- **Open Questions**: Unresolved issues requiring future attention or decision-making

Focus on concrete outcomes, not discussion topics. Avoid general conversation points, background information, or mentions that aren't actionable. Use precise language that eliminates ambiguity. Each section should contain only critical items requiring follow-up or tracking.

{{meeting-transcript}}

{{meeting-context}}

## Output
Format your response using these three sections:

### Key Decisions
[Concrete decisions and commitments finalized during the meeting]

### Next Steps
[Specific action items with owners and deadlines]

### Open Questions
[Unresolved issues requiring future discussion or decision-making]
```

## 用法 / Usage
- 必填變數 / Variables: {{meeting-context}}、{{meeting-transcript}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Analyze Meeting Notes is a free AI prompt that extracts actionable outcomes from meeting transcripts for e…

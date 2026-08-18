# Sprint Retrospective Summary Prompt

## 簡介

The Sprint Retrospective Summary Prompt is a free AI prompt that synthesizes agile retrospective discussions into actionable, well-organized summaries for project managers and scrum masters. This sprint retrospective prompt for ChatGPT analyzes team feedback and conversation notes to produce a structured summary with four clear sections: what went well, what needs improvement, prioritized action items ranked by impact and feasibility, and recommendations for the next sprint. It runs on ChatGPT, Claude, Gemini, and Grok, identifying recurring patterns, notable successes, persistent blockers, and team morale signals from raw retrospective input. Use it after every sprint ceremony to turn open-ended team discussions into a balanced, constructive record that drives continuous improvement. ● Categorizes feedback into standardized sections so every retrospective follows a consistent, scannable format. ● Ranks action items by impact and feasibility, helping teams focus on changes that matter most. ● Surfaces team dynamics and morale signals that might otherwise be lost in unstructured notes. ● Produces objective, constructive summaries that support transparency and psychological safety. ## Prompt

```
## Role
You are an expert project manager specializing in synthesizing Sprint Retrospective insights into actionable summaries.

## Task
Distill Sprint Retrospective notes into a concise, balanced summary that captures key themes, prioritizes next steps, and surfaces team dynamics.

## Context
{{sprint-context}}

Review the retrospective notes and discussions to identify:
- Main themes and recurring patterns
- Notable successes and persistent blockers
- Team morale and collaboration dynamics
- High-impact, feasible improvements

## Output
Provide a structured summary with these sections:

### What Went Well
- Bullet points highlighting successes and positive patterns

### What Needs Improvement
- Bullet points identifying challenges and areas for growth

### Action Items
- Prioritized list ranked by impact and feasibility
- Each item should be specific and assignable

### Recommendations for Next Sprint
- Clear, actionable guidance addressing team dynamics and process improvements

Maintain an objective, constructive tone throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{sprint-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sprint Retrospective Summary Prompt is a free AI prompt that synthesizes agile retrospective discussions i…
